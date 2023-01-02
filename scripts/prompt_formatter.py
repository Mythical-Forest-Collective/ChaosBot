#!/usr/bin/python

# This is just a basic script to format prompts (following the format)
# into JSON, and show you the amount of characters in the prompt

try:
  import readline
except ImportError:
  pass

__import__('os').system('')

from sys import platform
from string import ascii_lowercase
from random import choice as randchoice

import json

if platform == "linux" or platform == "linux2":
  use_colour = True
else:
  use_colour = False

if use_colour:
  class Colours:
    """ ANSI colour codes """
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"

else:
  class Colours:
    def __getattr__(self, attr):
      return ""

with open('prompts.json') as f:
  prompts = json.load(f)

def genId():
  result = ''

  for i in range(5):
    result += randchoice(ascii_lowercase)

  if result in prompts['ids']:
    return genId()

  return result

print(f"{Colours.GREEN}Input the prompt below.")

prompt = ""
characters = 0

while True:
  line = input(Colours.BLUE)

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

author = input(f"{Colours.GREEN}Input the prompt author:{Colours.END} ").strip()
tags = input(f"{Colours.GREEN}Enter a list of tags separated by a space:{Colours.END} ").lower().strip()
if tags == "":
  tags = []
else:
  tags = tags.split(' ')

if author == "": author = "N/A"

result = {'lines': prompt, 'author': author, 'tags': tags}


print(f"{Colours.GREEN}There are {characters} characters in this prompt. The JSON output is below.")
print(Colours.PURPLE + json.dumps(result, indent=2, ensure_ascii=False))

id = genId()

while True:
  ans = input(f"{Colours.GREEN}Is this JSON correct?{Colours.END} ").strip().lower()
  if ans in ('y', 'yes'):
    print(f"{Colours.GREEN}Adding the prompt to the prompt list...{Colours.END}")
    prompts['ids'].append(id)
    prompts[str(characters)][id] = result

    with open('prompts.json', 'w+') as f:
      json.dump(prompts, f, indent=2, ensure_ascii=False)

    break

  elif ans in ('n', 'no'):
    raise SystemExit(f"{Colours.RED}Alright, figure out the issue and come back when it's fixed.{Colours.END}")

  else:
    print(f"{Colours.RED}mThat's an invalid answer!")

print(f"{Colours.GREEN}The ID of the prompt is `{id}`{Colours.END}")
