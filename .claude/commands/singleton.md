---
description: Create a singleton MonoBehaviour pattern
argument-hint: <ClassName>
---

Create a thread-safe singleton MonoBehaviour pattern.

Class name: $ARGUMENTS

**Generate:**
```csharp
using UnityEngine;

namespace HaroFramework.Core
{
    /// <summary>
    /// Singleton implementation of $ARGUMENTS
    /// </summary>
    public class $ARGUMENTS : MonoBehaviour
    {
        private static $ARGUMENTS _instance;
        private static readonly object _lock = new object();
        private static bool _applicationIsQuitting = false;

        public static $ARGUMENTS Instance
        {
            get
            {
                if (_applicationIsQuitting)
                {
                    Debug.LogWarning($"[{nameof($ARGUMENTS)}] Instance already destroyed. Returning null.");
                    return null;
                }

                lock (_lock)
                {
                    if (_instance == null)
                    {
                        _instance = FindFirstObjectByType<$ARGUMENTS>();

                        if (_instance == null)
                        {
                            GameObject singleton = new GameObject($"{nameof($ARGUMENTS)} (Singleton)");
                            _instance = singleton.AddComponent<$ARGUMENTS>();
                            DontDestroyOnLoad(singleton);
                        }
                    }

                    return _instance;
                }
            }
        }

        protected virtual void Awake()
        {
            if (_instance == null)
            {
                _instance = this as $ARGUMENTS;
                DontDestroyOnLoad(gameObject);
            }
            else if (_instance != this)
            {
                Destroy(gameObject);
            }
        }

        protected virtual void OnDestroy()
        {
            if (_instance == this)
            {
                _applicationIsQuitting = true;
            }
        }
    }
}
```

**Features:**
- Thread-safe lazy initialization
- Handles scene reloads
- Prevents duplicate instances
- DontDestroyOnLoad support
