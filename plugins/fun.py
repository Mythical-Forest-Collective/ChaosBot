from hata import Client, Embed, Color

from json import load as jload, JSONDecodeError
from random import choice as randchoice

Chaos: Client

with open('prompts.json') as f:
  prompts = jload(f)

desc = ('str', 'Name for the generator')

@Chaos.interactions(is_global=True)
async def reload_prompts(client, event):
  global prompts
  if not client.is_owner(event.user):
    yield "You don't have the permissions to do this!"
    return

  yield "Reloading the prompts..."

  try:
    with open('prompts.json') as f:
      prompts = jload(f)

    yield "Done!"
  except JSONDecodeError as e:
    yield f"Got a `JSONDecodeError`! Error:```python\n{str(e)}```"

def quote_generator(a: desc, b: desc=None,
    c: desc=None, d: desc=None, e: desc=None, f: desc=None,
    exclude_tags: ('str', 'A list separated by a space! Valid tags are `ship` and `explicit`.')=""):
  """An incorrect quote generator command!"""
  count = 1

  if b:
    if not a:
      return "You need to set the first parameter to set the second!"
    count += 1

  if c:
    if not b:
      return "You need to set the second parameter to set the third!"
    count += 1

  if d:
    if not c:
      return "You need to set the third parameter to set the fourth!"
    count += 1

  if e:
    if not d:
      return "You need to set the fourth parameter to set the fifth!"
    count += 1

  if f:
    if not e:
      return "You need to set the fifth parameter to set the sixth!"
    count += 1

  prompt = ""

  key = randchoice(list(prompts[str(count)]))

  if any(item in prompts[str(count)][key]['tags'] for item in exclude_tags.split(' ')):
    return quote_generator(a, b, c, d, e, f, exclude_tags)

  for line in prompts[str(count)][key]['lines']:
    prompt += line.strip() + '\n'

  while prompt.endswith('\n'):
    prompt = prompt[:-1]

  prompt = prompt.replace('{A}', a)

  if b: prompt = prompt.replace('{B}', b)
  if c: prompt = prompt.replace('{C}', c).replace('{C^}', c.upper())
  if d: prompt = prompt.replace('{D}', d)
  if e: prompt = prompt.replace('{E}', e)
  if f: prompt = prompt.replace('{F}', f)

  e = Embed(title="Incorrect Quote!", description=prompt, color=Color.random())

  e.add_footer(f"Prompt key: {key}")

  if prompts[str(count)][key]['author'] != 'N/A':
    e.add_author(f"Prompt from {prompts[str(count)][key]['author']}")

  return e

@Chaos.interactions(is_global=True)
async def incorrect_quote_generator(a: desc, b: desc=None,
    c: desc=None, d: desc=None, e: desc=None, f: desc=None,
    exclude_tags: ('str', 'Valid tags to exclude in a space-separated format are `ship` and `explicit`.')=False):
  return quote_generator(a, b, c, d, e, f, exclude_tags)
