namespace HaroFramework.Core
{
    /// <summary>
    /// Base class for all framework modules.
    /// </summary>
    /// <remarks>
    /// Modules provide game-independent functionality (UI, Audio, Scene, Network, etc.).
    /// They are initialized by FrameworkManager in priority order.
    /// Override lifecycle methods to implement module-specific behavior.
    /// </remarks>
    public abstract class BaseModule : IModule
    {
        #region Properties

        /// <summary>
        /// Gets the unique name of this module.
        /// </summary>
        public abstract string ModuleName { get; }

        /// <summary>
        /// Gets the initialization priority of this module.
        /// Lower values are initialized first (e.g., 5 before 10).
        /// </summary>
        public abstract int Priority { get; }

        #endregion

        #region Lifecycle Methods

        /// <summary>
        /// Initializes the module.
        /// </summary>
        /// <remarks>
        /// Called by FrameworkManager in priority order.
        /// Use this to set up resources and register dependencies.
        /// </remarks>
        public virtual void Initialize()
        {
            // Override in derived classes
        }

        /// <summary>
        /// Shuts down the module and releases resources.
        /// </summary>
        /// <remarks>
        /// Called by FrameworkManager in reverse priority order.
        /// Use this to clean up resources and unregister dependencies.
        /// </remarks>
        public virtual void Shutdown()
        {
            // Override in derived classes
        }

        /// <summary>
        /// Called every frame by FrameworkManager.
        /// </summary>
        /// <remarks>
        /// Use this for module-specific per-frame updates.
        /// Keep logic lightweight to avoid performance issues.
        /// </remarks>
        public virtual void OnUpdate()
        {
            // Override in derived classes
        }

        #endregion
    }
}
