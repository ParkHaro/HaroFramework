---
description: Analyze Unity scene structure
argument-hint: <scene-name>
---

Analyze a Unity scene file and report its structure.

Scene: $ARGUMENTS

**Analysis:**
1. Read scene YAML file from Assets/Scenes/$ARGUMENTS.unity
2. List GameObject hierarchy
3. Identify all components and scripts
4. Find missing references or broken prefabs
5. Check for performance issues (excessive objects, complex hierarchies)
6. Suggest optimizations

**Report:**
- Total GameObjects
- Active/Inactive objects
- Component types used
- Script dependencies
- Prefab instances
- Missing references
- Optimization opportunities