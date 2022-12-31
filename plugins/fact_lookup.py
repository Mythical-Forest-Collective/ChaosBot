from hata import Client, Embed, Color as Colour

Chaos: Client

FACT_URL = "https://catfact.ninja/fact"
IMAGE_URL = "https://api.thecatapi.com/v1/images/search"

@Chaos.interactions(is_global=True)
async def cat_fact(client, event):
  yield

  async with client.http.get(FACT_URL) as response:
    fact = await response.json()

  yield

  async with client.http.get(IMAGE_URL) as response:
    image = (await response.json())[0]['url']

  Colour.set_seed()
  result = Embed("Cat Fact!", fact['fact'], Colour.random())  \
   .add_image(image)

  yield result
