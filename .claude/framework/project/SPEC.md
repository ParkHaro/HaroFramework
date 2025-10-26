---
title: HaroFramework Specification
version: 2.0.0
scope: framework
created: 2025-10-25
modified: 2025-10-26
category: Project Management
tags: [specification, architecture, documentation]
paired_document: SPEC_KOR.md
parent_documents: []
child_documents: []
references: []
status: approved
---



<!-- Navigation -->
**🏠 [HaroFramework Project](../../MASTER_INDEX.md)** | **📂 [HaroFramework Project Index](INDEX.md)** | **⬆️ [HaroFramework Project Index](INDEX.md)**

---
# HaroFramework Specification

## 1. Project Vision

### 1.1 Overview
HaroFramework is a reusable Unity game framework designed to serve as a foundation for developing games across various genres. The framework provides core systems, tools, and patterns that can be leveraged to accelerate game development while maintaining code quality and consistency.

### 1.2 Goals
- **Reusability**: Create a framework that can be used across multiple game projects
- **Extensibility**: Design systems that can be easily extended for specific game needs
- **Quality**: Maintain high code quality with comprehensive testing and documentation
- **Performance**: Ensure optimal performance for production games
- **Developer Experience**: Provide clear documentation and intuitive APIs

### 1.3 Target Use Cases
- Action games
- RPG games
- Puzzle games
- Platformers
- And other Unity-based game genres

---

## 2. Architecture

### 2.1 2-Scope System

The project uses a strict 2-scope architecture to separate framework concerns from game-specific implementation:

#### Framework Scope (Independent)
- **Purpose**: Provides reusable game systems and utilities
- **Independence**: Must not reference or depend on any game-specific code
- **Location**: `.claude/framework/`
- **Scope**: Core systems, tools, utilities, common patterns

#### Game Scope (Framework-Dependent)
- **Purpose**: Implements specific game logic and content
- **Dependency**: Can reference and use Framework scope
- **Location**: `.claude/games/[game-name]/`
- **Scope**: Game-specific mechanics, content, design

#### Dependency Rules
```
✅ ALLOWED:   Game → Framework (Game can use Framework)
❌ FORBIDDEN: Framework → Game (Framework cannot know about Game)
```

**Rationale**: This ensures the framework remains reusable across different game projects without coupling to specific game implementations.

### 2.2 Folder Structure

```
.claude/
│
├── framework/                        # 🔵 Framework Scope (Independent)
│   ├── doc/                         # Framework documentation
│   │   ├── guidelines/              # Development guidelines
│   │   │   ├── documentation-rules.md
│   │   │   ├── documentation-rules_KOR.md
│   │   │   ├── coding-conventions.md
│   │   │   └── coding-conventions_KOR.md
│   │   │
│   │   ├── architecture/            # Architecture documentation
│   │   │   ├── project-overview.md
│   │   │   ├── project-overview_KOR.md
│   │   │   ├── scope-system.md
│   │   │   └── scope-system_KOR.md
│   │   │
│   │   ├── systems/                 # Core systems documentation
│   │   │   ├── player/
│   │   │   ├── ai/
│   │   │   ├── ui/
│   │   │   └── audio/
│   │   │
│   │   ├── api/                     # API reference (auto-generated)
│   │   │
│   │   └── workflow/                # Development workflow
│   │       ├── development-workflow.md
│   │       └── development-workflow_KOR.md
│   │
│   ├── project/                     # Framework project management
│   │   ├── SPEC.md                  # This file
│   │   ├── SPEC_KOR.md
│   │   ├── TODO.md
│   │   └── TODO_KOR.md
│   │
│   └── scripts/                     # Framework-specific scripts
│       └── README.md
│
├── games/                            # 🟢 Game Scope (Framework-Dependent)
│   ├── _template/                   # New game project template
│   │   ├── doc/
│   │   │   ├── design/              # Game design documents
│   │   │   ├── mechanics/           # Gameplay mechanics
│   │   │   ├── levels/              # Level documentation
│   │   │   └── assets/              # Asset documentation
│   │   ├── project/
│   │   │   ├── SPEC.md
│   │   │   ├── SPEC_KOR.md
│   │   │   ├── TODO.md
│   │   │   └── TODO_KOR.md
│   │   └── GAME.md                  # Game-specific Claude config
│   │
│   └── [game-name]/                 # Actual game projects (future)
│
├── scripts/                          # 🔧 Common automation scripts
│   ├── doc_sync.py                  # Document synchronization
│   ├── doc_validate.py              # Link/metadata validation
│   ├── scope_validate.py            # Scope dependency validation
│   ├── version_bump.py              # Version management
│   └── README.md
│
├── CLAUDE.md                         # Framework work configuration
└── README.md                         # Project README
```

---

## 3. Documentation System

### 3.1 Bilingual Documentation Rule

**Every document must be duplicated in both English and Korean.**

#### File Naming Convention
- **Original Document**: `{document}.md` (English)
- **Korean Document**: `{document}_KOR.md` (Korean)

#### Examples
```
documentation-rules.md       → Original (English)
documentation-rules_KOR.md   → Korean translation

SPEC.md                      → Original (English)
SPEC_KOR.md                  → Korean translation
```

#### Synchronization Rules
1. **Korean Document Language**: Must be written 100% in Korean
2. **Content Linkage**: Both documents must maintain identical content
3. **Update Synchronization**: When one document is updated, the paired document must be updated accordingly
4. **Structure Consistency**: Both documents must maintain the same structure, headings, and organization

### 3.2 Metadata Standard

All documents must include YAML frontmatter metadata at the beginning.

#### Required Fields
```yaml
---
title: "Document Title"
version: "1.0.0"                    # Semantic versioning
scope: "framework|game"             # Scope classification
created: "2025-10-25"               # Creation date
modified: "2025-10-25"              # Last modification date
paired_document: "filename_KOR.md"  # Paired document reference
---
```

#### Optional Fields
```yaml
category: "Category"                # Document category
tags: [tag1, tag2]                  # Searchable tags
status: "draft|review|approved"     # Document status
parent_documents: []                # Parent document links
child_documents: []                 # Child document links
references: []                      # Referenced documents
```

#### Scope Field Values
- `framework`: Framework scope documents
- `game`: Game scope documents

**Purpose**: The `scope` field enables automated validation to prevent forbidden cross-scope references.

### 3.3 Version Management

#### Semantic Versioning (MAJOR.MINOR.PATCH)

**MAJOR** - Increment when:
- Document structure is significantly reorganized
- Breaking changes to document format or conventions
- Fundamental changes to documented systems
- Backward compatibility is broken

**MINOR** - Increment when:
- New sections or chapters are added
- Content is expanded with new information
- New features or systems are documented
- Backward-compatible additions

**PATCH** - Increment when:
- Typos or grammar errors are fixed
- Examples are improved or clarified
- Minor wording improvements
- Formatting corrections

#### Version Update Process
1. Determine the type of change (MAJOR/MINOR/PATCH)
2. Update version in metadata
3. Update `modified` date
4. Update paired document version to match
5. Document change in CHANGELOG (if applicable)

#### Version Management Script
Use `version_bump.py` to automate version updates:
```bash
python .claude/scripts/version_bump.py [document] [major|minor|patch]
```

### 3.4 Document Workflow Rules

#### Reading Optimization (Token Efficiency)
**Rule**: Claude Code reads ONLY original documents (*.md), NOT Korean documents (*_KOR.md)

**Rationale**:
- Reduces token usage by ~50%
- Original English documents contain all necessary information
- Korean documents are for human readers who prefer Korean

**Implementation**: Document reading tools and processes should exclude `*_KOR.md` files.

#### Context Management Protocol
**Rule**: When context usage reaches 85%, write SPEC/TODO and execute `/clear`

**Process**:
1. Monitor context usage during work
2. At 85% threshold:
   - Update current SPEC.md with progress
   - Update current TODO.md with remaining tasks
   - Update both Korean paired documents
   - Provide session restoration guide
   - Execute `/clear`
3. Resume work in new session using updated SPEC/TODO

**Rationale**: Prevents context overflow and ensures continuity across sessions.

#### Script-First Approach
**Rule**: When repetitive tasks are detected, propose script creation to the user

**Examples of Scriptable Tasks**:
- Document synchronization (doc_sync.py)
- Link validation (doc_validate.py)
- Version bumping (version_bump.py)
- Metadata validation
- Batch document operations

**Benefits**:
- Reduces token usage
- Ensures consistency
- Saves time in future operations
- Reduces human error

#### Folder Structure Management
**Rule**: Claude Code proposes appropriate folder structures before document operations

**Process**:
1. Analyze document purpose and category
2. Propose logical folder location
3. Wait for user approval
4. Create folders if approved
5. Document the structure

**Rationale**: Maintains organized, navigable documentation structure.

### 3.5 Document Linking System

**Rule**: Related documents must be linked hierarchically

#### Link Types
- **Parent-Child**: Hierarchical relationship (overview → details)
- **References**: Cross-references between related documents
- **See Also**: Related documents for additional context

#### Metadata Linking
```yaml
parent_documents:
  - "../SPEC.md"
child_documents:
  - "systems/player.md"
  - "systems/ai.md"
references:
  - "../guidelines/coding-conventions.md"
```

#### Link Validation
- Use `doc_validate.py` to verify all links are valid
- Detect broken links
- Ensure bidirectional linking where appropriate
- Verify scope boundaries are respected

#### Scope-Aware Linking
```yaml
# Framework document
references:
  - "./other-framework-doc.md"      # ✅ OK
  - "../../games/game1/design.md"   # ❌ FORBIDDEN

# Game document
references:
  - "../../framework/systems/player.md"  # ✅ OK
  - "./game-design.md"                   # ✅ OK
```

### 3.6 Automation Scripts

#### doc_sync.py - Document Synchronization
**Purpose**: Synchronize content between original and Korean documents

**Features**:
- Detect changes in original or Korean document
- Notify when synchronization is needed
- Support manual synchronization workflow
- Optional: Integration with translation APIs

**Usage**:
```bash
python .claude/scripts/doc_sync.py --check     # Check sync status
python .claude/scripts/doc_sync.py --sync      # Manual sync prompt
```

#### doc_validate.py - Document Validation
**Purpose**: Validate document integrity and metadata

**Checks**:
- Metadata format and required fields
- Paired document existence
- Link integrity (broken links)
- Version consistency between pairs
- Status field validity

**Usage**:
```bash
python .claude/scripts/doc_validate.py              # Validate all
python .claude/scripts/doc_validate.py [document]   # Validate one
```

#### scope_validate.py - Scope Dependency Validation
**Purpose**: Enforce scope dependency rules

**Validation**:
- Extract `scope` field from document metadata
- Parse all links and references
- Verify Framework documents don't reference Game documents
- Report violations with file and line information

**Algorithm**:
```python
def validate_layer_dependency(doc_path):
    scope = get_document_layer(doc_path)
    references = extract_all_references(doc_path)

    for ref in references:
        ref_layer = get_document_layer(ref)

        if scope == "framework" and ref_layer == "game":
            raise DependencyViolationError(
                f"FORBIDDEN: Framework document '{doc_path}' "
                f"cannot reference Game document '{ref}'"
            )

    return True
```

**Usage**:
```bash
python .claude/scripts/scope_validate.py              # Validate all
python .claude/scripts/scope_validate.py [document]   # Validate one
```

#### version_bump.py - Version Management
**Purpose**: Automate version updates

**Features**:
- Increment version (major/minor/patch)
- Update `modified` date automatically
- Update paired document version
- Generate CHANGELOG entry (optional)

**Usage**:
```bash
python .claude/scripts/version_bump.py [document] major
python .claude/scripts/version_bump.py [document] minor
python .claude/scripts/version_bump.py [document] patch
```

---

## 4. Scope Dependency Rules

### 4.1 Absolute Rules

#### ❌ FORBIDDEN: Framework → Game
Framework scope MUST NOT:
- Import or reference game-specific code
- Link to game documentation
- Contain game-specific logic or content
- Know about the existence of game projects

**Why**: Framework must remain reusable across all game projects.

#### ✅ ALLOWED: Game → Framework
Game scope CAN:
- Import and use framework systems
- Reference framework documentation
- Extend framework classes
- Build upon framework utilities

**Why**: Games are meant to leverage the framework.

### 4.2 Validation Methods

#### Metadata-Based Validation
Every document declares its scope:
```yaml
scope: framework  # or "game"
```

Validation script checks:
1. Document's declared scope
2. All referenced documents' scopes
3. Enforce: `framework` cannot reference `game`

#### Continuous Validation
- Run `scope_validate.py` before commits
- Integrate into CI/CD pipeline (future)
- Automated checks during document operations

#### Manual Review
- Code review checklist includes scope verification
- Architecture reviews examine scope boundaries
- Documentation reviews verify proper categorization

---

## 5. Core Framework Systems

### 5.1 Framework Architecture (6-Layer System)

The framework implements a strict 6-layer architecture with clear separation of concerns and dependency rules.

```
┌─────────────────────────────────────────────────────────┐
│                    Gameplay Layer                        │
│                   (게임플레이 영역)                        │
│  - MonoBehaviour 기반 게임 오브젝트                        │
│  - 실제 게임 로직 (Player, Enemy, UI 등)                  │
│  - BaseGameplay 상속                                     │
└─────────────────────────────────────────────────────────┘
                         ↓ 사용
┌─────────────────────────────────────────────────────────┐
│                     Service Layer                        │
│                    (서비스 영역)                          │
│  - 게임 특화 기능 구현                                     │
│  - Interface 구체 구현                                    │
│  - BaseService 상속                                      │
└─────────────────────────────────────────────────────────┘
                         ↓ 구현
┌─────────────────────────────────────────────────────────┐
│                   Interface Layer                        │
│                  (인터페이스 영역)                         │
│  - 게임 특화 계약 정의                                     │
│  - IService 인터페이스                                    │
│  - 의존성 역전 (DIP) 적용                                 │
└─────────────────────────────────────────────────────────┘
                         ↓ 참조
┌─────────────────────────────────────────────────────────┐
│                      Core Layer                          │
│                     (코어 영역)                           │
│  - 범용 모듈 (UI, Audio, Scene, Network)                 │
│  - BaseModule 상속                                       │
│  - 게임 독립적 (모든 프로젝트 공통)                         │
└─────────────────────────────────────────────────────────┘
       ↓ 사용                                  ↑ 접근
┌──────────────────────┐      ┌──────────────────────────┐
│    Domain Layer      │      │      Data Layer          │
│   (도메인 영역)       │←─────│     (데이터 영역)         │
│  - 데이터 가공/계산   │ 접근 │  - 순수 데이터 구조       │
│  - 게임 룰 적용       │      │  - BaseData 상속         │
│  - BaseDomain 상속    │      │  - 직렬화 가능           │
└──────────────────────┘      └──────────────────────────┘
```

#### Dependency Flow
```
Gameplay → Service → Interface → Core
   ↓          ↓
   └─→ Domain ←─┘
          ↓
        Data
```

**Principles**:
- Upper layers can reference lower layers
- Lower layers cannot reference upper layers
- Data layer is accessible from all layers (read-only)

#### Communication Methods
```
1. Direct Reference
   Gameplay → Service
   Service → Domain
   Domain → Data

2. Event Bus (EventBus)
   All layers ↔ All layers
   - Loose coupling
   - Asynchronous processing

3. Service Locator
   Gameplay/Service → Registered Services
   - Centralized management
   - Runtime resolution
```

### 5.2 Layer Details

#### 5.2.1 Data Layer (데이터 계층)

**Purpose**:
- Define pure data structures
- Support serialization/deserialization
- No game logic

**Structure**:
```csharp
// Required: Inherit BaseData
public abstract class BaseData
{
    public int Id { get; set; }

    // All data must provide validation logic
    public abstract bool Validate();
}
```

**Rules**:
1. **No Logic**: Data storage and representation only
2. **Immutability**: Use read-only properties when possible
3. **Serializable**: Must have `[System.Serializable]` attribute
4. **Naming**: `{Entity}Data` (e.g., `PlayerData`, `ItemData`)

**Example**:
```csharp
[System.Serializable]
public class ItemData : BaseData
{
    public string Name;
    public int BaseAttack;
    public float BaseCritRate;
    public ItemType Type;

    public override bool Validate()
    {
        return !string.IsNullOrEmpty(Name) && BaseAttack >= 0;
    }
}
```

**Location**: `Assets/Data/Base/` (BaseData), `Assets/Data/Game/` (Game-specific)

---

#### 5.2.2 Domain Layer (도메인 계층)

**Purpose**:
- Process and transform raw data
- Apply game formulas (stats, damage, probability)
- Data caching and optimization
- Implement business rules

**Structure**:
```csharp
// Required: Inherit BaseDomain<TData>
public abstract class BaseDomain<TData> where TData : BaseData
{
    public abstract string DomainName { get; }

    // Load → Process → Cache
    public abstract void LoadData();

    // Query by ID
    public abstract TData GetData(int id);

    // Query all
    public abstract IEnumerable<TData> GetAllData();
}
```

**Rules**:
1. **Data-Centric**: Read and process Data only
2. **Stateless**: No game state in Domain
3. **Caching**: Prevent repeated calculations
4. **Naming**: `{Entity}Domain` (e.g., `ItemDomain`, `PlayerStatsDomain`)

**Example**:
```csharp
public class ItemDomain : BaseDomain<ItemData>
{
    public override string DomainName => "Item";

    private Dictionary<int, ItemData> itemCache = new Dictionary<int, ItemData>();

    public override void LoadData()
    {
        // Load from JSON/CSV
        var json = Resources.Load<TextAsset>("Data/Items");
        var itemList = JsonUtility.FromJson<ItemDataList>(json.text);

        foreach (var item in itemList.items)
        {
            // Apply game rules
            item.FinalAttack = CalculateFinalAttack(item);
            itemCache[item.Id] = item;
        }
    }

    private int CalculateFinalAttack(ItemData item)
    {
        return item.BaseAttack + (item.Level * 5);
    }
}
```

**Location**: `Assets/Scripts/Domain/Base/` (BaseDomain), `Assets/Scripts/Domain/{GameName}/` (Game-specific)

---

#### 5.2.3 Core Layer (코어 계층)

**Purpose**:
- Provide game-independent universal modules
- Manage module lifecycle
- Framework foundation systems

**Structure**:
```csharp
// Required: Inherit BaseModule
public abstract class BaseModule : IModule
{
    public abstract string ModuleName { get; }
    public abstract int Priority { get; }

    // Lifecycle methods
    public void Initialize();
    public void Shutdown();
    public void OnUpdate();
}
```

**Default Modules**:

| Module | Responsibility | Priority |
|--------|----------------|----------|
| **DataModule** | Data load/save | 5 |
| **UIModule** | UI canvas management | 10 |
| **SceneModule** | Scene transition | 15 |
| **AudioModule** | BGM/SFX playback | 20 |
| **NetworkModule** | Network communication | 25 |

**Rules**:
1. **Game-Independent**: No specific game logic
2. **Independent**: No dependency on other modules
3. **Optional**: Can be enabled/disabled via config
4. **Naming**: `{Feature}Module` (e.g., `UIModule`, `AudioModule`)

**Location**: `Assets/Framework/Core/Modules/`

---

#### 5.2.4 Interface Layer (인터페이스 계층)

**Purpose**:
- Define game-specific contracts
- Apply Dependency Inversion Principle (DIP)
- Enforce Service implementation

**Structure**:
```csharp
// Required: Inherit IService
public interface IService
{
    string ServiceName { get; }
    void Initialize();
    void Dispose();
}

// Game-specific interface
public interface IInventorySystem : IService
{
    bool AddItem(int itemId, int count);
    bool RemoveItem(int itemId, int count);
    ItemData GetItem(int itemId);
}
```

**Rules**:
1. **Contract Definition**: Exclude implementation details
2. **IService Inheritance**: All interfaces implement IService
3. **Naming**: `I{System}System` (e.g., `IInventorySystem`, `IBattleSystem`)

**Location**: `Assets/Scripts/Interface/`

---

#### 5.2.5 Service Layer (서비스 계층)

**Purpose**:
- Concrete implementation of interfaces
- Game business logic processing
- Combine Core modules + Domain

**Structure**:
```csharp
// Required: Inherit BaseService + Implement Interface
public abstract class BaseService : IService
{
    public abstract string ServiceName { get; }

    protected EventBus EventBus { get; }
    protected ServiceLocator Services { get; }

    public virtual void Initialize();
    public virtual void Dispose();
}
```

**Rules**:
1. **Interface Implementation**: Must define interface first
2. **BaseService Inheritance**: Unified lifecycle
3. **State Management**: Manage game state in Service
4. **Event Publishing**: Publish events on state changes
5. **Naming**: `{System}Service` (e.g., `InventoryService`, `BattleService`)

**Example**:
```csharp
public class InventoryService : BaseService, IInventorySystem
{
    public override string ServiceName => "Inventory";

    private ItemDomain itemDomain;
    private Dictionary<int, int> inventory = new Dictionary<int, int>();

    protected override void InitializeService()
    {
        itemDomain = DataManager.Instance.GetDomain<ItemDomain>();
    }

    public bool AddItem(int itemId, int count)
    {
        var itemData = itemDomain.GetData(itemId);
        if (itemData == null) return false;

        if (!inventory.ContainsKey(itemId))
            inventory[itemId] = 0;

        inventory[itemId] += count;

        EventBus.Publish(new ItemAddedEvent
        {
            ItemId = itemId,
            Count = count
        });

        return true;
    }
}
```

**Location**: `Assets/Scripts/Service/Base/` (BaseService), `Assets/Scripts/Service/{GameName}/` (Game-specific)

---

#### 5.2.6 Gameplay Layer (게임플레이 계층)

**Purpose**:
- Implement actual game logic
- MonoBehaviour-based
- Use Service composition

**Structure**:
```csharp
// Required: Inherit BaseGameplay
public abstract class BaseGameplay : MonoBehaviour
{
    protected ServiceLocator Services { get; }
    protected EventBus EventBus { get; }

    // Unity lifecycle integration
    protected virtual void Awake() { }
    protected virtual void Start() { }
    protected virtual void OnDestroy() { }

    // Framework lifecycle
    protected abstract void RegisterServices();
    protected abstract void SubscribeEvents();
    protected abstract void UnsubscribeEvents();
}
```

**Rules**:
1. **BaseGameplay Inheritance**: Unified lifecycle
2. **Service Usage**: Call services, don't implement logic directly
3. **Event Subscription**: Subscribe to necessary events only
4. **Naming**: `{Entity}Controller` (e.g., `PlayerController`, `EnemyController`)

**Location**: `Assets/Scripts/Gameplay/Base/` (BaseGameplay), `Assets/Scripts/Gameplay/{GameName}/` (Game-specific)

### 5.3 Core Systems

#### 5.3.1 EventBus (이벤트 버스)

**Purpose**:
- Loose coupling between layers
- Asynchronous communication
- Event-driven architecture

**Interface**:
```csharp
public interface IGameEvent { }

public class EventBus : Singleton<EventBus>
{
    // Subscribe to event
    public void Subscribe<T>(Action<T> handler) where T : IGameEvent;

    // Unsubscribe from event
    public void Unsubscribe<T>(Action<T> handler) where T : IGameEvent;

    // Publish event
    public void Publish<T>(T gameEvent) where T : IGameEvent;
}
```

**Usage Rules**:
1. **Event Definition**: Implement IGameEvent
2. **Naming**: `{Action}{Entity}Event` (e.g., `ItemAddedEvent`, `PlayerDamagedEvent`)
3. **Data**: Include only necessary information
4. **Immutability**: Use readonly fields when possible

**Location**: `Assets/Framework/Core/Systems/EventBus.cs`

---

#### 5.3.2 ServiceLocator (서비스 로케이터)

**Purpose**:
- Centralized service management
- Runtime dependency resolution
- Global access provision

**Interface**:
```csharp
public class ServiceLocator : Singleton<ServiceLocator>
{
    // Register service
    public void Register<T>(T service) where T : IService;

    // Get service
    public T Get<T>() where T : IService;

    // Check service existence
    public bool Has<T>() where T : IService;

    // Clear all services
    public void Clear();
}
```

**Usage Rules**:
1. **Initialization**: Register all services at game start
2. **Single Instance**: Each service registered once
3. **Type-Based**: Register/query by interface type

**Location**: `Assets/Framework/Core/Systems/ServiceLocator.cs`

---

#### 5.3.3 DataManager (데이터 관리자)

**Purpose**:
- Centralized Domain management
- Unified data loading
- Domain access provision

**Interface**:
```csharp
public class DataManager : Singleton<DataManager>
{
    // Register Domain
    public void RegisterDomain<TDomain, TData>(TDomain domain)
        where TDomain : BaseDomain<TData>
        where TData : BaseData;

    // Get Domain
    public TDomain GetDomain<TDomain>() where TDomain : class;

    // Load all Domains
    public void LoadAllDomains();
}
```

**Location**: `Assets/Framework/Core/Systems/DataManager.cs`

### 5.4 Lifecycle Management

#### Initialization Flow
```
[Application Start]
       ↓
┌─────────────────┐
│ FrameworkManager│
│    .Awake()     │
└─────────────────┘
       ↓
┌─────────────────┐
│  Core Systems   │
│  - EventBus     │
│  - ServiceLocator│
│  - DataManager  │
└─────────────────┘
       ↓
┌─────────────────┐
│ Modules Init    │
│ (Priority Order)│
└─────────────────┘
       ↓
┌─────────────────┐
│ Domain LoadData │
└─────────────────┘
       ↓
┌─────────────────┐
│Services Register│
└─────────────────┘
       ↓
┌─────────────────┐
│ Scene Load      │
└─────────────────┘
       ↓
┌─────────────────┐
│Gameplay Init    │
└─────────────────┘
       ↓
   [Game Ready]
```

#### Shutdown Flow
```
[Application Quit]
       ↓
┌─────────────────┐
│ Gameplay        │
│  .OnDestroy()   │
└─────────────────┘
       ↓
┌─────────────────┐
│ Services        │
│  .Dispose()     │
└─────────────────┘
       ↓
┌─────────────────┐
│ Modules         │
│  .Shutdown()    │
│  (Reverse Order)│
└─────────────────┘
       ↓
   [Clean Exit]
```

#### Module Priority System
- **DataModule**: Priority 5 (First to initialize)
- **UIModule**: Priority 10
- **SceneModule**: Priority 15
- **AudioModule**: Priority 20
- **NetworkModule**: Priority 25 (Last to initialize)
- **Shutdown**: Reverse order (25 → 20 → 15 → 10 → 5)

### 5.5 Folder Structure Template

```
Assets/
├── Framework/                  # Common (Reusable)
│   ├── Core/
│   │   ├── Base/
│   │   │   ├── IModule.cs
│   │   │   ├── IService.cs
│   │   │   ├── BaseModule.cs
│   │   │   ├── BaseService.cs
│   │   │   ├── BaseDomain.cs
│   │   │   └── BaseGameplay.cs
│   │   ├── Modules/
│   │   │   ├── UIModule.cs
│   │   │   ├── AudioModule.cs
│   │   │   ├── SceneModule.cs
│   │   │   └── NetworkModule.cs
│   │   ├── Systems/
│   │   │   ├── EventBus.cs
│   │   │   ├── ServiceLocator.cs
│   │   │   ├── DataManager.cs
│   │   │   └── FrameworkLogger.cs
│   │   ├── FrameworkManager.cs
│   │   └── FrameworkConfig.cs
│   └── Data/
│       └── Base/
│           └── BaseData.cs
│
├── Data/                       # Game Data
│   ├── Json/
│   │   ├── Items.json
│   │   └── Stages.json
│   └── CSV/
│       └── Monsters.csv
│
└── Scripts/                    # Game-Specific
    ├── {GameName}/
    │   ├── Data/
    │   │   ├── ItemData.cs
    │   │   ├── PlayerData.cs
    │   │   └── StageData.cs
    │   ├── Domain/
    │   │   ├── ItemDomain.cs
    │   │   ├── PlayerStatsDomain.cs
    │   │   └── StageDomain.cs
    │   ├── Interface/
    │   │   ├── IInventorySystem.cs
    │   │   ├── IBattleSystem.cs
    │   │   └── IQuestSystem.cs
    │   ├── Service/
    │   │   ├── InventoryService.cs
    │   │   ├── BattleService.cs
    │   │   └── QuestService.cs
    │   └── Gameplay/
    │       ├── Player/
    │       │   └── PlayerController.cs
    │       ├── Enemy/
    │       │   └── EnemyAI.cs
    │       └── Stage/
    │           └── StageManager.cs
    │
    └── Common/                 # Game Common
        ├── Events/
        │   ├── ItemAddedEvent.cs
        │   ├── PlayerDamagedEvent.cs
        │   └── StageCompletedEvent.cs
        └── Utilities/
            └── Singleton.cs
```

### 5.6 Naming Conventions

| Layer | Suffix | Example |
|-------|--------|---------|
| Data | Data | `ItemData`, `PlayerData` |
| Domain | Domain | `ItemDomain`, `StatsDomain` |
| Interface | System | `IInventorySystem`, `IBattleSystem` |
| Service | Service | `InventoryService`, `BattleService` |
| Gameplay | Controller / Manager | `PlayerController`, `StageManager` |
| Event | Event | `ItemAddedEvent`, `StageCompletedEvent` |
| Module | Module | `UIModule`, `AudioModule` |

### 5.7 System Documentation Requirements

Each core system must have:
- Architecture overview
- API reference
- Usage examples
- Integration guide
- Best practices

Location: `.claude/framework/doc/systems/[category]/`

---

## 6. Quality Standards

### 6.1 Code Quality

#### Documentation Requirements
- **XML Documentation**: All public APIs must have XML documentation comments
- **Code Comments**: Complex algorithms and non-obvious logic must be commented
- **README Files**: Each system must have a README explaining purpose and usage

#### Testing Requirements
- **Unit Tests**: All core logic must have unit tests
- **Integration Tests**: System interactions must be tested
- **Coverage**: Aim for >80% code coverage on critical systems

#### Code Standards
- Follow `.claude/framework/doc/guidelines/coding-conventions.md`
- Pass all linter rules
- No compiler warnings
- Performance-conscious implementation

### 6.2 Documentation Quality

#### Completeness
- All required metadata fields present
- All sections properly documented
- Examples included where appropriate
- Links to related documents

#### Accuracy
- Content matches implementation
- Examples are tested and working
- Version information is current
- No outdated information

#### Consistency
- Follows documentation-rules.md
- Consistent terminology
- Consistent formatting
- Bilingual documents synchronized

### 6.3 Validation Requirements

All documents must pass:
- ✅ `doc_validate.py` - Metadata and link validation
- ✅ `scope_validate.py` - Scope dependency validation
- ✅ Paired document exists and synchronized
- ✅ All links are valid and reachable

---

## 7. Technology Stack

### 7.1 Unity Environment
- **Unity Version**: 6000.2.9f1 (Unity 6)
- **Render Pipeline**: Universal Render Pipeline (URP) 17.2.0
- **Input System**: New Input System 1.14.2
- **Target Platforms**: PC, Console (future: Mobile)

### 7.2 Development Tools
- **IDE**: Visual Studio / Rider
- **Version Control**: Git
- **Documentation**: Markdown
- **Scripting**: C# (Unity), Python (automation)

### 7.3 Framework Dependencies
- Minimize external dependencies
- Use Unity built-in packages when possible
- Document all third-party packages
- Justify dependency additions

---

## 8. Development Workflow

### 8.1 Framework Development Process

1. **Planning**: Define system requirements in SPEC
2. **Design**: Document architecture and API
3. **Implementation**: Write code following conventions
4. **Testing**: Create comprehensive tests
5. **Documentation**: Write system documentation
6. **Review**: Code and documentation review
7. **Integration**: Merge into framework
8. **Validation**: Run all validation scripts

### 8.2 Documentation Workflow

1. **Create**: Write original document (*.md)
2. **Translate**: Create Korean document (*_KOR.md)
3. **Metadata**: Add required frontmatter
4. **Link**: Connect related documents
5. **Validate**: Run validation scripts
6. **Review**: Peer review
7. **Approve**: Mark as approved
8. **Maintain**: Keep synchronized with changes

### 8.3 Session Management

When context usage approaches 85%:
1. Update SPEC.md with current progress
2. Update TODO.md with remaining tasks
3. Synchronize Korean documents
4. Create session restoration guide
5. Execute `/clear`
6. Resume in new session with updated context

---

## 9. Success Criteria

### 9.1 Framework Goals
- ✅ All core systems implemented and documented
- ✅ Comprehensive test coverage (>80%)
- ✅ Complete API documentation
- ✅ At least one game successfully built using framework

### 9.2 Documentation Goals
- ✅ All documents bilingual (English + Korean)
- ✅ All documents pass validation
- ✅ Zero broken links
- ✅ All scope dependencies respected

### 9.3 Quality Goals
- ✅ No compiler warnings
- ✅ All tests passing
- ✅ Performance targets met
- ✅ Code review standards met

---

## 10. Future Considerations

### 10.1 Planned Features
- Multiplayer framework foundation
- Advanced AI utilities
- Procedural generation tools
- Mobile platform support

### 10.2 Documentation Evolution
- API reference auto-generation
- Interactive documentation
- Video tutorials
- Community contributions

### 10.3 Tooling Improvements
- Automated translation integration
- CI/CD pipeline for validation
- Documentation website
- Code generation tools

---

## Appendix A: Glossary

**Framework Scope**: The reusable, game-agnostic foundation scope
**Game Scope**: Game-specific implementation that uses the framework
**Original Document**: English .md file
**Korean Document**: Korean _KOR.md file
**Bilingual Documentation**: Dual language documentation system
**Scope Validation**: Automated checking of dependency rules
**Paired Document**: The corresponding translation of a document

---

## Appendix B: Quick Reference

### Essential Commands
```bash
# Validation
python .claude/scripts/scope_validate.py
python .claude/scripts/doc_validate.py

# Documentation
python .claude/scripts/doc_sync.py --check
python .claude/scripts/version_bump.py [file] [major|minor|patch]
```

### Folder Locations
- Framework Docs: `.claude/framework/doc/`
- Framework SPEC/TODO: `.claude/framework/project/`
- Game Template: `.claude/games/_template/`
- Scripts: `.claude/scripts/`

### Important Files
- Framework Spec: `.claude/framework/project/SPEC.md`
- Framework TODO: `.claude/framework/project/TODO.md`
- Claude Config: `CLAUDE.md`
- Coding Conventions: `.claude/framework/doc/guidelines/coding-conventions.md`
- Documentation Rules: `.claude/framework/doc/guidelines/documentation-rules.md`

---

**Document Status**: Draft
**Next Review Date**: TBD
**Maintained By**: HaroFramework Team
