"""OpenClaw Plugin Template.

This is the entry point for your plugin. Modify PluginBase and PluginConfig
to match your use case, or import them in plugin.py and build from there.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class PluginConfig:
    """Configuration container for plugin settings.

    Reads from a config dict (parsed from plugin.toml or environment variables).
    """

    def __init__(self, data: dict[str, Any] | None = None) -> None:
        self._data = data or {}

    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration value by key."""
        return self._data.get(key, default)

    def require(self, key: str) -> Any:
        """Get a required configuration value. Raises if missing."""
        if key not in self._data:
            raise KeyError(f"Required config key missing: '{key}'")
        return self._data[key]

    def __repr__(self) -> str:
        keys = list(self._data.keys())
        return f"PluginConfig(keys={keys})"


class PluginBase(ABC):
    """Base class for all OpenClaw plugins.

    Subclass this and implement `setup()` and `execute()` to create a plugin.
    """

    name: str = "unnamed-plugin"
    version: str = "0.0.0"
    description: str = ""

    @abstractmethod
    def setup(self, config: PluginConfig) -> None:
        """Initialize the plugin with configuration.

        Called once when the plugin is loaded. Use this to validate config,
        establish connections, or prepare resources.
        """
        ...

    @abstractmethod
    def execute(self, context: dict[str, Any]) -> dict[str, Any]:
        """Execute the plugin's main logic.

        Called each time the plugin is invoked. Receives a context dict
        with runtime information and returns a result dict.
        """
        ...

    def teardown(self) -> None:
        """Clean up resources.

        Called when the plugin is unloaded. Override to close connections,
        flush buffers, etc. Default implementation does nothing.
        """

    def __repr__(self) -> str:
        return f"<Plugin: {self.name} v{self.version}>"


__all__ = ["PluginBase", "PluginConfig"]
