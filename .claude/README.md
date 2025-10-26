<!-- Navigation -->
**🏠 [HaroFramework Project](MASTER_INDEX.md)** | **📂 [Readme](README.md)** | **⬆️ [Readme](README.md)**

---


# .claude Directory

Claude Code configuration for **HaroFramework** Unity project.

## 📁 Directory Structure

```
.claude/
├── README.md                    # This file - overview
├── doc/                         # 📚 Comprehensive documentation
│   ├── README.md               # Documentation index
│   ├── project-overview.md     # Project architecture
│   ├── coding-conventions.md   # Code standards
│   ├── development-workflow.md # Development processes
│   ├── skills-guide.md         # Skills reference
│   └── commands-guide.md       # Commands reference
├── commands/                    # Slash commands (user-invoked)
│   └── *.md
└── skills/                      # Skills (auto-activated)
    └── */SKILL.md
```

## 📚 Documentation

**All detailed documentation is in the `doc/` folder.**

### Quick Links

- **[Documentation Index](doc/README.md)** - Start here for complete documentation guide
- **[Project Overview](doc/project-overview.md)** - Architecture and technologies
- **[Coding Conventions](doc/coding-conventions.md)** - Code standards
- **[Development Workflow](doc/development-workflow.md)** - Development process
- **[Skills Guide](doc/skills-guide.md)** - Auto-activated capabilities
- **[Commands Guide](doc/commands-guide.md)** - Manual commands

## 🚀 Quick Start

### For Development Tasks

1. **Read documentation first**: See `doc/README.md` for reading order
2. **Use Skills**: Natural language activates appropriate Skills automatically
3. **Use Commands**: Type `/` for explicit command invocation

### Skills vs Commands

| Type | Invocation | Example |
|------|------------|---------|
| **Skills** | Automatic | "Create a player controller" |
| **Commands** | Manual | `/component PlayerController` |

## 🎮 Unity Development Tools

### Auto-Activated Skills
- **unity-component**: MonoBehaviour creation
- **unity-scriptable**: ScriptableObject creation
- **unity-editor**: Editor extensions
- **unity-testing**: Test creation
- **unity-shader**: Shader development

### Manual Commands
- `/component` - Create MonoBehaviour
- `/scriptable` - Create ScriptableObject
- `/test` - Run tests
- `/build` - Build project
- `/asmdef` - Create Assembly Definition
- And more... (see `doc/commands-guide.md`)

## 📖 Documentation Philosophy

This configuration follows a **documentation-first approach**:

1. **CLAUDE.md** (root) - Core rules only
2. **`.claude/doc/`** - All detailed documentation
3. **Skills/Commands** - Specialized instructions

**Before any work**: Read relevant documentation from `doc/` folder.

## 🔗 Resources

- **Local Documentation**: [.claude/doc/](doc/)
- **Claude Code Docs**: [docs.claude.com/claude-code](https://docs.claude.com/en/docs/claude-code)
- **Skills Documentation**: [docs.claude.com/claude-code/skills](https://docs.claude.com/en/docs/claude-code/skills)
- **Commands Documentation**: [docs.claude.com/claude-code/slash-commands](https://docs.claude.com/en/docs/claude-code/slash-commands)
- **Unity 6 Documentation**: [docs.unity3d.com](https://docs.unity3d.com/)

---

**Note**: This directory is version controlled and shared with the team. All configuration is automatically available when the repository is cloned.
