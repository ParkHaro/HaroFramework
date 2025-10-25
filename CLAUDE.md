# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## ⚠️ CRITICAL: 2-Scope Architecture

HaroFramework uses a **strict 2-scope architecture**:

- **Framework Scope** (`.claude/framework/`): Reusable game framework
- **Game Scope** (`.claude/games/[game-name]/`): Specific game implementations

### Scope Dependency Rules
```
✅ ALLOWED:    Game → Framework (games can use framework)
❌ FORBIDDEN:  Framework → Game (framework CANNOT reference any game)
```

**Why this matters**: Framework must remain reusable across all games. Breaking this rule makes the framework coupled to specific games.

---

## 📚 IMPORTANT: Read Documentation First

### Framework Documentation (MUST READ)

**Before starting any work, read these documents from `.claude/framework/doc/`:**

#### Architecture & Guidelines (Read First)
1. **`doc/architecture/scope-system.md`** - 2-scope architecture details and dependency rules
2. **`doc/architecture/project-overview.md`** - Project structure, architecture, and technologies
3. **`doc/guidelines/coding-conventions.md`** - Naming conventions, code structure, Unity best practices
4. **`doc/guidelines/documentation-rules.md`** - Bilingual documentation system and metadata standards

#### Workflow & Tools
5. **`doc/workflow/development-workflow.md`** - Standard development workflow
6. **`doc/workflow/skills-guide.md`** - Auto-activated capabilities for Unity development
7. **`doc/workflow/commands-guide.md`** - Manual slash commands reference

#### Project Management
- **`project/SPEC.md`** - Comprehensive project specification
- **`project/TODO.md`** - Current tasks and progress tracking

### Documentation Reading Guidelines

**For Claude Code**:
- ✅ **Read ONLY English documents** (`.md` files)
- ❌ **Do NOT read Korean translations** (`_KOR.md` files)
- Reason: Saves ~50% context tokens, original documents are source of truth

**For Developers**:
- Choose language preference (English `.md` or Korean `_KOR.md`)
- Both versions contain identical information

---

## Core Rules

### 1. Documentation-First Approach
- **ALWAYS** read relevant documentation from `.claude/framework/doc/` before writing code
- Follow conventions in `coding-conventions.md`
- Reference `project-overview.md` for architecture decisions
- Understand scope boundaries from `scope-system.md`

### 2. Scope Awareness
**When writing code, ask yourself**:
- Am I in Framework or Game scope?
- If Framework: Does this reference any game-specific code? (Must be NO)
- If Game: Can I use Framework utilities? (Yes, encouraged)

### 3. Namespace Convention
```csharp
// Framework code
namespace HaroFramework.[Category]
{
    // All framework code MUST be in HaroFramework namespace
}

// Game code
namespace [GameName].[Category]
{
    // Game-specific code uses game name as root namespace
}
```

**Framework Categories**: `Core`, `Player`, `AI`, `UI`, `Audio`, `Gameplay`, `Systems`, `Data`, `Editor`, `Tests`

### 4. Code Structure
- Use **regions** for organization: `#region Inspector Fields`, `#region Unity Lifecycle`, etc.
- Private fields: `_camelCase` with underscore
- Public properties: `PascalCase`
- Cache component references in `Awake()`

### 5. Unity 6 Specific
- Use `FindFirstObjectByType<T>()` instead of deprecated `FindObjectOfType<T>()`
- MonoBehaviour (not Behavior) - Unity 6 spelling
- Universal Render Pipeline (URP) is active - use URP-compatible shaders

### 6. Testing Required
- Write tests for new functionality
- Use `/test` command to run tests
- Tests located in `Assets/Scripts/Tests/`

### 7. Documentation Required
- Add XML documentation (`///`) for public APIs
- Include `[Tooltip]` for serialized fields
- Add `[Header]` for inspector organization
- Follow bilingual documentation rules for `.md` files

---

## Quick Reference

### Unity Version
- **Unity**: 6000.2.9f1 (Unity 6)
- **URP**: 17.2.0
- **Input System**: 1.14.2 (New Input System - use this, not legacy)

### Key Commands
```bash
/test           # Run tests
/build          # Build project
/component      # Create MonoBehaviour
/scriptable     # Create ScriptableObject
```

### Skills (Auto-Activated)
Skills automatically activate based on your natural language request:
- **unity-component**: Creates MonoBehaviour components
- **unity-scriptable**: Creates ScriptableObjects
- **unity-editor**: Creates editor extensions
- **unity-testing**: Creates tests
- **unity-shader**: Creates URP shaders

---

## File Locations

### Scripts Organization
```
Assets/Scripts/
├── Runtime/         # Runtime code (to be organized with .asmdef)
├── Editor/          # Editor-only code
└── Tests/           # Test code
    ├── EditMode/    # Edit mode tests
    └── PlayMode/    # Play mode tests
```

### Framework Documentation (NEW STRUCTURE)
```
.claude/framework/
├── project/
│   ├── SPEC.md                         # Project specification
│   ├── SPEC_KOR.md                     # Korean translation
│   ├── TODO.md                         # Task tracking
│   └── TODO_KOR.md                     # Korean translation
├── doc/
│   ├── architecture/
│   │   ├── scope-system.md             # 2-scope architecture
│   │   ├── scope-system_KOR.md
│   │   ├── project-overview.md         # Project structure
│   │   └── project-overview_KOR.md
│   ├── guidelines/
│   │   ├── coding-conventions.md       # Code standards
│   │   ├── coding-conventions_KOR.md
│   │   ├── documentation-rules.md      # Documentation system
│   │   └── documentation-rules_KOR.md
│   └── workflow/
│       ├── development-workflow.md     # Development process
│       ├── development-workflow_KOR.md
│       ├── skills-guide.md             # Skills reference
│       ├── skills-guide_KOR.md
│       ├── commands-guide.md           # Commands reference
│       └── commands-guide_KOR.md
└── scripts/                            # Automation scripts (TBD)
    ├── scope_validate.py
    ├── doc_validate.py
    ├── doc_sync.py
    └── version_bump.py
```

### Game Projects (Future)
```
.claude/games/
├── _template/                          # Template for new games
│   └── [project structure]
└── [game-name]/                        # Specific game project
    ├── project/
    │   ├── GAME.md                     # Game specification
    │   ├── SPEC.md                     # Game-specific spec
    │   └── TODO.md                     # Game tasks
    └── doc/                            # Game-specific documentation
```

---

## Workflow Summary

1. **Read** framework documentation from `.claude/framework/doc/`
2. **Understand** which scope you're working in (Framework vs Game)
3. **Plan** approach based on conventions and scope boundaries
4. **Implement** following coding standards
5. **Test** with `/test` command
6. **Validate** code follows conventions and scope rules
7. **Document** with XML comments and update .md files if needed

---

## Git Commit Guidelines

### Commit Message Format
Follow conventional commits format:
```
<type>(<scope>): <subject>

<body>
```

**Types**: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

### IMPORTANT: Commit Message Rules
- ❌ **DO NOT include** `Generated with [Claude Code]` footer
- ❌ **DO NOT include** `Co-Authored-By: Claude` attribution
- ✅ **DO include** clear, concise descriptions of changes
- ✅ **DO use** conventional commit format

**Reason**: Keep commit history clean and focused on actual changes, not tooling attribution.

### Examples
```bash
# Good commit message
feat: Add player health system

Implement health management with damage calculation:
- Add HealthComponent with configurable max health
- Implement damage reduction based on armor
- Add death event system for game over handling

# Bad commit message (don't do this)
feat: Add player health system

🤖 Generated with [Claude Code](https://claude.com/claude-code)
Co-Authored-By: Claude <noreply@anthropic.com>
```

---

## When in Doubt

### For Code Standards
1. Check `.claude/framework/doc/guidelines/coding-conventions.md`
2. Check `.claude/framework/doc/architecture/project-overview.md`
3. Check `.claude/framework/doc/workflow/development-workflow.md`

### For Architecture Questions
1. Check `.claude/framework/doc/architecture/scope-system.md`
2. Check `.claude/framework/project/SPEC.md`
3. Ask clarifying questions if requirements are unclear

### For Scope Boundary Questions
**Ask yourself**:
- Is this Framework code trying to reference Game code? → **STOP, redesign**
- Is this Game code using Framework utilities? → **OK, proceed**
- Not sure which scope? → **Check `scope-system.md`**

---

## Context Management for Claude Code

### Token Optimization
- Read **ONLY** English `.md` files (skip `_KOR.md` translations)
- Use incremental context loading (read only what you need)
- When context reaches 85% (170K/200K tokens):
  - Update SPEC.md and TODO.md with current progress
  - Use `/clear` to reset context
  - Resume from updated SPEC.md and TODO.md

### Session Restoration
If starting a new session:
1. Read `.claude/framework/project/SPEC.md`
2. Read `.claude/framework/project/TODO.md`
3. Read task-specific documentation as needed
4. Continue from "🔴 Currently In Progress" section in TODO.md

---

**Remember**:
- This file contains only core rules and structure overview
- **All detailed documentation is in `.claude/framework/doc/`** and must be consulted before starting work
- **Respect the 2-scope architecture** - Framework NEVER references Game code
- **Read English documents only** to optimize context usage
