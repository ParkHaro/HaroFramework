using UnityEngine;

namespace HaroFramework.Core
{
    /// <summary>
    /// Base class for all gameplay-related MonoBehaviours.
    /// </summary>
    /// <remarks>
    /// Provides convenient access to framework services and event bus.
    /// Override Unity lifecycle methods (Awake, Start, OnDestroy) as needed.
    /// Override framework lifecycle methods (RegisterServices, SubscribeEvents, UnsubscribeEvents) for framework integration.
    /// </remarks>
    public abstract class BaseGameplay : MonoBehaviour
    {
        #region Properties

        /// <summary>
        /// Gets the ServiceLocator instance for accessing services.
        /// </summary>
        protected ServiceLocator Services => ServiceLocator.Instance;

        /// <summary>
        /// Gets the EventBus instance for publishing and subscribing to events.
        /// </summary>
        protected EventBus EventBus => EventBus.Instance;

        #endregion

        #region Unity Lifecycle

        /// <summary>
        /// Called when the script instance is being loaded.
        /// </summary>
        protected virtual void Awake()
        {
            RegisterServices();
        }

        /// <summary>
        /// Called before the first frame update.
        /// </summary>
        protected virtual void Start()
        {
            SubscribeEvents();
        }

        /// <summary>
        /// Called when the MonoBehaviour will be destroyed.
        /// </summary>
        protected virtual void OnDestroy()
        {
            UnsubscribeEvents();
        }

        #endregion

        #region Framework Lifecycle

        /// <summary>
        /// Register required services from ServiceLocator.
        /// </summary>
        /// <remarks>
        /// Called during Awake. Override to cache service references.
        /// Example: _inventoryService = Services.Get&lt;IInventorySystem&gt;();
        /// </remarks>
        protected virtual void RegisterServices()
        {
            // Override in derived classes
        }

        /// <summary>
        /// Subscribe to required events from EventBus.
        /// </summary>
        /// <remarks>
        /// Called during Start. Override to subscribe to game events.
        /// Example: EventBus.Subscribe&lt;ItemAddedEvent&gt;(OnItemAdded);
        /// </remarks>
        protected virtual void SubscribeEvents()
        {
            // Override in derived classes
        }

        /// <summary>
        /// Unsubscribe from all events.
        /// </summary>
        /// <remarks>
        /// Called during OnDestroy. Override to unsubscribe from game events.
        /// Example: EventBus.Unsubscribe&lt;ItemAddedEvent&gt;(OnItemAdded);
        /// </remarks>
        protected virtual void UnsubscribeEvents()
        {
            // Override in derived classes
        }

        #endregion
    }
}
