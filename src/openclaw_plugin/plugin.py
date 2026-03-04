"""Example plugin implementation.

Replace this with your actual plugin logic.
"""

from __future__ import annotations

from typing import Any

from openclaw_plugin import PluginBase, PluginConfig


class Plugin(PluginBase):
    """Example OpenClaw plugin.

    This is a minimal working example. Replace the logic in `execute()`
    with your own implementation.
    """

    name = "example-plugin"
    version = "0.1.0"
    description = "A minimal example plugin for OpenClaw."

    def setup(self, config: PluginConfig) -> None:
        """Initialize the plugin."""
        self.greeting = config.get("greeting", "Hello from OpenClaw")

    def execute(self, context: dict[str, Any]) -> dict[str, Any]:
        """Execute the plugin.

        Args:
            context: Runtime context containing invocation details.

        Returns:
            A dict with the execution result.
        """
        user = context.get("user", "world")
        message = f"{self.greeting}, {user}!"

        return {
            "status": "ok",
            "plugin": self.name,
            "message": message,
        }

    def teardown(self) -> None:
        """Clean up resources (nothing to clean up in this example)."""


def main() -> None:
    """Run the plugin standalone for development/testing."""
    plugin = Plugin()
    plugin.setup(PluginConfig({"greeting": "Hey there"}))

    result = plugin.execute({"user": "developer"})
    print(f"Plugin: {plugin}")
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
