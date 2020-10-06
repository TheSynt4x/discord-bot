import discord
import requests
from bot.api import api
from bot.helpers import save_image
from discord.ext import commands
from PIL import Image
from resources.data import eightball

from .helpers import remove_last_message


class MemeCommands(commands.Cog):

  @commands.command(name='shit', description='I stepped in shit')
  @remove_last_message()
  async def shit(self, ctx, user: discord.User = None):
    shit = Image.open('./resources/memes/shit.jpg')
    avatar = Image.open(requests.get(
        user.avatar_url,
        stream=True,
    ).raw,).convert('RGBA')

    avatar = avatar.resize((200, 200))
    avatar = avatar.rotate(310, expand=True)

    shit.paste(avatar, (150, 585), avatar)

    shit = save_image(shit)

    await ctx.send(file=shit)

  @commands.command(name='disability')
  @remove_last_message()
  async def disability(self, ctx, user: discord.User = None):
    disability = Image.open('./resources/memes/disability.jpg')
    avatar = Image.open(requests.get(
        user.avatar_url,
        stream=True,
    ).raw,).convert('RGBA')

    avatar = avatar.resize((120, 120))

    disability.paste(avatar, (360, 250), avatar)
    disability = save_image(disability)

    await ctx.send(file=disability)

  @commands.command('trump-quote', description='Trump quote')
  @remove_last_message()
  async def trump_quote(self, ctx):
    quote = api.get_trump_quote()

    await ctx.send('%s\n-Donald Trump, %s' % (
        quote.get('quote'),
        quote.get('year'),
    ))

  @commands.command('dadjoke', description='Dad joke')
  @remove_last_message()
  async def dad_joke(self, ctx):
    joke = api.get_dad_joke()

    await ctx.send('%s\n%s' % (joke.get('setup'), joke.get('punchline')))

  @commands.command(name='8ball')
  @remove_last_message()
  async def magic_ball(self, ctx, *args):
    if not ' '.join(args).endswith('?'):
      await ctx.send('You must provide a question.')
      return

    await ctx.send(eightball.get_random_answer())


def setup(bot):
  bot.add_cog(MemeCommands(bot))
