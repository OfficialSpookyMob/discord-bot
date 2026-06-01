import discord
from discord.ext import commands
import os
import time
from config import TOKEN, PREFIX, OWNER_ID, COLOR_PRIMARY

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=None)

# Bot start time
bot.start_time = time.time()

@bot.event
async def on_ready():
    print(f"✅ Bot logged in as {bot.user}")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=f"{PREFIX}help | Made by SpookyMob"
        )
    )
    
    # Load all cogs
    for filename in os.listdir("./cogs/commands"):
        if filename.endswith(".py") and filename != "__init__.py":
            try:
                await bot.load_extension(f"cogs.commands.{filename[:-3]}")
                print(f"✅ Loaded cogs.commands.{filename[:-3]}")
            except Exception as e:
                print(f"❌ Failed to load cogs.commands.{filename[:-3]}: {e}")

@bot.command(name="help")
async def help_command(ctx):
    """Display the help menu"""
    embed = discord.Embed(
        title="🤖 Bot Commands Help",
        description="Use the commands below to control the bot",
        color=COLOR_PRIMARY
    )
    
    embed.add_field(
        name="📊 **Info Commands**",
        value="`botinfo` - Bot information\n`uptime` - Bot uptime",
        inline=False
    )
    
    embed.add_field(
        name="🛡️ **Moderation Commands**",
        value="`ban <user> [reason]` - Ban a member\n`kick <user> [reason]` - Kick a member\n`timeout <user> <time> [reason]` - Timeout a member",
        inline=False
    )
    
    embed.add_field(
        name="⚙️ **Admin Commands**",
        value="`setprefix <prefix>` - Set bot prefix\n`adminlist` - List all admins\n`addadmin <user>` - Add admin\n`autorole <role>` - Set autorole",
        inline=False
    )
    
    embed.add_field(
        name="🎵 **Music Commands**",
        value="`play <song>` - Play a song\n`stop` - Stop music\n`pause` - Pause music\n`resume` - Resume music",
        inline=False
    )
    
    embed.add_field(
        name="🤖 **AI Commands**",
        value="`ai <question>` - Ask AI a question",
        inline=False
    )
    
    embed.add_field(
        name="🆘 **Ticket Commands**",
        value="`ticketsetup` - Setup ticket system\n`closeticket` - Close current ticket",
        inline=False
    )
    
    embed.add_field(
        name="📨 **Message Commands**",
        value="`dm <user> <message>` - DM a user\n`dmall <message>` - DM all members\n`autoresponder <enable/disable> <message>` - Auto responder",
        inline=False
    )
    
    embed.add_field(
        name="🔧 **Utility Commands**",
        value="`mcstatus <server>` - Check MC server status\n`automod <enable/disable>` - Toggle automod\n`antinuke <enable/disable>` - Toggle antinuke",
        inline=False
    )
    
    embed.set_footer(text=f"Prefix: {PREFIX} | Use {PREFIX}help <command> for more info")
    await ctx.send(embed=embed)

if __name__ == "__main__":
    bot.run(TOKEN)