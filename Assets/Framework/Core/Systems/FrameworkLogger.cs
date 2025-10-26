using UnityEngine;

namespace HaroFramework.Core
{
    /// <summary>
    /// Log level enumeration for framework logging.
    /// </summary>
    public enum LogLevel
    {
        /// <summary>
        /// Informational messages for normal operation.
        /// </summary>
        Info,

        /// <summary>
        /// Warning messages for potential issues.
        /// </summary>
        Warning,

        /// <summary>
        /// Error messages for failures.
        /// </summary>
        Error
    }

    /// <summary>
    /// Centralized logging system for the framework.
    /// </summary>
    /// <remarks>
    /// Provides consistent logging with conditional compilation support.
    /// Logs are disabled in Release builds for performance.
    /// Use this instead of Debug.Log for framework code.
    /// </remarks>
    public static class FrameworkLogger
    {
        #region Fields

        private static bool _isEnabled = true;
        private const string LogPrefix = "[HaroFramework]";

        #endregion

        #region Properties

        /// <summary>
        /// Gets or sets whether logging is enabled.
        /// </summary>
        public static bool IsEnabled
        {
            get => _isEnabled;
            set => _isEnabled = value;
        }

        #endregion

        #region Public Methods

        /// <summary>
        /// Logs an informational message.
        /// </summary>
        /// <param name="message">The message to log.</param>
        /// <param name="context">Optional Unity object for context.</param>
        [System.Diagnostics.Conditional("UNITY_EDITOR")]
        [System.Diagnostics.Conditional("DEVELOPMENT_BUILD")]
        public static void Log(string message, Object context = null)
        {
            if (!_isEnabled) return;

            Debug.Log($"{LogPrefix} {message}", context);
        }

        /// <summary>
        /// Logs a warning message.
        /// </summary>
        /// <param name="message">The message to log.</param>
        /// <param name="context">Optional Unity object for context.</param>
        [System.Diagnostics.Conditional("UNITY_EDITOR")]
        [System.Diagnostics.Conditional("DEVELOPMENT_BUILD")]
        public static void LogWarning(string message, Object context = null)
        {
            if (!_isEnabled) return;

            Debug.LogWarning($"{LogPrefix} {message}", context);
        }

        /// <summary>
        /// Logs an error message.
        /// </summary>
        /// <param name="message">The message to log.</param>
        /// <param name="context">Optional Unity object for context.</param>
        public static void LogError(string message, Object context = null)
        {
            if (!_isEnabled) return;

            Debug.LogError($"{LogPrefix} {message}", context);
        }

        /// <summary>
        /// Logs a message with specified log level.
        /// </summary>
        /// <param name="level">The log level.</param>
        /// <param name="message">The message to log.</param>
        /// <param name="context">Optional Unity object for context.</param>
        public static void Log(LogLevel level, string message, Object context = null)
        {
            switch (level)
            {
                case LogLevel.Info:
                    Log(message, context);
                    break;
                case LogLevel.Warning:
                    LogWarning(message, context);
                    break;
                case LogLevel.Error:
                    LogError(message, context);
                    break;
            }
        }

        #endregion
    }
}
