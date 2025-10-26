---
title: HaroFramework Project
version: 1.0.0
scope: framework
created: 2025-10-26
modified: 2025-10-26
category: Master Index
tags: [index, master, navigation, documentation, project-root]
paired_document: MASTER_INDEX_KOR.md
parent_documents: []
child_documents:
  - ./commands/INDEX.md
  - ./skills/INDEX.md
  - ./framework/doc/INDEX.md
  - ./framework/project/index.md
references:
  - ../CLAUDE.md
  - ./framework/project/QUICK_START.md
  - ./framework/project/READING_GUIDE.md
status: active
---



<!-- Navigation -->
**🏠 [HaroFramework Project](MASTER_INDEX.md)** | **📂 [Readme](README.md)** | **⬆️ [Readme](README.md)**

---
# HaroFramework Project

**Reusable Unity 6 Game Framework** with 6-layer architecture, bilingual documentation, and AI-driven development tools.

**Project Version**: 3.0.0 | **Unity**: 6000.2.9f1 | **URP**: 17.2.0 | **Input System**: 1.14.2

---

## 🚀 Quick Start

**New to HaroFramework?**
1. Read [Core Rules](../CLAUDE.md) (5 min)
2. Check [Quick Start Guide](./framework/project/QUICK_START.md) (10 min)
3. Start with [Phase 1 Tasks](./framework/project/todo/phase1-core-foundation/README.md)

**Continue Development?**
- View [TODO Dashboard](./framework/project/todo/PROGRESS.md)
- Check [Reading Guide](./framework/project/READING_GUIDE.md) for efficient document reading
- Review [Session Restoration](./framework/project/SESSION_RESTORE.md)

---

## 📂 Project Structure

### 1. Framework Documentation
**Location**: `.claude/framework/doc/`

Comprehensive documentation covering architecture, guidelines, and workflows.

**Key Documents**:
- [Scope System](./framework/doc/architecture/scope-system.md) - 2-scope architecture (Framework vs Game)
- [Coding Conventions](./framework/doc/guidelines/coding-conventions.md) - Unity 6 best practices
- [Development Workflow](./framework/doc/workflow/development-workflow.md) - 8-step process
- [Documentation Rules](./framework/doc/guidelines/documentation-rules.md) - Bilingual docs system

👉 **[Browse All Framework Docs](./framework/doc/INDEX.md)**

---

### 2. Project Management
**Location**: `.claude/framework/project/`

Project specifications, task tracking, and progress monitoring.

**Key Documents**:
- [Project Index](./framework/project/index.md) - Master project index
- [SPEC Index](./framework/project/spec/README.md) - 10-section specification
- [TODO Index](./framework/project/todo/README.md) - Task tracking system
- [Progress Dashboard](./framework/project/todo/PROGRESS.md) - Real-time progress

**Quick References**:
- [Quick Start Guide](./framework/project/QUICK_START.md) - Scenario-based guides
- [Reading Guide](./framework/project/READING_GUIDE.md) - Token optimization strategies

👉 **[View Project Management](./framework/project/index.md)**

---

### 3. Commands & Skills
**Location**: `.claude/commands/` & `.claude/skills/`

Development tools for Unity workflows - manual commands and auto-activated skills.

#### Commands (Manual Invocation)
Explicit slash commands for precise control.

**Popular Commands**:
- `/component <Name>` - Create MonoBehaviour component
- `/scriptable <Name>` - Create ScriptableObject
- `/test [Mode]` - Run Unity tests
- `/build [Platform]` - Build Unity project

👉 **[All Commands](./commands/INDEX.md)** (9 commands)

#### Skills (Auto-Activation)
AI-driven capabilities activated by natural language.

**Available Skills**:
- `unity-component` - MonoBehaviour creation
- `unity-scriptable` - ScriptableObject creation
- `unity-editor` - Editor extensions
- `unity-testing` - Test generation
- `unity-shader` - URP shader creation

👉 **[All Skills](./skills/INDEX.md)** (5 skills)

---

### 4. Automation Scripts
**Location**: `.claude/framework/scripts/` & `.claude/scripts/`

Validation, automation, and maintenance tools.

**Available Scripts**:
- `scope_validate.py` - Enforce scope dependency rules
- `doc_validate.py` - Validate documentation metadata
- `doc_sync.py` - Check bilingual doc synchronization
- `version_bump.py` - Automated version management
- `add_navigation.py` - Smart navigation generator

**Usage**:
```bash
# Validate scope dependencies
python .claude/scripts/scope_validate.py

# Check documentation
python .claude/scripts/doc_validate.py

# Add navigation to all docs
python .claude/framework/scripts/add_navigation.py --apply-all
```

👉 **[Scripts Documentation](./framework/scripts/README.md)**

---

### 5. Game Projects
**Location**: `.claude/games/`

Game-specific implementations using the framework.

**Structure**:
```
.claude/games/
├── _template/          # Game project template
│   ├── GAME.md         # Game-specific Claude config
│   ├── project/        # SPEC & TODO
│   └── doc/            # Game documentation
│
└── [game-name]/        # Actual game projects
    └── (same structure as template)
```

**Template Includes**:
- GAME.md configuration
- Project structure
- Documentation templates
- Bilingual support

👉 **[Game Template](./games/_template/GAME.md)**

---

## 🎯 Common Tasks

### For Claude Code

#### Starting a New Session
1. Read [Project Index](./framework/project/index.md)
2. Read [TODO Dashboard](./framework/project/todo/PROGRESS.md)
3. Check [Reading Guide](./framework/project/READING_GUIDE.md) for token optimization
4. Continue from last checkpoint in [Session Restoration](./framework/project/SESSION_RESTORE.md)

#### Implementing Core Foundation
1. Read task spec: [Phase 1 Tasks](./framework/project/todo/phase1-core-foundation/README.md)
2. Read SPEC: [Core Systems](./framework/project/spec/05-core-systems/README.md)
3. Follow conventions: [Coding Conventions](./framework/doc/guidelines/coding-conventions.md)
4. Run tests: `/test EditMode`

#### Writing Documentation
1. Read [Documentation Rules](./framework/doc/guidelines/documentation-rules.md)
2. Use bilingual templates
3. Add metadata
4. Validate: `python .claude/scripts/doc_validate.py`

---

### For Developers

#### Learning the Framework
1. **Architecture**: [6-Layer System](./framework/project/spec/02-architecture/6-layer-system.md)
2. **Scope Rules**: [Scope System](./framework/doc/architecture/scope-system.md)
3. **Conventions**: [Coding Conventions](./framework/doc/guidelines/coding-conventions.md)
4. **Workflow**: [Development Workflow](./framework/doc/workflow/development-workflow.md)

#### Creating Components
- **Automatic**: "Create a player health system" → unity-component skill
- **Manual**: `/component HealthSystem HaroFramework.Player`
- **Testing**: "Write tests for HealthSystem" → unity-testing skill

#### Starting a New Game
1. Copy [Game Template](./games/_template/)
2. Update GAME.md configuration
3. Follow [Scope Rules](./framework/doc/architecture/scope-system.md)
4. Games can use Framework, but Framework CANNOT reference Games

---

## 📖 Documentation System

### Bilingual Support
All documentation available in:
- **English**: `*.md` files
- **Korean**: `*_KOR.md` files

**For Claude Code**: Read ONLY English files (token optimization)
**For Developers**: Choose your language preference

### Navigation System
Every document includes smart navigation:
```markdown
🏠 [Home](path) | 📂 [Category](path) | ⬆️ [Parent](path)
```

Navigation shows actual document titles for easy navigation.

### Metadata Standards
All documents include YAML frontmatter:
```yaml
---
title: "Document Title"
version: "1.0.0"
scope: "framework|game"
created: "YYYY-MM-DD"
modified: "YYYY-MM-DD"
paired_document: "filename_KOR.md"
parent_documents: [...]
child_documents: [...]
references: [...]
status: "draft|review|approved|active"
---
```

---

## 🏗️ Architecture Overview

### 2-Scope System
```
Framework Scope (.claude/framework/)
  ✅ Reusable game framework
  ✅ Game-independent
  ❌ CANNOT reference Game scope

Game Scope (.claude/games/[game-name]/)
  ✅ Specific game implementations
  ✅ CAN use Framework
  ✅ CAN reference Framework
```

### 6-Layer Architecture
```
┌─────────────────────────────────────┐
│      Gameplay Layer (Game)          │ ← MonoBehaviour components
├─────────────────────────────────────┤
│      Service Layer                  │ ← Business logic services
├─────────────────────────────────────┤
│      Interface Layer                │ ← Contracts and interfaces
├─────────────────────────────────────┤
│      Core Layer                     │ ← Core systems (EventBus, ServiceLocator)
├─────────────────────────────────────┤
│      Domain Layer                   │ ← Business logic & validation
├─────────────────────────────────────┤
│      Data Layer                     │ ← ScriptableObject data
└─────────────────────────────────────┘
```

**Dependency Flow**: Top → Bottom only (no upward dependencies)

👉 **[Full Architecture Details](./framework/project/spec/02-architecture/6-layer-system.md)**

---

## 📊 Current Status

### Progress
- **Phase 0**: ✅ Documentation setup complete
- **Phase 1**: 🔴 Core Foundation (0/14 tasks) - PENDING
- **Phase 2**: ⏳ Core Modules (TBD)
- **Phase 3**: ⏳ Example Implementation (TBD)
- **Phase 4**: ⏳ Documentation & Testing (TBD)

👉 **[View Progress Dashboard](./framework/project/todo/PROGRESS.md)**

### Documentation
- **Total Files**: 148 (74 EN + 74 KR)
- **SPEC**: 62 files (31 EN + 31 KR)
- **TODO**: 66 files (33 EN + 33 KR)
- **Commands**: 9 files
- **Skills**: 5 files
- **Indexes**: 6 files (3 EN + 3 KR)

### Technology Stack
- **Unity**: 6000.2.9f1 (Unity 6)
- **URP**: 17.2.0 (Universal Render Pipeline)
- **Input System**: 1.14.2 (New Input System)
- **Testing**: Unity Test Framework
- **CI/CD**: Planned

---

## 💡 Best Practices

### For Claude Code
1. **Read Efficiently**: Use [Reading Guide](./framework/project/READING_GUIDE.md) based on context usage
2. **Check TODO**: Always review [TODO Dashboard](./framework/project/todo/PROGRESS.md) before starting
3. **Follow Conventions**: Adhere to [Coding Conventions](./framework/doc/guidelines/coding-conventions.md)
4. **Validate**: Run validation scripts before committing
5. **Document**: Update documentation as you code

### For Developers
1. **Understand Architecture**: Read [6-Layer System](./framework/project/spec/02-architecture/6-layer-system.md)
2. **Respect Scope**: Follow [Scope Rules](./framework/doc/architecture/scope-system.md) strictly
3. **Use Tools**: Leverage commands and skills for productivity
4. **Test Everything**: Aim for >80% test coverage
5. **Document**: Write bilingual documentation

---

## 🔍 Finding Information

### By Topic
- **Architecture**: [6-Layer System](./framework/project/spec/02-architecture/6-layer-system.md)
- **Coding**: [Coding Conventions](./framework/doc/guidelines/coding-conventions.md)
- **Documentation**: [Documentation Rules](./framework/doc/guidelines/documentation-rules.md)
- **Testing**: [Quality Standards](./framework/project/spec/06-quality/code-quality.md)
- **Workflow**: [Development Workflow](./framework/doc/workflow/development-workflow.md)

### By Role
- **New Developer**: Start with [Quick Start](./framework/project/QUICK_START.md)
- **AI Assistant**: Read [Reading Guide](./framework/project/READING_GUIDE.md)
- **Architect**: Review [SPEC Index](./framework/project/spec/README.md)
- **QA**: Check [Testing Guide](./framework/project/spec/06-quality/code-quality.md)

### By Task
- **Create Component**: Use `/component` or natural language
- **Run Tests**: Use `/test` command
- **Build Project**: Use `/build` command
- **Add Package**: Use `/package-add` command

---

## 📞 Support

### Documentation Issues
- Run `python .claude/scripts/doc_validate.py`
- Check [Documentation Rules](./framework/doc/guidelines/documentation-rules.md)
- Review metadata format

### Scope Violations
- Run `python .claude/scripts/scope_validate.py`
- Read [Scope System](./framework/doc/architecture/scope-system.md)
- Fix dependency direction

### Build Errors
- Check Unity version (6000.2.9f1)
- Verify package versions
- Review [Technology Stack](./framework/project/spec/07-tech-stack/unity-environment.md)

---

## 🎓 Learning Path

### Beginner (0-2 hours)
1. [Core Rules](../CLAUDE.md) - 5 min
2. [Quick Start](./framework/project/QUICK_START.md) - 10 min
3. [Scope System](./framework/doc/architecture/scope-system.md) - 15 min
4. [Coding Conventions](./framework/doc/guidelines/coding-conventions.md) - 30 min
5. Try creating a component with `/component` - 15 min

### Intermediate (2-8 hours)
1. [6-Layer Architecture](./framework/project/spec/02-architecture/6-layer-system.md) - 1 hour
2. [Core Systems SPEC](./framework/project/spec/05-core-systems/README.md) - 2 hours
3. Implement [Phase 1 Tasks](./framework/project/todo/phase1-core-foundation/README.md) - 4 hours
4. Write tests with unity-testing skill - 1 hour

### Advanced (8+ hours)
1. Complete Core Foundation (Phase 1) - 8 hours
2. Implement Core Modules (Phase 2) - 10 hours
3. Create example game (Phase 3) - 12 hours
4. Full documentation & testing (Phase 4) - 6 hours

---

**Document Status**: Active
**Maintained By**: HaroFramework Team
**Last Updated**: 2025-10-26
**Total Files**: 148 documentation files

**Welcome to HaroFramework! 🎮**
