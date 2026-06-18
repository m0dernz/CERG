# SURGE: Cyber Engineering, Risk & Governance

## CROWN JEWEL REGISTER AND LOSS SCENARIO LIBRARY
### What Would End Us, and Who Defends Each Chain End-to-End

---

| | |
|---|---|
| **Document ID** | CERG-GOV-CJ-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Risk Pillar Leader / Governance Pillar Leader |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) · [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md) · [`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) · [`CERG-GOV-FLOW-001`](CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md) · [`CERG-GOV-CEF-001`](CERG-GOV-CEF-001_Control_Effectiveness_Framework.md) · [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) · [`CERG-PLN-BC-001`](../plans/CERG-PLN-BC-001_Business_Continuity_and_Disaster_Recovery_Plan.md) · [`CERG-GOV-EDG-001`](CERG-GOV-EDG-001_Edge_Register.md) · `machine-readable/cerg-crown-jewel-schema.yaml` |
| **Review Cycle** | Annual / On material change to crown-jewel population or threat landscape |
| **Frameworks** | [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (IDENTIFY, GOVERN) · [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) (RA, CP, CA) · NIST 800-37 RMF |
| **Regulations** | NERC-CIP CIP-002 · [CMMC L2](https://dodcio.defense.gov/CMMC/) · [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC |
| **Environments** | All in-scope assets - owned, hybrid, cloud, SaaS, OT, CUI |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Relationship to Bottom-Up Risk](#2-relationship-to-bottom-up-risk)
3. [The Crown Jewel Register](#3-the-crown-jewel-register)
4. [The Loss Scenario Library](#4-the-loss-scenario-library)
5. [Scenario Pressure-Test Process](#5-scenario-pressure-test-process)
6. [Integration Points](#6-integration-points)
7. [Roles and Responsibilities](#7-roles-and-responsibilities)
8. [Document Control](#8-document-control)

---

## 1. Purpose and Scope

CERG's operational pipeline is bottom-up. A scanner, a penetration test, an audit, or a review produces an observation; Risk validates its reachability, scores it, and tracks it to closure through [`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) and the risk register in [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) Section 9. This pipeline is disciplined and measurable, and it is necessary. It is not sufficient.

A program can be green on every finding metric and still have an undefended path to a catastrophic loss, because nothing in the bottom-up pipeline asks the top-down question: **what is the small set of events that would actually end this organization, and is anyone defending each of those chains end-to-end?** A bottom-up pipeline sees individual findings. It does not see a chain that crosses four assets and three control families, where each link looks acceptable in isolation but the chain as a whole is fatal.

This document adds the top-down layer. It does two things:

1. Establishes the **Crown Jewel Register** as the authoritative inventory of the assets whose loss would be catastrophic or severe, and defines the minimum control profile those assets must carry, verified rather than assumed.
2. Establishes the **Loss Scenario Library**, a curated set of named loss scenarios that are pressure-tested against the program's actual control coverage, so that catastrophic gaps are discovered by deliberate exercise rather than by an incident or an auditor.

This document is scoped to CERG-managed assets and controls. It does not replace the System Categorization Register maintained under RMF-001 Section 3; it is a view over that register plus the scenario reasoning the register does not contain.

> **The Adaptive Test**
>
> An assessor asks: "Show me your crown jewels and the scenarios you test against them." A Repeatable program answers with a control list. An Adaptive program answers with a named-scenario library, the control families that should break each chain, the detections that should fire, the recovery path, and the dated record of the last time each scenario was walked end-to-end. The difference is whether the program waits to be surprised.

---

## 2. Relationship to Bottom-Up Risk

The two layers are complementary and must reconcile. Neither replaces the other.

| Dimension | Bottom-Up (existing) | Top-Down (this document) |
|---|---|---|
| **Starting point** | An observation: scan, test, audit, intel, review | A crown jewel and a named loss scenario |
| **Question asked** | "Is this finding reachable, and how bad is it?" | "What would end us, and is the chain broken?" |
| **Primary owner** | Exposure Management Lead / Risk Register Owner | Risk Pillar Leader (scenarios) / Governance (register) |
| **Authoritative home** | [`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md), RMF-001 Section 9 | This document |
| **Failure it catches** | Individual exploitable exposures | Cross-asset, cross-control kill chains |
| **Cadence** | Continuous | Scheduled pressure-test (Section 5) |

**Reconciliation rules:**

1. Every crown jewel in the register (Section 3) must exist as a categorized system in the RMF-001 Section 3 System Categorization Register. The register here does not invent assets; it flags and enriches the most consequential ones.
2. Every chain-breaking control named in a scenario (Section 4) must trace to a control in [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md). Scenarios do not invent controls; they assert which existing controls must hold.
3. Every gap surfaced by a pressure-test becomes a bottom-up artifact: a Finding Record per [`CERG-GOV-FLOW-001`](CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md) F-04. This is the bridge that returns top-down discoveries to the disciplined bottom-up pipeline for tracked closure.

---

## 3. The Crown Jewel Register

### 3.1 Criticality Tiers

The register classifies assets by the consequence of their loss. Tier 0 and Tier 1 assets are crown jewels and carry the minimum control profile in Section 3.3. Tiers 2 through 4 are governed by the standard baseline and overlays in CB-001. The tier definitions are the authoritative markdown form of the criticality tiers in `machine-readable/cerg-crown-jewel-schema.yaml`; where the two differ, this document wins and the schema is regenerated.

| Tier | Meaning | Control expectation |
|---|---|---|
| **Tier 0** | Crown Jewel. Loss would be catastrophic - existential or grid/safety-level. | All applicable controls at enhanced verification frequency, plus the Section 3.3 minimum profile. |
| **Tier 1** | Critical. Loss would be severe. | All applicable controls at standard verification frequency, plus the Section 3.3 minimum profile. |
| **Tier 2** | High. Loss would be significant. | All applicable controls per CB-001. |
| **Tier 3** | Moderate. Loss would be manageable. | Priority controls per CB-001. |
| **Tier 4** | Low. Loss would be minor. | Baseline controls per CB-001. |

### 3.2 Register Field Set

Each crown-jewel entry records the following fields. These are the authoritative form of the `crown_jewel_fields` in the machine-readable schema:

| Field | Description |
|---|---|
| `asset_id` / `system_id` | Identifier tying back to the System Categorization Register and asset inventory. |
| `business_service` | The business service the asset delivers. |
| `owner` | Accountable asset owner. |
| `executive_sponsor` | Named business executive sponsor (per OM-001 canonical roster). |
| `criticality_tier` | Tier 0 or Tier 1 for crown jewels. |
| `crown_jewel` | Boolean flag surfaced on the categorization register. |
| `regulated_scope` | BES Cyber System, CUI enclave, SOX ITGC, or none. |
| `data_classification` | Highest data sensitivity handled. |
| `operational_impact` / `safety_impact` / `financial_reporting_impact` / `customer_impact` | Consequence dimensions of loss. |
| `internet_exposed` | Whether any reachable path originates from the Internet. |
| `third_party_dependencies` | Vendors, SaaS tenants, or sub-processors in the asset's trust or recovery path (cross-reference [`CERG-GOV-EDG-001`](CERG-GOV-EDG-001_Edge_Register.md)). |
| `recovery_time_objective` / `recovery_point_objective` | RTO / RPO from BC-001. |
| `minimum_logging_profile` / `minimum_backup_profile` / `minimum_identity_profile` / `minimum_segmentation_profile` / `minimum_adversarial_validation_profile` | The verified minimum control profile (Section 3.3). |
| `review_date` | Next scheduled review of this entry. |

### 3.3 Minimum Control Profile for Crown Jewels

A crown jewel does not merely inherit a NIST baseline overlay. It carries a minimum control profile that must be **verified, not assumed**. Each line is additive on top of the asset's standard baseline and regulatory overlays per CB-001 (consistent with the CB-001 design principle that overlays add and never relax). A crown jewel that cannot evidence each line below generates a Finding Record per FLOW-001 F-04.

| Profile element | Tier 0 (Crown Jewel) | Tier 1 (Critical) | Verifying evidence | CB-001 / standard reference |
|---|---|---|---|---|
| **Tested recovery** | Recovery tested at enhanced frequency; backup demonstrably outside the asset's blast radius (separate trust domain / immutable / offline). | Recovery tested at standard frequency; backup isolation documented. | Restoration test record; backup isolation attestation. | CP family; [`CERG-STD-RES-001`](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) |
| **Phishing-resistant identity** | Phishing-resistant MFA enforced for all human and machine access paths; no legacy-auth bypass. | Phishing-resistant MFA for privileged access. | IdP enforcement report; legacy-auth disablement evidence. | AC, IA; [`CERG-STD-AC-001`](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |
| **Segmentation** | Asset is segmented to limit lateral movement; reachable paths enumerated and minimized. | Segmentation documented; reachable paths reviewed. | Segmentation diagram; reachability validation. | SC; [`CERG-STD-NET-001`](../standards/CERG-STD-NET-001_Network_Security_and_Segmentation_Standard.md) |
| **Day-one detection** | ATT&CK-mapped detections for the asset's likely kill chains are authored, tested, and operating. | Day-one detection set present and tested. | Detection coverage report (LM-001 DT-001). | AU, SI; [`CERG-STD-LM-001`](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |
| **Adversarial validation** | Validated by penetration test or purple-team exercise at enhanced frequency. | Validated at standard frequency. | Adversarial validation report. | CA-8; [`CERG-PRC-AV-001`](../procedures/CERG-PRC-AV-001_Adversarial_Validation_Procedure.md) |

> **Verified, Not Assumed**
>
> "We back it up" is not tested recovery. "MFA is on" is not phishing-resistant identity enforced with legacy auth disabled. "It's in its own VLAN" is not enumerated, minimized reachability. The crown-jewel profile is satisfied only by the named evidence, current within its freshness window. An assumed control on a crown jewel is the most expensive kind of optimism.

### 3.4 Relationship to the System Categorization Register

The crown-jewel register is a **view over** the RMF-001 Section 3 System Categorization Register, not a parallel inventory. The Tier 0 / Tier 1 flag lives on the categorization register; Governance maintains both records together. This document surfaces and operates the crown-jewel subset and attaches the minimum control profile and scenario linkage that the categorization register does not carry. There is exactly one authoritative list of systems, and it is the categorization register.

---

## 4. The Loss Scenario Library

### 4.1 Scenario Structure

A loss scenario is a named, narrated kill chain against one or more crown jewels. Each scenario is recorded with the following structure:

- **Scenario ID and Name**
- **Narrative**: one paragraph describing the loss event in business terms.
- **Crown jewels in blast radius**: the register entries the scenario threatens.
- **Kill chain**: the high-level adversary steps.
- **Chain-breaking controls**: the CB-001 control families that should stop the chain, with the specific control intent at each link.
- **Detections that should fire**: the ATT&CK techniques and LM-001 detections that should surface the activity.
- **Recovery path**: the BC-001 / RES-001 path that restores the service if prevention and detection both fail.
- **Owner**: the role accountable for keeping this scenario current and walking it.
- **Threat model ref**: the PRC-TM-001 threat model ID(s) that import this scenario. Populated when a threat model uses this scenario as a mandatory input.

Scenario-specific financial or impact figures are recorded as **preliminary defaults requiring organizational calibration**, following the RMF-001 Section 12 calibration pattern. They are not approved loss values until Finance and the CISO sign.

### 4.2 Starter Scenario Set

The following scenarios are the starting library. Each organization tailors the set to its own crown jewels and sector; the utility/OT and CUI flavor below reflects CERG's reference environment. The library should hold roughly ten to fifteen live scenarios at any time.

| ID | Name | Crown jewels in blast radius | Chain-breaking control families | Detections that should fire | Recovery path | Threat Model Ref |
|---|---|---|---|---|---|
| **SCN-01** | Ransomware encrypts production while backups share a trust domain | Primary business systems; backup infrastructure | CP (backup isolation), AC/IA (privilege containment), SC (segmentation), SI (anti-malware) | T1486 Data Encrypted for Impact; T1490 Inhibit System Recovery; mass file-change and backup-deletion alerts | Restore from blast-radius-isolated backup per RES-001; BC-001 activation | |
| **SCN-02** | OT/SCADA historian compromise causing loss of grid visibility or control | Historian; control servers; BES Cyber Systems | SC (IT/OT boundary), AC (least privilege), AU (OT monitoring), MA (controlled maintenance) | ATT&CK for ICS: T0859 Valid Accounts; T0816 Device Restart/Shutdown; OT protocol anomalies | OT recovery runbook; manual operations fallback; CIP-008 path | |
| **SCN-03** | CUI exfiltration via MSP or vendor admin path | CUI enclave; vendor admin tooling | SA/SR (vendor controls), AC (vendor privilege), AU (vendor-path logging), edge controls (EDG-001) | T1199 Trusted Relationship; T1078 Valid Accounts; anomalous vendor-path access | CUI containment; POA&M; SCCT activation per TPRM-001 | |
| **SCN-04** | Code-signing, CA, or secrets key compromise propagating to customers | Signing infrastructure; key management; CA hierarchy | CR (key management), AC (key access), AU (key-use logging), SI (integrity) | T1552 Unsecured Credentials; T1588.004 stolen certificates; anomalous signing events | Key revocation and re-issuance; IR-002 cryptographic playbook | |
| **SCN-05** | Identity provider or federation compromise yielding org-wide privilege | IdP; federation; PAM | IA (phishing-resistant MFA), AC (privileged access), AU (identity detection) | T1556 Modify Authentication Process; T1606 Forge Web Credentials; impossible-travel, MFA-fatigue | Emergency credential reset; break-glass procedures; federation rebuild | |
| **SCN-06** | Cloud control-plane / root account takeover | Cloud management plane; landing zones | AC (root protection), IA (MFA on root), CM (guardrails), AU (control-plane logging) | T1078.004 Cloud Accounts; T1098 Account Manipulation; root-use and policy-change alerts | Control-plane lockdown; account recovery; landing-zone redeploy | |
| **SCN-07** | Privileged insider exfiltrates or sabotages | Crown-jewel systems within insider's access | PS (personnel security), AC (least privilege, separation of duties), AU (privileged-session monitoring) | T1078 Valid Accounts; anomalous bulk access; privileged-session anomaly (AC-EFF-002) | Access revocation; HR/Legal coordination; investigation per IR-002 | |
| **SCN-08** | Critical SaaS tenant compromise where data lives off-premises | SaaS tenant holding regulated/crown-jewel data | SA (SaaS governance), AC (SaaS identity), AU (SaaS audit logs), edge controls (EDG-001) | T1078 Valid Accounts; SaaS audit-log anomalies; OAuth grant abuse (T1528) | SaaS tenant lockdown; provider escalation; data recovery per agreement | |
| **SCN-09** | Business email compromise leading to financial fraud or wire diversion | Email platform; finance approval workflow | AC/IA (email identity), AU (email-anomaly detection), AT (awareness) | T1566 Phishing; T1534 Internal Spearphishing; mailbox-rule and wire-anomaly alerts | Transaction reversal coordination; finance control review; LL-001 | |
| **SCN-10** | Sub-processor concentration failure cascading across multiple vendors | Services depending on a shared sub-processor | SR (supply chain), SA (vendor controls), edge controls (EDG-001 concentration rule) | Vendor-incident intelligence; concentration alert (>= 3 T1/T2 vendors on one sub-processor) | Vendor failover; TPRM-001 concentration response; SCCT | |

Each scenario above is maintained as a fuller record (narrative, kill-chain steps, owner, preliminary impact) in the scenario library operated by the Risk Pillar Leader. The table is the index; the records carry the detail.

---

## 5. Scenario Pressure-Test Process

### 5.1 What a Pressure-Test Is

A scenario pressure-test is a deliberate desk exercise in which the Risk pillar walks a named scenario's kill chain link by link and asks, at each link:

1. **Does the chain-breaking control exist** for the crown jewels in the blast radius?
2. **Is it Implemented** per CB-001 (not Planned, not assumed)?
3. **Is it Effective** per [`CERG-GOV-CEF-001`](CERG-GOV-CEF-001_Control_Effectiveness_Framework.md) (the effectiveness metric is green, not merely the implementation metric)?
4. **Would the detection fire**, and would someone investigate it within SLA?
5. **Does the recovery path work**, and is it tested?

Any answer of "no" or "unknown" is a gap.

### 5.2 What a Pressure-Test Is Not

This is a control-coverage validation, not an incident drill. Full incident-response tabletops are owned by the standing IR team and documented in the IR plan. A scenario pressure-test may be combined with an IR tabletop, but its purpose is distinct: the tabletop rehearses the response; the pressure-test verifies that the controls which should prevent, detect, and recover from the scenario actually exist and work. The pressure-test does not require an active incident or a live exercise; it is a structured walk of the chain against documented control state.

### 5.3 From Gap to Tracked Closure

Every gap a pressure-test surfaces is logged as a **Finding Record per FLOW-001 F-04**, entering the disciplined bottom-up pipeline for owned, dated closure. Where a gap materially changes the residual risk of an asset, it also triggers the RMF-001 Section 9 re-score (Section 6 below). This is how a top-down discovery becomes bottom-up tracked work rather than a slide that is forgotten after the meeting.

### 5.4 Cadence

Scenario pressure-tests are scheduled in [`CERG-GOV-CAL-001`](CERG-GOV-CAL-001_Annual_Security_and_Governance_Calendar.md). The recommended cadence is semi-annual for the full library, with any individual scenario re-walked when the threat landscape, the crown-jewel population, or a material control change warrants it. Each pressure-test produces a Scenario Pressure-Test Report and the associated Finding Records.

---

## 6. Integration Points

This document is connective tissue. Its value is in the cross-references below; each is wired in the named document.

| Integration | Where | What it does |
|---|---|---|
| **Re-score trigger** | [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) Section 9 | A pressure-test that reveals an unbroken chain on an asset in the blast radius re-scores every register risk touching that crown jewel. |
| **Project intake / design target** | [`CERG-GOV-FLOW-001`](CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md) F-02 | Projects touching or creating a crown jewel must meet the Section 3.3 minimum control profile pre-go-live; relevant scenarios become threat-model design targets. |
| **Coverage validation** | FLOW-001 F-03 | Asset registration validates that crown-jewel assets carry the verified minimum control profile, not just scan coverage. |
| **Control overlay** | [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md) | The Crown-Jewel Overlay applies the Section 3.3 profile additively on top of baseline and regulatory overlays. |
| **Metrics** | [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) | EM-006 (exposures on crown jewels) cites this register as its source; RM-007 (Scenario Defense Coverage) measures the fraction of scenarios fully defended. |
| **Board reporting** | [`CERG-TMPL-MTR-001`](../templates/CERG-TMPL-MTR-001_Board_and_CISO_Reporting_Deck_Template.md) | A Scenario Defense Posture view gives the board the top-down framing alongside the bottom-up top risks. |
| **Cadence and maturity** | [`CERG-GOV-CAL-001`](CERG-GOV-CAL-001_Annual_Security_and_Governance_Calendar.md), [`CERG-GOV-MAT-001`](CERG-GOV-MAT-001_Maturity_Self_Assessment_and_Scorecard.md) | The pressure-test is scheduled and the program's scenario coverage is scored as a maturity domain. |
| **Machine-readable** | `machine-readable/cerg-crown-jewel-schema.yaml` | The schema is the derived form of this register; this document is authoritative and the schema is regenerated from it. |

---

## 7. Roles and Responsibilities

| Role | Responsibility |
|---|---|
| **Risk Pillar Leader** | Owns the scenario library; runs the pressure-tests; produces the Scenario Pressure-Test Report; opens Finding Records for gaps. |
| **Governance Pillar Leader** | Maintains the crown-jewel flags on the System Categorization Register; owns this document's place in the catalog and review cycle; reports scenario coverage to the COG and board. |
| **Engineering Pillar Leader** | Implements the Section 3.3 minimum control profile on crown-jewel assets; treats scenarios as design targets at project intake. |
| **Executive Sponsor** | Named per crown jewel; concurs on residual risk where a scenario gap is accepted rather than remediated, per RMF-001 Section 9.7. |
| **CISO** | Approves the crown-jewel population and the scenario library; owns the board-level scenario defense posture. |

---

## 8. Document Control

| | |
|---|---|
| **Document ID** | CERG-GOV-CJ-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Approved By** | CISO |
| **Owner** | Risk Pillar Leader / Governance Pillar Leader |
| **Next Review** | Annual / On material change to crown-jewel population or threat landscape |

### Revision History

| **Version** | **Date** | **Author** | **Change** |
|---|---|---|---|
| 1.0 | 2026-06-12 | Risk Pillar Leader / Governance Pillar Leader | Initial publication. Establishes the crown-jewel register as authoritative, defines the Tier 0/1 minimum control profile, and creates the named loss scenario library with the pressure-test process. |

### Review Triggers

- Annual scheduled review.
- Material change to the crown-jewel population (new Tier 0/1 asset, decommission, ownership change).
- Material threat-landscape shift that introduces or retires a scenario.
- A scenario pressure-test or incident that proves a scenario or control assumption wrong.

### Related Documents

- [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) - Risk Management Framework (categorization, re-score triggers)
- [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md) - Unified Control Baseline (chain-breaking controls, Crown-Jewel Overlay)
- [`CERG-GOV-FLOW-001`](CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md) - Cross-Pillar Operational Flows (F-02, F-03, F-04)
- [`CERG-GOV-CEF-001`](CERG-GOV-CEF-001_Control_Effectiveness_Framework.md) - Control Effectiveness Framework (effectiveness test in pressure-test)
- [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) - Metrics and Reporting (EM-006, RM-007)
- [`CERG-PLN-BC-001`](../plans/CERG-PLN-BC-001_Business_Continuity_and_Disaster_Recovery_Plan.md) - Business Continuity and DR (recovery paths)
- [`CERG-GOV-EDG-001`](CERG-GOV-EDG-001_Edge_Register.md) - Edge Register (vendor and SaaS edges in scenarios)
