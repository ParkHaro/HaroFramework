---
title: Framework Documentation Index
version: 1.0.0
scope: framework
created: 2025-10-26
modified: 2025-10-26
category: Documentation
tags: [index, documentation, framework, reference]
paired_document: INDEX_KOR.md
parent_documents:
  - ../../MASTER_INDEX.md
child_documents:
  - ./architecture/scope-system.md
  - ./architecture/project-overview.md
  - ./guidelines/coding-conventions.md
  - ./guidelines/documentation-rules.md
  - ./workflow/development-workflow.md
  - ./workflow/skills-guide.md
  - ./workflow/commands-guide.md
  - ./reference/UNITY_FRAMEWORK_SPEC.md
references: []
status: active
---



<!-- Navigation -->
**🏠 [HaroFramework Project](../../MASTER_INDEX.md)** | **📂 [Framework Documentation Index](INDEX.md)** | **⬆️ [HaroFramework Project](../../MASTER_INDEX.md)**

---
# Framework Documentation Index

Core documentation for HaroFramework development - architecture, guidelines, and workflows.

**Total Documents**: 8 files (4 English + 4 Korean per category)

---

## 📂 Quick Navigation

| Category | Files | When to Read |
|----------|-------|--------------|
| [Architecture](#architecture) | 2 | Understanding system structure |
| [Guidelines](#guidelines) | 2 | Writing code or documentation |
| [Workflow](#workflow) | 3 | Following development process |
| [Reference](#reference) | 1 | Technical specifications |

---

## 🏗️ Architecture

**When to read**: Before implementing features, when understanding project structure

### [scope-system.md](./architecture/scope-system.md)
**Purpose**: 2-scope architecture (Framework vs Game)

**Key Concepts**:
- Framework ❌ Game (Framework CANNOT reference Game)
- Game ✅ Framework (Game CAN use Framework)
- Enforcement via `scope_validate.py`
- Reusability through scope isolation

**Read when**:
- Starting a new feature
- Unclear about dependency direction
- Adding game-specific code

---

### [project-overview.md](./architecture/project-overview.md)
**Purpose**: Project structure and technology stack

**Key Concepts**:
- 6-layer architecture overview
- Folder structure
- Naming conventions
- Technology stack (Unity 6, URP, Input System)

**Read when**:
- First time in project
- Navigating codebase
- Setting up development environment

---

## 📝 Guidelines

**When to read**: Before writing code or documentation

### [coding-conventions.md](./guidelines/coding-conventions.md)
**Purpose**: Unity 6 C# coding standards

**Key Standards**:
- Naming conventions (PascalCase, _camelCase)
- Region organization (`#region Inspector Fields`)
- Unity 6 API usage (FindFirstObjectByType)
- XML documentation requirements
- MonoBehaviour lifecycle patterns

**Read when**:
- Writing new scripts
- Code review
- Unsure about naming or structure

---

### [documentation-rules.md](./guidelines/documentation-rules.md)
**Purpose**: Bilingual documentation system

**Key Rules**:
- Every `.md` has paired `_KOR.md`
- YAML metadata required
- Version management (semantic versioning)
- Link validation
- Automation scripts usage

**Read when**:
- Creating new documentation
- Updating existing docs
- Documentation validation errors

---

## 🔄 Workflow

**When to read**: Following development process

### [development-workflow.md](./workflow/development-workflow.md)
**Purpose**: 8-step development process

**Process**:
1. Plan → 2. Design → 3. Implement → 4. Test → 5. Document → 6. Review → 7. Integrate → 8. Validate

**Read when**:
- Starting new task
- Unsure about process
- Quality gates needed

---

### [skills-guide.md](./workflow/skills-guide.md)
**Purpose**: Auto-activated AI capabilities

**Skills**:
- unity-component (MonoBehaviour)
- unity-scriptable (ScriptableObject)
- unity-editor (Editor extensions)
- unity-testing (Tests)
- unity-shader (URP shaders)

**Read when**:
- Using natural language for development
- Understanding skill activation
- Creating custom skills

---

### [commands-guide.md](./workflow/commands-guide.md)
**Purpose**: Manual slash commands

**Commands**:
- `/component`, `/scriptable`, `/singleton`
- `/test`, `/build`, `/asmdef`
- `/scene-analyze`, `/package-add`, `/input-action`

**Read when**:
- Need explicit control
- Repeating specific patterns
- Creating custom commands

---

## 📚 Reference

**When to read**: Technical specifications needed

### [UNITY_FRAMEWORK_SPEC.md](./reference/UNITY_FRAMEWORK_SPEC.md)
**Purpose**: Original Unity framework specification

**Contents**:
- Complete framework design
- Technical architecture details
- Implementation patterns

**Read when**:
- Deep architectural questions
- Historical context needed
- Technical decisions unclear

---

## 🎯 Reading Strategies

### For Claude Code

**Context < 30%**: Read comprehensively
- Start with architecture
- Review guidelines
- Understand workflow

**Context 30-60%**: Read selectively
- Only relevant sections
- Skip known content
- Focus on task-specific docs

**Context 60-85%**: Read minimally
- Task-specific only (1-2 docs)
- Use indexes for navigation
- Rely on memory

**Context 85%+**: Emergency mode
- INDEX files only
- Update SPEC/TODO
- Execute `/clear`

---

### For Developers

**First Time**:
1. [project-overview.md](./architecture/project-overview.md)
2. [scope-system.md](./architecture/scope-system.md)
3. [coding-conventions.md](./guidelines/coding-conventions.md)

**Daily Work**:
- Quick reference: Check index
- Specific questions: Read relevant section
- Documentation: Read documentation-rules.md

---

## 🔗 Related Documentation

### Project Management
- [Project Index](../project/index.md)
- [SPEC Index](../project/spec/README.md)
- [TODO Index](../project/todo/README.md)

### Tools
- [Commands Index](../../commands/INDEX.md)
- [Skills Index](../../skills/INDEX.md)

### Guides
- [Quick Start](../project/QUICK_START.md)
- [Reading Guide](../project/READING_GUIDE.md)

---

**Document Status**: Active
**Maintained By**: HaroFramework Team
**Last Updated**: 2025-10-26
