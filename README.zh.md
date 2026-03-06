# OpenClaw Skill 模板

[![使用此模板](https://img.shields.io/badge/use%20this-template-0075ca?logo=github)](https://github.com/effectorHQ/plugin-template/generate) [![CI](https://github.com/effectorHQ/plugin-template/actions/workflows/ci.yml/badge.svg)](https://github.com/effectorHQ/plugin-template/actions) [![ClawHub](https://img.shields.io/badge/publish%20to-ClawHub-E03E3E)](https://clawhub.com) [![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)

**[English →](./README.md)**

一个创建 OpenClaw Skill 的起始模板。**Skills** 是带有 YAML frontmatter 的语言无关 Markdown 文件，通过提供对工具、API 和外部系统的访问来扩展 OpenClaw 的能力。

**Fork 此 repo**，开始构建你自己的 skill。每一条 claw 都能延伸触达。

## 什么是 OpenClaw Skill？

OpenClaw Skill 是一个 Markdown 文件（`SKILL.md`），包含：

- **YAML frontmatter**：metadata（name、description、依赖、安装说明）
- **Markdown body**：描述用途、用法、命令和示例的文档

Skills 通过 **ClawHub 注册中心**分发，安装到本地 `~/.openclaw/workspace/skills/<skill-name>/` 目录。它们让 OpenClaw 能够与外部系统交互，无需代码部署或复杂的 plugin 基础设施。

## 快速开始

### 1. 使用此模板

在 GitHub 上点击 **"Use this template"** 按钮，基于此模板创建新 repo。

### 2. Clone 你的 repo

```bash
git clone https://github.com/YOUR_USERNAME/my-skill.git
cd my-skill
```

### 3. 编辑模板

修改 `SKILL.md`，填入你的 skill metadata 和文档：

```yaml
---
name: my-skill
description: "这个 skill 的功能，以及何时使用它。"
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
        label: "通过 Homebrew 安装"
---

## Purpose
...
```

### 4. 本地测试

```bash
# 安装到本地 skills 目录
cp -r . ~/.openclaw/workspace/skills/my-skill

# 验证加载
openclaw skills list | grep my-skill

# 测试调用
openclaw invoke my-skill --help
```

### 5. 发布到 ClawHub

```bash
# 在 skill 目录内执行
clawhub publish

# 验证发布成功
clawhub search my-skill
```

## 文件结构

```
my-skill/
├── SKILL.md          # 包含 frontmatter 和文档的主 skill 文件
├── README.md         # 英文 README
├── README.zh.md      # 中文 README（本文件）
├── CHANGELOG.md      # 版本历史
├── LICENSE           # MIT License
├── .github/
│   └── workflows/
│       └── ci.yml    # GitHub Actions 验证
└── examples/         # 示例 skill 实现
    ├── hello-world/
    │   └── SKILL.md
    └── api-connector/
        └── SKILL.md
```

## SKILL.md 格式参考

### Frontmatter 字段

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `name` | string | 是 | 唯一 skill 标识符（kebab-case） |
| `description` | string | 是 | skill 用途的单行描述 |
| `metadata.openclaw.emoji` | string | 否 | UI 展示用的单个 emoji |
| `metadata.openclaw.requires.bins` | array | 否 | 需要的可执行文件/二进制 |
| `metadata.openclaw.requires.env` | array | 否 | 需要的环境变量 |
| `metadata.openclaw.install` | array | 否 | 安装方式（brew、apt、manual） |

### 安装方式

定义用户应如何安装你的 skill 依赖：

```yaml
install:
  - id: brew
    kind: brew
    formula: package-name        # Homebrew 包名
    bins: [binary-name]          # 需要验证的目标二进制文件
    label: "通过 Homebrew 安装"

  - id: apt
    kind: apt
    package: package-name        # APT 包名
    bins: [binary-name]
    label: "通过 APT 安装"

  - id: manual
    kind: manual
    label: "手动安装"
    steps:
      - "第 1 步：..."
      - "第 2 步：..."
```

### Markdown Body 结构

SKILL.md body 的推荐章节：

1. **Purpose**：skill 的功能
2. **When to Use**：适合使用的具体场景
3. **When NOT to Use**：不适合使用此 skill 的场景
4. **Setup**：前置条件和本地测试说明
5. **Commands / Actions**：可用操作
6. **Examples**：可直接复制的示例
7. **Notes**：限制、安全性、故障排查

## 验证

本模板包含 GitHub Actions（`.github/workflows/ci.yml`），会自动验证：

- `SKILL.md` 文件存在
- YAML frontmatter 语法正确
- 必填字段（`name`、`description`）存在
- 所有引用的二进制文件有效

每次 push 和 PR 时都会运行验证。推荐使用 [skill-lint-action](https://github.com/effectorHQ/skill-lint-action) 获得更完整的检查和 PR 行内标注：

```yaml
- uses: effectorHQ/skill-lint-action@v1
  with:
    fail-on-warnings: 'true'
```

## 发布到 ClawHub

skill 完成后：

1. 更新 `CHANGELOG.md`
2. 确保 `SKILL.md` 包含所有必填字段
3. push 到 repo 并打 release 标签（如 `v1.0.0`）
4. 运行 `clawhub publish` 提交到注册中心
5. （可选）向 [awesome-openclaw](https://github.com/effectorHQ/awesome-openclaw) 提交 PR

## 最佳实践

- **清晰的描述**：用一句话说清 skill 的功能
- **真实示例**：提供用户可以直接复制使用的示例
- **记录限制**：说明 skill 不能做什么
- **本地测试**：发布前总是在 `~/.openclaw/workspace/skills/` 中测试
- **语义化版本**：在 `CHANGELOG.md` 中遵循 SEMVER
- **安全性**：永远不要在 skill 里存储凭证，使用环境变量

## 资源

- **OpenClaw 文档**：https://docs.openclaw.io
- **ClawHub 注册中心**：https://clawhub.com
- **贡献指南**：https://github.com/effectorHQ/.github/blob/main/CONTRIBUTING.md
- **参考实现**：https://github.com/effectorHQ/linear-skill（零 lint 错误的生产级 skill 示例）

## License

MIT License。详见 [LICENSE](LICENSE)。

---

由 [OpenClaw Skill 模板](https://github.com/effectorHQ/plugin-template)构建。每一条 claw 都能延伸触达。
