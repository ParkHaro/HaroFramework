---
title: Claude Code Reading Guide
version: 1.0.0
scope: framework
created: 2025-10-26
modified: 2025-10-26
category: Guide
tags: [guide, token-optimization, reading-strategy, context-management]
paired_document: READING_GUIDE_KOR.md
parent_documents:
  - ./index.md
child_documents: []
references:
  - ./QUICK_START.md
  - ./SESSION_RESTORE.md
  - ../doc/INDEX.md
status: active
---



<!-- Navigation -->
**🏠 [HaroFramework Project](../../MASTER_INDEX.md)** | **📂 [HaroFramework Project Index](INDEX.md)** | **⬆️ [HaroFramework Project Index](index.md)**

---
# Claude Code Reading Guide

**Token Optimization Strategies for Efficient Document Reading**

This guide helps Claude Code read only necessary documents based on context usage, saving 30-50% tokens.

**Context Limit**: 200K tokens | **Monitor**: Current token usage percentage

---

## 📊 Context-Based Reading Strategies

### 🟢 Green Zone (0-30% / 0-60K tokens)
**Status**: Plenty of context available

**Strategy**: **Comprehensive Reading**

**What to Read**:
- Start with [Master Index](../../MASTER_INDEX.md)
- Read [Project Index](./index.md)
- Review [TODO Dashboard](./todo/PROGRESS.md)
- Read task-specific SPEC sections
- Check [Quick Start](./QUICK_START.md) for scenarios

**Why**: Build complete understanding, no need to optimize

**Example**:
```
Starting new session with 15K tokens used
→ Read: index.md, TODO/PROGRESS.md, spec/05-core-systems/
→ Result: Full context, ready for complex tasks
```

---

### 🟡 Yellow Zone (30-60% / 60-120K tokens)
**Status**: Moderate context usage

**Strategy**: **Selective Reading**

**What to Read**:
- [TODO Dashboard](./todo/PROGRESS.md) - Current tasks only
- Task-specific SPEC (1-2 files)
- Relevant guidelines (as needed)
- Skip known architecture details

**What to Skip**:
- General overviews you've already read
- Detailed examples
- Full SPEC sections (use indexes instead)

**Why**: Save tokens while maintaining task context

**Example**:
```
Implementing Singleton.cs with 80K tokens used
→ Read: spec/05-core-systems/foundation/singleton.md
→ Skip: Full architecture docs, general guidelines
→ Result: Task-focused, efficient
```

---

### 🟠 Orange Zone (60-85% / 120-170K tokens)
**Status**: High context usage - **Be Careful**

**Strategy**: **Minimal Reading**

**What to Read** (Maximum 2-3 files):
- Specific task file from TODO
- One SPEC section directly related
- Quick reference from index

**What to Skip**:
- Everything not directly task-related
- Architecture overviews
- Guidelines (rely on memory)
- Examples and tutorials

**Why**: Critical token conservation

**Example**:
```
Fixing bug with 140K tokens used
→ Read: Only the specific SPEC for affected class
→ Skip: All other documentation
→ Result: Minimal token usage, task completion
```

---

### 🔴 Red Zone (85%+ / 170K+ tokens)
**Status**: **EMERGENCY** - Context almost full

**Strategy**: **Index-Only + Immediate Action**

**What to Read** (Maximum 1 file):
- [TODO Dashboard](./todo/PROGRESS.md) ONLY

**Immediate Actions**:
1. Update [TODO](./TODO.md) with current progress
2. Update [SPEC](./SPEC.md) with any changes
3. Document current state in [Session Restore](./SESSION_RESTORE.md)
4. Execute `/clear` command
5. Start fresh session from checkpoints

**Why**: Prevent context overflow, ensure continuity

**Example**:
```
Context at 185K/200K tokens
→ Update TODO.md with completed tasks
→ Update SPEC.md with implementation notes
→ Create SESSION_RESTORE.md checkpoint
→ Execute /clear
→ Next session: Read TODO.md, continue from checkpoint
```

---

## 🎯 Task-Based Reading Maps

Quick reference for "What to read for each task type"

### 1. Implementing Core Foundation Classes
**Context Budget**: 10-15K tokens

**Must Read** (Priority order):
1. Task file: `todo/phase1-core-foundation/[task].md` (2K)
2. SPEC: `spec/05-core-systems/foundation/[class].md` (3K)
3. Coding Conventions: `doc/guidelines/coding-conventions.md` (5K)

**Optional** (if context allows):
- 6-Layer Architecture: `spec/02-architecture/6-layer-system.md`

**Can Skip**:
- General project overview
- Other SPEC sections
- Workflow documentation

---

### 2. Creating New Game Project
**Context Budget**: 8-10K tokens

**Must Read**:
1. Game Template: `games/_template/GAME.md` (2K)
2. Scope System: `doc/architecture/scope-system.md` (3K)
3. Project Structure: `spec/02-architecture/folder-structure.md` (3K)

**Can Skip**:
- Detailed framework implementation
- Core systems SPEC
- Testing guidelines

---

### 3. Writing Documentation
**Context Budget**: 5-8K tokens

**Must Read**:
1. Documentation Rules: `doc/guidelines/documentation-rules.md` (8K)
2. Metadata Template from any existing doc (1K)

**Can Skip**:
- Code implementation details
- Architecture overviews
- Workflow docs

---

### 4. Running Tests
**Context Budget**: 5K tokens

**Must Read**:
1. Quality Standards: `spec/06-quality/code-quality.md` (3K)
2. Test command: `commands/test.md` (1K)

**Can Skip**:
- Implementation details
- Architecture docs
- Documentation rules

---

### 5. Understanding Architecture
**Context Budget**: 12-15K tokens

**Must Read**:
1. 6-Layer System: `spec/02-architecture/6-layer-system.md` (5K)
2. Scope System: `doc/architecture/scope-system.md` (3K)
3. Project Overview: `doc/architecture/project-overview.md` (4K)

**Optional**:
- Core Systems overview
- Examples

---

### 6. Code Review / Bug Fix
**Context Budget**: 5-8K tokens

**Must Read**:
1. Coding Conventions: `doc/guidelines/coding-conventions.md` (5K)
2. Specific SPEC for affected class (3K)

**Can Skip**:
- General architecture
- Workflow docs
- Examples

---

### 7. Session Restoration
**Context Budget**: 3-5K tokens

**Must Read**:
1. Session Restore: `SESSION_RESTORE.md` (1K)
2. TODO Dashboard: `todo/PROGRESS.md` (2K)
3. Last checkpoint in SPEC/TODO (2K)

**Can Skip**:
- Everything else (restore from memory)

---

### 8. Committing Changes
**Context Budget**: 2-3K tokens

**Must Read**:
1. Git guidelines in CLAUDE.md (2K)

**Can Skip**:
- All other documentation

---

### 9. Validation / Quality Check
**Context Budget**: 5-7K tokens

**Must Read**:
1. Quality Standards: `spec/06-quality/` (4K)
2. Validation Guide: `spec/06-quality/validation.md` (3K)

**Can Skip**:
- Implementation docs
- Architecture overviews

---

### 10. Adding New Command/Skill
**Context Budget**: 8-10K tokens

**Must Read**:
1. Commands/Skills Index (2K)
2. Example command/skill file (2K)
3. Workflow guide for commands/skills (4K)

**Can Skip**:
- Core systems SPEC
- Architecture details

---

## 💡 Token Saving Tips

### Reading Techniques

**1. Use Indexes First**
```
❌ Read entire SPEC → Find what you need
✅ Read INDEX → Navigate to specific section
Savings: 50-70% tokens
```

**2. Read English Only**
```
❌ Read both .md and _KOR.md
✅ Read .md only (Korean is for humans)
Savings: 50% tokens
```

**3. Read Metadata Before Content**
```
✅ Check metadata `references` field
→ Know what else you might need
→ Plan reading strategy
Savings: Avoid unnecessary re-reads
```

**4. Use Quick Start for Scenarios**
```
❌ Search through multiple docs
✅ Check QUICK_START.md for scenario
→ Get exact docs needed
Savings: 30-40% tokens
```

**5. Leverage Navigation**
```
✅ Every doc has navigation to related docs
→ Follow direct links instead of searching
Savings: Time and tokens
```

---

### Memory Management

**What to Remember Long-Term**:
- 2-scope architecture (Framework ❌ Game)
- 6-layer dependency flow (Top → Bottom)
- Coding conventions (regions, naming)
- Session checkpoints

**What to Re-read Each Time**:
- Specific task requirements
- Class-specific SPEC
- Current TODO status

---

### Progressive Context Usage

**Session Start** (Low context):
- Read broadly to understand
- Build mental model
- Cache architecture knowledge

**Mid-Session** (Moderate context):
- Focus on task-specific docs
- Skip overviews
- Use memory + targeted reading

**Session End** (High context):
- Minimal new reading
- Finish current task
- Prepare checkpoint for next session

---

## 📈 Monitoring Context Usage

### Check Context Regularly

**Every 30 minutes or after major operations**:
```
Current: X tokens / 200K tokens = Y%

If Y < 30%: Green zone - read freely
If 30% ≤ Y < 60%: Yellow zone - be selective
If 60% ≤ Y < 85%: Orange zone - minimal reading
If Y ≥ 85%: Red zone - emergency mode
```

### Context Usage Predictions

**Typical Token Costs**:
- Index file: 1-2K tokens
- Short guide (Quick Start): 3-5K tokens
- SPEC section: 3-8K tokens
- Full SPEC document: 15-30K tokens
- Code file: 2-5K tokens
- Command/Skill file: 1-2K tokens

**Example Calculation**:
```
Planning to implement Singleton.cs:
- Task file: 2K
- Singleton SPEC: 4K
- Coding conventions: 5K
Total: ~11K tokens

Current usage: 50K
After reading: 61K (30.5%) - Still in Green/Yellow zone ✅
```

---

## 🔄 Session Management

### The 85% Rule

**When context reaches 85% (170K tokens)**:

**Mandatory Actions**:
1. **Update TODO.md**
   - Mark completed tasks
   - Add newly discovered tasks
   - Note current progress

2. **Update SPEC.md** (if changed)
   - Document implementations
   - Note decisions made
   - Update relevant sections

3. **Create SESSION_RESTORE.md**
   ```markdown
   ## Last Session
   - Date: 2025-10-26
   - Context Used: 175K/200K (87.5%)
   - Completed: CF-001, CF-002, CF-003
   - In Progress: CF-004 (EventBus implementation)
   - Next: Complete EventBus tests
   - Important: EventBus uses Action<T> delegates
   ```

4. **Execute `/clear`**
   - Clears context
   - Saves TODO/SPEC/SESSION_RESTORE
   - Ready for next session

### Starting Fresh Session

**First Actions** (5-10K tokens):
1. Read SESSION_RESTORE.md (1K)
2. Read TODO Dashboard (2K)
3. Read in-progress task SPEC (4K)
4. Continue from checkpoint

---

## 🎓 Best Practices

### Do's ✅

1. **Check context before reading**
   - Know your zone
   - Plan what to read

2. **Use indexes and navigation**
   - Faster navigation
   - Lower token cost

3. **Read task-specific only**
   - Focused on current work
   - Skip irrelevant content

4. **Update checkpoints at 85%**
   - Ensure continuity
   - Prevent data loss

5. **Leverage memory**
   - Remember architecture
   - Don't re-read basics

### Don'ts ❌

1. **Don't read everything**
   - Wastes tokens
   - Slows down work

2. **Don't skip checkpointing**
   - Risk losing progress
   - Hard to restore

3. **Don't read Korean docs**
   - Duplicate content
   - 50% waste

4. **Don't ignore context warnings**
   - May hit limit
   - Lose context

5. **Don't read examples unless needed**
   - High token cost
   - Often not necessary

---

## 📚 Document Priority Matrix

When choosing what to read, use this priority:

### High Priority (Always Read)
- Current task file from TODO
- Directly related SPEC section
- Critical errors/warnings

### Medium Priority (Read if Context Allows)
- Coding conventions
- Architecture overviews
- Related SPEC sections

### Low Priority (Skip Unless Necessary)
- Examples and tutorials
- Full documentation rules
- Historical context
- Alternative approaches

---

## 🚀 Quick Decision Tree

```
Am I starting a new session?
├─ Yes → Read SESSION_RESTORE + TODO (5K tokens)
└─ No → Continue

What's my context usage?
├─ < 30% → Read comprehensively
├─ 30-60% → Read selectively (task-specific)
├─ 60-85% → Read minimally (1-2 files max)
└─ ≥ 85% → STOP - Update & /clear

What's my task?
├─ Implementation → Read task + SPEC + conventions
├─ Testing → Read quality standards + test guide
├─ Documentation → Read doc rules + metadata
├─ Architecture → Read 6-layer + scope system
└─ Bug fix → Read affected class SPEC + conventions

Can I use memory instead of reading?
├─ Yes (know the content) → Skip reading
└─ No (unfamiliar) → Read necessary docs
```

---

**Document Status**: Active
**Maintained By**: HaroFramework Team
**Last Updated**: 2025-10-26

**Remember**: Efficient reading = More context for actual work! 🚀
