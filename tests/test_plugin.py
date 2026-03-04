"""Tests for the example plugin."""

from __future__ import annotations

import pytest

from openclaw_plugin import PluginBase, PluginConfig
from openclaw_plugin.plugin import Plugin


class TestPluginConfig:
    """Tests for PluginConfig."""

    def test_get_existing_key(self) -> None:
        config = PluginConfig({"key": "value"})
        assert config.get("key") == "value"

    def test_get_missing_key_returns_default(self) -> None:
        config = PluginConfig({})
        assert config.get("missing", "fallback") == "fallback"

    def test_get_missing_key_returns_none(self) -> None:
        config = PluginConfig({})
        assert config.get("missing") is None

    def test_require_existing_key(self) -> None:
        config = PluginConfig({"key": "value"})
        assert config.require("key") == "value"

    def test_require_missing_key_raises(self) -> None:
        config = PluginConfig({})
        with pytest.raises(KeyError, match="Required config key missing"):
            config.require("missing")

    def test_repr(self) -> None:
        config = PluginConfig({"a": 1, "b": 2})
        assert "a" in repr(config)


class TestPlugin:
    """Tests for the example Plugin implementation."""

    def test_is_plugin_base(self) -> None:
        plugin = Plugin()
        assert isinstance(plugin, PluginBase)

    def test_metadata(self) -> None:
        plugin = Plugin()
        assert plugin.name == "example-plugin"
        assert plugin.version == "0.1.0"

    def test_setup(self) -> None:
        plugin = Plugin()
        plugin.setup(PluginConfig({"greeting": "Hi"}))
        assert plugin.greeting == "Hi"

    def test_setup_default_greeting(self) -> None:
        plugin = Plugin()
        plugin.setup(PluginConfig({}))
        assert plugin.greeting == "Hello from OpenClaw"

    def test_execute(self) -> None:
        plugin = Plugin()
        plugin.setup(PluginConfig({"greeting": "Hey"}))
        result = plugin.execute({"user": "tester"})
        assert result["status"] == "ok"
        assert result["message"] == "Hey, tester!"
        assert result["plugin"] == "example-plugin"

    def test_execute_default_user(self) -> None:
        plugin = Plugin()
        plugin.setup(PluginConfig({}))
        result = plugin.execute({})
        assert "world" in result["message"]

    def test_teardown_does_not_raise(self) -> None:
        plugin = Plugin()
        plugin.teardown()  # Should not raise

    def test_repr(self) -> None:
        plugin = Plugin()
        assert "example-plugin" in repr(plugin)
        assert "0.1.0" in repr(plugin)
