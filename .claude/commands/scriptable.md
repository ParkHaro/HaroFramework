---
description: Create a ScriptableObject asset class
argument-hint: <ClassName> [namespace]
---



<!-- Navigation -->
**🏠 [HaroFramework Project](../MASTER_INDEX.md)** | **📂 [HaroFramework Commands Index](INDEX.md)** | **⬆️ [HaroFramework Commands Index](INDEX.md)**

---
Create a ScriptableObject class for data-driven design.

Class name: $1
Namespace: $2 (default: HaroFramework.Data)

**Generate:**
```csharp
using UnityEngine;

namespace $2
{
    /// <summary>
    /// [Add description]
    /// </summary>
    [CreateAssetMenu(fileName = "$1", menuName = "HaroFramework/$1")]
    public class $1 : ScriptableObject
    {
        #region Serialized Fields

        #endregion

        #region Properties

        #endregion

        #region Unity Callbacks

        private void OnValidate()
        {
            // Validation logic here
        }

        #endregion

        #region Public Methods

        #endregion
    }
}
```

**Use Cases:**
- Game configuration data
- Event systems
- Item definitions
- Character stats
- Level data
