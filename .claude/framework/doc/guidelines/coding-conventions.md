---
title: "Coding Conventions"
version: "1.0.0"
scope: "framework"
created: "2025-10-25"
modified: "2025-10-25"
category: "Guidelines"
tags: [coding, conventions, standards, csharp, unity]
paired_document: "coding-conventions_KOR.md"
parent_documents:
  - "../../project/SPEC.md"
child_documents: []
references:
  - "./documentation-rules.md"
  - "../architecture/project-overview.md"
  - "../architecture/scope-system.md"
status: "approved"
---

# Coding Conventions

## Namespace Organization

### Structure
```csharp
namespace HaroFramework.[Category]
{
    // Code here
}
```

### Categories
- **Core**: Framework core systems
- **Player**: Player-related systems
- **AI**: Artificial intelligence
- **UI**: User interface
- **Audio**: Audio systems
- **Gameplay**: Gameplay mechanics
- **Systems**: Game systems (save, settings, etc.)
- **Data**: ScriptableObject definitions
- **Editor**: Editor extensions
- **Tests**: Test code

### Examples
```csharp
namespace HaroFramework.Player
namespace HaroFramework.AI.Pathfinding
namespace HaroFramework.UI.Menus
namespace HaroFramework.Data
```

## Naming Conventions

### Classes and Structs
- **PascalCase**
- Descriptive names
```csharp
public class PlayerController { }
public class HealthSystem { }
public struct DamageInfo { }
```

### Methods
- **PascalCase**
- Verb-noun format
```csharp
public void TakeDamage(int amount) { }
private void UpdateHealth() { }
```

### Fields
- **Private**: `_camelCase` with underscore prefix
- **Public**: `PascalCase`
- **Const/Static Readonly**: `PascalCase`

```csharp
private int _health;
private Transform _targetTransform;

public int MaxHealth { get; private set; }

private const int DefaultHealth = 100;
private static readonly Vector3 StartPosition = Vector3.zero;
```

### Properties
- **PascalCase**
- Prefer auto-properties
```csharp
public int Health { get; private set; }
public bool IsAlive => Health > 0;
```

### Serialized Fields
```csharp
[Header("Configuration")]
[Tooltip("Maximum health value")]
[SerializeField] private int _maxHealth = 100;

[Range(0f, 1f)]
[SerializeField] private float _damageReduction = 0.1f;
```

### Unity Event Functions
- Standard Unity naming
```csharp
private void Awake() { }
private void Start() { }
private void Update() { }
private void OnEnable() { }
private void OnDisable() { }
```

## Code Structure

### Region Organization
```csharp
public class ExampleComponent : MonoBehaviour
{
    #region Inspector Fields
    [SerializeField] private Type _field;
    #endregion

    #region Private Fields
    private Type _cachedComponent;
    #endregion

    #region Properties
    public Type Property { get; private set; }
    #endregion

    #region Unity Lifecycle
    private void Awake() { }
    private void Start() { }
    #endregion

    #region Public Methods
    public void PublicMethod() { }
    #endregion

    #region Private Methods
    private void PrivateMethod() { }
    #endregion

    #region Editor
    #if UNITY_EDITOR
    private void OnValidate() { }
    #endif
    #endregion
}
```

## Unity Best Practices

### Component Caching
```csharp
// Cache in Awake
private Transform _transform;

private void Awake()
{
    _transform = transform;
}
```

### GetComponent Usage
```csharp
// Avoid in Update
private void Update()
{
    // ❌ Bad
    GetComponent<Rigidbody>().AddForce(Vector3.up);
}

// Cache in Awake
private Rigidbody _rigidbody;

private void Awake()
{
    _rigidbody = GetComponent<Rigidbody>();
}

private void Update()
{
    // ✅ Good
    _rigidbody.AddForce(Vector3.up);
}
```

### RequireComponent
```csharp
[RequireComponent(typeof(Rigidbody))]
public class PhysicsController : MonoBehaviour
{
    private Rigidbody _rigidbody;

    private void Awake()
    {
        _rigidbody = GetComponent<Rigidbody>();
    }
}
```

### Coroutines
```csharp
// Store reference to stop later
private Coroutine _damageCoroutine;

public void StartDamageOverTime()
{
    if (_damageCoroutine != null)
        StopCoroutine(_damageCoroutine);

    _damageCoroutine = StartCoroutine(DamageCoroutine());
}

private IEnumerator DamageCoroutine()
{
    while (true)
    {
        TakeDamage(1);
        yield return new WaitForSeconds(1f);
    }
}
```

## Documentation

### XML Comments
```csharp
/// <summary>
/// Applies damage to the entity and triggers damage events.
/// </summary>
/// <param name="amount">Amount of damage to apply</param>
/// <returns>True if damage was applied successfully</returns>
public bool TakeDamage(int amount)
{
    // Implementation
}
```

### TODO Comments
```csharp
// TODO: Implement damage resistance
// FIXME: Health can go negative
// NOTE: This method is called by the animation event
```

## Error Handling

### Null Checks
```csharp
// Inspector references
private void Start()
{
    if (_targetTransform == null)
    {
        Debug.LogError($"{name}: Target transform not assigned!", this);
        enabled = false;
        return;
    }
}
```

### Validation
```csharp
#if UNITY_EDITOR
private void OnValidate()
{
    _maxHealth = Mathf.Max(1, _maxHealth);

    if (_healthBar == null)
        Debug.LogWarning($"{name}: Health bar reference missing", this);
}
#endif
```

## Performance Guidelines

### Avoid in Update
- String concatenation
- GetComponent calls
- Find operations
- Instantiate/Destroy
- Complex calculations

### Prefer
- Cached references
- Object pooling
- Fixed timestep for physics
- Coroutines for delayed actions
- Events over polling

### String Handling
```csharp
// ❌ Avoid in loops
for (int i = 0; i < 100; i++)
{
    string result = "Item " + i;
}

// ✅ Use StringBuilder
StringBuilder sb = new StringBuilder();
for (int i = 0; i < 100; i++)
{
    sb.Clear();
    sb.Append("Item ").Append(i);
}
```

## Unity 6 Specific

### FindObjectOfType Replacement
```csharp
// Unity 6 - Use FindFirstObjectByType
var manager = FindFirstObjectByType<GameManager>();

// Old way (deprecated)
var manager = FindObjectOfType<GameManager>();
```

### MonoBehaviour Spelling
```csharp
// Unity 6 - Correct spelling
public class MyComponent : MonoBehaviour { }

// Not "Behavior" anymore
```

## Assembly Definitions

### Naming
- `HaroFramework.Runtime` - Runtime code
- `HaroFramework.Editor` - Editor code
- `HaroFramework.Tests` - Test code

### References
- Editor assemblies reference Runtime
- Tests reference what they test
- Minimize cross-assembly dependencies

## File Organization

```
Scripts/
├── Runtime/
│   ├── Core/
│   ├── Player/
│   ├── AI/
│   └── HaroFramework.Runtime.asmdef
├── Editor/
│   ├── Inspectors/
│   ├── Tools/
│   └── HaroFramework.Editor.asmdef
└── Tests/
    ├── EditMode/
    ├── PlayMode/
    └── *.asmdef files
```

## Code Review Checklist

- [ ] Follows naming conventions
- [ ] Proper namespace usage
- [ ] XML documentation for public APIs
- [ ] No compiler warnings
- [ ] Cached component references
- [ ] Null checks for required references
- [ ] OnValidate for field validation
- [ ] No magic numbers (use const/readonly)
- [ ] Proper region organization
- [ ] Performance considerations addressed

## Related Documentation

- [SPEC.md](../../project/SPEC.md) - Complete project specification
- [Documentation Rules](./documentation-rules.md) - Documentation standards
- [Scope System](../architecture/scope-system.md) - 2-Scope architecture
- [Project Overview](../architecture/project-overview.md) - Project structure

---

**Document Status**: Approved
**Version**: 1.0.0
**Last Updated**: 2025-10-25
