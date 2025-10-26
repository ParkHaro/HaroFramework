---
description: Create Assembly Definition file
argument-hint: <AssemblyName> [Runtime|Editor|Tests]
---



<!-- Navigation -->
**🏠 [HaroFramework Project](../MASTER_INDEX.md)** | **📂 [HaroFramework Commands Index](INDEX.md)** | **⬆️ [HaroFramework Commands Index](INDEX.md)**

---
Create an Assembly Definition (.asmdef) file to organize code and improve compilation times.

Assembly name: $1
Type: $2 (default: Runtime)

**Benefits:**
- Faster compilation (only changed assemblies recompile)
- Clear dependency boundaries
- Required for Unity packages
- Better code organization

**Recommended Structure:**
```
Assets/HaroFramework/
  Runtime/
    HaroFramework.Runtime.asmdef
  Editor/
    HaroFramework.Editor.asmdef
  Tests/
    Runtime/
      HaroFramework.Tests.asmdef
    Editor/
      HaroFramework.Editor.Tests.asmdef
```

**Generate .asmdef JSON:**
```json
{
    "name": "$1",
    "rootNamespace": "$1",
    "references": [],
    "includePlatforms": [],
    "excludePlatforms": [],
    "allowUnsafeCode": false,
    "overrideReferences": false,
    "autoReferenced": true,
    "defineConstraints": [],
    "versionDefines": [],
    "noEngineReferences": false
}
```

Adjust platform settings and references based on assembly type.
