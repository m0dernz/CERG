## DOCUMENT AUTHORING AND STYLE GUIDE
### House Voice · Metadata · Structure · Cross-References · Skeleton · Quality Gates

---

| | |
|---|---|
| **Document ID** | CERG-GOV-STY-001 |
| **Version** | 1.02 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Policy & Standards) |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) · [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) · [`CERG-GOV-RAC-001`](CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) · [`CERG-GOV-VAR-001`](CERG-GOV-VAR-001_Organization_Adaptation_Profile.md) |
| **Review Cycle** | Annual / On material change to catalog, naming, role, or rendering conventions |
| **Frameworks** | NIST CSF 2.0 GOVERN · ISO/IEC 27001 A.5 · NIST 800-53r5 PM |
| **Regulations** | Cross-cutting |
| **Environments** | CERG documentation library |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [CERG House Voice](#2-cerg-house-voice)
3. [Document Anatomy](#3-document-anatomy)
4. [Metadata Rules](#4-metadata-rules)
5. [ID, File Name, and Status Rules](#5-id-file-name-and-status-rules)
6. [Role and RACI Rules](#6-role-and-raci-rules)
7. [Cross-Reference Rules](#7-cross-reference-rules)
8. [Callouts, Tables, and Lists](#8-callouts-tables-and-lists)
9. [Language and Style Rules](#9-language-and-style-rules)
10. [Org-Adaptation and Token Rules](#10-org-adaptation-and-token-rules)
11. [Blank Document Skeleton](#11-blank-document-skeleton)
12. [Quality Gates Before Commit](#12-quality-gates-before-commit)
12.5. [Document Lifecycle Procedure](#125-document-lifecycle-procedure)
13. [Document Control](#13-document-control)
14. [Document Appearance](#14-document-appearance)
---

## 1. Purpose and Scope

This guide defines how CERG documents are authored, reviewed, and kept consistent. It is the companion to the catalog. The catalog governs IDs, registration, status, and cross-reference discipline. This guide governs the writing pattern, metadata pattern, document skeleton, role discipline, quality gates, and house voice.

It applies to every new or revised CERG policy, governance instrument, standard, procedure, plan, template, and operational package.

> **Consistency Is a Control**
>
> A framework that looks like 60 unrelated documents is not a framework. Consistent structure, vocabulary, role names, metadata, and cross-references make the library operational. A reader should be able to open any artifact and know where to find scope, roles, evidence, approvals, and revision history without hunting.

---

## 2. CERG House Voice

CERG writing is:

- direct;
- practical;
- declarative;
- evidence-oriented;
- opinionated where ambiguity would create risk;
- clear about ownership and handoffs;
- usable by a small team without weakening the role model.

CERG writing is not:

- vendor marketing copy;
- legal boilerplate without operational direction;
- generic security advice;
- a list of controls without owners or evidence;
- a maturity fantasy that assumes a large staff;
- a compliance checklist with no operating model.

A CERG artifact should answer five questions quickly:

1. What does this document govern?
2. Who owns it?
3. What must happen?
4. What proves it happened?
5. Where does a reader go next?

---

## 3. Document Anatomy

Every full CERG artifact follows this structure unless the document type requires a narrow exception.

| **Section** | **Purpose** | **Required** |
|---|---|---|
| Title block | Names the artifact and subtitle. | Yes |
| Metadata table | Identifies ID, status, owner, parent, supporting documents, review cycle, frameworks, regulations, environments. | Yes |
| Table of Contents | Gives predictable navigation. | Yes for substantive artifacts |
| Purpose and Scope | Defines why the artifact exists and what it covers. | Yes |
| Operating content | Requirements, process, template, plan, or instrument body. | Yes |
| Roles and Responsibilities | Shows canonical role accountability. | Yes when the body assigns work |
| Evidence, metrics, or outputs | Shows what proves the process or control worked. | Yes where applicable |
| Document Control | Records version, approval, review, revision history, and triggers. | Yes |
| Related Documents | Lists authoritative links to related artifacts. | Yes |

---

## 4. Metadata Rules

Use this field set unless a sibling document of the same type uses a clearly established variant.

| **Field** | **Rule** |
|---|---|
| Document ID | Must match catalog ID and file name stem. |
| Version | New artifacts start at `1.0`. Catalog amendments increment the catalog version. |
| Status | New artifacts start as `Draft` unless the human owner has explicitly approved. |
| Classification | Use `Public` unless the artifact contains sensitive operational detail. |
| Owner | Use a canonical role from `CERG-GOV-OM-001` or an already established artifact owner. |
| Parent Policy / Parent Document / Parent Plan | Link to the governing artifact. |
| Supporting Documents | Link only to cataloged or planned artifacts. |
| Review Cycle | Use concrete cadence and trigger conditions. |
| Frameworks | Cite major frameworks that shape the artifact. |
| Regulations | List applicable regulatory drivers or `Cross-cutting`. |
| Environments | State the scope clearly. |

Metadata is not decorative. It is how the document participates in governance, audit, evidence, and lifecycle management.

---

## 5. ID, File Name, and Status Rules

### 5.1 ID Pattern

CERG IDs follow:

`CERG-<TYPE>-<DOMAIN>-<NNN>`

Examples:

| **Type** | **Example** | **Meaning** |
|---|---|---|
| `GOV` | `CERG-GOV-CAT-001` | Governance instrument |
| `STD` | `CERG-STD-AC-001` | Standard |
| `PRC` | `CERG-PRC-RM-001` | Procedure |
| `PLN` | `CERG-PLN-ISO-001` | Plan or operational package |
| `TMPL` | `CERG-TMPL-RM-002` | Standalone template |

New domain codes require a catalog amendment before the batch is complete.

### 5.2 File Name Pattern

Use:

`CERG-<TYPE>-<DOMAIN>-<NNN>_Readable_Title_With_Underscores.md`

Do not rename existing files casually. Links, catalog rows, and references depend on stable paths.

### 5.3 Status Pattern

| **Status** | **Use** |
|---|---|
| Draft | New artifact awaiting formal approval. |
| For Review | Draft artifact out for stakeholder or CISO review. |
| Approved | Human owner has approved the artifact for use; authoritative for operations and audit. |
| External Interface | Adjacent-function artifact included for cross-reference only; not CERG-governed. |
| Retired | Artifact no longer authoritative but retained for history. |

Publication is not a lifecycle status. Public-release eligibility is tracked separately in the publication manifest.

Do not self-approve new artifacts. If approval is pending, write `CISO (pending)` or the appropriate pending approver.

---

## 6. Role and RACI Rules

Use only canonical role names from `CERG-GOV-OM-001` and assignments from `CERG-GOV-RAC-001`.

Rules:

1. Do not invent role names.
2. Do not use synonyms if the canonical role exists.
3. A local roles table may explain responsibilities for the reader, but it must conform to `CERG-GOV-RAC-001`.
4. Scaling down is done by role consolidation onto fewer people, not by deleting roles.
5. Exactly one role is accountable for each activity where a RACI is used.
6. External teams may own adjacent programs; preserve those boundaries.

Examples of role discipline:

| **Avoid** | **Use Instead** |
|---|---|
| Security team | Governance Pillar Leader, Risk Pillar Leader, or Engineering Pillar Leader, as appropriate |
| AppSec owner | Application Security Engineer |
| Audit person | Evidence Librarian or Governance Pillar Leader |
| Vendor owner | Vendor Risk Analyst or Business Owner, depending on context |
| Executive security lead | Chief Information Security Officer (CISO) |

---

## 7. Cross-Reference Rules

The catalog's rules govern. This guide repeats the operational version for authors:

1. Link only to artifacts in the catalog (approved or planned).
2. Prefer Document ID over title in prose.
3. Use relative Markdown links to repo files.
4. Mark planned artifacts as `(Planned, V1.x)` or `(Planned, V2)`.
5. Do not cite a file that does not exist unless it is in the catalog as a planned artifact.
6. If an artifact is newly created, amend the catalog in the same batch.
7. If a related document is out of scope, state the boundary instead of inventing a fake artifact.

Good cross-reference:

`See [CERG-PRC-RM-001](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) for risk treatment workflow.`

Weak cross-reference:

`See the risk procedure.`

### 7.1 Stable Section ID Convention

CERG documents use numeric section numbers (e.g., `§9.7`) for sequential structure. However, cross-document references to numeric sections are fragile — renumbering a section in one document breaks references in all documents that point to the old number. To mitigate this, every substantive section SHOULD carry a stable anchor ID in addition to its numeric section heading.

#### Anchor ID Pattern

Add a stable HTML anchor directly before each top-level (`##`) and second-level (`###`) section heading:

```markdown
<a id="risk-acceptance-authority"></a>
## 9.7 Risk Acceptance Authority
```

Or use Markdown's built-in heading anchoring by choosing a stable, kebab-case heading slug and linking to it:

```markdown
## 9.7. Risk Acceptance Authority   {#risk-acceptance-authority}
```

For Markdown files in the CERG repository, the preferred approach is to append a stable anchor ID in curly braces after the heading:

```markdown
## 9.7. Risk Acceptance Authority   {#risk-acceptance-authority}
```

#### When to Use Stable Anchors

| **Section Type** | **Anchor Required?** | **Rationale** |
|---|---|---|
| Top-level sections (`## N. Title`) | Recommended | Frequently cross-referenced from other documents |
| Subsections (`### N.M Title`) referenced from other docs | Yes | Cross-document references are the primary fragility source |
| Subsections with no external references | Optional | Not yet referenced, but adding an anchor is cheap insurance |
| Appendices | Yes | Frequently referenced from regulatory packages |
| Document Control / Revision History | No | Never externally referenced by section number |

#### Anchor ID Convention

- Use lowercase kebab-case: `#risk-acceptance-authority`, `#evidence-library-structure`.
- Keep IDs concise but descriptive (2–5 words).
- Prefix with the document's domain segment if ambiguity is likely: `#cb-insm-overlay` rather than `#insm-overlay`.
- Do not include the numeric section number in the anchor ID (the whole point is to decouple from numbering).

#### Examples

```markdown
## 4. Authority and Status Lifecycle   {#authority-status-lifecycle}

### 4.1 Review Cadence Tiers   {#review-cadence-tiers}

### 4.2 CERG Source-of-Truth Model   {#source-of-truth-model}
```

Cross-reference format using stable anchors:

```
See [CERG-GOV-RMF-001](#risk-acceptance-authority) for risk acceptance approval authority.
For evidence tiers, refer to [CERG-GOV-AUD-001](#evidence-tier-requirements) §4.
```

> **Stable IDs Protect Cross-Document References**
>
> When §9.7 is renumbered to §9.8 because a new §9.6 is inserted, every cross-document link that said "§9.7" breaks silently. A stable anchor `#risk-acceptance-authority` survives renumbering. The numeric section remains in the heading for human readability; the anchor provides the machine-stable reference.

### 7.2 Cross-Reference Update Procedure

When section numbering changes in any document (insert, delete, or reorder sections):

1. **Identify affected references.** Search the entire CERG corpus for references to the renumbered document's old section numbers (e.g., search for `RMF-001 §9.7` across all `.md` files). Use `rgrep` or `search_files` tool.

2. **Update numeric references.** Replace each occurrence of the old section number with the new one in the referencing documents.

3. **Verify stable anchors.** If the renumbered section has a stable anchor (per §7.1), the anchor reference does NOT need updating — this is the benefit of stable anchors.

4. **Update TOC in the changed document.** The Table of Contents must reflect new section numbers and anchor links.

5. **Update internal cross-references.** Within the changed document itself, update any prose that references old section numbers.

6. **Validate.** Run `python3 tools/cerg-validate.py` to verify no broken links. Run `python3 tools/cerg-integrity-check.py` for broader drift detection.

7. **Commit.** One commit per changed file with message format: `renumber §§N–M in DOC-ID, update cross-references`.

#### Batch Renumbering for Inserted Sections

When inserting a new section between existing sections (e.g., inserting §6.5 between §6.4 and §6.5):

1. Renumber from the HIGHEST section number down to the insertion point to prevent cascading replacement.
2. Example: To insert §6.5 between §6.4 and §6.5, first renumber §6.5→§6.6, §6.6→§6.7, ..., then insert new §6.5.
3. Update all cross-document references to the renumbered sections (per step 1–2 above).

#### Cross-Reference Hygiene Checks (Pre-Commit)

Before committing any section renumbering:

- [ ] Search the corpus for references to the renumbered document.
- [ ] Update all found references.
- [ ] Run validator (0 errors required).
- [ ] Verify TOC matches new numbering.
- [ ] Verify stable anchors are present on externally-referenced sections.

---

## 8. Callouts, Tables, and Lists

### 8.1 Callouts

Use callouts to sharpen important guidance.

Pattern:

```markdown
> **Short Title**
>
> Practical explanation. Make the point directly. Avoid generic warnings.
```

Callouts should state a principle, pitfall, or operating rule. They should not repeat the paragraph above them.

### 8.2 Tables

Use tables when a reader must compare fields, owners, statuses, evidence, cadence, or approvals.

Rules:

- keep column names short;
- use canonical role names;
- make required fields obvious;
- avoid sprawling tables when a short list is clearer;
- include evidence or output columns when the table describes activity.

### 8.3 Lists

Use numbered lists for sequence. Use bullets for sets.

---

## 9. Language and Style Rules

### 9.1 Required Style

- Use active voice.
- Use direct verbs: owns, approves, records, reviews, escalates.
- Define thresholds, cadences, outputs, and evidence.
- Name the role that owns an activity.
- Prefer concrete nouns over vague terms.
- Use short paragraphs.

### 9.2 Prohibited or Discouraged Style

- No em dashes.
- Avoid passive constructions that hide ownership.
- Avoid `should` when the document creates a requirement. Use `must`, `shall`, or direct imperative language where appropriate.
- Avoid generic phrases such as `best practice`, `robust security`, or `industry standard` unless immediately defined.
- Do not cite regulations as decoration. Cite them when the artifact operationalizes a requirement.
- Do not add AI-tool attribution in commits, comments, or document text.

### 9.3 Terminology

| **Use** | **Avoid** |
|---|---|
| artifact | document thing, policy item |
| evidence | proof, support, backup material |
| accountable role | owner in vague contexts |
| residual risk | remaining risk when controls are considered |
| exception | waiver, unless the parent process uses waiver as a synonym |
| review cycle | cadence, unless speaking informally |

---

## 10. Org-Adaptation and Token Rules

`CERG-GOV-VAR-001` governs organization adaptation. Authors must not scatter hard-coded organization facts when a token should be used.

Rules:

1. Tokenize organization identity, scale, and example values when they are meant to vary by adopting organization.
2. Do not tokenize framework IDs, role names, core CERG terms, or control IDs.
3. Keep literal token examples intact in documents that teach the token scheme.
4. Run `python3 tools/cerg-render.py --check` before committing.
5. Do not edit rendered output back into source files unless the change is deliberate.

---

## 11. Blank Document Skeleton

Copy this skeleton for new substantive artifacts.

```markdown

## [DOCUMENT TITLE]
### [Subtitle: Topic · Topic · Topic]

---

| | |
|---|---|
| **Document ID** | CERG-[TYPE]-[DOMAIN]-[NNN] |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | [Canonical role] |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [Document links] |
| **Review Cycle** | Annual / [trigger] |
| **Frameworks** | [Frameworks] |
| **Regulations** | [Regulations] |
| **Environments** | [Scope] |

---

## Table of Contents


---

## 12. Quality Gates Before Commit

Every contribution must pass these gates before commit:

| **Gate** | **Command / Check** | **Pass Condition** |
|---|---|---|
| No em dash characters | Search files for the prohibited em dash character | No output |
| Render check | `python3 tools/cerg-render.py --check` | Passes |
| Catalog registration | Inspect `CERG-GOV-CAT-001` | New artifact listed or planned entry updated |
| Catalog status sync | `python3 tools/cerg-catalog-sync.py --ci` | Exit 0 — file frontmatter Status matches CAT-001 §5 |
| Role discipline | Compare against `CERG-GOV-OM-001` and `CERG-GOV-RAC-001` | No invented roles |
| Cross-reference discipline | Follow internal links or use a link checker when available | No dead links |
| Status discipline | Inspect metadata and Document Control | New artifact is Draft unless approved |
| Commit message hygiene | Review commit text | No AI-tool attribution |

A document is not complete until the catalog is amended where required.

---

## 12.5 Document Lifecycle Procedure

Every CERG document follows a defined lifecycle from creation through retirement.

### Status States

| **Status** | **Meaning** | **Who Can Set** |
|---|---|---|
| Planned | Artifact has an ID and owner but no draft yet | Governance Pillar Leader |
| Draft | Work in progress; not authoritative | Any author |
| For Review | Stakeholder or CISO review in progress | Governance Pillar Leader or document owner |
| Approved | Approved and active; authoritative for operations and audit | Approval authority defined in CAT-001 §4 |
| External Interface | Adjacent-function artifact included for cross-reference only | Adjacent-function owner, recorded by Governance |
| Retired | No longer authoritative but retained for history | CISO or Governance Pillar Leader |

### Lifecycle Workflow

1. **Create**: New artifact is drafted in `Draft` status. Document ID and naming follow [CERG-GOV-CAT-001](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) conventions.
2. **Peer Review**: Draft is reviewed by a second qualified analyst from the same or adjacent pillar. Review checks structure, cross-references, role discipline, and framework alignment.
3. **Pillar Leader Approval**: The owning pillar leader reviews and approves the document for publication.
4. **CISO Approval**: The CISO (or CISO designee) gives final approval. Material changes to policy (CERG-POL-001) require CISO approval directly.
5. **Approve / Release**: Status is set to `Approved` in both the header and Document Control section. The document is added to the catalog if new, or the catalog entry is updated if revised. Public-release eligibility is recorded separately in the publication manifest.
6. **Scheduled Review**: Each Approved document is reviewed on its assigned review cadence. The review is triggered by the review cycle defined in the document's front matter or by material changes to referenced frameworks, regulations, or organizational structure.
7. **Retire**: Documents that are superseded or no longer applicable are set to `Retired` status. The document is not deleted; it remains in the repository for historical reference.

### Emergency Fast-Track

When a document is needed urgently (e.g., to address a new regulatory requirement or respond to a significant incident), the peer review and pillar leader approval steps may be completed concurrently. CISO approval is still required before publication.

### Version Numbering

- New documents start at version 1.0.
- Material changes increment the minor version (1.0 → 1.1, 1.1 → 1.2).
- Major structural or scope changes increment the major version (1.x → 2.0).
- The version in the header front matter and the Document Control section must always match.
- Every version change is recorded in the Revision History table.

### Change Log Requirements

Every edit to an Approved document must include a Revision History entry with the following **standardised columns**:

| **Column** | **Required** | **Guidance** |
|---|---|---|
| **Version** | Yes | Document version at time of change (e.g., 1.22) |
| **Date** | Yes | Date of change in ISO 8601 format (YYYY-MM-DD) |
| **Author** | Yes | Canonical role name or named individual |
| **Change Type** | Yes | One of: `Major` (structural/scope change), `Minor` (new content, renumbering), `Patch` (typo, link fix, metadata correction) |
| **Summary** | Yes | Brief, specific description of what changed and why |
| **Linked Issue/PR** | Recommended | Reference to the issue, PR, or improvement register entry that drove the change |

Example:

| **Version** | **Date** | **Author** | **Change Type** | **Summary** | **Linked Issue/PR** |
|---|---|---|---|---|---|
| 1.22 | 2026-06-18 | Governance Pillar Leader | Minor | Expanded CIP-015 §13 from preliminary section to full INSM Implementation Annex | #INIT-9.1 |
| 1.21 | 2026-06-17 | Governance Pillar Leader | Patch | Updated supporting documents links | #42 |

> **Consistent Revision History Is an Audit Artifact**
>
> An auditor, regulator, or new team member should be able to reconstruct the change history of any CERG document from its Revision History table. Inconsistent columns, missing dates, or vague summaries ("updated section") undermine that. Use the standard columns above for every entry.

### Aggregated Changelog

The tool `tools/cerg-changelog.py` aggregates all Revision History entries from all Approved CERG documents into a single chronological changelog. Run it at any time to generate:

```bash
python3 tools/cerg-changelog.py                    # Print to stdout
python3 tools/cerg-changelog.py --since 2026-01-01  # Filter by date
python3 tools/cerg-changelog.py --doc PLN-CIP-001   # Filter by document
python3 tools/cerg-changelog.py --json              # JSON output
```

The aggregated changelog is a human-readable supplement, not a replacement for per-document Revision History tables.

### Framework-Wide Updates

When a new framework revision is published (e.g., NIST 800-53 Rev 6, NIST 800-171 Rev 4):

1. Governance Pillar Leader assesses impact across all documents.
2. Affected documents are prioritized by regulatory criticality.
3. Updates are drafted, reviewed, and published following the standard lifecycle.
4. The Document Catalog is updated to reflect new versions.
5. Stakeholders are notified of material changes through the CERG All-Hands or pillar sync.

---

## 13. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-STY-001 |
| **Version** | 1.02 |
| **Status** | Approved |
| **Effective Date** | 2026-06-14 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Policy & Standards) |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on material change to catalog, naming, role, or rendering conventions |
| **Next Scheduled Review** | 2027-05-22 |
| **Frameworks** | NIST CSF 2.0 GOVERN; ISO/IEC 27001 A.5; NIST 800-53r5 PM |
| **Regulations** | Cross-cutting |
| **Environments** | CERG documentation library |

---

## 14. Document Appearance

- Headers should use a solid color consistent with current branding.
- Do not use more than 1 color for headers.
- Keep complimentary colors minimal at 1-2
- Use the same color and font across related workbooks, tabs, intakes, and presentations.
- Avoid using fades or gradients.
- Avoid 'playful' hues that would take from the importance and professionalism of messaging. 

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.02 | 2026-06-18 | Governance Pillar Leader | Minor | Added Stable Section ID Convention (§7.1), Cross-Reference Update Procedure (§7.2), standardised Revision History columns, catalog sync reference in quality gates, and aggregated changelog tool reference. | INIT-10.1, INIT-10.3 |
| 1.01 | 2026-06-14 | Governance Pillar Leader | Minor | Aligned status lifecycle language to CAT-001 by using Approved as the authoritative status and treating publication eligibility as separate metadata. |
| 1.0 | 2026-05-22 | Cyber Governance | Initial release. Establishes the CERG house style, metadata and skeleton rules, role and cross-reference discipline, language rules, org-adaptation guidance, and pre-commit quality gates. |

### Review Triggers

- Catalog structure or cross-reference rule change
- Role roster or RACI change
- Org-adaptation token scheme change
- Quality gate or render tool change
- New artifact type introduced
- Direction from the CISO

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Document Catalog and Naming Convention | [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Authoritative ID, catalog, status, and cross-reference rule source |
| CERG Operating Model | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) | Canonical role roster source |
| Consolidated Roles and RACI Instrument | [`CERG-GOV-RAC-001`](CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) | RACI and role assignment source |
| Organization Adaptation Profile | [`CERG-GOV-VAR-001`](CERG-GOV-VAR-001_Organization_Adaptation_Profile.md) | Org-token and rendering guidance |
