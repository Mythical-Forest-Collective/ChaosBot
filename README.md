# ChaosBot
This is a crappy bot we're working on!

## `prompts.json`
`prompts.json` is just a collection of prompts we're using to provide
the incorrect quote generator command! We have a format in it, if you
take a look!

The format has an ID for the key (this is not used for indexing, it's
used for identification), a `lines` key for all of the lines in the
prompt as a string array, an `author` field for if we know the source
or original author who submitted it, and a `tags` key, for if we know
the prompt is a ship or explicit! We're still going through the
prompts though, so not all have been marked as such yet!

Strings meant to be replaced is `{A}`, `{B}`, `{C}`, `{D}`, `{E}` and
`{F}`. There's also `{C^}` which just means to replace it with C's
name, but uppercase.
