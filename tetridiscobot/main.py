import asyncio
from logging import DEBUG, Formatter, INFO
from discord.ext import commands
from dotenv import load_dotenv
import discord
import os

load_dotenv()

class TetriBot(commands.AutoShardedBot):
    def __init__(self, *args, **kwargs):
        super().__init__(
            intents=discord.Intents.default(),
            command_prefix=commands.when_mentioned_or('!')
        )
        self.remove_command("help")
        asyncio.run(self._initialize_bot("cogs.profile"))

    async def _initialize_bot(self, cog_path: str = None):
    #     await self.wait_until_ready()
        if cog_path is not None:
            await self.load_extension(cog_path)

if __name__ == "__main__":
    bot = TetriBot()
    bot.run(os.environ["DISCORD_TOKEN_PROD"], reconnect=True, log_level=INFO)
