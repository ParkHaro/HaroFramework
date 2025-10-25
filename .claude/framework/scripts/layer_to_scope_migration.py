#!/usr/bin/env python3
"""
Layer to Scope Migration Script

This script migrates all documentation from "Layer" terminology to "Scope" terminology.
Updates both English and Korean documents.
"""

import re
from pathlib import Path
from typing import List, Tuple

def replace_layer_with_scope(content: str) -> str:
    """Replace all layer-related terms with scope equivalents"""
    replacements = [
        # Metadata fields
        (r'\blayer:', 'scope:'),
        # File names in paths
        (r'layer-system', 'scope-system'),
        (r'layer_validate\.py', 'scope_validate.py'),
        # English terms
        (r'\bLayer\b', 'Scope'),
        (r'\blayer\b', 'scope'),
        (r'\bLayers\b', 'Scopes'),
        (r'\blayers\b', 'scopes'),
        # Korean terms
        (r'레이어', '스코프'),
    ]

    result = content
    for pattern, replacement in replacements:
        result = re.sub(pattern, replacement, result)

    return result

def process_file(file_path: Path) -> bool:
    """Process a single file and return True if modified"""
    try:
        print(f"Processing: {file_path.relative_to(file_path.parents[4])}")

        # Read original content
        content = file_path.read_text(encoding='utf-8')
        original_content = content

        # Skip if this is the migration script itself
        if 'layer_to_scope_migration.py' in file_path.name:
            print(f"  [Skip] Migration script itself")
            return False

        # Skip if already migrated (check for scope-system.md reference)
        if 'scope-system.md' in content and 'layer-system.md' not in content:
            print(f"  [Skip] Already migrated")
            return False

        # Apply replacements
        new_content = replace_layer_with_scope(content)

        # Check if content changed
        if new_content == original_content:
            print(f"  [Skip] No changes needed")
            return False

        # Write updated content
        file_path.write_text(new_content, encoding='utf-8')
        print(f"  [✓] Updated")
        return True

    except Exception as e:
        print(f"  [X] Error: {e}")
        return False

def main():
    """Main migration process"""
    print("=" * 70)
    print("Layer → Scope Migration")
    print("=" * 70)
    print()

    # Find project root
    current_dir = Path(__file__).resolve()
    root_path = current_dir.parents[4]  # Go up to project root

    print(f"Project root: {root_path}")
    print()

    # Find all markdown files
    claude_dir = root_path / '.claude'

    files_to_process = []
    for md_file in claude_dir.rglob('*.md'):
        # Skip files we've already created
        if 'scope-system' in md_file.name:
            continue
        # Skip layer-system files (will be deleted later)
        if 'layer-system' in md_file.name:
            continue
        files_to_process.append(md_file)

    # Also process root CLAUDE.md (already done but for consistency)
    claude_md = root_path / 'CLAUDE.md'
    if claude_md.exists():
        files_to_process.append(claude_md)

    print(f"Found {len(files_to_process)} files to process")
    print()

    # Process all files
    modified_count = 0
    for file_path in sorted(files_to_process):
        if process_file(file_path):
            modified_count += 1

    print()
    print("=" * 70)
    print(f"Migration complete: {modified_count}/{len(files_to_process)} files updated")
    print("=" * 70)
    print()
    print("Next steps:")
    print("1. Review changes with: git diff")
    print("2. Delete old files: layer-system.md, layer-system_KOR.md, layer_validate.py")
    print("3. Test validation: python .claude/framework/scripts/scope_validate.py")

if __name__ == '__main__':
    main()
