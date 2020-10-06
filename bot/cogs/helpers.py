from functools import wraps

from requests.utils import requote_uri
"""
Cog related helpers, used only in cogs
"""


def lmgtfy(query):
  return 'http://letmegooglethat.com/?q=%s' % requote_uri(' '.join(query))


def reverse_args(args):
  return ''.join(reversed(' '.join(args)))


def leet(text):
  chars = {"a": "4", "e": "3", "l": "1", "o": "0", "s": "5", "t": "7"}

  def getchar(c):
    return chars[c] if c in chars else c

  return ''.join(getchar(c) for c in text)


def remove_last_message():
  """
  Remove the command message
  """

  def inner(func):

    @wraps(func)
    async def wrapper(self, *args, **kwargs):
      async for x in args[0].history(limit=1):
        await x.delete()

      return await func(self, *args, **kwargs)

    return wrapper

  return inner
