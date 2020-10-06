from discord.ext import commands
from bot.core._config import settings

# Create a discord bot instance
bot = commands.Bot(
    command_prefix=settings.PREFIX,
    self_bot=settings.SELFBOT,
    fetch_offline_members=False,
)
