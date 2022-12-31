from hata import Client, Embed, Color

from json import load as jload
from random import choice as randchoice

Chaos: Client

with open('prompts.json') as f:
  prompts = jload(f)

desc = ('str', 'Name for the generator')

@Chaos.interactions(is_global=True)
async def incorrect_quote_generator(client, event, a: desc, b: desc=None,
    c: desc=None, d: desc=None, e: desc=None, f: desc=None):
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

  for line in randchoice(prompts[str(count)]):
    prompt += line.strip() + '\n'

  prompt = prompt[:-2]

  prompt = prompt.replace('{A}', a)

  if b: prompt = prompt.replace('{B}', b)
  if c: prompt = prompt.replace('{C}', c)
  if d: prompt = prompt.replace('{D}', d)
  if e: prompt = prompt.replace('{E}', e)
  if f: prompt = prompt.replace('{F}', f)

  return Embed(title="Incorrect Quote!", description=prompt, color=Color.random())
