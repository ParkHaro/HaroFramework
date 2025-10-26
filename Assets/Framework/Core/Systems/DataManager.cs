using System;
using System.Collections.Generic;
using UnityEngine;
using HaroFramework.Data;

namespace HaroFramework.Core
{
    /// <summary>
    /// Central manager for all domain objects.
    /// </summary>
    /// <remarks>
    /// Manages registration and access to domain objects.
    /// Domains handle data loading, caching, and business logic.
    /// Call LoadAllDomains during game initialization to load all data.
    /// </remarks>
    public class DataManager : Singleton<DataManager>
    {
        #region Fields

        private readonly Dictionary<Type, object> _domains = new Dictionary<Type, object>();
        private bool _isLoaded = false;

        #endregion

        #region Public Methods

        /// <summary>
        /// Registers a domain with the manager.
        /// </summary>
        /// <typeparam name="TDomain">The type of domain to register.</typeparam>
        /// <typeparam name="TData">The type of data the domain manages.</typeparam>
        /// <param name="domain">The domain instance to register.</param>
        /// <remarks>
        /// Domains must be registered before LoadAllDomains is called.
        /// Registering a domain with the same type twice will overwrite the previous registration.
        /// </remarks>
        public void RegisterDomain<TDomain, TData>(TDomain domain)
            where TDomain : BaseDomain<TData>
            where TData : BaseData
        {
            Type domainType = typeof(TDomain);

            if (_domains.ContainsKey(domainType))
            {
                Debug.LogWarning($"[DataManager] Domain of type {domainType.Name} is already registered. Overwriting.");
            }

            _domains[domainType] = domain;
            Debug.Log($"[DataManager] Registered domain: {domainType.Name}");
        }

        /// <summary>
        /// Gets a registered domain.
        /// </summary>
        /// <typeparam name="TDomain">The type of domain to retrieve.</typeparam>
        /// <returns>The domain instance.</returns>
        /// <exception cref="InvalidOperationException">Thrown if the domain is not registered.</exception>
        /// <remarks>
        /// Domains must be registered before they can be retrieved.
        /// Use HasDomain&lt;TDomain&gt;() to check if a domain is registered.
        /// </remarks>
        public TDomain GetDomain<TDomain>() where TDomain : class
        {
            Type domainType = typeof(TDomain);

            if (_domains.ContainsKey(domainType))
            {
                return _domains[domainType] as TDomain;
            }

            throw new InvalidOperationException($"[DataManager] Domain of type {domainType.Name} is not registered.");
        }

        /// <summary>
        /// Checks if a domain is registered.
        /// </summary>
        /// <typeparam name="TDomain">The type of domain to check.</typeparam>
        /// <returns>True if the domain is registered, false otherwise.</returns>
        public bool HasDomain<TDomain>() where TDomain : class
        {
            return _domains.ContainsKey(typeof(TDomain));
        }

        /// <summary>
        /// Loads data for all registered domains.
        /// </summary>
        /// <remarks>
        /// Should be called once during game initialization, after all domains are registered.
        /// Calls LoadData on each domain in registration order.
        /// This operation may take time depending on data size.
        /// </remarks>
        public void LoadAllDomains()
        {
            if (_isLoaded)
            {
                Debug.LogWarning("[DataManager] Domains already loaded. Skipping.");
                return;
            }

            Debug.Log("[DataManager] Loading all domains...");

            foreach (var kvp in _domains)
            {
                Type domainType = kvp.Key;
                object domain = kvp.Value;

                try
                {
                    // Get LoadData method through reflection
                    var loadDataMethod = domainType.GetMethod("LoadData");
                    loadDataMethod?.Invoke(domain, null);

                    Debug.Log($"[DataManager] Loaded domain: {domainType.Name}");
                }
                catch (Exception ex)
                {
                    Debug.LogError($"[DataManager] Failed to load domain {domainType.Name}: {ex.Message}");
                }
            }

            _isLoaded = true;
            Debug.Log("[DataManager] All domains loaded successfully.");
        }

        /// <summary>
        /// Clears all registered domains.
        /// </summary>
        /// <remarks>
        /// Useful for cleanup during scene transitions or application shutdown.
        /// After clearing, domains must be re-registered and loaded.
        /// </remarks>
        public void Clear()
        {
            _domains.Clear();
            _isLoaded = false;
            Debug.Log("[DataManager] Cleared all domains.");
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
