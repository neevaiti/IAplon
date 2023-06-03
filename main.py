import settings
import discord
import asyncio

from discord.ext import commands
from tools.other.ping import PingCog

logger = settings.logging.getLogger("bot")

async def run():
    intents = discord.Intents.default()
    intents.messages = True

    bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())
    
    # Import commands here
    await bot.add_cog(PingCog(bot))
    
    @bot.event
    async def on_ready():
        logger.info(f"Le bot {bot.user} (ID: {bot.user.id}) est en ligne.")
            
    await bot.start(settings.TOKEN, reconnect=True)

if __name__ == "__main__":
    asyncio.run(run())