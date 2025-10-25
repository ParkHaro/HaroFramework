---
title: HaroFramework Specification
version: 1.0.0
layer: framework
created: 2025-10-25
modified: 2025-10-25
category: Project Management
tags: [specification, architecture, documentation]
paired_document: SPEC_KOR.md
parent_documents: []
child_documents: []
references: []
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

### 2.1 2-Layer System

The project uses a strict 2-layer architecture to separate framework concerns from game-specific implementation:

#### Framework Layer (Independent)
- **Purpose**: Provides reusable game systems and utilities
- **Independence**: Must not reference or depend on any game-specific code
- **Location**: `.claude/framework/`
- **Scope**: Core systems, tools, utilities, common patterns

#### Game Layer (Framework-Dependent)
- **Purpose**: Implements specific game logic and content
- **Dependency**: Can reference and use Framework layer
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
├── framework/                        # 🔵 Framework Layer (Independent)
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
│   │   │   ├── layer-system.md
│   │   │   └── layer-system_KOR.md
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
├── games/                            # 🟢 Game Layer (Framework-Dependent)
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
│   ├── layer_validate.py            # Layer dependency validation
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
layer: "framework|game"             # Layer classification
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

#### Layer Field Values
- `framework`: Framework layer documents
- `game`: Game layer documents

**Purpose**: The `layer` field enables automated validation to prevent forbidden cross-layer references.

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
- Verify layer boundaries are respected

#### Layer-Aware Linking
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

#### layer_validate.py - Layer Dependency Validation
**Purpose**: Enforce layer dependency rules

**Validation**:
- Extract `layer` field from document metadata
- Parse all links and references
- Verify Framework documents don't reference Game documents
- Report violations with file and line information

**Algorithm**:
```python
def validate_layer_dependency(doc_path):
    layer = get_document_layer(doc_path)
    references = extract_all_references(doc_path)

    for ref in references:
        ref_layer = get_document_layer(ref)

        if layer == "framework" and ref_layer == "game":
            raise DependencyViolationError(
                f"FORBIDDEN: Framework document '{doc_path}' "
                f"cannot reference Game document '{ref}'"
            )

    return True
```

**Usage**:
```bash
python .claude/scripts/layer_validate.py              # Validate all
python .claude/scripts/layer_validate.py [document]   # Validate one
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

## 4. Layer Dependency Rules

### 4.1 Absolute Rules

#### ❌ FORBIDDEN: Framework → Game
Framework layer MUST NOT:
- Import or reference game-specific code
- Link to game documentation
- Contain game-specific logic or content
- Know about the existence of game projects

**Why**: Framework must remain reusable across all game projects.

#### ✅ ALLOWED: Game → Framework
Game layer CAN:
- Import and use framework systems
- Reference framework documentation
- Extend framework classes
- Build upon framework utilities

**Why**: Games are meant to leverage the framework.

### 4.2 Validation Methods

#### Metadata-Based Validation
Every document declares its layer:
```yaml
layer: framework  # or "game"
```

Validation script checks:
1. Document's declared layer
2. All referenced documents' layers
3. Enforce: `framework` cannot reference `game`

#### Continuous Validation
- Run `layer_validate.py` before commits
- Integrate into CI/CD pipeline (future)
- Automated checks during document operations

#### Manual Review
- Code review checklist includes layer verification
- Architecture reviews examine layer boundaries
- Documentation reviews verify proper categorization

---

## 5. Core Framework Systems

### 5.1 System Categories

The framework is organized into the following core system categories:

#### Core
- Framework initialization
- Service locator
- Dependency injection
- Event system
- Object pooling

#### Player
- Player controller
- Input handling
- Player state management
- Camera control

#### AI
- Behavior trees
- Pathfinding
- Decision making
- AI state machines

#### UI
- Menu system
- HUD elements
- Dialog system
- UI utilities

#### Audio
- Audio manager
- Sound effects
- Music system
- Audio mixing

#### Gameplay
- Game rules
- Game state management
- Progression system
- Achievement system

#### Systems
- Save/load system
- Settings management
- Localization
- Analytics integration

#### Data
- ScriptableObject definitions
- Data containers
- Configuration assets

#### Editor
- Custom inspectors
- Editor windows
- Build tools
- Development utilities

#### Tests
- Unit tests
- Integration tests
- Play mode tests
- Test utilities

### 5.2 System Documentation

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
- ✅ `layer_validate.py` - Layer dependency validation
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
- ✅ All layer dependencies respected

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

**Framework Layer**: The reusable, game-agnostic foundation layer
**Game Layer**: Game-specific implementation that uses the framework
**Original Document**: English .md file
**Korean Document**: Korean _KOR.md file
**Bilingual Documentation**: Dual language documentation system
**Layer Validation**: Automated checking of dependency rules
**Paired Document**: The corresponding translation of a document

---

## Appendix B: Quick Reference

### Essential Commands
```bash
# Validation
python .claude/scripts/layer_validate.py
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
