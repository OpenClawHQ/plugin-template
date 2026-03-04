"""Plugin configuration schema.

Edit this file to define what settings your plugin accepts.
"""

PLUGIN_CONFIG = {
    "name": "example-plugin",
    "version": "0.1.0",
    "description": "A minimal example plugin for OpenClaw.",
    "author": "OpenClawHQ",
    "license": "MIT",
    "settings": {
        "greeting": {
            "type": "string",
            "required": False,
            "default": "Hello from OpenClaw",
            "description": "The greeting message the plugin returns.",
        },
    },
}
