---
description: Build Unity project for specified platform
argument-hint: [platform]
---

Build the Unity project for the target platform (Windows/Mac/Linux/Android/iOS/WebGL).

Platform: $ARGUMENTS

**Tasks:**
1. Check EditorBuildSettings.asset for scenes in build
2. Validate all required assets and dependencies
3. Check for compilation errors
4. Provide the appropriate Unity command line build arguments
5. Suggest optimization opportunities

If platform is not specified, analyze current build settings and provide recommendations.
