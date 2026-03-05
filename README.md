# OpenClaw Skill Template

A starter template for creating OpenClaw Skills. **Skills** are language-agnostic Markdown files with YAML frontmatter that extend Claude's capabilities by providing access to tools, APIs, and external systems.

**Fork this repo** and start building your own skill to extend Claude's reach.

## What is an OpenClaw Skill?

An OpenClaw Skill is a Markdown file (`SKILL.md`) containing:

- **YAML frontmatter**: Metadata (name, description, requirements, installation instructions)
- **Markdown body**: Documentation describing purpose, usage, commands, and examples

Skills are distributed via the **ClawHub registry** and installed locally to `~/.openclaw/workspace/skills/<skill-name>/`. They enable Claude to interact with external systems without requiring code deployments or complex plugin infrastructure.

## Quick Start

### 1. Use This Template

Click the **"Use this template"** button on GitHub to create a new repo based on this template.

### 2. Clone Your Repo

```bash
git clone https://github.com/YOUR_USERNAME/my-skill.git
cd my-skill
```

### 3. Edit the Template

Edit `SKILL.md` with your skill's metadata and documentation:

```yaml
---
name: my-skill
description: "What my skill does and when to use it."
metadata:
  openclaw:
    emoji: 🎯
    requires:
      bins:
        - my-cli-tool
    install:
      - id: brew
        kind: brew
        formula: my-tool
        bins: [my-cli-tool]
        label: "Install via Homebrew"
---

## Purpose
...
```

### 4. Test Locally

```bash
# Install to your local skills directory
cp -r . ~/.openclaw/workspace/skills/my-skill

# Verify it loads
openclaw skills list | grep my-skill

# Test invocation
openclaw invoke my-skill --help
```

### 5. Publish to ClawHub

```bash
# From within the skill directory
clawhub publish

# Verify it's published
clawhub search my-skill
```

## File Structure

```
my-skill/
├── SKILL.md          # Main skill file with frontmatter and docs
├── README.md         # This file
├── CHANGELOG.md      # Version history
├── LICENSE           # MIT License
├── .github/
│   └── workflows/
│       └── ci.yml    # GitHub Actions validation
└── examples/         # Example skill implementations
    ├── hello-world/
    │   └── SKILL.md
    └── api-connector/
        └── SKILL.md
```

## SKILL.md Format Reference

### Frontmatter Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes | Unique skill identifier (kebab-case) |
| `description` | string | Yes | One-line description of the skill's purpose |
| `metadata.openclaw.emoji` | string | No | Single emoji for UI display |
| `metadata.openclaw.requires.bins` | array | No | Required executables/binaries |
| `metadata.openclaw.requires.env` | array | No | Required environment variables |
| `metadata.openclaw.install` | array | No | Installation methods (brew, apt, manual) |

### Installation Methods

Define how users should install your skill's dependencies:

```yaml
install:
  - id: brew
    kind: brew
    formula: package-name        # Homebrew package name
    bins: [binary-name]          # Resulting binary to verify
    label: "Install via Homebrew"

  - id: apt
    kind: apt
    package: package-name        # APT package name
    bins: [binary-name]
    label: "Install via APT"

  - id: manual
    kind: manual
    label: "Manual installation"
    steps:
      - "Step 1: ..."
      - "Step 2: ..."
```

### Markdown Body Structure

Recommended sections in your SKILL.md body:

1. **Purpose**: What the skill does
2. **When to Use**: Specific use cases
3. **When NOT to Use**: Where this skill is inappropriate
4. **Setup**: Prerequisites and local testing instructions
5. **Commands / Actions**: Available operations
6. **Examples**: Copy-paste-ready examples
7. **Notes**: Limitations, security, troubleshooting

## Examples

This template includes two example skills in the `examples/` directory:

### `examples/hello-world/SKILL.md`

The simplest possible skill with no dependencies. Great for understanding the basics.

### `examples/api-connector/SKILL.md`

A more complex skill that requires environment variables and a CLI tool. Demonstrates real-world patterns.

## Validation

This template includes GitHub Actions (`.github/workflows/ci.yml`) that automatically validates:

- `SKILL.md` exists
- YAML frontmatter is syntactically valid
- Required fields (`name`, `description`) are present
- All referenced binaries are valid

Validation runs on every push and pull request.

## Publishing to ClawHub

When your skill is complete:

1. Update `CHANGELOG.md` with your changes
2. Ensure `SKILL.md` has all required fields
3. Push to your repo and tag a release (e.g., `v1.0.0`)
4. Run `clawhub publish` to submit to the registry
5. (Optional) Submit a PR to [awesome-openclaw](https://github.com/OpenClawHQ/awesome-openclaw)

## Installation Methods Reference

### Homebrew Installation

For macOS and Linux users:

```yaml
- id: brew
  kind: brew
  formula: my-package
  bins: [my-binary]
  label: "Install via Homebrew"
```

### APT Installation

For Debian/Ubuntu users:

```yaml
- id: apt
  kind: apt
  package: my-package
  bins: [my-binary]
  label: "Install via APT"
```

### Manual Installation

For tools without package managers or custom setups:

```yaml
- id: manual
  kind: manual
  label: "Manual installation"
  steps:
    - "Download from https://example.com/download"
    - "Extract the archive"
    - "Add to PATH or move to /usr/local/bin"
    - "Verify: my-binary --version"
```

## Best Practices

- **Clear description**: Make it obvious what your skill does in one sentence
- **Real examples**: Include working examples that users can copy
- **Document limitations**: Explain what your skill can't do
- **Test locally**: Always test with `~/.openclaw/workspace/skills/` before publishing
- **Semantic versioning**: Follow SEMVER in your `CHANGELOG.md`
- **Security**: Never store credentials in the skill; use environment variables

## Resources

- **OpenClaw Docs**: https://docs.openclaw.io
- **ClawHub Registry**: https://clawhub.io
- **GitHub Skills Repository**: https://github.com/OpenClawHQ/skills
- **Contributing Guide**: https://github.com/OpenClawHQ/.github/blob/main/CONTRIBUTING.md

## Contributing

Have questions or found an issue? Open an issue or submit a PR on GitHub.

## License

MIT License. See [LICENSE](LICENSE) for details.

---

Built with the [OpenClaw Skill Template](https://github.com/OpenClawHQ/skill-template). Every skill extends Claude's reach.
