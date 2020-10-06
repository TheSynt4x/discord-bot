import json


class Settings:
  TOKEN: str
  PREFIX: str

  COGS = [
      {
          'name': 'base',
          'description': 'Base cog for loading, reloading and unloading cogs'
      },
      {
          'name': 'utility',
          'description': 'Utility cog'
      },
      {
          'name': 'meme',
          'description': 'Meme cog'
      },
  ]

  def __init__(self, *args, **kwargs) -> None:
    self.TOKEN = kwargs['token']
    self.PREFIX = kwargs['prefix']
    self.SELFBOT = kwargs['selfbot']


with open('config.json') as config:
  settings = Settings(**json.load(config))

settings = settings
