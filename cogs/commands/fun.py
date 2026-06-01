import discord
from discord.ext import commands
from config import COLOR_PRIMARY, OWNER_ID

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def is_owner(ctx):
        return ctx.author.id == OWNER_ID

    @commands.command(name="ai")
    async def ai(self, ctx, *, question: str):
        """Ask AI a question (requires OpenAI API key)"""
        try:
            from config import OPENAI_API_KEY
            
            if not OPENAI_API_KEY:
                embed = discord.Embed(
                    title="❌ Error",
                    description="OpenAI API key not configured",
                    color=0xED4245
                )
                await ctx.send(embed=embed)
                return
            
            import openai
            openai.api_key = OPENAI_API_KEY
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": question}]
            )
            
            answer = response["choices"][0]["message"]["content"]
            
            embed = discord.Embed(
                title="🤖 AI Response",
                description=answer[:2000],
                color=COLOR_PRIMARY
            )
            
            await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(
                title="❌ Error",
                description=f"Failed to get AI response: {str(e)}",
                color=0xED4245
            )
            await ctx.send(embed=embed)

    @commands.command(name="autoresponder")
    @commands.check(is_owner)
    async def autoresponder(self, ctx, action: str, *, message: str = None):
        """Set up automatic responses"""
        if action.lower() == "enable" and message:
            embed = discord.Embed(
                title="✅ Auto-responder Enabled",
                description=f"Response: {message}",
                color=0x57F287
            )
        elif action.lower() == "disable":
            embed = discord.Embed(
                title="✅ Auto-responder Disabled",
                color=0x57F287
            )
        else:
            embed = discord.Embed(
                title="❌ Invalid Action",
                description="Use: `autoresponder enable <message>` or `autoresponder disable`",
                color=0xED4245
            )
        
        await ctx.send(embed=embed)

    @commands.command(name="welcome")
    async def welcome(self, ctx):
        """Show welcome message"""
        embed = discord.Embed(
            title="👋 Welcome!",
            description="Welcome to our server! Feel free to explore and don't hesitate to ask questions.",
            color=COLOR_PRIMARY
        )
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Fun(bot))