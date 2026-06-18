# SURGE: Cyber Engineering, Risk & Governance

## CALIBRATION CHECKLIST
### Consolidated Preliminary Default Register

---

| | |
|---|---|
| **Document ID** | CERG-GOV-CAL-002 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Policy & Standards) |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on any change to the risk appetite calibration |
| **Frameworks** | NIST CSF 2.0 (GOVERN); ISO/IEC 27001 A.6.1 |
| **Regulations** | Cross-cutting |
| **Environments** | Program-wide |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Using This Checklist](#2-using-this-checklist)
3. [Risk Appetite and Impact Calibration (RMF-001)](#3-risk-appetite-and-impact-calibration-rmf-001)
4. [Service Level Commitment Calibration (SLC-001)](#4-service-level-commitment-calibration-slc-001)
5. [Metric Threshold Calibration (MTR-001)](#5-metric-threshold-calibration-mtr-001)
6. [Crown Jewel Scenario Calibration (CJ-001)](#6-crown-jewel-scenario-calibration-cj-001)
7. [Risk Acceptance Duration Calibration (RMF-001)](#7-risk-acceptance-duration-calibration-rmf-001)
8. [Calibration Governance](#8-calibration-governance)
9. [Document Control](#9-document-control)

---

## 1. Purpose and Scope

The CERG framework embeds **preliminary defaults requiring organizational calibration** across multiple documents. These defaults are educated starting points for a mid-market organization; they are not approved values until calibrated against the organization's specific risk profile, staffing, and financial context. A program that operates on uncalibrated defaults makes decisions against thresholds that do not reflect its actual exposure.

This document consolidates **every preliminary default** in the CERG corpus into a single register. It identifies each parameter, its default value, the calibration inputs required, the calibration method, the owning role, and the review cadence.

It is the authoritative reference for the organization's calibration status. Adopting teams use this checklist during adoption (IMP-001 §5) and maintain it as the calibration maturity tracker.

> **Calibration Is Not Optional**
>
> Risk acceptance decisions made against uncalibrated values are opinions, not risk management. SLA commitments made against uncalibrated values are promises the organization may not be able to keep. Every preliminary default in this register must have either a calibrated value or a documented plan for calibration, with a target date, before the CISO signs the adoption gate.

---

## 2. Using This Checklist

### 2.1 Register Structure

Each calibration item records:

| Field | Description |
|-------|-------------|
| **Parameter** | The value that requires calibration |
| **Document** | Source document containing the default |
| **Section** | Section reference in the source document |
| **Default Value** | The uncalibrated starting value |
| **Calibration Inputs** | Organizational data required to determine the calibrated value |
| **Calibration Method** | How inputs are combined to produce the calibrated value |
| **Owning Role** | Canonical role responsible for calibration |
| **Review Cadence** | How often the calibrated value is reviewed |
| **Organization Value** | (To be filled) The organization's calibrated value |
| **Last Calibrated** | (To be filled) Date of last calibration |
| **Next Review** | (To be filled) Date of next scheduled review |

### 2.2 Calibration Priority

- **Gate 2 (Operating)** — Risk appetite bands and impact thresholds must be calibrated before operating risk acceptance.
- **Gate 3 (Governed)** — SLA commitments and metric thresholds must be calibrated before publishing SLAs.
- **Gate 4 (Adaptive)** — All remaining defaults should be calibrated, including scenario-specific figures.

### 2.3 Verification

At each adoption gate review, the Governance Pillar Leader (Policy & Standards) presents the calibration register with current status for each item. Items that remain uncalibrated must be accompanied by a documented plan and target date.

---

## 3. Risk Appetite and Impact Calibration (RMF-001)

### 3.1 Loss Magnitude (Impact) Bands

| Field | Value |
|-------|-------|
| **Parameter** | Loss Magnitude bands (Catastrophic / Major / Medium / Minor / Negligible) |
| **Document** | [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.5 |
| **Section** | §9.5 — Impact (LM) bands |
| **Default Value** | Catastrophic >$10M · Major $1M–$10M · Medium $100K–$1M · Minor $10K–$100K · Negligible <$10K |
| **Calibration Inputs** | Annual revenue; critical service downtime cost (per hour); regulatory fine exposure (per incident); cyber insurance retention; cyber insurance coverage limit; board reporting materiality threshold |
| **Calibration Method** | Ratio of revenue × risk factor. Small org ($100M rev) at ~5% revenue; mid-market ($500M–$2B) at midpoint; large ($5B+) at ~2%. Calibration workbook in RMF-001 §9.8.1 provides structured prompts. |
| **Owning Role** | Governance Pillar Leader (Policy & Standards) coordinates with Finance (CFO office) |
| **Review Cadence** | Annual; on material change to revenue, insurance, or regulatory exposure |
| **Organization Value** | |
| **Last Calibrated** | |
| **Next Review** | |

### 3.2 Annualized Loss Exposure (ALE) Tolerance Bands

| Field | Value |
|-------|-------|
| **Parameter** | Total open ALE (Critical + High) — OK / Caution / Escalate |
| **Document** | [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.8 |
| **Section** | §9.8 — Quantitative tolerance (preliminary calibration) |
| **Default Value** | OK <$5M · Caution $5M–$15M · Escalate >$15M |
| **Calibration Inputs** | Same as §3.1 above |
| **Calibration Method** | Revenue-gated scaling per workbook in §9.8.1. Small (<$100M rev): OK <$500K, Caution $500K–$2M, Escalate >$2M. Mid: <$5M / $5M–$15M / >$15M. Large: <$25M / $25M–$100M / >$100M. |
| **Owning Role** | Governance Pillar Leader (Policy & Standards) coordinates with Finance |
| **Review Cadence** | Annual; on revenue change or material risk change |
| **Organization Value** | |
| **Last Calibrated** | |
| **Next Review** | |

### 3.3 Single-Risk ALE Mandatory CISO Review Threshold

| Field | Value |
|-------|-------|
| **Parameter** | Single-risk ALE requiring mandatory CISO review |
| **Document** | [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.8 |
| **Section** | §9.8 table — Single-risk ALE |
| **Default Value** | >$2M |
| **Calibration Inputs** | Revenue; insurance retention; maximum single-incident loss tolerance |
| **Calibration Method** | Revenue-proportional: Small >$250K · Mid >$2M · Large >$10M |
| **Owning Role** | Governance Pillar Leader (Policy & Standards) |
| **Review Cadence** | Annual |
| **Organization Value** | |
| **Last Calibrated** | |
| **Next Review** | |

---

## 4. Service Level Commitment Calibration (SLC-001)

### 4.1 Architecture Review Turnaround

| Field | Value |
|-------|-------|
| **Parameter** | Architecture review turnaround time |
| **Document** | [`CERG-GOV-SLC-001`](CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md) §3.1 |
| **Section** | §3.1 — Project Engagement — Architecture review disposition |
| **Default Value** | Tier 1 (high-impact/regulated/OT/AI): 10 business days · Tier 2 (standard): 7 business days · Tier 3 (minimal): 5 business days |
| **Calibration Inputs** | Staffing levels; intake volume; average review complexity; regulatory deadlines |
| **Calibration Method** | Measure actual turnaround over 2 complete quarters; set targets at P80 of actual performance; tighten as staffing grows. Adoption-phase SLA targets in SLC-001 §3.5 provide graduated defaults (15/10/5 business days for Gates 1/2/3). |
| **Owning Role** | Engineering Pillar Leader (coordinates with Risk and Governance) |
| **Review Cadence** | Annual; on material staffing change |
| **Organization Value** | |
| **Last Calibrated** | |
| **Next Review** | |

### 4.2 Continuous Service Coverage SLA

| Field | Value |
|-------|-------|
| **Parameter** | New asset vulnerability/CSPM coverage establishment |
| **Document** | [`CERG-GOV-SLC-001`](CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md) §3.2 |
| **Section** | §3.2 — Continuous Service |
| **Default Value** | Coverage established within 5 business days of go-live notification |
| **Calibration Inputs** | Tooling maturity; onboarding automation; staffing; asset churn rate |
| **Calibration Method** | Measure actual coverage establishment time over 2 quarters; set internal target based on tooling capability. |
| **Owning Role** | Risk Pillar Leader |
| **Review Cadence** | Annual; on tooling change |
| **Organization Value** | |
| **Last Calibrated** | |
| **Next Review** | |

### 4.3 Advisory Response Time

| Field | Value |
|-------|-------|
| **Parameter** | Advisory or office-hours question response time |
| **Document** | [`CERG-GOV-SLC-001`](CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md) §3.3 |
| **Section** | §3.3 — Advisory |
| **Default Value** | Substantive written response within 3 business days |
| **Calibration Inputs** | Staffing; advisory volume; question complexity distribution |
| **Calibration Method** | Measure P80 response time over 2 quarters; set target accordingly. |
| **Owning Role** | Owning Pillar Leader per question |
| **Review Cadence** | Annual |
| **Organization Value** | |
| **Last Calibrated** | |
| **Next Review** | |

### 4.4 New SaaS/Cloud Service Review

| Field | Value |
|-------|-------|
| **Parameter** | New SaaS/cloud service review decision time |
| **Document** | [`CERG-GOV-SLC-001`](CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md) §3.3 |
| **Section** | §3.3 — Advisory — New SaaS/cloud service review |
| **Default Value** | Restricted-data placement: 10 business days · Non-Restricted: 5 business days |
| **Calibration Inputs** | Staffing; review volume; vendor response time |
| **Calibration Method** | Measure P80 over 2 quarters; calibrate by data classification. |
| **Owning Role** | Governance Pillar Leader (Policy & Standards) |
| **Review Cadence** | Annual |
| **Organization Value** | |
| **Last Calibrated** | |
| **Next Review** | |

### 4.5 Exception/Risk-Acceptance Request Intake

| Field | Value |
|-------|-------|
| **Parameter** | Exception/risk-acceptance request acknowledgement and routing |
| **Document** | [`CERG-GOV-SLC-001`](CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md) §3.4 |
| **Section** | §3.4 — Program Oversight |
| **Default Value** | Acknowledge and route within 3 business days |
| **Calibration Inputs** | Request volume; staffing; automation of routing |
| **Calibration Method** | Measure P80 acknowledgement time over 2 quarters. |
| **Owning Role** | Risk Register Owner |
| **Review Cadence** | Annual |
| **Organization Value** | |
| **Last Calibrated** | |
| **Next Review** | |

---

## 5. Metric Threshold Calibration (MTR-001)

### 5.1 Service Responsiveness Metric Thresholds

| Field | Value |
|-------|-------|
| **Parameter** | Green/Amber/Red thresholds for SR-001 through SR-005 |
| **Document** | [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) §3.9 |
| **Section** | §3.9 — Service Responsiveness Metrics |
| **Default Value** | Preliminary defaults per SLC-001 commitment values until organizationally calibrated |
| **Calibration Inputs** | Actual performance data over 2+ quarters; staffing levels; demand patterns |
| **Calibration Method** | Measure actual performance distribution; set green threshold at or above P80 of actual performance; amber as buffer zone. Review adoption-phase targets from SLC-001 §3.5 as starting point. |
| **Owning Role** | Governance Pillar Leader (Policy & Standards) |
| **Review Cadence** | Annual; or when metric is red-stalled for 3+ consecutive months |
| **Organization Value** | |
| **Last Calibrated** | |
| **Next Review** | |

### 5.2 Other Metric Thresholds

All discipline metrics (EM-001 through EM-010, RM-001 through RM-008, GV-001 through GV-006) carry preliminary green/amber/red thresholds defined in MTR-001 §3. These thresholds follow the same calibration rules (MTR-001 §10): tighten on green drift, escalate on red stall, adjust on risk appetite change. The initial preliminary values remain in effect until either triggered by the calibration rules or reviewed at the annual metrics program review.

| Field | Value |
|-------|-------|
| **Parameter** | All discipline metric thresholds |
| **Document** | [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) §3.1–§3.9 |
| **Section** | §3 — Discipline Metrics |
| **Default Value** | Per-metric thresholds defined in MTR-001 §3 tables |
| **Calibration Inputs** | Actual performance data; risk appetite changes; maturity improvements; peer benchmarks |
| **Calibration Method** | MTR-001 §10 triggers: Green drift (tighten), Red stall (escalate/recalibrate), Risk appetite change (proportional adjustment), Maturity improvement (review for tightening), External benchmark (peer comparison). One change per domain per quarter. |
| **Owning Role** | Governance Pillar Leader (Policy & Standards) |
| **Review Cadence** | Continuous (trigger-based); annual comprehensive review |
| **Organization Value** | |
| **Last Calibrated** | |
| **Next Review** | |

---

## 6. Crown Jewel Scenario Calibration (CJ-001)

### 6.1 Scenario Financial Impact Figures

| Field | Value |
|-------|-------|
| **Parameter** | Scenario-specific financial or impact figures in crown jewel loss scenarios |
| **Document** | [`CERG-GOV-CJ-001`](CERG-GOV-CJ-001_Crown_Jewel_Register_and_Scenario_Library.md) §4.1 |
| **Section** | §4.1 — Scenario Record Components |
| **Default Value** | Preliminary defaults per scenario; not approved loss values until Finance and CISO sign |
| **Calibration Inputs** | Business impact analysis data; revenue exposure per scenario; regulatory fines; operational downtime cost |
| **Calibration Method** | For each scenario (SCN-01 through SCN-10+), the owning role works with the business unit owner to estimate: direct financial loss, regulatory exposure, operational downtime cost, and reputational impact. Record calibrated values in the scenario record. |
| **Owning Role** | Risk Pillar Leader (scenario library owner) coordinates with impacted business unit owners |
| **Review Cadence** | Semi-annual; on material change to crown jewel population or business operations |
| **Organization Value** | |
| **Last Calibrated** | |
| **Next Review** | |

---

## 7. Risk Acceptance Duration Calibration (RMF-001)

### 7.1 Default Risk Acceptance Durations

| Field | Value |
|-------|-------|
| **Parameter** | Maximum duration for each risk acceptance tier |
| **Document** | [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.7 |
| **Section** | §9.7 — Risk Acceptance Authority — Default Max Duration column |
| **Default Value** | Critical: 30 days · High: 90 days · Medium: 180 days · Low: 365 days |
| **Calibration Inputs** | Regulatory deadlines; audit cycle; typical remediation timelines; business constraints |
| **Calibration Method** | Compare against environment-specific rules, regulatory packages, POA&M, CIP deviations, contracts, and procedures. The shortest applicable duration wins per §9.7 Duration Rule. |
| **Owning Role** | Governance Pillar Leader (Policy & Standards) |
| **Review Cadence** | Annual; when a regulatory package or procedure sets a conflicting duration |
| **Organization Value** | |
| **Last Calibrated** | |
| **Next Review** | |

---

## 8. Calibration Governance

### 8.1 Calibration Status Register

The Governance Pillar Leader (Policy & Standards) maintains the calibration status of each item in this document. The register records, for each item:

- **Status:** Uncalibrated / In Progress / Calibrated / Reviewed — No Change Needed
- **Calibrated Value:** The organization-approved value
- **Date:** When calibration was completed or last reviewed
- **Next Review:** Scheduled review date based on cadence
- **Approver:** CISO or designee (per RMF-001 §9.7 delegation rules)

### 8.2 Calibration Cadence

| Activity | Frequency | Owner |
|----------|-----------|-------|
| Risk appetite and impact band calibration | Annual (aligned to budget cycle) | Governance Pillar Leader + Finance |
| SLA commitment calibration | Annual | Governance Pillar Leader |
| Metric threshold review | Continuous (trigger-based); annual comprehensive | Governance Pillar Leader |
| Crown jewel scenario calibration | Semi-annual | Risk Pillar Leader |
| Risk acceptance duration review | Annual | Governance Pillar Leader |
| Full calibration register status report to CISO | Quarterly (concurrent with CISO Risk & Posture Review) | Governance Pillar Leader |

### 8.3 Calibration Documentation

Every calibration decision is documented in the organization's Decision Log (IMP-002 §4) with:

- Parameter being calibrated
- Previous value (default or last calibrated)
- New calibrated value
- Rationale and data sources
- Approver name and date
- Next review date

### 8.4 Integration with Other CERG Instruments

- **Adoption gates (IMP-005):** Calibration status is a Gate 2→3 transition criterion. At least risk appetite and impact bands must be calibrated before exiting Gate 2.
- **Risk acceptance (RMF-001):** Risk acceptance decisions made against uncalibrated values use qualitative judgment until calibration occurs. Document this in the risk acceptance record.
- **Metrics (MTR-001):** Metric thresholds that reference SLC-001 commitment values remain as preliminary defaults until SLC-001 is calibrated.
- **Improvement register (IMPREG-001):** Calibration actions are recorded as improvement register entries of type "Metric or threshold change" when they improve program precision.

---

## 9. Document Control

| Field | Value |
|-------|-------|
| **Document ID** | CERG-GOV-CAL-002 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Effective Date** | 2026-06-18 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Policy & Standards) |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on any change to the risk appetite calibration |
| **Next Scheduled Review** | 2027-06-18 |
| **Frameworks** | NIST CSF 2.0 (GOVERN); ISO/IEC 27001 A.6.1 |
| **Regulations** | Cross-cutting |
| **Environments** | Program-wide |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 Draft | 2026-06-18 | Cyber Governance | Initial release. Consolidates all preliminary defaults from RMF-001, SLC-001, MTR-001, and CJ-001 into a single calibration register. Provides calibration inputs, methods, owning roles, and review cadence for each parameter. |

### Review Triggers

- Material change to organizational revenue or risk appetite
- Change to cyber insurance coverage or retention
- Regulatory change affecting impact thresholds
- Metric that is red-stalled for 3+ consecutive months (indicates unrealistic threshold)
- Feedback from adoption gate reviews indicating calibration gaps
- Direction from the CISO

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| Risk Management Framework | [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) | Source of risk appetite and impact band defaults |
| Service Level Commitments | [`CERG-GOV-SLC-001`](CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md) | Source of SLA commitment defaults |
| Metrics Dashboard and Reporting | [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) | Source of metric threshold defaults and calibration rules |
| Crown Jewel Register | [`CERG-GOV-CJ-001`](CERG-GOV-CJ-001_Crown_Jewel_Register_and_Scenario_Library.md) | Source of scenario financial impact defaults |
| Adoption Safety Guide | [`CERG-GOV-IMP-002`](CERG-GOV-IMP-002_Adoption_Safety_Guide.md) | Decision Log for calibration records |
| Program Improvement Register | [`CERG-GOV-IMPREG-001`](CERG-GOV-IMPREG-001_Program_Improvement_Register.md) | Tracks calibration actions |
| Document Catalog | [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Registers this artifact |

Governance owns this document. The Governance Pillar Leader (Policy & Standards) is responsible for initiating reviews, managing the revision cycle, and obtaining CISO endorsement for all changes.
