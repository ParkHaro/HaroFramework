---
title: HaroFramework Skills Index
version: 1.0.0
scope: framework
created: 2025-10-26
modified: 2025-10-26
category: Skills
tags: [skills, index, auto-activation, unity, ai-driven]
paired_document: INDEX_KOR.md
parent_documents:
  - ../MASTER_INDEX.md
child_documents: []
references:
  - ../commands/INDEX.md
  - ../framework/doc/workflow/skills-guide.md
status: active
---



<!-- Navigation -->
**🏠 [HaroFramework Project](../MASTER_INDEX.md)** | **📂 [HaroFramework Skills Index](INDEX.md)** | **⬆️ [HaroFramework Project](../MASTER_INDEX.md)**

---
# HaroFramework Skills Index

Model-invoked capabilities that Claude automatically activates based on context. Skills enable natural language workflows without explicit command invocation.

**Total Skills**: 5

---

## 📋 Quick Reference

| Skill | Purpose | Auto-Activates When | Output |
|-------|---------|---------------------|--------|
| `unity-component` | Create MonoBehaviour | Gameplay scripts, controllers, managers | Production-ready component |
| `unity-scriptable` | Create ScriptableObject | Data assets, game config, events | Designer-friendly data |
| `unity-editor` | Create Editor extensions | Custom inspectors, property drawers, tools | Enhanced editor workflow |
| `unity-testing` | Create UTF tests | Unit tests, integration tests, TDD | Complete test coverage |
| `unity-shader` | Create URP shaders | Visual effects, materials, rendering | URP-compatible shaders |

---

## 🎯 Skills vs Commands

### Skills (Model-Invoked) ✨
**Automatic activation based on natural language**

**How it works**:
1. You describe what you want in natural language
2. Claude detects the context and intent
3. Appropriate skill automatically activates
4. Result is generated following best practices

**Example**:
```
User: "I need a health system for my player"
→ Claude: *unity-component skill activates*
→ Creates: HealthSystem.cs with proper structure
```

**Benefits**:
- Natural workflow
- No syntax to remember
- Context-aware
- Best practices built-in

---

### Commands (User-Invoked) ⌨️
**Manual invocation with explicit parameters**

**How it works**:
1. Type `/command-name` with specific arguments
2. Command executes with given parameters
3. Result is generated exactly as specified

**Example**:
```
User: "/component HealthSystem HaroFramework.Player"
→ Creates: HealthSystem.cs in specified namespace
```

**Benefits**:
- Explicit control
- Predictable output
- Precise configuration

**See Also**: [Commands Index](../commands/INDEX.md)

---

## 📚 Skill Catalog

### 🎮 unity-component
**Purpose**: Create well-structured Unity MonoBehaviour components

**Auto-Activation Triggers**:
- "Create a player controller"
- "I need a combat system"
- "Build a movement script"
- "Make a manager for..."
- Any gameplay component request

**Generated Structure**:
```csharp
using UnityEngine;

namespace HaroFramework.{Category}
{
    /// <summary>
    /// XML documentation auto-generated
    /// </summary>
    public class ComponentName : MonoBehaviour
    {
        #region Inspector Fields
        [SerializeField] private float _speed = 5f;
        #endregion

        #region Unity Lifecycle
        private void Awake()
        {
            // Component caching
        }

        private void Start()
        {
            // Initialization
        }

        private void Update()
        {
            // Frame updates
        }
        #endregion

        #region Public Methods
        // Public API
        #endregion

        #region Private Methods
        // Internal logic
        #endregion
    }
}
```

**Features**:
- Proper namespace organization
- Region-based structure
- XML documentation
- Unity 6 lifecycle methods
- SerializeField best practices
- Component caching patterns

**Best Practices Applied**:
- `[SerializeField]` for private fields
- `[RequireComponent]` where needed
- Component references cached in Awake()
- Public API clearly separated
- Unity 6 API usage (FindFirstObjectByType)

**Related Documents**:
- [Coding Conventions](../framework/doc/guidelines/coding-conventions.md)
- [6-Layer Architecture](../framework/project/spec/02-architecture/6-layer-system.md)

---

### 📦 unity-scriptable
**Purpose**: Create Unity ScriptableObjects for data-driven design

**Auto-Activation Triggers**:
- "Create game settings data"
- "I need an event system"
- "Make an item definition"
- "Build character stats data"
- Any data asset request

**Generated Structure**:
```csharp
using UnityEngine;

namespace HaroFramework.Data
{
    /// <summary>
    /// ScriptableObject for [purpose]
    /// </summary>
    [CreateAssetMenu(fileName = "NewAssetName", menuName = "HaroFramework/Category/AssetName")]
    public class AssetName : ScriptableObject
    {
        #region Serialized Fields
        [Header("Configuration")]
        [SerializeField] private string _assetName;
        [SerializeField] private int _value;
        #endregion

        #region Properties
        public string AssetName => _assetName;
        public int Value => _value;
        #endregion

        #region Unity Callbacks
        private void OnValidate()
        {
            // Runtime validation
            _value = Mathf.Max(0, _value);
        }
        #endregion

        #region Public Methods
        // Data access API
        #endregion
    }
}
```

**Features**:
- `[CreateAssetMenu]` for easy creation
- OnValidate() for data validation
- Property-based access
- Designer-friendly structure
- Proper namespace organization

**Common Use Cases**:
- **Game Configuration**: Settings, difficulty levels
- **Event Systems**: ScriptableObject events for decoupling
- **Item Definitions**: Inventory items, weapons, abilities
- **Character Data**: Stats, attributes, progression
- **Level Data**: Wave definitions, spawn points
- **Audio Events**: Sound effect triggers

**Design Patterns**:
- Event-driven architecture with ScriptableObjects
- Data-driven game design
- Designer-friendly data editing
- Shared runtime data

**Related Documents**:
- [Data Layer](../framework/project/spec/02-architecture/6-layer-system.md)
- [ScriptableObject Patterns](https://docs.unity3d.com/Manual/class-ScriptableObject.html)

---

### 🛠️ unity-editor
**Purpose**: Create Unity Editor extensions and custom tools

**Auto-Activation Triggers**:
- "Make a custom inspector for..."
- "Create a property drawer"
- "Build an editor window"
- "Add a menu item"
- Any editor extension request

**Generated Categories**:

**1. Custom Inspectors**:
```csharp
using UnityEditor;
using UnityEngine;

namespace HaroFramework.Editor
{
    [CustomEditor(typeof(TargetScript))]
    public class TargetScriptEditor : Editor
    {
        public override void OnInspectorGUI()
        {
            serializedObject.Update();

            // Custom inspector UI
            EditorGUILayout.PropertyField(serializedObject.FindProperty("_fieldName"));

            // Custom buttons
            if (GUILayout.Button("Action"))
            {
                (target as TargetScript)?.PerformAction();
            }

            serializedObject.ApplyModifiedProperties();
        }
    }
}
```

**2. Property Drawers**:
```csharp
[CustomPropertyDrawer(typeof(CustomAttribute))]
public class CustomDrawer : PropertyDrawer
{
    public override void OnGUI(Rect position, SerializedProperty property, GUIContent label)
    {
        // Custom property field rendering
    }
}
```

**3. Editor Windows**:
```csharp
public class CustomEditorWindow : EditorWindow
{
    [MenuItem("HaroFramework/Custom Tool")]
    public static void ShowWindow()
    {
        GetWindow<CustomEditorWindow>("Custom Tool");
    }

    private void OnGUI()
    {
        // Window content
    }
}
```

**4. Menu Items**:
```csharp
public class CustomMenuItems
{
    [MenuItem("HaroFramework/Action %g")] // Ctrl+G shortcut
    private static void ExecuteAction()
    {
        // Menu action
    }
}
```

**Features**:
- Editor-only scripts (automatically placed in Editor folder)
- Keyboard shortcuts support
- Undo/Redo integration
- SerializedObject/SerializedProperty patterns
- EditorGUI/EditorGUILayout usage

**Related Documents**:
- [Editor Extension Guide](https://docs.unity3d.com/Manual/ExtendingTheEditor.html)

---

### ✅ unity-testing
**Purpose**: Create Unity Test Framework tests with comprehensive coverage

**Auto-Activation Triggers**:
- "Write tests for..."
- "Create unit tests"
- "I need integration tests"
- "Test the health system"
- Any testing request

**Generated Structure**:

**EditMode Tests** (Faster, no play mode):
```csharp
using NUnit.Framework;
using UnityEngine;

namespace HaroFramework.Tests
{
    public class ComponentNameTests
    {
        [Test]
        public void Method_Condition_ExpectedBehavior()
        {
            // Arrange
            var component = new GameObject().AddComponent<ComponentName>();
            var expectedValue = 10;

            // Act
            component.SetValue(expectedValue);

            // Assert
            Assert.AreEqual(expectedValue, component.GetValue());
        }

        [Test]
        public void Method_InvalidInput_ThrowsException()
        {
            // Arrange
            var component = new GameObject().AddComponent<ComponentName>();

            // Act & Assert
            Assert.Throws<ArgumentException>(() => component.SetValue(-1));
        }
    }
}
```

**PlayMode Tests** (Slower, realistic):
```csharp
using System.Collections;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.TestTools;

namespace HaroFramework.Tests
{
    public class ComponentNamePlayModeTests
    {
        [UnityTest]
        public IEnumerator Component_AfterFrames_BehavesCorrectly()
        {
            // Arrange
            var go = new GameObject();
            var component = go.AddComponent<ComponentName>();

            // Act
            component.Initialize();
            yield return null; // Wait one frame

            // Assert
            Assert.IsTrue(component.IsInitialized);

            // Cleanup
            Object.Destroy(go);
        }
    }
}
```

**Features**:
- AAA pattern (Arrange, Act, Assert)
- Descriptive test names
- Setup/TearDown methods
- Test assembly organization
- Both EditMode and PlayMode tests
- UnityTest for coroutines

**Test Assembly Configuration**:
```json
{
    "name": "HaroFramework.Tests",
    "references": [
        "HaroFramework.Runtime",
        "UnityEngine.TestRunner",
        "UnityEditor.TestRunner"
    ],
    "optionalUnityReferences": [
        "TestAssemblies"
    ],
    "includePlatforms": [],
    "excludePlatforms": []
}
```

**Best Practices**:
- Test method naming: `Method_Condition_ExpectedBehavior`
- One assertion per test (when possible)
- Clear setup and cleanup
- Test data builders for complex objects
- Parameterized tests with `[TestCase]`

**Related Documents**:
- [Testing Guide](../framework/project/spec/06-quality/code-quality.md)
- [Unity Test Framework](https://docs.unity3d.com/Packages/com.unity.test-framework@latest)

---

### 🎨 unity-shader
**Purpose**: Create Unity shaders for Universal Render Pipeline (URP)

**Auto-Activation Triggers**:
- "Create a dissolve shader"
- "I need a custom material"
- "Make a hologram effect"
- "Build a toon shader"
- Any shader/visual effect request

**Shader Approaches**:

**1. Shader Graph (Recommended for most cases)**:
- Visual node-based editing
- Artist-friendly
- URP optimized
- Easy iteration

**2. HLSL/ShaderLab (For advanced cases)**:
- Full control
- Performance optimization
- Complex effects

**Generated Shader Graph Structure**:
```
Properties:
- Base Color (Color)
- Base Map (Texture2D)
- Metallic (Float)
- Smoothness (Float)
- Normal Map (Texture2D)
- Emission (Color)

Nodes:
- Sample Texture 2D (Base Map)
- Multiply (Color Tint)
- Sample Texture 2D (Normal Map)
- PBR Master (URP output)

Output:
- URP/Lit or URP/Unlit target
```

**HLSL Shader Template**:
```hlsl
Shader "HaroFramework/CustomShader"
{
    Properties
    {
        _BaseMap("Base Map", 2D) = "white" {}
        _BaseColor("Base Color", Color) = (1,1,1,1)
    }

    SubShader
    {
        Tags
        {
            "RenderType" = "Opaque"
            "RenderPipeline" = "UniversalPipeline"
        }

        Pass
        {
            Name "ForwardLit"
            Tags { "LightMode" = "UniversalForward" }

            HLSLPROGRAM
            #pragma vertex vert
            #pragma fragment frag

            #include "Packages/com.unity.render-pipelines.universal/ShaderLibrary/Core.hlsl"

            struct Attributes
            {
                float4 positionOS : POSITION;
                float2 uv : TEXCOORD0;
            };

            struct Varyings
            {
                float4 positionHCS : SV_POSITION;
                float2 uv : TEXCOORD0;
            };

            TEXTURE2D(_BaseMap);
            SAMPLER(sampler_BaseMap);
            float4 _BaseColor;

            Varyings vert(Attributes IN)
            {
                Varyings OUT;
                OUT.positionHCS = TransformObjectToHClip(IN.positionOS.xyz);
                OUT.uv = IN.uv;
                return OUT;
            }

            half4 frag(Varyings IN) : SV_Target
            {
                half4 baseMap = SAMPLE_TEXTURE2D(_BaseMap, sampler_BaseMap, IN.uv);
                return baseMap * _BaseColor;
            }
            ENDHLSL
        }
    }
}
```

**URP-Specific Features**:
- SRP Batcher compatibility
- Proper render pipeline tags
- URP shader library includes
- Forward rendering path
- Multi-pass support

**Common Shader Types**:
- **PBR Materials**: Metallic, specular workflows
- **Toon/Cel Shading**: Stylized rendering
- **Dissolve Effects**: Object dissol

ve/materialize
- **Outline Shaders**: Character outlines
- **Water/Liquids**: Animated surfaces
- **Particle Effects**: Custom particle shaders

**Related Documents**:
- [URP Shader Documentation](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest)
- [Shader Graph Manual](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest)

---

## 🚀 Usage Patterns

### Natural Language Workflow

**Example 1: Component Creation**
```
User: "Create a player movement system with WASD controls"

Claude: *unity-component skill activates*
→ Creates: PlayerMovement.cs
→ Includes: Input handling, movement logic, regions
→ Follows: HaroFramework conventions
```

**Example 2: Data Assets**
```
User: "I need weapon data with damage, range, and fire rate"

Claude: *unity-scriptable skill activates*
→ Creates: WeaponData.cs
→ Includes: ScriptableObject setup, validation
→ Menu: HaroFramework/Weapons/WeaponData
```

**Example 3: Testing**
```
User: "Write tests for the HealthSystem component"

Claude: *unity-testing skill activates*
→ Creates: HealthSystemTests.cs
→ Includes: AAA pattern tests, edge cases
→ Coverage: Public API, edge cases, integration
```

### Combined Workflows

**Full Feature Implementation**:
```
1. "Create an inventory system"
   → unity-component: InventorySystem.cs

2. "Make inventory item data"
   → unity-scriptable: InventoryItemData.cs

3. "Create a custom inspector for inventory"
   → unity-editor: InventorySystemEditor.cs

4. "Write tests for the inventory"
   → unity-testing: InventorySystemTests.cs

5. "Create an item highlight shader"
   → unity-shader: ItemHighlight shader graph
```

---

## 💡 Tips & Best Practices

### Skill Activation
- **Be specific**: "Create a health system" > "Make a script"
- **Provide context**: Mention Unity-specific terms (MonoBehaviour, ScriptableObject)
- **Natural language**: Describe what you want, not how to do it

### When Skills Don't Activate
If Claude doesn't use the expected skill:
1. Be more specific about Unity context
2. Mention the component type explicitly
3. Use Unity terminology
4. Provide more detail about the feature

### Combining Skills and Commands
**Best approach**:
- Use **Skills** for feature descriptions
- Use **Commands** for precise, repeated patterns

**Example**:
```
Skill: "Create a combat system"
Command: /component DamageReceiver HaroFramework.Combat
Skill: "Test the combat system"
```

---

## 🔗 Related Documentation

### Commands (Manual)
- [Commands Index](../commands/INDEX.md) - Manual slash commands
- [Commands Guide](../framework/doc/workflow/commands-guide.md)

### Development Guides
- [Skills Guide](../framework/doc/workflow/skills-guide.md) - Detailed skill documentation
- [Development Workflow](../framework/doc/workflow/development-workflow.md)
- [Coding Conventions](../framework/doc/guidelines/coding-conventions.md)

### Architecture
- [6-Layer System](../framework/project/spec/02-architecture/6-layer-system.md)
- [Project Overview](../framework/doc/architecture/project-overview.md)

### Quick Starts
- [Quick Start Guide](../framework/project/QUICK_START.md)
- [Reading Guide](../framework/project/READING_GUIDE.md)

---

## 📚 Official Resources

- [Claude Code Skills Documentation](https://docs.claude.com/en/docs/claude-code/skills)
- [Unity 6 Documentation](https://docs.unity3d.com/)
- [URP Documentation](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest)
- [Unity Test Framework](https://docs.unity3d.com/Packages/com.unity.test-framework@latest)

---

**Document Status**: Active
**Maintained By**: HaroFramework Team
**Last Updated**: 2025-10-26
**Project Context**: Unity 6, URP 17.2.0, Input System 1.14.2

**Note**: Skills activate automatically - no syntax to remember, just describe what you want to build!
