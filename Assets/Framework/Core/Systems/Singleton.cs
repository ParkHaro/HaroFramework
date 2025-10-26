using UnityEngine;

namespace HaroFramework.Core
{
    /// <summary>
    /// Generic singleton pattern for MonoBehaviour classes.
    /// </summary>
    /// <typeparam name="T">The type of the singleton class.</typeparam>
    /// <remarks>
    /// Provides thread-safe lazy initialization of singleton instances.
    /// Automatically creates a GameObject with DontDestroyOnLoad if instance doesn't exist.
    /// Use this for manager classes that need to persist across scenes.
    /// </remarks>
    public class Singleton<T> : MonoBehaviour where T : MonoBehaviour
    {
        #region Fields

        private static T _instance;
        private static object _lock = new object();
        private static bool _applicationIsQuitting = false;

        #endregion

        #region Properties

        /// <summary>
        /// Gets the singleton instance.
        /// Creates a new instance if one doesn't exist.
        /// </summary>
        public static T Instance
        {
            get
            {
                if (_applicationIsQuitting)
                {
                    Debug.LogWarning($"[Singleton] Instance of {typeof(T)} already destroyed. Returning null.");
                    return null;
                }

                lock (_lock)
                {
                    if (_instance == null)
                    {
                        _instance = FindFirstObjectByType<T>();

                        if (_instance == null)
                        {
                            GameObject singletonObject = new GameObject();
                            _instance = singletonObject.AddComponent<T>();
                            singletonObject.name = $"{typeof(T).Name} (Singleton)";

                            DontDestroyOnLoad(singletonObject);
                        }
                    }

                    return _instance;
                }
            }
        }

        #endregion

        #region Unity Lifecycle

        /// <summary>
        /// Called when the application quits.
        /// </summary>
        protected virtual void OnApplicationQuit()
        {
            _applicationIsQuitting = true;
        }

        /// <summary>
        /// Called when the MonoBehaviour is destroyed.
        /// </summary>
        protected virtual void OnDestroy()
        {
            if (_instance == this)
            {
                _applicationIsQuitting = true;
            }
        }

        #endregion
    }
}
