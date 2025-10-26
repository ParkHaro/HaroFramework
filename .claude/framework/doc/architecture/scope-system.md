---
title: 2-Scope Architecture System
version: 1.0.0
scope: framework
created: 2025-10-25
modified: 2025-10-26
category: Architecture
tags: [architecture, scopes, design, separation-of-concerns]
paired_document: scope-system_KOR.md
parent_documents:
  - ../../project/SPEC.md
child_documents: []
references:
  - ../guidelines/documentation-rules.md
  - ../guidelines/coding-conventions.md
status: approved
---



<!-- Navigation -->
**🏠 [HaroFramework Project](../../../MASTER_INDEX.md)** | **📂 [2-Scope Architecture System](./)** | **⬆️ [HaroFramework Specification](../../project/SPEC.md)**

---
# 2-Scope Architecture System

## Overview

HaroFramework uses a strict **2-scope architecture** to ensure the framework remains reusable across multiple game projects. This architecture enforces clear separation between framework code and game-specific code through unidirectional dependency rules.

**Key Principle**: The framework must be game-agnostic and reusable, while games are free to use and extend the framework.

---

## Architecture Scopes

### Scope 1: Framework Scope (Base/Foundation)

**Purpose**: Provide reusable game systems, utilities, and patterns that can be leveraged across multiple game projects.

**Characteristics**:
- **Independent**: Has no knowledge of any game project
- **Reusable**: Can be used by any game without modification
- **Generic**: Provides general-purpose systems and tools
- **Stable**: Changes infrequently, maintains backward compatibility
- **Well-Documented**: Comprehensive documentation and examples

**Location**:
- Code: `Assets/Scripts/Runtime/` (with HaroFramework namespace)
- Documentation: `.claude/framework/`

**Namespace Convention**:
```csharp
namespace HaroFramework.Core
namespace HaroFramework.Player
namespace HaroFramework.AI
namespace HaroFramework.UI
// etc.
```

**Responsibilities**:
- Core systems (Player, AI, UI, Audio, etc.)
- Common utilities and helpers
- Framework initialization and lifecycle
- Service locator and dependency injection
- Event system and messaging
- Object pooling and memory management
- Data structures and containers
- Editor tools and utilities
- Framework testing infrastructure

**What Framework Scope Contains**:
- ✅ Abstract base classes for game systems
- ✅ Interfaces and contracts
- ✅ Utility functions and extensions
- ✅ Common data structures
- ✅ Design pattern implementations
- ✅ Generic systems (input, audio, etc.)
- ✅ Editor tools for framework

**What Framework Scope NEVER Contains**:
- ❌ Game-specific logic or rules
- ❌ Game content or assets
- ❌ References to game code
- ❌ Game-specific configurations
- ❌ Knowledge of game existence

---

### Scope 2: Game Scope (Implementation)

**Purpose**: Implement specific game logic, content, and mechanics using the framework as a foundation.

**Characteristics**:
- **Dependent**: Relies on and extends the Framework Scope
- **Specific**: Contains game-specific implementations
- **Flexible**: Can be modified frequently for game needs
- **Concrete**: Implements actual game behavior
- **Custom**: Tailored to specific game requirements

**Location**:
- Code: `Assets/Scripts/Runtime/` (game-specific namespaces)
- Documentation: `.claude/games/[game-name]/`

**Namespace Convention**:
```csharp
namespace GameName.Gameplay
namespace GameName.Characters
namespace GameName.Levels
// etc.
```

**Responsibilities**:
- Game-specific implementations
- Game rules and mechanics
- Game content and data
- Level design and progression
- Game UI and menus
- Game-specific editor tools
- Game testing

**What Game Scope Contains**:
- ✅ Concrete implementations of framework systems
- ✅ Game-specific logic and rules
- ✅ Game content and configurations
- ✅ Custom game mechanics
- ✅ Level-specific scripts
- ✅ Game UI implementations
- ✅ References to framework code

**What Game Scope Should Avoid**:
- ⚠️ Modifying framework code directly (extend instead)
- ⚠️ Duplicating framework functionality
- ⚠️ Working around framework limitations (request framework changes)

---

## Dependency Rules

### The Golden Rule: Unidirectional Dependency

```
┌─────────────┐
│  Game Scope │
└──────┬──────┘
       │ depends on
       ↓ (✅ ALLOWED)
┌─────────────────┐
│ Framework Scope │
└─────────────────┘
       │
       ↑ (❌ FORBIDDEN)
       │ cannot depend on
┌──────────────┐
│  Game Scope  │
└──────────────┘
```

### Rule 1: Game → Framework (✅ ALLOWED)

**Game Scope CAN**:
- Import and use framework classes
- Inherit from framework base classes
- Implement framework interfaces
- Call framework APIs
- Reference framework documentation
- Extend framework functionality
- Use framework utilities

**Examples**:
```csharp
// ✅ Game class inheriting from framework
namespace MyGame.Characters
{
    using HaroFramework.Player;

    public class MyGamePlayer : PlayerController
    {
        // Game-specific player implementation
    }
}

// ✅ Game using framework utilities
namespace MyGame.Gameplay
{
    using HaroFramework.Core;

    public class GameManager : MonoBehaviour
    {
        private ServiceLocator _services;

        private void Awake()
        {
            _services = ServiceLocator.Instance;
        }
    }
}
```

### Rule 2: Framework → Game (❌ FORBIDDEN)

**Framework Scope CANNOT**:
- Import game classes
- Reference game-specific code
- Know about game existence
- Contain game-specific logic
- Link to game documentation
- Call game APIs

**Why This Rule Exists**:
1. **Reusability**: Framework can be used by any game
2. **Maintainability**: Framework changes don't require game changes
3. **Testability**: Framework can be tested independently
4. **Modularity**: Clear separation of concerns
5. **Scalability**: Easy to add new games

---

## Architecture Diagrams

### High-Level Structure

```
┌───────────────────────────────────────────┐
│           Multiple Games                  │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ │
│  │  Game A  │ │  Game B  │ │  Game C  │ │
│  └────┬─────┘ └────┬─────┘ └────┬─────┘ │
│       └────────────┼────────────┘       │
└────────────────────┼──────────────────────┘
                     ↓ (all depend on)
         ┌───────────────────────┐
         │   HaroFramework       │
         │  (Shared Foundation)  │
         └───────────────────────┘
```

### Folder Structure

```
Assets/Scripts/
├── Runtime/
│   ├── HaroFramework/          # Framework Scope
│   │   ├── Core/
│   │   ├── Player/
│   │   ├── AI/
│   │   └── UI/
│   │
│   └── [GameName]/             # Game Scope
│       ├── Gameplay/
│       ├── Characters/
│       └── Levels/
│
├── Editor/
│   ├── HaroFramework/          # Framework Editor
│   └── [GameName]/             # Game Editor
│
└── Tests/
    ├── Framework/              # Framework Tests
    └── [GameName]/             # Game Tests
```

### Dependency Flow

```
Game Gameplay Logic
        ↓ uses
Game Character Controller (concrete)
        ↓ extends
Framework PlayerController (abstract)
        ↓ uses
Framework Core Systems
```

---

## Correct Architecture Examples

### Example 1: Framework Base Class, Game Implementation

**Framework Scope** (`HaroFramework.Player`):
```csharp
namespace HaroFramework.Player
{
    /// <summary>
    /// Base class for all player controllers.
    /// Provides common functionality for player movement and input.
    /// </summary>
    public abstract class PlayerController : MonoBehaviour
    {
        [SerializeField] protected float _moveSpeed = 5f;

        protected virtual void Update()
        {
            HandleInput();
            Move();
        }

        protected abstract void HandleInput();
        protected abstract void Move();

        /// <summary>
        /// Framework utility: Get movement direction from input.
        /// </summary>
        protected Vector2 GetMovementInput()
        {
            // Generic input handling
            return new Vector2(Input.GetAxis("Horizontal"),
                             Input.GetAxis("Vertical"));
        }
    }
}
```

**Game Scope** (`MyPlatformer.Player`):
```csharp
namespace MyPlatformer.Player
{
    using HaroFramework.Player;

    /// <summary>
    /// Platformer-specific player controller with jump mechanics.
    /// </summary>
    public class PlatformerPlayer : PlayerController
    {
        [SerializeField] private float _jumpForce = 10f;
        private Rigidbody2D _rigidbody;
        private bool _isGrounded;

        protected override void HandleInput()
        {
            // Game-specific: Handle jump input
            if (Input.GetButtonDown("Jump") && _isGrounded)
            {
                Jump();
            }
        }

        protected override void Move()
        {
            Vector2 input = GetMovementInput(); // Use framework utility
            _rigidbody.velocity = new Vector2(input.x * _moveSpeed,
                                             _rigidbody.velocity.y);
        }

        private void Jump()
        {
            // Game-specific jump implementation
            _rigidbody.AddForce(Vector2.up * _jumpForce, ForceMode2D.Impulse);
        }
    }
}
```

### Example 2: Framework Interface, Game Implementation

**Framework Scope** (`HaroFramework.Core`):
```csharp
namespace HaroFramework.Core
{
    /// <summary>
    /// Interface for objects that can take damage.
    /// </summary>
    public interface IDamageable
    {
        int Health { get; }
        int MaxHealth { get; }
        bool IsAlive { get; }

        void TakeDamage(int amount);
        void Heal(int amount);
    }
}
```

**Game Scope** (`MyGame.Combat`):
```csharp
namespace MyGame.Combat
{
    using HaroFramework.Core;

    /// <summary>
    /// Game-specific enemy with custom damage behavior.
    /// </summary>
    public class Enemy : MonoBehaviour, IDamageable
    {
        [SerializeField] private int _maxHealth = 100;
        private int _currentHealth;

        public int Health => _currentHealth;
        public int MaxHealth => _maxHealth;
        public bool IsAlive => _currentHealth > 0;

        private void Start()
        {
            _currentHealth = _maxHealth;
        }

        public void TakeDamage(int amount)
        {
            _currentHealth -= amount;

            // Game-specific: Play hurt animation
            PlayHurtAnimation();

            if (!IsAlive)
            {
                Die();
            }
        }

        public void Heal(int amount)
        {
            _currentHealth = Mathf.Min(_currentHealth + amount, _maxHealth);
        }

        private void PlayHurtAnimation()
        {
            // Game-specific animation logic
        }

        private void Die()
        {
            // Game-specific death logic
            Destroy(gameObject);
        }
    }
}
```

---

## Anti-Patterns (What NOT to Do)

### ❌ Anti-Pattern 1: Framework Referencing Game

**WRONG** - Framework code knowing about specific game:
```csharp
namespace HaroFramework.Player
{
    using MyGame.Characters; // ❌ Framework importing game!

    public class PlayerController : MonoBehaviour
    {
        public void Initialize()
        {
            // ❌ Framework creating game-specific objects
            var gamePlayer = new MyGamePlayer();
        }
    }
}
```

**CORRECT** - Use abstraction:
```csharp
namespace HaroFramework.Player
{
    // ✅ Framework provides abstract base
    public abstract class PlayerController : MonoBehaviour
    {
        public abstract void Initialize();
    }
}

namespace MyGame.Characters
{
    using HaroFramework.Player;

    // ✅ Game implements concrete behavior
    public class MyGamePlayer : PlayerController
    {
        public override void Initialize()
        {
            // Game-specific initialization
        }
    }
}
```

### ❌ Anti-Pattern 2: Hardcoded Game Values in Framework

**WRONG** - Framework with game-specific constants:
```csharp
namespace HaroFramework.Combat
{
    public class DamageSystem
    {
        // ❌ Game-specific values in framework
        private const int SWORD_DAMAGE = 25;
        private const int AXE_DAMAGE = 35;

        public void ApplyWeaponDamage(string weaponType)
        {
            // ❌ Framework knowing about specific weapons
        }
    }
}
```

**CORRECT** - Framework provides generic system:
```csharp
namespace HaroFramework.Combat
{
    // ✅ Framework provides generic damage system
    public class DamageSystem
    {
        public void ApplyDamage(IDamageable target, int amount)
        {
            target.TakeDamage(amount);
        }
    }
}

namespace MyGame.Items
{
    using HaroFramework.Combat;

    // ✅ Game defines specific weapons
    public class Weapon : MonoBehaviour
    {
        [SerializeField] private int _damage = 25;

        public void Attack(IDamageable target)
        {
            DamageSystem.Instance.ApplyDamage(target, _damage);
        }
    }
}
```

### ❌ Anti-Pattern 3: Mixing Framework and Game Code

**WRONG** - Framework and game logic in same class:
```csharp
namespace HaroFramework.UI
{
    public class MainMenu : MonoBehaviour
    {
        public void OnPlayClicked()
        {
            // ❌ Framework UI with game-specific logic
            StartMySpecificGame();
            LoadMyGameLevel("Level1");
        }
    }
}
```

**CORRECT** - Separate concerns:
```csharp
namespace HaroFramework.UI
{
    // ✅ Framework provides generic menu system
    public abstract class MenuBase : MonoBehaviour
    {
        public abstract void OnPlayClicked();
        public abstract void OnQuitClicked();
    }
}

namespace MyGame.UI
{
    using HaroFramework.UI;

    // ✅ Game implements specific menu behavior
    public class MyGameMainMenu : MenuBase
    {
        public override void OnPlayClicked()
        {
            // Game-specific logic
            GameManager.Instance.StartGame();
        }

        public override void OnQuitClicked()
        {
            Application.Quit();
        }
    }
}
```

---

## Practical Guidelines

### For Framework Developers

**DO**:
- ✅ Design for reusability across different game genres
- ✅ Use abstraction (abstract classes, interfaces)
- ✅ Provide extensibility points for games
- ✅ Write comprehensive documentation
- ✅ Think in terms of "systems" not "games"
- ✅ Use dependency injection and service locator
- ✅ Create editor tools for framework configuration

**DON'T**:
- ❌ Make assumptions about specific games
- ❌ Hardcode game-specific values or logic
- ❌ Reference game code in any way
- ❌ Create game-specific features

### For Game Developers

**DO**:
- ✅ Extend framework classes for game needs
- ✅ Implement framework interfaces
- ✅ Use framework utilities and systems
- ✅ Follow framework conventions and patterns
- ✅ Report framework limitations or bugs
- ✅ Request new framework features if needed

**DON'T**:
- ❌ Modify framework code directly
- ❌ Duplicate framework functionality
- ❌ Work around framework (fix framework instead)
- ❌ Bypass framework systems

---

## Validation and Enforcement

### Automated Validation

Use `scope_validate.py` script to enforce scope rules:
```bash
python .claude/scripts/scope_validate.py
```

This script:
- Parses all document metadata
- Extracts scope field and references
- Detects forbidden framework → game references
- Reports violations with file and line info

### Manual Review Checklist

During code review, verify:
- [ ] Framework code has no game imports
- [ ] Namespaces follow scope conventions
- [ ] No hardcoded game-specific values in framework
- [ ] Framework classes are abstract/generic
- [ ] Game code extends (not modifies) framework
- [ ] Documentation references respect scope boundaries

---

## Benefits of 2-Scope Architecture

### For Framework
- **Reusability**: Use across multiple game projects
- **Maintainability**: Changes isolated from games
- **Testability**: Framework tested independently
- **Modularity**: Clear system boundaries
- **Quality**: Higher quality through focus

### For Games
- **Productivity**: Leverage proven framework systems
- **Consistency**: Uniform patterns across games
- **Focus**: Concentrate on game-specific logic
- **Quality**: Framework bugs fixed for all games
- **Speed**: Faster development with framework foundation

---

## Migration from Monolithic to 2-Scope

If you have existing code that mixes framework and game concerns:

1. **Identify**: Determine which code is framework vs game
2. **Extract**: Move generic code to framework namespace
3. **Abstract**: Create abstract base classes in framework
4. **Implement**: Implement game-specific behavior in game scope
5. **Validate**: Run `scope_validate.py` to verify separation
6. **Test**: Ensure functionality unchanged after refactor

---

## FAQ

**Q: Can framework code use Unity-specific classes?**
A: Yes! Framework can use Unity classes (MonoBehaviour, Vector3, etc.) but should remain game-agnostic.

**Q: What if I need game-specific behavior in framework?**
A: Use abstraction. Framework provides abstract base or interface, game implements concrete behavior.

**Q: Can I have multiple games in one Unity project?**
A: Not recommended. Use framework as package/submodule and separate game projects.

**Q: What if framework is missing functionality I need?**
A: Request framework enhancement rather than working around in game code.

**Q: How do I share code between games?**
A: If truly reusable, add to framework. If game-specific, keep separate per game.

---

## Related Documentation

- [SPEC.md](../../project/SPEC.md) - Full project specification
- [documentation-rules.md](../guidelines/documentation-rules.md) - Documentation standards
- [coding-conventions.md](../guidelines/coding-conventions.md) - Code standards

---

**Document Status**: Approved
**Version**: 1.0.0
**Last Updated**: 2025-10-26
