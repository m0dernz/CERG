# SURGE: Cyber Engineering, Risk & Governance

## FRAMEWORK SYSTEM MAP
### Front Door · Document Relationships · Adoption Navigation

---

| | |
|---|---|
| **Document ID** | CERG-GOV-FRM-002 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Quarterly / Upon significant library structure change |
| **Frameworks** | NIST CSF 2.0 (GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER) |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG adoption paths |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [The CERG Spine](#2-the-cerg-spine)
3. [How the Library Fits Together](#3-how-the-library-fits-together)
4. [How Work Moves Through CERG](#4-how-work-moves-through-cerg)
5. [Navigation by User Need](#5-navigation-by-user-need)
6. [Navigation by Adoption Path](#6-navigation-by-adoption-path)
7. [Navigation by Pillar](#7-navigation-by-pillar)
8. [Document Control](#8-document-control)

---

## 1. Purpose and Scope

CERG is intentionally complete. That completeness can make the first hour difficult for a new reader. This document is the map.

It explains how the policy, framework, operating model, risk model, controls, standards, procedures, templates, records, evidence, metrics, and improvement loops relate to one another. It does not replace those documents. It tells the reader which document to open next and why.

Use this document when:

- A leader asks, "What is CERG?"
- A new adopter asks, "Where do I start?"
- A practitioner asks, "Which artifact owns this activity?"
- A contributor asks, "Where does a proposed document belong?"
- An auditor asks, "How do policy statements become evidence?"

---

## 2. The CERG Spine

The CERG spine is the minimum chain that turns security intent into operating work.

> **Architecture Decision Records (ADRs)**
>
> Key architectural decisions — three pillars, NIST spine, overlay model, evidence tiers, inheritance package — are documented in [`/governance/adr/`](../governance/adr/). Each ADR captures the context, alternatives considered, decision rationale, and consequences. New CERG contributors and maintainers should review these before proposing structural changes.

```text
Cybersecurity Policy
  -> CERG Framework
  -> CERG Operating Model
  -> Risk Management Framework
  -> Unified Control Baseline
  -> Standards
  -> Procedures and Plans
  -> Templates and Records
  -> Evidence
  -> Metrics and Oversight
  -> Program Improvement
```

| Layer | Primary artifact | What it answers |
|---|---|---|
| Policy | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) | What is always true? |
| Framework | [CERG-GOV-FRM-001](CERG-GOV-FRM-001_CERG_Framework.md) | How is the program conceptually organized? |
| Operating model | [CERG-GOV-OM-001](CERG-GOV-OM-001_CERG_Operating_Model.md) | Who owns the work and how do the pillars interact? |
| Risk model | [CERG-GOV-RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework.md) | How is risk categorized, scored, treated, accepted, and monitored? |
| Control model | [CERG-GOV-CB-001](CERG-GOV-CB-001_Unified_Control_Baseline.md) | Which control expectations exist and what evidence supports them? |
| Operating flows | [CERG-GOV-FLOW-001](CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md) | How does work move across Engineering, Risk, and Governance? |
| Requirements | Standards in [`../standards/`](../standards/) | What requirements apply by domain? |
| Execution | Procedures in [`../procedures/`](../procedures/) | How is the work performed? |
| Records | [CERG-GOV-CAT-002](CERG-GOV-CAT-002_Record_Catalog.md) | What records prove work happened? |
| Evidence quality | [CERG-GOV-AUD-001](CERG-GOV-AUD-001_Evidence_Quality_Standard.md) | What makes evidence reliable? |
| Metrics | [CERG-GOV-MTR-001](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) | How is posture reported and governed? |
| Improvement | [CERG-GOV-IMPREG-001](CERG-GOV-IMPREG-001_Program_Improvement_Register.md) | How does the program learn and change? |

---

## 3. How the Library Fits Together

### 3.1 Authority hierarchy

| Level | Artifact type | Authority | Example |
|---|---|---|---|
| 1 | Policy | Executive / CISO | Cybersecurity Policy |
| 2 | Governance instruments | CISO / Pillar Leaders | Framework, Operating Model, RMF, Control Baseline |
| 3 | Standards | Governance Pillar Leader | Access, Cloud, OT, CUI, Logging, Endpoint |
| 4 | Procedures | Pillar Owner | Exposure Management, TPRM, Architecture Review |
| 5 | Plans and packages | Pillar Owner | IR Plan, CUI package, NERC-CIP package, SOX package |
| 6 | Templates and records | Process Owner | Risk register, exception form, evidence worksheet |

### 3.2 Execution chain

```text
Policy principle
  -> control objective
  -> standard requirement
  -> procedure step
  -> assigned role
  -> record created
  -> evidence stored
  -> metric updated
  -> oversight decision
```

If any link is missing, the program can still have activity, but it will not have an auditable operating loop.

### 3.3 Three-pillar accountability

| Pillar | Primary question | Typical output |
|---|---|---|
| Cyber Engineering | How do we build and operate this securely? | Architecture decisions, baselines, secure patterns, remediations |
| Cyber Risk | What exposure remains and what treatment is required? | Findings, risk records, vendor assessments, threat validation |
| Cyber Governance | What rule, evidence, decision, or report governs this? | Standards, evidence records, metrics, audit packages, improvement actions |

---

## 4. How Work Moves Through CERG

CERG work should not move by informal chat alone. It should move through one of the canonical flows in [FLOW-001](CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md).

| Flow | Use when | Primary output |
|---|---|---|
| F-01 Control Intent to Implementation | A policy, regulation, audit result, or risk decision needs implementation | Control implementation record |
| F-02 Project Intake, Architecture Review, and Threat Modeling | A project, platform, application, SaaS, cloud workload, or OT change needs review | Project security review record |
| F-03 Asset Registration and Coverage Validation | A new or changed asset enters scope | Asset coverage record |
| F-04 Finding to Remediation, Exception, or Residual Risk | A vulnerability, audit finding, test result, or gap is found | Finding record, remediation record, exception, or risk acceptance |
| F-05 Change and Release Security Routing | A change could alter security posture | Security change review record |
| F-06 Incident to Recovery to Standards Feedback | An incident or exercise produces learning | Lessons learned record and improvement action |
| F-07 Metrics, Oversight, and Improvement Routing | Metrics, maturity results, or oversight decisions require action | Program improvement record |

---

## 5. Navigation by User Need

| If you need to... | Start with | Then use |
|---|---|---|
| Explain CERG to executives | This document and [FRM-001](CERG-GOV-FRM-001_CERG_Framework.md) | [MTR-001](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) board reporting sections |
| Adopt CERG for the first time | [START-HERE](../START-HERE.md) | [IMP-001](CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md), [IMP-005](CERG-GOV-IMP-005_Adoption_Decision_Tree_and_Dependency_Matrix.md) |
| Run a small-team version | [IMP-003](CERG-GOV-IMP-003_Small_Team_Adoption_Path.md) | [IMP-006](CERG-GOV-IMP-006_Role_Based_Implementation_Checklists.md) |
| Decide which documents apply | [IMP-005](CERG-GOV-IMP-005_Adoption_Decision_Tree_and_Dependency_Matrix.md) | [VAR-001](CERG-GOV-VAR-001_Organization_Adaptation_Profile.md) |
| Know what records to create | [CAT-002](CERG-GOV-CAT-002_Record_Catalog.md) | Procedure-specific templates |
| Prepare for audit | [AUD-001](CERG-GOV-AUD-001_Evidence_Quality_Standard.md) | [PRC-AUD-001](../procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md), operational package for the regulator |
| Stand up risk management | [RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework.md) | [PRC-RM-001](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md), [TMPL-RM-001](../templates/CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md) |
| Start exposure management | [PRC-VM-001](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) | [RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework.md), [CAT-002](CERG-GOV-CAT-002_Record_Catalog.md) |
| Review a new system or SaaS | [PRC-AR-001](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) | [TMPL-AR-001](../templates/CERG-TMPL-AR-001_Architecture_and_Project_Intake_Form.md), [PRC-TPRM-001](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) |

---

## 6. Navigation by Adoption Path

### 6.1 CERG Lite

Use when the organization has a small security team or first security hire. The goal is to create a real operating spine without adopting every document.

Start with:

1. Policy
2. Framework
3. Operating Model
4. Document Catalog
5. RMF
6. Risk Register and Exception Process
7. Risk Register Templates
8. Exposure Management Procedure
9. Record Catalog
10. Role-Based Implementation Checklists

### 6.2 CERG Standard

Use when the organization has an existing security function and needs consistent operation.

Add:

- Core standards for access, assets, configuration, IT/cloud/SaaS, logging, endpoint, network, and resilience.
- Architecture review and project intake.
- Third-party and supply-chain risk.
- Metrics and reporting.
- Evidence quality and audit procedure.

### 6.3 CERG Regulated

Use when the organization has explicit regulatory obligations.

Add the applicable package:

| Obligation | Add |
|---|---|
| CUI / CMMC | CUI standard, CUI operational package, SSP, POA&M, evidence matrix |
| NERC-CIP / OT | OT standard, NERC-CIP operational package, segmentation, logging, access, recovery |
| SOX | SOX ITGC operational package, access/change/evidence controls |
| ISO 27001 | ISO operational package, control baseline, SoA support |
| Privacy | Privacy and data protection operational package, data governance standard |

---

## 7. Navigation by Pillar

| Pillar | First documents to read | Operating artifacts to run |
|---|---|---|
| Engineering | [OM-001](CERG-GOV-OM-001_CERG_Operating_Model.md), [FLOW-001](CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md), relevant standards | Architecture intake, asset coverage, configuration baseline, remediation records |
| Risk | [RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework.md), [TAX-001](CERG-GOV-TAX-001_Risk_Taxonomy.md), [FLOW-001](CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md) | Risk register, finding records, vendor assessments, threat validation records |
| Governance | [POL-001](CERG-POL-001_Cybersecurity_Policy.md), [CAT-001](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md), [CB-001](CERG-GOV-CB-001_Unified_Control_Baseline.md), [AUD-001](CERG-GOV-AUD-001_Evidence_Quality_Standard.md) | Evidence index, control implementation records, metrics dashboard, improvement register |

---

## 8. Document Control

| | |
|---|---|
| **Document ID** | CERG-GOV-FRM-002 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Approved By** | CISO |
| **Owner** | Governance Pillar Leader |
| **Next Review** | Quarterly / Upon significant library structure change |

### Revision History

| **Version** | **Date** | **Author** | **Change** |
|---|---|---|---|
| 1.0 | 2026-06-13 | Governance Pillar Leader | Initial publication. Adds a front-door system map for CERG navigation, adoption, and document relationships. |

### Review Triggers

- New top-level governance artifact.
- Change to adoption paths.
- Change to canonical cross-pillar flows.
- New regulated operational package.
- User feedback indicating navigation confusion.

### Related Documents

- [CERG-GOV-FRM-001](CERG-GOV-FRM-001_CERG_Framework.md) - CERG Framework
- [CERG-GOV-OM-001](CERG-GOV-OM-001_CERG_Operating_Model.md) - Operating Model
- [CERG-GOV-FLOW-001](CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md) - Cross-Pillar Operational Flows
- [CERG-GOV-IMP-001](CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) - Implementation and Adaptation Guide
- [CERG-GOV-IMP-005](CERG-GOV-IMP-005_Adoption_Decision_Tree_and_Dependency_Matrix.md) - Adoption Decision Tree and Dependency Matrix
- [CERG-GOV-CAT-002](CERG-GOV-CAT-002_Record_Catalog.md) - Record Catalog
