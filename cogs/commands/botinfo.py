import discord
from discord.ext import commands
from config import COLOR_PRIMARY, OWNER_ID
import time

class BotInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="botinfo")
    async def botinfo(self, ctx):
        """Display bot information"""
        embed = discord.Embed(
            title="🤖 Bot Information",
            color=COLOR_PRIMARY
        )
        
        embed.add_field(name="Bot Name", value=self.bot.user.name, inline=False)
        embed.add_field(name="Bot ID", value=self.bot.user.id, inline=False)
        embed.add_field(name="Owner", value=f"<@{OWNER_ID}>", inline=False)
        embed.add_field(name="Ping", value=f"{round(self.bot.latency * 1000)}ms", inline=False)
        embed.add_field(name="Guilds", value=len(self.bot.guilds), inline=False)
        embed.add_field(name="Users", value=len(set(self.bot.get_all_members())), inline=False)
        
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.set_footer(text="Made with discord.py")
        
        await ctx.send(embed=embed)

    @commands.command(name="uptime")
    async def uptime(self, ctx):
        """Display bot uptime"""
        uptime_seconds = time.time() - self.bot.start_time
        
        days = int(uptime_seconds // 86400)
        hours = int((uptime_seconds % 86400) // 3600)
        minutes = int((uptime_seconds % 3600) // 60)
        seconds = int(uptime_seconds % 60)
        
        embed = discord.Embed(
            title="⏱️ Bot Uptime",
            description=f"`{days}d {hours}h {minutes}m {seconds}s`",
            color=COLOR_PRIMARY
        )
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(BotInfo(bot))