---
name: hello-world
description: "A simple example skill that requires no dependencies. Perfect for learning the skill format."
metadata:
  openclaw:
    emoji: 👋
---

## Purpose

This is the simplest possible OpenClaw skill. It demonstrates the minimal required structure and format with no external dependencies.

Use this as a reference when creating your first skill or to understand the basics of the SKILL.md format.

## When to Use

- Learning the OpenClaw skill format
- Testing your local skill setup
- Creating a proof-of-concept skill

## When NOT to Use

This is an example only. It doesn't provide real functionality—use it as a template, not as a dependency.

## Setup

No setup required! This skill has no dependencies.

### Local Testing

```bash
# Copy to your skills directory
cp -r examples/hello-world ~/.openclaw/workspace/skills/hello-world

# Verify it appears in the list
openclaw skills list

# You can reference it in Claude conversations
```

## Commands / Actions

This example skill doesn't define any commands—it's purely a reference implementation.

## Examples

In a Claude conversation, you might reference this skill like:

```
I want to learn about OpenClaw skills. Can you explain the hello-world example skill?
```

Claude can then look at this skill's SKILL.md to understand the minimal format required.

## Notes

- **No dependencies**: This skill requires no installation
- **Educational purpose**: Use as a template for your own skills
- **Minimal frontmatter**: Demonstrates the smallest valid skill structure
- **Reference only**: Replace this content with your own skill implementation

## Next Steps

Once you understand this example:

1. Check out `examples/api-connector/SKILL.md` for a more complex example
2. Edit `SKILL.md` in the root directory with your own skill
3. Test locally by copying to `~/.openclaw/workspace/skills/my-skill`
4. Publish to ClawHub with `clawhub publish`
