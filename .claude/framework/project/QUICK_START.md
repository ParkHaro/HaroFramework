---
title: Quick Start Guide
version: 1.0.0
scope: framework
created: 2025-10-26
modified: 2025-10-26
category: Guide
tags: [guide, quick-start, scenarios, checklists]
paired_document: QUICK_START_KOR.md
parent_documents:
  - ./index.md
child_documents: []
references:
  - ./READING_GUIDE.md
  - ../doc/INDEX.md
  - ../../commands/INDEX.md
  - ../../skills/INDEX.md
status: active
---



<!-- Navigation -->
**🏠 [HaroFramework Project](../../MASTER_INDEX.md)** | **📂 [HaroFramework Project Index](INDEX.md)** | **⬆️ [HaroFramework Project Index](index.md)**

---
# Quick Start Guide

**Scenario-based checklists for common development tasks**

Jump directly to the scenario you need - each includes essential docs, tools, and validation steps.

---

## 📑 Scenarios

1. [Create Unity Component](#1-create-unity-component)
2. [Create ScriptableObject](#2-create-scriptableobject)
3. [Write Tests](#3-write-tests)
4. [Write Documentation](#4-write-documentation)
5. [Understand Architecture](#5-understand-architecture)
6. [Implement Core Foundation](#6-implement-core-foundation)
7. [Start New Game Project](#7-start-new-game-project)
8. [Restore Session](#8-restore-session)
9. [Fix Bug](#9-fix-bug)
10. [Validate Documentation](#10-validate-documentation)

---

## 1. Create Unity Component

**Goal**: Create MonoBehaviour script following framework conventions

**Read** (5-10K tokens):
1. ✅ [Coding Conventions](../doc/guidelines/coding-conventions.md) - **Required**
2. ⭕ [6-Layer System](./spec/02-architecture/6-layer-system.md) - Optional

**Tools**:
- **Auto**: "Create a player controller" → `unity-component` skill
- **Manual**: `/component PlayerController HaroFramework.Player`

**Checklist**:
- [ ] Namespace: `HaroFramework.*`
- [ ] Regions: Inspector Fields, Unity Lifecycle, Methods
- [ ] XML documentation (`///`)
- [ ] SerializeField for private inspector fields
- [ ] Component caching in Awake()

**Validate**:
```bash
# Check compiles
/test EditMode
```

**Result**: `Assets/Scripts/Runtime/[Category]/PlayerController.cs`

---

## 2. Create ScriptableObject

**Goal**: Create data asset for game configuration

**Read** (3-5K tokens):
1. ✅ [Coding Conventions](../doc/guidelines/coding-conventions.md) - **Required**

**Tools**:
- **Auto**: "Create weapon data with damage and range" → `unity-scriptable` skill
- **Manual**: `/scriptable WeaponData HaroFramework.Data`

**Checklist**:
- [ ] Namespace: `HaroFramework.Data`
- [ ] `[CreateAssetMenu]` attribute
- [ ] OnValidate() for data validation
- [ ] XML documentation

**Validate**:
- Right-click in Project → Create → HaroFramework → [Asset]

**Result**: `Assets/Scripts/Runtime/Data/WeaponData.cs`

---

## 3. Write Tests

**Goal**: Create unit/integration tests for component

**Read** (3-5K tokens):
1. ✅ [Quality Standards](./spec/06-quality/code-quality.md) - **Required**

**Tools**:
- **Auto**: "Write tests for HealthSystem" → `unity-testing` skill
- **Manual**: Use test template from quality standards

**Checklist**:
- [ ] Test assembly (.asmdef) in Tests/ folder
- [ ] AAA pattern (Arrange, Act, Assert)
- [ ] Method names: `Method_Condition_ExpectedBehavior`
- [ ] Both positive and negative test cases

**Validate**:
```bash
/test EditMode    # Fast tests
/test PlayMode    # Integration tests
```

**Result**: `Assets/Scripts/Tests/EditMode/HealthSystemTests.cs`

---

## 4. Write Documentation

**Goal**: Create or update bilingual markdown documentation

**Read** (5-8K tokens):
1. ✅ [Documentation Rules](../doc/guidelines/documentation-rules.md) - **Required**

**Tools**:
- Text editor for markdown

**Checklist**:
- [ ] YAML frontmatter with all required fields
- [ ] Create English `.md` first
- [ ] Create Korean `_KOR.md` immediately
- [ ] Link via `paired_document` field
- [ ] Add navigation (will be auto-added later)

**Validate**:
```bash
python .claude/scripts/doc_validate.py
python .claude/scripts/doc_sync.py --check
```

**Result**: Validated bilingual documentation pair

---

## 5. Understand Architecture

**Goal**: Learn framework structure and design

**Read** (12-15K tokens):
1. ✅ [6-Layer System](./spec/02-architecture/6-layer-system.md) - **Required**
2. ✅ [Scope System](../doc/architecture/scope-system.md) - **Required**
3. ⭕ [Project Overview](../doc/architecture/project-overview.md) - Optional

**Key Concepts**:
- **2-Scope**: Framework ❌ Game, Game ✅ Framework
- **6-Layer**: Data → Domain → Core → Interface → Service → Gameplay
- **Dependency Flow**: Top → Bottom only

**No Tools Needed**: Pure learning

**Result**: Understanding of architecture principles

---

## 6. Implement Core Foundation

**Goal**: Implement one of 14 core foundation classes

**Read** (10-15K tokens):
1. ✅ Task: `todo/phase1-core-foundation/[task].md` - **Required**
2. ✅ SPEC: `spec/05-core-systems/foundation/[class].md` - **Required**
3. ✅ [Coding Conventions](../doc/guidelines/coding-conventions.md) - **Required**
4. ⭕ [6-Layer System](./spec/02-architecture/6-layer-system.md) - If needed

**Tools**:
- Manual implementation (complex logic)
- Skills for boilerplate

**Checklist**:
- [ ] Read task SPEC completely
- [ ] Understand dependencies
- [ ] Implement class following SPEC
- [ ] Write XML documentation
- [ ] Write tests (unity-testing skill)
- [ ] Run tests: `/test EditMode`
- [ ] Mark task complete in TODO

**Validate**:
```bash
/test EditMode
```

**Result**: Core class implemented with tests

---

## 7. Start New Game Project

**Goal**: Create new game using framework

**Read** (8-10K tokens):
1. ✅ [Game Template](../../games/_template/GAME.md) - **Required**
2. ✅ [Scope System](../doc/architecture/scope-system.md) - **Required**
3. ⭕ [Folder Structure](./spec/02-architecture/folder-structure.md) - Optional

**Tools**:
- File system (copy template)

**Checklist**:
- [ ] Copy `.claude/games/_template/` → `.claude/games/[game-name]/`
- [ ] Update `GAME.md` with game-specific config
- [ ] Create game namespace: `[GameName].*`
- [ ] Game can use Framework (✅)
- [ ] Framework CANNOT reference Game (❌)

**Validate**:
```bash
python .claude/scripts/scope_validate.py
```

**Result**: New game project following scope rules

---

## 8. Restore Session

**Goal**: Continue work from previous Claude session

**Read** (3-5K tokens):
1. ✅ [Session Restore](./SESSION_RESTORE.md) - **Required**
2. ✅ [TODO Dashboard](./todo/PROGRESS.md) - **Required**
3. ⭕ Last checkpoint in SPEC/TODO - If needed

**Tools**:
- None (just reading)

**Checklist**:
- [ ] Read SESSION_RESTORE.md
- [ ] Check TODO for in-progress tasks
- [ ] Read relevant SPEC section
- [ ] Continue from checkpoint

**Result**: Context restored, ready to continue

---

## 9. Fix Bug

**Goal**: Debug and fix code issue

**Read** (5-8K tokens):
1. ✅ [Coding Conventions](../doc/guidelines/coding-conventions.md) - **Required**
2. ✅ Affected class SPEC - **Required**
3. ⭕ Related system SPEC - If needed

**Tools**:
- Unity debugger
- Tests

**Checklist**:
- [ ] Reproduce bug
- [ ] Identify affected class
- [ ] Read class SPEC
- [ ] Fix following conventions
- [ ] Write test to prevent regression
- [ ] Run all tests

**Validate**:
```bash
/test All
```

**Result**: Bug fixed with regression test

---

## 10. Validate Documentation

**Goal**: Check documentation quality and synchronization

**Read** (2-3K tokens):
- ⭕ Error messages from validation scripts

**Tools**:
- Validation scripts

**Checklist**:
- [ ] Run metadata validation
- [ ] Run synchronization check
- [ ] Run scope validation
- [ ] Fix any errors

**Validate**:
```bash
python .claude/scripts/doc_validate.py
python .claude/scripts/doc_sync.py --check
python .claude/scripts/scope_validate.py
```

**Result**: All documentation validated

---

## 🎯 Choosing the Right Scenario

**If you want to...**
- Create gameplay code → Scenario #1 (Component)
- Create data assets → Scenario #2 (ScriptableObject)
- Ensure quality → Scenario #3 (Tests)
- Document features → Scenario #4 (Documentation)
- Learn framework → Scenario #5 (Architecture)
- Build core → Scenario #6 (Core Foundation)
- Make a game → Scenario #7 (New Game)
- Continue work → Scenario #8 (Restore Session)
- Fix issues → Scenario #9 (Fix Bug)
- Check quality → Scenario #10 (Validate)

---

## 💡 Tips

### Before Starting Any Scenario

1. **Check context usage**: Use [Reading Guide](./READING_GUIDE.md)
2. **Check TODO**: Review [Progress Dashboard](./todo/PROGRESS.md)
3. **Read minimally**: Only required documents

### During Work

1. **Follow checklists**: Don't skip steps
2. **Validate early**: Run tests/validation frequently
3. **Document as you go**: Don't wait until end

### After Completing

1. **Update TODO**: Mark tasks complete
2. **Run validation**: Ensure quality
3. **Commit changes**: Follow git guidelines

---

**Document Status**: Active
**Maintained By**: HaroFramework Team
**Last Updated**: 2025-10-26

**Remember**: These are starting points - adjust based on your specific needs!
