---
title: HaroFramework Project Index
version: 3.0.0
scope: framework
created: 2025-10-26
modified: 2025-10-26
category: Project Management
tags: [index, navigation, master-index]
paired_document: index_KOR.md
parent_documents: []
child_documents:
  - ./spec/README.md
  - ./todo/README.md
references: []
status: active
---

# HaroFramework Project Index

Welcome to HaroFramework project documentation. This is the master index for navigating all project documentation.

## 📋 Documentation Structure

### SPEC (Specification)
**Complete project specification and architecture documentation**

👉 **[Go to SPEC Index](./spec/README.md)**

Quick access to major sections:
- [01. Project Vision](./spec/01-vision/overview.md) - Project goals and objectives
- [02. Architecture](./spec/02-architecture/6-layer-system.md) - 6-layer system architecture
- [03. Documentation System](./spec/03-documentation-system/bilingual-rules.md) - Documentation standards
- [04. Scope Dependency Rules](./spec/04-scope-dependency/rules.md) - Framework/Game scope rules
- [05. Core Systems](./spec/05-core-systems/README.md) - Core Foundation & Modules
  - [Foundation Details](./spec/05-core-systems/foundation/singleton.md) - 14 core classes
- [06. Quality Standards](./spec/06-quality/code-quality.md) - Code and documentation quality
- [07. Technology Stack](./spec/07-tech-stack/unity-environment.md) - Unity 6, URP, tools
- [08. Development Workflow](./spec/08-workflow/development-process.md) - Development process
- [09. Success Criteria](./spec/09-success-criteria/framework-goals.md) - Project goals
- [10. Future Plans](./spec/10-future/planned-features.md) - Roadmap

### TODO (Task Tracking)
**Task management and progress tracking**

👉 **[Go to TODO Index](./todo/README.md)**

👉 **[View Progress Dashboard](./todo/PROGRESS.md)**

#### Current Phase
**Phase 1: Core Foundation** - Status: PENDING (0/14 completed)

Next task: [CF-001: Singleton.cs](./todo/phase1-core-foundation/phase-a-foundation/CF-001-singleton.md)

#### All Phases
- [✅ Completed Tasks](./todo/completed/) - Documentation setup, automation scripts
- [🔵 Phase 1: Core Foundation](./todo/phase1-core-foundation/README.md) - 14 tasks (0-4 weeks)
- [⏳ Phase 2: Core Modules](./todo/phase2-core-modules/README.md) - To be detailed
- [⏳ Phase 3: Example Implementation](./todo/phase3-example/README.md) - To be detailed
- [⏳ Phase 4: Documentation & Testing](./todo/phase4-documentation/README.md) - To be detailed

---

## 🔗 Quick Navigation

### For Developers

**Starting Development?**
1. Read [Project Vision](./spec/01-vision/overview.md)
2. Understand [6-Layer Architecture](./spec/02-architecture/6-layer-system.md)
3. Follow [Coding Conventions](../doc/guidelines/coding-conventions.md)
4. Check [Development Workflow](./spec/08-workflow/development-process.md)

**Working on Core Foundation?**
1. Check [Progress Dashboard](./todo/PROGRESS.md)
2. Find your task in [Phase 1](./todo/phase1-core-foundation/README.md)
3. Read related [SPEC documentation](./spec/05-core-systems/foundation/singleton.md)
4. Follow task checklist

### For Documentation

**Writing Documentation?**
- [Bilingual Documentation Rules](./spec/03-documentation-system/bilingual-rules.md)
- [Metadata Standards](./spec/03-documentation-system/metadata-standard.md)
- [Version Management](./spec/03-documentation-system/version-management.md)
- [Workflow Rules](./spec/03-documentation-system/workflow-rules.md)

**Validating Documentation?**
- Run `python .claude/scripts/doc_validate.py`
- Run `python .claude/scripts/scope_validate.py`
- Check [Validation Guide](./spec/06-quality/validation.md)

### For Project Management

**Tracking Progress?**
- [Progress Dashboard](./todo/PROGRESS.md) - Overall progress metrics
- [Phase 1 Status](./todo/phase1-core-foundation/README.md) - Current phase details
- [Completed Tasks](./todo/completed/) - Historical records

**Planning Next Steps?**
- Review [Success Criteria](./spec/09-success-criteria/framework-goals.md)
- Check [Future Plans](./spec/10-future/planned-features.md)
- Consult [Session Management](./spec/08-workflow/session-management.md)

---

## 📚 External Documentation

### Framework Documentation
- [Architecture Documentation](../doc/architecture/scope-system.md)
- [Development Guidelines](../doc/guidelines/coding-conventions.md)
- [Workflow Guides](../doc/workflow/development-workflow.md)
- [Skills Guide](../doc/workflow/skills-guide.md)
- [Commands Guide](../doc/workflow/commands-guide.md)

### Automation Scripts
- [Scope Validation](../../scripts/scope_validate.py)
- [Document Validation](../../scripts/doc_validate.py)
- [Document Sync](../../scripts/doc_sync.py)
- [Version Bump](../../scripts/version_bump.py)
- [Scripts README](../../scripts/README.md)

---

## 🎯 Document Structure Benefits

### Modular Organization
- **Small Files**: Each document 100-300 lines (easy to read/edit)
- **Clear Hierarchy**: Intuitive folder structure
- **Easy Navigation**: Index files and cross-references
- **Git-Friendly**: Clear diffs, minimal conflicts

### Progress Tracking
- **Phase-Based**: Tasks organized by development phase
- **Status Tracking**: PENDING → IN_PROGRESS → COMPLETED
- **Dependencies**: Clear task dependencies
- **History**: Completed tasks archived

### Scalability
- **Easy Addition**: Add new sections without modifying others
- **Independent Updates**: Update one document at a time
- **Version Control**: Each document has independent versioning
- **Collaboration**: Multiple people can work simultaneously

---

## 📖 How to Use This Index

### Finding Information

**If you want to understand the project:**
→ Start with [SPEC Index](./spec/README.md) → Read Vision & Architecture

**If you want to implement a feature:**
→ Check [TODO Index](./todo/README.md) → Find your task → Read related SPEC

**If you want to contribute:**
→ Read [Development Workflow](./spec/08-workflow/development-process.md) → Follow conventions

### Navigation Tips

1. **Use Index Files**: Start from index, drill down to specifics
2. **Follow Cross-References**: Documents link to related content
3. **Check Metadata**: Each document lists parent/child relationships
4. **Use Search**: Find files by name or grep for keywords

---

## 🔄 Version History

| Version | Date | Changes |
|---------|------|---------|
| 3.0.0 | 2025-10-26 | Modularized structure (136 files) |
| 2.0.0 | 2025-10-25 | Single-file SPEC/TODO (2 files) |
| 1.0.0 | 2025-10-25 | Initial documentation setup |

---

## 📞 Support

**For Questions:**
- Check relevant SPEC section
- Review development workflow
- Consult coding conventions

**For Issues:**
- Document validation errors → Run validation scripts
- Missing information → Check index navigation
- Unclear requirements → Review SPEC details

---

**Document Status**: Active
**Maintained By**: HaroFramework Team
**Last Major Update**: 2025-10-26 (v3.0.0 - Modular structure)

**Total Files**: 136 (70 English + 66 Korean)
- SPEC: 62 files (31 English + 31 Korean)
- TODO: 66 files (33 English + 33 Korean)
- Archive: 4 files
- Indexes: 4 files
