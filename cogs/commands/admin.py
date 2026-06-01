import discord
from discord.ext import commands
from config import COLOR_PRIMARY, COLOR_SUCCESS, OWNER_ID
import json
import os

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.admin_file = "admins.json"
        self.load_admins()

    def load_admins(self):
        if os.path.exists(self.admin_file):
            with open(self.admin_file) as f:
                self.admins = json.load(f)
        else:
            self.admins = {}

    def save_admins(self):
        with open(self.admin_file, "w") as f:
            json.dump(self.admins, f, indent=4)

    def is_owner(ctx):
        return ctx.author.id == OWNER_ID

    @commands.command(name="setprefix")
    @commands.check(is_owner)
    async def setprefix(self, ctx, prefix: str):
        """Set bot prefix"""
        self.bot.command_prefix = prefix
        
        embed = discord.Embed(
            title="✅ Prefix Changed",
            description=f"New prefix: `{prefix}`",
            color=COLOR_SUCCESS
        )
        
        await ctx.send(embed=embed)

    @commands.command(name="addadmin")
    @commands.check(is_owner)
    async def addadmin(self, ctx, user: discord.User):
        """Add an admin"""
        guild_id = str(ctx.guild.id)
        
        if guild_id not in self.admins:
            self.admins[guild_id] = []
        
        if user.id not in self.admins[guild_id]:
            self.admins[guild_id].append(user.id)
            self.save_admins()
            
            embed = discord.Embed(
                title="✅ Admin Added",
                description=f"{user.mention} has been added as admin",
                color=COLOR_SUCCESS
            )
        else:
            embed = discord.Embed(
                title="⚠️ Already Admin",
                description=f"{user.mention} is already an admin",
                color=0xFAA61A
            )
        
        await ctx.send(embed=embed)

    @commands.command(name="adminlist")
    async def adminlist(self, ctx):
        """List all admins"""
        guild_id = str(ctx.guild.id)
        
        embed = discord.Embed(
            title="👥 Admin List",
            color=COLOR_PRIMARY
        )
        
        if guild_id in self.admins and self.admins[guild_id]:
            admins_mention = ", ".join([f"<@{admin_id}>" for admin_id in self.admins[guild_id]])
            embed.description = admins_mention
        else:
            embed.description = "No admins found"
        
        await ctx.send(embed=embed)

    @commands.command(name="autorole")
    @commands.check(is_owner)
    async def autorole(self, ctx, role: discord.Role):
        """Set automatic role for new members"""
        guild_id = str(ctx.guild.id)
        
        if guild_id not in self.admins:
            self.admins[guild_id] = {}
        
        self.admins[guild_id]["autorole"] = role.id
        self.save_admins()
        
        embed = discord.Embed(
            title="✅ Autorole Set",
            description=f"New members will receive {role.mention}",
            color=COLOR_SUCCESS
        )
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Admin(bot))