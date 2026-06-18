
# SURGE: Cyber Engineering, Risk & Governance

## DOCUMENT CATALOG AND NAMING CONVENTION
### Authoritative Inventory · ID Scheme · Roadmap

---

| | |
|---|---|
| **Document ID** | CERG-GOV-CAT-001 |
| **Version** | 1.40 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Document Control) |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Quarterly - or upon any artifact add/retire |
| **Frameworks** | [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (GOVERN) · ISO/IEC 27001 A.5 |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed documentation |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Naming Convention](#2-naming-convention)
3. [Document Types](#3-document-types)
4. [Authority and Status Lifecycle](#4-authority-and-status-lifecycle)
5. [Authoritative Catalog (V1)](#5-authoritative-catalog-v1)
6. [Cross-Reference Rules](#6-cross-reference-rules)
7. [Artifact Roadmap (V1.x → V2)](#7-artifact-roadmap-v1x--v2)
8. [Document Control](#8-document-control)

## 1. Purpose and Scope

[CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) establishes a hierarchy of policy, standards, procedures, and guidelines. As the library grows, that hierarchy is only useful if there is a single, authoritative inventory of which artifacts exist, which are planned, which are authoritative, and which are exports of an authoritative artifact for a specific audience. This document is that inventory.

It applies to every CERG-owned artifact, policy, standard, procedure, plan, guideline, template, and operational package, regardless of medium (Markdown source, exported Word/PDF, intranet page, or third-party portal entry).

> **One Source, Many Exports**
>
> The authoritative source for every CERG document is the Markdown file in the CERG content repository. Everything else, Word exports, PDF deliverables, intranet pages, regulator portal uploads, is an export. Exports inherit the ID and version of the source. If the source and an export disagree, the source wins.

---

## 2. Naming Convention

Every CERG artifact has a Document ID of the form:

```
CERG-<TYPE>-<DOMAIN>-<NNN>
```

Where:

| **Element** | **Meaning** | **Examples** |
|---|---|---|
| `CERG` | Program prefix; never changes | - |
| `<TYPE>` | Document type - see Section 3 | `POL`, `STD`, `PRC`, `PLN`, `GL`, `TMPL`, `GOV` |
| `<DOMAIN>` | Two-to-four-letter domain code | `IT`, `OT`, `CUI`, `AC`, `RM`, `VM`, `CIP`, `LM` |
| `<NNN>` | Three-digit sequence within type+domain | `001`, `002` |

Files are named `<DocumentID>_<Short_Title>.md` using underscore-separated title case (e.g., `CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md`).



> **Stable ID Policy**: Document IDs are never reused. A retired ID remains reserved permanently. A superseding document identifies its predecessor. The machine-readable manifest preserves artifact history. Breaking changes to IDs, statuses, or role names are documented in the revision history.

> **Convention, Not Bureaucracy**
>
> The ID format exists so that a person reading a control reference can tell at a glance what kind of artifact they're being pointed at. A reader who sees `CERG-STD-OT-001` knows it's a standard; a reader who sees `CERG-PRC-VM-001` knows it's a procedure they can execute. Anything that obscures that signal, clever domain codes, free-form titles in the ID, is a mistake.

### 2.1 Domain Codes (V1)

| **Code** | **Domain** |
|---|---|
| `IT` | IT / cloud / SaaS |
| `OT` | Operational technology / grid control systems |
| `CUI` | Controlled Unclassified Information / [CMMC](https://dodcio.defense.gov/CMMC/) |
| `AC` | Access management / identity |
| `VM` | Exposure management |
| `RM` | Risk management (register, exceptions, scoring) |
| `IR` | Incident response (CERG-facing artifacts only) |
| `CIP` | NERC-CIP |
| `SOX` | Sarbanes-Oxley ITGC |
| `LM` | Logging, monitoring, detection |
| `CFG` | Secure configuration / hardening |
| `RES` | Cyber resilience and backup |
| `CR` | Cryptography and key management |
| `AR` | Architecture review / project intake |
| `TPRM` | Third-party / supply chain risk |
| `AV` | Adversarial validation |
| `MTR` | Metrics and reporting |
| `OM` | Operating model |
| `CAT` | Catalog / inventory |
| `CB` | Control baseline |
| `FRM` | Program-level framework narrative (e.g., the CERG Framework) |
| `TAX` | Risk taxonomy |
| `CMX` | Compliance matrix |
| `RMF` | Risk Management Framework |
| `IMP` | Implementation and adaptation guidance |
| `VAR` | Organization adaptation / variable and token scheme |
| `MAT` | Maturity self-assessment |
| `RAC` | Roles, responsibilities, and RACI |
| `SDL` | Secure software development / application security |
| `AM` | Asset management and inventory |
| `NET` | Network security and segmentation |
| `EP` | Endpoint and mobile security |
| `DG` | Data governance and classification |
| `AI` | Artificial intelligence security |
| `MSG` | Email and messaging security |
| `TM` | Threat modeling |
| `TI` | Threat intelligence |
| `AUD` | Audit and evidence management |
| `CHG` | Security change management |
| `BC` | Business continuity and disaster recovery |
| `ISO` | ISO/IEC 27001 operational package |
| `PRIV` | Privacy and data protection |
| `CAL` | Annual security and governance calendar |
| `STY` | Document authoring and style guide |
| `TRC` | Control-to-procedure traceability |
| `LL` | Lessons learned and program improvement |
| `IMPREG` | Program improvement register |
| `CEF` | Control effectiveness |
| `JA` | Job architecture and grade framework |
| `JD` | Job descriptions |
| `CMP` | Competency model and behavioral anchors |
| `PERF` | Performance management and promotion framework |
| `ONB` | Onboarding and integration program |
| `WFP` | Workforce planning and capacity model |
| `EDG` | Edge Register |
| `TRN` | Training, development, and certification framework |
| `SUCC` | Succession planning and talent review framework |
| `CON` | Contractor and non-employee staff integration |
| `JF` | Job Families and workforce architecture |
| `FLOW` | Cross-pillar operational flows |
| `CJ` | Crown jewels and loss-scenario library |
| `SLC` | CERG service-level commitments (CERG-to-business) |

New domains are added only by amendment to this catalog.

> **Domain codes reserved for workforce and operational flows:** `JF` (Job Families) and `FLOW` (Cross-Pillar Operational Flows) were added in CAT-001 v1.31 as part of the workforce architecture and operational flow build-out.

> **Type-Code Discipline**
>
> Only the seven type codes defined in §3 are valid: `POL`, `STD`, `PRC`, `PLN`, `GL`, `TMPL`, `GOV`. Any document that uses a different type code (e.g., `PROC` instead of `PRC`) is mis-named; the correction is to rename, not to silently accept the variant. Forward references to non-existent or planned artifacts must follow §6.2 and §7.

---

## 3. Document Types

| **Type Code** | **Type** | **Authority** | **What It Looks Like** |
|---|---|---|---|
| `POL` | Policy | CISO / Executive | Durable principles. Short. Rarely changes. One per program. |
| `STD` | Standard | Governance Pillar Leader | Specific, measurable, technology-aware requirements that implement policy principles. |
| `PRC` | Procedure | Pillar Owner | Step-by-step "how" - workflow, owner, evidence, frequency. |
| `PLN` | Plan / Operational Package | Pillar Owner | Bundled procedure + templates + checklists for a regulated or assessor-facing program (e.g., CIP, CUI, [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)). |
| `GL` | Guideline | Pillar Owner | Recommendations and good practice, not mandatory. |
| `TMPL` | Template | Pillar Owner | A blank artifact to be filled in (intake form, exception request, SSP). |
| `GOV` | Governance Instrument | Governance Pillar Leader | Cross-cutting instruments that aren't a single policy/standard/procedure - catalogs, control baselines, operating model, metrics dictionary. |

> **PLN vs. PRC**
>
> A `PRC` is a single procedure. A `PLN` is an operational package that bundles a procedure with templates, checklists, and registers because the regulator or auditor expects to see the bundle together (NERC-CIP, CUI/[CMMC](https://dodcio.defense.gov/CMMC/), [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)). When in doubt, prefer `PRC` and add templates as appendices.

---

## 4. Authority and Status Lifecycle

| **Status** | **Meaning** | **In Catalog?** |
|---|---|---|
| `Planned` | Artifact has an ID and an owner but no draft yet. | Yes - Section 7. |
| `Draft` | Work in progress. Not authoritative. | Yes - Section 5, flagged. |
| `For Review` | Out for stakeholder/CISO review. | Yes - Section 5. |
| `Approved` | Signed off and authoritative. | Yes - Section 5. |
| `Retired` | Replaced or no longer in force. Retained for audit. | Yes - appendix to Section 5. |
| `External Interface` | Artifact owned by an adjacent function (e.g., IR team). Included for cross-reference only. Not a CERG-governed document. | Yes — Section 5, flagged ⚠ |

Approval authority follows [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) Section 7:

- Policy (`POL`), CISO approves; Executive leadership endorses.
- Standard (`STD`), Governance Pillar Leader approves; CISO endorses.
- Procedure / Plan / Guideline (`PRC`, `PLN`, `GL`), Pillar Owner approves; Governance Pillar Leader endorses.
- Template (`TMPL`), Pillar Owner approves.
- Governance instrument (`GOV`), Governance Pillar Leader approves.

---


### 4.1 Review Cadence Tiers

Not all documents require the same review frequency. Documents are assigned to one of three review tiers based on their criticality and change rate:

| Tier | Review Cadence | Applies To | Review Depth |
|------|---------------|-----------|-------------|
| **Tier 1 — Critical** | Quarterly | POL-001, OM-001, RAC-001, RMF-001, CB-001, FLOW-001, CAT-001 | Full content review; verify all cross-references; confirm regulatory alignment |
| **Tier 2 — Active** | Semi-Annual | All Standards (STD-*), all Procedures (PRC-*), JA-001, CMP-001, TRN-001, MTR-001, CMX-001, TAX-001 | Content review; verify key cross-references; update metrics and framework references |
| **Tier 3 — Stable** | Annual | All Plans (PLN-*), all Templates (TMPL-*), remaining Governance documents (GOV-*), all per-role JD documents, family index documents | Light review; confirm currency; update owner if role changed; verify links |


### 4.2 CERG Source-of-Truth Model

The CERG framework defines which system is authoritative for each type of operational data. If two systems disagree, the source of truth wins.

| Data Type | Source of Truth | Notes |
|-----------|----------------|-------|
| Policy, standards, procedures, plans | CERG markdown repository | The .md files in this repo. Word/PDF exports are copies. If they disagree, the .md wins. |
| Risk register entries, exception records | GRC system or designated spreadsheet | The risk register is the single authoritative record of organizational risk. Other systems (ticketing, spreadsheets) are views into it. |
| Asset inventory | CMDB or asset management system | The authoritative inventory. If CERG asset-related content (e.g., F-03 evidence) disagrees with CMDB, investigate — do not assume either is correct. |
| Access review population, identity source | IAM platform or HRIS | Identity data comes from the IdP and HRIS. Access review evidence from CERG should reference the source population. |
| Log data | SIEM or data lake | Evidence of logging coverage comes from the SIEM, not from a policy document. |
| Audit evidence | Evidence repository (as structured per IMP-003 §8) | The evidence library is the authoritative collection. GRC records reference files in the library. |
| Control implementation status | CB-001 or GRC control catalog | Status is tracked near the control, not in a separate spreadsheet. |
| Metrics and reporting | BI dashboard or reporting tool | Dashboards are views. The canonical metric definitions are in MTR-001. |

### 4.3 Record Naming Convention

Operational records (risk register entries, exceptions, findings, etc.) use standard ID formats. These IDs are referenced in CERG artifacts and procedures.

| Record Type | ID Format | Example | Source of Truth |
|------------|-----------|---------|-----------------|
| Risk Register Entry | RISK-YYYY-NNN | RISK-2026-001 | GRC system or risk register spreadsheet |
| Exception | EXC-YYYY-NNN | EXC-2026-001 | GRC system or exception register spreadsheet |
| Finding | FIND-YYYY-NNN | FIND-2026-001 | GRC system or exposure backlog spreadsheet |
| Vulnerability | VULN-YYYY-NNN | VULN-2026-001 | GRC system or exposure backlog |
| Vendor Assessment | VEN-YYYY-NNN | VEN-2026-001 | GRC system or vendor inventory spreadsheet |
| Evidence Item | EVD-YYYY-NNN | EVD-2026-001 | Evidence library (per IMP-003 §8) |
| Incident | IR-YYYY-NNN | IR-2026-001 | IR incident tracking system |
| Decision Log Entry | DEC-YYYY-NNN | DEC-2026-001 | Decision log (per IMP-002 §4) |
| Audit Request | AUD-YYYY-NNN | AUD-2026-001 | GRC system or audit evidence package |
| Improvement Item | IMPG-YYYY-NNN | IMPG-2026-001 | Program improvement register |
| Requirement (atomic) | CERG-REQ-DOC-NNN | CERG-REQ-AC-001 | machine-readable/ requirements YAML |

### 4.4 Document Deprecation Policy

Documents in the CERG corpus follow these rules when they are retired or superseded:

- **IDs are never reused.** A retired Document ID is permanently reserved. No new document will ever receive that ID.
- **Superseding documents identify their predecessor.** When a document is replaced, the new version or replacement document states which document it supersedes.
- **The machine-readable manifest preserves history.** The manifest (cerg-manifest.yaml) retains entries for retired documents with status: Retired.
- **Breaking changes are documented.** Any change to Document IDs, statuses, role names, or workflow structures that would break cross-references is recorded in the revision history of the affected document and noted in the changelog (ROADMAP).
- **Retired documents remain in the repository.** They are not deleted. They are retained for audit trail and cross-reference integrity.
- **Retired artifacts may still be referenced** by older versions of documents. The referencing document should note the retirement in its next review cycle.

### 4.5 Ownership Delegation

The Owner field in each document's metadata assigns accountability for review initiation and content accuracy. To prevent ownership concentration, the following delegation rules apply:

- **Per-role JD documents** (CERG-GOV-JD-*): Owned by the Pillar Leader of the role's pillar, not by Governance Pillar Leader. Example: Cloud Security Engineer (SECENG-001) is owned by Engineering Pillar Leader.
- **Family index documents** (CERG-GOV-JD-*-000): Owned by the Pillar Leader of the family's primary pillar.
- **Machine-readable artifacts** (machine-readable/*.yaml): Governed collectively by METADATA.yaml. The Governance Pillar Leader (Document Control) owns the METADATA.yaml. Individual YAML files are regenerated from source — the source document owner is accountable for the content.
- **Single-owner rule:** No individual may be listed as Owner of more than 15 Tier 1 or Tier 2 documents. If a role would exceed this threshold, delegate ownership to the relevant Pillar Leader or domain expert.

Review initiation is the Owner's responsibility. If a scheduled review is missed by more than 30 days, the Document Control function creates a Finding Record and escalates to the Governance Pillar Leader.

## 5. Authoritative Catalog (V1)

The V1 library is the set below. Every artifact listed has either an approved or for-review source in the CERG content repository.

### 5.1 Policy

| **ID** | **Title** | **Owner** | **Status** |
|---|---|---|---|
| [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | Cybersecurity Policy | CISO | Approved |

### 5.2 Framework, Operating Model, and Cross-Cutting Instruments

| **ID** | **Title** | **Owner** | **Status** |
|---|---|---|---|
| [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) | CERG Operating Model | CISO / Pillar Owners | Approved |
| `CERG-GOV-CAT-001` | Document Catalog and Naming Convention | Governance Pillar Leader | Approved (this doc) |
| [`CERG-GOV-CAT-002`](CERG-GOV-CAT-002_Record_Catalog.md) | Record Catalog | Governance Pillar Leader (Document Control) | Approved |
| [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md) | Unified Control Baseline | Governance Pillar Leader | Approved |
| [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) | Metrics, Dashboard, and CISO/Board Reporting | Governance Pillar Leader | Approved |
| [`CERG-GOV-FRM-001`](CERG-GOV-FRM-001_CERG_Framework.md) | SURGE / CERG Framework (narrative) | CISO | Approved |
| [`CERG-GOV-FRM-002`](CERG-GOV-FRM-002_Framework_System_Map.md) | Framework System Map | Governance Pillar Leader | Approved |
| [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) | Risk Management Framework | Governance Pillar Leader | Approved |
| [`CERG-GOV-TAX-001`](CERG-GOV-TAX-001_Risk_Taxonomy.md) | Risk Taxonomy | Cyber Risk | Approved |
| [`CERG-GOV-CMX-001`](CERG-GOV-CMX-001_Compliance_Matrix.md) | Compliance Matrix | Governance Pillar Leader | Approved |
| [`CERG-GOV-IMP-001`](CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) | Implementation and Adaptation Guide | Governance Pillar Leader | Approved |
| [`CERG-GOV-IMP-002`](CERG-GOV-IMP-002_Adoption_Safety_Guide.md) | Adoption Safety Guide | Governance Pillar Leader | Approved |
| [`CERG-GOV-IMP-003`](CERG-GOV-IMP-003_Small_Team_Adoption_Path.md) | Small Team Adoption Path | Governance Pillar Leader | Approved |
| [`CERG-GOV-IMP-004`](CERG-GOV-IMP-004_Implementation_Cards.md) | Implementation Cards | Governance Pillar Leader | Approved |
| [`CERG-GOV-IMP-005`](CERG-GOV-IMP-005_Adoption_Decision_Tree_and_Dependency_Matrix.md) | Adoption Decision Tree and Dependency Matrix | Governance Pillar Leader | Approved |
| [`CERG-GOV-IMP-006`](CERG-GOV-IMP-006_Role_Based_Implementation_Checklists.md) | Role-Based Implementation Checklists | Governance Pillar Leader | Approved |
| [`CERG-GOV-VAR-001`](CERG-GOV-VAR-001_Organization_Adaptation_Profile.md) | Organization Adaptation Profile | Governance Pillar Leader | Approved |
| [`CERG-GOV-MAT-001`](CERG-GOV-MAT-001_Maturity_Self_Assessment_and_Scorecard.md) | Maturity Self-Assessment and Scorecard | Governance Pillar Leader | Approved |
| [`CERG-GOV-RAC-001`](CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) | Consolidated Roles, Responsibilities, and RACI Instrument | Governance Pillar Leader | Approved |
| [`CERG-GOV-CAL-001`](CERG-GOV-CAL-001_Annual_Security_and_Governance_Calendar.md) | Annual Security and Governance Calendar | Governance Pillar Leader | Approved |
| [`CERG-GOV-STY-001`](CERG-GOV-STY-001_Document_Authoring_and_Style_Guide.md) | Document Authoring and Style Guide | Governance Pillar Leader (Policy & Standards) | Approved |
| [`CERG-GOV-STY-002`](CERG-GOV-STY-002_Style_Compliance_Tracker.md) | Style Compliance Tracker | Governance Pillar Leader (Document Control) | Approved |
| [`CERG-GOV-TRC-001`](CERG-GOV-TRC-001_Control_to_Procedure_Traceability_Matrix.md) | Control-to-Procedure Traceability Matrix | Governance Pillar Leader (Control Baseline) | Approved |
| [`CERG-GOV-IMPREG-001`](CERG-GOV-IMPREG-001_Program_Improvement_Register.md) | Program Improvement Register | Governance Pillar Leader | Approved |
| [`CERG-GOV-CEF-001`](CERG-GOV-CEF-001_Control_Effectiveness_Framework.md) | Control Effectiveness Framework | Governance Pillar Leader | Approved |
| [`CERG-GOV-AUD-001`](CERG-GOV-AUD-001_Evidence_Quality_Standard.md) | Evidence Quality Standard | Governance Pillar Leader | Approved |
| [`CERG-GOV-ADR-001`](../governance/adr/ADR-001-Three-Pillars.md) | ADR-001: Three-Pillar Operating Model | Governance Pillar Leader | Approved |
| [`CERG-GOV-ADR-002`](../governance/adr/ADR-002-NIST-Spine.md) | ADR-002: NIST 800-53 as Control Spine | Governance Pillar Leader | Approved |
| [`CERG-GOV-ADR-003`](../governance/adr/ADR-003-FAIR-Risk-Statements.md) | ADR-003: FAIR-Aligned Risk Statements | Governance Pillar Leader | Approved |
| [`CERG-GOV-ADR-004`](../governance/adr/ADR-004-Overlay-Model.md) | ADR-004: Overlay Control Model | Governance Pillar Leader | Approved |
| [`CERG-GOV-ADR-005`](../governance/adr/ADR-005-Evidence-Tiers.md) | ADR-005: Evidence Tiers E1/E2/E3 | Governance Pillar Leader | Approved |
| [`CERG-GOV-ADR-006`](../governance/adr/ADR-006-Inheritance-Package.md) | ADR-006: Inheritance Evidence Package | Governance Pillar Leader | Approved |
| [`CERG-GOV-JA-001`](CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) | Job Architecture and Grade Framework | Governance Pillar Leader (Policy & Standards) | Approved |
| [`CERG-GOV-JD-001`](CERG-GOV-JD-001_CERG_Job_Descriptions.md) | CERG Job Descriptions | Governance Pillar Leader (Policy & Standards) | Approved |
| [`CERG-GOV-CMP-001`](CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md) | Competency Model and Behavioral Anchors | Governance Pillar Leader (Policy & Standards) | Approved |
| [`CERG-GOV-PERF-001`](CERG-GOV-PERF-001_Performance_Management_and_Promotion_Framework.md) | Performance Management and Promotion Framework | Governance Pillar Leader (Policy & Standards) | Approved |
| [`CERG-GOV-ONB-001`](CERG-GOV-ONB-001_Onboarding_and_Integration_Program.md) | Onboarding and Integration Program | Governance Pillar Leader (Policy & Standards) | Approved |
| [`CERG-GOV-WFP-001`](CERG-GOV-WFP-001_Workforce_Planning_and_Capacity_Model.md) | Workforce Planning and Capacity Model | Governance Pillar Leader (Policy & Standards) | Approved |
| [`CERG-GOV-TRN-001`](CERG-GOV-TRN-001_Training_Development_and_Certification_Framework.md) | Training, Development, and Certification Framework | Governance Pillar Leader (Policy & Standards) | Approved |
| [`CERG-GOV-SUCC-001`](CERG-GOV-SUCC-001_Succession_Planning_and_Talent_Review_Framework.md) | Succession Planning and Talent Review Framework | CISO | Approved |
| [`CERG-GOV-CON-001`](CERG-GOV-CON-001_Contractor_and_Non-Employee_Staff_Integration_Guide.md) | Contractor and Non-Employee Staff Integration Guide | Governance Pillar Leader (Policy & Standards) | Approved |
| [`CERG-GOV-JF-001`](../roles/CERG-GOV-JF-001_Job_Families_Overview.md) | Job Families Overview | Governance Pillar Leader (Policy & Standards) | Approved |
| [`CERG-GOV-JF-002`](../roles/CERG-GOV-JF-002_NICE_Workforce_Framework_Crosswalk.md) | NICE Workforce Framework Crosswalk | Governance Pillar Leader (Policy & Standards) | Approved |
| [`CERG-GOV-FLOW-001`](CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md) | Cross-Pillar Operational Flows | Governance Pillar Leader | Approved |
| [`CERG-GOV-EDG-001`](CERG-GOV-EDG-001_Edge_Register.md) | Edge Register | Governance Pillar Leader / Vendor Risk Analyst | Approved |
| [`CERG-GOV-CJ-001`](CERG-GOV-CJ-001_Crown_Jewel_Register_and_Scenario_Library.md) | Crown Jewel Register and Loss Scenario Library | Risk Pillar Leader / Governance Pillar Leader | Approved |
| [`CERG-GOV-SLC-001`](CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md) | CERG Service-Level Commitments | CISO | Approved |

### 5.3 Standards

| **ID** | **Title** | **Owner** | **Status** |
|---|---|---|---|
| [`CERG-STD-IT-001`](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) | IT / Cloud / SaaS Security Standard | Cyber Governance - IT/Cloud | Approved |
| [`CERG-STD-OT-001`](../standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) | Grid Control Systems Security Standard | Cyber Governance - OT | Approved |
| [`CERG-STD-CUI-001`](../standards/CERG-STD-CUI-001_CUI_Handling_Standard.md) | CUI Handling Standard | Cyber Governance - CUI/CMMC | Approved |
| [`CERG-STD-AC-001`](../standards/CERG-STD-AC-001_Access_Management_Standard.md) | Access Management Standard | Cyber Governance - Identity | Approved |
| [`CERG-STD-CFG-001`](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) | Secure Configuration Baseline Standard (DISH) | Cyber Engineering - Platforms | Approved |
| [`CERG-STD-LM-001`](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) | Logging, Monitoring, and Detection Standard | Cyber Risk - Detection | Approved |
| [`CERG-STD-RES-001`](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) | Cyber Resilience and Backup Standard | Cyber Engineering - Resilience | Approved |
| [`CERG-STD-CR-001`](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) | Cryptography and Key Management Standard | Cyber Engineering - Platforms | Approved |
| [`CERG-STD-SDL-001`](../standards/CERG-STD-SDL-001_Secure_Software_Development_and_Application_Security_Standard.md) | Secure Software Development and Application Security Standard | Cyber Engineering - Application Security | Approved |
| [`CERG-STD-AM-001`](../standards/CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md) | Asset Management and Inventory Standard | Cyber Engineering - Platforms | Approved |
| [`CERG-STD-NET-001`](../standards/CERG-STD-NET-001_Network_Security_and_Segmentation_Standard.md) | Network Security and Segmentation Standard | Cyber Engineering - Platforms | Approved |
| [`CERG-STD-EP-001`](../standards/CERG-STD-EP-001_Endpoint_and_Mobile_Security_Standard.md) | Endpoint and Mobile Security Standard | Cyber Engineering - Endpoint | Approved |
| [`CERG-STD-DG-001`](../standards/CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md) | Data Governance and Classification Standard | Cyber Governance - Policy & Standards | Approved |
| [`CERG-STD-AI-001`](../standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md) | Artificial Intelligence Security Standard | Cyber Engineering - Application Security | Approved |
| [`CERG-STD-MSG-001`](../standards/CERG-STD-MSG-001_Email_and_Messaging_Security_Standard.md) | Email and Messaging Security Standard | Cyber Engineering - Platforms | Approved |

### 5.4 Procedures

| **ID** | **Title** | **Owner** | **Status** |
|---|---|---|---|
| [`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) | Exposure Management Procedure | Cyber Risk | Approved |
| [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Risk Register and Exception Process | Cyber Governance - Risk Register | Approved |
| [`CERG-PRC-AR-001`](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) | Architecture Review and Project Intake Procedure | Cyber Engineering | Approved |
| [`CERG-PRC-AC-002`](../procedures/CERG-PRC-AC-002_Access_Management_Runbook.md) | Access Management Runbook | Identity Engineer (or IAM team if external) | Approved |
| [`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) | Third-Party and Supply Chain Risk Procedure | Cyber Risk - Vendor Risk | Approved |
| [`CERG-PRC-AV-001`](../procedures/CERG-PRC-AV-001_Adversarial_Validation_Procedure.md) | Adversarial Validation Procedure | Cyber Risk - Offensive Security | Approved |
| [`CERG-PRC-IR-002`](../procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md) | Incident Response Playbook Set ⚠ ADJACENT — owned by standing IR team; included for cross-reference only | Standing IR Team / Incident Commander | External Interface |
| [`CERG-PRC-TM-001`](../procedures/CERG-PRC-TM-001_Threat_Modeling_Procedure.md) | Threat Modeling Procedure | Cyber Risk | Approved |
| [`CERG-PRC-TI-001`](../procedures/CERG-PRC-TI-001_Threat_Intelligence_Procedure.md) | Threat Intelligence Procedure | Cyber Risk - Threat Intelligence | Approved |
| [`CERG-PRC-AUD-001`](../procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) | Audit and Evidence Management Procedure | Cyber Governance | Approved |
| [`CERG-PRC-CHG-001`](../procedures/CERG-PRC-CHG-001_Security_Change_Management_Procedure.md) | Security Change Management Procedure | Cyber Engineering | Approved |
| [`CERG-PRC-LL-001`](../procedures/CERG-PRC-LL-001_Lessons_Learned_and_Program_Improvement_Procedure.md) | Lessons Learned and Program Improvement Procedure | Governance Pillar Leader | Approved |

> **Numbering note: CERG-PRC-AC-001.** The Access Management Runbook is identifier `CERG-PRC-AC-002` rather than `-001` because the original `-001` slot was reserved for a planned standalone Access Review Runbook that has not been authored; the work was folded into the parent standard [`CERG-STD-AC-001`](../standards/CERG-STD-AC-001_Access_Management_Standard.md) §9. The `-002` ID is preserved to avoid renumbering existing references. The `-001` slot is reserved for future use.

### 5.5 Plans / Operational Packages

| **ID** | **Title** | **Owner** | **Status** |
|---|---|---|---|
| [`CERG-PLN-IR-001`](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md) | Incident Response Plan ⚠ ADJACENT — owned by standing IR team; included for cross-reference only | Standing IR Team / Incident Commander | External Interface |
| [`CERG-PLN-CUI-001`](../plans/CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md) | CUI / CMMC Operational Package | Cyber Governance - CUI/CMMC | Approved |
| [`CERG-PLN-CIP-001`](../plans/CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md) | NERC-CIP Operational Package | Cyber Governance - OT | Approved |
| [`CERG-PLN-SOX-001`](../plans/CERG-PLN-SOX-001_SOX_ITGC_Operational_Package.md) | SOX ITGC Operational Package | Cyber Governance - SOX | Approved |
| [`CERG-PLN-BC-001`](../plans/CERG-PLN-BC-001_Business_Continuity_and_Disaster_Recovery_Plan.md) | Business Continuity and Disaster Recovery Plan | Governance Pillar Leader | Approved |
| [`CERG-PLN-ISO-001`](../plans/CERG-PLN-ISO-001_ISO_IEC_27001_Operational_Package.md) | ISO/IEC 27001 Operational Package | Governance Pillar Leader | Approved |
| [`CERG-PLN-PRIV-001`](../plans/CERG-PLN-PRIV-001_Privacy_and_Data_Protection_Operational_Package.md) | Privacy and Data Protection Operational Package | Governance Pillar Leader | Approved |

### 5.6 Templates

| **ID** | **Title** | **Owner** | **Status** |
|---|---|---|---|
| [`CERG-TMPL-RM-001`](../templates/CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md) | Risk Register Templates and Reporting | Cyber Governance - Risk Register | Approved |
| [`CERG-TMPL-CUI-001`](../templates/CERG-TMPL-CUI-001_System_Security_Plan_Template.md) | System Security Plan Template | CMMC / Federal Compliance Manager | Approved |
| [`CERG-TMPL-CUI-002`](../templates/CERG-TMPL-CUI-002_POAM_Template.md) | Plan of Action and Milestones Template | CMMC / Federal Compliance Manager | Approved |
| [`CERG-TMPL-RM-002`](../templates/CERG-TMPL-RM-002_Security_Exception_Request_Form.md) | Security Exception Request Form | Risk Register Owner | Approved |
| [`CERG-TMPL-AR-001`](../templates/CERG-TMPL-AR-001_Architecture_and_Project_Intake_Form.md) | Architecture and Project Intake Form | Engineering Pillar Leader | Approved |
| [`CERG-TMPL-TPRM-001`](../templates/CERG-TMPL-TPRM-001_Vendor_Security_Questionnaire_and_Assessment_Template.md) | Vendor Security Questionnaire and TPRM Assessment Template | Vendor Risk Analyst | Approved |
| [`CERG-TMPL-RM-003`](../templates/CERG-TMPL-RM-003_Risk_Acceptance_Memo_Template.md) | Risk Acceptance Memo Template | Risk Pillar Leader | Approved |
| [`CERG-TMPL-AI-001`](../templates/CERG-TMPL-AI-001_AI_Intake_and_Sanctioning_Template.md) | AI Intake and Sanctioning Template | Governance Pillar Leader | Approved |
| [`CERG-TMPL-AI-002`](../templates/CERG-TMPL-AI-002_Sanctioned_AI_Tools_Register_Template.md) | Sanctioned AI Tools Register Template | Governance Pillar Leader | Approved |
| [`CERG-TMPL-AI-003`](../templates/CERG-TMPL-AI-003_AI_System_and_Model_Register_Template.md) | AI System and Model Register Template | Application Security Engineer | Approved |
| [`CERG-TMPL-AUD-001`](../templates/CERG-TMPL-AUD-001_Control_Evidence_and_Test_Worksheet.md) | Control Evidence and Test Worksheet | Evidence Librarian | Approved |
| [`CERG-TMPL-MTR-001`](../templates/CERG-TMPL-MTR-001_Board_and_CISO_Reporting_Deck_Template.md) | Board and CISO Reporting Deck Template | Governance Pillar Leader | Approved |
| [`CERG-TMPL-GOV-001`](../templates/CERG-TMPL-GOV-001_Stakeholder_Perception_Survey.md) | Stakeholder Perception Survey | Governance Pillar Leader | Approved |

| [`CERG-TMPL-SAAS-001`](../templates/CERG-TMPL-SAAS-001_SaaS_Evidence_Collection_Checklist.md) | SaaS Evidence Collection Checklist | Governance Pillar Leader | Approved |
| [`CERG-TMPL-SBOM-001`](../templates/CERG-TMPL-SBOM-001_SBOM_Evidence_Collection_Checklist.md) | SBOM Evidence Collection Checklist | Vendor Risk Analyst | Approved |
Other templates remain embedded as appendices of their parent procedure or plan unless they have independent reuse outside that artifact. The Document Catalog references the parent.

---


### 5.7 Job Descriptions (Per-Role)

| **ID** | **Title** | **Owner** | **Status** |
|---|---|---|---|
| `CERG-GOV-JD-SECENG-001` | Cloud Security Engineer | Engineering Pillar Leader | Approved |
| `CERG-GOV-JD-SECENG-002` | Identity Engineer | Engineering Pillar Leader | Approved |
| `CERG-GOV-JD-SECENG-003` | OT Security Engineer | Engineering Pillar Leader | Approved |
| `CERG-GOV-JD-SECENG-004` | Application Security Engineer | Engineering Pillar Leader | Approved |
| `CERG-GOV-JD-SECENG-005` | Endpoint Engineer | Engineering Pillar Leader | Approved |
| `CERG-GOV-JD-SECENG-006` | Cryptography Engineer | Engineering Pillar Leader | Approved |
| `CERG-GOV-JD-SECENG-007` | Engineering Pillar Leader | Engineering Pillar Leader | Approved |
| `CERG-GOV-JD-SECENG-008` | Pre-production Reviewer | Engineering Pillar Leader | Approved |
| `CERG-GOV-JD-RISKOPS-001` | Exposure Management Lead | Risk Pillar Leader | Approved |
| `CERG-GOV-JD-RISKOPS-002` | Adversarial Testing Lead | Risk Pillar Leader | Approved |
| `CERG-GOV-JD-RISKOPS-003` | Threat Intelligence Analyst | Risk Pillar Leader | Approved |
| `CERG-GOV-JD-RISKOPS-004` | Detection Engineer | Risk Pillar Leader | Approved |
| `CERG-GOV-JD-RISKOPS-005` | OT Risk Analyst | Risk Pillar Leader | Approved |
| `CERG-GOV-JD-RISKOPS-006` | Identity Risk Analyst | Risk Pillar Leader | Approved |
| `CERG-GOV-JD-RISKOPS-007` | Vendor Risk Analyst | Risk Pillar Leader | Approved |
| `CERG-GOV-JD-RISKOPS-008` | Risk Pillar Leader | Risk Pillar Leader | Approved |
| `CERG-GOV-JD-GOVCOMP-001` | NERC-CIP Compliance Manager | Governance Pillar Leader | Approved |
| `CERG-GOV-JD-GOVCOMP-002` | CMMC / Federal Compliance Manager | Governance Pillar Leader | Approved |
| `CERG-GOV-JD-GOVCOMP-003` | SOX ITGC Lead | Governance Pillar Leader | Approved |
| `CERG-GOV-JD-GOVCOMP-004` | Policy & Standards Manager | Governance Pillar Leader | Approved |
| `CERG-GOV-JD-GOVCOMP-005` | Risk Register Owner | Governance Pillar Leader | Approved |
| `CERG-GOV-JD-GOVCOMP-006` | Evidence Librarian | Governance Pillar Leader | Approved |
| `CERG-GOV-JD-GOVCOMP-007` | Governance Pillar Leader | Governance Pillar Leader | Approved |
| `CERG-GOV-JD-EXEC-001` | Chief Information Security Officer (CISO) | CISO | Approved |
| `CERG-GOV-JD-EXEC-002` | Executive Sponsor | CISO | Approved |
| `CERG-GOV-JD-ADJUNCT-001` | Incident Commander | Governance Pillar Leader | Approved |
| `CERG-GOV-JD-ADJUNCT-002` | Lead Investigator | Governance Pillar Leader | Approved |
| `CERG-GOV-JD-SECENG-000` | Security Engineering Family Index | Engineering Pillar Leader | Approved |
| `CERG-GOV-JD-RISKOPS-000` | Risk Operations Family Index | Risk Pillar Leader | Approved |
| `CERG-GOV-JD-GOVCOMP-000` | Governance & Compliance Family Index | Governance Pillar Leader | Approved |
| `CERG-GOV-JD-EXEC-000` | Executive Leadership Family Index | CISO | Approved |
| `CERG-GOV-JD-ADJUNCT-000` | Incident Response Family Index | Governance Pillar Leader | Approved |

### 5.8 Machine-Readable Artifacts

The `machine-readable/` directory contains YAML specifications generated from the CERG corpus for LLM and automation consumption. These are derived artifacts, not independently authored documents. See `machine-readable/README.md` for the complete inventory.

Key artifacts include:
- `cerg-llm-index.json` — Full local Markdown corpus index for LLM/agent consumption
- `cerg-manifest.yaml` — Canonical manifest of governed source artifacts
- `cerg-publication-manifest.yaml` — Publication eligibility separate from lifecycle approval status
- `cerg-requirements.yaml` — Pilot atomic requirements extracted from 8 normative source documents
- `cerg-flows.yaml` — Cross-pillar operational flow specifications (7 flows)
- `cerg-record-schemas.yaml` — Core operational record schemas
- Companion schema files for runtime model, evidence, metrics, crown jewels, vulnerability priority, IR interface, vendor kill switch, identity, segmentation, AI intake, workforce capacity, and decision logging

## 6. Cross-Reference Rules

These rules govern every "Related Documents" table, every footnote reference, and every link in a CERG artifact.

1. **Link only to artifacts that appear in this catalog.** If the artifact does not appear in Section 5 or Section 7, do not reference it.
2. **Distinguish approved from planned.** When a Related Documents table includes a Planned artifact, mark it `(Planned, V1.x)` or `(Planned, V2)` so the reader knows it does not yet exist.
3. **Use the Document ID, not the file name.** File names change; IDs do not.
4. **Avoid forward references to TMPL artifacts that live inside a parent.** Cite the parent and the appendix (`CERG-PRC-AR-001 Appendix B, Security Project Intake Form`).
5. **External standards (NIST, CIS, IEC, ISO) are cited by short form**, `NIST 800-53r5 AC-2`, `CIS Benchmark Windows Server 2022 L1`, `IEC 62443-3-3 SR 1.1`. Each artifact's metadata table lists the framework set in scope.

> **The Reference Discipline Test**
>
> A new CERG team member opens any artifact, follows a reference, and arrives at exactly the document the reference named, at the version the catalog records, with no dead links and no surprises. If that holds for every reference in the library, the catalog is doing its job. If it does not, the catalog, not the citing document, is the artifact that needs the fix.

---

## 7. Artifact Roadmap (V1.x to V2)

This section is the authoritative list of planned artifacts. Per Cross-Reference Rule 1, a planned artifact may be referenced by another artifact only if it appears here, and the reference is marked `(Planned, V1.x)` or `(Planned, V2)`.

An artifact moves from this section to Section 5 when it is authored and reaches `Draft` or above. An artifact in this section has an ID reserved and an owner assigned but is not yet authoritative and must not be relied upon.

### 7.1 Status of the V1.x Build

The V1.x build extends the original V1 library along six tracks: the adoption layer, the Engineering-pillar standards, the governance glue, the missing procedures, the missing operational packages, and the standalone template library. As of this version of the catalog, the adoption layer (`IMP`, `VAR`, `MAT`), the seven Engineering and data standards (`SDL`, `AM`, `NET`, `EP`, `DG`, `AI`, `MSG`), the consolidated RACI instrument (`RAC`), the Group C in-scope procedures (`IR-002`, `TM`, `TI`, `AUD`, `CHG`), the Group D operational packages (`BC`, `ISO`, `PRIV`), the Group E standalone templates, and the F2-F4 governance instruments (`CAL`, `STY`, `TRC`) are authored and registered in Section 5. The artifacts below remain planned.

### 7.2 Planned Procedures


| [`CERG-PRC-AC-001`]() | Access Review Runbook (reserved) | Identity Engineer | Planned, V1.x |

No in-scope Group C procedures remain planned in V1.x. Security Awareness and Training and SOC / Forensics operations are intentionally out of CERG scope and are not reserved here.

### 7.3 Planned Plans and Operational Packages

No Group D operational packages remain planned. Business Continuity and Disaster Recovery, ISO/IEC 27001, and Privacy and Data Protection packages are authored and registered in Section 5.5.

### 7.4 Planned Templates

No Group E standalone templates remain planned. The System Security Plan, POA&M, security exception request, architecture and project intake form, vendor security questionnaire, risk acceptance memo, control evidence worksheet, and Board / CISO reporting deck templates are authored and registered in Section 5.6.

The incident report and post-incident review template remains embedded in the incident response plan and playbook set unless promoted by a future amendment.

### 7.5 Planned Governance Instruments


| [`CERG-GOV-CIP-001`]() | NERC-CIP Governance Instrument (reserved) | OT Security Engineer | Planned, V1.x |
| [`CERG-GL-OT-001`]() | OT Security Guideline (reserved) | OT Security Engineer | Planned, V1.x |
| [`CERG-TMPL-CIP-001`]() | NERC-CIP Template (reserved) | NERC-CIP Compliance Manager | Planned, V1.x |

No F2-F4 governance instruments remain planned. The Annual Security and Governance Calendar, Document Authoring and Style Guide, and Control-to-Procedure Traceability Matrix are authored and registered in Section 5.2.

> **The Roadmap Is a Commitment, Not a Wishlist**
>
> An ID in this section is a reserved identifier with a named owner. It is not a vague intention. When an artifact is listed here, a citing document is permitted to forward-reference it, which means readers will encounter the reference before the artifact exists. That is only safe if this section is honest: every entry has a real owner and a real target, and an entry that is no longer intended is removed by amendment, not left to mislead.

---

## 8. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-CAT-001 |
| **Version** | 1.40 |
| **Status** | Approved |
| **Effective Date** | 2026-06-17 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Document Control) |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Quarterly, or upon any artifact add or retire |
| **Next Scheduled Review** | 2026-09-17 |
| **Frameworks** | NIST CSF 2.0 (GOVERN); ISO/IEC 27001 A.5 |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed documentation |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.40 | 2026-06-17 | Governance Pillar Leader | Reconciled concurrent catalog revision history and updated the next scheduled review date after AI and SaaS/SBOM additions. |
| 1.39 | 2026-06-17 | Governance Pillar Leader | Removed the hardcoded machine-readable manifest artifact count so the catalog does not drift when templates are added. |
| 1.38 | 2026-06-17 | Governance Pillar Leader | Registered CERG-TMPL-AI-003 as the AI system and model register template. |
| 1.37 | 2026-06-17 | Governance Pillar Leader | Registered CERG-TMPL-AI-002 as the sanctioned AI tools register template. |
| 1.36 | 2026-06-17 | Governance Pillar Leader | Registered CERG-TMPL-AI-001 as the standalone AI intake and sanctioning template. |
| 1.35 | 2026-06-14 | Governance Pillar Leader | Removed duplicate Table of Contents entries after the machine-readable artifact update. |
| 1.34 | 2026-06-14 | Governance Pillar Leader | Updated machine-readable artifact inventory language to reflect regenerated local manifests, canonical paths, and the full LLM index. |
| 1.33 | 2026-06-14 | Governance Pillar Leader | Status taxonomy cleanup. Replaced Published and Active catalog statuses with Approved; publication eligibility remains tracked separately in the publication manifest. |
| 1.32 | 2026-06-13 | Governance Pillar Leader | Adoption usability amendment. Added FRM-002 Framework System Map, CAT-002 Record Catalog, IMP-005 Adoption Decision Tree and Dependency Matrix, and IMP-006 Role-Based Implementation Checklists to Section 5.2. |
| 1.0 | 2026-05-01 | Cyber Governance | Initial release. Established the naming convention, document types, the authority and status lifecycle, the V1 authoritative catalog, and the cross-reference rules. |
| 1.21 | 2026-05-01 | Cyber Governance | Catalog maintenance release aligning artifact versions across the V1 library. |
| 1.22 | 2026-05-21 | Cyber Governance | Registered the adoption-layer domains `IMP`, `VAR`, and `MAT` in Section 2.1 and added `CERG-GOV-IMP-001`, `CERG-GOV-VAR-001`, and `CERG-GOV-MAT-001` to Section 5.2. |
| 1.23 | 2026-05-21 | Cyber Governance | Registered domains `RAC`, `SDL`, `AM`, `NET`, `EP`, `DG`, `AI`, and `MSG`. Added `CERG-GOV-RAC-001` to Section 5.2 and seven standards to Section 5.3. Set `CERG-GOV-RAC-001` and the seven new standards to `Approved` on CISO sign-off. Restored the document to its full structure: completed the Section 6 Reference Discipline Test callout, and authored Section 7 (Artifact Roadmap) and Section 8 (Document Control), which had been absent. |
| 1.24 | 2026-05-22 | Cyber Governance | Registered domains `TM`, `TI`, `AUD`, and `CHG`; added `CERG-PRC-IR-002`, `CERG-PRC-TM-001`, `CERG-PRC-TI-001`, `CERG-PRC-AUD-001`, and `CERG-PRC-CHG-001` to Section 5.4 as Draft; removed the now-authored Group C procedure reservations from Section 7.2; noted that Security Awareness and Training and SOC / Forensics operations are intentionally out of CERG scope. |
| 1.25 | 2026-05-22 | Cyber Governance | Registered domains `BC`, `ISO`, and `PRIV`; added `CERG-PLN-BC-001`, `CERG-PLN-ISO-001`, and `CERG-PLN-PRIV-001` to Section 5.5 as Draft; removed the now-authored Group D operational package reservations from Section 7.3. |
| 1.26 | 2026-05-22 | Cyber Governance | Added eight standalone Group E templates to Section 5.6 as Draft: `CERG-TMPL-CUI-001`, `CERG-TMPL-CUI-002`, `CERG-TMPL-RM-002`, `CERG-TMPL-AR-001`, `CERG-TMPL-TPRM-001`, `CERG-TMPL-RM-003`, `CERG-TMPL-AUD-001`, and `CERG-TMPL-MTR-001`; updated Section 7.4 to state that no Group E standalone templates remain planned. |
| 1.27 | 2026-05-22 | Cyber Governance | Registered domains `CAL`, `STY`, and `TRC`; added `CERG-GOV-CAL-001`, `CERG-GOV-STY-001`, and `CERG-GOV-TRC-001` to Section 5.2 as Draft; updated Section 7.5 to state that no F2-F4 governance instruments remain planned. |
| 1.30 | 2026-05-27 | Cyber Governance | HR program build-out amendment. Registered domains `CMP`, `PERF`, `ONB`, `WFP`, `TRN`, `SUCC`, `CON`, and `EDG`. Added to Section 5.2: `CERG-GOV-CMP-001` (Competency Model and Behavioral Anchors), `CERG-GOV-PERF-001` (Performance Management and Promotion Framework), `CERG-GOV-ONB-001` (Onboarding and Integration Program), `CERG-GOV-WFP-001` (Workforce Planning and Capacity Model), `CERG-GOV-TRN-001` (Training, Development, and Certification Framework), `CERG-GOV-SUCC-001` (Succession Planning and Talent Review Framework), and `CERG-GOV-CON-001` (Contractor and Non-Employee Staff Integration Guide). Extended `CERG-GOV-IMP-001` to v1.1 with Employer Brand and Talent Attraction section. |
| 1.31 | 2026-06-11 | Governance Pillar Leader | Workforce architecture and cross-pillar flows amendment. Registered domains `JF` and `FLOW`. Added JF-001 (Job Families Overview), JF-002 (NICE Crosswalk), and FLOW-001 (Cross-Pillar Operational Flows) to §5.2. Added §5.7 (Job Descriptions — 27 per-role documents across five job families) and §5.8 (Machine-Readable Artifacts). Rewrote JD-001 as family-level index. Modified RAC-001, JA-001, CMP-001, TRN-001, PERF-001, and OM-001 with NICE and Job Family cross-references. |
| 1.29 | 2026-05-27 | Cyber Governance | Job architecture and human capital amendment. Registered domains `JA` and `JD`. Added to Section 5.2: `CERG-GOV-JA-001` (Job Architecture and Grade Framework) and `CERG-GOV-JD-001` (CERG Job Descriptions). The JA-001 establishes the two-track grade structure (SME: Specialist through Sr. Advisor; Management: Manager through Director), leveling dimensions, span-of-control guidelines, and compensation philosophy. The JD-001 provides full job descriptions for all 25 canonical CERG roles. |
| 1.28 | 2026-05-26 | Cyber Governance | NIST CSF Adaptive gap closure amendment. Registered domains `LL`, `IMPREG`, and `CEF`. Added to Section 5.2: `CERG-GOV-IMPREG-001` (Program Improvement Register) and `CERG-GOV-CEF-001` (Control Effectiveness Framework). Added to Section 5.4: `CERG-PRC-LL-001` (Lessons Learned and Program Improvement Procedure). Added to Section 5.6: `CERG-TMPL-GOV-001` (Stakeholder Perception Survey). Noted extended artifacts: PRC-TI-001 v1.1, MTR-001 v1.3, PRC-AV-001 v1.2, RMF-001 v1.3, MAT-001 v1.1, OM-001 v1.22. |

### Review Triggers

- Any artifact added to, or retired from, the CERG library
- Any new domain or type code required by a new artifact
- A change to the naming convention or the cross-reference rules
- A planned artifact in Section 7 reaching `Draft` or above, which moves it to Section 5
- Direction from the CISO

Governance owns this document. The Governance Pillar Leader (Document Control) is responsible for initiating reviews, managing the revision cycle, and obtaining approval for all changes.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | Parent policy; establishes the document hierarchy this catalog inventories |
| CERG Operating Model | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) | Defines the roles cited as artifact owners |
| Consolidated Roles, Responsibilities, and RACI Instrument | [`CERG-GOV-RAC-001`](CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) | Master RACI for ownership of every artifact in this catalog |
| Implementation and Adaptation Guide | [`CERG-GOV-IMP-001`](CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) | Adoption sequencing; instructs adopters to keep this catalog current | 
