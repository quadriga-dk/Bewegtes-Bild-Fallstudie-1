"""Extract learning objectives with metadata from Lernziele.md files."""

from __future__ import annotations
import logging
import re
from pathlib import Path
from typing import Any
from .utils import get_repo_root, save_yaml_file, get_file_path, load_yaml_file

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


# Default values for missing metadata
DEFAULT_COMPETENCY = "nicht anwendbar"
DEFAULT_BLOOMS = "nicht anwendbar"
DEFAULT_DATA_FLOW = "nicht anwendbar"


def normalize_whitespace(text: str) -> str:
    """Normalize repeated whitespace and newlines to single spaces."""
    return re.sub(r"\s+", " ", text).strip()


def parse_metadata_comment(comment: str) -> dict[str, str]:
    """
    Parse metadata from HTML comment.
    
    Format: <!-- competency: X | blooms: Y -->
    
    Args:
        comment: HTML comment string
    
    Returns:
        dict: Parsed metadata
    """
    metadata = {}
    
    # Remove HTML comment markers
    content = re.sub(r'<!--\s*|\s*-->', '', comment)
    
    for part in content.split('|'):
        part = part.strip()
        if ':' not in part:
            continue
        key, value = part.split(':', 1)
        key = key.strip().lower().replace(' ', '-')
        value = value.strip()
        if not value:
            continue
        # Map 'blooms' key to the expected 'blooms-category' field name
        if key == 'blooms':
            metadata['blooms-category'] = value
        elif key == 'competency':
            metadata[key] = value
    
    return metadata


def validate_objective_metadata(objective_data: dict[str, Any]) -> list[str]:
    """
    Validate and fill in missing metadata for a learning objective (in place).
    
    Args:
        objective_data: Objective data dictionary (mutated in place)
    
    Returns:
        list[str]: Names of fields that were missing and filled with defaults
    """
    missing_fields = []
    
    if not objective_data.get('competency'):
        missing_fields.append('competency')
        objective_data['competency'] = DEFAULT_COMPETENCY
    
    if not objective_data.get('blooms-category'):
        missing_fields.append('blooms-category')
        objective_data['blooms-category'] = DEFAULT_BLOOMS
    
    if not objective_data.get('data-flow'):
        objective_data['data-flow'] = derive_data_flow(
            objective_data.get('competency', DEFAULT_COMPETENCY)
        )
    
    return missing_fields


def derive_data_flow(competency: str) -> str:
    """Derive data-flow from competency."""
    competency_normalized = normalize_whitespace(competency)

    if competency_normalized == "Orientierungswissen":
        return "übergreifend"

    if competency_normalized.startswith("1."):
        return "1 Planung"

    if competency_normalized.startswith("2."):
        return "2 Erhebung und Aufbereitung"

    if competency_normalized.startswith("3."):
        return "3 Management"

    if competency_normalized.startswith("4."):
        return "4 Analyse"

    if competency_normalized.startswith("5."):
        return "5 Publikation und Nachnutzung"

    return DEFAULT_DATA_FLOW


def extract_admonition_blocks(
    content: str
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """
    Extract all admonition blocks with learning objectives from Markdown content.
    
    Args:
        content: Markdown file content
    
    Returns:
        tuple: (extracted blocks, validation issues)
    """
    blocks = []
    validation_issues = []
    
    # Pattern to match admonition blocks with their content
    admonition_pattern = r'```\{admonition\}\s+(.+?)\n((?::[^\n]+\n)*)((?:(?!```).)+)```'
    
    matches = re.finditer(admonition_pattern, content, re.DOTALL | re.MULTILINE)
    
    for match in matches:
        title_line = match.group(1).strip()
        body = match.group(3).strip()
        
        # Parse title - extract text and reference
        title_match = re.match(r'\[(.+?)\]\((.+?)\)(\s*\(\*(.+?)\*\))?', title_line)
        
        if not title_match:
            logger.warning("Could not parse admonition title: %s", title_line)
            continue
        
        section_title = title_match.group(1)
        section_ref = title_match.group(2)
        section_note = title_match.group(4) if title_match.group(4) else None

        # Extract optional learning goal; fall back to the admonition title
        # Format: <!-- learning-goal: ... -->
        learning_goal_match = re.search(
            r'<!--\s*learning-goal:\s*(.+?)\s*-->',
            body,
            re.DOTALL,
        )
        if learning_goal_match:
            learning_goal = normalize_whitespace(learning_goal_match.group(1))
        else:
            learning_goal = section_title # make it TODO
            validation_issues.append({
                'section': section_title,
                'missing_fields': ['learning-goal']
            })

        # Extract chapter name from the outermost START marker
        chapter = None
        start_marker_match = re.search(r'<!--\s*START:\s*(.+?)\s*-->', body)
        if start_marker_match:
            chapter = start_marker_match.group(1).strip()

        # Strip all START/END markers so both wrapped and bare formats parse identically
        body_cleaned = re.sub(r'<!--\s*START:\s*.+?\s*-->\s*', '', body)
        body_cleaned = re.sub(r'\s*<!--\s*END:\s*.+?\s*-->', '', body_cleaned)

        # Parse numbered objectives with optional inline metadata comment
        objectives = []
        objective_pattern = r'\d+\.\s+(.+?)(?:\n\s*<!--\s*(.+?)\s*-->)?(?=\n\d+\.|\n\n|$)'

        for obj_match in re.finditer(objective_pattern, body_cleaned, re.DOTALL):
            objective_text = normalize_whitespace(obj_match.group(1))
            metadata_comment = obj_match.group(2)

            objective_data = {'learning-objective': objective_text}
            if metadata_comment:
                objective_data.update(parse_metadata_comment(metadata_comment))

            missing_fields = validate_objective_metadata(objective_data)
            if missing_fields:
                validation_issues.append({
                    'section': section_title,
                    'objective': objective_text[:60],
                    'missing_fields': missing_fields
                })

            objectives.append(objective_data)
        
        if objectives:
            block_data = {
                'section-title': section_title,
                'section-reference': section_ref,
                'learning-goal': learning_goal,
                'objectives': objectives
            }
            
            if section_note:
                block_data['section-note'] = section_note
            
            if chapter:
                block_data['chapter'] = chapter
            else:
                logger.warning(
                    "No chapter specified for section '%s'. "
                    "Add '<!-- START: ChapterName -->' at the beginning of the objectives.",
                    section_title
                )
                validation_issues.append({
                    'section': section_title,
                    'missing_fields': ['chapter']
                })
            
            blocks.append(block_data)
            logger.info(
                "Extracted section '%s' with %d objectives (chapter: %s)",
                section_title,
                len(objectives),
                chapter or "unknown"
            )
    
    return blocks, validation_issues


def extract_from_lernziele_file(
    md_file_path: Path
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """
    Extract learning objectives from a Lernziele.md file.
    
    Args:
        md_file_path: Path to Lernziele.md
    
    Returns:
        tuple: (extracted sections, validation issues)
    """
    try:
        with md_file_path.open(encoding="utf-8") as f:
            content = f.read()
        
        blocks, issues = extract_admonition_blocks(content)
        
        logger.info(
            "Extracted %d admonition blocks from %s",
            len(blocks),
            md_file_path.name
        )
        
        if issues:
            logger.info(
                "Found %d objectives with missing metadata in %s",
                len(issues),
                md_file_path.name
            )
        
        return blocks, issues
        
    except FileNotFoundError:
        logger.error("File not found: %s", md_file_path)
        return [], []
    except Exception:
        logger.exception("Error reading file: %s", md_file_path)
        return [], []


def generate_validation_report(
    validation_issues: list[dict[str, Any]],
    output_path: Path | None = None
) -> str:
    """
    Generate a human-readable validation report.
    
    Args:
        validation_issues: List of validation issues
        output_path: Optional path to save the report
    
    Returns:
        str: Formatted report
    """
    if not validation_issues:
        report = "✅ All learning objectives have complete metadata!\n"
    else:
        report = f"⚠️ Found {len(validation_issues)} learning objectives with missing metadata:\n\n"
        
        for i, issue in enumerate(validation_issues, 1):
            report += f"{i}. Section: {issue['section']}\n"
            if 'objective' in issue:
                report += f"   Objective: {issue['objective']}...\n"
            report += f"   Missing: {', '.join(issue['missing_fields'])}\n\n"
        
        report += "\nTo fix missing competency/blooms: Add HTML comments after each objective:\n"
        report += "<!-- competency: X | blooms: Y -->\n"
        report += "\nTo fix missing learning-goal: Add a comment inside the admonition block:\n"
        report += "<!-- learning-goal: Your learning goal text -->\n"
        report += "\nTo fix missing chapter: Add a START marker inside the admonition block:\n"
        report += "<!-- START: ChapterName -->\n"
    
    if output_path:
        with output_path.open("w", encoding="utf-8") as f:
            f.write(report)
        logger.info("Validation report saved to %s", output_path)
    
    return report


def merge_learning_objectives_into_metadata() -> bool:
    """
    Extract learning objectives from Lernziele.md and merge into metadata.yml.

    Returns:
        bool: True if successful
    """
    try:
        repo_root = get_repo_root()

        # Find the single Lernziele.md file
        excluded_parts = {"_build", "_jupyter_execute", "_sources", "__pycache__"}

        def is_valid(f: Path) -> bool:
            return (
                not f.name.startswith('_')
                and f.suffix != '.j2'
                and not any(part in excluded_parts for part in f.parts)
            )

        patterns = ["**/[Ll]ernziel*.md", "**/*learning*objective*.md"]
        md_file = next(
            (f for pattern in patterns for f in repo_root.glob(pattern) if is_valid(f)),
            None,
        )

        if md_file is None:
            logger.warning("No Lernziele file found")
            return True

        sections, validation_issues = extract_from_lernziele_file(md_file)

        # Handle validation report
        report_path = repo_root / "learning-objectives-validation.txt"
        if validation_issues:
            generate_validation_report(validation_issues, report_path)
            logger.warning(
                "⚠️ Found %d objectives with missing metadata. "
                "See learning-objectives-validation.txt for details.",
                len(validation_issues),
            )
        else:
            logger.info("✅ All learning objectives have complete metadata")
            if report_path.exists():
                report_path.unlink()
                logger.info("Removed old validation report (no issues found)")

        if not sections:
            logger.warning("No learning objectives extracted")
            return True

        # Load existing metadata.yml
        metadata_path = get_file_path("metadata.yml", repo_root)
        metadata = load_yaml_file(metadata_path)

        if not metadata or not isinstance(metadata, dict):
            logger.error("Could not load metadata.yml")
            return False

        # Build chapter → objectives/learning-goal mappings
        chapter_objectives: dict[str, list] = {}
        chapter_learning_goals: dict[str, str] = {}
        for section in sections:
            chapter = section.get('chapter')
            if not chapter:
                continue
            chapter_objectives.setdefault(chapter, []).extend(section['objectives'])
            learning_goal = section.get('learning-goal')
            if learning_goal:
                if chapter in chapter_learning_goals and chapter_learning_goals[chapter] != learning_goal:
                    logger.warning(
                        "Multiple learning goals found for chapter '%s'. Using first one.",
                        chapter,
                    )
                else:
                    chapter_learning_goals[chapter] = learning_goal

        # Merge into metadata chapters
        for chapter in metadata.get("chapters", []):
            if not isinstance(chapter, dict):
                continue
            chapter_title = chapter.get("title", "")
            if chapter_title not in chapter_objectives:
                continue
            chapter["learning-goal"] = chapter_learning_goals.get(chapter_title, "TODO")
            chapter["learning-objectives"] = chapter_objectives[chapter_title]

        if save_yaml_file(metadata_path, metadata):
            logger.info("Successfully merged learning objectives into metadata.yml")
            return True
        else:
            logger.error("Failed to save updated metadata.yml")
            return False

    except Exception:
        logger.exception("Error merging learning objectives")
        return False


if __name__ == "__main__":
    # Extract and merge into metadata
    success = merge_learning_objectives_into_metadata()
    exit(0 if success else 1)