import io

from discord import Activity, Embed, File
"""
Discord related helpers, used globally in the project
"""


def rich_embed(title, description, color, fields=[]):
  """ Discord rich embed """

  embed = Embed(title=title, description=description, color=color)

  for field in fields:
    embed.add_field(
        name=field.get('name'),
        value=field.get('value'),
        inline=field.get('inline'),
    )

  return embed


async def change_activity(bot, activity_type, activity):
  """ Change bot activity """

  await bot.change_presence(
      activity=Activity(type=activity_type, name=activity))


def save_image(image):
  """ Return a discord file """
  arr = io.BytesIO()

  image.save(arr, format='PNG')
  arr.seek(0)

  return File(arr, 'default.png')
