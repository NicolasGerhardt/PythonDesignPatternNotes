"""simple plugin loader"""

import importlib

class PluginInterface:
    """A plugin has a single function called initalize"""

    @staticmethod
    def init() -> None:
        """Initalize the plugin"""


def import_module(name: str) -> PluginInterface:
    return importlib.import_module(name)

def load_plugins(plugins: list[str]) -> None:
    """ load plugins defined in the plugin's list"""
    for plugin_name in plugins:
        print(f"Loading Plugin: {plugin_name}")
        plugin = import_module(plugin_name)
        plugin.init()
