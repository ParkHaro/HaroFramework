using System;

namespace HaroFramework.Core
{
    /// <summary>
    /// Interface for all game services.
    /// Services implement game-specific business logic and are registered with ServiceLocator.
    /// </summary>
    /// <remarks>
    /// Services should implement game-specific interfaces that inherit from IService.
    /// All services have access to EventBus and ServiceLocator through BaseService.
    /// </remarks>
    public interface IService : IDisposable
    {
        #region Properties

        /// <summary>
        /// Gets the unique name of this service.
        /// </summary>
        string ServiceName { get; }

        #endregion

        #region Lifecycle Methods

        /// <summary>
        /// Initializes the service.
        /// Called when the service is registered with ServiceLocator.
        /// </summary>
        void Initialize();

        #endregion
    }
}
