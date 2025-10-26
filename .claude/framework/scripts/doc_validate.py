#!/usr/bin/env python3
"""
Documentation Metadata Validator for HaroFramework

This script validates documentation metadata and link integrity:
- Validates required metadata fields
- Checks paired document existence
- Verifies link integrity
- Validates version format
- Checks status values

Usage:
    python doc_validate.py [--verbose] [--strict]

Options:
    --verbose   Show detailed validation progress
    --strict    Treat warnings as errors
"""

import os
import sys
import re
from pathlib import Path
from typing import List, Dict, Optional, Set
from dataclasses import dataclass, field


@dataclass
class ValidationError:
    """Represents a validation error"""
    file_path: Path
    severity: str  # "error" or "warning"
    category: str
    message: str

    def __str__(self):
        symbol = "[X]" if self.severity == "error" else "[!]"
        return (
            f"{symbol} {self.severity.upper()}: {self.category}\n"
            f"    File: {self.file_path.name}\n"
            f"    Issue: {self.message}"
        )


@dataclass
class Document:
    """Represents a documentation file"""
    path: Path
    metadata: Dict
    errors: List[ValidationError] = field(default_factory=list)
    warnings: List[ValidationError] = field(default_factory=list)

    def add_error(self, category: str, message: str):
        """Add an error to this document"""
        error = ValidationError(
            file_path=self.path,
            severity="error",
            category=category,
            message=message
        )
        self.errors.append(error)

    def add_warning(self, category: str, message: str):
        """Add a warning to this document"""
        warning = ValidationError(
            file_path=self.path,
            severity="warning",
            category=category,
            message=message
        )
        self.warnings.append(warning)

    @property
    def has_errors(self) -> bool:
        return len(self.errors) > 0

    @property
    def has_warnings(self) -> bool:
        return len(self.warnings) > 0


class DocumentValidator:
    """Validates documentation metadata and links"""

    REQUIRED_FIELDS = [
        'title', 'version', 'scope', 'created', 'modified',
        'category', 'tags', 'paired_document', 'status'
    ]

    VALID_STATUSES = ['draft', 'review', 'approved', 'deprecated', 'active']

    VERSION_PATTERN = re.compile(r'^\d+\.\d+\.\d+$')  # MAJOR.MINOR.PATCH

    def __init__(self, root_path: Path, verbose: bool = False, strict: bool = False):
        self.root_path = root_path
        self.verbose = verbose
        self.strict = strict
        self.documents: List[Document] = []
        self.all_md_files: Set[Path] = set()

    def log(self, message: str):
        """Print message if verbose mode is enabled"""
        if self.verbose:
            print(f"  {message}")

    def parse_frontmatter(self, content: str) -> Optional[Dict]:
        """Parse YAML frontmatter from markdown content"""
        pattern = r'^---\s*\n(.*?)\n---\s*\n'
        match = re.match(pattern, content, re.DOTALL)

        if not match:
            return None

        yaml_content = match.group(1)
        metadata = {}
        current_key = None
        current_list = None

        for line in yaml_content.split('\n'):
            line = line.rstrip()

            if not line or line.startswith('#'):
                continue

            # List item
            if line.startswith('  - '):
                if current_list is not None:
                    value = line[4:].strip().strip('"').strip("'")
                    current_list.append(value)
                continue

            # Key-value pair
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
        """Load all markdown documents"""
        print("[*] Loading documents...\n")

        claude_dir = self.root_path / '.claude'

        # First pass: collect all .md files
        for md_file in claude_dir.rglob('*.md'):
            self.all_md_files.add(md_file)

        # Second pass: parse documents (skip _KOR.md)
        for md_file in claude_dir.rglob('*.md'):
            # Skip Korean translations
            if md_file.stem.endswith('_KOR'):
                continue

            # Skip commands and skills folders (different metadata structure)
            if 'commands' in md_file.parts or 'skills' in md_file.parts:
                continue

            # Skip certain files
            if md_file.name in ['CLAUDE.md', 'README.md']:
                continue

            self.log(f"Loading {md_file.relative_to(self.root_path)}")

            try:
                content = md_file.read_text(encoding='utf-8')
                metadata = self.parse_frontmatter(content)

                if not metadata:
                    # No frontmatter - create document with error
                    doc = Document(path=md_file, metadata={})
                    doc.add_error(
                        "Missing Frontmatter",
                        "Document has no YAML frontmatter metadata"
                    )
                    self.documents.append(doc)
                    self.log("  [X] No frontmatter")
                    continue

                doc = Document(path=md_file, metadata=metadata)
                self.documents.append(doc)
                self.log(f"  [+] Loaded")

            except Exception as e:
                print(f"  [X] Error loading {md_file.name}: {e}")

        print(f"[+] Loaded {len(self.documents)} documents\n")

    def validate_required_fields(self, doc: Document):
        """Validate that all required fields are present"""
        for field in self.REQUIRED_FIELDS:
            if field not in doc.metadata or not doc.metadata[field]:
                doc.add_error(
                    "Missing Required Field",
                    f"Required field '{field}' is missing or empty"
                )

    def validate_version_format(self, doc: Document):
        """Validate version format (MAJOR.MINOR.PATCH)"""
        version = doc.metadata.get('version', '')

        if not version:
            return  # Already caught by required fields check

        if not self.VERSION_PATTERN.match(version):
            doc.add_error(
                "Invalid Version Format",
                f"Version '{version}' must follow MAJOR.MINOR.PATCH format (e.g., 1.0.0)"
            )

    def validate_status(self, doc: Document):
        """Validate status value"""
        status = doc.metadata.get('status', '')

        if not status:
            return  # Already caught by required fields check

        if status not in self.VALID_STATUSES:
            doc.add_error(
                "Invalid Status",
                f"Status '{status}' must be one of: {', '.join(self.VALID_STATUSES)}"
            )

    def validate_paired_document(self, doc: Document):
        """Validate that paired document exists"""
        paired = doc.metadata.get('paired_document', '')

        if not paired:
            return  # Already caught by required fields check

        # Resolve paired document path
        doc_dir = doc.path.parent
        paired_path = doc_dir / paired

        if not paired_path.exists():
            doc.add_error(
                "Missing Paired Document",
                f"Paired document '{paired}' does not exist"
            )
        else:
            self.log(f"    [+] Paired document exists: {paired}")

    def validate_references(self, doc: Document):
        """Validate that referenced documents exist"""
        references = doc.metadata.get('references', [])

        if isinstance(references, str):
            references = [references]

        if not references:
            return  # No references to check

        doc_dir = doc.path.parent

        for ref in references:
            # Resolve reference path
            if ref.startswith('./'):
                ref_path = doc_dir / ref[2:]
            elif ref.startswith('../'):
                ref_path = doc_dir / ref
            else:
                ref_path = doc_dir / ref

            try:
                ref_path = ref_path.resolve()

                if not ref_path.exists():
                    doc.add_warning(
                        "Broken Reference",
                        f"Referenced file '{ref}' does not exist"
                    )
                else:
                    self.log(f"    [+] Reference exists: {ref}")
            except Exception as e:
                doc.add_warning(
                    "Invalid Reference Path",
                    f"Could not resolve reference '{ref}': {e}"
                )

    def validate_parent_documents(self, doc: Document):
        """Validate that parent documents exist"""
        parents = doc.metadata.get('parent_documents', [])

        if isinstance(parents, str):
            parents = [parents]

        if not parents:
            return  # No parents to check

        doc_dir = doc.path.parent

        for parent in parents:
            # Resolve parent path
            if parent.startswith('./'):
                parent_path = doc_dir / parent[2:]
            elif parent.startswith('../'):
                parent_path = doc_dir / parent
            else:
                parent_path = doc_dir / parent

            try:
                parent_path = parent_path.resolve()

                if not parent_path.exists():
                    doc.add_error(
                        "Missing Parent Document",
                        f"Parent document '{parent}' does not exist"
                    )
                else:
                    self.log(f"    [+] Parent exists: {parent}")
            except Exception as e:
                doc.add_error(
                    "Invalid Parent Path",
                    f"Could not resolve parent '{parent}': {e}"
                )

    def validate_all_documents(self):
        """Run all validation checks"""
        print("[*] Validating documents...\n")

        for doc in self.documents:
            self.log(f"Validating {doc.path.name}...")

            self.validate_required_fields(doc)
            self.validate_version_format(doc)
            self.validate_status(doc)
            self.validate_paired_document(doc)
            self.validate_references(doc)
            self.validate_parent_documents(doc)

            if doc.has_errors:
                self.log(f"  [X] {len(doc.errors)} error(s)")
            if doc.has_warnings:
                self.log(f"  [!] {len(doc.warnings)} warning(s)")
            if not doc.has_errors and not doc.has_warnings:
                self.log(f"  [+] Valid")

        print()  # Empty line

    def report_results(self) -> int:
        """Print validation report and return exit code"""
        total_errors = sum(len(doc.errors) for doc in self.documents)
        total_warnings = sum(len(doc.warnings) for doc in self.documents)

        docs_with_errors = [doc for doc in self.documents if doc.has_errors]
        docs_with_warnings = [doc for doc in self.documents if doc.has_warnings]

        if total_errors == 0 and (total_warnings == 0 or not self.strict):
            print("[+] VALIDATION PASSED")
            print(f"    Validated {len(self.documents)} documents")
            if total_warnings > 0:
                print(f"    {total_warnings} warning(s) found (not treated as errors)")
            return 0

        # Print errors
        if total_errors > 0:
            print(f"[X] VALIDATION FAILED: {total_errors} error(s) found\n")

            for doc in docs_with_errors:
                print(f"File: {doc.path.relative_to(self.root_path)}")
                for error in doc.errors:
                    print(f"  {error}\n")

        # Print warnings
        if total_warnings > 0:
            severity = "ERRORS" if self.strict else "WARNINGS"
            print(f"[!] {total_warnings} {severity.lower()} found\n")

            for doc in docs_with_warnings:
                if doc in docs_with_errors:
                    continue  # Already printed
                print(f"File: {doc.path.relative_to(self.root_path)}")
                for warning in doc.warnings:
                    print(f"  {warning}\n")

        # Summary
        print(f"\nSummary:")
        print(f"  Documents validated: {len(self.documents)}")
        print(f"  Errors: {total_errors}")
        print(f"  Warnings: {total_warnings}")

        if self.strict and total_warnings > 0:
            print(f"\n[X] Strict mode: Treating warnings as errors")
            return 1

        return 1 if total_errors > 0 else 0

    def run(self) -> int:
        """Run validation and return exit code"""
        print("=" * 70)
        print("Documentation Metadata Validator")
        print("=" * 70)
        print()

        self.load_documents()
        self.validate_all_documents()
        return self.report_results()


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description='Validate HaroFramework documentation metadata and links'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Show detailed validation progress'
    )
    parser.add_argument(
        '--strict', '-s',
        action='store_true',
        help='Treat warnings as errors'
    )

    args = parser.parse_args()

    # Find project root
    current_dir = Path.cwd()
    root_path = current_dir

    while not (root_path / '.claude').exists():
        if root_path.parent == root_path:
            print("[X] Error: Could not find .claude directory")
            print("    Run this script from within the HaroFramework project")
            return 1
        root_path = root_path.parent

    # Run validation
    validator = DocumentValidator(root_path, verbose=args.verbose, strict=args.strict)
    return validator.run()


if __name__ == '__main__':
    sys.exit(main())
