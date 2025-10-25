# HaroFramework Documentation Automation Scripts

Automation scripts for maintaining HaroFramework documentation quality and consistency.

## Available Scripts

### 1. `layer_validate.py` - Layer Dependency Validator

Enforces the 2-layer architecture rule: Framework documents CANNOT reference Game documents.

**Usage:**
```bash
# Basic validation
python layer_validate.py

# With detailed progress
python layer_validate.py --verbose
```

**What it checks:**
- Framework documents don't reference Game layer documents
- References in `references` and `parent_documents` fields

**Exit codes:**
- `0` - All layer dependencies are correct
- `1` - Violations found

---

### 2. `doc_validate.py` - Documentation Metadata Validator

Validates documentation metadata format and link integrity.

**Usage:**
```bash
# Basic validation
python doc_validate.py

# With detailed progress
python doc_validate.py --verbose

# Treat warnings as errors
python doc_validate.py --strict
```

**What it checks:**
- ✅ Required metadata fields (title, version, layer, etc.)
- ✅ Version format (MAJOR.MINOR.PATCH)
- ✅ Valid status values (draft/review/approved/deprecated/active)
- ✅ Paired document existence
- ✅ Reference link integrity
- ✅ Parent document existence

**Exit codes:**
- `0` - All documents valid
- `1` - Errors found (or warnings in strict mode)

---

### 3. `doc_sync.py` - Documentation Synchronization Checker

Detects when original documents are newer than their Korean translations.

**Usage:**
```bash
# Basic check
python doc_sync.py

# With detailed progress
python doc_sync.py --verbose
```

**What it checks:**
- Compares `modified` dates between document pairs
- Identifies translations that need updating

**Exit codes:**
- `0` - All translations in sync
- `1` - Out-of-sync documents found

---

### 4. `version_bump.py` - Version Management

Increments document version numbers and updates modification dates.

**Usage:**
```bash
# Bump patch version (1.0.0 -> 1.0.1)
python version_bump.py framework/doc/architecture/layer-system.md patch

# Bump minor version (1.0.0 -> 1.1.0)
python version_bump.py framework/doc/architecture/layer-system.md minor

# Bump major version (1.0.0 -> 2.0.0)
python version_bump.py framework/doc/architecture/layer-system.md major

# Dry run (show changes without modifying)
python version_bump.py framework/doc/architecture/layer-system.md patch --dry-run
```

**What it does:**
- Increments version number (major/minor/patch)
- Updates `modified` date to today
- Automatically updates paired Korean document

**Version bump rules:**
- **major**: Breaking changes, major restructuring (1.0.0 -> 2.0.0)
- **minor**: New content, significant additions (1.0.0 -> 1.1.0)
- **patch**: Typo fixes, minor clarifications (1.0.0 -> 1.0.1)

---

## Recommended Workflow

### 1. Before Committing Changes

```bash
# Validate layer dependencies
python layer_validate.py

# Validate metadata and links
python doc_validate.py

# Check translation sync
python doc_sync.py
```

All scripts should pass before committing.

### 2. After Updating Documentation

```bash
# Bump version (choose appropriate type)
python version_bump.py framework/doc/architecture/layer-system.md patch

# Validate changes
python doc_validate.py
```

### 3. CI/CD Integration (Future)

Add to pre-commit hook or CI pipeline:
```bash
#!/bin/bash
cd .claude/framework/scripts

python layer_validate.py || exit 1
python doc_validate.py --strict || exit 1
python doc_sync.py || exit 1

echo "[+] All validation checks passed"
```

---

## Script Requirements

- **Python**: 3.7+
- **Dependencies**: None (uses only Python standard library)
- **Platform**: Cross-platform (Windows, macOS, Linux)

---

## File Structure

```
.claude/framework/scripts/
├── README.md              # This file
├── layer_validate.py      # Layer dependency validator
├── doc_validate.py        # Metadata validator
├── doc_sync.py            # Synchronization checker
└── version_bump.py        # Version management
```

---

## Troubleshooting

### "Could not find .claude directory"

**Solution**: Run scripts from within the HaroFramework project directory.

```bash
cd /path/to/HaroFramework
python .claude/framework/scripts/layer_validate.py
```

### "No frontmatter found"

**Solution**: Ensure document has YAML frontmatter:

```markdown
---
title: "Document Title"
version: "1.0.0"
layer: "framework"
created: "2025-10-26"
modified: "2025-10-26"
category: "Architecture"
tags: [tag1, tag2]
paired_document: "document_KOR.md"
parent_documents: []
child_documents: []
references: []
status: "approved"
---

# Document Content
```

### "Invalid version format"

**Solution**: Version must follow `MAJOR.MINOR.PATCH` format:
- ✅ `1.0.0`
- ✅ `2.3.1`
- ❌ `1.0` (missing patch)
- ❌ `v1.0.0` (no 'v' prefix)

---

## Future Enhancements

Planned improvements:
- [ ] Auto-fix mode for common issues
- [ ] CHANGELOG generation from version bumps
- [ ] Automated translation sync tracking
- [ ] GitHub Actions integration
- [ ] Pre-commit hook template
- [ ] Batch version bump for related documents

---

## Related Documentation

- [Documentation Rules](../doc/guidelines/documentation-rules.md) - Documentation standards
- [Layer System](../doc/architecture/layer-system.md) - 2-layer architecture
- [SPEC.md](../project/SPEC.md) - Project specification
- [TODO.md](../project/TODO.md) - Task tracking

---

**Last Updated**: 2025-10-26
**Maintained By**: HaroFramework Team
