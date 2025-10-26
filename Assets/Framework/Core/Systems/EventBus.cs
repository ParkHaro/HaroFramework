using System;
using System.Collections.Generic;

namespace HaroFramework.Core
{
    /// <summary>
    /// Marker interface for all game events.
    /// </summary>
    /// <remarks>
    /// All event classes must implement this interface.
    /// Events should be immutable data containers with no logic.
    /// </remarks>
    public interface IGameEvent { }

    /// <summary>
    /// Central event bus for loose coupling between game systems.
    /// </summary>
    /// <remarks>
    /// Provides publish-subscribe pattern for game-wide communication.
    /// Events are processed synchronously in the order they are published.
    /// Remember to unsubscribe in OnDestroy to prevent memory leaks.
    /// </remarks>
    public class EventBus : Singleton<EventBus>
    {
        #region Fields

        private readonly Dictionary<Type, List<Delegate>> _eventHandlers = new Dictionary<Type, List<Delegate>>();

        #endregion

        #region Public Methods

        /// <summary>
        /// Subscribes to an event type.
        /// </summary>
        /// <typeparam name="T">The type of event to subscribe to.</typeparam>
        /// <param name="handler">The handler to call when the event is published.</param>
        /// <remarks>
        /// Multiple handlers can be subscribed to the same event type.
        /// Handlers are called in the order they were subscribed.
        /// </remarks>
        public void Subscribe<T>(Action<T> handler) where T : IGameEvent
        {
            Type eventType = typeof(T);

            if (!_eventHandlers.ContainsKey(eventType))
            {
                _eventHandlers[eventType] = new List<Delegate>();
            }

            if (!_eventHandlers[eventType].Contains(handler))
            {
                _eventHandlers[eventType].Add(handler);
            }
        }

        /// <summary>
        /// Unsubscribes from an event type.
        /// </summary>
        /// <typeparam name="T">The type of event to unsubscribe from.</typeparam>
        /// <param name="handler">The handler to remove.</param>
        /// <remarks>
        /// Always unsubscribe in OnDestroy to prevent memory leaks.
        /// Safe to call even if the handler was never subscribed.
        /// </remarks>
        public void Unsubscribe<T>(Action<T> handler) where T : IGameEvent
        {
            Type eventType = typeof(T);

            if (_eventHandlers.ContainsKey(eventType))
            {
                _eventHandlers[eventType].Remove(handler);

                if (_eventHandlers[eventType].Count == 0)
                {
                    _eventHandlers.Remove(eventType);
                }
            }
        }

        /// <summary>
        /// Publishes an event to all subscribers.
        /// </summary>
        /// <typeparam name="T">The type of event to publish.</typeparam>
        /// <param name="gameEvent">The event instance to publish.</param>
        /// <remarks>
        /// Events are processed synchronously in the order handlers were subscribed.
        /// If a handler throws an exception, subsequent handlers will not be called.
        /// </remarks>
        public void Publish<T>(T gameEvent) where T : IGameEvent
        {
            Type eventType = typeof(T);

            if (_eventHandlers.ContainsKey(eventType))
            {
                // Create a copy to avoid modification during iteration
                List<Delegate> handlers = new List<Delegate>(_eventHandlers[eventType]);

                foreach (Delegate handler in handlers)
                {
                    (handler as Action<T>)?.Invoke(gameEvent);
                }
            }
        }

        /// <summary>
        /// Clears all event subscriptions.
        /// </summary>
        /// <remarks>
        /// Useful for cleanup during scene transitions or application shutdown.
        /// Use with caution as it will remove all subscribers.
        /// </remarks>
        public void Clear()
        {
            _eventHandlers.Clear();
        }

        #endregion
    }
}
