#!/usr/bin/python

# This is just a basic script to add tags to existing prompts

try:
  import readline
except ImportError:
  pass

from string import ascii_lowercase
from random import choice as randchoice

import json

with open('prompts.json') as f:
  prompts = json.load(f)

id = input("What prompt (indexed by IDs) do you want to edit? ").lower().strip()

tags = input("What tags do you want to add? (Space-separated list) ").lower().strip()
if tags == "":
  tags = []
else:
  tags = tags.split(' ')

chars = "0"
for i in range(1, 7):
  i = str(i)

  if id in list(prompts[i].keys()):
    chars = i
    break

  raise SystemExit(f"Couldn't find the prompt with the ID `{id}`!")

print("The prompt will be printed below:")
print('\n'.join(prompts[chars][id]['lines']))

while True:
  ans = input("Is the entered information correct? ").strip().lower()
  if ans in ('y', 'yes'):
    print("Setting the prompt's tags to the new tags...")
    prompts[chars][id]['tags'] = tags

    with open('prompts.json', 'w+') as f:
      json.dump(prompts, f, indent=2, ensure_ascii=False)

    break

  elif ans in ('n', 'no'):
    raise SystemExit("Alright, figure out the issue and come back when it's fixed.")

  else:
    print("That's an invalid answer!")

print(f"The ID of the prompt is `{id}`")
