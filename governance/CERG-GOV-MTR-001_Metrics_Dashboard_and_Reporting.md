
## METRICS, DASHBOARD, AND CISO / BOARD REPORTING
### Metrics Dictionary · KRI/KPI Data Source Map · CISO Dashboard · Brief and Report Templates

---

| | |
|---|---|
| **Document ID** | CERG-GOV-MTR-001 |
| **Version** | 1.34 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Reporting) |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [CERG-GOV-CB-001](CERG-GOV-CB-001_Unified_Control_Baseline.md) · [CERG-TMPL-RM-001](../templates/CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md) · [CERG-PRC-VM-001](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) · [CERG-PRC-RM-001](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) · [CERG-GOV-OM-001](CERG-GOV-OM-001_CERG_Operating_Model.md) · [CERG-GOV-RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework.md) · [CERG-PRC-LL-001](../procedures/CERG-PRC-LL-001_Lessons_Learned_and_Program_Improvement_Procedure.md) · [CERG-GOV-IMPREG-001](CERG-GOV-IMPREG-001_Program_Improvement_Register.md) · [CERG-GOV-CEF-001](CERG-GOV-CEF-001_Control_Effectiveness_Framework.md) |
| **Review Cycle** | Annual / On metrics-platform change |
| **Frameworks** | [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (GOVERN) · NIST 800-55 · ISO/IEC 27004 |
| **Regulations** | All - board reporting |
| **Environments** | Program-wide |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Reporting Principles](#2-reporting-principles)
3. [Metrics Dictionary](#3-metrics-dictionary)
4. [KRI / KPI Data Source Map](#4-kri--kpi-data-source-map)
5. [CISO Risk and Posture Dashboard](#5-ciso-risk-and-posture-dashboard)
6. [Quarterly Cyber Oversight Group Brief Template](#6-quarterly-cyber-oversight-group-brief-template)
7. [Monthly CERG Leadership Report Template](#7-monthly-cerg-leadership-report-template)
8. [Anti-Shallow-Metrics Guardrails](#8-anti-shallow-metrics-guardrails)
9. [Cadence and Ownership](#9-cadence-and-ownership)
10. [Threshold Calibration](#10-threshold-calibration)
11. [Document Control](#11-document-control)

---

## 1. Purpose and Scope

[CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) commits the CISO to reporting compliance posture and material risk to executive leadership and the board. The Operating Model defines maturity indicators; the RMF defines KRIs and escalation triggers; the VM and Risk procedures define standing metrics. This document closes the gap between those conceptual metrics and the operational reporting the CISO actually publishes.

It applies to every CERG-produced metric and every CERG-produced report consumed by the Cyber Oversight Group (CISO's reporting line, operating unit leadership, executives, or board depending on org structure), executive leadership, and the board.

---

## 2. Reporting Principles

Five principles govern how CERG reports, in order of priority:

1. **Trend over snapshot.** A single-point metric tells the consumer almost nothing. Every CISO-facing visual shows direction and rate of change.
2. **Heat-map over count.** The consumer wants to know *where* concentration is, not the totalled number. Bands and concentration over raw counts.
3. **Score sum over volume.** Closing 200 Lows while 4 Criticals sit is worse than closing 8 Criticals. CERG reports residual-score weighted sums first, raw counts second.
4. **Compare, then explain.** Operating units against each other; this period against last; us against peer benchmarks where credible. Narrative memos are reserved for the board's specific questions.
5. **Audience-appropriate altitude.** The CISO sees comparison and trend. The Cyber Oversight Group sees the same plus a narrative. The board sees the top five risks and one strategic chart per pillar.

> **What the CISO Does Not Care About**
>
> The CISO does not care that the team scanned 14,000 assets last month. The CISO cares which OU is worse than the others, where the concentration is, whether it's getting better, and what's blocking it. Metrics that don't answer one of those four questions don't reach the dashboard.

---

## 3. Metrics Dictionary

The dictionary is the source-of-truth definition for every CERG metric. Each entry has: ID · Name · Definition · Formula · Source · Owner · Refresh · Threshold (Green/Amber/Red) · Trend Direction · Reported In.

### 3.1 Risk-Side Metrics (Owner: Cyber Risk + Risk Register Owner)

| **ID** | **Name** | **Formula** | **Source** | **Refresh** | **G / A / R** | **Reported In** |
|---|---|---|---|---|---|---|
| 1.31 | 2026-06-14 | Governance Pillar Leader | Moved orphan anti-vanity and program-quality metric sections under §8 so metadata remains at the top of the document and section numbering is deterministic. |
| RM-001 | Open Critical+High Residual Risks | Count of `Status ∈ {Open, In Treatment}` with residual band ≥ High | Risk register | Daily | ≤ 10 / 11–25 / > 25 | CISO Dashboard, COG Brief |
| RM-002 | Residual Risk Score (Sum) | Σ residual score over open risks | Risk register | Daily | ≤ baseline−10% / ±10% / > baseline+10% | CISO Dashboard, Trend Lines |
| RM-003 | Mean Time to Close (High+) | Mean days from `Open` → `Closed/Accepted` for High and Critical | Risk register | Monthly | ≤ 60d / 61–120d / > 120d | CISO Dashboard |
| RM-004 | Exception Backlog | Open exceptions count | Exception register | Weekly | ≤ 25 / 26–60 / > 60 | CISO Dashboard |
| RM-005 | Exception Aging | % of open exceptions older than 12 months | Exception register | Monthly | ≤ 5% / 6–15% / > 15% | CISO Dashboard, COG Brief |
| RM-006 | OU Risk Concentration Index | Std deviation of OU residual-score weighted sums | Risk register | Monthly | ≤ baseline / ±10% / > baseline+10% | CISO Dashboard |
| RM-007 | Scenario Defense Coverage | % of named loss scenarios ([`CJ-001`](CERG-GOV-CJ-001_Crown_Jewel_Register_and_Scenario_Library.md)) where every chain-breaking control is Implemented (CB-001) AND Effective (CEF-001) | CJ-001 + CB-001 + CEF-001 | Quarterly | ≥ 90% / 75–90% / < 75% | CISO Dashboard, COG Brief, Board |

### 3.2 Exposure Management Metrics (Owner: Cyber Risk)

These metrics measure exposure reduction, not scanner activity. They track the pipeline from observation to verified closure.

| **ID** | **Name** | **Formula** | **Source** | **Refresh** | **G / A / R** | **Reported In** |
|---|---|---|---|---|---|---|
| EM-001 | Confirmed Reachable Critical Exposure | Count of exposures in "Confirmed Exposure" or "Material Risk" state with Internet-facing reachability | Exposure pipeline | Daily | 0 / 1–3 / > 3 | CISO Dashboard |
| EM-002 | Observations Awaiting Triage | Count of observations in "Observed" state past their validation SLA | Exposure pipeline | Daily | ≤ 5% / 6–15% / > 15% | CISO Dashboard |
| EM-003 | Critical Observations Downgraded | % of Critical/High CVSS observations reclassified to Hygiene Debt or lower after context validation | Exposure pipeline | Monthly | Informational; no control target | CISO Dashboard |
| EM-004 | KEV with Reachable Path | Count of KEV-matched observations in "Exposure Confirmed" or "Material Risk" state | Exposure pipeline + KEV catalog | Daily | 0 / 1–5 / > 5 | CISO Dashboard |
| EM-005 | KEV Blocked by Verified Control | Count of KEV-matched observations classified as "Confirmed Flaw, Not Exposed" due to verified compensating controls | Exposure pipeline + KEV catalog | Weekly | Watchlist; no control target | CISO Dashboard |
| EM-006 | Exposures on Crown Jewels | Count of confirmed exposures on crown-jewel-classified assets | Exposure pipeline + CJ-001 crown-jewel register | Daily | 0 / 1–2 / > 2 | CISO Dashboard |
| EM-007 | SLA Misses with Compensating Controls | Exposures past SLA where a verified compensating control exists | Exposure pipeline | Weekly | ≤ 5 / 6–15 / > 15 | CISO Dashboard |
| EM-008 | SLA Misses with No Controls | Exposures past SLA with no compensating control | Exposure pipeline | Weekly | 0 / 1–3 / > 3 | CISO Dashboard, COG Brief |
| EM-009 | Observation-to-Decision Time | Median days from observation intake to classification | Exposure pipeline | Monthly | ≤ 3d / 4–7d / > 7d | COG Brief |
| EM-010 | Decision-to-Treatment Time | Median days from classification to treatment selection | Exposure pipeline | Monthly | ≤ 2d / 3–5d / > 5d | COG Brief |

### 3.2a Patch Hygiene Metrics (Owner: Cyber Engineering: Platforms)

Patch hygiene is a maintenance function distinct from exposure reduction. These track platform currency, not risk.

| **ID** | **Name** | **Formula** | **Source** | **Refresh** | **G / A / R** | **Reported In** |
|---|---|---|---|---|---|---|
| PH-001 | Patch Currency Rate | % of assets within their platform-class patch cadence window per [PRC-VM-001](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) §10 | Patch management tool | Weekly | ≥ 95% / 85–95% / < 85% | COG Brief |
| PH-002 | Hygiene Debt by Platform | Count of Hygiene Debt observations, grouped by platform class | Exposure pipeline | Monthly | Trend-only; no control target | COG Brief |
| PH-003 | End-of-Support Count | Assets running software past vendor end-of-support date | Asset inventory | Monthly | 0 / 1–10 / > 10 | COG Brief |

### 3.2b Detection Metrics (Owner: Cyber Risk)

### 3.3 Engineering / Configuration Metrics (Owner: Cyber Engineering)

| **ID** | **Name** | **Formula** | **Source** | **Refresh** | **G / A / R** | **Reported In** |
|---|---|---|---|---|---|---|
| CM-001 | Baseline Drift Rate | % of assets failing DISH baseline | DISH scan | Daily | ≤ 2% / 3–8% / > 8% | CISO Dashboard |
| CM-002 | Architecture Reviews Completed Pre-Production | % of in-scope projects with completed AR before go-live | AR log | Monthly | ≥ 95% / 85–95% / < 85% | CISO Dashboard, COG Brief |
| CM-003 | Citizen-Dev Platforms with Guardrails | % of approved citizen-dev platforms with documented guardrails | Platform register | Quarterly | 100% / 90–100% / < 90% | COG Brief |
| CM-004 | Backup Success Rate (Critical Systems) | % of Critical-tier backups completed successfully | Backup tool | Daily | ≥ 99% / 95–99% / < 95% | CISO Dashboard |
| CM-005 | Restoration Test Currency | % of Tier-1 systems with current restoration test evidence | Resilience register | Quarterly | ≥ 95% / 80–95% / < 80% | CISO Dashboard |

### 3.4 Identity Metrics (Owner: Cyber Engineering: Identity)

| **ID** | **Name** | **Formula** | **Source** | **Refresh** | **G / A / R** | **Reported In** |
|---|---|---|---|---|---|---|
| ID-001 | Phishing-Resistant MFA Coverage (Privileged) | % of privileged accounts with phishing-resistant MFA | IdP | Daily | 100% / 95–100% / < 95% | CISO Dashboard |
| ID-002 | Access Recertification Currency | % of in-scope systems with current recert | IGA | Monthly | ≥ 95% / 85–95% / < 85% | CISO Dashboard |
| ID-003 | Dormant Privileged Accounts | Count of privileged accounts with no use in 60 days | PAM | Weekly | 0 / 1–10 / > 10 | CISO Dashboard |
| ID-004 | Break-Glass Account Hygiene | % of break-glass accounts within rotation policy | PAM | Monthly | 100% / 90–100% / < 90% | CISO Dashboard |
| ID-005 | Identity Assurance Package Currency | % of Tier 1 / regulated / critical identity scopes with current assurance package per STD-AC-001 §2.3 | Evidence library + system inventory | Monthly | ≥ 95% / 85–95% / < 85% | CISO Dashboard, COG Brief |
| ID-006 | External Identity Staleness | Count of vendor, contractor, guest, or federated identities past expiration or inactive >60 days without sponsor attestation | IdP / IGA / TPRM | Weekly | 0 / 1–10 / > 10 | CISO Dashboard |
| ID-007 | NHI Rotation and Ownership Compliance | % of non-human identities with named owner, approved scope, current review date, and compliant rotation / expiration | NHI registry + secrets manager | Monthly | ≥ 95% / 85–95% / < 85% | CISO Dashboard |
| ID-008 | Identity Containment Path Documentation | % of Tier 1 IdP, SaaS, cloud, privileged, and vendor identity paths with documented force-sign-out, token revocation, emergency-disable, and owner escalation steps | Identity assurance package + IR playbook | Monthly | 100% / 95–100% / < 95% | CISO Dashboard, COG Brief |
| ID-009 | Session / Token Containment Test Currency | % of Tier 1 IdP, SaaS, cloud, privileged, and vendor identity paths with tested force-sign-out, token revocation, or emergency-disable path in prior 12 months | IR exercise records + IAM test evidence | Quarterly | ≥ 95% / 80–95% / < 80% | COG Brief |
| ID-010 | Identity Assurance Package Accuracy | % of sampled identity assurance packages where architecture, populations, configured controls, and review evidence match authoritative source exports | Evidence spot-check + IdP / IGA / PAM / SaaS exports | Quarterly | ≥ 95% / 85–95% / < 85% | COG Brief |

### 3.5 Third-Party / Supply Chain Metrics (Owner: Cyber Risk: TPRM)

| **ID** | **Name** | **Formula** | **Source** | **Refresh** | **G / A / R** | **Reported In** |
|---|---|---|---|---|---|---|
| TP-001 | Tier 1 Vendors with Current Attestation | % | TPRM tool | Monthly | ≥ 95% / 85–95% / < 85% | CISO Dashboard |
| TP-002 | SCCT Activations (Trailing 12m) | Count of SCCT activations | TPRM tool | Monthly | n/a - informational | COG Brief |
| TP-003 | International Access Exceptions | Open international-access exceptions | Exception register | Monthly | ≤ baseline / ±20% / > baseline+20% | CISO Dashboard |
| TP-004 | SBOM Coverage (Tier 1 Software) | % of Tier 1 software products with SBOM on file | TPRM tool | Quarterly | ≥ 90% / 75–90% / < 75% | COG Brief |

### 3.6 Governance / Regulatory Metrics (Owner: Cyber Governance)

| **ID** | **Name** | **Formula** | **Source** | **Refresh** | **G / A / R** | **Reported In** |
|---|---|---|---|---|---|---|
| GV-001 | CUI Practices Implemented ([CMMC L2](https://dodcio.defense.gov/CMMC/)) | % of in-scope 800-171 practices `Implemented` (Partial = 0.5) | CUI register | Monthly | 100% / 95–100% / < 95% | CISO Dashboard, Reg Posture |
| GV-002 | Open POA&M Items (CUI) | Count + age of open POA&M | POA&M | Monthly | n/a - age-weighted | Reg Posture |
| GV-003 | NERC-CIP Evidence Library Currency | % of CIP requirements with current evidence ≤ cycle | OT GRC | Monthly | ≥ 98% / 90–98% / < 90% | Reg Posture |
| GV-004 | CIP Deviations Open | Count of approved deviations + average days open | OT GRC | Monthly | n/a | Reg Posture |
| GV-005 | SOX ITGC Control Pass Rate | % of in-scope SOX ITGC tests passed in cycle | SOX program | Quarterly | 100% / 95–100% / < 95% | Reg Posture |
| GV-006 | Policy/Standard Currency | % of CERG-managed artifacts within review cycle | Document Catalog | Monthly | >= 95% / 85-95% / < 85% | CISO Dashboard |

### 3.6a Control Effectiveness Metrics (Owner: Risk + Governance)

These metrics measure whether controls are actually effective, not just present. They bridge the Control Effectiveness Framework ([`CERG-GOV-CEF-001`](CERG-GOV-CEF-001_Control_Effectiveness_Framework.md)) to the metrics dashboard. All three reference the control baseline ([`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md)) statuses and CEF-001 testing cadence.

| **ID** | **Name** | **Formula** | **Source** | **Refresh** | **G / A / R** | **Reported In** |
|---|---|---|---|---|---|---|
| CE-001 | Controls with Current Operating Effectiveness Test | % of `Implemented` controls with a current operating effectiveness test per CEF-001 cadence | CEF-001 testing schedule + CB-001 status | Monthly | >= 90% / 75-90% / < 75% | CISO Dashboard, COG Brief |
| CE-002 | Critical/High Overlay Controls with E3 Evidence | % of Critical/High overlay controls (§8 of CB-001) that have E3 evidence (independent verification per AUD-001) | CB-001 overlay matrix + AUD-001 evidence tier mapping | Monthly | 100% / 90-100% / < 90% | CISO Dashboard, Reg Posture |
| CE-003 | Control Testing Completion vs. Annual Plan | % of planned control tests completed within the current testing cycle per CEF-001 annual plan | CEF-001 testing plan + execution log | Quarterly | >= 95% / 80-95% / < 80% | COG Brief |

> **CE Metrics Depend on CB-001 Status Accuracy.** CE-001 and CE-002 are only as meaningful as the control statuses recorded in CB-001 §4. A control marked `Implemented` without current evidence (or marked `Partially Implemented` when it should be `Implemented`) produces misleading CE scores. The annual Security Control Assessment (SCA) and the quarterly control effectiveness review serve as cross-checks on status accuracy.

### 3.7 Predictive and Leading Indicators (Owner: Governance Pillar Leader, with Risk and Engineering inputs)

The metrics above are lagging indicators : they tell you what already happened. An Adaptive program also tracks predictive indicators that warn of trouble before it materializes. The following leading indicators complement the lagging dictionary. When any leading indicator breaches its defined threshold, it triggers a review at the quarterly Lessons Aggregation Review (PRC-LL-001 Section 5).

| **ID** | **Name** | **Formula** | **Why Predictive** | **Source** | **Refresh** | **G / A / R** | **Reported In** |
|---|---|---|---|---|---|---|---|
| PL-001 | Mean Time to Exploit vs. Patch Velocity | (Avg days from CVE publication to known exploit) / (Avg days from CVE publication to patch deployment) | When ratio > 1.0, attackers are faster than patching. Trend direction predicts incident probability. | Exposure pipeline + threat intelligence | Monthly | <= 0.5 / 0.5-1.0 / > 1.0 | CISO Dashboard, COG Brief |
| PL-002 | Attack Surface Change Rate | (New externally-facing assets + decommissioned assets + changed services this month) / total externally-facing assets | Rapid surface expansion without corresponding review capacity predicts exposure gaps. | Asset inventory + CMDB | Monthly | <= 5% / 5-15% / > 15% | CISO Dashboard |
| PL-003 | Near-Miss Rate (Trailing Quarter) | Count of events that met detection thresholds but were contained before impact, per quarter | Rising near-miss rate can predict an incident when controls fatigue or coverage gaps align. A flat or falling rate after mitigations confirms effectiveness. | Near-miss log (PRC-LL-001) | Quarterly | n/a: informational; trend is the signal | COG Brief |
| PL-004 | Threat-Intelligence-Tilted Risk Score | Sum of (risk score x TI confidence x sector targeting relevance) for top 20 risks | Incorporates whether threat actors are actively targeting the sector with TTPs relevant to each risk. Higher tilt = stronger alignment between risk register and threat landscape. | Risk register + TI assessment | Quarterly | n/a: informational; rising tilt demands attention | COG Brief |
| PL-005 | Control Coverage vs. Threat Coverage | % of top 10 MITRE ATT&CK techniques for the sector that map to an operational CERG control | A falling percentage means threat evolution is outpacing control evolution : a predictive gap signal. | TRC-001 + ATT&CK mapping | Quarterly | >= 80% / 60-80% / < 60% | COG Brief |
| PL-006 | Unpatched Vulns with Known Exploit | Count of open vulnerabilities where CISA KEV or vendor confirms active exploitation, regardless of CVSS score | More predictive than raw vulnerability count: these are the vulnerabilities attackers are actually using in the wild. | Exposure pipeline + CISA KEV | Daily | 0 / 1-5 / > 5 | CISO Dashboard |
| PL-007 | Privileged Account Anomaly Rate | % of privileged sessions flagged as anomalous by UEBA or behavioral rules | Rising anomaly rate without corresponding investigation capacity predicts credential misuse incidents. | PAM / UEBA tool | Weekly | <= 2% / 2-5% / > 5% | CISO Dashboard |

> **Leading Indicators Are Early Warning, Not Precision Instruments**
>
> A leading indicator does not need to be precise to be useful. It needs to change direction before the lagging indicator it predicts, and it needs to produce a signal the program can act on. PL-003 (near-miss rate) rising over three consecutive quarters is a signal even if the exact incident probability is unknown. The program that waits for precision misses the window to act.

#### Minimum Viable Data Pipelines for PL Metrics

Each predictive indicator requires correlation across multiple data sources. The following MVP pipelines define the automated data path that makes each metric continuously producible, not reliant on manual quarterly analysis:

| Metric | MVP Pipeline | Automation Level | Manual Fallback |
|--------|-------------|-----------------|-----------------|
| **PL-001** (MTTE vs Patch Velocity) | CISA KEV feed → vulnerability scanner API → patch management API → daily ratio calculation | Full (API-driven) | Monthly CISA KEV download + manual spreadsheet ratio |
| **PL-002** (Attack Surface Change Rate) | CMDB/asset API → daily snapshot → delta comparison vs prior day | Full (API-driven) | Monthly manual asset export + spreadsheet delta |
| **PL-003** (Near-Miss Rate) | Near-miss log (PRC-LL-001) → metrics platform → quarterly aggregation | Partial (log capture automated; classification manual) | Quarterly manual review of incident log |
| **PL-004** (TI-Tilted Risk Score) | Risk register API + TI platform feed → weighted score calculation | Partial (risk data automated; TI confidence manual) | Quarterly Risk + TI lead workshop |
| **PL-005** (Control vs Threat Coverage) | ATT&CK mapping file (maintained by Detection Engineer) + detection rule registry → quarterly coverage % | Partial (registry automated; mapping manual) | Quarterly ATT&CK mapping review |
| **PL-006** (Unpatched Vulns with Known Exploit) | CISA KEV feed + vulnerability scanner API → daily intersection (KEV ∩ open vulns) | Full (API-driven) | Weekly CISA KEV check + manual scanner query |
| **PL-007** (Privileged Account Anomaly Rate) | PAM/UEBA tool API → weekly anomaly % calculation | Full (API-driven) | Monthly PAM report export + manual percentage |

> **MVP Pipeline Priority.** Implement PL-006 (CISA KEV intersection) first — it has the highest automation potential and the clearest operational value. PL-001 and PL-004 follow. PL-003 and PL-005 can remain partially manual until maturity warrants automation investment.

### 3.8 Knowledge Management Metrics (Owner: Governance Pillar Leader)

Knowledge "in the system" means knowledge that survives when the person who holds it is unavailable. These metrics measure whether critical knowledge is documented and transferable.

| **ID** | **Name** | **Formula** | **Source** | **Refresh** | **G / A / R** | **Reported In** |
|---|---|---|---|---|---|---|
| KM-001 | Procedure Documentation Currency | % of critical processes with current (<= 12 month) procedure documentation. "Critical" means the procedure supports a control marked Implemented in CB-001. | Document Catalog + procedure review dates | Quarterly | >= 95% / 85-95% / < 85% | CISO Dashboard |
| KM-002 | Role Backup Currency | % of canonical roles (OM-001 Section 6.1) with a documented secondary or backup who has performed the role in an exercise or real event within 18 months | Cross-training log | Annual | >= 90% / 75-90% / < 75% | COG Brief |
| KM-003 | Cross-Training Hours per Team Member | Mean cross-pillar knowledge activity hours per CERG team member per quarter. Target: >= 4 hours per quarter (OM-001 Section 10.4). | Cross-training log | Quarterly | >= 4.0 / 2.0-4.0 / < 2.0 | CISO Dashboard |

### 3.9 CERG Service Responsiveness Metrics (Owner: CISO / Pillar Leaders)

These metrics hold CERG accountable to its own service-level commitments ([`CERG-GOV-SLC-001`](CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md)). They are reported alongside, and with equal weight to, the discipline metrics that measure the business. Targets reference the SLC-001 commitment values, which are preliminary defaults until organizationally calibrated.

| **ID** | **Name** | **Formula** | **Source** | **Refresh** | **G / A / R** | **Reported In** |
|---|---|---|---|---|---|---|
| SR-001 | Architecture Review Turnaround | Median business days from complete AR intake to disposition, by project tier | AR log / intake system | Monthly | <= SLC target / 1-2x target / > 2x target | CISO Dashboard, COG Brief |
| SR-002 | Advisory Response Time | Median business days from advisory request to substantive written response | Intake system | Monthly | <= 3d / 4-7d / > 7d | CISO Dashboard |
| SR-003 | Intake Disposition Time | Median business days from project / SaaS intake to security disposition | Intake system | Monthly | <= SLC target / 1-2x target / > 2x target | CISO Dashboard, COG Brief |
| SR-004 | SLC Commitment Adherence | % of CERG requests answered within the published SLC-001 commitment | Intake system | Monthly | >= 90% / 75-90% / < 75% | CISO Dashboard, COG Brief, Board |
| SR-005 | Time-to-Coverage | Median days from asset go-live to exposure-management / CSPM coverage | Exposure pipeline + asset inventory | Monthly | <= 5d / 6-15d / > 15d | COG Brief |

#### Adoption-Phase SLA Targets

New adopters have no baseline. SR metrics are reported with phase context so that Red during initial adoption is understood as transitional, not program failure. SR-004 (SLC Commitment Adherence) uses the phase-adjusted target, not the mature target, for its G/A/R band.

| Phase | Architecture Review (SR-001) | Advisory Response (SR-002) | Intake Disposition (SR-003) | Time-to-Coverage (SR-005) |
|-------|----------------------------|---------------------------|----------------------------|--------------------------|
| **Gate 1 (Spine, 0–90 days)** | 15 business days | 10 business days | 15 business days | 15 business days |
| **Gate 2 (Operating, 90–180 days)** | 10 business days | 5 business days | 10 business days | 10 business days |
| **Gate 3+ (Governed / Adaptive)** | Per SLC-001 §3.1 | Per SLC-001 §3.3 (3 business days) | Per SLC-001 §3.1 / §3.3 | Per SLC-001 §3.2 (5 business days) |

> **Phase-Context Reporting.** The CISO Dashboard reports SR metrics with a phase-context indicator (e.g., "Gate 1 — transitional target"). The COG Brief includes the phase label in the SR-001 through SR-005 tiles. Phase advancement is recorded in the adoption gates document ([`CERG-GOV-IMP-005`](CERG-GOV-IMP-005_Adoption_Decision_Tree_and_Dependency_Matrix.md)).

---

## 4. KRI / KPI Data Source Map

The data source map tells the reporting team where each metric's underlying data comes from, who keeps it healthy, and what happens when it breaks.

| **Metric IDs** | **Primary System of Record** | **Owning Role** | **Refresh Path** | **Failure Mode** |
|---|---|---|---|---|
| RM-001 – RM-006 | Risk register tool | Risk Register Owner | Nightly extract → metrics platform | Stale ETL: hold the day's CISO Dashboard, raise an Amber data-quality flag. |
| EM-001 – EM-010 | Exposure pipeline (scanner, CSPM, SSPM, SCA, KEV, reachability context) | Exposure Management Lead | Hourly API / pipeline export → metrics platform | Source outage: fall back to last-known-good snapshot with timestamp banner. |
| DT-001 – DT-003 | SIEM + detection coverage tool | Cyber Risk - Detection | Nightly source inventory + detection registry export | Missing source: detection coverage shown as Red. |
| CM-001 – CM-005 | Configuration / VM / Backup tools | Cyber Engineering - Platforms / Resilience | Nightly aggregation | Backup tool outage: pull from job log; flag as Amber. |
| ID-001 – ID-010 | IdP / IGA / PAM / NHI registry / secrets manager / evidence library / TPRM | Identity Engineer + IAM Operator + Evidence Librarian | Nightly export for operational metrics; monthly evidence-library reconciliation | Source change: re-baseline before publishing; missing package evidence reports Red until reconciled. |
| TP-001 – TP-004 | TPRM tool | Cyber Risk - TPRM | Daily/weekly export | - |
|| GV-001 – GV-006 | CUI register / OT GRC / SOX program / Document Catalog | Cyber Governance - domain owners | Monthly publish | - |
|| PL-001 – PL-007 | See §3.7 MVP pipelines: CISA KEV feed, vulnerability scanner API, patch management API, CMDB, near-miss log, risk register, TI platform, ATT&CK mapping, PAM/UEBA | Governance Pillar Leader (aggregation) + Risk (data sources) | Daily (PL-001, PL-006); Weekly (PL-002, PL-007); Quarterly (PL-003, PL-004, PL-005) | Source API outage: fall back to manual fallback per §3.7 MVP table; flag as Amber data-quality |

> **One Source per Metric**
>
> Each metric has exactly one system of record. Where two systems disagree, the system named here is authoritative and the other is reconciled. Reports that average two disagreeing sources hide the truth.

---

## 5. CISO Risk and Posture Dashboard

The CISO dashboard is the single page that opens every monthly review. It is laid out around the five standing views defined in [`CERG-TMPL-RM-001`](../templates/CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md) Section 7, plus the regulatory posture strip.

```
┌────────────────────────────────────────────────────────────────────────┐
│  CISO RISK & POSTURE - <Month> <YYYY>                                  │
├────────────────────────────────────────────────────────────────────────┤
│  TREND LINES (13-mo rolling)                                           │
│  · Residual Score Sum (RM-002)        ▁▂▃▄▄▅▆▇▆▅▄▄▃    ↓             │
│  · Critical+High Open Count (RM-001)  ▆▆▅▅▄▄▄▃▃▃▃▂▂   ↓             │
│  · Mean Time to Close H+ (RM-003)     ▂▃▄▅▅▄▃▃▃▂▂▂▂   ↓             │
├────────────────────────────────────────────────────────────────────────┤
│  OU SCORECARD (residual-score weighted, ranked)                        │
│  OU         │ Crit │ High │  Σ  │ Δ vs prior │ Trend │ Exc │ SLA breach│
│  Gen Ops    │   2  │   8  │ 184 │     -12    │  ↓    │  6  │     1     │
│  Trans Ops  │   1  │   5  │ 121 │      +4    │  ↑    │  3  │     2     │
│  Dist Ops   │   0  │   4  │  98 │      -3    │  →    │  4  │     0     │
│  Corp IT    │   1  │   3  │  85 │      -7    │  ↓    │  9  │     0     │
│  CUI Enclave│   0  │   2  │  46 │      -2    │  →    │  1  │     0     │
├────────────────────────────────────────────────────────────────────────┤
│  OU × FAMILY HEAT MAP (Critical+High concentration)                    │
│           AC  AU  CM  CP  IA  RA  SC  SI  SR                           │
│  Gen Ops  .   .   ▓▓  .   ▓   .   ▓▓  ▓   .                           │
│  Trans    .   .   ▓   .   .   .   ▓▓  ▓   .                           │
│  ...                                                                   │
├────────────────────────────────────────────────────────────────────────┤
│  TOP 10 RISKS                                                          │
│  ID         │ OU       │ Score │ Age │ Owner       │ Next Milestone   │
│  R-2026-0048│ Gen Ops  │  12   │ 91d │ Gen Ops Dir │ MFA wave 1 - Q3  │
│  ...                                                                   │
├────────────────────────────────────────────────────────────────────────┤
│  REGULATORY POSTURE                                                    │
│  CUI/CMMC L2 │ Practices: 92%  POA&M open: 18 (mean 67d)  Assessor: H1│
│  NERC-CIP    │ Evidence currency: 96%  Deviations open: 3              │
│  SOX ITGC    │ Test pass rate: 98%  Open deficiencies: 1               │
└────────────────────────────────────────────────────────────────────────┘
```

The dashboard is published from the metrics platform; the ASCII above is the layout reference for designers and dashboard builders. Color rules follow Section 3 Green/Amber/Red bands.

---

## 6. Quarterly Cyber Oversight Group Brief Template

The Cyber Oversight Group is whoever the CISO reports to, depending on org structure, it is IT and OU leadership, executive leadership, or the board itself. The brief is identical in structure regardless of audience; depth is calibrated by audience.

```
QUARTERLY CYBER OVERSIGHT GROUP BRIEF - Q<n> <YYYY>

1. EXECUTIVE TAKEAWAY (1 page max)
   · Are we more or less exposed than last quarter? Why?
   · The one decision the group needs to make this quarter.

2. STATE OF RISK
   · Trend Lines slide (RM-002, RM-001, RM-003)
   · OU Scorecard
   · Top 10 Risks with one-line status per risk

3. STATE OF THE PROGRAM
   · Maturity indicators against [CERG-GOV-OM-001](CERG-GOV-OM-001_CERG_Operating_Model.md) targets
   · CERG capability deltas this quarter (people, tooling, scope expansion)

4. REGULATORY POSTURE
   · CUI / NERC-CIP / SOX one-line state each
   · Upcoming assessments / audits with dates and gating issues

5. INCIDENTS AND NEAR-MISSES (CERG-facing summary; full IR report separate)
   · Material events this quarter; lessons learned actioned

6. ASKS
   · Decisions, funding, scope, or organizational moves required from the group

7. APPENDIX
   · OU × Family Heat Map
   · Standing dashboard exports
   · Risk register changes since last brief
```

The brief is published five business days before the meeting. Slides are read-ahead; the meeting is for discussion of the Asks.

### 6.1 Control Funding Decision Brief Pattern

Use this one-page pattern when a control gap, repeated metric miss, overdue treatment, or risk acceptance requires a business funding or prioritization decision. The brief is a decision aid, not a replacement for the risk register, control baseline, or acceptance form.

| **Field** | **Content** |
|---|---|
| Decision Needed | `[Fund / defer / reduce scope / accept residual risk / retire service / other]` |
| Control or Risk Link | `[CB-001 control ID, risk ID, finding ID, or metric ID]` |
| Business Capability Affected | `[System, process, customer obligation, regulatory scope]` |
| Current Exposure | `[Plain-language consequence and residual rating]` |
| Recommended Treatment | `[Control, project, staffing, tool, vendor, process change]` |
| Funding / Capacity Ask | `[Amount, FTE, team capacity, vendor spend, schedule slot]` |
| Options Considered | `[Option A/B/C with risk and cost tradeoff]` |
| Decision Deadline | `[Date and reason: SLA, audit date, contract, threat activity, go-live]` |
| If Approved | `[Expected risk reduction, metric movement, evidence produced]` |
| If Deferred or Declined | `[Risk acceptance required? expiration? escalation?]` |
| Named Owners | `[Business Owner, treatment owner, CERG reviewer]` |

If the decision is to defer treatment while residual risk remains, route the resulting acceptance through [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) and [`CERG-TMPL-RM-004`](../templates/CERG-TMPL-RM-004_Risk_Acceptance_Request_Form.md). Funding denial is not itself a risk acceptance; the Business Owner or required RMF-001 authority must explicitly accept the consequence.

---

## 7. Monthly CERG Leadership Report Template

The internal CERG leadership report is consumed by Engineering / Risk / Governance pillar owners and the CISO. It is operational where the CISO Dashboard is comparative.

```
MONTHLY CERG LEADERSHIP REPORT - <Month> <YYYY>

A. SCORECARD vs. METRIC TARGETS
   · Full Section 3 dictionary, this month, with G/A/R indicator and 3-month spark

B. THIS MONTH'S DELTAS
   · Metrics that moved out of Green
   · Metrics that recovered into Green
   · Net new risks ≥ High and exceptions opened

C. PILLAR HIGHLIGHTS (one paragraph each)
   · Engineering - projects intaken, ARs completed, baselines deployed
   · Risk - VM trends, vendor activity, adversarial validation results
   · Governance - policy/standard changes, regulatory milestones, audit interactions

D. CROSS-PILLAR ITEMS
   · Items where ownership is unclear or work is blocked across pillars

E. NEXT MONTH
   · Top three deliverables and named owner
```

---

## 8. Anti-Shallow-Metrics Guardrails

The guardrails below define how CERG avoids vanity metrics and program-health blind spots.

### 8.1 Metrics That Should Not Be Used Alone

The following metrics are commonly reported but are easily gamed, misinterpreted, or disconnected from actual risk reduction. If you report them, pair them with a companion metric that provides context.

| Vanity Metric | Why It Misleads | Pair With |
|--------------|----------------|-----------|
| Number of vulnerabilities closed | Rewards volume over severity. A team closing 100 Low findings looks better than a team closing 3 Criticals. | Exposure age by asset criticality; % of Critical/High findings past SLA |
| Number of phishing emails blocked | Your email gateway blocks 99% of phishing — the 1% that gets through is what matters. | Phishing simulation click rate; time from phish report to containment |
| Number of policies published | Publishing policies is not implementing controls. | % of controls with current evidence (E2+) |
| Number of alerts generated | Alert volume is noise. Signal is what matters. | Detection signal-to-noise ratio; % of alerts resulting in validated incidents |
| Number of vendors reviewed | A checkbox review of 100 vendors is worse than a thorough review of 10 high-risk vendors. | % of high-risk vendors with current assessment; vendor risk concentration |
| Percent compliant without evidence quality | "95% compliant" based on policy existence, not control operation. | % of controls with E3 evidence; % of evidence current |
| Training completion rate | Completion proves attendance, not comprehension or behavior change. | Phishing simulation results; incident root causes tracing to human error |

### 8.2 Program Quality Metrics

These metrics measure whether the CERG program itself is healthy — not whether individual controls are operating.

| Metric | What It Measures | Target |
|--------|-----------------|--------|
| % of risks with named business owner (not security) | Business accountability for risk | >90% |
| % of exceptions with expiration date | Exception discipline | 100% |
| % of control evidence current (within freshness window) | Evidence freshness | >85% |
| % of Tier 0/Tier 1 assets with tested recovery | Resilience readiness | >95% |
| % of high-risk vendors reviewed on schedule | Vendor risk currency | >90% |
| % of adopted documents reviewed on schedule | Document governance | >80% |
| Number of "Approved" documents with "Pending" approver | Governance hygiene | 0 |
| Number of unresolved template values in approved documents | Operational readiness | 0 in adopted documents |
| % of findings with a named owner assigned within SLA | Accountability timeliness | >90% |
| % of accepted risks past expiration without review | Risk acceptance discipline | 0% |
| % of recurring findings (same vulnerability, same system, >2 times) | Remediation effectiveness | <10% of total findings |
| Average time from finding identification to owner assignment | Triage responsiveness | <SLA for severity |
| Number of SLA breaches by pillar per month | Pillar performance | Trending down |

### 8.3 Guardrail Rules

The guardrails baked into the metric definitions and reporting views above:

1. **Score sum first, count second.** Headline figures are residual-score weighted (RM-002), not raw count.
2. **Partial = 0.5, not 1.** Regulatory implementation percentages count Partially Implemented as half. (Forces honesty.)
3. **Age weighting on regulatory openness.** POA&M items report mean age, not just count.
4. **Decision and treatment velocity, not closure count.** EM-009 and EM-010 show whether exposure work is moving through the pipeline, so closing 200 Lows doesn't mask 4 Criticals stalled before treatment.
5. **Concentration over volume.** OU heat map colors on Critical+High concentration, not total findings.
6. **No "scanned X assets" headlines.** Activity metrics are operational, never on the CISO dashboard.
7. **Trend direction is the headline.** Every CISO-facing metric carries a 13-month spark or arrow.
8. **Bands published with the metric.** Green/Amber/Red bands are part of the definition; moving them requires a change request, not an editorial decision.

> **A Metric That Can't Show "Worse" Should Not Be Reported**
> If a metric is structured such that good operating units always look good and bad ones can hide, it's vanity. CERG either reframes the metric to expose the gap or removes it from the dashboard.

---

## 9. Cadence and Ownership

| **Metric Group** | **Owner** | **Cadence** | **Audience** |
|---|---|---|---|
| RM-001 through RM-006 (Risk) | Risk Register Owner | Risk posture review: weekly for High/Critical; monthly for full register | CISO, Risk Pillar Leader |
| EM-001 through EM-010 (Exposure Management) | Exposure Management Lead | Daily dashboard update; monthly trend report | CISO, Risk Pillar Leader |
| DT-001 through DT-003 (Detection) | Detection Engineer | Monthly | Risk Pillar Leader, CISO |
| CM-001 through CM-005 (Engineering) | Engineering Pillar Leader | Daily for CM-001, CM-004; monthly for others; quarterly for CM-003, CM-005 | CISO, Engineering Pillar Leader |
| ID-001 through ID-010 (Identity) | Identity Engineer + IAM Operator | Daily for ID-001; weekly for ID-003 and ID-006; monthly for ID-002, ID-004, ID-005, ID-007, ID-008; quarterly for ID-009 and ID-010 | CISO, Identity Engineer, IAM Operator |
| TP-001 through TP-004 (Third-Party) | Vendor Risk Analyst | Monthly; quarterly for TP-004 | Risk Pillar Leader, CISO |
| GV-001 through GV-006 (Governance) | Governance Pillar Leader | Monthly; quarterly for GV-005 | CISO, Governance Pillar Leader |
|| PL-001 – PL-007 (Predictive) | Governance Pillar Leader, with Risk and Engineering inputs | Monthly for PL-001, PL-002, PL-006; weekly for PL-007; quarterly for PL-003, PL-004, PL-005 | CISO, COG Brief |
|| CE-001 – CE-003 (Control Effectiveness) | Risk Pillar Leader + Governance Pillar Leader | Monthly for CE-001, CE-002; quarterly for CE-003 | CISO, COG Brief |

The Governance Pillar Leader owns the metrics program overall and is accountable for dashboard accuracy, timely publication, and threshold governance.

---

## 10. Threshold Calibration

The metric thresholds in Section 3 are not permanent. An Adaptive program adjusts its own measurement yardstick as the program matures, the threat landscape shifts, and risk appetite changes. Thresholds that were appropriate for an Informed program may be too loose for a Repeatable program and too tight for a newly adopted one.

### 10.1 Calibration Cadence

Thresholds are reviewed:

- **Annually**, aligned with the risk appetite review (GOV-RMF-001)
- **When triggered** by any of the conditions in Section 10.2

### 10.2 Calibration Triggers

| Trigger | Condition | Action |
|---|---|---|
| **Green drift** | A metric has been green for 6+ consecutive months | Tighten the threshold to drive improvement. Exception: the metric has reached its theoretical maximum (e.g., 100% MFA coverage). |
| **Red stall** | A metric has been red for 3+ consecutive months and no improvement actions are in progress | Either escalate to the CISO with a remediation demand, or recalibrate if the threshold was set unrealistically. A metric that is permanently red without program response is noise, not measurement. |
| **Risk appetite change** | Risk appetite tightens or loosens in a domain (per RMF-001) | Corresponding metric thresholds tighten or loosen proportionally. |
| **Maturity improvement** | The maturity scorecard (MAT-001) shows domain improvement (e.g., Partial to Repeatable) | Relevant metric thresholds are reviewed for tightening. A domain that has matured should be held to a higher standard. |
| **External benchmark** | Peer benchmarking data (PRC-TI-001 Section 10.2) shows a significant gap | Threshold is reviewed against the peer norm. |

### 10.3 Calibration Rules

1. **Tighten, do not loosen without cause.** The default direction is tighter. A threshold is only loosened when: the metric was set unrealistically and cannot be met after documented good-faith effort, or risk appetite explicitly relaxes in the domain.
2. **One change at a time.** When multiple calibration triggers fire simultaneously, change one threshold per domain per quarter. Changing multiple thresholds simultaneously makes it impossible to determine which change drove which outcome.
3. **Communicate before enforcing.** When a threshold changes, the affected metric owners and the CISO are notified before the new threshold takes effect. The next reporting period shows both the old and new threshold for transition.

### 10.4 Threshold Change Log

The Governance Pillar Leader maintains a threshold change log. Every change records:

| Field | Example |
|---|---|
| Metric ID | EM-001 |
| Date changed | 2026-09-01 |
| Old threshold (Red) | > 5 |
| New threshold (Red) | > 2 |
| Trigger | Green drift : metric was green for 8 consecutive months |
| Rationale | The program has consistently met the original threshold; tightening drives further improvement |
| Approver | Governance Pillar Leader |

The change log is reviewed at the annual metrics program review and is available to auditors as evidence of program evolution.

### 10.5 Integration

Threshold changes are recorded as improvement register entries (IMPREG-001, type: Metric or threshold change) when they represent a deliberate program improvement, not just a routine calibration. A threshold tightened due to green drift is a program improvement; a threshold corrected because it was set incorrectly from the start is a bug fix. Both are documented; only the former is an improvement.

---

## 11. Document Control

| | |
|---|---|
| **Document ID** | CERG-GOV-MTR-001 |
| **Version** | 1.34 |
| **Approved By** | CISO |
| **Next Review** | Annual / metrics-platform change |
| **Change Log** | 1.0 - Initial publication. Establishes dictionary, source map, CISO dashboard, briefs, and anti-shallow guardrails. · 1.1 - Added Section 3.7 Predictive and Leading Indicators (PL-001 through PL-007). · 1.2 - Restored Section 9 Cadence and Ownership. · 1.3 - Added Section 10 Threshold Calibration: cadence, triggers, rules, change log, and improvement register integration. · 1.32 - Added §6.1 Control Funding Decision Brief pattern for business funding/prioritization decisions tied to control gaps and risk treatments. · 1.33 - Expanded identity metrics ID-005 through ID-008 for identity assurance package currency, external identity staleness, NHI compliance, and session/token containment readiness. · 1.34 - Split session/token containment into documented-path and tested-path metrics, and added identity assurance package accuracy spot-check metric. |

