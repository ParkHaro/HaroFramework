namespace HaroFramework.Core
{
    /// <summary>
    /// Base class for all game services.
    /// </summary>
    /// <remarks>
    /// Services implement game-specific business logic and are registered with ServiceLocator.
    /// All services have access to EventBus and ServiceLocator for communication.
    /// Override Initialize and Dispose to implement service-specific setup and cleanup.
    /// </remarks>
    public abstract class BaseService : IService
    {
        #region Properties

        /// <summary>
        /// Gets the unique name of this service.
        /// </summary>
        public abstract string ServiceName { get; }

        /// <summary>
        /// Gets the EventBus instance for publishing and subscribing to events.
        /// </summary>
        protected EventBus EventBus => EventBus.Instance;

        /// <summary>
        /// Gets the ServiceLocator instance for accessing other services.
        /// </summary>
        protected ServiceLocator Services => ServiceLocator.Instance;

        #endregion

        #region Lifecycle Methods

        /// <summary>
        /// Initializes the service.
        /// </summary>
        /// <remarks>
        /// Called when the service is registered with ServiceLocator.
        /// Override this method to implement service-specific initialization.
        /// </remarks>
        public virtual void Initialize()
        {
            // Override in derived classes
        }

        /// <summary>
        /// Disposes the service and releases resources.
        /// </summary>
        /// <remarks>
        /// Called when the service is removed from ServiceLocator or application quits.
        /// Override this method to implement service-specific cleanup.
        /// </remarks>
        public virtual void Dispose()
        {
            // Override in derived classes
        }

        #endregion
    }
}
