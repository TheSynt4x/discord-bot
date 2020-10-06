from bot.core._config import settings
from bot.events import bot

for cog in settings.COGS:
  bot.load_extension('bot.cogs.%s' % cog.get('name'))

bot.run(settings.TOKEN, bot=False)
