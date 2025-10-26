using System.Collections.Generic;
using HaroFramework.Data;

namespace HaroFramework.Core
{
    /// <summary>
    /// Base class for all domain logic classes.
    /// </summary>
    /// <typeparam name="TData">The type of data this domain manages.</typeparam>
    /// <remarks>
    /// Domains handle data loading, caching, and business logic.
    /// They process raw data and apply game rules/calculations.
    /// Domains are registered with DataManager and accessed through it.
    /// </remarks>
    public abstract class BaseDomain<TData> where TData : BaseData
    {
        #region Properties

        /// <summary>
        /// Gets the unique name of this domain.
        /// </summary>
        public abstract string DomainName { get; }

        #endregion

        #region Lifecycle Methods

        /// <summary>
        /// Loads and processes data for this domain.
        /// </summary>
        /// <remarks>
        /// Called by DataManager during initialization.
        /// Implement data loading from JSON, CSV, or other sources.
        /// Apply business rules and cache processed data.
        /// </remarks>
        public abstract void LoadData();

        #endregion

        #region Data Access Methods

        /// <summary>
        /// Gets a single data entry by ID.
        /// </summary>
        /// <param name="id">The unique identifier of the data entry.</param>
        /// <returns>The data entry, or null if not found.</returns>
        public abstract TData GetData(int id);

        /// <summary>
        /// Gets all data entries in this domain.
        /// </summary>
        /// <returns>An enumerable collection of all data entries.</returns>
        public abstract IEnumerable<TData> GetAllData();

        #endregion
    }
}
