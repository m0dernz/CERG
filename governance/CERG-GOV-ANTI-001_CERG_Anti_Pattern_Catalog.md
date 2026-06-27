## CERG ANTI-PATTERN CATALOG
### Common Failure Modes · Observable Symptoms · Corrective Actions

---

| | |
|---|---|
| **Document ID** | CERG-GOV-ANTI-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [`CERG-GOV-IMP-002`](CERG-GOV-IMP-002_Adoption_Safety_Guide.md) · [`CERG-GOV-FRM-001`](CERG-GOV-FRM-001_CERG_Framework.md) · [`CERG-GOV-JA-001`](CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) · [`CERG-GOV-AUD-001`](CERG-GOV-AUD-001_Evidence_Quality_Standard.md) · [`CERG-GOV-CMX-001`](CERG-GOV-CMX-001_Compliance_Matrix.md) |
| **Review Cycle** | Annual / On material adoption feedback |
| **Frameworks** | NIST CSF 2.0 (GOVERN) |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG adopters |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [How to Use This Catalog](#2-how-to-use-this-catalog)
3. [Anti-Pattern Index](#3-anti-pattern-index)
4. [Workforce and Role Anti-Patterns](#4-workforce-and-role-anti-patterns)
5. [Capability Anti-Patterns](#5-capability-anti-patterns)
6. [Evidence and Compliance Anti-Patterns](#6-evidence-and-compliance-anti-patterns)
7. [Using Anti-Patterns in Program Review](#7-using-anti-patterns-in-program-review)
8. [Document Control](#8-document-control)

---

## 1. Purpose and Scope

CERG is more than a rulebook. It is a contract between leadership and the people who actually run the program. This catalog exists because most programs do not fail from missing policies. They fail from pretending the policies are already true.

This catalog collects the failure modes that show up again and again across adoption, workforce design, capability building, evidence management, and compliance. It is blunt by design. It is meant to be read by CISOs, pillar leads, and engineers who want to know what is actually broken instead of what the status deck says is working. It does not replace detailed guidance in the source documents; those documents explain what right looks like. This document explains what right looks like when nobody is watching and the metrics still look green.

An anti-pattern is included when it meets three tests:

1. It is common enough that adopters will almost certainly encounter it.
2. It creates operational risk, governance confusion, or false confidence.
3. It has a practical correction already available inside CERG.

---

## 2. How to Use This Catalog

Use this catalog during implementation planning, quarterly program review, red-team walkthroughs, incident post-mortems, and maturity assessment.

- **Adopters** use it to surface dysfunction before it becomes embedded.
- **CISOs and pillar leaders** use it to challenge optimistic status reporting.
- **Governance teams** use it to convert recurring failure modes into improvement items with owners and dates.
- **Auditors and assessors** use it to understand where CERG expects evidence, ownership, and validation.
- **Contributors** use it to identify gaps in the framework itself; if a repeated anti-pattern has no corrective guidance, the corpus needs improvement.

The catalog is intentionally blunt. The goal is not to shame teams. The goal is to make weak operating patterns visible early, when they are still cheap to correct.

---

## 3. Anti-Pattern Index

| ID | Anti-Pattern | Domain | Observable Symptom | Corrective Anchor |
|---|---|---|---|---|
| ANTI-ADOPT-001 | Fork-and-Declare | Adoption | Repository forked, names changed, no operating cadence or evidence | [`CERG-GOV-IMP-002`](CERG-GOV-IMP-002_Adoption_Safety_Guide.md) |
| ANTI-ADOPT-002 | Delete Roles Instead of Consolidating | Adoption / Workforce | Unstaffed accountabilities disappear from the RACI | [`CERG-GOV-RAC-001`](CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) |
| ANTI-WF-001 | Hero Role | Workforce | One senior person informally owns too many critical functions | [`CERG-GOV-WFP-001`](CERG-GOV-WFP-001_Workforce_Planning_and_Capacity_Model.md) |
| ANTI-WF-002 | Title Inflation Instead of Career Pathing | Workforce | Management titles used to retain single-domain experts without management scope | [`CERG-GOV-JA-001`](CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) |
| ANTI-WF-003 | Accountability Without Capacity | Workforce | A named owner has no time, authority, tooling, or escalation path | [`CERG-GOV-SLC-001`](CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md) |
| ANTI-CAP-001 | Capability by Tool Purchase | Capability | A tool is bought and the capability is declared implemented | [`CERG-GOV-FRM-001`](CERG-GOV-FRM-001_CERG_Framework.md) §3 |
| ANTI-CAP-002 | Capability by Meeting | Capability | Meetings exist, but decisions, owners, and evidence do not | [`CERG-GOV-FLOW-001`](CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md) |
| ANTI-CAP-003 | Capability by Dashboard | Capability | Dashboards show state, but no one acts or validates outcomes | [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) |
| ANTI-CAP-004 | Capability Without Validation | Capability | A capability is claimed but has never been tested, sampled, or exercised | [`CERG-GOV-CEF-001`](CERG-GOV-CEF-001_Control_Effectiveness_Framework.md) |
| ANTI-EVID-001 | Screenshot Theater | Evidence | Screenshots lack scope, owner, timestamp, or control mapping | [`CERG-GOV-AUD-001`](CERG-GOV-AUD-001_Evidence_Quality_Standard.md) |
| ANTI-EVID-002 | Pre-Audit Archaeology | Evidence | Evidence is reconstructed immediately before an audit | [`CERG-PRC-AUD-001`](../procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) |
| ANTI-EVID-003 | Policy-as-Evidence | Evidence | A policy statement is used as proof that a control operated | [`CERG-GOV-AUD-001`](CERG-GOV-AUD-001_Evidence_Quality_Standard.md) |
| ANTI-COMP-001 | Control Mapping as Control Operation | Compliance | A mapped control is treated as implemented without operating evidence | [`CERG-GOV-CMX-001`](CERG-GOV-CMX-001_Compliance_Matrix.md) |
| ANTI-COMP-002 | POA&M as Permission Slip | Compliance | Gaps are parked in POA&M with no credible owner, funding, or date | [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) |
| ANTI-COMP-003 | Regulation-First Operating Model | Compliance | Teams organize around frameworks instead of reusable capabilities and evidence | [`CERG-GOV-FRM-001`](CERG-GOV-FRM-001_CERG_Framework.md) §12 |

---

## 4. Workforce and Role Anti-Patterns

### 4.1 ANTI-WF-001 — Hero Role

**What it looks like:** One senior person informally owns architecture review, risk acceptance preparation, incident support, vendor risk review, evidence quality, and executive reporting. The work gets done because that person is exceptional.

**Why it fails:** The program works only while the hero is present. The capability lives in a person, not in the operating model. When the person is unavailable, leaves, or burns out, handoffs fail and institutional memory disappears.

**Corrective action:** Move the work into explicit roles, procedures, records, and review cadences. Consolidation is allowed, but hidden ownership is not. If one person must cover multiple roles, record the consolidation in the Decision Log and define compensating controls for self-review risk.

### 4.2 ANTI-WF-002 — Title Inflation Instead of Career Pathing

**What it looks like:** A single strong engineer becomes "Manager of Cloud Security" or "Director of Risk" to improve retention, even though they do not manage people, budget, or a multi-team function.

**Why it fails:** The title creates management expectations without management scope. It also hides the real need: a strong SME career path. The organization may end up with inflated titles, unclear authority, and no real management capacity.

**Corrective action:** Use the SME track in [`CERG-GOV-JA-001`](CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md). Promote depth and influence as Advisor or Sr. Advisor when the work is expert contribution. Create management roles only when span of control, domain divergence, succession need, or distribution requires one.

### 4.3 ANTI-WF-003 — Accountability Without Capacity

**What it looks like:** A RACI names an owner, but the person has no time allocation, decision authority, tools, budget input, or escalation path. The owner is accountable in the document but powerless in practice.

**Why it fails:** Named ownership without capacity is symbolic governance. It creates a false sense that the work is covered while guaranteeing overdue actions, unreviewed evidence, and quiet risk acceptance by neglect.

**Corrective action:** Every accountable role must have enough capacity, authority, and escalation support to perform the work. If capacity is unavailable, reduce scope, defer the capability explicitly, automate part of the workflow, or escalate for staffing and budget. Do not mark the role covered merely because a name appears in the table.

---

## 5. Capability Anti-Patterns

### 5.1 ANTI-CAP-001 — Capability by Tool Purchase

**What it looks like:** The organization buys a SIEM, scanner, GRC platform, CSPM, SSPM, or ticketing workflow and declares the related capability implemented.

**Why it fails:** Tools support capabilities; they do not create them. Detection requires telemetry, tuned analytics, triage ownership, response paths, and validation. Exposure management requires coverage, prioritization, owner follow-up, SLA tracking, and treatment decisions. Governance requires decision rights, evidence quality, review cadence, and accountable owners.

**Corrective action:** For each tool, name the capability it supports, the procedure it feeds, the owner who acts on its output, and the evidence that proves the capability operates. If those outputs are absent, the capability is still Ad Hoc.

### 5.2 ANTI-CAP-002 — Capability by Meeting

**What it looks like:** A weekly risk meeting, architecture review board, or compliance sync exists, so leaders believe the capability is operating.

**Why it fails:** Meetings are coordination mechanisms, not evidence of capability. A meeting that produces no decision, no owner, no due date, no evidence link, and no follow-up is operational theater.

**Corrective action:** Every recurring CERG meeting must produce one or more operational records: decision log entry, risk record update, finding update, evidence request, exception decision, improvement item, or escalation. If a meeting does not produce records, redesign or cancel it.

### 5.3 ANTI-CAP-003 — Capability by Dashboard

**What it looks like:** A dashboard shows vulnerability counts, alert volume, compliance percentages, or project queue status. Because the dashboard exists, the capability is treated as mature.

**Why it fails:** Dashboards report state. They do not prove that the organization can act. A metric without owner action, threshold logic, and escalation path becomes passive observation.

**Corrective action:** Tie each dashboard metric to an owner, threshold, decision rule, and corrective action path. If a metric crosses a threshold and nothing happens, the metric is decorative, not operational.

### 5.4 ANTI-CAP-004 — Capability Without Validation

**What it looks like:** The organization claims detection, recovery, segmentation, vendor response, or evidence retrieval capability, but the capability has never been tested, sampled, exercised, or independently reviewed.

**Why it fails:** Untested capability is an assumption. The gap usually appears during an incident, audit, or executive deadline, when correction is most expensive.

**Corrective action:** Define a validation method for each material capability: adversarial validation, tabletop exercise, evidence spot-check, restore test, sample audit, control effectiveness test, or automated re-validation. The maturity level is capped by the weakest unvalidated link.

---

## 6. Evidence and Compliance Anti-Patterns

### 6.1 ANTI-EVID-001 — Screenshot Theater

**What it looks like:** Evidence folders contain screenshots with no timestamp, no scope statement, no accountable owner, no system identifier, and no control mapping.

**Why it fails:** Screenshots can be useful supporting evidence, but unmanaged screenshots prove little. They are hard to validate, easy to misread, and often impossible to tie to a control period.

**Corrective action:** Evidence must be dated, attributable, scoped, relevant, complete, and retrievable. Use screenshots only when they are linked to a control, system, period, and owner, and when no stronger system export or record exists.

### 6.2 ANTI-EVID-002 — Pre-Audit Archaeology

**What it looks like:** Evidence is assembled weeks before an audit by searching shared drives, asking engineers for exports, and reconstructing decisions from chat history.

**Why it fails:** Evidence reconstructed under audit pressure is incomplete, inconsistent, and expensive. It also proves the program is not producing evidence as a byproduct of normal operations.

**Corrective action:** Use the evidence calendar, record catalog, and audit procedure to collect evidence on cadence. If evidence cannot be retrieved without heroics, create a Program Improvement Register entry.

### 6.3 ANTI-EVID-003 — Policy-as-Evidence

**What it looks like:** A policy says access reviews, backups, logging, or risk reviews must happen, so the control is marked implemented.

**Why it fails:** A policy proves intent. It does not prove operation. Auditors and leaders need evidence that the activity occurred, exceptions were handled, and outcomes were reviewed.

**Corrective action:** Pair every policy requirement with operating evidence: review record, log export, ticket, register update, test result, or approval record. Use policy as design evidence, not operating evidence.

### 6.4 ANTI-CAP-005 — Measurement Theater

**What it looks like:** The program produces frameworks full of KPIs, KRIs, and coverage percentages, yet no metric changes a decision, triggers an escalation, or changes a budget line. Dashboards are reviewed; nothing acts on them.

**Why it fails:** Measurement without decision rules is observation, not management. A metric that cannot change behavior is decorative. This anti-pattern often appears alongside ANTI-CAP-003, but is worse: the dashboard exists, the conversation exists, and still nothing moves.

**Corrective action:** Every metric must have an explicit decision rule and owner: "If X crosses Y, then owner Z must do A by date B." If a metric has no such rule, remove it from reporting or convert it into an action.

### 6.5 ANTI-CAP-006 — Detection as a Rule Count

**What it looks like:** The program claims detection maturity by counting Sigma rules, analytics, or detection coverage percentages without demonstrating alert triage, owner assignment, SLA compliance, or false-positive reduction.

**Why it fails:** Rule count is an input, not a capability. An analyst drowning in noise with no triage path, no coverage validation, and no test cadence does not have detection capability no matter how many rules exist.

**Corrective action:** Measure detection by outcome: alert-to-triage time, triage-to-closure time, false-positive rate by rule family, and coverage validated by red-team exercise. Count rules as a development metric, not a maturity metric.

### 6.6 ANTI-CAP-007 — Detection by Anonymous Hero

**What it looks like:** Detection rules, hunts, and triage decisions originate primarily from one individual rather than from documented procedures, playbooks, hunt cycles, and peer-reviewed analytics.

**Why it fails:** The capability is embedded in a person, not in the program. When that person is unavailable, the organization cannot defend itself. This pattern is the detection-engineering version of ANTI-WF-001.

**Corrective action:** Move detection logic into version-controlled rule sets, documented hunt hypotheses, peer review gates, and owned detection services. Every rule should have an owner, a maintenance date, and a test record.

### 6.7 ANTI-EVID-004 — False-Positive Management Theater

**What it looks like:** Alert tuning focuses on suppressing alerts to improve mean-time-to-detect or alert volume metrics, rather than improving signal quality. Tuning decisions are undocumented, ownership is unclear, and the resulting "clean" dashboards hide real gaps in coverage.

**Why it fails:** Suppressing alerts without documenting the decision, the rationale, and the residual risk is evidence that the tuning process is operating, not that detection is effective. It may satisfy a metric but breaks the program when the first novel attack bypasses the blind spot.

**Corrective action:** Tuning must produce evidence: the rule delta, the rationale, the risk acceptance if applicable, the owner approval, and the impact on coverage. Track blind-spot risks created by suppression explicitly.
### 6.8 ANTI-COMP-001 — Control Mapping as Control Operation

**What it looks like:** A control is mapped to NIST, CMMC, NERC-CIP, SOX, or ISO and is therefore treated as mature.

**Why it fails:** Mapping proves alignment intent. It does not prove that the control is designed, operating, evidenced, or effective.

**Corrective action:** Treat mapping as the start of the evidence chain. A mapped control still needs owner, implementation path, operating record, evidence quality, and validation.

### 6.9 ANTI-COMP-002 — POA&M as Permission Slip

**What it looks like:** Every gap becomes a POA&M item, but the item has no credible owner, funding, schedule, dependency plan, or evidence of progress.

**Why it fails:** A POA&M is a plan for closing a gap, not permission to ignore it. Weak POA&Ms create the appearance of management while preserving the exposure.

**Corrective action:** Every POA&M item must have an owner, target date, funding or capacity path, interim risk treatment, and progress evidence. Stale POA&M items must promote to risk or executive escalation.

### 6.10 ANTI-COMP-003 — Regulation-First Operating Model

**What it looks like:** Separate teams, evidence stores, calendars, and status reports are built for each framework: one for CMMC, one for SOX, one for NERC-CIP, one for ISO.

**Why it fails:** The organization duplicates work and confuses ownership. Operators experience compliance as multiple parallel asks rather than one evidence-producing operating model.

**Corrective action:** Build reusable capabilities and evidence factories first. Map the resulting evidence to frameworks through the Compliance Matrix and regulatory operational packages. Compliance should reuse operational evidence, not create a parallel universe.

---

## 7. Using Anti-Patterns in Program Review

During quarterly program review, ask each pillar leader to identify any anti-patterns currently present in their scope. For each selected anti-pattern, record:

| Field | Description |
|---|---|
| Anti-pattern ID | The catalog ID, e.g., ANTI-CAP-003 |
| Affected capability or workflow | The capability, procedure, or team where the pattern appears |
| Evidence observed | What shows the pattern is present |
| Risk created | The operational or governance risk the pattern creates |
| Corrective action | The specific change to role, procedure, evidence, tooling, or cadence |
| Owner and due date | Named owner and target closure |
| Tracking record | Risk record, finding, exception, or Program Improvement Register item |

If the same anti-pattern appears in two consecutive reviews, it must be tracked as a program improvement item. If it appears in three consecutive reviews, it is a maturity constraint: the affected capability cannot score above Defined until the pattern is corrected.

---

## 8. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-ANTI-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Effective Date** | 2026-06-24 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual / On material adoption feedback |
| **Next Scheduled Review** | 2027-06-24 |
| **Frameworks** | NIST CSF 2.0 (GOVERN) |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG adopters |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 | 2026-06-24 | Governance Pillar Leader | Initial release. Establishes the cross-domain anti-pattern catalog, including workforce, capability, evidence, and compliance failure modes. |

### Review Triggers

- Adoption feedback identifies a recurring failure mode not represented here
- A lessons-learned review identifies a systemic operating-model weakness
- A maturity assessment finds repeated capability overstatement
- A new CERG artifact introduces an anti-pattern callout that should be registered centrally
- Direction from the CISO or Governance Pillar Leader

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Adoption Safety Guide | [`CERG-GOV-IMP-002`](CERG-GOV-IMP-002_Adoption_Safety_Guide.md) | Source of adoption anti-patterns and safety rules |
| CERG Framework | [`CERG-GOV-FRM-001`](CERG-GOV-FRM-001_CERG_Framework.md) | Capability model and evidence-factory framing |
| Job Architecture and Grade Framework | [`CERG-GOV-JA-001`](CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) | Workforce and career-path corrective guidance |
| Evidence Quality Standard | [`CERG-GOV-AUD-001`](CERG-GOV-AUD-001_Evidence_Quality_Standard.md) | Evidence anti-pattern corrective guidance |
| Compliance Matrix | [`CERG-GOV-CMX-001`](CERG-GOV-CMX-001_Compliance_Matrix.md) | Compliance mapping and evidence reuse guidance |
| Program Improvement Register | [`CERG-GOV-IMPREG-001`](CERG-GOV-IMPREG-001_Program_Improvement_Register.md) | Tracks recurring anti-pattern correction actions |

---
