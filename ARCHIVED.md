# Archived

This repository has been **archived**. Its functionality has been merged into [`create-effector`](https://github.com/effectorHQ/create-effector).

## Why

`plugin-template` was a GitHub template repo for creating skills. `create-effector` now serves this purpose with:

- Interactive scaffolding: `npx create-effector my-skill --type skill`
- Support for all 6 effector types (skill, extension, workflow, workspace, bridge, prompt)
- Built-in example skills (merged from this repo's `examples/` directory)
- Generates `effector.toml` manifests automatically

## Migration

Use `create-effector` instead:

```bash
npx create-effector my-skill --type skill
```

Or copy the reference implementation: [linear-skill](https://github.com/effectorHQ/linear-skill)
