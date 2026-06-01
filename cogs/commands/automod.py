import discord
from discord.ext import commands
from config import COLOR_PRIMARY, COLOR_SUCCESS, OWNER_ID
import json
import os

class Automod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config_file = "automod_config.json"
        self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file) as f:
                self.config = json.load(f)
        else:
            self.config = {}

    def save_config(self):
        with open(self.config_file, "w") as f:
            json.dump(self.config, f, indent=4)

    def is_owner(ctx):
        return ctx.author.id == OWNER_ID

    @commands.command(name="automod")
    @commands.check(is_owner)
    async def automod(self, ctx, action: str):
        """Enable/Disable automod"""
        guild_id = str(ctx.guild.id)
        
        if action.lower() == "enable":
            self.config[guild_id] = True
            self.save_config()
            
            embed = discord.Embed(
                title="✅ Automod Enabled",
                color=COLOR_SUCCESS
            )
        elif action.lower() == "disable":
            self.config[guild_id] = False
            self.save_config()
            
            embed = discord.Embed(
                title="✅ Automod Disabled",
                color=COLOR_SUCCESS
            )
        else:
            embed = discord.Embed(
                title="❌ Invalid Action",
                description="Use: `automod enable` or `automod disable`",
                color=0xED4245
            )
        
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        
        guild_id = str(message.guild.id)
        
        if self.config.get(guild_id, False):
            # Add your automod checks here
            pass

    @commands.command(name="antinuke")
    @commands.check(is_owner)
    async def antinuke(self, ctx, action: str):
        """Enable/Disable antinuke protection"""
        if action.lower() == "enable":
            embed = discord.Embed(
                title="✅ Antinuke Enabled",
                color=COLOR_SUCCESS
            )
        elif action.lower() == "disable":
            embed = discord.Embed(
                title="✅ Antinuke Disabled",
                color=COLOR_SUCCESS
            )
        else:
            embed = discord.Embed(
                title="❌ Invalid Action",
                description="Use: `antinuke enable` or `antinuke disable`",
                color=0xED4245
            )
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Automod(bot))