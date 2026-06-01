import discord
from discord.ext import commands
from config import COLOR_PRIMARY, COLOR_SUCCESS

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="play")
    async def play(self, ctx, *, query: str):
        """Play a song"""
        if not ctx.author.voice:
            embed = discord.Embed(
                title="❌ Error",
                description="You must be in a voice channel",
                color=0xED4245
            )
            await ctx.send(embed=embed)
            return
        
        embed = discord.Embed(
            title="🎵 Now Playing",
            description=query,
            color=COLOR_PRIMARY
        )
        
        await ctx.send(embed=embed)

    @commands.command(name="stop")
    async def stop(self, ctx):
        """Stop music"""
        embed = discord.Embed(
            title="⏹️ Music Stopped",
            color=COLOR_SUCCESS
        )
        
        await ctx.send(embed=embed)

    @commands.command(name="pause")
    async def pause(self, ctx):
        """Pause music"""
        embed = discord.Embed(
            title="⏸️ Music Paused",
            color=COLOR_SUCCESS
        )
        
        await ctx.send(embed=embed)

    @commands.command(name="resume")
    async def resume(self, ctx):
        """Resume music"""
        embed = discord.Embed(
            title="▶️ Music Resumed",
            color=COLOR_SUCCESS
        )
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Music(bot))