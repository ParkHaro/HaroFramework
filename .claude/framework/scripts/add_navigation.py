#!/usr/bin/env python3
"""
add_navigation.py - Smart Navigation Generator for HaroFramework Documentation

Purpose: Automatically add intelligent navigation to all markdown documents.
         Navigation includes actual target document titles for better UX.

Usage:
    python add_navigation.py --apply-all              # Apply to all documents
    python add_navigation.py --dir .claude/commands/  # Specific directory
    python add_navigation.py --dry-run                # Preview changes
    python add_navigation.py --file path/to/doc.md    # Single file

Features:
- Reads target document metadata to extract titles
- Calculates relative paths for Home, Category, Parent
- Inserts navigation after metadata block
- Safe file operations with backup
- Comprehensive error handling and reporting

Author: HaroFramework Team
Version: 1.0.0
"""

import os
import re
import sys
import argparse
import logging
from pathlib import Path
from typing import Dict, Optional, Tuple
import yaml

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)

# Navigation template
NAV_TEMPLATE = '<!-- Navigation -->\n**🏠 [{home_title}]({home_path})** | **📂 [{category_title}]({category_path})** | **⬆️ [{parent_title}]({parent_path})**\n\n---\n'

# Navigation markers for detection
NAV_START_MARKER = '<!-- Navigation -->'
NAV_END_MARKER = '---'


class DocumentNavigator:
    """Handles navigation generation for documentation."""

    def __init__(self, root_dir: str):
        """
        Initialize navigator.

        Args:
            root_dir: Project root directory path
        """
        self.root_dir = Path(root_dir).resolve()
        self.title_cache = {}  # Cache for document titles
        self.stats = {
            'processed': 0,
            'updated': 0,
            'skipped': 0,
            'errors': 0
        }

    def extract_metadata(self, file_path: Path) -> Optional[Dict]:
        """
        Extract YAML frontmatter metadata from markdown file.

        Args:
            file_path: Path to markdown file

        Returns:
            Metadata dictionary or None if not found
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Match YAML frontmatter (between --- markers)
            match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
            if not match:
                logger.warning(f"No metadata found in {file_path.name}")
                return None

            yaml_content = match.group(1)
            metadata = yaml.safe_load(yaml_content)
            return metadata

        except Exception as e:
            logger.error(f"Error extracting metadata from {file_path}: {e}")
            return None

    def get_document_title(self, file_path: Path) -> str:
        """
        Get document title from metadata or filename.

        Args:
            file_path: Path to document

        Returns:
            Document title
        """
        # Check cache first
        file_key = str(file_path)
        if file_key in self.title_cache:
            return self.title_cache[file_key]

        # Try to read metadata
        metadata = self.extract_metadata(file_path)
        if metadata and 'title' in metadata:
            title = metadata['title']
            self.title_cache[file_key] = title
            return title

        # Fallback to filename
        title = file_path.stem.replace('_', ' ').replace('-', ' ').title()
        self.title_cache[file_key] = title
        return title

    def calculate_home_path(self, current_file: Path) -> str:
        """
        Calculate relative path to MASTER_INDEX.md (or _KOR.md for Korean docs).

        Args:
            current_file: Current document path

        Returns:
            Relative path string
        """
        # Determine if current file is Korean
        is_korean = current_file.stem.endswith('_KOR')
        index_name = 'MASTER_INDEX_KOR.md' if is_korean else 'MASTER_INDEX.md'
        master_index = self.root_dir / '.claude' / index_name

        try:
            rel_path = os.path.relpath(master_index, current_file.parent)
            return rel_path.replace('\\', '/')
        except Exception as e:
            logger.error(f"Error calculating home path for {current_file}: {e}")
            return f'./{index_name}'

    def find_category_index(self, current_file: Path) -> Optional[Path]:
        """
        Find category index file (INDEX.md/INDEX_KOR.md or README.md/README_KOR.md).

        Args:
            current_file: Current document path

        Returns:
            Path to category index or None
        """
        current_dir = current_file.parent
        is_korean = current_file.stem.endswith('_KOR')

        # Define index file names based on language
        if is_korean:
            index_names = ['INDEX_KOR.md', 'README_KOR.md', 'index_KOR.md']
        else:
            index_names = ['INDEX.md', 'README.md', 'index.md']

        # Check for index files in order of priority
        for index_name in index_names:
            index_file = current_dir / index_name
            if index_file.exists():
                return index_file

        return None

    def calculate_category_path(self, current_file: Path) -> Tuple[str, Path]:
        """
        Calculate relative path to category index.

        Args:
            current_file: Current document path

        Returns:
            Tuple of (relative path, absolute path to category index)
        """
        category_index = self.find_category_index(current_file)

        if category_index is None:
            # No category index, use current file as fallback
            return './', current_file

        try:
            rel_path = os.path.relpath(category_index, current_file.parent)
            return rel_path.replace('\\', '/'), category_index
        except Exception as e:
            logger.error(f"Error calculating category path for {current_file}: {e}")
            return './', current_file

    def calculate_parent_path(self, current_file: Path, metadata: Dict) -> Tuple[str, Path]:
        """
        Calculate relative path to parent document.

        Args:
            current_file: Current document path
            metadata: Document metadata

        Returns:
            Tuple of (relative path, absolute path to parent)
        """
        is_korean = current_file.stem.endswith('_KOR')

        # Try to get parent from metadata
        parent_docs = metadata.get('parent_documents', [])

        if parent_docs:
            # Use first parent document
            parent_rel = parent_docs[0]

            # Convert to Korean version if needed
            if is_korean and not parent_rel.endswith('_KOR.md'):
                # Replace .md with _KOR.md
                parent_rel = parent_rel.replace('.md', '_KOR.md')

            parent_abs = (current_file.parent / parent_rel).resolve()

            if parent_abs.exists():
                try:
                    rel_path = os.path.relpath(parent_abs, current_file.parent)
                    return rel_path.replace('\\', '/'), parent_abs
                except Exception as e:
                    logger.warning(f"Error with parent path from metadata: {e}")

        # Fallback to category index
        category_path, category_abs = self.calculate_category_path(current_file)
        return category_path, category_abs

    def generate_navigation(self, file_path: Path) -> Optional[str]:
        """
        Generate navigation HTML for a document.

        Args:
            file_path: Path to document

        Returns:
            Navigation HTML string or None if error
        """
        try:
            # Extract metadata
            metadata = self.extract_metadata(file_path)
            if metadata is None:
                metadata = {}  # Use empty dict as fallback

            # Calculate paths
            home_path = self.calculate_home_path(file_path)
            category_path, category_abs = self.calculate_category_path(file_path)
            parent_path, parent_abs = self.calculate_parent_path(file_path, metadata)

            # Get titles
            home_title = "HaroFramework Project"  # Master index title
            category_title = self.get_document_title(category_abs) if category_abs else "Category"
            parent_title = self.get_document_title(parent_abs) if parent_abs else "Parent"

            # Generate navigation
            nav = NAV_TEMPLATE.format(
                home_title=home_title,
                home_path=home_path,
                category_title=category_title,
                category_path=category_path,
                parent_title=parent_title,
                parent_path=parent_path
            )

            return nav

        except Exception as e:
            logger.error(f"Error generating navigation for {file_path}: {e}")
            return None

    def has_navigation(self, content: str) -> bool:
        """Check if content already has navigation block."""
        return NAV_START_MARKER in content

    def remove_existing_navigation(self, content: str) -> str:
        """Remove existing navigation block from content."""
        # Pattern to match navigation block
        # From <!-- Navigation --> to next ---
        pattern = r'<!-- Navigation -->.*?---\n'
        content = re.sub(pattern, '', content, flags=re.DOTALL)
        return content

    def insert_navigation(self, content: str, navigation: str) -> str:
        """
        Insert navigation after metadata block.

        Args:
            content: Original file content
            navigation: Navigation HTML to insert

        Returns:
            Updated content with navigation
        """
        # Remove existing navigation first
        content = self.remove_existing_navigation(content)

        # Find end of metadata block (second ---)
        metadata_pattern = r'^(---\s*\n.*?\n---\s*\n)'
        match = re.match(metadata_pattern, content, re.DOTALL)

        if match:
            # Insert navigation after metadata
            metadata_end = match.end()
            new_content = (
                content[:metadata_end] +
                '\n' +
                navigation +
                content[metadata_end:].lstrip('\n')
            )
            return new_content
        else:
            # No metadata found, insert at beginning
            logger.warning("No metadata found, inserting navigation at beginning")
            return navigation + '\n' + content

    def process_file(self, file_path: Path, dry_run: bool = False) -> bool:
        """
        Process a single markdown file to add navigation.

        Args:
            file_path: Path to markdown file
            dry_run: If True, only simulate changes

        Returns:
            True if successful, False otherwise
        """
        try:
            self.stats['processed'] += 1

            # Read file
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()

            # Generate navigation
            navigation = self.generate_navigation(file_path)
            if navigation is None:
                logger.error(f"Failed to generate navigation for {file_path.name}")
                self.stats['errors'] += 1
                return False

            # Insert navigation
            new_content = self.insert_navigation(original_content, navigation)

            # Check if content changed
            if new_content == original_content:
                logger.info(f"No changes needed for {file_path.name}")
                self.stats['skipped'] += 1
                return True

            if dry_run:
                logger.info(f"[DRY RUN] Would update {file_path.name}")
                logger.debug(f"Navigation preview:\n{navigation}")
                self.stats['updated'] += 1
                return True

            # Backup original file
            backup_path = file_path.with_suffix('.md.bak')
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(original_content)

            # Write updated content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

            logger.info(f"✓ Updated {file_path.name}")
            self.stats['updated'] += 1
            return True

        except Exception as e:
            logger.error(f"Error processing {file_path}: {e}")
            self.stats['errors'] += 1
            return False

    def process_directory(self, directory: Path, dry_run: bool = False):
        """
        Process all markdown files in a directory recursively.

        Args:
            directory: Directory path to process
            dry_run: If True, only simulate changes
        """
        md_files = list(directory.rglob('*.md'))

        logger.info(f"Found {len(md_files)} markdown files in {directory}")

        for md_file in md_files:
            self.process_file(md_file, dry_run)

    def print_statistics(self):
        """Print processing statistics."""
        logger.info("\n" + "="*60)
        logger.info("NAVIGATION GENERATION STATISTICS")
        logger.info("="*60)
        logger.info(f"Processed: {self.stats['processed']}")
        logger.info(f"Updated:   {self.stats['updated']}")
        logger.info(f"Skipped:   {self.stats['skipped']}")
        logger.info(f"Errors:    {self.stats['errors']}")
        logger.info("="*60)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Add smart navigation to HaroFramework documentation'
    )

    parser.add_argument(
        '--apply-all',
        action='store_true',
        help='Apply navigation to all documents in project'
    )

    parser.add_argument(
        '--dir',
        type=str,
        help='Apply to specific directory'
    )

    parser.add_argument(
        '--file',
        type=str,
        help='Apply to specific file'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview changes without modifying files'
    )

    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Enable verbose logging'
    )

    args = parser.parse_args()

    # Configure logging level
    if args.verbose:
        logger.setLevel(logging.DEBUG)

    # Determine project root (assuming script is in .claude/framework/scripts/)
    script_path = Path(__file__).resolve()
    project_root = script_path.parent.parent.parent.parent

    logger.info(f"Project root: {project_root}")

    # Initialize navigator
    navigator = DocumentNavigator(project_root)

    # Process based on arguments
    if args.file:
        # Single file
        file_path = Path(args.file).resolve()
        if not file_path.exists():
            logger.error(f"File not found: {file_path}")
            sys.exit(1)

        navigator.process_file(file_path, args.dry_run)

    elif args.dir:
        # Specific directory
        dir_path = Path(args.dir).resolve()
        if not dir_path.is_dir():
            logger.error(f"Directory not found: {dir_path}")
            sys.exit(1)

        navigator.process_directory(dir_path, args.dry_run)

    elif args.apply_all:
        # All documents in .claude directory
        claude_dir = project_root / '.claude'
        if not claude_dir.is_dir():
            logger.error(f".claude directory not found: {claude_dir}")
            sys.exit(1)

        navigator.process_directory(claude_dir, args.dry_run)

    else:
        parser.print_help()
        sys.exit(1)

    # Print statistics
    navigator.print_statistics()

    # Exit with error code if there were errors
    if navigator.stats['errors'] > 0:
        sys.exit(1)


if __name__ == '__main__':
    main()
