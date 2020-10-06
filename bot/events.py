from bot.core._bot import bot
from bot.core._config import settings
from bot.core._logger import logger
"""
Discord bot events

https://discordpy.readthedocs.io/en/latest/api.html#event-reference
"""


@bot.event
async def on_ready():
  logger.info(bot.user.name)
  logger.info(bot.user.id)


if not settings.SELFBOT:

  @bot.event
  async def on_member_join(member):
    logger.info(f'{member} has joined the server')
