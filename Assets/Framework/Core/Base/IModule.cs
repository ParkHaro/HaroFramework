namespace HaroFramework.Core
{
    /// <summary>
    /// Interface for all framework modules.
    /// Modules provide game-independent functionality and are initialized by FrameworkManager.
    /// </summary>
    /// <remarks>
    /// Modules are initialized in priority order (lower priority number = earlier initialization).
    /// All modules must implement Initialize, Shutdown, and OnUpdate lifecycle methods.
    /// </remarks>
    public interface IModule
    {
        #region Properties

        /// <summary>
        /// Gets the unique name of this module.
        /// </summary>
        string ModuleName { get; }

        /// <summary>
        /// Gets the initialization priority of this module.
        /// Lower values are initialized first.
        /// </summary>
        int Priority { get; }

        #endregion

        #region Lifecycle Methods

        /// <summary>
        /// Initializes the module.
        /// Called by FrameworkManager in priority order.
        /// </summary>
        void Initialize();

        /// <summary>
        /// Shuts down the module and releases resources.
        /// Called in reverse priority order.
        /// </summary>
        void Shutdown();

        /// <summary>
        /// Called every frame by FrameworkManager.
        /// </summary>
        void OnUpdate();

        #endregion
    }
}
