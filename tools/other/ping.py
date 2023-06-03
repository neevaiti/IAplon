from discord.ext import commands

class PingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Répond avec le ping du bot."""
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")
