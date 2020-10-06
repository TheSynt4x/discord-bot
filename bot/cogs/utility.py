import asyncio
import random

import discord
from bot.core._logger import logger
from bot.helpers import rich_embed
from discord.ext import commands

from . import helpers
from .helpers import remove_last_message


class UtilityCommands(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command(name='purge', description='Purge your messages')
  async def purge(self, ctx, limit: int):
    async for x in ctx.history(limit=limit):
      await x.delete()
      await asyncio.sleep(1)  # avoid rate limit

    logger.info('%s messages were just deleted' % limit)

  @commands.command(name='avatar', description='Get a user avatar')
  @remove_last_message()
  async def avatar(self, ctx, user: discord.User = None):
    user = ctx.message.author if user is None else user

    embed = rich_embed(f'Avatar {user.name}', '', 0x8A2BE2)
    embed.set_image(url=user.avatar_url)

    await ctx.send(embed=embed)

  @commands.command(name='leet')
  @remove_last_message()
  async def leet(self, ctx, *args):
    await ctx.send(helpers.leet(' '.join(args)))

  @commands.command(name='reverse')
  @remove_last_message()
  async def reverse(self, ctx, *args):
    await ctx.send(helpers.reverse_args(args))

  @commands.command(name='lmgtfy', description='Let me google that for you')
  @remove_last_message()
  async def lmgtfy(self, ctx, *args):
    await ctx.send(helpers.lmgtfy(args))

  @commands.command()
  @remove_last_message()
  async def roll(self, ctx):
    r = random.randint(1, 101)

    message = 'Rolled: %s'

    if r == 100:
      message = 'Gottem! Rolled: %s'
    elif r == 99:
      message = 'Bullseye! Rolled: %s'
    elif r == 0:
      message = 'Try again. Rolled: %s'

    await ctx.send(message % r)


def setup(bot):
  bot.add_cog(UtilityCommands(bot))
