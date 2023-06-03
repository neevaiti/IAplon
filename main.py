import settings
import discord

from discord.ext import commands


logger = settings.logging.getLogger("bot")

def run():
    
    intents = discord.Intents.default()
    intents.messages = True

    bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())
    
    @bot.event
    async def on_ready():
        logger.info(f"Le bot {bot.user} (ID: {bot.user.id}) est en ligne.")
        
    
    @bot.command()
    async def ping(ctx):
        await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")
    
    
    bot.run(settings.TOKEN, root_logger=True)
    
if __name__ == "__main__":
    run()