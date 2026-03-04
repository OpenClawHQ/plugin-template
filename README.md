# OpenClaw Plugin Template

A starter template for building OpenClaw plugins. Fork this repo and start building.

## Quick start

```bash
# 1. Fork this template on GitHub (click "Use this template")

# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/my-plugin.git
cd my-plugin

# 3. Install dependencies
pip install -e ".[dev]"

# 4. Run the example
python -m openclaw_plugin

# 5. Run tests
pytest
```

## Project structure

```
my-plugin/
├── src/
│   └── openclaw_plugin/
│       ├── __init__.py      # Plugin entry point & metadata
│       ├── plugin.py        # Core plugin logic
│       └── config.py        # Configuration schema
├── tests/
│   ├── __init__.py
│   └── test_plugin.py       # Plugin tests
├── pyproject.toml            # Project config & dependencies
├── LICENSE                   # MIT License
├── CHANGELOG.md              # Version history
└── README.md                 # You are here
```

## Writing your plugin

### 1. Define your plugin

Edit `src/openclaw_plugin/plugin.py`. The `Plugin` class is the entry point:

```python
from openclaw_plugin import PluginBase, PluginConfig

class Plugin(PluginBase):
    """Your plugin description here."""

    name = "my-plugin"
    version = "0.1.0"

    def setup(self, config: PluginConfig) -> None:
        """Called once when the plugin is loaded."""
        self.api_key = config.get("api_key")

    def execute(self, context: dict) -> dict:
        """Called when the plugin is invoked."""
        # Your logic here
        return {"status": "ok", "result": "..."}
```

### 2. Configure it

Edit `src/openclaw_plugin/config.py` to define what configuration your plugin accepts:

```python
PLUGIN_CONFIG = {
    "name": "my-plugin",
    "version": "0.1.0",
    "description": "What this plugin does.",
    "author": "Your Name",
    "settings": {
        "api_key": {
            "type": "string",
            "required": True,
            "description": "API key for the target service."
        },
        "timeout": {
            "type": "integer",
            "default": 30,
            "description": "Request timeout in seconds."
        }
    }
}
```

### 3. Test it

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=openclaw_plugin

# Run a specific test
pytest tests/test_plugin.py::test_execute
```

### 4. Ship it

When your plugin is ready:

1. Update the version in `pyproject.toml` and `config.py`.
2. Update `CHANGELOG.md` with your changes.
3. Push to your repo and tag a release.
4. (Optional) Submit it to [awesome-openclaw](https://github.com/OpenClawHQ/awesome-openclaw).

## Configuration

Runtime configuration is loaded from environment variables or a `plugin.toml` file:

```toml
# plugin.toml
[plugin]
name = "my-plugin"

[settings]
api_key = "sk-..."
timeout = 60
```

Or via environment variables:

```bash
export OPENCLAW_PLUGIN_API_KEY="sk-..."
export OPENCLAW_PLUGIN_TIMEOUT=60
```

## CI/CD

This template includes a GitHub Actions workflow (`.github/workflows/ci.yml`) that runs on every push and PR:

- Linting with Ruff
- Type checking with mypy
- Tests with pytest
- Coverage reporting

## Contributing

See the [OpenClawHQ Contributing Guide](https://github.com/OpenClawHQ/.github/blob/main/CONTRIBUTING.md).

## License

MIT License. See [LICENSE](LICENSE) for details.

---

<sub>Built with the [OpenClawHQ Plugin Template](https://github.com/OpenClawHQ/plugin-template). Every claw extends the reach.</sub>
