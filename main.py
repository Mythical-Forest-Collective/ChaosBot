from datetime import datetime
from json import load as jload

from hata import Client
from hata.ext.plugin_loader import PLUGIN_LOADER as PL


with open('config.json') as f:
  config = jload(f)

Chaos = Client(
  token=config['token'],
  extensions='slash'
)

@Chaos.events
async def ready(client):
  print(f"{client:f} has joined the party!")

PL.add_default_variables(
  BOT_STARTED_AT=datetime.now(),

  Chaos=Chaos,

  config=config
)

PL.register('plugins')
PL.load_all()

Chaos.start()
