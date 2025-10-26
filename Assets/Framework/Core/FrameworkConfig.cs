using UnityEngine;

namespace HaroFramework.Core
{
    /// <summary>
    /// Configuration asset for framework settings.
    /// </summary>
    /// <remarks>
    /// Create via Assets/Create/HaroFramework/Framework Config.
    /// Configure which modules are enabled and their priorities.
    /// Assign to FrameworkManager in scene.
    /// </remarks>
    [CreateAssetMenu(fileName = "FrameworkConfig", menuName = "HaroFramework/Framework Config", order = 0)]
    public class FrameworkConfig : ScriptableObject
    {
        #region Module Settings

        [Header("Module Settings")]
        [Tooltip("Enable/disable framework logging")]
        public bool EnableLogging = true;

        [Tooltip("Enable EventBus system")]
        public bool EnableEventBus = true;

        [Tooltip("Enable ServiceLocator system")]
        public bool EnableServiceLocator = true;

        [Tooltip("Enable DataManager system")]
        public bool EnableDataManager = true;

        #endregion

        #region Framework Settings

        [Header("Framework Settings")]
        [Tooltip("Auto-initialize framework on Awake")]
        public bool AutoInitialize = true;

        [Tooltip("Enable DontDestroyOnLoad for framework manager")]
        public bool PersistAcrossScenes = true;

        #endregion

        #region Validation

        private void OnValidate()
        {
            // Ensure at least core systems are enabled
            if (!EnableEventBus && !EnableServiceLocator && !EnableDataManager)
            {
                Debug.LogWarning("[FrameworkConfig] At least one core system should be enabled for the framework to function properly.");
            }
        }

        #endregion
    }
}
