import discord
from discord.ext import commands
from config import COLOR_SUCCESS, COLOR_ERROR, OWNER_ID

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def is_owner(ctx):
        return ctx.author.id == OWNER_ID

    @commands.command(name="ban")
    @commands.check(is_owner)
    async def ban(self, ctx, user: discord.User, *, reason="No reason provided"):
        """Ban a user from the server"""
        try:
            await ctx.guild.ban(user, reason=reason)
            
            embed = discord.Embed(
                title="✅ User Banned",
                description=f"**User:** {user.mention}\n**Reason:** {reason}",
                color=COLOR_SUCCESS
            )
            
            await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(
                title="❌ Error",
                description=f"Failed to ban user: {str(e)}",
                color=COLOR_ERROR
            )
            await ctx.send(embed=embed)

    @commands.command(name="kick")
    @commands.check(is_owner)
    async def kick(self, ctx, user: discord.User, *, reason="No reason provided"):
        """Kick a user from the server"""
        try:
            member = await ctx.guild.fetch_member(user.id)
            await member.kick(reason=reason)
            
            embed = discord.Embed(
                title="✅ User Kicked",
                description=f"**User:** {user.mention}\n**Reason:** {reason}",
                color=COLOR_SUCCESS
            )
            
            await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(
                title="❌ Error",
                description=f"Failed to kick user: {str(e)}",
                color=COLOR_ERROR
            )
            await ctx.send(embed=embed)

    @commands.command(name="timeout")
    @commands.check(is_owner)
    async def timeout(self, ctx, user: discord.User, time_str: str, *, reason="No reason provided"):
        """Timeout a user"""
        try:
            member = await ctx.guild.fetch_member(user.id)
            
            # Parse time (e.g., "10m", "1h", "1d")
            time_unit = time_str[-1].lower()
            time_amount = int(time_str[:-1])
            
            if time_unit == 'm':
                timeout_duration = discord.utils.utcnow() + discord.utils.timedelta(minutes=time_amount)
            elif time_unit == 'h':
                timeout_duration = discord.utils.utcnow() + discord.utils.timedelta(hours=time_amount)
            elif time_unit == 'd':
                timeout_duration = discord.utils.utcnow() + discord.utils.timedelta(days=time_amount)
            else:
                await ctx.send("Invalid time format. Use: 10m, 1h, 1d")
                return
            
            await member.timeout(timeout_duration, reason=reason)
            
            embed = discord.Embed(
                title="✅ User Timed Out",
                description=f"**User:** {user.mention}\n**Duration:** {time_str}\n**Reason:** {reason}",
                color=COLOR_SUCCESS
            )
            
            await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(
                title="❌ Error",
                description=f"Failed to timeout user: {str(e)}",
                color=COLOR_ERROR
            )
            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Moderation(bot))