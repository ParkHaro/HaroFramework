---
name: unity-scriptable
description: Create Unity ScriptableObjects for data-driven design including game configurations, events, item definitions, and shared data assets. Use when implementing data assets, event systems, or any data that should be independent of scene hierarchy.
allowed-tools: Read, Write, Edit, Glob, Grep
---

# Unity ScriptableObject Builder

Expert skill for creating production-ready Unity ScriptableObject assets for data-driven architecture.

## When to Use This Skill

Activate this skill when the user requests:
- Game configuration data (settings, balancing)
- Event systems (game events, channels)
- Item definitions (weapons, armor, consumables)
- Character stats and progression
- Audio/Visual effect configurations
- Shared runtime data between components
- Design-time data that persists between scenes

## ScriptableObject Benefits

- **Designer-Friendly**: Edit in Inspector without code changes
- **Memory Efficient**: Shared references, not duplicated data
- **Scene-Independent**: No GameObject dependency
- **Version Control**: Easy to track and merge changes
- **Runtime Creation**: Can be created at runtime if needed

## ScriptableObject Template

```csharp
using UnityEngine;

namespace HaroFramework.Data
{
    /// <summary>
    /// [Purpose and usage of this ScriptableObject]
    /// </summary>
    [CreateAssetMenu(
        fileName = "New[ClassName]",
        menuName = "HaroFramework/[Category]/[ClassName]",
        order = 0)]
    public class ClassName : ScriptableObject
    {
        #region Inspector Fields

        [Header("Basic Settings")]
        [Tooltip("Description")]
        [SerializeField] private Type _fieldName;

        [Header("Advanced Settings")]
        [SerializeField] private Type _advancedField;

        #endregion

        #region Properties

        public Type PropertyName => _fieldName;

        #endregion

        #region Unity Callbacks

        private void OnEnable()
        {
            // Initialize when asset is loaded
            // Subscribe to events if needed
        }

        private void OnDisable()
        {
            // Cleanup when asset is unloaded
            // Unsubscribe from events
        }

        private void OnValidate()
        {
            // Validate field values
            // Clamp ranges
            // Enforce constraints
        }

        #endregion

        #region Public Methods

        /// <summary>
        /// [Method description]
        /// </summary>
        public void MethodName()
        {

        }

        #endregion

        #region Private Methods

        private void ValidateData()
        {
            // Validation logic
        }

        #endregion

        #region Editor

        #if UNITY_EDITOR
        [ContextMenu("Validate All Data")]
        private void EditorValidate()
        {
            ValidateData();
            UnityEditor.EditorUtility.SetDirty(this);
        }
        #endif

        #endregion
    }
}
```

## Common Patterns

### 1. Game Event System
```csharp
[CreateAssetMenu(menuName = "HaroFramework/Events/GameEvent")]
public class GameEvent : ScriptableObject
{
    private readonly List<GameEventListener> _listeners = new();

    public void Raise()
    {
        for (int i = _listeners.Count - 1; i >= 0; i--)
            _listeners[i].OnEventRaised();
    }

    public void RegisterListener(GameEventListener listener)
        => _listeners.Add(listener);

    public void UnregisterListener(GameEventListener listener)
        => _listeners.Remove(listener);
}
```

### 2. Configuration Data
```csharp
[CreateAssetMenu(menuName = "HaroFramework/Config/GameSettings")]
public class GameSettings : ScriptableObject
{
    [Header("Audio")]
    [Range(0f, 1f)] public float masterVolume = 1f;
    [Range(0f, 1f)] public float musicVolume = 0.8f;
    [Range(0f, 1f)] public float sfxVolume = 1f;

    [Header("Graphics")]
    public int targetFrameRate = 60;
    public bool vSync = true;

    private void OnValidate()
    {
        masterVolume = Mathf.Clamp01(masterVolume);
        musicVolume = Mathf.Clamp01(musicVolume);
        sfxVolume = Mathf.Clamp01(sfxVolume);
        targetFrameRate = Mathf.Max(30, targetFrameRate);
    }
}
```

### 3. Item Definition
```csharp
[CreateAssetMenu(menuName = "HaroFramework/Items/Item")]
public class ItemData : ScriptableObject
{
    [Header("Basic Info")]
    public string itemName;
    [TextArea(3, 5)] public string description;
    public Sprite icon;

    [Header("Properties")]
    public ItemType type;
    public int maxStackSize = 1;
    public float weight;

    [Header("Values")]
    public int buyPrice;
    public int sellPrice;

    private void OnValidate()
    {
        maxStackSize = Mathf.Max(1, maxStackSize);
        sellPrice = Mathf.Min(sellPrice, buyPrice);
    }
}
```

### 4. Runtime Set (Shared Collection)
```csharp
[CreateAssetMenu(menuName = "HaroFramework/Sets/RuntimeSet")]
public class RuntimeSet<T> : ScriptableObject
{
    private readonly List<T> _items = new();

    public IReadOnlyList<T> Items => _items;

    public void Add(T item)
    {
        if (!_items.Contains(item))
            _items.Add(item);
    }

    public void Remove(T item)
        => _items.Remove(item);

    public void Clear()
        => _items.Clear();

    private void OnDisable()
        => _items.Clear();
}
```

### 5. Variable (Shared Value)
```csharp
[CreateAssetMenu(menuName = "HaroFramework/Variables/FloatVariable")]
public class FloatVariable : ScriptableObject
{
    [SerializeField] private float _value;

    public float Value
    {
        get => _value;
        set
        {
            _value = value;
            OnValueChanged?.Invoke(_value);
        }
    }

    public event System.Action<float> OnValueChanged;

    public void SetValue(float value) => Value = value;
    public void Add(float amount) => Value += amount;
}
```

## Best Practices

### Menu Organization
```csharp
// Good hierarchy
[CreateAssetMenu(menuName = "HaroFramework/Audio/SoundEffect", order = 0)]
[CreateAssetMenu(menuName = "HaroFramework/Audio/MusicTrack", order = 1)]
[CreateAssetMenu(menuName = "HaroFramework/Items/Weapon", order = 10)]
```

### Validation
```csharp
private void OnValidate()
{
    // Enforce constraints
    health = Mathf.Max(0, health);

    // Auto-generate values
    if (string.IsNullOrEmpty(id))
        id = System.Guid.NewGuid().ToString();

    // Validate references
    if (icon == null)
        Debug.LogWarning($"{name}: Missing icon reference");
}
```

### Runtime Creation
```csharp
// Create at runtime (for procedural generation)
var data = ScriptableObject.CreateInstance<ItemData>();
data.itemName = "Procedural Item";
// Note: Won't persist unless saved to disk
```

### Resource Loading
```csharp
// Load from Resources folder
var config = Resources.Load<GameSettings>("Config/GameSettings");

// Better: Use Addressables or direct references
[SerializeField] private GameSettings _settings;
```

## Categories for CreateAssetMenu

- **Events**: Game events, channels, signals
- **Config**: Settings, configurations, constants
- **Data**: Item definitions, character stats, progression
- **Audio**: Sound effects, music tracks, audio mixers
- **Variables**: Shared values, runtime sets
- **AI**: Behavior data, state machines, decision trees

## Questions to Ask

Before creating a ScriptableObject:
1. What data needs to be stored?
2. Will this be shared between multiple objects?
3. Should designers be able to create instances?
4. Does it need runtime modification?
5. Are there validation requirements?

## File Organization

```
Assets/
  Data/
    ScriptableObjects/
      Audio/
        *.asset
      Config/
        *.asset
      Items/
        *.asset
      Events/
        *.asset
  Scripts/
    Data/
      *.cs (ScriptableObject class definitions)
```

## Output Format

1. Create the .cs file in Assets/Scripts/Data/
2. Include complete, production-ready code
3. Add appropriate CreateAssetMenu attributes
4. Include OnValidate for data integrity
5. Add usage examples in comments
6. Suggest where to create asset instances
