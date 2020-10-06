from bot.core._config import settings
from bot.core._logger import logger
from bot.helpers import rich_embed
from discord.ext import commands

from .helpers import remove_last_message


class BaseCommands(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command(name='listcogs', description='List all available cogs')
  @remove_last_message()
  async def list_cogs(self, ctx) -> None:
    """ List all available cogs """

    logger.info('Available cogs: %s' % settings.COGS)

    fields = []
    for cog in settings.COGS:
      fields.append({
          'name': cog.get('name'),
          'value': cog.get('description'),
          'inline': False
      })

    embed = rich_embed(
        'Cogs',
        'Down below is a list of available cogs',
        0x8A2BE2,
        fields,
    )

    await ctx.send(embed=embed)

  @commands.command(name='load', description='Load a cog by name')
  @remove_last_message()
  async def load(self, ctx, name) -> None:
    """ Load a cog by name """

    logger.info('Loading cog: %s' % name)

    try:
      self.bot.load_extension('bot.cogs.%s' % name)

    except Exception as e:
      logger.info(e)
      ctx.send(e)

  @commands.command(name='reload', description='Reload a cog')
  @remove_last_message()
  async def reload_cog(self, ctx, name) -> None:
    """ Reload a cog """

    logger.info('Reloading cog: %s' % name)

    try:
      self.bot.reload_extension('bot.cogs.%s' % name)

    except Exception as e:
      logger.info(e)
      ctx.send(e)

  @commands.command(name='unload', description='Unload a cog')
  @remove_last_message()
  async def unload(self, ctx, name) -> None:
    """ Unload a cog """

    logger.info('Unloading cog: %s' % name)

    try:
      self.bot.unload_extension('bot.cogs.%s' % name)

    except Exception as e:
      logger.info(e)
      ctx.send(e)


def setup(bot):
  bot.add_cog(BaseCommands(bot))
