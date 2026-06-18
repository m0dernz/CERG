
# SURGE: Cyber Engineering, Risk & Governance

## CUI / [CMMC](https://dodcio.defense.gov/CMMC/) OPERATIONAL PACKAGE
### SSP · POA&M · SPRS · Boundary · 800-171 Practice Evidence · [CMMC L2](https://dodcio.defense.gov/CMMC/) Readiness · Subcontractor Register

---

| | |
|---|---|
| **Document ID** | CERG-PLN-CUI-001 |
| **Version** | 1.22 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | CMMC / Federal Compliance Manager |
| **Parent Policy** | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Parent Standard** | [CERG-STD-CUI-001](../standards/CERG-STD-CUI-001_CUI_Handling_Standard.md) - CUI Handling Standard |
| **Supporting Documents** | [CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md) · [CERG-GOV-CB-001](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) · [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) · [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) · [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) · [CERG-STD-RES-001](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) · [CERG-STD-CR-001](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) · [CERG-PRC-AR-001](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) · [CERG-PRC-RM-001](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) · [CERG-PRC-TPRM-001](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) · [CERG-PRC-AV-001](../procedures/CERG-PRC-AV-001_Adversarial_Validation_Procedure.md) |
| **Review Cycle** | Annual / Continuous - POA&M monthly, SSP on material change |
| **Frameworks** | [NIST 800-171r3](https://csrc.nist.gov/pubs/sp/800/171/r3/final) · [NIST 800-172](https://csrc.nist.gov/pubs/sp/800/172/final) (selected) · [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) mappings · [CMMC L2](https://dodcio.defense.gov/CMMC/) |
| **Regulations** | DFARS 252.204-7012 · DFARS 252.204-7019/7020/7021 · [CMMC L2](https://dodcio.defense.gov/CMMC/) |
| **Environments** | All systems within the CUI boundary |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Assumed Scrutiny Level, CMMC L2 Third-Party Assessment](#2-assumed-scrutiny-level--cmmc-l2-third-party-assessment)
3. [CUI Boundary, Finding It and Drawing It](#3-cui-boundary--finding-it-and-drawing-it)
4. [SSP Template](#4-ssp-template)
5. [POA&M Template](#5-poam-template)
6. [SPRS Score Worksheet](#6-sprs-score-worksheet)
7. [CUI Boundary Diagram Template](#7-cui-boundary-diagram-template)
8. [CUI Data Flow Map Template](#8-cui-data-flow-map-template)
9. [CUI Category Register](#9-cui-category-register)
10. [800-171 Practice Evidence Matrix](#10-800-171-practice-evidence-matrix)
11. [CMMC L2 Readiness Checklist](#11-cmmc-l2-readiness-checklist)
12. [C3PAO Assessment Logistics](#12-c3pao-assessment-logistics)
13. [CUI Subcontractor Register](#13-cui-subcontractor-register)
14. [FedRAMP Equivalency Evidence Checklist](#14-fedramp-equivalency-evidence-checklist)
15. [Operating Cadence](#15-operating-cadence)
15. [Regulatory and Framework Alignment Summary](#15-regulatory-and-framework-alignment-summary)
16. [Document Control](#16-document-control)

---

## 1. Purpose and Scope

The CUI Handling Standard names what is required; this package makes the standard executable. It assembles the SSP, POA&M, SPRS worksheet, boundary diagrams, data flow maps, category register, 800-171 evidence matrix, [CMMC L2](https://dodcio.defense.gov/CMMC/) readiness checklist, C3PAO logistics, subcontractor register, and FedRAMP equivalency evidence into a single operational binder.

It applies to every system, person, and process within the CUI boundary, and to every CUI subcontractor receiving CUI from the organization.

---

## 2. Assumed Scrutiny Level: [CMMC L2](https://dodcio.defense.gov/CMMC/) Third-Party Assessment

CERG operates the CUI program at the level required to pass a **[CMMC](https://dodcio.defense.gov/CMMC/) Level 2 third-party assessment** by an authorized C3PAO. [CMMC L1](https://dodcio.defense.gov/CMMC/) is treated as a strict subset that is automatically met when L2 is met.

> **Why Plan for L2 Third-Party as the Baseline**
>
> [CMMC L2](https://dodcio.defense.gov/CMMC/) with C3PAO assessment is the highest practical scrutiny most CUI primes face on a routine cadence. If the program is ready for that scrutiny, it is ready for the lesser ones. Designing to a lower level and hoping to "lift later" produces a program that drifts under audit pressure.

---

## 3. CUI Boundary: Finding It and Drawing It

The CUI boundary is the set of systems, people, processes, and physical spaces that store, process, or transmit CUI. Defining it is the first executable step; it drives everything else.

### 3.1 Discovery Method

1. **Start from contracts.** DFARS-flowed contracts identify CUI obligations and (often) the categories.
2. **Add data discovery.** Use DLP, data discovery tools, and labelled storage signals to locate CUI in environments that may have it.
3. **Add process discovery.** Interview business units that interact with contracts; identify where CUI enters the environment.
4. **Validate via Architecture Review records.** [`CERG-PRC-AR-001`](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) should have intaken any system handling CUI; any CUI-handling system not in the AR record is a finding.
5. **Reconcile against the CUI Category Register** (Section 9).

### 3.2 Categories of CUI Currently In Scope

The CUI Category Register (Section 9) lists categories actually handled (e.g., Controlled Technical Information, Export Control, Procurement Sensitive). Categories not handled are explicitly noted as Not-In-Scope so future inquiries are unambiguous.

### 3.3 Boundary Statement (Example Skeleton)

```
The CUI boundary comprises:
  - <named CUI enclave> in <provider> (FedRAMP Moderate / equivalent)
  - <named on-prem CUI work area> in <facility>
  - <named CUI endpoints> assigned to <named groups>
  - <named CUI applications> with their associated identity, logging, and backup systems
Excludes:
  - General corporate IT
  - OT environments (separately governed by [CERG-STD-OT-001](../standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) / [CERG-PLN-CIP-001](CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md))
  - SOX-relevant systems that do not also handle CUI
```

---

## 4. SSP Template

The System Security Plan is the assessor-facing description of the CUI environment and how each 800-171 practice is implemented.

```
SYSTEM SECURITY PLAN - <CUI System / Enclave Name>     SSP-CUI-NNN

1. SYSTEM IDENTIFICATION
   System Name(s) / Aliases
   System Type            (enclave / app / hybrid)
   Operational Status
   Executive Sponsor / System Representative
   Authorizing Official (CISO)
   Information System Security Point of Contact (CMMC / Federal Compliance Manager or delegate)
   System Boundary Description (Section 3.3 instance)

2. SYSTEM ENVIRONMENT
   Architecture and components (reference Section 7 diagram)
   Hardware and software inventory
   Network topology (reference Section 7 diagram)
   Hosting / cloud / SaaS providers and FedRAMP / equivalency status (Section 14)
   Interconnections and authorized data flows (reference Section 8 map)

3. CUI CATEGORIES PROCESSED
   List of categories per Section 9 register
   Sensitivity considerations (export control, etc.)

4. SECURITY REQUIREMENT IMPLEMENTATION
   For each 800-171r3 practice (3.1.1 … 3.14.x):
     - Practice statement
     - Implementation status (Implemented / Partially / Inherited / Planned / N/A) per [CERG-GOV-CB-001](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) Section 4
     - Implementation description (specific, system-specific text)
     - Inheritance source (if inherited; references Section 14)
     - Evidence pointer (system / artifact / location)
     - Cross-reference to CERG control / standard / procedure

5. ROLES AND RESPONSIBILITIES
   Named roles for system operations and security

6. CONTINUOUS MONITORING STRATEGY
   Detection coverage; vulnerability scanning; recertification; control test cadence

7. INCIDENT RESPONSE
   Reference to [CERG-PLN-IR-001](CERG-PLN-IR-001_Incident_Response_Plan.md) with CUI-specific notes (DC3 reporting, 72-hour notification)

8. APPROVALS
   Information System Security Point of Contact, Executive Sponsor / System Representative, CISO

Appendices:
  A. CUI Boundary Diagram (Section 7)
  B. CUI Data Flow Map (Section 8)
  C. 800-171 Practice Evidence Matrix (Section 10)
  D. POA&M (Section 5)
  E. Inheritance Evidence Packages (Section 14)
```

> **The SSP Is Specific, Not Aspirational**
>
> "Multi-factor authentication is implemented" is not implementation language. "Phishing-resistant MFA via Entra ID enforced by Conditional Access policy 'CUI-Enclave-Privileged-MFA' for all privileged role holders, with break-glass exception per [`CERG-PRC-AC-002`](../procedures/CERG-PRC-AC-002_Access_Management_Runbook.md) §7" is. C3PAO assessors read implementation language for specificity; vague text invites probing questions and findings.

---

## 5. POA&M Template

The Plan of Action and Milestones tracks Partially Implemented and Planned items toward closure.

| **Field** | **Description** |
|---|---|
| POAM ID | `POAM-CUI-YYYY-NNNN` |
| 800-171 Practice | e.g., 3.13.11 |
| Weakness | Specific, not vague |
| Affected Systems | Reference SSP boundary |
| Source | Self-assessed · Internal audit · C3PAO · Pen test · Vuln scan |
| Severity | Per [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) scoring |
| Owner | Named role |
| Resources Required | People / budget / vendor |
| Original Identification Date | - |
| Target Milestones | Step-level with dates |
| Completion Date | Target |
| Status | Open · In Progress · Completed · Risk Accepted |
| Linked Risk Register ID | If risk-accepted or material |
| Evidence on Closure | Artifact required at close |

POA&M is updated **monthly** at minimum; closures must include evidence acceptable at C3PAO assessment.

---

## 6. SPRS Score Worksheet

The Supplier Performance Risk System score is the self-reported [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) maturity number reported under DFARS 252.204-7019. The worksheet:

| **Field** | **Description** |
|---|---|
| Assessment Date | - |
| Assessment Scope | SSP-CUI-NNN reference |
| Methodology | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) DoD Assessment Methodology v1.2.1 |
| Starting Score | 110 |
| Weighted Deductions Applied | Per DoD scoring template - list each practice missed and its deduction |
| Final Score | Calculated |
| POA&M Items at Time of Score | Count + IDs |
| Expected Closure Schedule | Per POA&M |
| Reporter | Named role |
| Submitted to SPRS Date | - |

The worksheet is reproduced from the public DoD methodology; CERG does not invent its own scoring weights.

---

## 7. CUI Boundary Diagram Template

The diagram is produced in the architecture tool used by [`CERG-PRC-AR-001`](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md). The required elements:

- The **trust boundary** of the CUI environment, clearly drawn.
- All **CUI-processing systems** inside the boundary.
- All **entry / exit points** with named identity, network, and encryption controls.
- **External services** that touch the boundary (FedRAMP / equivalency status annotated).
- **Subcontractor connections** (Section 13).
- **Out-of-scope adjacent systems** distinguished with shading or annotation.

A diagram is required at SSP submission and refreshed on any material change.

---

## 8. CUI Data Flow Map Template

The data flow map shows how CUI moves from contract intake → processing → archival, including:

- Each **transit hop** annotated with protocol and [`CERG-STD-CR-001`](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) encryption details.
- Each **transformation** (where CUI is combined, derived, or labeled).
- Each **storage location** with classification label, retention, and access pattern.
- Each **export** (to a customer, a subcontractor, or a contracting officer) with delivery method.

The map is referenced from the SSP and from the boundary diagram.

---

## 9. CUI Category Register

| **Field** | **Description** |
|---|---|
| Category | e.g., Controlled Technical Information, Export Control, Procurement Sensitive |
| Source Authority | E.g., 32 CFR § 2002, DFARS 252.204-7012 |
| First Seen | When CUI of this category entered scope |
| Currently In Scope | Y/N |
| Receiving Systems | SSP references |
| Special Handling | Export control, FedRAMP requirement, etc. |
| Disposition on Contract End | Return / Destroy / Retain per contract |

Categories never handled are explicitly listed as Not-In-Scope so future inquiries are unambiguous.

---

## 10. 800-171 Practice Evidence Matrix

The matrix is the row-per-practice spine. It is the principal artifact a C3PAO uses to navigate the SSP.

| **Field** | **Description** |
|---|---|
| Practice ID | e.g., 3.13.11 |
| Practice Statement | [NIST 800-171r3](https://csrc.nist.gov/pubs/sp/800/171/r3/final) language |
| Implementation Status | Per [`CERG-GOV-CB-001`](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) Section 4 |
| CERG Control(s) | From [`CERG-GOV-CB-001`](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) |
| Subordinate Standard / Procedure | E.g., [`CERG-STD-CR-001`](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) §9 |
| System(s) Implementing | Per SSP |
| Evidence Artifact | Specific document / report / configuration export |
| Evidence Location | URI / system / binder reference |
| Last Verified | Date |
| Next Verification | Date |
| Open POA&M | POAM ID if applicable |
| Notes | Special handling, exceptions |

The matrix is the artifact CERG ships with the SSP. It is updated whenever an evidence artifact is refreshed.

---

## 11. [CMMC L2](https://dodcio.defense.gov/CMMC/) Readiness Checklist

A pre-assessment self-check, repeated quarterly and aggressively in the 90 days before an assessment.

| **Area** | **Check** | **Pass** |
|---|---|---|
| Scope | CUI boundary documented and currently accurate | Y / N |
| Scope | All CUI-handling systems intaken via [`CERG-PRC-AR-001`](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) | Y / N |
| SSP | SSP current; specific implementation language; appendices complete | Y / N |
| Evidence | Evidence Matrix has artifact for every practice | Y / N |
| Evidence | Every evidence artifact dates within the assessor's expected window | Y / N |
| POA&M | All Partially Implemented items have current POA&M | Y / N |
| Inheritance | Every Inherited practice has Inheritance Evidence Package per [`CERG-GOV-CB-001`](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) Section 5 | Y / N |
| Crypto | FIPS profile per [`CERG-STD-CR-001`](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) Section 9 satisfied | Y / N |
| Logging | Mandatory log sources onboarded per [`CERG-STD-LM-001`](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) | Y / N |
| Detection | Day-one detection set in CUI environment | Y / N |
| Access | Phishing-resistant MFA on CUI access paths | Y / N |
| Backup | Recovery plan exists; recent restoration test for CUI tier | Y / N |
| Vendor / Sub | Subcontractor register current; flow-down validated | Y / N |
| Incident Response | DC3 reporting path tested or rehearsed | Y / N |
| People | Awareness training current for CUI handlers | Y / N |
| Physical | CUI work areas conform to physical control requirements | Y / N |
| **Sampled Walkthroughs** | At least one walkthrough per CUI system in the 90-day window | Y / N |

### 11.2 Mock CMMC Assessment Procedure

The Mock Assessment Procedure is scheduled 6 months before the target C3PAO assessment date. It simulates the full CMMC Level 2 assessment process using internal or partner assessors to identify gaps before the real assessment.

#### Scope Definition

| **Scope Element** | **Description** |
|---|---|
| Assessment Boundary | All systems, people, processes, and facilities within the CUI boundary (Section 3) |
| Framework | CMMC Level 2 practices and processes (ALL 110+ practices across 14 domains) |
| Assessment Type | Full mock (practice-by-practice evidence review + interview simulation) |
| Exclusions | Explicitly documented; any exclusion must be approved by CMMC / Federal Compliance Manager |
| Evidence Window | Evidence from prior 12 months minimum; assessors may request specific periods |

#### Assessor Assignment

| **Assessor Role** | **Source** | **Responsibilities** |
|---|---|---|
| Lead Assessor | Internal (Governance Pillar Leader or qualified senior CERG member) OR external partner (e.g., consulting firm, C3PAO-in-training) | Overall assessment coordination, final findings report, exit briefing |
| Practice Reviewer | Internal (Engineering, Risk, Governance pillar members NOT responsible for the systems under assessment) | Practice-by-practice evidence review per Practice Evidence Matrix |
| Interviewer | Internal (trained assessor or HR-partnered facilitator) | Conduct leadership, system owner, and operator interviews |
| Scribe | Internal (Evidence Librarian or designee) | Document findings, observations, and notes during all sessions |
| Observer | CMMC / Federal Compliance Manager | Observe process; no scoring authority during mock |

#### Independence Requirement

- No assessor may evaluate practices they personally own or operate.
- If the organization has only 2–3 CERG team members, use an external partner for at least the Lead Assessor role.
- Independence declarations are signed by each assessor before the mock begins.

#### Practice-by-Practice Evidence Review

The core of the mock assessment. Each CMMC Level 2 practice (ALL 110+) is reviewed against the Practice Evidence Matrix (Section 10).

| **Review Step** | **Details** |
|---|---|
| Pre-populate | Evidence Matrix is pre-populated with current evidence artifacts, status, and last-verified dates |
| Reviewer assignment | Each practice assigned to a Practice Reviewer; 20–30 practices per reviewer typical |
| Evidence inspection | Reviewer inspects each evidence artifact for: completeness (per Section 10 matrix), freshness (within expected window), traceability (artifact maps to the practice claim), and quality (per [`CERG-GOV-AUD-001`](../governance/CERG-GOV-AUD-001_Evidence_Quality_Standard.md)) |
| Scoring | Per CMMC scoring: MET / NOT MET / NOT APPLICABLE |
| Observation notes | Reviewer records observations, concerns, and clarifying questions per practice |
| Gap flagging | Any practice scored NOT MET is flagged with the specific deficiency, root cause, and recommended remediation |
| Re-review | Remediated practices are re-reviewed within 2 weeks of closure evidence |

#### Interview Simulation

Interviews simulate C3PAO assessor interaction with key personnel.

| **Interview Session** | **Participants** | **Duration** | **Topics** |
|---|---|---|---|
| Leadership | CISO, Governance Pillar Leader, CMMC / Federal Compliance Manager | 60 min | Program governance, risk posture, resource adequacy, CISO awareness |
| System Owners | Named system owners for each CUI system | 45 min per system | System architecture, boundary, data flows, SSP accuracy, evidence accessibility |
| Operators | Engineering and IT staff operating CUI systems | 30 min per group | Day-to-day operations, control execution, evidence production, training awareness |
| Policy & Process | Policy & Standards Manager, relevant process owners | 45 min | Policy awareness, process adherence, document currency, exception handling |
| Incident Response | Incident Commander, IR team members | 30 min | IR plan awareness, DC3 reporting path, tabletop exercise experience |

#### Findings Report

| **Report Section** | **Content** |
|---|---|
| Executive Summary | Overall mock assessment result, total practices scored NOT MET, top 5 risks |
| Scope and Methodology | Assessment boundary, assessor roles, evidence window, interview participants |
| Practice-by-Practice Results | Full matrix: practice ID, scoring, observations, evidence state |
| Findings Detail | Each NOT MET practice: deficiency description, root cause, evidence gap analysis, risk impact |
| Strengths | Practices where evidence is exemplary — maintain as-is |
| Interview Observations | Notable themes, awareness gaps, procedural inconsistencies |
| Recommendations | Prioritised remediation actions with owners and target dates |

#### Remediation Timeline

| **Phase** | **Activities** | **Duration** | **Owner** |
|---|---|---|---|
| Findings Review | CMMC / Federal Compliance Manager reviews findings; categorises by severity and effort | 1 week | CMMC / Federal Compliance Manager |
| Remediation Planning | Owner assigned per finding; remediation plan with milestones | 2 weeks | Practice owners |
| Quick Wins | Fixes requiring <2 hours effort: missing evidence labels, stale dates, documentation corrections | 2 weeks | Practice owners |
| Medium Remediation | Fixes requiring 2–40 hours: new evidence collection, SOP updates, control implementation | 6 weeks | Practice owners |
| Major Remediation | Fixes requiring >40 hours: new tooling, architecture changes, policy creation | 8–12 weeks | Governance Pillar Leader + pillar owners |
| Milestone Review | Biweekly check-ins on remediation progress | Until closed | CMMC / Federal Compliance Manager |

#### Re-Test

| **Re-Test Element** | **Detail** |
|---|---|
| Timing | 30 days before target C3PAO assessment date |
| Scope | Only previously scored NOT MET practices + any practice affected by remediation |
| Assessor | Same Lead Assessor (or equivalent independence) |
| Method | Full evidence re-inspection + targeted interviews on changed practices |
| Outcome | Updated findings report; remaining NOT MET practices are either remediated with evidence or escalated to CISO for risk acceptance decision |
| Go/No-Go Decision | CISO, Governance Pillar Leader, and CMMC / Federal Compliance Manager decide based on re-test results: proceed to C3PAO assessment, delay (with contract impact assessment), or proceed with known gaps documented |

---

## 12. C3PAO Assessment Logistics

Logistics that consistently surprise organizations on assessment day; CERG handles them ahead of time.

| **Item** | **Owner** | **Pre-Assessment Action** |
|---|---|---|
| Authorized C3PAO selected and scheduled | Governance - CUI | 90+ days out |
| Assessment scope confirmed in writing | C3PAO + Governance - CUI | 60 days out |
| Pre-assessment evidence package shipped | Governance - CUI | 30 days out |
| On-site / remote logistics arranged | Governance - CUI | 30 days out |
| Named interviewees prepared (system owners, ISSO, leadership) | Governance - CUI | 30 days out |
| Workspace / shared evidence repo configured for assessor access | Governance - CUI | 30 days out |
| Daily out-brief cadence agreed | C3PAO + Governance - CUI | At kickoff |
| Finding response process agreed | C3PAO + Governance - CUI | At kickoff |
| Final report receipt and POA&M response window | Governance - CUI | At report |
| CISO and executive comms prepared | CISO + Governance | Pre-final |

---

## 13. CUI Subcontractor Register

| **Field** | **Description** |
|---|---|
| Subcontractor Name | - |
| Contract ID(s) | - |
| CUI Category Received | Per Section 9 |
| Flow-Down Verified | Y/N + verification date |
| [CMMC L2](https://dodcio.defense.gov/CMMC/) Status | Status + assessment expiry |
| FedRAMP Equivalency | If subcontractor hosts in cloud |
| Cyber POC | Named contact |
| Incident Notification Path | Reference; tested? |
| Last Review | Date |
| Next Review | Date |
| Status | Active · Inactive · Suspended |

The register is maintained jointly by Governance, CUI and TPRM; the TPRM record is canonical for vendor data with this register adding CUI-specific fields.

---

## 14. FedRAMP Equivalency Evidence Checklist

For cloud / SaaS providers handling CUI that are not FedRAMP-authorized, the equivalency package required by [`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) Section 14. Repeated here as a CUI-program reference.

| **Element** | **Required** |
|---|---|
| SOC 2 Type II with [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) Moderate baseline mapping | ✓ |
| 3PAO-equivalent assessment letter / independent assessor attestation | ✓ |
| Customer-side configuration commitments (CUI label, region, key control) | ✓ |
| Sub-service organization carve-outs reconciled | ✓ |
| Re-papering trigger documented | ✓ |
| Inheritance Evidence Package per [`CERG-GOV-CB-001`](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) Section 5 on file | ✓ |

---
## 15. Regulatory and Framework Alignment Summary

| **Regulation / Framework** | **Where in This Package** |
|---|---|
| [NIST 800-171r3](https://csrc.nist.gov/pubs/sp/800/171/r3/final) | All sections; Section 10 is the principal evidence artifact |
| [NIST 800-172](https://csrc.nist.gov/pubs/sp/800/172/final) (selected enhancements) | Where contract requires |
| [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) (Moderate baseline mapping) | Sections 4, 14 |
| [CMMC L2](https://dodcio.defense.gov/CMMC/) | All sections; Section 11 is the readiness check |
| DFARS 252.204-7012 | Sections 4, 13 (flow-down) |
| DFARS 252.204-7019 / 7020 / 7021 | Section 6 (SPRS) |

---

## 16. Document Control

| | |
|---|---|
| **Document ID** | CERG-PLN-CUI-001 |
| **Version** | 1.22 |
| **Approved By** | CISO |
| **Next Review** | Annual / on regulatory change |
| **Change Log** | 1.0 - Initial publication. SSP, POA&M, SPRS, boundary, flow map, category register, evidence matrix, readiness, C3PAO logistics, subcontractor register, FedRAMP equivalency. 1.22 - Added Mock CMMC Assessment Procedure (§11.2) with scope, assessor assignment, practice-by-practice evidence review, interview simulation, findings report, remediation timeline, and re-test. |

