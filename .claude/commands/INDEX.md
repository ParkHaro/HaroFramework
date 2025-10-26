---
title: HaroFramework Commands Index
version: 1.0.0
scope: framework
created: 2025-10-26
modified: 2025-10-26
category: Commands
tags: [commands, index, slash-commands, unity, reference]
paired_document: INDEX_KOR.md
parent_documents:
  - ../MASTER_INDEX.md
child_documents: []
references:
  - ../skills/INDEX.md
  - ../framework/doc/workflow/development-workflow.md
status: active
---



<!-- Navigation -->
**🏠 [HaroFramework Project](../MASTER_INDEX.md)** | **📂 [HaroFramework Commands Index](INDEX.md)** | **⬆️ [HaroFramework Project](../MASTER_INDEX.md)**

---
# HaroFramework Commands Index

Manual slash commands for Unity development workflows. Commands require explicit invocation by typing `/command-name`.

**Total Commands**: 9

---

## 📋 Quick Reference

| Command | Description | Arguments | Use Case |
|---------|-------------|-----------|----------|
| `/component` | Create MonoBehaviour | `<Name> [namespace]` | Gameplay scripts, controllers |
| `/scriptable` | Create ScriptableObject | `<Name> [namespace]` | Data assets, game config |
| `/singleton` | Create Singleton pattern | `<Name>` | Manager classes |
| `/test` | Run Unity tests | `[EditMode\|PlayMode\|All]` | Test execution, validation |
| `/build` | Build Unity project | `[platform]` | Deployment, builds |
| `/asmdef` | Create Assembly Definition | `<Name> [Runtime\|Editor\|Tests]` | Code organization |
| `/scene-analyze` | Analyze scene structure | `<scene-name>` | Scene debugging, optimization |
| `/package-add` | Add Unity package | `<package-name>` | Package management |
| `/input-action` | Create Input Action map | `<ActionMapName>` | Input System setup |

---

## 🎯 Commands vs Skills

### When to Use Commands (Manual)
✅ **Explicit control needed**
- You know exactly what you want
- Need specific configuration
- Prefer manual invocation

**Example**: `/component PlayerController HaroFramework.Player`

### When to Use Skills (Automatic)
✅ **Natural language workflow**
- Describe what you want to build
- Claude chooses appropriate tool
- Automatic activation based on context

**Example**: "Create a health system for the player"
→ Claude automatically uses `unity-component` skill

**See Also**: [Skills Index](../skills/INDEX.md) for auto-activated capabilities

---

## 📚 Command Categories

### Code Generation Commands

#### `/component <ComponentName> [namespace]`
**Purpose**: Create well-structured MonoBehaviour component

**Generated Structure**:
- XML documentation
- Organized regions (Inspector Fields, Unity Lifecycle, Methods)
- Proper namespace
- Unity 6 best practices

**Default Namespace**: `HaroFramework`

**Example**:
```bash
/component PlayerController HaroFramework.Player
```

**Output**:
```csharp
namespace HaroFramework.Player
{
    /// <summary>
    /// [Add description]
    /// </summary>
    public class PlayerController : MonoBehaviour
    {
        #region Serialized Fields
        // Inspector-visible fields
        #endregion

        #region Unity Lifecycle
        private void Awake() { }
        private void Start() { }
        #endregion

        #region Public Methods
        // Public API
        #endregion

        #region Private Methods
        // Internal implementation
        #endregion
    }
}
```

**Related**:
- [Coding Conventions](../framework/doc/guidelines/coding-conventions.md)
- [6-Layer Architecture](../framework/project/spec/02-architecture/6-layer-system.md)

---

#### `/scriptable <ClassName> [namespace]`
**Purpose**: Create ScriptableObject for data-driven design

**Generated Structure**:
- `[CreateAssetMenu]` attribute
- OnValidate() for runtime validation
- Proper namespace organization

**Default Namespace**: `HaroFramework.Data`

**Example**:
```bash
/scriptable ItemData HaroFramework.Data
```

**Use Cases**:
- Game configuration data
- Event systems (Event ScriptableObjects)
- Item/Character definitions
- Level data
- Designer-friendly data assets

**Related**:
- [Data Layer](../framework/project/spec/02-architecture/6-layer-system.md)

---

#### `/singleton <ClassName>`
**Purpose**: Create thread-safe singleton MonoBehaviour pattern

**Features**:
- Thread-safe lazy initialization
- DontDestroyOnLoad support
- Duplicate instance prevention
- Unity 6 compatible (`FindFirstObjectByType`)
- Application quit handling

**Default Namespace**: `HaroFramework.Core`

**Example**:
```bash
/singleton GameManager
```

**Best Practices**:
- Use sparingly (singletons can create coupling)
- Prefer dependency injection for testability
- Good for: GameManager, AudioManager, InputManager
- Avoid for: Data classes, utility classes

**Related**:
- [Singleton Pattern Spec](../framework/project/spec/05-core-systems/foundation/singleton.md)

---

#### `/asmdef <AssemblyName> [Runtime|Editor|Tests]`
**Purpose**: Create Assembly Definition for code organization

**Benefits**:
- Faster compilation (incremental compilation)
- Clear dependency boundaries
- Required for Unity packages
- Better code organization

**Assembly Types**:
- **Runtime**: Gameplay code (default)
- **Editor**: Editor-only scripts
- **Tests**: Test assemblies

**Example**:
```bash
/asmdef HaroFramework.Core Runtime
/asmdef HaroFramework.Editor Editor
/asmdef HaroFramework.Tests Tests
```

**Recommended Structure**:
```
Assets/Scripts/
├── Runtime/
│   └── HaroFramework.Runtime.asmdef
├── Editor/
│   └── HaroFramework.Editor.asmdef
└── Tests/
    ├── EditMode/
    │   └── HaroFramework.EditMode.Tests.asmdef
    └── PlayMode/
        └── HaroFramework.PlayMode.Tests.asmdef
```

**Related**:
- [Project Structure](../framework/project/spec/02-architecture/folder-structure.md)

---

#### `/input-action <ActionMapName>`
**Purpose**: Create Input System action map asset

**Note**: This project uses Unity Input System (1.14.2), **not** legacy Input Manager

**Generated**:
- .inputactions asset structure
- Action map with common actions
- Control schemes (Keyboard/Mouse, Gamepad, Touch)
- C# wrapper class generation guidance

**Common Actions**:
- Movement (Vector2)
- Look (Vector2)
- Jump (Button)
- Interact (Button)
- Pause (Button)

**Example**:
```bash
/input-action PlayerControls
```

**Related**:
- [Input System Package](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.14/manual/index.html)

---

### Testing & Quality Commands

#### `/test [EditMode|PlayMode|All]`
**Purpose**: Execute Unity Test Framework tests

**Test Types**:
- **EditMode**: Tests run in editor without play mode (faster)
- **PlayMode**: Tests require play mode execution (slower, more realistic)
- **All**: Run both test types (default)

**Example**:
```bash
/test EditMode        # Quick tests
/test PlayMode        # Integration tests
/test All             # Full test suite
```

**Tasks Performed**:
1. Find all test assemblies (.asmdef with test references)
2. Locate test scripts in Tests/ directories
3. Execute tests and collect results
4. Report coverage and failures
5. Suggest fixes for common issues

**Related**:
- [Testing Guide](../framework/project/spec/06-quality/code-quality.md)
- [unity-testing Skill](../skills/unity-testing/SKILL.md)

---

### Project Management Commands

#### `/build [platform]`
**Purpose**: Build Unity project for target platform

**Supported Platforms**:
- Windows (default)
- Mac
- Linux
- Android
- iOS
- WebGL

**Example**:
```bash
/build                # Analyze current settings
/build Windows        # Build for Windows
/build Android        # Build for Android
```

**Tasks Performed**:
1. Check EditorBuildSettings for scenes
2. Validate assets and dependencies
3. Check for compilation errors
4. Provide Unity CLI build arguments
5. Suggest optimization opportunities

**Related**:
- [Build Configuration](../framework/project/spec/07-tech-stack/unity-environment.md)

---

#### `/scene-analyze <scene-name>`
**Purpose**: Analyze Unity scene structure and optimization

**Example**:
```bash
/scene-analyze MainMenu
/scene-analyze GameLevel01
```

**Analysis Includes**:
- GameObject hierarchy
- Component types and counts
- Script dependencies
- Missing references
- Broken prefabs
- Performance issues
- Optimization suggestions

**Report Metrics**:
- Total GameObjects (Active/Inactive)
- Component usage statistics
- Prefab instances
- Missing references
- Performance bottlenecks

**Related**:
- Scene organization best practices

---

#### `/package-add <package-name>`
**Purpose**: Add Unity package via Package Manager

**Package Sources**:
- Unity Registry (official packages)
- Git repositories
- Local packages

**Example**:
```bash
/package-add Cinemachine
/package-add com.unity.cinemachine
/package-add https://github.com/user/repo.git#1.0.0
```

**Common Packages**:
- `com.unity.cinemachine` - Camera system
- `com.unity.probuilder` - Level design
- `com.unity.textmeshpro` - Text rendering
- `com.unity.addressables` - Asset management
- `com.unity.2d.*` - 2D game packages

**Tasks Performed**:
1. Read current Packages/manifest.json
2. Identify package source
3. Determine compatible version
4. Check dependency conflicts
5. Update manifest.json

**Related**:
- [Dependencies](../framework/project/spec/07-tech-stack/dependencies.md)

---

## 🚀 Usage Patterns

### Typical Workflow Examples

#### 1. Creating a New Gameplay Feature
```bash
# 1. Create component
/component HealthSystem HaroFramework.Gameplay

# 2. Create data asset
/scriptable HealthConfig HaroFramework.Data

# 3. Create tests
# (Use unity-testing skill via natural language)
"Create tests for HealthSystem"

# 4. Run tests
/test EditMode
```

#### 2. Setting Up Project Structure
```bash
# 1. Create assembly definitions
/asmdef HaroFramework.Core Runtime
/asmdef HaroFramework.Editor Editor
/asmdef HaroFramework.Tests Tests

# 2. Add required packages
/package-add Cinemachine
/package-add TextMeshPro

# 3. Create input system
/input-action PlayerControls
```

#### 3. Quality Assurance Workflow
```bash
# 1. Analyze scene
/scene-analyze GameLevel01

# 2. Run tests
/test All

# 3. Build for platform
/build Windows
```

---

## 💡 Tips & Best Practices

### Command Usage
- **Tab completion**: Type `/` and press tab to see available commands
- **Arguments**: Use quotes for multi-word arguments: `/component "Player Controller"`
- **Defaults**: Most commands have sensible defaults if arguments are omitted

### Choosing Between Commands and Skills
**Use Commands when**:
- You need exact control over parameters
- You're repeating a specific pattern
- You want explicit configuration

**Use Skills when**:
- Describing a feature to build
- Letting Claude choose best approach
- Working with natural language

### Integration with Framework
All commands:
- Follow HaroFramework conventions
- Respect 2-scope architecture (Framework vs Game)
- Generate Unity 6 compatible code
- Include XML documentation
- Use proper namespace organization

---

## 🔗 Related Documentation

### Skills (Auto-Activated)
- [Skills Index](../skills/INDEX.md) - Automatic capabilities
- [Skills vs Commands](../skills/README.md) - When to use what

### Development Guides
- [Development Workflow](../framework/doc/workflow/development-workflow.md)
- [Coding Conventions](../framework/doc/guidelines/coding-conventions.md)
- [Documentation Rules](../framework/doc/guidelines/documentation-rules.md)

### Architecture
- [6-Layer System](../framework/project/spec/02-architecture/6-layer-system.md)
- [Scope System](../framework/doc/architecture/scope-system.md)
- [Project Overview](../framework/doc/architecture/project-overview.md)

### Quick Starts
- [Quick Start Guide](../framework/project/QUICK_START.md)
- [Reading Guide](../framework/project/READING_GUIDE.md)

---

## 📝 Adding Custom Commands

To create your own project-specific commands:

1. **Create command file**: `.claude/commands/your-command.md`

2. **Add metadata**:
```markdown
---
description: Brief description of what this command does
argument-hint: <required> [optional]
---
```

3. **Document behavior**:
- What the command does
- Arguments and defaults
- Example usage
- Generated output

4. **Test command**:
```bash
/your-command arg1 arg2
```

**Example Custom Command**:
```markdown
---
description: Generate a combat system
argument-hint: <SystemName>
---

Create a combat system with damage calculation and hit detection.

System name: $ARGUMENTS

[Implementation details...]
```

---

**Document Status**: Active
**Maintained By**: HaroFramework Team
**Last Updated**: 2025-10-26

**See Also**:
- [Skills Index](../skills/INDEX.md) - Auto-activated capabilities
- [Master Index](../MASTER_INDEX.md) - All project documentation
