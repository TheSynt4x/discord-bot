import requests
"""
Separate your API calls here to not make your cog classes bloated
"""


def get_trump_quote():
  r = requests.get('https://api.tronalddump.io/random/quote')
  r = r.json()

  return {'quote': r.get('value'), 'year': r.get('appeared_at').split('-')[0]}


def get_dad_joke():
  r = requests.get('https://us-central1-dadsofunny.cloudfunctions.net/'
                   'DadJokes/random/jokes')
  r = r.json()

  return {'setup': r.get('setup'), 'punchline': r.get('punchline')}
