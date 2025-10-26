---
title: "Skills Guide"
version: "1.0.0"
scope: "framework"
created: "2025-10-25"
modified: "2025-10-25"
category: "Workflow"
tags: [skills, automation, tools, reference, ai]
paired_document: "skills-guide_KOR.md"
parent_documents:
  - "../../project/SPEC.md"
child_documents: []
references:
  - "./commands-guide.md"
  - "./development-workflow.md"
  - "../guidelines/coding-conventions.md"
status: "approved"
---



<!-- Navigation -->
**🏠 [HaroFramework Project](../../../MASTER_INDEX.md)** | **📂 [Skills Guide](./)** | **⬆️ [HaroFramework Specification](../../project/SPEC.md)**

---
# Skills Guide

Skills are **model-invoked** capabilities that Claude automatically activates based on context.

## What are Skills?

Unlike slash commands (which you invoke manually), Skills are:
- **Automatic**: Claude decides when to use them
- **Context-aware**: Activated based on your natural language request
- **Specialized**: Each Skill is an expert in its domain
- **Production-ready**: Generate high-quality, complete code

## Available Skills

### 🎮 unity-component

**Purpose**: Create well-structured Unity MonoBehaviour components.

**Auto-activates when you request:**
- Player controllers
- Enemy AI scripts
- Game managers
- UI controllers
- Gameplay mechanics
- Component-based systems

**Examples that trigger this Skill:**
- "Create a player movement controller"
- "I need a health system"
- "Build an enemy AI component"
- "Make a game manager singleton"

**Generated code includes:**
- Proper namespace organization
- Unity lifecycle methods (Awake, Start, Update, etc.)
- Serialized fields with tooltips
- Region organization
- XML documentation
- Performance best practices
- Unity 6 compatibility

---

### 📦 unity-scriptable

**Purpose**: Create Unity ScriptableObjects for data-driven design.

**Auto-activates when you request:**
- Game configuration data
- Event systems
- Item definitions
- Character stats
- Shared data assets
- Settings management

**Examples that trigger this Skill:**
- "Create a game settings ScriptableObject"
- "I need a weapon data asset"
- "Build an event system"
- "Make a character stats data structure"

**Generated code includes:**
- CreateAssetMenu attributes
- OnValidate for data integrity
- Proper namespace (HaroFramework.Data)
- Inspector organization
- XML documentation
- Usage examples

---

### 🛠️ unity-editor

**Purpose**: Create Unity Editor extensions and custom tools.

**Auto-activates when you request:**
- Custom inspectors
- Property drawers
- Editor windows
- Menu items
- Scene view tools
- Asset processors

**Examples that trigger this Skill:**
- "Create a custom inspector for GameManager"
- "I need a property drawer for my struct"
- "Build an editor window for level management"
- "Add a menu item to create prefabs"

**Generated code includes:**
- Custom Editor classes
- Property drawer implementations
- Editor window layouts
- Undo/Redo support
- Multi-object editing support
- Scene GUI integration

---

### ✅ unity-testing

**Purpose**: Create Unity Test Framework tests.

**Auto-activates when you request:**
- Unit tests
- Integration tests
- PlayMode tests
- EditMode tests
- Test-Driven Development setup
- Test coverage

**Examples that trigger this Skill:**
- "Write tests for the PlayerController"
- "Create unit tests for the damage system"
- "I need PlayMode tests for scene loading"
- "Set up TDD for this feature"

**Generated code includes:**
- Test assembly definitions
- EditMode and PlayMode tests
- AAA pattern (Arrange, Act, Assert)
- Test helpers and utilities
- Performance tests
- Proper test naming conventions

---

### 🎨 unity-shader

**Purpose**: Create Unity shaders for Universal Render Pipeline.

**Auto-activates when you request:**
- Visual effects
- Custom shaders
- Shader Graph creation
- Material effects
- Post-processing
- Rendering optimizations

**Examples that trigger this Skill:**
- "Create a dissolve shader effect"
- "I need a hologram shader"
- "Build a water shader for URP"
- "Make a toon shading effect"

**Generated code includes:**
- URP-compatible shaders
- Shader Graph setups
- HLSL custom functions
- Proper lighting integration
- Shadow support
- Performance optimizations

---

## How Skills Activate

Skills use their **description** field to determine when to activate. Claude analyzes your request and matches it against Skill descriptions.

### Activation Flow

```
User: "Create a player health system"
    ↓
Claude analyzes request
    ↓
Matches: unity-component skill
    ↓
Loads skill instructions
    ↓
Generates MonoBehaviour component
    ↓
Returns production-ready code
```

## Skills vs Commands Comparison

| Feature | Skills | Slash Commands |
|---------|--------|----------------|
| **Invocation** | Automatic by Claude | Manual by user (`/cmd`) |
| **Usage** | Natural language | Explicit command |
| **Flexibility** | High - adapts to context | Fixed - specific operation |
| **Discovery** | AI-driven | User must know command |
| **Best for** | Complex, contextual tasks | Quick, specific operations |

### Example Comparison

**Want to create a player controller:**

**Using Skill (Recommended):**
```
"I need a player controller with movement and jumping"
→ Claude uses unity-component skill
→ Generates complete controller with your requirements
```

**Using Command (Alternative):**
```
/component PlayerController HaroFramework.Player
→ Generates basic component template
→ You specify additional requirements separately
```

## Skill Files Structure

Each Skill is a directory in `.claude/skills/` containing:

```
.claude/skills/
└── skill-name/
    ├── SKILL.md           # Required: Main instructions
    ├── reference.md       # Optional: Reference docs
    ├── examples.md        # Optional: Code examples
    ├── scripts/           # Optional: Helper scripts
    └── templates/         # Optional: Code templates
```

### SKILL.md Format

```markdown
---
name: skill-name
description: What this skill does and when Claude should use it. This is critical for activation!
allowed-tools: Read, Write, Edit, Glob, Grep
---

# Skill Name

## When to Use This Skill

Detailed activation criteria...

## Instructions

Step-by-step instructions for Claude...

## Best Practices

Guidelines and standards...

## Output Format

Expected output structure...
```

## Creating Custom Skills

### 1. Create Directory Structure
```bash
mkdir -p .claude/skills/my-skill
```

### 2. Create SKILL.md

**Good Description (activates reliably):**
```yaml
description: Create inventory systems with item management, storage, and UI integration. Use when implementing item collection, equipment, or crafting systems.
```

**Bad Description (won't activate):**
```yaml
description: Inventory stuff
```

### 3. Write Clear Instructions

Include:
- When to activate
- What to generate
- Code standards to follow
- Examples and patterns
- Output format expectations

### 4. Test Activation

Try natural language requests that should trigger your Skill:
- "Create an inventory system"
- "I need item management"
- "Build a crafting system"

## Best Practices

### For Skill Descriptions
1. **Include "What"**: What does this Skill do?
2. **Include "When"**: When should Claude use it?
3. **Be Specific**: Use domain keywords
4. **Keep Concise**: Max 1024 characters
5. **Use Examples**: Include use case examples

### For Skill Instructions
1. **Be Explicit**: Don't assume knowledge
2. **Provide Templates**: Include code structure
3. **Show Patterns**: Demonstrate conventions
4. **Explain Context**: Why things are done this way
5. **Include Validation**: How to verify correctness

### For Tool Restrictions
```yaml
# Read/write access (default)
allowed-tools: Read, Write, Edit, Glob, Grep

# Read-only (for analysis skills)
allowed-tools: Read, Grep, Glob

# Specific tools only
allowed-tools: Read, Edit
```

## Progressive Context Loading

Claude loads Skill files progressively:
1. **SKILL.md** - Always loaded first
2. **reference.md** - Loaded when more detail needed
3. **examples.md** - Loaded when examples requested
4. **Other files** - Loaded on-demand

This optimizes token usage while maintaining rich context.

## Debugging Skills

### Skill Not Activating?

**Check:**
1. Description mentions relevant keywords
2. Description explains WHEN to use it
3. Skill name matches directory name
4. SKILL.md has valid YAML frontmatter
5. Request uses domain terminology

### Skill Generates Wrong Output?

**Review:**
1. Instructions are clear and explicit
2. Code templates are correct
3. Examples match desired output
4. Context about project structure included

## Related Documentation

- [Commands Guide](./commands-guide.md) - Manual slash commands reference
- [Development Workflow](./development-workflow.md) - Development process
- [Coding Conventions](../guidelines/coding-conventions.md) - Code standards
- [Claude Code Skills](https://docs.claude.com/en/docs/claude-code/skills) - Official documentation
- [Anthropic Skills Repo](https://github.com/anthropics/skills) - Example skills

---

**Document Status**: Approved
**Version**: 1.0.0
**Last Updated**: 2025-10-25
