---
title: Documentation Standards and Rules
version: 1.0.0
scope: framework
created: 2025-10-25
modified: 2025-10-25
category: Guidelines
tags: [documentation, standards, rules, workflow, bilingual]
paired_document: documentation-rules_KOR.md
parent_documents:
  - ../../project/SPEC.md
child_documents: []
references:
  - ./coding-conventions.md
  - ../architecture/scope-system.md
status: approved
---

# Documentation Standards and Rules

## Overview

This document defines comprehensive documentation standards and rules for HaroFramework. All documentation must follow these rules to ensure consistency, maintainability, and accessibility across the project.

**Core Philosophy**: "Clear documentation enables effective development. Bilingual documentation serves global teams. Automation reduces manual effort."

---

## 1. Bilingual Documentation Rule

### 1.1 The Golden Rule

**Every document MUST be duplicated in both English and Korean.**

This is non-negotiable and applies to ALL documentation in the project.

### 1.2 File Naming Convention

**Original Document (English)**:
```
{document-name}.md
```

**Korean Document**:
```
{document-name}_KOR.md
```

### 1.3 Examples

```
SPEC.md                          → Original (English)
SPEC_KOR.md                      → Korean translation

scope-system.md                  → Original (English)
scope-system_KOR.md              → Korean translation

documentation-rules.md           → Original (English)
documentation-rules_KOR.md       → Korean translation
```

### 1.4 Synchronization Requirements

#### Language Rule
- **Original Document**: Written in English
- **Korean Document**: Written 100% in Korean
- No language mixing in either document

#### Content Linkage
Both documents must maintain:
- Identical structure (same headings, sections, subsections)
- Equivalent content (same information, translated)
- Matching examples (code samples stay as-is, comments translated)
- Consistent formatting (same markdown styles)

#### Update Synchronization
When either document is updated:
1. Identify all changes made
2. Apply equivalent changes to paired document
3. Update `modified` date in both documents
4. Verify synchronization with `doc_sync.py`

### 1.5 Creation Workflow

**When creating a new document**:
1. Write original document (English) first
2. Immediately create Korean document
3. Add metadata to both documents
4. Link documents via `paired_document` field
5. Validate with `doc_validate.py`

**Template**:
```markdown
---
title: "Document Title"
version: "1.0.0"
scope: "framework|game"
created: "2025-10-25"
modified: "2025-10-25"
paired_document: "filename_KOR.md"  # or "filename.md"
---

# Document Title

Content here...
```

---

## 2. Metadata Standards

### 2.1 YAML Frontmatter

All documents MUST include YAML frontmatter metadata at the beginning.

### 2.2 Required Fields

```yaml
---
title: "Document Title"
version: "1.0.0"                    # Semantic versioning
scope: "framework|game"             # Scope classification
created: "YYYY-MM-DD"               # Creation date
modified: "YYYY-MM-DD"              # Last modification date
paired_document: "filename_KOR.md"  # Paired document filename
---
```

**Field Descriptions**:

**`title`** (string, required)
- Human-readable document title
- Use title case
- Keep concise (< 60 characters)

**`version`** (string, required)
- Semantic versioning: `MAJOR.MINOR.PATCH`
- Start at `0.1.0` for drafts, `1.0.0` for approved
- See Version Management section for rules

**`scope`** (enum, required)
- Values: `framework` or `game`
- Determines scope boundary validation
- Must match document location

**`created`** (date, required)
- ISO 8601 format: `YYYY-MM-DD`
- Set once when document is created
- Never changed

**`modified`** (date, required)
- ISO 8601 format: `YYYY-MM-DD`
- Updated every time document changes
- Always ≥ created date

**`paired_document`** (string, required)
- Filename of paired translation
- English doc: `filename_KOR.md`
- Korean doc: `filename.md`

### 2.3 Optional Fields

```yaml
category: "Category Name"          # Document category
tags: [tag1, tag2, tag3]           # Searchable tags
status: "draft|review|approved"    # Document status
parent_documents: []               # Parent doc links
child_documents: []                # Child doc links
references: []                     # Referenced docs
author: "Author Name"              # Document author
---
```

**Field Descriptions**:

**`category`** (string, optional)
- Broad classification
- Examples: "Guidelines", "Architecture", "API"

**`tags`** (array, optional)
- Keywords for searching and filtering
- Use lowercase with hyphens: `documentation-standards`

**`status`** (enum, optional)
- `draft`: Work in progress
- `review`: Ready for review
- `approved`: Reviewed and approved
- `deprecated`: No longer valid

**`parent_documents`** (array, optional)
- Relative paths to parent documents
- Example: `["../../project/SPEC.md"]`

**`child_documents`** (array, optional)
- Relative paths to child documents
- Example: `["systems/player.md"]`

**`references`** (array, optional)
- Relative paths to referenced documents
- Must respect scope boundaries

**`author`** (string, optional)
- Document creator or maintainer
- Optional for team-maintained docs

### 2.4 Example: Complete Metadata

```yaml
---
title: "Player System Documentation"
version: "1.2.0"
scope: "framework"
created: "2025-10-20"
modified: "2025-10-25"
category: "Systems"
tags: [player, movement, input, core-system]
paired_document: "player_KOR.md"
parent_documents:
  - "../project-overview.md"
child_documents:
  - "player/movement.md"
  - "player/input.md"
references:
  - "../core/input-system.md"
  - "../architecture/scope-system.md"
status: "approved"
author: "Framework Team"
---
```

---

## 3. Version Management

### 3.1 Semantic Versioning

Format: `MAJOR.MINOR.PATCH`

### 3.2 Version Increment Rules

**MAJOR** (X.0.0) - Increment when:
- Document structure is significantly reorganized
- Breaking changes to documented interfaces or APIs
- Fundamental changes that invalidate previous understanding
- Backward compatibility is broken
- Major sections removed or completely rewritten

**Examples**:
- Restructuring entire document organization
- Changing core concepts or principles
- API breaking changes in documented code

**MINOR** (x.Y.0) - Increment when:
- New sections or chapters added
- Content expanded with new information
- New features or systems documented
- Backward-compatible additions
- Additional examples or clarifications

**Examples**:
- Adding new subsection to existing section
- Documenting new feature
- Adding FAQ section
- Expanding existing content

**PATCH** (x.y.Z) - Increment when:
- Typos or grammar errors fixed
- Examples improved or clarified
- Minor wording improvements
- Formatting corrections
- Link fixes
- Metadata updates (except version)

**Examples**:
- Fixing spelling mistakes
- Improving code example clarity
- Correcting broken links
- Adjusting formatting

### 3.3 Version Update Process

1. **Determine Change Type**
   - Review all changes made
   - Classify as MAJOR, MINOR, or PATCH
   - When in doubt, choose higher level

2. **Update Metadata**
   ```yaml
   version: "1.2.0"  # Old version
   version: "1.3.0"  # New version (MINOR update)
   modified: "2025-10-25"  # Update date
   ```

3. **Update Paired Document**
   - Apply same version to paired document
   - Ensure both have matching versions
   - Update both `modified` dates

4. **Document Changes** (optional but recommended)
   - Add changelog entry
   - Note significant changes at top of document
   - Reference related issues or PRs

### 3.4 Automated Version Management

Use `version_bump.py` script:

```bash
# Increment MAJOR version
python .claude/scripts/version_bump.py {document}.md major

# Increment MINOR version
python .claude/scripts/version_bump.py {document}.md minor

# Increment PATCH version
python .claude/scripts/version_bump.py {document}.md patch
```

Script automatically:
- Increments version number
- Updates `modified` date
- Updates paired document
- Generates changelog entry (if configured)

---

## 4. Document Workflow Rules

### 4.1 Reading Optimization (Token Efficiency)

**Rule**: Claude Code reads ONLY original documents (`*.md`), NOT Korean documents (`*_KOR.md`)

**Rationale**:
- Reduces token usage by approximately 50%
- Original English documents contain all necessary information
- Korean documents are for human readers who prefer Korean
- Avoids redundant processing of identical content

**Implementation**:
- Document reading tools exclude `*_KOR.md` files
- Search operations skip Korean documents
- Analysis focuses on original documents only

**When Korean Documents Are Read**:
- Manual user request
- Translation verification
- Synchronization checks

### 4.2 Writing and Creating Documents

**Standard Workflow**:

1. **Plan**
   - Determine document purpose and audience
   - Identify appropriate folder location
   - Check if similar documents exist

2. **Create Original Document**
   - Write content in English
   - Add complete metadata
   - Follow markdown formatting standards
   - Include code examples if applicable

3. **Create Korean Document**
   - Translate content to Korean
   - Maintain identical structure
   - Keep code examples as-is (translate comments)
   - Add complete metadata

4. **Link Documents**
   - Set `paired_document` in metadata
   - Add parent/child relationships
   - Add references to related documents

5. **Validate**
   - Run `doc_validate.py`
   - Check for broken links
   - Verify metadata completeness

### 4.3 Updating Documents

**Standard Workflow**:

1. **Edit Original Document**
   - Make changes to `*.md` file
   - Update `modified` date
   - Increment `version` appropriately

2. **Sync Korean Document**
   - Apply equivalent changes to `*_KOR.md`
   - Match `modified` date
   - Match `version` number

3. **Validate**
   - Run `doc_sync.py --check`
   - Run `doc_validate.py`
   - Verify synchronization

### 4.4 Deleting Documents

**Standard Workflow**:

1. **Mark as Deprecated**
   - Update status to `deprecated`
   - Add deprecation notice at top
   - Specify replacement document if applicable

2. **Wait Period**
   - Keep deprecated docs for transition period
   - Allow users to migrate to new docs

3. **Delete Both Documents**
   - Delete original document
   - Delete Korean document
   - Update all references in other documents
   - Run `doc_validate.py` to check for broken links

---

## 5. Context Management Protocol

### 5.1 The 85% Rule

**Rule**: When context usage reaches 85%, write SPEC/TODO and execute `/clear`

**Purpose**:
- Prevent context overflow
- Ensure continuity across sessions
- Maintain working memory for Claude

### 5.2 Context Monitoring

**Continuous Monitoring**:
- Track token usage during all operations
- Calculate percentage used (tokens_used / tokens_total)
- Alert at threshold levels

**Thresholds**:
- 🟢 **0-60%**: Normal operation
- 🟡 **60-75%**: Begin planning wrap-up
- 🟠 **75-85%**: Prepare SPEC/TODO update
- 🔴 **85%+**: Mandatory SPEC/TODO update and `/clear`

### 5.3 Session Wrap-Up Process

**When reaching 85% context**:

1. **Update SPEC.md**
   - Document current progress
   - Note any decisions made
   - List completed tasks
   - Update relevant sections

2. **Update TODO.md**
   - Mark completed tasks
   - Add newly discovered tasks
   - Update priority and estimates
   - Add session restoration notes

3. **Sync Korean Documents**
   - Update SPEC_KOR.md
   - Update TODO_KOR.md

4. **Create Session Restoration Guide**
   ```markdown
   ## Session Restoration
   - **Last Session**: 2025-10-25
   - **Context Used**: 170K/200K (85%)
   - **Completed**: [task list]
   - **Next Steps**: [next task list]
   - **Important Context**: [key information to remember]
   ```

5. **Execute `/clear`**

### 5.4 Session Restoration

**Starting New Session**:

1. **Read SPEC** (original document only)
2. **Read TODO** (original document only)
3. **Review Session Restoration Guide**
4. **Continue from last checkpoint**

---

## 6. Folder Structure Management

### 6.1 Folder Organization Principles

**Before Creating Documents**:
- Analyze document purpose and category
- Propose logical folder location to user
- Wait for approval before creating folders
- Document folder structure decisions

**Folder Naming**:
- Use lowercase with hyphens: `folder-name`
- Keep names short but descriptive
- Group related documents together
- Separate by scope (framework vs game)

### 6.2 Framework Documentation Structure

```
.claude/framework/
├── doc/
│   ├── guidelines/              # Development guidelines
│   │   ├── documentation-rules.md
│   │   ├── documentation-rules_KOR.md
│   │   ├── coding-conventions.md
│   │   └── coding-conventions_KOR.md
│   │
│   ├── architecture/            # Architecture docs
│   │   ├── project-overview.md
│   │   ├── project-overview_KOR.md
│   │   ├── scope-system.md
│   │   └── scope-system_KOR.md
│   │
│   ├── systems/                 # System-specific docs
│   │   ├── player/
│   │   ├── ai/
│   │   ├── ui/
│   │   └── audio/
│   │
│   ├── api/                     # API reference
│   │
│   └── workflow/                # Development workflow
│       ├── development-workflow.md
│       └── development-workflow_KOR.md
│
├── project/                     # Project management
│   ├── SPEC.md
│   ├── SPEC_KOR.md
│   ├── TODO.md
│   └── TODO_KOR.md
│
└── scripts/                     # Framework scripts
    └── README.md
```

### 6.3 Game Documentation Structure

```
.claude/games/
├── _template/                   # Game project template
│   ├── doc/
│   │   ├── design/              # Game design docs
│   │   ├── mechanics/           # Gameplay mechanics
│   │   ├── levels/              # Level documentation
│   │   └── assets/              # Asset documentation
│   │
│   ├── project/
│   │   ├── SPEC.md
│   │   ├── SPEC_KOR.md
│   │   ├── TODO.md
│   │   └── TODO_KOR.md
│   │
│   └── GAME.md                  # Game Claude config
│
└── [game-name]/                 # Actual game projects
    └── (same structure as template)
```

---

## 7. Document Linking System

### 7.1 Link Types

**Parent-Child Links**:
- Hierarchical relationship
- Parent provides overview, children provide details
- Used in metadata fields

**References**:
- Cross-references to related documents
- Not hierarchical, but related content
- Used in metadata and document body

**See Also**:
- Additional context or related topics
- Typically at end of document
- Less critical than references

### 7.2 Metadata Linking

```yaml
parent_documents:
  - "../SPEC.md"                   # Relative path to parent

child_documents:
  - "systems/player.md"            # Relative paths to children
  - "systems/ai.md"

references:
  - "../coding-conventions.md"     # Related documents
  - "scope-system.md"
```

### 7.3 In-Document Linking

**Relative Links**:
```markdown
See [Scope System](../architecture/scope-system.md) for details.
```

**Anchor Links** (same document):
```markdown
See [Metadata Standards](#metadata-standards) section above.
```

**External Links**:
```markdown
[Unity Documentation](https://docs.unity3d.com/)
```

### 7.4 Scope-Aware Linking

**Rule**: Respect scope boundaries in document links

**Framework Documents**:
```yaml
# ✅ ALLOWED
references:
  - "./other-framework-doc.md"
  - "../guidelines/coding-conventions.md"

# ❌ FORBIDDEN
references:
  - "../../games/game1/design.md"  # Cannot reference game scope
```

**Game Documents**:
```yaml
# ✅ ALLOWED
references:
  - "./game-design.md"                         # Within game
  - "../../framework/systems/player.md"        # Framework reference

# ✅ ALLOWED (but be careful)
references:
  - "../other-game/shared-pattern.md"  # Between games (rare case)
```

### 7.5 Link Validation

Use `doc_validate.py` to verify:
- All links are valid and reachable
- No broken links exist
- Scope boundaries are respected
- Bidirectional links are consistent

```bash
python .claude/scripts/doc_validate.py
```

---

## 8. Automation Scripts

### 8.1 doc_sync.py - Document Synchronization

**Purpose**: Detect and manage synchronization between original and Korean documents.

**Features**:
- Detect changes in either document
- Compare content and structure
- Notify when synchronization needed
- Support manual sync workflow

**Usage**:
```bash
# Check synchronization status
python .claude/scripts/doc_sync.py --check

# Check specific document
python .claude/scripts/doc_sync.py --check SPEC.md

# Interactive sync mode
python .claude/scripts/doc_sync.py --sync

# List out-of-sync documents
python .claude/scripts/doc_sync.py --list
```

**Output Example**:
```
Checking document synchronization...

✅ SPEC.md ↔ SPEC_KOR.md
   Versions match: 1.0.0
   Modified dates match: 2025-10-25

⚠️  TODO.md ↔ TODO_KOR.md
   Version mismatch: 1.1.0 vs 1.0.0
   Modified dates differ: 2025-10-25 vs 2025-10-24
   → Korean document needs update

Summary: 2 document pairs checked
         1 synchronized
         1 needs attention
```

### 8.2 doc_validate.py - Document Validation

**Purpose**: Validate document integrity, metadata, and links.

**Checks**:
- Metadata format and required fields
- Paired document existence
- Link integrity (broken links)
- Version consistency between pairs
- Status field validity
- Scope boundary violations

**Usage**:
```bash
# Validate all documents
python .claude/scripts/doc_validate.py

# Validate specific document
python .claude/scripts/doc_validate.py SPEC.md

# Validate specific folder
python .claude/scripts/doc_validate.py --folder .claude/framework/doc/

# Check only metadata
python .claude/scripts/doc_validate.py --metadata-only

# Check only links
python .claude/scripts/doc_validate.py --links-only
```

**Output Example**:
```
Validating documents...

✅ SPEC.md
   Metadata: Valid
   Paired document: Found (SPEC_KOR.md)
   Links: 5 checked, all valid
   Scope: framework

❌ old-document.md
   Error: Missing 'version' in metadata
   Warning: Paired document not found
   Error: Broken link: ../deleted-doc.md

Summary: 10 documents validated
         9 passed
         1 failed
```

### 8.3 scope_validate.py - Scope Dependency Validation

**Purpose**: Enforce scope dependency rules (Framework → Game forbidden).

**Algorithm**:
```python
def validate_layer_dependency(doc_path):
    # Extract document scope
    scope = get_document_layer(doc_path)

    # Extract all references
    references = extract_all_references(doc_path)

    for ref in references:
        ref_layer = get_document_layer(ref)

        # Enforce rule: framework cannot reference game
        if scope == "framework" and ref_layer == "game":
            raise DependencyViolationError(
                f"FORBIDDEN: Framework document '{doc_path}' "
                f"cannot reference Game document '{ref}'"
            )

    return True
```

**Usage**:
```bash
# Validate all documents
python .claude/scripts/scope_validate.py

# Validate specific document
python .claude/scripts/scope_validate.py scope-system.md

# Validate framework scope only
python .claude/scripts/scope_validate.py --scope framework

# Validate game scope only
python .claude/scripts/scope_validate.py --scope game
```

**Output Example**:
```
Validating scope dependencies...

✅ scope-system.md (framework)
   References: 3 checked, all valid scopes

❌ bad-framework-doc.md (framework)
   Error: References game document '../../games/mygame/design.md'
   Line 45: [See Game Design](../../games/mygame/design.md)

   VIOLATION: Framework scope cannot reference Game scope

Summary: 15 documents validated
         14 passed
         1 violation found
```

### 8.4 version_bump.py - Version Management

**Purpose**: Automate version updates for documents.

**Features**:
- Increment version (major/minor/patch)
- Update `modified` date automatically
- Update paired document version
- Generate changelog entry (optional)
- Batch version updates

**Usage**:
```bash
# Increment patch version
python .claude/scripts/version_bump.py SPEC.md patch

# Increment minor version
python .claude/scripts/version_bump.py SPEC.md minor

# Increment major version
python .claude/scripts/version_bump.py SPEC.md major

# Update with custom message
python .claude/scripts/version_bump.py SPEC.md minor --message "Added new section"

# Batch update multiple documents
python .claude/scripts/version_bump.py *.md patch
```

**Output Example**:
```
Bumping version for SPEC.md...

Current version: 1.0.0
New version: 1.1.0 (minor)

Updated SPEC.md:
  version: 1.0.0 → 1.1.0
  modified: 2025-10-24 → 2025-10-25

Updated SPEC_KOR.md:
  version: 1.0.0 → 1.1.0
  modified: 2025-10-24 → 2025-10-25

✅ Version bump completed successfully
```

---

## 9. Script-First Approach

### 9.1 When to Propose Scripts

**Claude should propose script creation when**:
- Task is repetitive (will be done multiple times)
- Manual process is error-prone
- Task involves multiple files or complex logic
- Automation would save significant time
- Consistency is critical

**Examples**:
- Document synchronization checking
- Batch metadata updates
- Link validation across project
- Version bumping multiple documents
- Documentation report generation

### 9.2 Script Proposal Template

**When proposing a script**:
```markdown
I notice we're doing [task] repeatedly. I recommend creating a script to automate this.

**Script Purpose**: [What it will do]
**Benefits**:
- [Benefit 1]
- [Benefit 2]

**Usage Example**:
```bash
python .claude/scripts/proposed_script.py [args]
```

**Estimated Development Time**: [time estimate]

Should I proceed with creating this script?
```

### 9.3 Script Documentation

**All scripts MUST have**:
- Docstring explaining purpose
- Usage examples in comments
- Help text (`--help` flag)
- Error handling with clear messages
- Logging for debugging

**Example Script Structure**:
```python
"""
doc_sync.py - Document Synchronization Tool

Purpose: Check and manage synchronization between original and Korean documents.

Usage:
    python doc_sync.py --check              # Check all documents
    python doc_sync.py --check SPEC.md      # Check specific document
    python doc_sync.py --sync               # Interactive sync mode

Author: HaroFramework Team
"""

import argparse
import logging

def main():
    parser = argparse.ArgumentParser(description="Document sync tool")
    # ... argument parsing

if __name__ == "__main__":
    main()
```

---

## 10. Quality Standards

### 10.1 Completeness

**All documents must have**:
- Complete metadata (all required fields)
- Clear introduction explaining purpose
- Well-organized sections with headings
- Examples where appropriate
- Related documentation links
- Paired translation document

### 10.2 Accuracy

**Documents must be**:
- Technically correct
- Up-to-date with current implementation
- Consistent with related documents
- Free of outdated information

### 10.3 Clarity

**Writing should be**:
- Clear and concise
- Well-structured
- Easy to understand
- Appropriate for target audience
- Free of jargon (or jargon explained)

### 10.4 Consistency

**Documentation must maintain**:
- Consistent terminology throughout
- Consistent formatting (markdown style)
- Consistent structure (similar docs use similar organization)
- Consistent metadata format

---

## 11. Templates

### 11.1 Document Template

```markdown
---
title: "[Document Title]"
version: "0.1.0"
scope: "framework|game"
created: "YYYY-MM-DD"
modified: "YYYY-MM-DD"
category: "[Category]"
tags: [tag1, tag2]
paired_document: "[filename_KOR.md]"
parent_documents: []
child_documents: []
references: []
status: "draft"
---

# [Document Title]

## Overview

[Brief description of what this document covers]

## [Main Section 1]

[Content]

## [Main Section 2]

[Content]

## Related Documentation

- [Related Doc 1](path/to/doc1.md)
- [Related Doc 2](path/to/doc2.md)

---

**Document Status**: Draft
**Version**: 0.1.0
**Last Updated**: YYYY-MM-DD
```

### 11.2 Metadata Template

```yaml
---
title: ""
version: "0.1.0"
scope: ""
created: "YYYY-MM-DD"
modified: "YYYY-MM-DD"
category: ""
tags: []
paired_document: ""
parent_documents: []
child_documents: []
references: []
status: "draft"
---
```

---

## 12. Best Practices

### 12.1 Documentation Workflow

1. **Plan before writing**
2. **Write original first**
3. **Create translation immediately**
4. **Link related documents**
5. **Validate before committing**

### 12.2 Maintenance

- Review documentation regularly
- Update when code changes
- Remove outdated information
- Keep versions synchronized
- Check links periodically

### 12.3 Collaboration

- One person updates both language versions
- Review both versions together
- Use version control for tracking changes
- Document significant decisions

---

## Related Documentation

- [SPEC.md](../../project/SPEC.md) - Complete project specification
- [scope-system.md](../architecture/scope-system.md) - Scope architecture
- [coding-conventions.md](./coding-conventions.md) - Code standards

---

**Document Status**: Approved
**Version**: 1.0.0
**Last Updated**: 2025-10-25
