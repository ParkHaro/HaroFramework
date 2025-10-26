---
description: Run Unity Test Framework tests
argument-hint: [EditMode|PlayMode|All]
---



<!-- Navigation -->
**🏠 [HaroFramework Project](../MASTER_INDEX.md)** | **📂 [HaroFramework Commands Index](INDEX.md)** | **⬆️ [HaroFramework Commands Index](INDEX.md)**

---
Execute Unity tests and analyze results.

Test mode: $ARGUMENTS (default: All)

**Tasks:**
1. Find all test assemblies (.asmdef files with test references)
2. Locate test scripts in Tests/ directories
3. Report test coverage and results
4. Identify failing tests with stack traces
5. Suggest fixes for common test failures

**Test Types:**
- EditMode: Tests run in editor without play mode
- PlayMode: Tests require play mode execution
- All: Run both test types
