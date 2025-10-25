#!/usr/bin/env python3
"""
Documentation Version Management for HaroFramework

Increments document version numbers and updates modification dates.

Usage:
    python version_bump.py <file> <major|minor|patch> [--dry-run]

Arguments:
    file        Path to document file (e.g., doc/architecture/layer-system.md)
    bump_type   Type of version bump: major, minor, or patch

Options:
    --dry-run   Show what would be changed without modifying files

Examples:
    python version_bump.py doc/architecture/layer-system.md patch
    python version_bump.py doc/architecture/layer-system.md minor --dry-run
"""

import sys
import re
from pathlib import Path
from datetime import datetime
from typing import Optional, Tuple


class VersionBumper:
    """Manages document version numbers"""

    def __init__(self, root_path: Path, dry_run: bool = False):
        self.root_path = root_path
        self.dry_run = dry_run

    def parse_version(self, version_str: str) -> Optional[Tuple[int, int, int]]:
        """Parse version string to (major, minor, patch)"""
        pattern = r'^(\d+)\.(\d+)\.(\d+)$'
        match = re.match(pattern, version_str)

        if not match:
            return None

        return (int(match.group(1)), int(match.group(2)), int(match.group(3)))

    def bump_version(self, version: Tuple[int, int, int], bump_type: str) -> Tuple[int, int, int]:
        """Bump version number"""
        major, minor, patch = version

        if bump_type == 'major':
            return (major + 1, 0, 0)
        elif bump_type == 'minor':
            return (major, minor + 1, 0)
        elif bump_type == 'patch':
            return (major, minor, patch + 1)
        else:
            raise ValueError(f"Invalid bump type: {bump_type}")

    def format_version(self, version: Tuple[int, int, int]) -> str:
        """Format version tuple as string"""
        return f"{version[0]}.{version[1]}.{version[2]}"

    def get_today_date(self) -> str:
        """Get today's date in YYYY-MM-DD format"""
        return datetime.now().strftime('%Y-%m-%d')

    def update_document(self, file_path: Path, bump_type: str) -> bool:
        """Update document version and modification date"""
        if not file_path.exists():
            print(f"[X] File not found: {file_path}")
            return False

        try:
            # Read content
            content = file_path.read_text(encoding='utf-8')

            # Extract frontmatter
            pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
            match = re.match(pattern, content, re.DOTALL)

            if not match:
                print(f"[X] No frontmatter found in {file_path.name}")
                return False

            frontmatter = match.group(1)
            body = match.group(2)

            # Parse current version
            version_match = re.search(r'^version:\s*["\']?([^"\'\n]+)["\']?', frontmatter, re.MULTILINE)
            if not version_match:
                print(f"[X] No version field found in {file_path.name}")
                return False

            current_version_str = version_match.group(1)
            current_version = self.parse_version(current_version_str)

            if not current_version:
                print(f"[X] Invalid version format: {current_version_str}")
                return False

            # Bump version
            new_version = self.bump_version(current_version, bump_type)
            new_version_str = self.format_version(new_version)

            # Get today's date
            today = self.get_today_date()

            # Update frontmatter
            new_frontmatter = re.sub(
                r'^version:\s*["\']?[^"\'\n]+["\']?',
                f'version: "{new_version_str}"',
                frontmatter,
                flags=re.MULTILINE
            )

            new_frontmatter = re.sub(
                r'^modified:\s*["\']?[^"\'\n]+["\']?',
                f'modified: "{today}"',
                new_frontmatter,
                flags=re.MULTILINE
            )

            # Reconstruct content
            new_content = f"---\n{new_frontmatter}\n---\n{body}"

            # Print changes
            print(f"\nFile: {file_path.relative_to(self.root_path)}")
            print(f"  Version: {current_version_str} -> {new_version_str}")
            print(f"  Modified: (updated to {today})")

            if self.dry_run:
                print(f"  [DRY RUN] No changes made")
                return True

            # Write updated content
            file_path.write_text(new_content, encoding='utf-8')
            print(f"  [+] Updated successfully")

            # Check for paired document
            paired_pattern = r'^paired_document:\s*["\']?([^"\'\n]+)["\']?'
            paired_match = re.search(paired_pattern, frontmatter, re.MULTILINE)

            if paired_match:
                paired_name = paired_match.group(1)
                paired_path = file_path.parent / paired_name

                if paired_path.exists():
                    print(f"\n[*] Updating paired document: {paired_name}")
                    self.update_document(paired_path, bump_type)

            return True

        except Exception as e:
            print(f"[X] Error updating {file_path.name}: {e}")
            return False

    def run(self, file_path: str, bump_type: str) -> int:
        """Run version bump"""
        print("=" * 70)
        print("Documentation Version Bumper")
        print("=" * 70)

        # Resolve file path
        path = Path(file_path)

        if not path.is_absolute():
            # Try relative to root
            path = self.root_path / path

        if not path.exists():
            # Try relative to .claude directory
            path = self.root_path / '.claude' / file_path

        if not path.exists():
            print(f"\n[X] File not found: {file_path}")
            print(f"    Searched:")
            print(f"      - {Path(file_path).absolute()}")
            print(f"      - {self.root_path / file_path}")
            print(f"      - {self.root_path / '.claude' / file_path}")
            return 1

        # Update document
        success = self.update_document(path, bump_type)

        if success:
            print(f"\n[+] Version bump completed")
            if self.dry_run:
                print(f"    (Dry run - no files were modified)")
            return 0
        else:
            print(f"\n[X] Version bump failed")
            return 1


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description='Bump HaroFramework documentation version',
        epilog='Examples:\n'
               '  python version_bump.py doc/architecture/layer-system.md patch\n'
               '  python version_bump.py framework/doc/architecture/layer-system.md minor',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        'file',
        help='Path to document file'
    )
    parser.add_argument(
        'bump_type',
        choices=['major', 'minor', 'patch'],
        help='Type of version bump'
    )
    parser.add_argument(
        '--dry-run', '-d',
        action='store_true',
        help='Show changes without modifying files'
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

    # Run version bump
    bumper = VersionBumper(root_path, dry_run=args.dry_run)
    return bumper.run(args.file, args.bump_type)


if __name__ == '__main__':
    sys.exit(main())
