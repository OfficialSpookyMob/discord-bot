import discord
from discord.ext import commands
from config import COLOR_PRIMARY, COLOR_SUCCESS, OWNER_ID
import aiohttp

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def is_owner(ctx):
        return ctx.author.id == OWNER_ID

    @commands.command(name="mcstatus")
    async def mcstatus(self, ctx, server: str):
        """Check Minecraft server status"""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://api.mcsrvstat.us/2/{server}") as resp:
                    data = await resp.json()
            
            embed = discord.Embed(
                title=f"🎮 MC Server: {server}",
                color=COLOR_PRIMARY
            )
            
            embed.add_field(name="Status", value="🟢 Online" if data.get("online") else "🔴 Offline", inline=False)
            
            if data.get("online"):
                embed.add_field(name="Players", value=f"{data['players']['online']}/{data['players']['max']}", inline=False)
            
            await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(
                title="❌ Error",
                description=f"Could not fetch server info: {str(e)}",
                color=0xED4245
            )
            await ctx.send(embed=embed)

    @commands.command(name="dm")
    @commands.check(is_owner)
    async def dm(self, ctx, user: discord.User, *, message: str):
        """DM a user"""
        try:
            await user.send(message)
            
            embed = discord.Embed(
                title="✅ Message Sent",
                description=f"Sent DM to {user.mention}",
                color=COLOR_SUCCESS
            )
            
            await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(
                title="❌ Error",
                description=f"Failed to send DM: {str(e)}",
                color=0xED4245
            )
            await ctx.send(embed=embed)

    @commands.command(name="dmall")
    @commands.check(is_owner)
    async def dmall(self, ctx, *, message: str):
        """DM all members"""
        count = 0
        
        for member in ctx.guild.members:
            if not member.bot:
                try:
                    await member.send(message)
                    count += 1
                except:
                    pass
        
        embed = discord.Embed(
            title="✅ Messages Sent",
            description=f"Sent DM to {count} members",
            color=COLOR_SUCCESS
        )
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Utility(bot))