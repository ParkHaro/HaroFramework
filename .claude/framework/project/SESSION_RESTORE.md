---
title: Session Restoration Guide
version: 1.0.0
scope: framework
created: 2025-10-26
modified: 2025-10-26
category: Session Management
tags: [session, restore, context, continuation]
status: active
---

# Session Restoration Guide

**Session Date**: 2025-10-26
**Context Usage at Break**: 85% (170k/200k tokens)
**Reason for Break**: Context threshold reached during modular documentation restructuring

---

## 🎯 Current Task

**Main Objective**: Restructure SPEC.md (1,280 lines) and TODO.md (720 lines) into modular file structure

**Total Plan**: Create 136 files (70 English + 66 Korean)
- SPEC: 62 files
- TODO: 66 files
- Indexes: 4 files
- Archive: 4 files

---

## ✅ Completed Work (Step 1-2)

### Step 1: Folder Structure ✓
**Created 21 folders**:

**SPEC Folders** (11):
```
.claude/framework/project/spec/
├── 01-vision/
├── 02-architecture/
├── 03-documentation-system/
├── 04-scope-dependency/
├── 05-core-systems/
│   ├── foundation/
│   └── modules/
├── 06-quality/
├── 07-tech-stack/
├── 08-workflow/
├── 09-success-criteria/
└── 10-future/
```

**TODO Folders** (9):
```
.claude/framework/project/todo/
├── completed/
│   ├── documentation-setup/
│   └── automation-scripts/
├── phase1-core-foundation/
│   ├── phase-a-foundation/
│   ├── phase-b-core-systems/
│   ├── phase-c-base-classes/
│   └── phase-d-framework-manager/
├── phase2-core-modules/
├── phase3-example/
└── phase4-documentation/
```

**Archive Folder** (1):
```
.claude/framework/project/archive/
```

### Step 2: Master Index Files (Partial) ✓
**Created 4 English files** (256+294+283+354 = 1,187 lines):

1. ✅ `project/index.md` (256 lines)
   - Master project index
   - Links to SPEC and TODO
   - Quick navigation guide

2. ✅ `project/spec/README.md` (294 lines)
   - SPEC index with 10 sections
   - Core Systems breakdown (14 classes)
   - Navigation guide

3. ✅ `project/todo/README.md` (283 lines)
   - TODO index with phase structure
   - Task tables for Phase 1 (14 tasks)
   - Status tracking

4. ✅ `project/todo/PROGRESS.md` (354 lines)
   - Progress dashboard
   - Phase breakdown
   - Metrics and timeline

**Remaining Step 2 Work**:
- ❌ Korean translations (4 files): `*_KOR.md` for above files

---

## 🔄 Remaining Work (Step 3-12)

### Step 3: SPEC Sections 1-4 (1 hour)
**Create 30 files** (15 English + 15 Korean):
- 01-vision/ (2 docs)
- 02-architecture/ (4 docs)
- 03-documentation-system/ (5 docs)
- 04-scope-dependency/ (3 docs)
- **Translations** (15 Korean files)

### Step 4: SPEC Core Systems (1 hour)
**Create 30 files** (15 English + 15 Korean):
- 05-core-systems/foundation/ (14 class specs + 1 lifecycle)
- **Translations** (15 Korean files)

**14 Core Classes to Document**:
1. Singleton.cs
2. IModule.cs
3. IService.cs
4. EventBus.cs
5. ServiceLocator.cs
6. DataManager.cs
7. FrameworkLogger.cs
8. BaseData.cs
9. BaseDomain.cs
10. BaseModule.cs
11. BaseService.cs
12. BaseGameplay.cs
13. FrameworkConfig.cs
14. FrameworkManager.cs

### Step 5: SPEC Sections 6-10 (30 min)
**Create 24 files** (12 English + 12 Korean):
- 06-quality/ (3 docs)
- 07-tech-stack/ (3 docs)
- 08-workflow/ (3 docs)
- 09-success-criteria/ (3 docs)
- 10-future/ (3 docs)

### Step 6: TODO Completed Tasks (20 min)
**Create 4 files** (2 English + 2 Korean):
- completed/documentation-setup/IP-001.md
- completed/automation-scripts/P-002.md

### Step 7: TODO Phase 1 Tasks (1 hour)
**Create 30 files** (15 English + 15 Korean):
- phase1-core-foundation/README.md (1 file)
- phase-a-foundation/ (3 CF tasks)
- phase-b-core-systems/ (4 CF tasks)
- phase-c-base-classes/ (5 CF tasks)
- phase-d-framework-manager/ (2 CF tasks)

**14 CF Tasks** (CF-001 ~ CF-014):
Each task file includes:
- Task overview
- Implementation checklist
- Validation criteria
- Related SPEC links
- Commit template

### Step 8: TODO Phase 2-4 Placeholders (15 min)
**Create 6 files** (3 English + 3 Korean):
- phase2-core-modules/README.md
- phase3-example/README.md
- phase4-documentation/README.md

### Step 9: Backup Existing Files (5 min)
**Backup 4 files**:
- Copy SPEC.md → archive/SPEC-v2.0.0-backup.md
- Copy SPEC_KOR.md → archive/SPEC_KOR-v2.0.0-backup.md
- Copy TODO.md → archive/TODO-v2.0.0-backup.md
- Copy TODO_KOR.md → archive/TODO_KOR-v2.0.0-backup.md

### Step 10: Link Setup (30 min)
- Add metadata relationships
- Cross-reference links
- Task → SPEC links
- Task dependency links

### Step 11: Validation (20 min)
- Run doc_validate.py
- Run scope_validate.py
- Navigation test
- Link integrity test

### Step 12: Git Commit (10 min)
- Commit 1: Indexes
- Commit 2: SPEC modularization
- Commit 3: TODO modularization
- Commit 4: Archive old files

---

## 📂 Important File Locations

### Current Session Files
```
.claude/framework/project/
├── index.md                    # ✅ Created
├── spec/
│   └── README.md               # ✅ Created
├── todo/
│   ├── README.md               # ✅ Created
│   └── PROGRESS.md             # ✅ Created
└── SESSION_RESTORE.md          # ✅ This file
```

### Source Files (to be split)
```
.claude/framework/project/
├── SPEC.md                     # 1,280 lines - TO BE ARCHIVED
├── SPEC_KOR.md                 # Korean version - TO BE ARCHIVED
├── TODO.md                     # 720 lines - TO BE ARCHIVED
└── TODO_KOR.md                 # Korean version - TO BE ARCHIVED
```

### Key Reference Documents
```
.claude/framework/doc/
├── guidelines/
│   ├── coding-conventions.md
│   └── documentation-rules.md
└── architecture/
    ├── project-overview.md
    └── scope-system.md
```

---

## 🚀 How to Resume Work

### Step-by-Step Resume Process

1. **Start Fresh Session**
   ```bash
   # Check current location
   pwd
   # Should be: C:\Users\haro7\Projects\Unity\HaroFramework
   ```

2. **Read Context Documents** (in order)
   - `project/SESSION_RESTORE.md` (this file)
   - `project/index.md` (master index)
   - `project/spec/README.md` (SPEC structure)
   - `project/todo/README.md` (TODO structure)
   - `project/todo/PROGRESS.md` (current progress)

3. **Verify Existing Work**
   ```bash
   # Check folder structure
   ls -R .claude/framework/project/

   # Should see:
   # - spec/ with 11 subfolders
   # - todo/ with 9 subfolders
   # - 4 index/progress files created
   ```

4. **Continue from Step 2 (Korean Translations)**
   - Create `index_KOR.md`
   - Create `spec/README_KOR.md`
   - Create `todo/README_KOR.md`
   - Create `todo/PROGRESS_KOR.md`

5. **Or Skip to Step 3 (SPEC Modularization)**
   - Start with Section 01-vision
   - Extract content from original SPEC.md
   - Create individual section files
   - Add Korean translations

---

## 📋 Quick Reference

### What Was Completed
- ✅ 21 folders created
- ✅ 4 master index files (English only)
- ✅ Navigation structure established
- ✅ Progress dashboard created

### What's Next
- ❌ 4 Korean translation files
- ❌ 60+ SPEC section files
- ❌ 30+ TODO task files
- ❌ Backup and archive
- ❌ Link setup and validation

### File Count Progress
- **Created**: 4 files (3% of 136)
- **Remaining**: 132 files (97%)

---

## 💡 Decision Points for Next Session

### Option A: Complete Step 2 First
**Pros**: Finish current step, maintain consistency
**Cons**: 1 hour for translations before moving forward
**Recommendation**: If want clean completion

### Option B: Skip to Step 3
**Pros**: Get to content faster, Korean later
**Cons**: Incomplete step, need to return
**Recommendation**: If want to see structure first

### Option C: Create Sample Files
**Pros**: Test structure before full implementation
**Cons**: Rework needed
**Recommendation**: If uncertain about structure

---

## 🎯 Recommended Next Actions

### Immediate Next Task (5-10 minutes)
**Test the Structure**:
1. Open `project/index.md` in editor
2. Click through links to verify navigation
3. Check folder structure makes sense
4. Confirm approach before continuing

### If Structure Looks Good (Continue)
**Resume with Step 2**:
- Create 4 Korean translation files
- Then proceed to Step 3

**OR Resume with Step 3**:
- Start SPEC modularization
- Do Korean translations at end

### If Structure Needs Adjustment
**Discuss Changes**:
- What folder structure changes?
- What file naming changes?
- What content organization changes?

---

## 📊 Context Management

### Token Usage
- **At Break**: 170k/200k (85%)
- **Recommended**: < 170k for optimal performance
- **Critical**: 185k+ (approaching limit)

### For Next Session
- **Expected**: Start at ~50k (system + memory files)
- **Buffer**: ~150k available for work
- **Strategy**: Create files incrementally, commit regularly

---

## 🔗 Important Links

### Master Documents
- [Project Index](./index.md)
- [SPEC Index](./spec/README.md)
- [TODO Index](./todo/README.md)
- [Progress Dashboard](./todo/PROGRESS.md)

### Original Files
- [Original SPEC.md](./SPEC.md) - 1,280 lines
- [Original TODO.md](./TODO.md) - 720 lines

### Guidelines
- [Coding Conventions](../doc/guidelines/coding-conventions.md)
- [Documentation Rules](../doc/guidelines/documentation-rules.md)

---

## 📝 Notes for Claude Code

### Context Optimization
- **Read only**: English documents (skip Korean for now)
- **Incremental**: Create files in batches, validate, commit
- **Reference**: Use SESSION_RESTORE.md as primary guide

### Task Priority
1. Verify existing structure works
2. Complete remaining index files (if needed)
3. SPEC modularization (core content)
4. TODO modularization (task details)
5. Korean translations (can be done in batches)
6. Validation and commit

### Success Criteria
- All 136 files created
- Navigation works end-to-end
- Korean translations synchronized
- Validation scripts pass
- Git committed with clear history

---

**Status**: Session paused at 85% context
**Resume Point**: Step 2 (Korean translations) or Step 3 (SPEC modularization)
**Estimated Remaining Time**: 3-4 hours
**Next Milestone**: Complete modular structure, validate, commit

---

**Created**: 2025-10-26
**Last Updated**: 2025-10-26
**Session**: Modular Documentation Restructuring
**Phase**: Foundation Setup (21% complete)
