#!/usr/bin/python

# This is just a basic script to format prompts (following the format)
# into JSON, and show you the amount of characters in the prompt

try:
  import readline
except ImportError:
  pass

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

result = "      [\n"
for line in prompt:
  result += '         "' + line.replace('"', '\\"') + '"'
  if prompt.index(line) != len(prompt) - 1:
    result += ",\n"

result += "\n      ],"

print(f"There are {characters} characters in this prompt, the JSON formatted output is below:")
print(result)
