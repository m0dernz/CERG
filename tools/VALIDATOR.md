# CERG Validator — `cerg-validate.py`

| Field | Value |
|-------|-------|
| **Version** | 1.0 |
| **Status** | Active |
| **Owner** | Governance Pillar Leader |
| **CI Gate** | Yes — 0 errors required before commit |

## Overview

`tools/cerg-validate.py` is the authoritative CI gate for CERG repository changes. It validates markdown link integrity, catalog references, file inventory, and metadata consistency across the corpus. **Zero errors are required before committing.**

## Error Classes

| Error Code | Check | Severity | Fix |
|------------|-------|----------|-----|
| `FILE_NOT_IN_CATALOG` | Every markdown file in the repository must be registered in CAT-001 §5 | Error | Add the file to CAT-001 §5 catalog table |
| `ID_NOT_IN_CATALOG` | Every cross-referenced CERG document ID must exist in CAT-001 | Error | Register the referenced ID or fix the cross-reference |
| `STATUS_MISMATCH` | File metadata Status field must match CAT-001 catalog entry | Error | Update either the file frontmatter or the catalog entry |
| `LINK_MISSING` | Every markdown link target must resolve to an existing file on disk | Error | Create the target file or fix the link path |
| `DRAFT_VERSION` | File status is Approved but version string contains "Draft" | Error | Update version to a numbered release or change status to Draft |
| `RESTRICTED_CLASSIFICATION` | A Public document references an Internal or Confidential document | Warning | Use generic description instead of direct link, or reclassify |
| `FRONTMATTER_MISSING` | File is missing the required metadata table | Error | Add metadata table per STY-001 §4 |
| `SECTION_NUMBER_GAP` | Section numbering has gaps or is out of sequence | Error | Renumber sections from highest to lowest |

## Usage

```bash
# Run the full validation suite
python3 tools/cerg-validate.py

# Check specific file(s)
python3 tools/cerg-validate.py governance/CERG-GOV-OM-001_CERG_Operating_Model.md

# Verbose output showing all checks passed
python3 tools/cerg-validate.py --verbose
```

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | All checks passed — no errors |
| 1 | One or more errors found |

## Inputs

- The entire CERG markdown corpus (recursive directory walk)
- `CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md` for catalog registration checks
- Individual file frontmatter/metadata for STATUS_MISMATCH

## Outputs

- Human-readable error output listing each error with file path, line number (where applicable), and description
- Non-zero exit code if any error-level check fails

## Error-free Commit Checklist

Before committing, verify:

- [ ] `python3 tools/cerg-validate.py` exits with code 0
- [ ] New files are registered in CAT-001 §5
- [ ] New cross-references point to existing files with correct relative paths
- [ ] Metadata table follows STY-001 §4 format
- [ ] Section numbering is sequential with no gaps
- [ ] Classification levels are consistent (Public files do not link to Internal/Confidential files)

## Related Documents

| Document | Relationship |
|----------|-------------|
| [AGENTS.md](../AGENTS.md) | CI gate requirements and workflow |
| [CERG-GOV-CAT-001](../governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Authoritative document catalog |
| [CERG-GOV-STY-001](../governance/CERG-GOV-STY-001_Document_Authoring_and_Style_Guide.md) | Metadata table format, section numbering rules |
| [tools/cerg-integrity-check.py](cerg-integrity-check.py) | Supplementary integrity checker (not a release gate) |
