# Claude Code Skills for HaroFramework

This directory contains **Skills** for Claude Code to enhance Unity development workflows.

## What are Skills?

Skills are **model-invoked** capabilities that Claude automatically activates based on context. Unlike slash commands (user-invoked), Skills are autonomously selected by Claude when your request matches the Skill's description.

## Available Skills

### 🎮 unity-component
**Purpose**: Create well-structured Unity MonoBehaviour components

**Auto-activates when**:
- Creating gameplay scripts (player controllers, enemy AI, managers)
- Building component-based game mechanics
- Implementing Unity lifecycle methods
- Need proper namespace organization and best practices

**Output**: Production-ready MonoBehaviour scripts with proper structure, lifecycle methods, serialization, and documentation.

---

### 📦 unity-scriptable
**Purpose**: Create Unity ScriptableObjects for data-driven design

**Auto-activates when**:
- Creating game configuration data
- Building event systems
- Defining items, characters, or game data
- Need designer-friendly data assets
- Implementing shared runtime data

**Output**: ScriptableObject classes with CreateAssetMenu attributes, validation, and proper organization.

---

### 🛠️ unity-editor
**Purpose**: Create Unity Editor extensions and tools

**Auto-activates when**:
- Building custom inspectors
- Creating property drawers
- Implementing editor windows
- Adding menu items or shortcuts
- Enhancing Unity Editor workflow

**Output**: Editor scripts with custom inspectors, property drawers, editor windows, or menu items that enhance development workflow.

---

### ✅ unity-testing
**Purpose**: Create Unity Test Framework tests

**Auto-activates when**:
- Implementing unit tests
- Creating integration tests
- Setting up Test-Driven Development (TDD)
- Building PlayMode or EditMode tests
- Need automated quality assurance

**Output**: Complete test classes with proper test assembly setup, AAA pattern, and comprehensive coverage.

---

### 🎨 unity-shader
**Purpose**: Create Unity shaders for URP

**Auto-activates when**:
- Creating custom visual effects
- Building shaders (Shader Graph or HLSL)
- Implementing rendering effects
- Need material customization
- Optimizing rendering performance

**Output**: Shader Graph assets or ShaderLab/HLSL code for Universal Render Pipeline with proper URP compatibility.

---

## How Skills Work

### Model-Invoked (Automatic)
Skills activate automatically when Claude detects relevant context:

```
User: "I need a player controller script"
→ Claude automatically uses unity-component skill
→ Creates MonoBehaviour with proper structure
```

### vs. Slash Commands (Manual)
Slash commands require explicit invocation:

```
User: "/component PlayerController"
→ Explicitly runs the component command
```

## Skill Discovery

Claude uses the **description** field in each `SKILL.md` to determine when to activate. Descriptions include:
- What the Skill does
- When to use it
- Context clues for activation

## File Structure

```
.claude/skills/
├── README.md                          # This file
├── unity-component/
│   └── SKILL.md                       # MonoBehaviour creation
├── unity-scriptable/
│   └── SKILL.md                       # ScriptableObject creation
├── unity-editor/
│   └── SKILL.md                       # Editor extensions
├── unity-testing/
│   └── SKILL.md                       # Test creation
└── unity-shader/
    └── SKILL.md                       # Shader development
```

## Creating Custom Skills

To add your own Skills:

1. **Create a directory**: `.claude/skills/your-skill-name/`

2. **Create SKILL.md**:
```markdown
---
name: your-skill-name
description: Brief description of what this does and when to use it
allowed-tools: Read, Write, Edit, Glob, Grep
---

# Your Skill Name

Detailed instructions for Claude...
```

3. **Key points**:
   - **name**: lowercase, hyphens only, max 64 chars
   - **description**: Include WHAT it does and WHEN to use it (max 1024 chars)
   - **allowed-tools**: Optional, restricts tool usage for security

4. **Optional files**:
   - `reference.md` - Additional documentation
   - `examples.md` - Usage examples
   - `scripts/` - Helper scripts
   - `templates/` - Code templates

## Best Practices

### Writing Descriptions
✅ **Good**: "Create MonoBehaviour components with proper Unity lifecycle methods, serialization, and namespace organization. Use when creating gameplay scripts, controllers, or managers."

❌ **Bad**: "Creates Unity scripts."

### Tool Restrictions
```yaml
allowed-tools: Read, Write, Edit, Glob, Grep  # Read/write access
allowed-tools: Read, Grep, Glob                # Read-only
```

### Progressive Context
Claude reads supporting files (reference.md, examples.md) only when needed, optimizing token usage.

## Examples

### Automatic Skill Usage

**Request**: "Create a health system for my game"
- **Activates**: unity-component
- **Reason**: Creating gameplay system (MonoBehaviour)

**Request**: "I need a game settings ScriptableObject"
- **Activates**: unity-scriptable
- **Reason**: Data asset creation

**Request**: "Write tests for the PlayerController"
- **Activates**: unity-testing
- **Reason**: Test creation request

**Request**: "Make a custom inspector for GameSettings"
- **Activates**: unity-editor
- **Reason**: Editor extension request

**Request**: "Create a dissolve shader"
- **Activates**: unity-shader
- **Reason**: Shader/visual effect request

## Resources

- **Official Docs**: [Claude Code Skills Documentation](https://docs.claude.com/en/docs/claude-code/skills)
- **Example Skills**: [Anthropic Skills Repository](https://github.com/anthropics/skills)
- **Unity 6 Docs**: [Unity Documentation](https://docs.unity3d.com/)

## Project Context

These Skills are tailored for:
- **Unity Version**: 6000.2.9f1 (Unity 6)
- **Render Pipeline**: Universal Render Pipeline (URP)
- **Input System**: New Input System (1.14.2)
- **Architecture**: HaroFramework namespace conventions
- **Best Practices**: Unity 6 modern C# patterns

## Sharing Skills

Skills in `.claude/skills/` are automatically shared when you commit to git, making them available to your entire team!

---

**Note**: Skills complement slash commands. Use slash commands for explicit control, rely on Skills for intelligent automation.
