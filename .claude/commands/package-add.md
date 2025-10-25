---
description: Add Unity package to project
argument-hint: <package-name>
---

Add a Unity package via Package Manager.

Package: $ARGUMENTS

**Steps:**
1. Read current Packages/manifest.json
2. Identify package source (Unity Registry, Git, or local)
3. Determine latest compatible version
4. Add package to dependencies
5. Check for dependency conflicts
6. Update manifest.json

**Common Packages:**
- Cinemachine: `com.unity.cinemachine`
- ProBuilder: `com.unity.probuilder`
- TextMeshPro: `com.unity.textmeshpro`
- Addressables: `com.unity.addressables`
- 2D packages: `com.unity.2d.*`

**Git Packages:**
Format: `"package-name": "https://github.com/user/repo.git#version"`

After adding, Unity will resolve dependencies automatically.