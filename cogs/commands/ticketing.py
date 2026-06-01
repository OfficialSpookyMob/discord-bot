import discord
from discord.ext import commands
from config import COLOR_PRIMARY, COLOR_SUCCESS, OWNER_ID, TICKET_CATEGORIES
import json
import os

class TicketingSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ticket_file = "tickets.json"
        self.load_tickets()

    def load_tickets(self):
        if os.path.exists(self.ticket_file):
            with open(self.ticket_file) as f:
                self.tickets = json.load(f)
        else:
            self.tickets = {}

    def save_tickets(self):
        with open(self.ticket_file, "w") as f:
            json.dump(self.tickets, f, indent=4)

    def is_owner(ctx):
        return ctx.author.id == OWNER_ID

    @commands.command(name="ticketsetup")
    @commands.check(is_owner)
    async def ticketsetup(self, ctx):
        """Setup ticket system in current channel"""
        
        embed = discord.Embed(
            title="Help & Support Center",
            description="Welcome to the support system! If you need assistance, wish to report a bug, or want to appeal a moderation action, you are in the right place.",
            color=COLOR_PRIMARY
        )
        
        embed.add_field(
            name="How to use:",
            value="• Choose the category that best fits your issue from the menu below.\n"
                  "• A private ticket channel will be opened for you.\n"
                  "• Provide all relevant details, and our staff will assist you.",
            inline=False
        )
        
        embed.add_field(
            name="📌 Note:",
            value="⚠️ Abuse of the ticket system may result in restrictions.",
            inline=False
        )
        
        # Create dropdown menu
        view = TicketDropdown()
        msg = await ctx.send(embed=embed, view=view)
        
        embed_success = discord.Embed(
            title="✅ Ticket System Setup",
            description=f"Ticket system initialized in {ctx.channel.mention}",
            color=COLOR_SUCCESS
        )
        
        await ctx.send(embed=embed_success)

    @commands.command(name="closeticket")
    async def closeticket(self, ctx):
        """Close current ticket"""
        channel_name = ctx.channel.name
        
        if not channel_name.startswith("ticket-"):
            embed = discord.Embed(
                title="❌ Error",
                description="This command can only be used in a ticket channel",
                color=0xED4245
            )
            await ctx.send(embed=embed)
            return
        
        embed = discord.Embed(
            title="🔒 Ticket Closed",
            description="This ticket will be deleted in 5 seconds...",
            color=COLOR_SUCCESS
        )
        
        await ctx.send(embed=embed)
        
        # Delete channel after 5 seconds
        import asyncio
        await asyncio.sleep(5)
        await ctx.channel.delete(reason="Ticket closed")

class TicketDropdown(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.select(
        placeholder="Select a ticket category...",
        min_values=1,
        max_values=1,
        options=[
            discord.SelectOption(label="🐛 Bug Report", value="bug_report"),
            discord.SelectOption(label="✨ Feature Request", value="feature_request"),
            discord.SelectOption(label="📞 Appeal Moderation", value="appeal"),
            discord.SelectOption(label="🆘 General Support", value="support"),
        ]
    )
    async def select_category(self, interaction: discord.Interaction, select: discord.ui.Select):
        category = select.values[0]
        
        # Get the guild
        guild = interaction.guild
        
        # Create ticket category if it doesn't exist
        ticket_category = discord.utils.get(guild.categories, name="Tickets")
        if not ticket_category:
            ticket_category = await guild.create_category("Tickets")
        
        # Create private channel
        ticket_number = len([c for c in ticket_category.channels if c.name.startswith("ticket-")]) + 1
        channel_name = f"ticket-{category}-{ticket_number}"
        
        # Create permissions
        permissions = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages=True),
        }
        
        # Add admin/moderator permissions
        admin_role = discord.utils.get(guild.roles, name="Admin")
        mod_role = discord.utils.get(guild.roles, name="Moderator")
        
        if admin_role:
            permissions[admin_role] = discord.PermissionOverwrite(read_messages=True, send_messages=True)
        if mod_role:
            permissions[mod_role] = discord.PermissionOverwrite(read_messages=True, send_messages=True)
        
        # Create the ticket channel
        ticket_channel = await ticket_category.create_text_channel(
            channel_name,
            overwrites=permissions
        )
        
        # Create ticket embed
        embed = discord.Embed(
            title=f"Support Ticket - {TICKET_CATEGORIES.get(category, 'Support')}",
            description=f"**User:** {interaction.user.mention}\n**Category:** {TICKET_CATEGORIES.get(category, 'Support')}\n\nPlease describe your issue in detail.",
            color=COLOR_PRIMARY
        )
        
        # Get admin/mod for mentioning
        mention_text = ""
        if admin_role:
            mention_text += f"{admin_role.mention} "
        if mod_role:
            mention_text += f"{mod_role.mention}"
        
        if mention_text.strip():
            msg = await ticket_channel.send(f"{mention_text.strip()}\n{embed}")
        else:
            msg = await ticket_channel.send(embed=embed)
        
        # Send confirmation to user
        confirm_embed = discord.Embed(
            title="✅ Ticket Created",
            description=f"Your ticket has been created: {ticket_channel.mention}",
            color=COLOR_SUCCESS
        )
        
        await interaction.response.send_message(embed=confirm_embed, ephemeral=True)

async def setup(bot):
    await bot.add_cog(TicketingSystem(bot))