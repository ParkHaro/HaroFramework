---
title: HaroFramework SPEC Index
version: 3.0.0
scope: framework
created: 2025-10-26
modified: 2025-10-26
category: Specification
tags: [spec, index, architecture, documentation]
paired_document: README_KOR.md
parent_documents:
  - ../index.md
child_documents:
  - ./01-vision/overview.md
  - ./02-architecture/6-layer-system.md
  - ./03-documentation-system/bilingual-rules.md
  - ./04-scope-dependency/rules.md
  - ./05-core-systems/README.md
  - ./06-quality/code-quality.md
  - ./07-tech-stack/unity-environment.md
  - ./08-workflow/development-process.md
  - ./09-success-criteria/framework-goals.md
  - ./10-future/planned-features.md
references: []
status: active
---

# HaroFramework SPEC Index

Complete project specification and architecture documentation organized into 10 major sections.

**Total SPEC Files**: 62 (31 English + 31 Korean)

---

## 📑 Table of Contents

### [01. Project Vision](./01-vision/overview.md)
**What and why we're building**

- [Overview](./01-vision/overview.md) - Project purpose and target use cases
- [Goals](./01-vision/goals.md) - Reusability, extensibility, quality, performance

**Key Concepts**: Game framework foundation, multi-genre support, developer experience

---

### [02. Architecture](./02-architecture/6-layer-system.md)
**How the system is structured**

- [2-Scope Summary](./02-architecture/2-scope-summary.md) - Framework vs Game scope separation
- [6-Layer System](./02-architecture/6-layer-system.md) - Complete layer architecture
  - Data, Domain, Core, Interface, Service, Gameplay
- [Folder Structure](./02-architecture/folder-structure.md) - Project organization
- [Naming Conventions](./02-architecture/naming-conventions.md) - Consistent naming rules

**Key Concepts**: 2-scope system, 6-layer architecture, dependency flow, communication patterns

---

### [03. Documentation System](./03-documentation-system/bilingual-rules.md)
**How we document the project**

- [Bilingual Rules](./03-documentation-system/bilingual-rules.md) - English/Korean documentation
- [Metadata Standard](./03-documentation-system/metadata-standard.md) - YAML frontmatter
- [Version Management](./03-documentation-system/version-management.md) - Semantic versioning
- [Workflow Rules](./03-documentation-system/workflow-rules.md) - Documentation processes
- [Automation Scripts](./03-documentation-system/automation-scripts.md) - Validation tools

**Key Concepts**: Bilingual docs, modular structure, metadata, automation

---

### [04. Scope Dependency Rules](./04-scope-dependency/rules.md)
**Critical architectural constraints**

- [Rules](./04-scope-dependency/rules.md) - Framework ❌ Game, Game ✅ Framework
- [Validation](./04-scope-dependency/validation.md) - Automated enforcement
- [Examples](./04-scope-dependency/examples.md) - Good and bad patterns

**Key Concepts**: Scope isolation, reusability enforcement, validation scripts

---

### [05. Core Systems](./05-core-systems/README.md) ⭐
**Detailed specifications for all framework systems**

#### [Core Foundation](./05-core-systems/foundation/singleton.md)
14 foundational classes that form the base of the framework:

**Foundation (3)**:
- [Singleton](./05-core-systems/foundation/singleton.md) - Thread-safe singleton pattern
- [IModule](./05-core-systems/foundation/imodule.md) - Module interface
- [IService](./05-core-systems/foundation/iservice.md) - Service interface

**Core Systems (4)**:
- [EventBus](./05-core-systems/foundation/eventbus.md) - Event-driven communication
- [ServiceLocator](./05-core-systems/foundation/service-locator.md) - Service management
- [DataManager](./05-core-systems/foundation/data-manager.md) - Domain management
- [FrameworkLogger](./05-core-systems/foundation/framework-logger.md) - Logging system

**Base Classes (5)**:
- [BaseData](./05-core-systems/foundation/base-data.md) - Data layer base
- [BaseDomain](./05-core-systems/foundation/base-domain.md) - Domain layer base
- [BaseModule](./05-core-systems/foundation/base-module.md) - Module layer base
- [BaseService](./05-core-systems/foundation/base-service.md) - Service layer base
- [BaseGameplay](./05-core-systems/foundation/base-gameplay.md) - Gameplay layer base

**Framework Manager (2)**:
- [FrameworkConfig](./05-core-systems/foundation/framework-config.md) - Configuration
- [FrameworkManager](./05-core-systems/foundation/framework-manager.md) - Initialization manager

#### [Core Modules](./05-core-systems/modules/) (Phase 2)
To be implemented: UIModule, AudioModule, SceneModule, NetworkModule

#### [Lifecycle Management](./05-core-systems/lifecycle.md)
Initialization and shutdown sequences

**Key Concepts**: Core Foundation, 6-layer bases, lifecycle, event-driven, service-oriented

---

### [06. Quality Standards](./06-quality/code-quality.md)
**What quality means for this project**

- [Code Quality](./06-quality/code-quality.md) - Documentation, testing, standards
- [Documentation Quality](./06-quality/documentation-quality.md) - Completeness, accuracy
- [Validation](./06-quality/validation.md) - Automated quality gates

**Key Concepts**: >80% test coverage, XML docs, validation scripts, coding conventions

---

### [07. Technology Stack](./07-tech-stack/unity-environment.md)
**Technologies and tools we use**

- [Unity Environment](./07-tech-stack/unity-environment.md) - Unity 6, URP, Input System
- [Development Tools](./07-tech-stack/development-tools.md) - IDE, Git, documentation
- [Dependencies](./07-tech-stack/dependencies.md) - Package management

**Key Concepts**: Unity 6, URP 17.2.0, New Input System, minimal dependencies

---

### [08. Development Workflow](./08-workflow/development-process.md)
**How we develop features**

- [Development Process](./08-workflow/development-process.md) - 8-step process
- [Documentation Workflow](./08-workflow/documentation-workflow.md) - Doc creation process
- [Session Management](./08-workflow/session-management.md) - Context management (85% rule)

**Key Concepts**: Plan → Design → Implement → Test → Document → Review → Integrate → Validate

---

### [09. Success Criteria](./09-success-criteria/framework-goals.md)
**How we measure success**

- [Framework Goals](./09-success-criteria/framework-goals.md) - Core systems, tests, docs
- [Documentation Goals](./09-success-criteria/documentation-goals.md) - Bilingual, validated
- [Quality Goals](./09-success-criteria/quality-goals.md) - No warnings, tests pass

**Key Concepts**: Measurable goals, completion criteria, quality gates

---

### [10. Future Plans](./10-future/planned-features.md)
**What comes next**

- [Planned Features](./10-future/planned-features.md) - Multiplayer, AI, procedural gen
- [Documentation Evolution](./10-future/documentation-evolution.md) - Auto-gen, interactive
- [Tooling Improvements](./10-future/tooling-improvements.md) - CI/CD, translation, website

**Key Concepts**: Roadmap, scalability, community

---

## 🔍 How to Navigate

### For First-Time Readers
**Recommended reading order:**
1. [01. Project Vision](./01-vision/overview.md) - Understand the "why"
2. [02. Architecture - 6-Layer System](./02-architecture/6-layer-system.md) - Understand the structure
3. [05. Core Systems - Foundation](./05-core-systems/foundation/singleton.md) - See implementation details
4. [06. Quality Standards](./06-quality/code-quality.md) - Learn quality requirements

### For Developers
**Quick reference:**
- Architecture → [6-Layer System](./02-architecture/6-layer-system.md)
- Implementation → [Core Foundation](./05-core-systems/foundation/singleton.md)
- Standards → [Quality](./06-quality/code-quality.md)
- Workflow → [Development Process](./08-workflow/development-process.md)

### For Documentation Writers
**Essential reading:**
- [Bilingual Rules](./03-documentation-system/bilingual-rules.md)
- [Metadata Standard](./03-documentation-system/metadata-standard.md)
- [Workflow Rules](./03-documentation-system/workflow-rules.md)

---

## 📊 SPEC Statistics

### File Count by Section

| Section | Files | Topics |
|---------|-------|--------|
| 01. Vision | 2 | Overview, Goals |
| 02. Architecture | 4 | Scope, Layers, Structure, Naming |
| 03. Documentation | 5 | Rules, Metadata, Versioning, Workflow, Scripts |
| 04. Scope Dependency | 3 | Rules, Validation, Examples |
| 05. Core Systems | 16 | 14 classes + lifecycle + index |
| 06. Quality | 3 | Code, Docs, Validation |
| 07. Tech Stack | 3 | Unity, Tools, Dependencies |
| 08. Workflow | 3 | Development, Docs, Sessions |
| 09. Success | 3 | Framework, Docs, Quality |
| 10. Future | 3 | Features, Docs, Tooling |

**Total**: 45 documents (English), 45 translations (Korean), 2 indexes = **92 SPEC files**

### Key Metrics
- **Deepest Section**: Core Systems (14 class specifications)
- **Most Critical**: Architecture (6-layer system, scope rules)
- **Most Referenced**: Core Foundation (all Phase 1 tasks link here)

---

## 🔗 Related Documentation

### Internal Links
- [Back to Project Index](../index.md)
- [TODO Index](../todo/README.md)
- [Progress Dashboard](../todo/PROGRESS.md)

### External Resources
- [Coding Conventions](../../doc/guidelines/coding-conventions.md)
- [Development Workflow](../../doc/workflow/development-workflow.md)
- [Scope System Guide](../../doc/architecture/scope-system.md)

### Tools
- [Scope Validation Script](../../../scripts/scope_validate.py)
- [Document Validation Script](../../../scripts/doc_validate.py)

---

## 📝 Document Maintenance

### Version Control
Each SPEC document has independent versioning following semantic versioning:
- **MAJOR**: Breaking changes to specifications
- **MINOR**: New sections or significant additions
- **PATCH**: Clarifications, typos, examples

### Update Workflow
1. Update English document
2. Update `modified` date in metadata
3. Increment version appropriately
4. Update Korean translation
5. Run `doc_validate.py`
6. Commit changes

### Quality Checklist
- [ ] Metadata complete and accurate
- [ ] Korean translation synchronized
- [ ] Cross-references valid
- [ ] Examples tested and working
- [ ] Passes validation scripts

---

**Document Status**: Active
**Maintained By**: HaroFramework Team
**Last Updated**: 2025-10-26
**Next Review**: After Phase 1 completion
