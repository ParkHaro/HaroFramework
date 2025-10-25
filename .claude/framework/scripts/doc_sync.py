#!/usr/bin/env python3
"""
Documentation Synchronization Checker for HaroFramework

Detects when original documents have been modified more recently than
their Korean translations, indicating translation sync is needed.

Usage:
    python doc_sync.py [--verbose]

Options:
    --verbose   Show all document pairs checked
"""

import sys
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Optional


class DocumentSyncChecker:
    """Check synchronization between original and translated documents"""

    def __init__(self, root_path: Path, verbose: bool = False):
        self.root_path = root_path
        self.verbose = verbose
        self.out_of_sync_docs: List[Tuple[Path, Path, str, str]] = []

    def log(self, message: str):
        if self.verbose:
            print(f"  {message}")

    def parse_frontmatter(self, content: str) -> Optional[Dict]:
        """Parse YAML frontmatter"""
        pattern = r'^---\s*\n(.*?)\n---\s*\n'
        match = re.match(pattern, content, re.DOTALL)

        if not match:
            return None

        yaml_content = match.group(1)
        metadata = {}

        for line in yaml_content.split('\n'):
            if ':' in line and not line.startswith(' '):
                key, value = line.split(':', 1)
                metadata[key.strip()] = value.strip().strip('"').strip("'")

        return metadata

    def get_modified_date(self, file_path: Path) -> Optional[str]:
        """Get modified date from document frontmatter"""
        try:
            content = file_path.read_text(encoding='utf-8')
            metadata = self.parse_frontmatter(content)
            return metadata.get('modified') if metadata else None
        except Exception as e:
            print(f"[X] Error reading {file_path.name}: {e}")
            return None

    def check_sync(self):
        """Check all document pairs for synchronization"""
        print("[*] Checking document synchronization...\n")

        claude_dir = self.root_path / '.claude'

        # Find all original documents (non-_KOR.md)
        for md_file in claude_dir.rglob('*.md'):
            # Skip Korean translations
            if md_file.stem.endswith('_KOR'):
                continue

            # Skip certain files
            if md_file.name in ['CLAUDE.md', 'README.md']:
                continue

            # Check if this file has metadata with paired_document
            try:
                content = md_file.read_text(encoding='utf-8')
                metadata = self.parse_frontmatter(content)

                if not metadata or 'paired_document' not in metadata:
                    continue

                paired_name = metadata.get('paired_document', '')
                if not paired_name:
                    continue

                # Get paired document path
                paired_path = md_file.parent / paired_name

                if not paired_path.exists():
                    self.log(f"[!] Paired document not found: {paired_name}")
                    continue

                # Get modified dates
                orig_modified = metadata.get('modified', '')
                paired_modified = self.get_modified_date(paired_path)

                if not orig_modified or not paired_modified:
                    continue

                # Compare dates
                self.log(f"Checking {md_file.name} vs {paired_name}")
                self.log(f"  Original: {orig_modified}")
                self.log(f"  Paired:   {paired_modified}")

                if orig_modified > paired_modified:
                    self.out_of_sync_docs.append((
                        md_file,
                        paired_path,
                        orig_modified,
                        paired_modified
                    ))
                    self.log(f"  [!] OUT OF SYNC")
                else:
                    self.log(f"  [+] In sync")

            except Exception as e:
                print(f"[X] Error checking {md_file.name}: {e}")

        print()  # Empty line

    def report(self) -> int:
        """Print report and return exit code"""
        if not self.out_of_sync_docs:
            print("[+] ALL DOCUMENTS IN SYNC")
            print("    All translations are up to date with originals")
            return 0

        print(f"[!] {len(self.out_of_sync_docs)} document pair(s) out of sync:\n")

        for orig_path, paired_path, orig_mod, paired_mod in self.out_of_sync_docs:
            print(f"Original: {orig_path.relative_to(self.root_path)}")
            print(f"  Modified: {orig_mod}")
            print(f"Korean:   {paired_path.relative_to(self.root_path)}")
            print(f"  Modified: {paired_mod}")
            print(f"  [!] Translation needs update\n")

        print("[*] Action needed:")
        print("    1. Review original document changes")
        print("    2. Update Korean translation")
        print("    3. Update 'modified' date in Korean document")
        print("    4. Run this script again to verify")

        return 1

    def run(self) -> int:
        """Run synchronization check"""
        print("=" * 70)
        print("Documentation Synchronization Checker")
        print("=" * 70)
        print()

        self.check_sync()
        return self.report()


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description='Check HaroFramework documentation synchronization'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Show all document pairs checked'
    )

    args = parser.parse_args()

    # Find project root
    current_dir = Path.cwd()
    root_path = current_dir

    while not (root_path / '.claude').exists():
        if root_path.parent == root_path:
            print("[X] Error: Could not find .claude directory")
            return 1
        root_path = root_path.parent

    # Run check
    checker = DocumentSyncChecker(root_path, verbose=args.verbose)
    return checker.run()


if __name__ == '__main__':
    sys.exit(main())
