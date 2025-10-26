using System;
using System.Collections.Generic;
using UnityEngine;

namespace HaroFramework.Core
{
    /// <summary>
    /// Central service locator for runtime dependency resolution.
    /// </summary>
    /// <remarks>
    /// Provides centralized registration and access to game services.
    /// Services are registered by interface type and retrieved by the same type.
    /// All services must implement IService interface.
    /// </remarks>
    public class ServiceLocator : Singleton<ServiceLocator>
    {
        #region Fields

        private readonly Dictionary<Type, IService> _services = new Dictionary<Type, IService>();

        #endregion

        #region Public Methods

        /// <summary>
        /// Registers a service with the locator.
        /// </summary>
        /// <typeparam name="T">The interface type of the service.</typeparam>
        /// <param name="service">The service instance to register.</param>
        /// <remarks>
        /// Services are registered by interface type, not concrete type.
        /// Registering a service with the same type twice will overwrite the previous registration.
        /// The service's Initialize method is called automatically after registration.
        /// </remarks>
        public void Register<T>(T service) where T : IService
        {
            Type serviceType = typeof(T);

            if (_services.ContainsKey(serviceType))
            {
                Debug.LogWarning($"[ServiceLocator] Service of type {serviceType.Name} is already registered. Overwriting.");
                _services[serviceType].Dispose();
            }

            _services[serviceType] = service;
            service.Initialize();

            Debug.Log($"[ServiceLocator] Registered service: {serviceType.Name}");
        }

        /// <summary>
        /// Gets a registered service.
        /// </summary>
        /// <typeparam name="T">The interface type of the service.</typeparam>
        /// <returns>The service instance.</returns>
        /// <exception cref="InvalidOperationException">Thrown if the service is not registered.</exception>
        /// <remarks>
        /// Services must be registered before they can be retrieved.
        /// Use Has&lt;T&gt;() to check if a service is registered before calling Get&lt;T&gt;().
        /// </remarks>
        public T Get<T>() where T : IService
        {
            Type serviceType = typeof(T);

            if (_services.ContainsKey(serviceType))
            {
                return (T)_services[serviceType];
            }

            throw new InvalidOperationException($"[ServiceLocator] Service of type {serviceType.Name} is not registered.");
        }

        /// <summary>
        /// Checks if a service is registered.
        /// </summary>
        /// <typeparam name="T">The interface type of the service.</typeparam>
        /// <returns>True if the service is registered, false otherwise.</returns>
        public bool Has<T>() where T : IService
        {
            return _services.ContainsKey(typeof(T));
        }

        /// <summary>
        /// Unregisters a service from the locator.
        /// </summary>
        /// <typeparam name="T">The interface type of the service.</typeparam>
        /// <remarks>
        /// The service's Dispose method is called automatically before removal.
        /// Safe to call even if the service is not registered.
        /// </remarks>
        public void Unregister<T>() where T : IService
        {
            Type serviceType = typeof(T);

            if (_services.ContainsKey(serviceType))
            {
                _services[serviceType].Dispose();
                _services.Remove(serviceType);
                Debug.Log($"[ServiceLocator] Unregistered service: {serviceType.Name}");
            }
        }

        /// <summary>
        /// Clears all registered services.
        /// </summary>
        /// <remarks>
        /// Calls Dispose on all registered services before clearing.
        /// Useful during scene transitions or application shutdown.
        /// </remarks>
        public void Clear()
        {
            foreach (var service in _services.Values)
            {
                service.Dispose();
            }

            _services.Clear();
            Debug.Log("[ServiceLocator] Cleared all services.");
        }

        #endregion

        #region Unity Lifecycle

        protected override void OnDestroy()
        {
            Clear();
            base.OnDestroy();
        }

        #endregion
    }
}
