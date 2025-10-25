---
description: Create Input System action map
argument-hint: <ActionMapName>
---

Create a new Input Action asset for Unity's Input System.

Action Map Name: $ARGUMENTS

**Note:** This project uses Unity Input System (1.14.2), not the legacy Input Manager.

**Generate:**
1. Create .inputactions asset structure
2. Define action map with common actions
3. Setup control schemes (Keyboard/Mouse, Gamepad, Touch)
4. Generate C# wrapper class

**Common Actions:**
- Movement (Vector2)
- Look (Vector2)
- Jump (Button)
- Interact (Button)
- Pause (Button)

**Control Bindings:**
- WASD/Arrow keys for movement
- Mouse for look
- Space for jump
- E for interact
- Escape for pause

Provide instructions for:
1. Creating the .inputactions file
2. Generating C# class
3. Using in scripts via PlayerInput component
