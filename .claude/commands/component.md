---
description: Create a new MonoBehaviour component
argument-hint: <ComponentName> [namespace]
---

Create a well-structured Unity MonoBehaviour component.

Component: $1
Namespace: $2 (default: HaroFramework)

**Generate:**
```csharp
using UnityEngine;

namespace $2
{
    /// <summary>
    /// [Add description]
    /// </summary>
    public class $1 : MonoBehaviour
    {
        #region Serialized Fields

        #endregion

        #region Unity Lifecycle

        private void Awake()
        {

        }

        private void Start()
        {

        }

        #endregion

        #region Public Methods

        #endregion

        #region Private Methods

        #endregion
    }
}
```

**Best Practices:**
- Use [SerializeField] for inspector fields
- Cache components in Awake()
- Add [RequireComponent] if needed
- Include XML documentation
