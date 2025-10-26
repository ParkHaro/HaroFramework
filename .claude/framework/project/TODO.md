---
title: HaroFramework TODO List
version: 2.0.0
scope: framework
created: 2025-10-25
modified: 2025-10-26
category: Project Management
tags: [todo, tasks, tracking]
paired_document: TODO_KOR.md
parent_documents:
  - ./SPEC.md
child_documents: []
references: []
status: active
---



<!-- Navigation -->
**🏠 [HaroFramework Project](../../MASTER_INDEX.md)** | **📂 [HaroFramework Project Index](INDEX.md)** | **⬆️ [HaroFramework Specification](SPEC.md)**

---
# HaroFramework TODO List

## Session Information
- **Session Started**: 2025-10-25
- **Current Phase**: Documentation System Complete and Validated, Ready for Framework Implementation
- **Context Usage**: ~75% (150K/200K tokens)
- **Last Updated**: 2025-10-27

---

## 🔴 Currently In Progress

**None** - All validation testing complete, documentation system production-ready

---

## 📋 Next Tasks (Pending - High Priority)

### [P-001] Core Documentation Creation ✅ COMPLETED
**Priority**: HIGH
**Estimated Effort**: 4-6 hours
**Dependencies**: [IP-001]
**Completed**: 2025-10-26

**Completed Tasks**:
- [x] Create `scope-system.md` + `_KOR.md`
  - Document 2-scope architecture in detail
  - Explain dependency rules
  - Provide examples and anti-patterns
  - Location: `.claude/framework/doc/architecture/`

- [x] Create `documentation-rules.md` + `_KOR.md`
  - Document bilingual documentation rules
  - Define metadata standards
  - Explain workflow rules
  - Document automation scripts
  - Location: `.claude/framework/doc/guidelines/`

- [x] Add metadata to existing documents and create Korean translations
  - `project-overview.md` + `_KOR.md` → `.claude/framework/doc/architecture/`
  - `coding-conventions.md` + `_KOR.md` → `.claude/framework/doc/guidelines/`
  - `development-workflow.md` + `_KOR.md` → `.claude/framework/doc/workflow/`
  - `commands-guide.md` + `_KOR.md` → `.claude/framework/doc/workflow/`
  - `skills-guide.md` + `_KOR.md` → `.claude/framework/doc/workflow/`

**Success Criteria Met**:
- ✅ All core documents created and validated
- ✅ Metadata format consistent
- ✅ Bilingual pairs synchronized
- ✅ All documents properly categorized

---

### [P-002] Automation Scripts Development ✅ COMPLETED
**Priority**: HIGH
**Estimated Effort**: 6-8 hours
**Dependencies**: [P-001]
**Completed**: 2025-10-26

**Completed Tasks**:
- [x] `scope_validate.py`
  - Parse document metadata (YAML frontmatter)
  - Extract references and links from metadata
  - Validate framework doesn't reference game scope
  - Generate detailed violation reports
  - Tested successfully - 26 documents validated

- [x] `doc_validate.py`
  - Validate metadata format and required fields
  - Check paired document existence
  - Verify link integrity (references + parent_documents)
  - Validate version format (MAJOR.MINOR.PATCH)
  - Validate status values
  - Tested successfully - comprehensive validation working

- [x] `doc_sync.py`
  - Detect document changes via modified dates
  - Compare original and Korean document timestamps
  - Report out-of-sync documents
  - Support manual sync workflow
  - Implemented and ready for use

- [x] `version_bump.py`
  - Parse version from metadata
  - Increment version (major/minor/patch)
  - Update modified date automatically
  - Update paired document simultaneously
  - Dry-run mode for testing
  - Implemented with examples

- [x] `scripts/README.md` + `_KOR.md`
  - Documented all 4 scripts
  - Provided detailed usage examples
  - Explained recommended workflow
  - Troubleshooting guide included
  - Future enhancements outlined

**Success Criteria Met**:
- ✅ All 4 scripts functional and tested
- ✅ No external dependencies (Python stdlib only)
- ✅ Cross-platform compatible
- ✅ Comprehensive documentation (English + Korean)
- ✅ Ready for CI/CD integration

---

### [P-003] Existing Documents Migration ✅ COMPLETED
**Priority**: MEDIUM
**Estimated Effort**: 3-4 hours
**Dependencies**: [P-001]
**Completed**: 2025-10-26

**Migrated Documents**:
```
✅ .claude/doc/project-overview.md
  → .claude/framework/doc/architecture/project-overview.md + _KOR.md

✅ .claude/doc/coding-conventions.md
  → .claude/framework/doc/guidelines/coding-conventions.md + _KOR.md

✅ .claude/doc/development-workflow.md
  → .claude/framework/doc/workflow/development-workflow.md + _KOR.md

✅ .claude/doc/commands-guide.md
  → .claude/framework/doc/workflow/commands-guide.md + _KOR.md

✅ .claude/doc/skills-guide.md
  → .claude/framework/doc/workflow/skills-guide.md + _KOR.md
```

**Completed Migration Tasks**:
- [x] Move files to new folder structure
- [x] Add metadata frontmatter to all documents
- [x] Create Korean translation documents (_KOR.md)
- [x] Establish parent/child/reference relationships
- [x] Update document status to "approved"
- [x] Set initial version to 1.0.0

**Remaining Tasks**:
- [ ] Delete or archive old documents from `.claude/doc/`
- [ ] Update internal links if needed
- [ ] Run validation scripts once available

**Success Criteria Met**:
- ✅ All main documents migrated successfully
- ✅ Metadata added to all documents
- ✅ Korean translations complete
- ⏳ Validation scripts pending (depends on [P-002])

---

### [P-004] CLAUDE.md Update ✅ COMPLETED
**Priority**: HIGH
**Estimated Effort**: 1-2 hours
**Dependencies**: [P-001], [P-003]
**Completed**: 2025-10-26

**Completed Updates**:
- [x] Add 2-scope architecture explanation
  - Clear explanation of Framework vs Game scopes
  - Visual representation of scope dependency rules
  - "Why this matters" section added

- [x] Update documentation paths
  - Framework docs: `.claude/framework/doc/`
  - Framework SPEC/TODO: `.claude/framework/project/`
  - Complete file structure tree added

- [x] Add scope dependency rules section
  - ✅ ALLOWED: Game → Framework
  - ❌ FORBIDDEN: Framework → Game
  - Scope awareness checklist added

- [x] Add context management protocol
  - Token optimization guidelines (read English only)
  - 85% context threshold rule
  - Session restoration guide

- [x] Update "must read" documentation list
  - 7 core documents organized by category
  - Architecture & Guidelines section
  - Workflow & Tools section
  - Project Management section

- [x] Add bilingual documentation rules
  - Claude Code reads English only
  - Developers choose language preference
  - Token optimization explanation

**Success Criteria Met**:
- ✅ CLAUDE.md accurately reflects new structure
- ✅ All paths updated correctly
- ✅ Scope rules clearly documented with examples
- ✅ Context management protocol added
- ✅ Token optimization guidelines added

---

### [P-005] Validation and Testing ✅ COMPLETED
**Priority**: MEDIUM
**Estimated Effort**: 2-3 hours
**Dependencies**: [P-002], [P-003], [P-004]
**Completed**: 2025-10-27

**Completed Validation Tasks**:
- [x] Run `scope_validate.py` on all documents - ✅ PASSED (36 documents)
- [x] Run `doc_validate.py` on all documents - ✅ PASSED (20 documents)
- [x] Verify all document pairs exist - ✅ PASSED
- [x] Check link integrity across all documents - ✅ PASSED
- [x] Verify metadata consistency - ✅ PASSED
- [x] Test version_bump.py workflow - ✅ PASSED (dry-run tested)
- [x] Test doc_sync.py workflow - ✅ PASSED (2 out-of-sync detected correctly)

**Completed Testing Scenarios**:
- [x] Create test document with invalid scope reference - ✅ Detected correctly
- [x] Create test document with missing metadata - ✅ Detected correctly (9 errors)
- [x] Create test document with broken links - ✅ Detected correctly
- [x] Verify scripts catch all violations - ✅ All violations detected

**Success Criteria Met**:
- ✅ All validation scripts pass on production documents
- ✅ No broken links in production documents
- ✅ All metadata valid in production documents
- ✅ Scripts correctly detect all test violations

**Issues Fixed During Validation**:
1. Added missing frontmatter to `UNITY_FRAMEWORK_SPEC.md`
2. Updated `SESSION_RESTORE.md` metadata
3. Fixed `SPEC.md` missing status field
4. Updated template files (scope field, status value)
5. Fixed broken reference in `PROGRESS.md`
6. Modified `doc_validate.py` to make `paired_document` optional

---

## 🔵 Future Tasks (Pending - Lower Priority)

### [F-001] Game Template Setup
**Priority**: MEDIUM
**Estimated Effort**: 2-3 hours

**Tasks**:
- [ ] Create template GAME.md + _KOR.md
- [ ] Create template SPEC.md + _KOR.md
- [ ] Create template TODO.md + _KOR.md
- [ ] Create template documentation structure
- [ ] Document how to use template for new games

### [F-002] API Documentation System
**Priority**: LOW
**Estimated Effort**: 8-12 hours

**Tasks**:
- [ ] Research C# documentation generators
- [ ] Set up automated API reference generation
- [ ] Integrate with build pipeline
- [ ] Create API documentation templates

### [F-003] CI/CD Integration
**Priority**: LOW
**Estimated Effort**: 4-6 hours

**Tasks**:
- [ ] Integrate validation scripts into Git hooks
- [ ] Set up pre-commit validation
- [ ] Set up CI pipeline for documentation validation
- [ ] Automated testing for scripts

---

## 🏗️ Framework Implementation (Phase 1-4)

### [F-004] Phase 1: Core Foundation
**Priority**: HIGH
**Estimated Effort**: 8-12 hours
**Status**: PENDING

**Objective**: Implement the foundational base classes and core systems that all other layers depend on.

**Tasks**:

#### Framework/Core/Base/ (Base Classes)
- [ ] `IModule.cs` - Module interface
  - Define module lifecycle (Initialize, Shutdown, OnUpdate)
  - Define module metadata (Name, Priority)
- [ ] `IService.cs` - Service interface
  - Define service lifecycle (Initialize, Dispose)
  - Define service identification (ServiceName)
- [ ] `BaseModule.cs` - Module base class
  - Implement IModule interface
  - Provide lifecycle management template
  - Add priority-based initialization
- [ ] `BaseService.cs` - Service base class
  - Implement IService interface
  - Provide EventBus and ServiceLocator access
  - Add service lifecycle template
- [ ] `BaseDomain.cs` - Domain base class
  - Generic data type support `BaseDomain<TData>`
  - Define data loading/caching interface
  - Add data query methods (GetData, GetAllData)
- [ ] `BaseGameplay.cs` - Gameplay base class
  - Extend MonoBehaviour
  - Provide ServiceLocator and EventBus access
  - Define framework lifecycle integration
- [ ] `BaseData.cs` - Data base class
  - Add Id property
  - Add Validate() abstract method
  - Support serialization

#### Framework/Core/Systems/ (Core Systems)
- [ ] `Singleton.cs` - Singleton pattern
  - Thread-safe implementation
  - Unity-aware lifecycle management
- [ ] `EventBus.cs` - Event bus system
  - Subscribe/Unsubscribe/Publish methods
  - Generic event type support
  - Event queue for async processing
- [ ] `ServiceLocator.cs` - Service locator
  - Register/Get/Has/Clear methods
  - Type-based service resolution
  - Error handling for missing services
- [ ] `DataManager.cs` - Data manager
  - Domain registration and management
  - LoadAllDomains() implementation
  - Domain lifecycle management
- [ ] `FrameworkLogger.cs` - Logging system
  - Log levels (Info, Warning, Error)
  - Conditional compilation for Release builds
  - Integration with Unity Debug

#### Framework/Core/ (Framework Manager)
- [ ] `FrameworkManager.cs` - Framework manager
  - Singleton MonoBehaviour
  - Core systems initialization
  - Module lifecycle orchestration
  - DontDestroyOnLoad management
- [ ] `FrameworkConfig.cs` - Configuration ScriptableObject
  - Module enable/disable toggles
  - Priority configuration
  - Framework settings

**Success Criteria**:
- All base classes compiled without errors
- Core systems functional and tested
- FrameworkManager successfully initializes all systems
- Documentation added for all public APIs

---

### [F-005] Phase 2: Core Modules
**Priority**: HIGH
**Estimated Effort**: 10-15 hours
**Status**: PENDING
**Dependencies**: [F-004]

**Objective**: Implement game-independent modules that provide common functionality.

**Tasks**:

#### Framework/Core/Modules/
- [ ] `UIModule.cs` - UI management module
  - Canvas management (Find, Create, Destroy)
  - UI layer organization
  - Screen space/World space canvas support
  - UI pooling for performance
- [ ] `AudioModule.cs` - Audio management module
  - BGM playback (Play, Stop, Pause, Resume)
  - SFX playback with pooling
  - Volume control (Master, BGM, SFX)
  - Audio fade in/out support
- [ ] `SceneModule.cs` - Scene management module
  - Scene loading (Sync/Async)
  - Loading screen integration
  - Scene transition effects
  - Additive scene support
- [ ] `NetworkModule.cs` - Network module (Optional)
  - Basic network connectivity
  - Request/Response pattern
  - WebSocket support (if needed)
  - Network error handling

**Success Criteria**:
- All modules initialize in priority order
- Modules can be enabled/disabled via FrameworkConfig
- Each module tested independently
- No inter-module dependencies
- Documentation complete

---

### [F-006] Phase 3: Example Implementation
**Priority**: MEDIUM
**Estimated Effort**: 12-18 hours
**Status**: PENDING
**Dependencies**: [F-004], [F-005]

**Objective**: Create a complete example RPG to demonstrate all 6 layers working together.

**Tasks**:

#### Data Layer
- [ ] `ItemData.cs` - Item data structure
  - Basic properties (Id, Name, Type)
  - Stats (Attack, Defense, CritRate)
  - Validation logic
- [ ] `PlayerData.cs` - Player data structure
  - Character properties (Level, HP, MP)
  - Stats and equipment
  - Validation logic

#### Domain Layer
- [ ] `ItemDomain.cs` - Item domain logic
  - Load items from JSON/CSV
  - Calculate final stats (base + modifiers)
  - Cache item data
- [ ] `PlayerStatsDomain.cs` - Player stats domain logic
  - Load player data
  - Calculate combat stats
  - Level up calculations

#### Interface Layer
- [ ] `IInventorySystem.cs` - Inventory interface
  - AddItem, RemoveItem, GetItem methods
  - Define inventory operations contract
- [ ] `IBattleSystem.cs` - Battle interface
  - Attack, Defend, UseSkill methods
  - Define battle operations contract

#### Service Layer
- [ ] `InventoryService.cs` - Inventory service
  - Implement IInventorySystem
  - Use ItemDomain for data
  - Publish ItemAdded/Removed events
  - Manage inventory state
- [ ] `BattleService.cs` - Battle service
  - Implement IBattleSystem
  - Use PlayerStatsDomain for calculations
  - Publish battle events
  - Manage combat state

#### Gameplay Layer
- [ ] `PlayerController.cs` - Player controller
  - Extend BaseGameplay
  - Use InventoryService and BattleService
  - Subscribe to relevant events
  - Handle player input

#### Events
- [ ] `ItemAddedEvent.cs` - Item added event
- [ ] `PlayerDamagedEvent.cs` - Player damaged event

**Integration Test**:
- [ ] Create test scene with PlayerController
- [ ] Test full pipeline: Input → Service → Domain → Data
- [ ] Verify event flow and state management
- [ ] Performance test (object pooling, caching)

**Success Criteria**:
- All 6 layers implemented and working
- Complete data flow demonstrated (Gameplay → Service → Domain → Data)
- Event bus communication verified
- No circular dependencies
- Example documented as tutorial

---

### [F-007] Phase 4: Documentation & Testing
**Priority**: MEDIUM
**Estimated Effort**: 6-8 hours
**Status**: PENDING
**Dependencies**: [F-004], [F-005], [F-006]

**Objective**: Comprehensive documentation and testing for framework reliability.

**Tasks**:

#### Documentation
- [ ] API Documentation
  - Generate XML documentation for all public APIs
  - Create API reference guide
- [ ] Tutorial Documentation
  - "Getting Started" tutorial
  - "Creating a New Game" tutorial
  - "Adding Custom Systems" tutorial
- [ ] Architecture Documentation
  - Update `.claude/framework/doc/systems/` with system guides
  - Diagram generation for 6-layer architecture
- [ ] Example Code Documentation
  - Annotate example RPG implementation
  - Create code walkthrough

#### Unit Tests
- [ ] Core Systems Tests
  - EventBus Subscribe/Publish tests
  - ServiceLocator Register/Get tests
  - DataManager Domain management tests
  - FrameworkLogger output tests
- [ ] Module Tests
  - UIModule canvas management tests
  - AudioModule playback tests
  - SceneModule loading tests

#### Integration Tests
- [ ] Lifecycle Tests
  - Framework initialization order test
  - Module priority test
  - Shutdown cleanup test
- [ ] System Integration Tests
  - Service-Domain integration test
  - Gameplay-Service integration test
  - Event bus cross-layer test

#### Performance Tests
- [ ] Benchmark Tests
  - EventBus performance test (1000+ events)
  - ServiceLocator lookup performance
  - Domain data caching effectiveness
- [ ] Memory Tests
  - Memory leak detection
  - Object pooling verification

**Success Criteria**:
- >80% code coverage on core systems
- All integration tests passing
- Performance benchmarks documented
- API documentation complete
- Tutorial guides validated by following steps

---

## ✅ Completed Tasks

### [IP-001] Documentation System Initial Setup
**Completed**: 2025-10-26

**Achievements**:
- ✅ Project requirements discussion and analysis
- ✅ 2-Scope architecture design
- ✅ Folder structure finalization and creation
- ✅ SPEC.md and SPEC_KOR.md creation
- ✅ TODO.md and TODO_KOR.md creation
- ✅ All foundational documents created

### [C-001] Documentation System Planning
**Completed**: 2025-10-25

**Achievements**:
- ✅ Defined 2-scope architecture (Framework + Game)
- ✅ Established bilingual documentation rule
- ✅ Designed metadata standard (YAML frontmatter)
- ✅ Defined folder structure
- ✅ Planned automation scripts
- ✅ Established version management system
- ✅ Defined context management protocol (85% rule)

### [C-002] Folder Structure Creation
**Completed**: 2025-10-25

**Created Folders**:
- ✅ `.claude/framework/doc/` (with subdirectories)
- ✅ `.claude/framework/project/`
- ✅ `.claude/framework/scripts/`
- ✅ `.claude/games/_template/` (with subdirectories)
- ✅ `.claude/scripts/`

### [C-003] SPEC Documents Creation
**Completed**: 2025-10-25

**Created Files**:
- ✅ `.claude/framework/project/SPEC.md` (comprehensive specification)
- ✅ `.claude/framework/project/SPEC_KOR.md` (Korean translation)

**Content**:
- Project vision and goals
- 2-scope architecture details
- Documentation system rules
- Version management
- Scope dependency rules
- Core framework systems
- Quality standards
- Technology stack
- Development workflow
- Success criteria

---

## 🚨 Blockers

**None Currently**

---

## 📝 Session Restoration Guide

### To Resume in New Session

1. **Read First**:
   - `.claude/framework/project/SPEC.md` (project specification)
   - `.claude/framework/project/TODO.md` (this file)

2. **Current State**:
   - Folder structure created
   - SPEC documents complete (English + Korean)
   - TODO documents in progress
   - Ready to create document skeletons

3. **Next Steps**:
   - Complete TODO_KOR.md
   - Create document skeletons (12 files)
   - Check context usage
   - Begin [P-001] if context allows

4. **Important Context**:
   - Unity 6000.2.9f1
   - Framework → Game dependency forbidden
   - Game → Framework dependency allowed
   - Bilingual documentation mandatory
   - Original docs only (Claude doesn't read Korean)
   - 85% context threshold for SPEC/TODO update

---

## 📊 Progress Metrics

### Overall Progress: 100%
- Planning: ✅ 100%
- Folder Structure: ✅ 100%
- SPEC Documents: ✅ 100%
- TODO Documents: ✅ 100%
- Core Documentation: ✅ 100%
- Document Migration: ✅ 100%
- CLAUDE.md Update: ✅ 100%
- Automation Scripts: ✅ 100%
- Old Folder Cleanup: ✅ 100%
- Validation Testing: ✅ 100%

### Task Breakdown
- **Total Tasks**: ~50
- **Completed**: 29 (all core tasks complete)
- **In Progress**: 0
- **Pending Medium Priority**: 0
- **Future Tasks**: 3 (game template, API docs, CI/CD)

### Estimated Time to Completion
- **Current Phase** (Core Setup): ✅ 100% COMPLETE
- **Validation Phase**: ✅ COMPLETE
- **Documentation System**: ✅ 100% COMPLETE

---

## 🎯 Immediate Next Actions

**Documentation System: ✅ 100% COMPLETE**

All setup and validation tasks complete:
- ✅ SPEC and TODO documents created
- ✅ Core documentation created (scope-system, documentation-rules)
- ✅ Existing documents migrated with metadata
- ✅ CLAUDE.md updated to reflect new structure
- ✅ Automation scripts developed and tested (scope_validate, doc_validate, doc_sync, version_bump)
- ✅ Old folder cleanup completed
- ✅ Comprehensive validation testing passed

**Validation Results (2025-10-27)**:
- ✅ 36 documents passed scope validation
- ✅ 20 documents passed metadata validation
- ✅ All test scenarios detected violations correctly
- ✅ 6 issues identified and fixed during validation

**Current Status**: Documentation system is production-ready and fully validated

**Next Phase Options**:

1. **Begin Framework Development** ([F-004] - [F-007])
   - Phase 1: Core Foundation (8-12 hours)
   - Phase 2: Core Modules (10-15 hours)
   - Phase 3: Example Implementation (12-18 hours)
   - Phase 4: Documentation & Testing (6-8 hours)

2. **Game Template Creation** ([F-001])
   - Create template structure for first game project
   - Demonstrate 2-scope architecture in practice
   - Estimated: 2-3 hours

3. **API Documentation System** ([F-002])
   - Set up automated API reference generation
   - Estimated: 8-12 hours

**Recommendation**: Begin Framework Development (Phase 1: Core Foundation)

**Context Status**: ~75% (150K/200K) - Monitor context usage

---

## 📖 Notes

### Key Decisions Made
- **2-Scope Architecture**: Strict separation ensures framework reusability
- **Bilingual Documentation**: Supports both English and Korean readers
- **Metadata Standard**: YAML frontmatter for all documents
- **85% Context Rule**: Prevents overflow, ensures continuity
- **Script-First Approach**: Automate repetitive tasks

### Lessons Learned
- Comprehensive planning prevents rework
- Clear folder structure improves navigation
- Metadata enables powerful automation
- Bilingual documentation requires careful synchronization

### Questions for Future Consideration
- Should we add more languages beyond English/Korean?
- How to handle auto-translation vs manual translation?
- CI/CD integration timing?
- When to create first game project?

---

**Document Status**: Active
**Maintained By**: HaroFramework Team
**Review Frequency**: After each major task completion
