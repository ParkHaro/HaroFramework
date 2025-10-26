---
title: "Slash Commands Guide"
version: "1.0.0"
scope: "framework"
created: "2025-10-25"
modified: "2025-10-25"
category: "Workflow"
tags: [commands, slash-commands, tools, reference]
paired_document: "commands-guide_KOR.md"
parent_documents:
  - "../../project/SPEC.md"
child_documents: []
references:
  - "./skills-guide.md"
  - "./development-workflow.md"
  - "../guidelines/coding-conventions.md"
status: "approved"
---



<!-- Navigation -->
**🏠 [HaroFramework Project](../../../MASTER_INDEX.md)** | **📂 [Slash Commands Guide](./)** | **⬆️ [HaroFramework Specification](../../project/SPEC.md)**

---
# Slash Commands Guide

Slash commands are **user-invoked** commands that you explicitly call by typing `/command-name`.

## Available Commands

### Component Creation Commands

#### `/component <Name> [namespace]`
Create a MonoBehaviour component with proper structure.

**Arguments:**
- `<Name>`: Component class name (required)
- `[namespace]`: Namespace (default: HaroFramework)

**Example:**
```
/component PlayerController HaroFramework.Player
/component HealthSystem
```

#### `/scriptable <Name> [namespace]`
Create a ScriptableObject class.

**Arguments:**
- `<Name>`: ScriptableObject class name (required)
- `[namespace]`: Namespace (default: HaroFramework.Data)

**Example:**
```
/scriptable GameSettings HaroFramework.Data
/scriptable WeaponData
```

#### `/singleton <Name>`
Create a singleton MonoBehaviour pattern.

**Arguments:**
- `<Name>`: Singleton class name (required)

**Example:**
```
/singleton GameManager
/singleton AudioManager
```

### Project Management Commands

#### `/build [platform]`
Build project for specified platform.

**Arguments:**
- `[platform]`: Target platform (Windows/Mac/Linux/Android/iOS/WebGL)

**Example:**
```
/build Windows
/build Android
/build
```

#### `/test [mode]`
Run Unity Test Framework tests.

**Arguments:**
- `[mode]`: Test mode (EditMode/PlayMode/All, default: All)

**Example:**
```
/test EditMode
/test PlayMode
/test
```

#### `/package-add <package-name>`
Add Unity package to project.

**Arguments:**
- `<package-name>`: Unity package name or URL

**Example:**
```
/package-add com.unity.cinemachine
/package-add com.unity.textmeshpro
```

#### `/asmdef <Name> [Type]`
Create Assembly Definition file.

**Arguments:**
- `<Name>`: Assembly name (required)
- `[Type]`: Assembly type (Runtime/Editor/Tests, default: Runtime)

**Example:**
```
/asmdef HaroFramework.Runtime Runtime
/asmdef HaroFramework.Editor Editor
```

### Analysis & Tools Commands

#### `/scene-analyze <scene-name>`
Analyze Unity scene structure and provide insights.

**Arguments:**
- `<scene-name>`: Scene file name (without .unity extension)

**Example:**
```
/scene-analyze MainMenu
/scene-analyze Level1
```

#### `/input-action <ActionMapName>`
Create Input System action map.

**Arguments:**
- `<ActionMapName>`: Name for the Input Action asset

**Example:**
```
/input-action PlayerControls
/input-action UIControls
```

## Command Syntax

### Argument Types
- `<required>` - Must be provided
- `[optional]` - Can be omitted (uses default)
- `$ARGUMENTS` - All arguments as single string
- `$1, $2, $3...` - Positional parameters

### Examples
```bash
# Required argument
/component PlayerController

# Required + optional
/component PlayerController HaroFramework.Player

# Optional only
/build

# With optional
/build Windows
```

## Creating Custom Commands

Create a `.md` file in `.claude/commands/` directory:

```markdown
---
description: Brief description of the command
argument-hint: <arg1> [arg2]
---

Detailed instructions for Claude.

Use $1 for first argument, $2 for second, or $ARGUMENTS for all.

Include examples and context about when to use this command.
```

### Example Custom Command

**File:** `.claude/commands/my-command.md`

```markdown
---
description: Create a custom game component
argument-hint: <ComponentName>
---

Create a custom game component for HaroFramework.

Component name: $1

Generate a MonoBehaviour with:
1. Proper namespace (HaroFramework.Gameplay)
2. Inspector fields with tooltips
3. Unity lifecycle methods
4. XML documentation

Place in Assets/Scripts/Runtime/Gameplay/
```

## Best Practices

1. **Use Descriptive Names**: Command names should clearly indicate their purpose
2. **Provide Hints**: Use `argument-hint` to show expected arguments
3. **Add Context**: Include when and how to use the command
4. **Use Examples**: Show real usage examples
5. **Keep Focused**: Each command should do one thing well

## When to Use Commands vs Skills

| Scenario | Use Command | Use Skill |
|----------|-------------|-----------|
| Exact control needed | ✅ `/component PlayerController` | ❌ |
| Natural language | ❌ | ✅ "Create a player script" |
| Repeated operation | ✅ `/build Windows` | ❌ |
| Complex task | ❌ | ✅ "Build a health system" |
| Documentation | ✅ `/scene-analyze MainMenu` | ❌ |

## Command Location

Commands are stored in `.claude/commands/` and are automatically:
- Discovered by Claude Code
- Shared via git with team
- Available in command palette (type `/`)

## Related Documentation

- [Skills Guide](./skills-guide.md) - Auto-activated skills reference
- [Development Workflow](./development-workflow.md) - Development process
- [Coding Conventions](../guidelines/coding-conventions.md) - Code standards
- [Claude Code Slash Commands Docs](https://docs.claude.com/en/docs/claude-code/slash-commands)

---

**Document Status**: Approved
**Version**: 1.0.0
**Last Updated**: 2025-10-25
