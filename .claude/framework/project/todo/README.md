---
title: HaroFramework TODO Index
version: 3.0.0
scope: framework
created: 2025-10-26
modified: 2025-10-26
category: Task Management
tags: [todo, tasks, index, progress]
paired_document: README_KOR.md
parent_documents:
  - ../index.md
child_documents:
  - ./PROGRESS.md
  - ./phase1-core-foundation/README.md
  - ./phase2-core-modules/README.md
  - ./phase3-example/README.md
  - ./phase4-documentation/README.md
references:
  - ../spec/README.md
status: active
---

# HaroFramework TODO Index

Task management and progress tracking for HaroFramework development.

**Total TODO Files**: 66 (33 English + 33 Korean)

---

## 📊 Overall Progress

👉 **[View Detailed Progress Dashboard](./PROGRESS.md)**

### Quick Stats
- **Total Phases**: 4
- **Total Tasks**: 40+ (14 in Phase 1)
- **Completed**: 6 (Documentation setup, automation scripts)
- **In Progress**: 0
- **Pending**: 34+

### Current Focus
**Phase 1: Core Foundation** - 14 tasks (PENDING)

Next task: **[CF-001: Singleton.cs](./phase1-core-foundation/phase-a-foundation/CF-001-singleton.md)**

---

## 📁 Task Structure

### ✅ [Completed Tasks](./completed/)
**Status**: ARCHIVED

Tasks that have been successfully completed and archived for reference.

#### [Documentation Setup](./completed/documentation-setup/)
- **IP-001**: Initial project structure and SPEC/TODO creation
- **Completed**: 2025-10-26
- **Achievements**: Folder structure, bilingual documentation system, metadata standards

#### [Automation Scripts](./completed/automation-scripts/)
- **P-002**: Development of 4 automation scripts
- **Completed**: 2025-10-26
- **Deliverables**: scope_validate.py, doc_validate.py, doc_sync.py, version_bump.py

---

### 🔵 [Phase 1: Core Foundation](./phase1-core-foundation/README.md)
**Status**: PENDING | **Tasks**: 14 | **Completion**: 0%

**Objective**: Implement foundational base classes and core systems

**Estimated Effort**: 8-12 hours

**Phases**:
- [Phase A: Foundation Layer](./phase1-core-foundation/phase-a-foundation/) - 3 tasks (50 min)
- [Phase B: Core Systems](./phase1-core-foundation/phase-b-core-systems/) - 4 tasks (2.5 hours)
- [Phase C: Base Classes](./phase1-core-foundation/phase-c-base-classes/) - 5 tasks (3 hours)
- [Phase D: Framework Manager](./phase1-core-foundation/phase-d-framework-manager/) - 2 tasks (2 hours)

#### Phase A: Foundation Layer (3 tasks)
| Task | Name | Effort | Status |
|------|------|--------|--------|
| [CF-001](./phase1-core-foundation/phase-a-foundation/CF-001-singleton.md) | Singleton.cs | 20 min | 🔴 PENDING |
| [CF-002](./phase1-core-foundation/phase-a-foundation/CF-002-imodule.md) | IModule.cs | 15 min | 🔴 PENDING |
| [CF-003](./phase1-core-foundation/phase-a-foundation/CF-003-iservice.md) | IService.cs | 15 min | 🔴 PENDING |

#### Phase B: Core Systems (4 tasks)
| Task | Name | Effort | Dependencies | Status |
|------|------|--------|--------------|--------|
| [CF-004](./phase1-core-foundation/phase-b-core-systems/CF-004-eventbus.md) | EventBus.cs | 40 min | CF-001 | 🔴 PENDING |
| [CF-005](./phase1-core-foundation/phase-b-core-systems/CF-005-service-locator.md) | ServiceLocator.cs | 30 min | CF-001, CF-003 | 🔴 PENDING |
| [CF-006](./phase1-core-foundation/phase-b-core-systems/CF-006-data-manager.md) | DataManager.cs | 30 min | CF-001 | 🔴 PENDING |
| [CF-007](./phase1-core-foundation/phase-b-core-systems/CF-007-framework-logger.md) | FrameworkLogger.cs | 30 min | None | 🔴 PENDING |

#### Phase C: Base Classes (5 tasks)
| Task | Name | Effort | Dependencies | Status |
|------|------|--------|--------------|--------|
| [CF-008](./phase1-core-foundation/phase-c-base-classes/CF-008-base-data.md) | BaseData.cs | 20 min | None | 🔴 PENDING |
| [CF-009](./phase1-core-foundation/phase-c-base-classes/CF-009-base-domain.md) | BaseDomain.cs | 30 min | CF-008, CF-006 | 🔴 PENDING |
| [CF-010](./phase1-core-foundation/phase-c-base-classes/CF-010-base-module.md) | BaseModule.cs | 30 min | CF-002, CF-004, CF-005, CF-006 | 🔴 PENDING |
| [CF-011](./phase1-core-foundation/phase-c-base-classes/CF-011-base-service.md) | BaseService.cs | 30 min | CF-003, CF-004, CF-005, CF-006 | 🔴 PENDING |
| [CF-012](./phase1-core-foundation/phase-c-base-classes/CF-012-base-gameplay.md) | BaseGameplay.cs | 40 min | CF-004, CF-005 | 🔴 PENDING |

#### Phase D: Framework Manager (2 tasks)
| Task | Name | Effort | Dependencies | Status |
|------|------|--------|--------------|--------|
| [CF-013](./phase1-core-foundation/phase-d-framework-manager/CF-013-framework-config.md) | FrameworkConfig.cs | 30 min | None | 🔴 PENDING |
| [CF-014](./phase1-core-foundation/phase-d-framework-manager/CF-014-framework-manager.md) | FrameworkManager.cs | 90 min | All previous | 🔴 PENDING |

---

### ⏳ [Phase 2: Core Modules](./phase2-core-modules/README.md)
**Status**: PLANNING | **Tasks**: TBD | **Completion**: 0%

**Objective**: Implement game-independent core modules

**Estimated Effort**: 10-15 hours

**Modules**:
- UIModule - Canvas management and UI pooling
- AudioModule - BGM/SFX playback and volume control
- SceneModule - Scene loading and transitions
- NetworkModule - Basic networking (optional)

**Details**: To be specified after Phase 1 completion

---

### ⏳ [Phase 3: Example Implementation](./phase3-example/README.md)
**Status**: PLANNING | **Tasks**: TBD | **Completion**: 0%

**Objective**: Create complete RPG example demonstrating all 6 layers

**Estimated Effort**: 12-18 hours

**Components**:
- Data Layer: ItemData, PlayerData
- Domain Layer: ItemDomain, PlayerStatsDomain
- Interface Layer: IInventorySystem, IBattleSystem
- Service Layer: InventoryService, BattleService
- Gameplay Layer: PlayerController
- Events: ItemAddedEvent, PlayerDamagedEvent

**Details**: To be specified after Phase 2 completion

---

### ⏳ [Phase 4: Documentation & Testing](./phase4-documentation/README.md)
**Status**: PLANNING | **Tasks**: TBD | **Completion**: 0%

**Objective**: Comprehensive documentation and testing coverage

**Estimated Effort**: 6-8 hours

**Areas**:
- API Documentation generation
- Tutorial documentation
- Unit tests (>80% coverage)
- Integration tests
- Performance benchmarks

**Details**: To be specified after Phase 3 completion

---

## 🎯 How to Use This TODO System

### For Task Execution

**Starting a New Task:**
1. Check [Progress Dashboard](./PROGRESS.md) for current phase
2. Navigate to phase folder (e.g., [Phase 1](./phase1-core-foundation/README.md))
3. Find next pending task (e.g., [CF-001](./phase1-core-foundation/phase-a-foundation/CF-001-singleton.md))
4. Read task details and checklist
5. Read related [SPEC documentation](../spec/05-core-systems/foundation/singleton.md)
6. Follow implementation checklist
7. Complete validation criteria
8. Mark task as completed
9. Move to next task

**Task Document Structure:**
Each task document contains:
- 📊 Task Overview (ID, status, priority, effort, dependencies)
- 🎯 목표 (Goal and purpose)
- 📝 상세 설명 (Detailed description)
- ✅ 구현 체크리스트 (Implementation checklist)
- 🧪 검증 기준 (Validation criteria)
- 📚 참고 문서 (Reference documents)
- ✔️ 완료 조건 (Completion criteria)
- 📦 Git Commit (Commit message template)
- 🔗 연관 태스크 (Related tasks)
- 📅 Timeline (Dates and duration)
- 💬 Notes (Tips and known issues)

### For Progress Tracking

**Daily Progress Review:**
- Check [Progress Dashboard](./PROGRESS.md)
- Review completed tasks from previous day
- Identify next tasks
- Update task status

**Weekly Planning:**
- Review phase progress
- Adjust estimates based on actual time spent
- Identify blockers
- Plan next week's focus

### For Project Management

**Status Indicators:**
- 🔴 PENDING - Not started
- 🟡 IN_PROGRESS - Currently working
- 🟢 COMPLETED - Finished and validated
- ⏸️ BLOCKED - Waiting on dependency
- 🚧 ON_HOLD - Temporarily paused

**Updating Task Status:**
1. Open task markdown file
2. Update `status` field in metadata
3. Update status icon in README
4. Update [Progress Dashboard](./PROGRESS.md)
5. Commit changes

---

## 📈 Progress Dashboard Link

For detailed metrics, timelines, and analytics:

👉 **[View Full Progress Dashboard](./PROGRESS.md)**

Includes:
- Phase-by-phase breakdown
- Task completion timeline
- Effort tracking (estimated vs actual)
- Blocker analysis
- Velocity metrics

---

## 🔗 Related Documentation

### SPEC References
- [Project Index](../index.md)
- [SPEC Index](../spec/README.md)
- [Core Systems SPEC](../spec/05-core-systems/README.md)
- [Core Foundation Details](../spec/05-core-systems/foundation/singleton.md)

### Development Resources
- [Coding Conventions](../../doc/guidelines/coding-conventions.md)
- [Development Workflow](../../doc/workflow/development-workflow.md)
- [Documentation Rules](../../doc/guidelines/documentation-rules.md)

### Tools
- [Scope Validation](../../../scripts/scope_validate.py)
- [Document Validation](../../../scripts/doc_validate.py)

---

## 📝 Task Management Guidelines

### Task Creation
- **Granularity**: 15 min - 2 hours per task
- **Dependencies**: Clearly specified
- **Validation**: Measurable completion criteria
- **Documentation**: Link to relevant SPEC

### Task Execution
- **One at a time**: Single focus
- **Checklist-driven**: Follow all steps
- **Validation**: Test before marking complete
- **Documentation**: Update as you go

### Task Completion
- **All criteria met**: Don't skip validation
- **Tests passing**: If applicable
- **Documentation updated**: If needed
- **Committed**: Git commit with proper message

---

**Document Status**: Active
**Maintained By**: HaroFramework Team
**Last Updated**: 2025-10-26
**Current Phase**: Phase 1 - Core Foundation
**Next Task**: [CF-001: Singleton.cs](./phase1-core-foundation/phase-a-foundation/CF-001-singleton.md)
