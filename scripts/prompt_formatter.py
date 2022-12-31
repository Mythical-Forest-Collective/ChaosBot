#!/usr/bin/python

# This is just a basic script to format prompts (following the format)
# into JSON, and show you the amount of characters in the prompt

try:
  import readline
except ImportError:
  pass

from string import ascii_lowercase
from random import choice as randchoice

import json

with open('prompts.json') as f:
  prompts = json.load(f)

def genId():
  result = ''

  for i in range(5):
    result += randchoice(ascii_lowercase)

  if result in prompts['ids']:
    return genId()

  return result

print("Input the prompt below.")

prompt = ""
characters = 0

while True:
  line = input("")

  if line.strip() == "":
    break

  prompt += line.strip() + '\n'

prompt = prompt[:-1]

if '{A}' in prompt:
  characters += 1

if '{B}' in prompt:
  characters += 1

if '{C}' in prompt:
  characters += 1

if '{D}' in prompt:
  characters += 1

if '{E}' in prompt:
  characters += 1

if '{F}' in prompt:
  characters += 1

prompt = prompt.splitlines()

author = input("Input the prompt author: ").strip()
if author == "": author = "N/A"

result = {'lines': prompt, 'ship': False, 'author': author}


print(f"There are {characters} characters in this prompt. The JSON output is below.")
print(json.dumps(result, indent=2, ensure_ascii=False))

id = genId()

while True:
  ans = input("Is this JSON correct? ").strip().lower()
  if ans in ('y', 'yes'):
    print("Adding the prompt to the prompt list...")
    prompts['ids'].append(id)
    prompts[str(characters)][id] = result

    with open('prompts.json', 'w+') as f:
      json.dump(prompts, f, indent=2, ensure_ascii=False)

    break

  elif ans in ('n', 'no'):
    raise SystemExit("Alright, figure out the issue and come back when it's fixed.")

  else:
    print("That's an invalid answer!")

print(f"The ID of the prompt is `{id}`")

