using System;

namespace HaroFramework.Data
{
    /// <summary>
    /// Base class for all data structures in the framework.
    /// </summary>
    /// <remarks>
    /// All game data classes should inherit from BaseData.
    /// Data classes should be serializable and contain no game logic.
    /// Use Domain layer for data processing and business rules.
    /// </remarks>
    [Serializable]
    public abstract class BaseData
    {
        #region Inspector Fields

        /// <summary>
        /// Unique identifier for this data entry.
        /// </summary>
        public int Id;

        #endregion

        #region Public Methods

        /// <summary>
        /// Validates the data integrity.
        /// </summary>
        /// <returns>True if the data is valid, false otherwise.</returns>
        /// <remarks>
        /// Override this method to implement data-specific validation rules.
        /// Called after deserialization to ensure data integrity.
        /// </remarks>
        public abstract bool Validate();

        #endregion
    }
}
