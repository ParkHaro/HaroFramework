#!/usr/bin/env python3
"""
Layer Dependency Validator for HaroFramework Documentation

This script enforces the 2-layer architecture rule:
✅ ALLOWED:    Game → Framework (games can use framework)
❌ FORBIDDEN:  Framework → Game (framework CANNOT reference any game)

Usage:
    python layer_validate.py [--fix] [--verbose]

Options:
    --fix       Attempt to auto-fix violations (not implemented yet)
    --verbose   Show detailed validation progress
"""

import os
import sys
import re
import argparse
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass


@dataclass
class Document:
    """Represents a documentation file with metadata"""
    path: Path
    layer: str  # "framework" or "game"
    title: str
    references: List[str]
    parent_documents: List[str]

    def __str__(self):
        return f"{self.layer}/{self.path.relative_to(self.path.parents[4])}"


@dataclass
class Violation:
    """Represents a layer dependency violation"""
    source_doc: Document
    target_path: str
    target_layer: str
    violation_type: str  # "reference" or "parent"

    def __str__(self):
        return (
            f"[X] VIOLATION: {self.source_doc.layer} document references {self.target_layer}\n"
            f"    Source: {self.source_doc.path.name}\n"
            f"    Target: {self.target_path}\n"
            f"    Type: {self.violation_type}"
        )


class LayerValidator:
    """Validates layer dependencies in documentation"""

    def __init__(self, root_path: Path, verbose: bool = False):
        self.root_path = root_path
        self.verbose = verbose
        self.documents: List[Document] = []
        self.violations: List[Violation] = []

    def log(self, message: str):
        """Print message if verbose mode is enabled"""
        if self.verbose:
            print(f"  {message}")

    def parse_frontmatter(self, content: str) -> Optional[Dict]:
        """Parse YAML frontmatter from markdown content"""
        # Match YAML frontmatter between --- delimiters
        pattern = r'^---\s*\n(.*?)\n---\s*\n'
        match = re.match(pattern, content, re.DOTALL)

        if not match:
            return None

        yaml_content = match.group(1)
        metadata = {}

        # Simple YAML parsing (works for our use case)
        current_key = None
        current_list = None

        for line in yaml_content.split('\n'):
            line = line.rstrip()

            if not line or line.startswith('#'):
                continue

            # Check for list item
            if line.startswith('  - '):
                if current_list is not None:
                    value = line[4:].strip().strip('"').strip("'")
                    current_list.append(value)
                continue

            # Check for key-value pair
            if ':' in line and not line.startswith(' '):
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip().strip('"').strip("'")

                if value.startswith('[') and value.endswith(']'):
                    # Inline list
                    metadata[key] = [
                        v.strip().strip('"').strip("'")
                        for v in value[1:-1].split(',') if v.strip()
                    ]
                elif not value:
                    # Empty value, might be a list
                    metadata[key] = []
                    current_key = key
                    current_list = metadata[key]
                else:
                    metadata[key] = value
                    current_list = None

        return metadata

    def load_documents(self):
        """Load all markdown documents and extract metadata"""
        print("[*] Loading documents...")

        # Find all .md files in .claude directory (excluding _KOR.md)
        claude_dir = self.root_path / '.claude'

        for md_file in claude_dir.rglob('*.md'):
            # Skip Korean translations
            if md_file.stem.endswith('_KOR'):
                continue

            # Skip certain files
            if md_file.name in ['CLAUDE.md', 'README.md']:
                continue

            self.log(f"Loading {md_file.relative_to(self.root_path)}")

            try:
                content = md_file.read_text(encoding='utf-8')
                metadata = self.parse_frontmatter(content)

                if not metadata:
                    self.log(f"  [!] No frontmatter found, skipping")
                    continue

                # Determine layer from path or metadata
                layer = metadata.get('layer', 'unknown')

                # Extract references and parent_documents
                references = metadata.get('references', [])
                parent_documents = metadata.get('parent_documents', [])

                # Ensure they are lists
                if isinstance(references, str):
                    references = [references]
                if isinstance(parent_documents, str):
                    parent_documents = [parent_documents]

                doc = Document(
                    path=md_file,
                    layer=layer,
                    title=metadata.get('title', md_file.stem),
                    references=references,
                    parent_documents=parent_documents
                )

                self.documents.append(doc)
                self.log(f"  [+] Loaded: {doc.title} (layer: {layer})")

            except Exception as e:
                print(f"  [X] Error loading {md_file.name}: {e}")

        print(f"[+] Loaded {len(self.documents)} documents\n")

    def determine_layer_from_path(self, ref_path: str, source_doc: Document) -> str:
        """Determine the layer of a referenced document from its path"""
        # Resolve relative path from source document
        source_dir = source_doc.path.parent

        # Normalize path separators
        ref_path = ref_path.replace('\\', '/')

        # Check if path contains layer indicators
        if '/framework/' in ref_path or ref_path.startswith('../'):
            # Try to determine from path structure
            if '/games/' in ref_path:
                return 'game'
            elif '/framework/' in ref_path:
                return 'framework'

        # If we can't determine from path, look for the actual file
        try:
            # Try to resolve the path
            if ref_path.startswith('./'):
                target_path = source_dir / ref_path[2:]
            elif ref_path.startswith('../'):
                target_path = source_dir / ref_path
            else:
                target_path = source_dir / ref_path

            target_path = target_path.resolve()

            # Check if path exists and determine layer
            if target_path.exists():
                path_str = str(target_path)
                if '/games/' in path_str or '\\games\\' in path_str:
                    return 'game'
                elif '/framework/' in path_str or '\\framework\\' in path_str:
                    return 'framework'
        except:
            pass

        # Default: assume same layer if we can't determine
        return source_doc.layer

    def validate_dependencies(self):
        """Validate that Framework documents don't reference Game documents"""
        print("[*] Validating layer dependencies...\n")

        for doc in self.documents:
            if doc.layer != 'framework':
                continue  # Only check framework documents

            self.log(f"Checking {doc.title}...")

            # Check references
            for ref in doc.references:
                target_layer = self.determine_layer_from_path(ref, doc)

                if target_layer == 'game':
                    violation = Violation(
                        source_doc=doc,
                        target_path=ref,
                        target_layer=target_layer,
                        violation_type='reference'
                    )
                    self.violations.append(violation)
                    self.log(f"  [X] Found violation in references: {ref}")

            # Check parent_documents
            for parent in doc.parent_documents:
                target_layer = self.determine_layer_from_path(parent, doc)

                if target_layer == 'game':
                    violation = Violation(
                        source_doc=doc,
                        target_path=parent,
                        target_layer=target_layer,
                        violation_type='parent'
                    )
                    self.violations.append(violation)
                    self.log(f"  [X] Found violation in parent_documents: {parent}")

        print()  # Empty line after validation

    def report_violations(self) -> int:
        """Print validation report and return exit code"""
        if not self.violations:
            print("[+] VALIDATION PASSED")
            print("    All layer dependencies are correct!")
            print("    Framework documents do not reference Game layer.")
            return 0

        print("[X] VALIDATION FAILED")
        print(f"    Found {len(self.violations)} layer dependency violation(s):\n")

        for i, violation in enumerate(self.violations, 1):
            print(f"{i}. {violation}\n")

        print("[*] How to fix:")
        print("    1. Review the violations above")
        print("    2. Remove Game references from Framework documents")
        print("    3. Restructure to make Framework reusable")
        print("    4. Run this script again to verify")

        return 1

    def run(self) -> int:
        """Run the validation and return exit code"""
        print("=" * 70)
        print("Layer Dependency Validator")
        print("=" * 70)
        print()

        self.load_documents()
        self.validate_dependencies()
        return self.report_violations()


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Validate layer dependencies in HaroFramework documentation'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Show detailed validation progress'
    )
    parser.add_argument(
        '--fix',
        action='store_true',
        help='Attempt to auto-fix violations (not implemented)'
    )

    args = parser.parse_args()

    if args.fix:
        print("[X] Auto-fix is not implemented yet")
        return 1

    # Find project root (directory containing .claude folder)
    current_dir = Path.cwd()
    root_path = current_dir

    # Search upwards for .claude directory
    while not (root_path / '.claude').exists():
        if root_path.parent == root_path:
            print("[X] Error: Could not find .claude directory")
            print("    Run this script from within the HaroFramework project")
            return 1
        root_path = root_path.parent

    # Run validation
    validator = LayerValidator(root_path, verbose=args.verbose)
    return validator.run()


if __name__ == '__main__':
    sys.exit(main())
