using System.Collections.Generic;
using System.Linq;
using UnityEngine;

namespace HaroFramework.Core
{
    /// <summary>
    /// Central manager for the HaroFramework.
    /// </summary>
    /// <remarks>
    /// Manages framework initialization, module lifecycle, and core systems.
    /// Add to a GameObject in the first scene and configure with FrameworkConfig.
    /// Automatically initializes on Awake if AutoInitialize is enabled.
    /// </remarks>
    [DefaultExecutionOrder(-100)]
    public class FrameworkManager : Singleton<FrameworkManager>
    {
        #region Inspector Fields

        [Header("Configuration")]
        [SerializeField]
        [Tooltip("Framework configuration asset")]
        private FrameworkConfig _config;

        #endregion

        #region Fields

        private List<IModule> _modules = new List<IModule>();
        private bool _isInitialized = false;

        #endregion

        #region Properties

        /// <summary>
        /// Gets whether the framework is initialized.
        /// </summary>
        public bool IsInitialized => _isInitialized;

        /// <summary>
        /// Gets the framework configuration.
        /// </summary>
        public FrameworkConfig Config => _config;

        #endregion

        #region Unity Lifecycle

        private void Awake()
        {
            if (_config == null)
            {
                Debug.LogError("[FrameworkManager] FrameworkConfig is not assigned. Please assign a config asset.");
                return;
            }

            if (_config.PersistAcrossScenes)
            {
                DontDestroyOnLoad(gameObject);
            }

            if (_config.AutoInitialize)
            {
                Initialize();
            }
        }

        private void Update()
        {
            if (!_isInitialized) return;

            // Update all modules
            foreach (var module in _modules)
            {
                module.OnUpdate();
            }
        }

        protected override void OnDestroy()
        {
            Shutdown();
            base.OnDestroy();
        }

        #endregion

        #region Public Methods

        /// <summary>
        /// Initializes the framework.
        /// </summary>
        /// <remarks>
        /// Initializes core systems and modules in priority order.
        /// Safe to call multiple times (will skip if already initialized).
        /// </remarks>
        public void Initialize()
        {
            if (_isInitialized)
            {
                FrameworkLogger.LogWarning("Framework already initialized. Skipping.");
                return;
            }

            FrameworkLogger.Log("Initializing HaroFramework...");

            // Initialize core systems
            InitializeCoreSystems();

            // Initialize modules
            InitializeModules();

            _isInitialized = true;
            FrameworkLogger.Log("HaroFramework initialized successfully.");
        }

        /// <summary>
        /// Shuts down the framework.
        /// </summary>
        /// <remarks>
        /// Shuts down modules and core systems in reverse order.
        /// Called automatically on application quit.
        /// </remarks>
        public void Shutdown()
        {
            if (!_isInitialized) return;

            FrameworkLogger.Log("Shutting down HaroFramework...");

            // Shutdown modules in reverse order
            for (int i = _modules.Count - 1; i >= 0; i--)
            {
                _modules[i].Shutdown();
                FrameworkLogger.Log($"Shutdown module: {_modules[i].ModuleName}");
            }

            _modules.Clear();

            // Shutdown core systems
            ShutdownCoreSystems();

            _isInitialized = false;
            FrameworkLogger.Log("HaroFramework shutdown complete.");
        }

        /// <summary>
        /// Registers a module with the framework.
        /// </summary>
        /// <param name="module">The module to register.</param>
        /// <remarks>
        /// Modules are initialized in priority order after registration.
        /// If framework is already initialized, the module is initialized immediately.
        /// </remarks>
        public void RegisterModule(IModule module)
        {
            if (_modules.Contains(module))
            {
                FrameworkLogger.LogWarning($"Module {module.ModuleName} is already registered.");
                return;
            }

            _modules.Add(module);
            _modules = _modules.OrderBy(m => m.Priority).ToList();

            FrameworkLogger.Log($"Registered module: {module.ModuleName} (Priority: {module.Priority})");

            if (_isInitialized)
            {
                module.Initialize();
                FrameworkLogger.Log($"Initialized module: {module.ModuleName}");
            }
        }

        /// <summary>
        /// Unregisters a module from the framework.
        /// </summary>
        /// <param name="module">The module to unregister.</param>
        public void UnregisterModule(IModule module)
        {
            if (!_modules.Contains(module))
            {
                FrameworkLogger.LogWarning($"Module {module.ModuleName} is not registered.");
                return;
            }

            module.Shutdown();
            _modules.Remove(module);

            FrameworkLogger.Log($"Unregistered module: {module.ModuleName}");
        }

        #endregion

        #region Private Methods

        private void InitializeCoreSystems()
        {
            FrameworkLogger.IsEnabled = _config.EnableLogging;

            if (_config.EnableEventBus)
            {
                _ = EventBus.Instance;
                FrameworkLogger.Log("EventBus initialized.");
            }

            if (_config.EnableServiceLocator)
            {
                _ = ServiceLocator.Instance;
                FrameworkLogger.Log("ServiceLocator initialized.");
            }

            if (_config.EnableDataManager)
            {
                _ = DataManager.Instance;
                FrameworkLogger.Log("DataManager initialized.");
            }
        }

        private void InitializeModules()
        {
            // Sort modules by priority
            _modules = _modules.OrderBy(m => m.Priority).ToList();

            // Initialize each module
            foreach (var module in _modules)
            {
                module.Initialize();
                FrameworkLogger.Log($"Initialized module: {module.ModuleName} (Priority: {module.Priority})");
            }
        }

        private void ShutdownCoreSystems()
        {
            if (_config.EnableDataManager && DataManager.Instance != null)
            {
                DataManager.Instance.Clear();
            }

            if (_config.EnableServiceLocator && ServiceLocator.Instance != null)
            {
                ServiceLocator.Instance.Clear();
            }

            if (_config.EnableEventBus && EventBus.Instance != null)
            {
                EventBus.Instance.Clear();
            }
        }

        #endregion
    }
}
