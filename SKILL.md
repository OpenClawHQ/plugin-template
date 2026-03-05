---
# Frontmatter: Core metadata for your skill
name: my-skill
description: "A brief one-liner describing what this skill does and when to use it."

# Optional: Extended metadata
metadata:
  openclaw:
    # Display icon (emoji) for this skill in the UI
    emoji: 🔧

    # System requirements for this skill
    requires:
      # List of required binaries/executables
      bins:
        - required-cli-tool
        - another-tool

      # Environment variables that must be set
      env:
        - API_KEY
        - WORKSPACE_ID

    # Installation instructions (shown during skill setup)
    install:
      # Installation method 1: Homebrew (macOS/Linux)
      - id: brew
        kind: brew
        formula: my-package-name
        bins:
          - required-cli-tool
        label: "Install via Homebrew (macOS/Linux)"

      # Installation method 2: APT (Debian/Ubuntu)
      - id: apt
        kind: apt
        package: my-package-name
        bins:
          - required-cli-tool
        label: "Install via APT (Ubuntu/Debian)"

      # Installation method 3: Manual installation
      - id: manual
        kind: manual
        label: "Manual installation"
        steps:
          - "Visit https://example.com/download"
          - "Follow the installation instructions"
          - "Verify with: my-tool --version"
---

## Purpose

A concise description of what this skill does. Explain its primary use cases and what problems it solves.

For example:
- Controls cloud infrastructure via CLI
- Automates data transformations
- Integrates with external APIs
- Manages CI/CD pipelines

## When to Use

Explain the specific scenarios where this skill is most appropriate:

- Scenario 1: Provide concrete examples of tasks that this skill handles well
- Scenario 2: Another use case with practical details
- Scenario 3: More examples that clarify its purpose

## When NOT to Use

Explain scenarios where this skill is NOT appropriate or where other tools/skills would be better:

- Avoid using for: Scenario where this skill is not the right tool
- Don't rely on this for: Another scenario where alternatives exist
- Not suitable for: Use cases requiring different capabilities

## Setup

### Prerequisites

List all prerequisites and how to install them:

1. **Required Tool 1**: Install with `brew install package-name` or `apt install package-name`
2. **Required Tool 2**: Download from https://example.com
3. **Environment Variables**: Set `API_KEY`, `WORKSPACE_ID`, etc.

### Local Testing

To install this skill locally for testing:

```bash
# Copy the skill to your local skills directory
cp -r /path/to/skill ~/.openclaw/workspace/skills/my-skill

# Verify installation
openclaw skills list | grep my-skill

# Test the skill
openclaw invoke my-skill --help
```

### Publishing to ClawHub

When ready to share:

```bash
# Navigate to the skill directory
cd ~/.openclaw/workspace/skills/my-skill

# Publish to ClawHub registry
clawhub publish

# Verify publication
clawhub search my-skill
```

## Commands / Actions

Describe the main operations this skill provides:

### Primary Operation
**Description**: What this does
```
openclaw invoke my-skill primary-action --arg value
```

### Secondary Operation
**Description**: What this does
```
openclaw invoke my-skill secondary-action --option value
```

List all major commands with brief descriptions and syntax.

## Examples

Provide concrete, copy-paste-ready examples:

### Example 1: Basic Usage
```bash
openclaw invoke my-skill basic-operation --target myresource
```
Expected output: Brief description of what happens

### Example 2: Advanced Usage with Options
```bash
openclaw invoke my-skill operation --flag value --another-flag true
```
Expected output: What the user should see

### Example 3: Integration Pattern
Explain how this skill works with other skills or Claude's capabilities.

## Notes

- **Limitations**: Document any known limitations or edge cases
- **Performance**: Note expected performance characteristics if relevant
- **Dependencies**: Mention if this skill depends on other skills
- **Troubleshooting**: Common issues and how to resolve them
  - Issue: Tool command fails with permission error
  - Solution: Run with elevated permissions or check PATH

- **Security**: If applicable, note security considerations
  - API keys should be stored in environment variables, not in scripts
  - Never commit credentials to version control

- **Configuration**: Optional: Explain configuration files or environment setup
