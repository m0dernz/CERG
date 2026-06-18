# SURGE: Cyber Engineering, Risk & Governance

## ADOPTION DECISION TREE AND DEPENDENCY MATRIX
### Scope Selection · Safe Tailoring · Required Companion Artifacts

---

| | |
|---|---|
| **Document ID** | CERG-GOV-IMP-005 |
| **Version** | 1.02 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Quarterly / Upon adoption path or catalog change |
| **Frameworks** | NIST CSF 2.0 (GOVERN) |
| **Regulations** | NERC-CIP · CMMC L2 · SOX ITGC · ISO/IEC 27001 |
| **Environments** | All CERG adoption paths |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Adoption Decision Tree](#2-adoption-decision-tree)
3. [Safe Tailoring Rules](#3-safe-tailoring-rules)
4. [Dependency Matrix](#4-dependency-matrix)
5. [Required, Conditional, Recommended, and Example Labels](#5-required-conditional-recommended-and-example-labels)
6. [Adoption Gates](#6-adoption-gates)
7. [Document Control](#7-document-control)

---

## 1. Purpose and Scope

CERG is modular, but it is not arbitrary. Some artifacts can be deferred safely. Others must travel together because they form an operating loop.

This document helps an adopter decide:

- Which CERG path applies.
- Which documents are required immediately.
- Which documents are conditional on regulatory or environmental scope.
- Which artifacts must be adopted together.
- Which tailoring choices are safe.
- Which tailoring choices break the model.

---

## 2. Adoption Decision Tree

### 2.1 Readiness gate

Before adopting CERG, answer these questions:

| Question | If no |
|---|---|
| Is there a named person accountable for security? | Do not adopt CERG yet. Establish ownership first. |
| Does leadership support guardrails, decisions, and evidence, not only tooling? | Use NIST CSF or CIS Controls until sponsorship exists. |
| Can the organization name its systems, business units, and regulators? | Complete basic scoping before adopting documents. |
| Will the organization track versions, decisions, records, and evidence? | CERG will become shelfware. Fix evidence discipline first. |

If all answers are yes, continue.

### 2.2 Path selection

```text
Security team size 2-8 people?
  yes -> CERG Lite
  no -> continue

One-person security function?
  yes -> use CERG as a planning reference; adopt MVC only after an Executive Sponsor and independent High/Critical risk approver are named
  no -> continue

Existing security team with multiple functions but limited formal governance?
  yes -> CERG Standard
  no -> continue

Regulatory obligation or OT/CUI/SOX scope exists?
  yes -> CERG Regulated overlay on Lite or Standard
  no -> CERG Standard
```

### 2.3 Regulatory overlay selector

| Question | If yes, add |
|---|---|
| Do you handle CUI or FCI for federal contracts? | CUI standard, CUI/CMMC operational package, SSP, POA&M, CUI evidence matrix |
| Are you subject to NERC-CIP or responsible for BES Cyber Systems? | OT standard, NERC-CIP operational package, access, logging, segmentation, recovery evidence |
| Are systems in scope for SOX financial reporting? | SOX ITGC operational package, access/change/evidence procedures, SOX system register |
| Are you pursuing ISO/IEC 27001 certification or readiness? | ISO operational package, ISMS scope, statement of applicability support, management review records |
| Do privacy or data protection obligations apply? | Data governance standard, privacy operational package, security support records |
| Do you build or operate customer-facing software? | Secure SDLC standard, threat modeling procedure, architecture intake, vulnerability disclosure considerations |
| Do you operate OT but not NERC-CIP? | OT standard, network segmentation standard, incident/recovery plan, OT-safe evidence and testing |
| Do you use AI tools, AI-enabled SaaS, or build AI features? | AI security standard, data governance standard, vendor risk assessment updates, AI intake template, sanctioned AI tools register, AI system/model register where built or embedded AI exists |

---

## 3. Safe Tailoring Rules

### 3.1 Safe tailoring

These changes are acceptable when documented in the Organization Adaptation Profile:

- Combine multiple CERG roles into one person in a small team.
- Use spreadsheets instead of a GRC platform.
- Rename roles to match local job titles while preserving CERG accountability.
- Defer standards for environments that do not exist.
- Adopt only the core standards needed for current scope.
- Use manual evidence collection before automation exists.
- Use a lightweight Cyber Oversight Group if the executive team is small.
- Store records in ticketing systems when required fields are preserved.

### 3.2 Unsafe tailoring

These changes break the model:

- Deleting the risk register.
- Treating security exceptions as informal approvals.
- Allowing Engineering to accept high risk without business or CISO authority.
- Claiming regulatory alignment without the required operational package and evidence.
- Marking controls implemented without evidence.
- Adopting standards but not procedures or records.
- Running vulnerability scans without asset ownership, remediation SLAs, or exception handling.
- Treating vendor security review as optional for systems that handle sensitive data, privileged access, or regulated scope.
- Removing document control, version history, or approval status.

---

## 4. Dependency Matrix

### 4.1 Core dependencies

| If adopting | Also adopt | Why |
|---|---|---|
| Cybersecurity Policy | Framework, Operating Model | Policy needs an operating structure. |
| CERG Framework | Operating Model, RMF | The conceptual model needs roles and risk mechanics. |
| Operating Model | RACI Instrument, Cross-Pillar Flows | Roles need decision rights and handoffs. |
| RMF | Risk Register Procedure, Risk Register Templates | Risk model needs executable records. |
| Unified Control Baseline | Evidence Quality Standard, Control-to-Procedure Traceability Matrix | Controls need evidence and procedures. |
| Metrics and Reporting | Record Catalog, Evidence Quality Standard | Metrics must be reproducible from records. |
| Maturity Assessment | Program Improvement Register | Gaps must become owned improvement work. |

### 4.2 Procedure dependencies

| If adopting | Also adopt | Why |
|---|---|---|
| Exposure Management Procedure | Asset Standard, RMF, Risk Register Procedure | Findings need assets, scoring, ownership, treatment, and exceptions. |
| Architecture Review Procedure | Architecture Intake Template, Threat Modeling Procedure, Flow F-02 | Reviews need intake data, threat reasoning, and disposition records. |
| Third-Party Risk Procedure | Vendor Questionnaire, Edge Register, Data Governance Standard | Vendor risk depends on data, access, external control, and assessment evidence. |
| Security Change Management Procedure | Configuration Standard, Architecture Review Procedure | Changes need baseline impact and review routing. |
| Audit and Evidence Procedure | Evidence Quality Standard, Control Baseline, Record Catalog | Audit response needs evidence criteria, control mapping, and source records. |
| Lessons Learned Procedure | Program Improvement Register, Incident Response Plan | Lessons must become tracked improvements. |
| Threat Intelligence Procedure | Logging and Detection Standard, Adversarial Validation Procedure | Intelligence should drive detection and validation priorities. |
| Threat Modeling Procedure | Architecture Review Procedure, Secure SDLC Standard | Threat modeling needs project context and design-stage action. |

### 4.3 Standard dependencies

| If adopting | Also adopt | Why |
|---|---|---|
| Access Standard | Access Runbook, Evidence Quality Standard, Metrics | Access controls require operational review and evidence. |
| Asset Standard | Asset Coverage flow, Exposure Management Procedure | Asset data feeds scanning, logging, backup, and ownership. |
| IT / Cloud / SaaS Standard | Architecture Review, TPRM, Access, Logging, Configuration | Cloud/SaaS risk crosses identity, vendor, logging, and baseline control. |
| OT Standard | NERC-CIP package if applicable, Network, Access, Logging, Resilience | OT security depends on segmentation, privileged access, visibility, and recovery. |
| CUI Standard | CUI Operational Package, SSP, POA&M, Access, Configuration, Logging | CUI compliance requires boundary, control, and remediation evidence. |
| Logging and Detection Standard | Threat Intelligence, Adversarial Validation, Incident Response | Detection must be threat-informed, tested, and usable in response. |
| Secure SDLC Standard | Architecture Review, Threat Modeling, Exposure Management | Application security requires design, build, test, and finding workflows. |
| AI Security Standard | Data Governance, TPRM, Secure SDLC, Access, AI Intake, Sanctioned AI Tools Register, AI System/Model Register where applicable | AI risk includes data, vendor features, product development, privilege, sanctioned-use decisions, and model inventory. |
| Resilience and Backup Standard | BCDR Plan, Incident Response Plan, Asset Coverage | Recovery controls need scope, tests, and incident integration. |

### 4.4 Regulated package dependencies

| If adopting | Also adopt | Why |
|---|---|---|
| CUI / CMMC Package | CUI Standard, SSP, POA&M, Evidence Quality, Access, Asset, Config, Logging | Assessment readiness requires system boundary, controls, gaps, and evidence. |
| NERC-CIP Package | OT Standard, Access, Logging, Network, Incident, Recovery | CIP evidence depends on OT control operation and documented records. |
| SOX ITGC Package | Access, Change, Evidence, Asset/System Register | SOX control testing needs population, access/change records, and evidence. |
| ISO Package | Control Baseline, Metrics, Maturity, Evidence, Improvement | ISMS operation requires scope, controls, monitoring, management review, and improvement. |
| Privacy Package | Data Governance, TPRM, Access, Incident Response | Privacy support depends on data classification, vendors, access, and incident coordination. |

---

## 5. Required, Conditional, Recommended, and Example Labels

CERG adopters should label adopted artifacts in their local catalog using these values.

| Label | Meaning |
|---|---|
| Required-Core | Required for every CERG implementation. |
| Required-Path | Required for the selected adoption path. |
| Conditional-Regulatory | Required only when a regulator, contract, or certification applies. |
| Conditional-Environment | Required only when the environment exists, such as OT, cloud, SaaS, or AI. |
| Recommended | Useful but deferrable without breaking the operating model. |
| Example | Illustrative only. Not a requirement until adopted locally. |
| Deferred | Not currently adopted. Deferral rationale must be recorded. |
| Not Applicable | Does not apply to the organization. Basis must be recorded. |

### 5.1 Preliminary default labels

| Artifact group | Default label |
|---|---|
| Policy, Framework, Operating Model, RMF, Catalog, Risk Register, Exposure Management | Required-Core |
| Record Catalog, Framework System Map, Role-Based Checklists, Decision Tree | Recommended for all, Required-Path for first adoption projects |
| Access, Asset, Configuration, IT/Cloud where applicable, Logging, Resilience | Required-Path for Standard and Regulated |
| Cryptography and Key Management | Recommended for Standard; Required-Path where managed keys, certificates, encryption controls, CUI, OT, SOX, or other regulated scope applies |
| OT, CUI, SOX, ISO, Privacy packages | Conditional-Regulatory or Conditional-Environment |
| AI standard and AI operational templates | Conditional-Environment when AI tools, AI-enabled SaaS, embedded AI, or built AI exists |
| Workforce architecture documents | Recommended for Standard, Required-Path for large teams or formal hiring model |
| Example profiles | Example |

---

## 6. Adoption Gates

### Gate 0: Not Ready

The organization has no named owner, no executive support, unclear scope, or no willingness to maintain records.

Exit criteria:

- Security owner named.
- Executive sponsor identified.
- Scope and regulators listed.
- Decision made to maintain records and evidence.

### Gate 1: Spine Adopted

The organization has adopted the core CERG spine.

Exit criteria:

- Policy signed.
- Organization Adaptation Profile completed.
- Role Assignment Map completed.
- Initial risk register created.
- Initial exposure backlog created.
- Document catalog updated.

### Gate 2: Operating

The organization is producing recurring security work from the MVC spine.

Exit criteria:

- At least two recurring risk register reviews completed, including recorded decisions, owners, and next actions.
- Exposure or vulnerability management cycle running with SLA metrics produced for at least two cycles.
- Risk exceptions and acceptances follow [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md), with no informal high-risk approvals.
- Project intake or architecture review path exists, and at least one disposition has been issued. If no real project occurred, a tabletop review with a documented disposition is acceptable.
- Asset inventory has owners for the assets in the initial exposure scope.
- Evidence index exists and links risk, exposure, ownership, exception, and decision records.
- First metrics report produced and reviewed by the CISO or equivalent security owner.
- Each pillar has produced at least one operating record. In small teams, this means the Engineering, Risk, and Governance accountabilities are evidenced even if one person holds multiple roles.

### Gate 2 to Gate 3 Transition Test

The organization should not start broad standard-layer adoption until Gate 2 is stable. Gate 3 adoption begins when the CISO or equivalent security owner records that all of the following are true:

| **Condition** | **Minimum Evidence** |
|---|---|
| Risk cadence is real | Two completed risk register reviews, or three where monthly cadence is already established. |
| Exposure cadence is measurable | Two exposure or vulnerability cycles with SLA performance, backlog trend, and exception handling visible. |
| Intake path works | One architecture or project intake disposition, or a tabletop disposition if no qualifying project occurred. |
| Evidence can be found | Evidence index links the MVC records needed to explain risk, exposure, ownership, decisions, and exceptions. |
| Pillars are operating | Engineering, Risk, and Governance have each produced at least one record or decision in their accountability area. |
| Adoption plan exists | Standard-layer adoption plan identifies which core standards, procedures, and overlays are next, with owners and target dates. |

If any condition is missing, remain at Gate 2 and fix the operating loop before adopting additional documents. Gate 3 is triggered by evidence that the MVC runs, not by the calendar reaching day 60 or day 90.

### Gate 3: Governed

The organization can explain and evidence its control posture.

Exit criteria:

- Control baseline status recorded.
- Core standards adopted.
- Evidence quality checks applied.
- Cyber Oversight Group or equivalent meets on cadence.
- Program improvement register active.

### Gate 4: Adaptive

The organization improves based on evidence, threats, incidents, metrics, and maturity results.

Exit criteria:

- Control effectiveness tested.
- Threat intelligence changes detection or priorities.
- Lessons learned produce control or procedure updates.
- Maturity assessment drives roadmap.
- Board or executive reporting influences risk and resourcing decisions.

---

## 7. Document Control

| | |
|---|---|
| **Document ID** | CERG-GOV-IMP-005 |
| **Version** | 1.02 |
| **Status** | Approved |
| **Approved By** | CISO |
| **Owner** | Governance Pillar Leader |
| **Next Review** | Quarterly / Upon adoption path or catalog change |

### Revision History

| **Version** | **Date** | **Author** | **Change** |
|---|---|---|---|
| 1.02 | 2026-06-17 | Governance Pillar Leader | Added AI operational templates and registers to adoption selector, dependency matrix, and default labels. |
| 1.01 | 2026-06-14 | Governance Pillar Leader | Aligned Lite path sizing and core-standard labels with README, START-HERE, IMP-001, and IMP-003. |
| 1.0 | 2026-06-13 | Governance Pillar Leader | Initial publication. Adds adoption decision tree, safe tailoring rules, dependency matrix, artifact labels, and adoption gates. |

### Review Triggers

- New adoption path.
- New regulated operational package.
- New core standard or procedure dependency.
- User feedback indicating over-adoption or unsafe tailoring.
- Catalog change affecting document IDs or status.

### Related Documents

- [START-HERE](../START-HERE.md) - First 48 hours guide
- [CERG-GOV-IMP-001](CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) - Implementation and Adaptation Guide
- [CERG-GOV-IMP-002](CERG-GOV-IMP-002_Adoption_Safety_Guide.md) - Adoption Safety Guide
- [CERG-GOV-IMP-003](CERG-GOV-IMP-003_Small_Team_Adoption_Path.md) - Small Team Adoption Path
- [CERG-GOV-VAR-001](CERG-GOV-VAR-001_Organization_Adaptation_Profile.md) - Organization Adaptation Profile
- [CERG-GOV-CAT-002](CERG-GOV-CAT-002_Record_Catalog.md) - Record Catalog
- [CERG-STD-AI-001](../standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md) - Artificial Intelligence Security Standard
- [CERG-TMPL-AI-001](../templates/CERG-TMPL-AI-001_AI_Intake_and_Sanctioning_Template.md) - AI Intake and Sanctioning Template
- [CERG-TMPL-AI-002](../templates/CERG-TMPL-AI-002_Sanctioned_AI_Tools_Register_Template.md) - Sanctioned AI Tools Register Template
- [CERG-TMPL-AI-003](../templates/CERG-TMPL-AI-003_AI_System_and_Model_Register_Template.md) - AI System and Model Register Template
