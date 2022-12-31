from hata import Client
from hata.ext.plugin_loader import PLUGIN_LOADER, PLUGINS

Chaos: Client

PLUGIN_MANAGER_COMMANDS = Chaos.interactions(
  None,
  name="plugin-manager",
  is_global=True
)

@PLUGIN_MANAGER_COMMANDS.interactions
async def reload_all(client, event):
  if not client.is_owner(event.user):
    yield "You don't have the permissions to do this!"
    return

  yield "Reloading all plugins..."
  PLUGIN_LOADER.reload_all()
  yield "Done!"

@PLUGIN_MANAGER_COMMANDS.interactions
async def load(client, event, plugin: ('str', 'The plugin to load!')):
  if not client.is_owner(event.user):
    yield "You don't have the permissions to do this!"
    return

  yield f"Attempting to load the plugin `{plugin}`..."
  try:
    PLUGIN_LOADER.register_and_load(plugin)
    yield f"Loaded `{plugin}`!"

  except ImportError:
    yield f"The plugin `{plugin}` does not exist! Check if you made a typo!"

  except PluginError:
    yield "The plugin is accessible, but there is an error with the code within it!"

@PLUGIN_MANAGER_COMMANDS.interactions
async def unload(client, event, plugin: ('str', 'The plugin to unload!')):
  if not client.is_owner(event.user):
    yield "You don't have the permissions to do this!"
    return

  if plugin.lower() not in (plugin.name.lower() for plugin in PLUGINS.values()):
    yield "The plugin you've entered is not valid! Please use a plugin from the list!"
    return

  yield f"Attempting to unload the plugin `{plugin}`..."
  try:
    PLUGIN_LOADER.unload(plugin)
    yield f"Unloaded `{plugin}`!"

  except PluginError:
    yield "The plugin could not be unloaded for some reason! Is it locked?"

@PLUGIN_MANAGER_COMMANDS.interactions
async def reload(client, event, plugin: ('str', 'The plugin to unload!')):
  if not client.is_owner(event.user):
    yield "You don't have the permissions to do this!"
    return

  if plugin.lower() not in (plugin.name.lower() for plugin in PLUGINS.values()):
    yield "The plugin you've entered is not valid! Please use a plugin from the list!"
    return

  yield f"Attempting to reload the plugin `{plugin}`..."
  try:
    PLUGIN_LOADER.reload(plugin)
    yield f"Reloaded `{plugin}`!"

  except PluginError:
    yield "The plugin could be loaded, but there is an error with the code within it!"


@PLUGIN_MANAGER_COMMANDS.autocomplete('plugin')
async def load_plugin_autocomplete(value):
  results = []

  plugin_names = (plugin.name for plugin in PLUGINS.values())

  if value is None: return plugin_names

  for plugin_name in plugin_names:
    if value.lower() in plugin_name.lower():
      results.append(plugin_name)

  return results
