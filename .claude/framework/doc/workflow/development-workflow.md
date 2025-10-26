---
title: "Development Workflow"
version: "1.0.0"
scope: "framework"
created: "2025-10-25"
modified: "2025-10-25"
category: "Workflow"
tags: [workflow, development, process, testing, git]
paired_document: "development-workflow_KOR.md"
parent_documents:
  - "../../project/SPEC.md"
child_documents: []
references:
  - "../guidelines/coding-conventions.md"
  - "../architecture/project-overview.md"
  - "./commands-guide.md"
  - "./skills-guide.md"
status: "approved"
---



<!-- Navigation -->
**🏠 [HaroFramework Project](../../../MASTER_INDEX.md)** | **📂 [Development Workflow](./)** | **⬆️ [HaroFramework Specification](../../project/SPEC.md)**

---
# Development Workflow

## Overview

This document outlines the standard development workflow for HaroFramework.

## Pre-Work Checklist

Before starting any task:

1. **Read Documentation**
   - Review `.claude/doc/coding-conventions.md`
   - Check relevant Skills/Commands in `.claude/doc/`
   - Review project structure in `.claude/doc/project-overview.md`

2. **Understand Requirements**
   - What is the feature/fix?
   - What components are affected?
   - What are the acceptance criteria?

3. **Plan Approach**
   - Which patterns to use?
   - What tests are needed?
   - What documentation is required?

## Development Stages

### 1. Planning Stage

**Activities:**
- Define feature requirements
- Identify affected systems
- Plan architecture and design
- Determine test strategy

**Tools:**
- Natural language for Skills activation
- `/component`, `/scriptable` for structure planning

**Output:**
- Feature design document (if needed)
- List of files to create/modify
- Test plan

### 2. Implementation Stage

**Activities:**
- Write code following conventions
- Create tests alongside code (TDD)
- Add XML documentation
- Validate with OnValidate methods

**Best Practices:**
- **Small Commits**: Commit logical chunks
- **Test First**: Write tests before/with code
- **Document As You Go**: Add XML comments immediately
- **Validate Early**: Use OnValidate for field checks

**Unity Workflow:**
```
1. Create script with proper namespace
2. Add to Unity (Scripts/Runtime/Category/)
3. Implement core functionality
4. Add serialized fields with tooltips
5. Cache references in Awake()
6. Write tests
7. Test in Unity Editor
8. Iterate
```

### 3. Testing Stage

**Edit Mode Tests:**
```csharp
// Test pure logic
[Test]
public void HealthSystem_TakeDamage_ReducesHealth()
{
    var health = new HealthSystem(100);
    health.TakeDamage(30);
    Assert.AreEqual(70, health.CurrentHealth);
}
```

**Play Mode Tests:**
```csharp
// Test Unity runtime behavior
[UnityTest]
public IEnumerator Player_OnDamage_TriggersAnimation()
{
    var player = CreateTestPlayer();
    player.TakeDamage(10);
    yield return null; // Wait one frame
    Assert.IsTrue(player.IsPlayingDamageAnimation);
}
```

**Testing Commands:**
```bash
/test EditMode    # Run logic tests
/test PlayMode    # Run runtime tests
/test            # Run all tests
```

### 4. Documentation Stage

**Code Documentation:**
```csharp
/// <summary>
/// Manages player health and damage.
/// </summary>
public class HealthSystem
{
    /// <summary>
    /// Applies damage and triggers death if health reaches zero.
    /// </summary>
    /// <param name="amount">Damage amount to apply</param>
    public void TakeDamage(int amount) { }
}
```

**Asset Documentation:**
- Add tooltips to serialized fields
- Include usage examples in code comments
- Update relevant .md files in `.claude/doc/` if needed

### 5. Review Stage

**Self-Review Checklist:**
- [ ] Follows coding conventions
- [ ] Has proper namespace
- [ ] Includes XML documentation
- [ ] Has tests with good coverage
- [ ] No compiler warnings
- [ ] Cached references properly
- [ ] OnValidate for field validation
- [ ] No magic numbers
- [ ] Follows Unity best practices
- [ ] Performance considerations addressed

**Tools:**
- Unity Console (check for warnings)
- Test Runner (verify all tests pass)
- `/build` (verify no build errors)

### 6. Integration Stage

**Before Committing:**
```bash
# Verify tests pass
/test

# Check build
/build

# Review changes
git status
git diff
```

**Commit Message Format:**
```
Short summary (50 chars or less)

Detailed explanation if needed:
- What changed
- Why it changed
- Any breaking changes
- Related issue numbers
```

## Feature Development Pattern

### Example: Creating a Health System

**1. Planning:**
```
Request: "Create a health system"
→ unity-component skill activates
→ Plan: MonoBehaviour + ScriptableObject for config
```

**2. Create Data Asset:**
```
Request: "Create health configuration data"
→ unity-scriptable skill activates
→ Generates: HealthData.cs (ScriptableObject)
```

**3. Create Component:**
```
Request: "Create health system component"
→ unity-component skill activates
→ Generates: HealthSystem.cs (MonoBehaviour)
```

**4. Create Tests:**
```
Request: "Write tests for health system"
→ unity-testing skill activates
→ Generates: HealthSystemTests.cs
```

**5. Create Custom Inspector (if needed):**
```
Request: "Create custom inspector for health system"
→ unity-editor skill activates
→ Generates: HealthSystemEditor.cs
```

## Iteration Workflow

```
Requirements → Plan → Implement → Test → Review
                 ↑                           ↓
                 └──────── Refine ←──────────┘
```

### Rapid Iteration:
1. Make small changes
2. Test immediately in Unity
3. Run automated tests: `/test`
4. Refine based on results
5. Repeat

## Common Workflows

### Adding New Feature
```
1. Read conventions: .claude/doc/coding-conventions.md
2. Use Skill: "Create [feature] system"
3. Write tests: "Create tests for [feature]"
4. Integrate: Add to existing systems
5. Test: /test
6. Document: Update relevant docs
7. Commit: git commit with clear message
```

### Fixing Bug
```
1. Reproduce bug in test
2. Make test fail (demonstrates bug)
3. Fix code to pass test
4. Verify fix: /test
5. Check no side effects: /build
6. Commit fix with issue reference
```

### Refactoring
```
1. Ensure tests exist and pass
2. Refactor code
3. Verify tests still pass
4. Check no warnings
5. Commit refactoring
```

### Adding Tests
```
1. Use skill: "Write tests for [component]"
2. Review generated tests
3. Add edge case tests
4. Run: /test
5. Verify coverage
6. Commit tests
```

## Build Workflow

### Development Build
```bash
/build          # Check current settings
/build Windows  # Build for Windows
```

### Release Build
```
1. Ensure all tests pass: /test
2. Update version number
3. Build for target platforms
4. Test builds on target platform
5. Create release notes
6. Tag release in git
```

## Git Workflow

### Branch Strategy
```
main (stable)
  └── feature/pscope-system (working)
  └── fix/health-bug (working)
```

### Standard Flow
```bash
# Start new feature
git checkout -b feature/feature-name

# Work and commit
git add .
git commit -m "Implement feature"

# Prepare for merge
/test
/build

# Merge when ready
git checkout main
git merge feature/feature-name
```

## Performance Testing

```
1. Implement feature
2. Profile in Unity Profiler
3. Identify bottlenecks
4. Optimize hot paths
5. Cache references
6. Use object pooling if needed
7. Re-profile to verify improvements
```

## Debugging Workflow

```
1. Reproduce issue
2. Check Unity Console for errors
3. Add Debug.Log statements
4. Use Unity Debugger
5. Check component inspector values
6. Verify references not null
7. Check execution order
8. Fix issue
9. Add test to prevent regression
```

## Related Documentation

- [Coding Conventions](../guidelines/coding-conventions.md) - Code standards
- [Project Overview](../architecture/project-overview.md) - Project structure
- [Commands Guide](./commands-guide.md) - Command reference
- [Skills Guide](./skills-guide.md) - Skills reference

---

**Document Status**: Approved
**Version**: 1.0.0
**Last Updated**: 2025-10-25
