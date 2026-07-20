## CERG Risk Management Framework
| | |
|---|---|
| **Document ID** | CERG-GOV-RMF-001 |
| **Version** | 1.33 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - CERG Cybersecurity Policy |
| **Review Cycle** | Annual; triggered by significant regulatory change or organizational change |
| **Frameworks** | NIST SP 800-37 (RMF); NIST SP 800-53r5; NIST CSF 2.0 |
| **Regulations** | NERC-CIP (CIP-005, CIP-007, CIP-010); CMMC L2; SOX ITGC |
| **Environments** | All in-scope environments: IT, OT, Cloud, CUI |

> *A NIST-grounded, operationally adaptive risk management framework designed for IT and OT environments across CMMC, NERC-CIP, and SOX.*

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Framework Architecture](#2-framework-architecture)
3. [Phase 1, Categorize](#3-phase-1--categorize)
4. [Phase 2, Select](#4-phase-2--select)
5. [Phase 3, Implement](#5-phase-3--implement)
6. [Phase 4, Assess](#6-phase-4--assess)
7. [Phase 5, Authorize](#7-phase-5--authorize)
8. [Phase 6, Monitor](#8-phase-6--monitor)
9. [Risk Register and Risk Treatment](#9-risk-register-and-risk-treatment)
10. [IT/OT Risk Management Considerations](#10-itot-risk-management-considerations)
11. [Regulatory Alignment Quick Reference](#11-regulatory-alignment-quick-reference)
12. [Risk Appetite Calibration](#12-risk-appetite-calibration)
13. [Document Control and Review](#13-document-control-and-review)

---

## 1. Purpose and Scope

The CERG Risk Management Framework (CERG-RMF) defines how CERG, the Cyber Engineering, Risk, and Governance function, identifies, assesses, treats, and monitors cybersecurity risk across the enterprise. It is the connective tissue between the three CERG pillars and the foundational document that gives every risk decision a shared vocabulary, a shared process, and a clear owner.

This framework is purpose-built to:

- Align with NIST RMF Steps 1–6 (Categorize, Select, Implement, Assess, Authorize, Monitor) while making each step operationally practical within CERG's three-pillar model.
- Satisfy the risk management requirements of [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (Adaptive tier), [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) Rev 5, [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) Rev 3, [CMMC](https://dodcio.defense.gov/CMMC/) Level 2, NERC-CIP, and [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC simultaneously.
- Apply equally to IT and OT environments, accounting for the operational availability constraints and extended patch windows common in industrial and grid-connected systems.
- Scale from a small team to a large organization without requiring structural changes.

> **Design Intent**
>
> Risk management in CERG is not a periodic checkbox exercise. It is a continuous, adaptive cycle, one that feeds intelligence back into Engineering, drives accountability through Governance, and produces a risk posture the CISO can defend to regulators, auditors, and the board at any point in time.

---

## 2. Framework Architecture

### 2.1 The CERG-RMF Cycle

The CERG Risk Management Framework operates as a continuous cycle, not a linear waterfall. Each phase feeds the next, and intelligence gathered in later phases (Monitor, Assess) loops back to update decisions made in earlier ones (Categorize, Select). This is the structural characteristic that distinguishes an Adaptive-tier program from a Repeatable one.

The six phases map directly to the NIST RMF, with CERG pillar ownership assigned at each step:

| Phase         | NIST RMF Step       | CERG Primary Owner | Supporting Pillars |
| ------------- | ------------------- | ------------------ | ------------------ |
| 1. Categorize | Step 1 - Categorize | Governance         | Engineering, Risk  |
| 2. Select     | Step 2 - Select     | Governance         | Engineering        |
| 3. Implement  | Step 3 - Implement  | Engineering        | Governance         |
| 4. Assess     | Step 4 - Assess     | Risk               | Governance         |
| 5. Authorize  | Step 5 - Authorize  | Governance         | Risk, Engineering  |
| 6. Monitor    | Step 6 - Monitor    | Risk + Governance  | Engineering        |

#### Phase RACI Sub-Matrices

The following RACI sub-matrices resolve pillar ownership ambiguity for specific activities within each phase. **R** = Responsible (does the work), **A** = Accountable (owns the outcome — one per row), **C** = Consulted (provides input before decision), **I** = Informed (notified after decision).

##### Phase 1: Categorize — RACI

| Activity | Governance | Engineering | Risk |
|----------|-----------|-------------|------|
| System impact-level determination (CIA) | R | C | I |
| Regulatory scope declaration (BES/CUI/SOX) | A/R | C | C |
| Asset inventory handoff from Engineering | I | R | A |
| Data classification mapping | R | C | C |
| System Categorization Register maintenance | A/R | I | I |

##### Phase 2: Select — RACI

| Activity | Governance | Engineering | Risk |
|----------|-----------|-------------|------|
| Baseline control selection per impact level | A/R | C | I |
| Overlay identification (CUI/BES/SOX/etc.) | A/R | C | C |
| Tailoring and compensating control approval | A | R | C |
| Exception/Deviation scoping | A | R | C |
| Control selection documentation for SSP | A/R | C | I |

##### Phase 3: Implement — RACI

| Activity | Governance | Engineering | Risk |
|----------|-----------|-------------|------|
| Baseline design and configuration | C | A/R | I |
| Control implementation | I | A/R | C |
| Implementation evidence collection | C | R | A |
| Handoff package preparation | C | A/R | C |
| Pre-production security review | C | R | A |

##### Phase 4: Assess — RACI

| Activity | Governance | Engineering | Risk |
|----------|-----------|-------------|------|
| Vulnerability scanning and coverage | I | C | A/R |
| Penetration testing coordination | I | C | A/R |
| Control effectiveness testing | C | C | A/R |
| Finding validation and prioritization | I | R | A |
| Risk assessment report production | C | I | A/R |

##### Phase 5: Authorize — RACI

| Activity | Governance | Engineering | Risk |
|----------|-----------|-------------|------|
| Authorization package assembly | A/R | C | C |
| POA&M compilation and tracking | A/R | I | C |
| CISO recommendation preparation | A | C | R |
| Business-owner acceptance coordination | A/R | I | I |
| Authorization letter and recordkeeping | A/R | I | I |

##### Phase 6: Monitor — RACI

| Activity | Governance | Engineering | Risk |
|----------|-----------|-------------|------|
| Continuous vulnerability monitoring | I | C | A/R |
| Configuration drift detection and remediation | I | A/R | C |
| Threat intelligence ingestion and analysis | I | I | A/R |
| Risk register updates and review | A/R | C | R |
| Control effectiveness re-assessment | A | C | R |
| Compliance calendar execution | A/R | I | I |

### 2.2 [NIST CSF 2.0](https://www.nist.gov/cyberframework) Function Mapping

[NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) defines six functions. The CERG-RMF operationalizes all six within the risk cycle:

| [CSF](https://www.nist.gov/cyberframework) Function | CERG-RMF Phase(s) | What CERG Does |
|---|---|---|
| **GOVERN** | Categorize, Authorize | Provides insights on risk strategy, risk appetite, and accountability structures to organizational leaders. Maintains policy hierarchy that governs all risk decisions. |
| **IDENTIFY** | Categorize, Assess | Maintains asset inventories and system categorization. Conducts risk assessments, threat modeling, and vendor risk reviews. |
| **PROTECT** | Select, Implement | Engineering designs and deploys protective controls per selected baselines. Governance sets the standard; Risk validates effectiveness. |
| **DETECT** | Monitor, Assess | Risk operates vulnerability scanning, threat intelligence, and anomaly detection. Feeds findings to IR and Governance continuously. |
| **RESPOND** | Monitor (IR hand-off) | Risk provides threat context during incidents. Governance owns playbook library and post-incident documentation. |
| **RECOVER** | Monitor (lessons learned) | Governance captures lessons learned and drives improvement tracking. Engineering supports architectural changes post-incident. |

---

## 3. Phase 1: Categorize

### 3.1 Objective

Categorization establishes the impact level of each system and data type, the foundation for every subsequent risk decision. A system that is improperly categorized will be under-controlled or over-controlled; neither outcome is acceptable.

### 3.2 What Gets Categorized

- All information systems and technology assets (IT and OT) that store, process, or transmit organizational data or perform operational functions.
- Data types by confidentiality, integrity, and availability (CIA) impact: Low, Medium, or High, per FIPS 199 / [NIST 800-60](https://csrc.nist.gov/pubs/sp/800/60/v1/r1/final).
- Operational Technology systems are categorized with additional consideration for Safety, Reliability, and Continuity impacts, recognizing that an OT system failure may carry consequences beyond information loss.

> **OT Categorization Note**
>
> For OT environments, including BES Cyber Systems under NERC-CIP and ICS/SCADA systems in manufacturing or utilities, availability and integrity are typically the dominant impact categories. Confidentiality, while important, is often secondary to the consequences of a system outage or process manipulation. Categorization must reflect this reality, and control selection must weight accordingly.

### 3.3 CERG Roles in Categorization

| Pillar | Categorization Responsibility |
|---|---|
| **Governance** | Leads the categorization process. Maintains the system categorization register. Ensures regulatory designations (BES Cyber System, CUI scope, [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) scope) are documented and current. Coordinates annual review. |
| **Engineering** | Provides technical input on system function, data flows, interconnections, and dependencies. Produces or confirms asset documentation at project handoff. |
| **Risk** | Validates asset inventory completeness via scan coverage. Identifies systems that may be missing from the register. Contributes threat context to impact analysis. |

### 3.4 Categorization Outputs

- **System Categorization Register**: master list of all in-scope systems with CIA impact ratings, regulatory designations, and assigned asset owners.
- **Data Classification Map**: inventory of data types by sensitivity level, mapped to the systems that handle them.
- **Regulatory Scope Declarations**: explicit documentation of which systems are in-scope for NERC-CIP (BES/EACMS/PACS), [CMMC](https://dodcio.defense.gov/CMMC/) (CUI enclave), and [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC.

### 3.5 Regulatory Alignment: Categorize

| Framework | Categorization Requirement | CERG Satisfies Via |
|---|---|---|
| NIST RMF | Step 1: Categorize the system using FIPS 199 / [NIST 800-60](https://csrc.nist.gov/pubs/sp/800/60/v1/r1/final) | System Categorization Register; CIA impact ratings per asset |
| [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) | RA-2: Security Categorization | Governance-maintained categorization register reviewed annually |
| NERC-CIP | CIP-002: BES Cyber System identification and categorization (High/Medium/Low) | Governance leads CIP-002 process; Engineering validates connectivity; Risk confirms inventory |
| [CMMC](https://dodcio.defense.gov/CMMC/) | All 14 domains require defined CUI scope | CUI enclave declaration maintained by Governance; boundary confirmed by Engineering |
| [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) | ITGC scoping: identify systems that support financial reporting | Governance maintains [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC system register in coordination with Finance and Internal Audit |

---

## 4. Phase 2: Select

### 4.1 Objective

Control selection translates categorization outputs into a tailored set of security controls appropriate to the system's impact level, operating environment (IT vs OT), and applicable regulatory requirements. Governance leads selection; Engineering translates selected controls into technical implementation requirements.

### 4.2 Control Baseline Structure

CERG uses a layered baseline model. Every system inherits the Organizational Baseline. Systems with elevated categorization or regulatory scope inherit additional overlay controls:

| Baseline Layer | Applies To | Primary Source |
|---|---|---|
| **Organizational Baseline** | All systems | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) Rev 5 Moderate baseline; [NIST CSF 2.0](https://www.nist.gov/cyberframework) Subcategories |
| **High Impact Overlay** | Systems with any High CIA impact rating | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) High baseline additions |
| **CUI Overlay** | Systems handling Controlled Unclassified Information | [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) Rev 3 |
| **BES Overlay** | BES Cyber Systems, EACMs, PACSs | NERC-CIP CIP-002 through CIP-014 |
| **[SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC Overlay** | Systems supporting financial reporting | COSO/ITGC: Change management, access, availability |
| **OT Safety Overlay** | ICS/SCADA with safety implications | IEC 62443 + [NIST 800-82](https://csrc.nist.gov/pubs/sp/800/82/r3/final) supplemental controls |

> **The Overlay Principle**
>
> Overlays do not restart the control selection process, they add to the organizational baseline. A system in both the CUI scope and [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) scope carries the organizational baseline plus both applicable overlays. Governance tracks the combined control set per system; Engineering implements it. This prevents the "compliance tunnel vision" problem where teams optimize for one framework and inadvertently create gaps in another.

### 4.3 Tailoring and Scoping

Not every control applies equally to every system. CERG's tailoring process allows for three types of adjustments, all of which require documentation and, above a threshold, CISO or Risk approval:

| Tailoring Action | Definition | Approval Required |
|---|---|---|
| **Compensating Control** | An alternative control that meets the intent of the baseline control when the standard control cannot be implemented (common in OT environments) | Risk assessment + Risk Pillar Leader approval |
| **Control Enhancement** | Additional control implementation above baseline, based on threat intelligence or risk assessment findings | Engineering + Governance alignment |
| **Exception / Deviation** | Documented acknowledgment that a control cannot be satisfied; requires compensating controls and risk acceptance | Per the canonical Risk Acceptance Authority table in [§9.7 Risk Acceptance Authority](#97-risk-acceptance-authority-canonical) |

---

## 5. Phase 3: Implement

### 5.1 Objective

Implementation translates selected controls into working technical and administrative safeguards. In CERG, implementation is Engineering's domain, but it is not Engineering's burden alone. Governance provides the standard; Risk validates the result.

### 5.2 Engineering's Implementation Model

Cyber Engineering operates as an internal consulting function. Engineers embed with IT and business project teams early, before architecture decisions are locked, and ensure that security controls are designed in, not bolted on after the fact.

| Project Stage | Engineering Role | CERG-RMF Output |
|---|---|---|
| **Concept / Requirements** | Engage at business requirements stage. Identify regulatory scope and control obligations. Flag OT safety considerations early. | Preliminary security requirements documented in project charter. |
| **Design / Architecture** | Review proposed architecture. Validate that selected controls are achievable in the design. Identify gaps and drive remediation before build begins. | Security architecture review (SAR) findings; control gap list. |
| **Build / Configure** | Provide hands-on implementation support. Produce or validate configuration baselines. Document control implementation for evidence library. | Configuration baselines; implementation records for Governance evidence library. |
| **Pre-Production** | Coordinate pre-production Risk assessment (vulnerability scan, architecture review). Confirm open findings are remediated or risk-accepted. | Pre-production sign-off; open risk items transferred to risk register. |
| **Production Handoff** | Produce handoff documentation: asset registration, baseline, control mapping, open risks. Transfer ongoing oversight to Risk and Governance. | Handoff package; asset added to categorization register. |

### 5.3 Implementation Standards

Engineering implements controls to the following baselines, maintained as living standards by Governance:

- **CIS Benchmarks** (Level 1 minimum, Level 2 for High-impact and BES systems) for server, endpoint, and network device hardening.
- **[NIST 800-82](https://csrc.nist.gov/pubs/sp/800/82/r3/final)** supplemental guidance for OT and ICS system hardening, recognizing that CIS benchmarks may not directly apply to industrial control systems.
- **Organizational configuration baselines** maintained per platform class (Windows Server, Linux, network infrastructure, cloud, OT/ICS), version-controlled by Governance.
- **Zero-trust architecture principles** for network segmentation, identity verification, and least-privilege access, applicable to both IT and OT network boundaries.

> **OT Implementation Reality**
>
> In OT environments, "implement the control" and "deploy the patch" are not always immediately achievable. Operational availability requirements, vendor support limitations, and safety system constraints mean that some controls require compensating measures and extended implementation timelines. CERG's risk register and exception process exist precisely for this situation. Engineering documents the gap, Risk assesses the exposure, and Governance records the compensating controls and target remediation date. For NERC-CIP environments, this triggers the deviation and mitigation plan process.

---

## 6. Phase 4: Assess

### 6.1 Objective

Assessment validates that implemented controls are working as intended. In CERG, assessment is Cyber Risk's core function, executed continuously through exposure management and threat intelligence, and periodically through structured security assessments and adversarial validation.

### 6.2 Assessment Portfolio

| Assessment Type | Frequency | Pillar Owner | Primary Output |
|---|---|---|---|
| **Continuous Vulnerability Scanning** | Continuous (authenticated scan weekly; unauthenticated daily) | Risk | Prioritized finding register with SLA tracking; remediation evidence. |
| **OT / ICS Vulnerability Assessment** | Quarterly minimum; OT-safe passive scanning methods | Risk + Engineering | OT-specific finding register; compensating control documentation for unpatchable findings. |
| **Adversarial Validation - External Pen Test** | Annual minimum; after significant architecture changes | Risk (internal) / Third Party | Pen test report; findings tracked to closure with Engineering review. |
| **Adversarial Validation - Internal Pen Test** | Annual minimum; includes lateral movement and privilege escalation testing | Risk | Internal pen test report; architecture remediation recommendations for Engineering. |
| **Adversarial Validation - Purple Team** | Quarterly minimum for detection validation where detection engineering is in scope | Risk + Incident Response | Detection validation results; tuned analytics and control-improvement actions. |
| **Adversarial Validation - OT / ICS Red Team** | Biennial minimum (or as required by NERC-CIP or contract) | Risk + Third Party | Red team report; OT-specific findings require CISO review before disclosure. |
| **Vendor / Third-Party Risk Assessment** | At onboarding; annually for Critical vendors; triggered by incidents or contract changes | Risk | Vendor risk rating; contract risk terms; ongoing monitoring requirements. |
| **Security Control Assessment (SCA)** | Annual; scope aligned to regulatory cycle | Risk + Governance | SCA report; POA&M updates; evidence for authorization decision. |
| **Threat Intelligence Review** | Continuous ingestion; structured analysis weekly; strategic briefing monthly | Risk | Threat intel products: tactical (IOCs), operational (TTPs), strategic (threat landscape). |

### 6.3 Finding Severity and SLAs

All findings from assessment activities are assigned a severity rating and a remediation SLA. Exceptions to SLAs require documented risk acceptance per the process in [§9.7 Risk Acceptance Authority](#97-risk-acceptance-authority-canonical).

The authoritative remediation-SLA table lives in [`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) §5. The values published there govern every CERG-managed scan, adversarial validation, and assessment finding across IT, cloud, SaaS, and (with the BES schedule overlay) OT environments. Pillar dashboards and KRIs in [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) measure compliance against PRC-VM-001's SLA values, not against a separate table.

> **One Source of Truth**
>
> Earlier drafts of this document carried a parallel SLA table. That table has been retired so that there is exactly one place in the library where a remediation SLA can be changed. If you find a stale SLA citation in another document, the corrective action is to update the citing document to point at PRC-VM-001 ,  not to restate the values.

---

## 7. Phase 5: Authorize

### 7.1 Objective

Authorization is a formal risk acceptance decision made by an accountable leader before a system is allowed to operate or continue operating. It is the point at which residual risk is explicitly acknowledged, owned, and documented. In CERG, Governance structures and manages the authorization process; the CISO is the primary Authorizing Official (AO) for the cybersecurity program.

### 7.2 Authorization Decision Types

| Decision Type | When Applied | Authorizing Authority |
|---|---|---|
| **Authority to Operate (ATO)** | New systems entering production after pre-production assessment. Full ATO requires all High and Critical findings resolved or risk-accepted. | CISO (with Risk and Engineering concurrence) |
| **Interim Authority to Operate (IATO)** | Systems with residual High findings that have documented compensating controls and an approved remediation timeline (maximum 90 days). OT systems with constrained patch windows may require IATO. | CISO; must include documented compensating controls and target full ATO date |
| **Denial of Authorization (DATO)** | Systems where residual risk exceeds the organization's risk appetite and compensating controls are insufficient. System must be isolated or decommissioned. | CISO (mandatory notification to CEO and Board for business-critical systems) |
| **Ongoing Authorization** | Systems with continuous monitoring in place that demonstrate consistent control effectiveness. Replaces periodic point-in-time reauthorization for mature, stable systems. | CISO with quarterly Risk and Governance attestation |

### 7.3 Authorization Package Contents

Governance assembles the authorization package for CISO review. A complete package includes:

- **System Security Plan (SSP)**: documents system boundary, categorization, control implementation status, and responsible parties.
- **Risk Assessment Report (RAR)**: Risk-produced finding report from pre-authorization assessment activities.
- **Plan of Action and Milestones (POA&M)**: documents all open findings with owners, compensating controls, and target remediation dates.
- **Continuous Monitoring Strategy**: defines ongoing monitoring activities that will maintain risk visibility post-authorization.
- **Regulatory Compliance Attestation**: Governance attestation that applicable regulatory controls are satisfied or that deviations are documented per regulatory process.

> **Authorizing OT Systems**
>
> For OT and BES Cyber Systems, authorization must explicitly address operational continuity risk alongside cybersecurity risk. A finding that would result in DATO for an IT system (e.g., unpatched Critical vulnerability) may result in IATO for a BES system if immediate isolation would cause a reliability event. The NERC-CIP deviation and mitigation plan process must be initiated in parallel. The CISO coordinates with Operations leadership and, where required, the Reliability Coordinator.

---

## 8. Phase 6: Monitor

### 8.1 Objective

Continuous monitoring is the phase that separates Adaptive-tier programs from Repeatable ones. It is not a periodic review, it is an always-on operational posture that keeps the organization's risk picture current, feeds intelligence back into earlier RMF phases, and provides the CISO with real-time awareness of the organization's exposure.

### 8.2 Monitoring Program Components

| Component | Pillar Owner | Frequency | Output / Deliverable |
|---|---|---|---|
| Exposure scan coverage | Risk | Continuous | Updated finding register; SLA tracking dashboard; escalation alerts for Critical findings. |
| Configuration drift detection | Risk + Engineering | Continuous (automated) | Drift alerts to Engineering; deviation from baseline triggers change management review. |
| Threat intelligence ingestion | Risk | Continuous; structured analysis weekly | Tactical threat products (IOCs); operational advisories; strategic threat briefings for CISO. |
| Risk register review | Governance | Monthly (full); weekly (high/critical items) | Updated risk register with treatment status; escalation to CISO for items approaching SLA. |
| POA&M status tracking | Governance | Biweekly | POA&M status report; owner accountability communications; escalation for missed milestones. |
| Control effectiveness review | Risk + Governance | Quarterly | Control testing results; evidence library updates; findings fed into next SCA cycle. |
| Compliance calendar execution | Governance | Per regulatory schedule | Regulatory submissions, evidence packages, audit coordination, deviation filings. |
| Vendor and supply chain monitoring | Risk | Continuous (automated); quarterly structured review | Vendor risk rating updates; notification of third-party breaches or advisories. |
| CISO risk dashboard | Governance + Risk | Weekly refresh; real-time for Critical events | Executive risk posture summary; KRI trending; board-ready quarterly summary. |

### 8.3 Key Risk Indicators (KRIs)

| KRI | Target | Owner | Escalation Trigger |
|---|---|---|---|
| Mean Time to Remediate - PPR (0-day) | ≤48 hours (Internet-facing) / ≤72 hours (internal) per [`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) §5 | Risk | Any PPR finding past SLA |
| Mean Time to Remediate - Critical | ≤3 days per [`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) §5 | Risk | Any Critical past SLA without documented compensating control |
| Mean Time to Remediate - High | ≤15 days per [`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) §5 | Risk | Any High past SLA without approved exception |
| Scan Coverage - IT | ≥98% of known assets | Risk | <95% coverage |
| Scan Coverage - OT | ≥90% of known assets (passive methods) | Risk | <85% coverage |
| Open Critical/High Findings | 0 Critical past SLA; <10 High past SLA | Risk + Governance | Any Critical past SLA; >10 High past SLA |
| Risk Register Items Past Target Date | 0 items past target date | Governance | Any item >30 days past target; CISO briefing required if more than 3 items are past target at the monthly Risk Posture Review |
| Policy Review Compliance | 100% of policies reviewed within defined cycle | Governance | Any policy >12 months since last review |
| SSP / Authorization Currency | 100% of in-scope systems with current ATO/IATO | Governance | Any in-scope system without current authorization |
| Vendor Risk Assessments Current | ≥95% of Critical vendors with current assessment | Risk | <90% triggers escalation |
| Security Training Completion | ≥95% completion within defined window | Governance (coord w/ Awareness) | <90% completion triggers escalation to CISO |

---

## 9. Risk Register and Risk Treatment

### 9.1 The Risk Register

The CERG Risk Register is the authoritative record of all identified, assessed, and tracked cybersecurity risks. It is owned by Governance, populated by Risk, and informed by Engineering. It is not a spreadsheet that lives on a network share, it is a living operational tool that drives accountability and informs every authorization decision.

### 9.2 Risk Statement Format (FAIR-Aligned)

Every risk entered into the register is written in a single, consistent statement format derived from the FAIR (Factor Analysis of Information Risk) model. FAIR decomposes risk into a Loss Event Frequency (LEF) and a Loss Magnitude (LM); the CERG statement format makes both halves explicit so that every register entry can be reasoned about, compared, and rolled up the same way.

**Canonical risk statement:**

> *"[Threat community] using [threat action / vector] against [affected asset / scope] could result in [primary and secondary loss types] of [loss magnitude range], at an estimated frequency of [LEF range]."*

**Components:**

| Component | What It Captures | Examples |
|---|---|---|
| **Threat community** | Who or what is initiating the loss event (FAIR Threat Community). See §9.3. | Organized cybercriminal, nation-state, malicious insider, negligent insider, third-party supply chain |
| **Threat action / vector** | How the loss event is initiated | Ransomware, credential stuffing, phishing, exploitation of unpatched CVE, lateral movement from compromised vendor |
| **Affected asset / scope** | What is harmed and the scope of harm | The CUI enclave, a specific BES Cyber System, the SOX-relevant ERP, the corporate identity store |
| **Loss types** | One or more of FAIR's six primary loss forms | Productivity, response, replacement, fines and judgments, competitive advantage, reputation |
| **Loss magnitude range** | Expected loss as a calibrated range (PERT min / most likely / max) | $250K - $1.5M - $4M |
| **LEF range** | Expected frequency the loss event occurs in a year (PERT min / most likely / max) | 0.05 - 0.15 - 0.4 (i.e., once every 2 to 20 years) |

Risk statements that cannot be written in this form are not yet risks; they are observations or findings. Findings remain in the vulnerability or assessment register until they can be expressed in a complete loss-event scenario, at which point they are promoted to the Risk Register.

### 9.3 Threat Community Reference

The FAIR Threat Community is the actor or natural force that initiates a loss event. The taxonomy below is the CERG default. Subordinate documents ,  particularly [`CERG Risk Taxonomy`](CERG-GOV-TAX-001_Risk_Taxonomy.md) ,  extend it with sector-specific actors (e.g., ICS-targeted APTs for OT).

| Community | Examples | Primary Loss Forms |
|---|---|---|
| **Nation-state / APT** | State-aligned threat actors with strategic objectives (intellectual property, infrastructure pre-positioning) | Replacement, competitive advantage, response, reputation |
| **Organized cybercriminal** | Financially motivated groups (ransomware, BEC, fraud) | Response, replacement, productivity, fines and judgments |
| **Hacktivist** | Ideologically motivated; disruption and disclosure | Reputation, productivity, response |
| **Malicious insider** | Authorized user acting against the organization | Replacement, competitive advantage, fines and judgments |
| **Negligent insider** | Authorized user causing loss through error or policy violation | Productivity, response, fines and judgments |
| **Third-party / supply chain** | Trusted vendor or service compromised, propagating to the organization | Response, productivity, fines and judgments |
| **Non-malicious (environmental)** | Natural events, infrastructure failures, accidental conditions | Productivity, replacement, response |

### 9.4 Risk Register Data Elements

| Field | Description |
|---|---|
| **Risk ID** | Unique identifier (format: CERG-RISK-YYYY-NNN) |
| **Source** | How the risk was identified: vulnerability scan, pen test, threat intel, vendor assessment, audit, self-identification, or incident. |
| **Affected System(s)** | System(s) or asset(s) associated with the risk, with regulatory designation (BES/CUI/SOX) noted. |
| **Risk Statement** | The canonical FAIR-aligned statement per §9.2. |
| **Threat Community** | Selected from §9.3 (one primary; additional secondaries permitted). |
| **Threat Action / Vector** | How the loss event is initiated. |
| **Loss Types** | One or more of: productivity, response, replacement, fines and judgments, competitive advantage, reputation. |
| **Likelihood (LEF)** | Rated using the band table in §9.5; supported by a PERT range where calibration data exists. |
| **Impact (LM)** | Rated using the band table in §9.5; supported by a PERT range where calibration data exists. |
| **Overall Severity** | Composite severity rating per §9.5: Critical / High / Medium / Low / Informational. |
| **Risk Owner** | Accountable leader (business unit or IT/OT operations) responsible for risk treatment decision. |
| **Treatment Decision** | Remediate / Mitigate / Transfer / Accept - with documented rationale per §9.6. |
| **Compensating Controls** | Controls in place that reduce exposure while the primary risk remains open. |
| **Target Remediation Date** | Committed date for risk closure or next status review. |
| **Approval** | Authority approving the treatment decision; date; reference to the canonical authority table at §9.7. |
| **Status** | Approved |
| **Regulatory Implication** | Whether the risk has regulatory reporting, deviation, or mitigation plan implications (NERC-CIP, CMMC, SOX). |

### 9.5 Likelihood, Impact, and Severity Bands

CERG uses a 5x5 model: likelihood and impact are each rated 1-5, scored, and mapped to a severity band. The bands below are the canonical CERG model. Every CERG document that scores risk must produce the same severity rating as this table.

**Likelihood (LEF) bands.** Calibrated as expected loss events per year. Tune the numeric ranges against your loss-event history; the band labels are fixed.

| Score | Label | Annualized Frequency |
|---|---|---|
| 5 | Very High | >10 events / year |
| 4 | High | 1 - 10 events / year |
| 3 | Medium | 1 event / 1 - 10 years |
| 2 | Low | 1 event / 10 - 100 years |
| 1 | Very Low | <1 event / 100 years |

**Impact (LM) bands.** Calibrated against organizational loss-magnitude reference points. The dollar bands below are preliminary defaults requiring organizational calibration; the Risk pillar lead refreshes them annually with Finance using revenue, insurance retention, downtime cost, and regulatory exposure as the basis.

| Score | Label | Loss Magnitude (preliminary default requiring organizational calibration) |
|---|---|---|
| 5 | Catastrophic | >$10M single-event loss; material to financial statements; sustained reputation damage |
| 4 | Major | $1M - $10M single-event loss; regulatory enforcement action; significant reputation damage |
| 3 | Medium | $100K - $1M single-event loss; reportable to leadership; limited reputation impact |
| 2 | Minor | $10K - $100K single-event loss; absorbed within normal operating costs |
| 1 | Negligible | <$10K single-event loss; no leadership notification required |

**Composite severity.** Likelihood score x Impact score = Severity score; mapped to band.

| Severity Score | Severity Band |
|---|---|
| 20 - 25 | **Critical** |
| 12 - 19 | **High** |
| 6 - 11 | **Medium** |
| 2 - 5 | **Low** |
| 1 | **Informational** |

**Exposure-management precedence.** This 5x5 risk score determines register severity and acceptance authority. It does not replace exposure-treatment clocks. When a vulnerability, KEV item, PPR-tier exposure, or other finding is governed by [`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md), the PRC-VM classification and SLA are authoritative for remediation timing. Use the stricter outcome when risk score and exposure SLA point to different urgency.

### 9.6 Risk Treatment Options

| Treatment | Definition | When Appropriate | CERG Process |
|---|---|---|---|
| **Remediate** | Eliminate the risk by removing the vulnerability, threat source, or exposure. | When technically feasible within a reasonable timeframe and at proportionate cost. | Engineering leads technical remediation. Risk verifies closure via rescan or retest. Governance closes the risk register item. |
| **Mitigate** | Reduce the likelihood or impact of the risk to an acceptable level through compensating controls. | When full remediation is not immediately feasible (common in OT); when residual risk after mitigation falls within risk appetite. | Engineering implements compensating controls. Risk validates control effectiveness. Governance documents and tracks to eventual remediation. |
| **Transfer** | Shift the financial impact of the risk through insurance or contractual liability provisions. | For risks where cyber insurance coverage is appropriate and available. | Governance coordinates with Legal/Finance for contract and insurance language. Risk quantifies the risk for insurance submission. |
| **Accept** | Formally acknowledge and document the risk without further treatment, when residual risk falls within risk appetite. | For Low/Informational risks where cost of treatment exceeds the risk value; or when all other options have been exhausted and the risk owner is willing to own the consequence. | Requires documented approval at the authority level defined in §9.7. Risk provides a written risk finding. Governance records the acceptance in the risk register. The business owner accepts the residual risk — security does not accept business risk. |

### 9.7 Risk Acceptance Authority (Canonical)

This table is the single source of truth for who may accept residual risk. Every other CERG document that references acceptance authority points at this section.

Security can assess, recommend, document, validate compensating controls, and escalate. But the business owner owns the consequence. Risk acceptance requires a business risk owner at every level where business impact exists. The CISO approves on behalf of the cybersecurity program; the Business Owner or Executive Sponsor accepts on behalf of the business unit that bears the operational impact.

| Residual Risk | Risk Role | Governance Role | Business Role | Acceptance By | Documentation | Default Max Duration |
|---|---|---|---|---|---|---|
| **Critical** | Signs finding; validates compensating controls; provides written risk assessment | Structures acceptance package; ensures regulatory notification; tracks conditions | **Executive Sponsor** accepts business consequence; Board notified at next cycle | **CISO + Executive Sponsor** | Risk assessment, compensating controls, business justification, target remediation date | **30 days**; renewal requires material change in treatment plan |
| **High** | Signs finding; validates compensating controls; provides written risk assessment | Structures acceptance package; ensures conditions documented | **Business Owner** accepts business consequence | **CISO + Business Owner** | Risk assessment, compensating controls, business justification, target remediation date | **90 days**; renewal requires documented progress toward remediation |
| **Medium** | Performs risk assessment; confirms residual risk level | Confirms exception conditions; documents acceptance in register | **Business Owner** accepts business consequence | **Business Owner + Pillar Leader or Governance Pillar Leader** | Risk assessment, compensating controls, target remediation date | **180 days**; renewal requires confirmation that conditions have not worsened |
| **Low** | Confirms low residual risk (if needed) | Approves procedural exception; tracks in risk register | **Business Owner** owns local decision | **Business Owner + Risk Register Owner** | Brief justification; tracked in risk register | **365 days**; annual review at minimum |
| **Informational** | N/A | Tracks in register; reports in quarterly trending | **No formal acceptance required** | Risk Register Owner | Tracked in risk register | Reviewed annually |

> **Duration rule**
>
> The durations above are CERG defaults. If an environment-specific rule, regulatory package, POA&M, CIP deviation, contract, or procedure sets a shorter duration, the shortest applicable duration wins.

> **Renewals**
>
> No acceptance renews automatically. An acceptance at any tier requires a fresh approval cycle at expiration. An acceptance renewed more than twice without movement on the treatment plan escalates one tier above the original approver.

> **Role names** below match the canonical roster in [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1. If a role name disagrees with that roster, the roster wins.


### 9.7a Policy Exception vs. Risk Acceptance

These are not the same thing. Collapsing them into one process creates confusion about who owns what.

| Scenario | Type | Path | Owner |
|----------|------|------|-------|
| "We cannot meet password length because legacy system maxes at 12 characters" | **Policy / control exception** | Governance-owned exception workflow | Governance Pillar Leader |
| "The legacy system is Internet-reachable, privileged, and has weak auth" | **Risk** | Risk-owned residual risk analysis | Risk Pillar Leader |
| "We will isolate it, broker access, monitor sessions, and retire by Q3" | **Treatment** | Engineering + Risk | Engineering Pillar Leader |
| "The VP of Operations accepts the residual risk until Q3" | **Business risk acceptance** | Business owner accepts per §9.7 | Business owner |

**Governance** owns the exception workflow: when a control cannot be met, Governance determines whether the gap is a procedural exception (low risk, documented and tracked) or a risk event (requires Risk assessment). **Risk** owns residual risk analysis: when a gap creates material exposure, Risk quantifies it, validates compensating controls, and recommends treatment. **Business** owns the consequence: business leaders accept risk on systems they own, because they own the operational impact.

Use separate artifacts for the two paths. A policy or control exception uses the [Security Exception Request Form](../templates/CERG-TMPL-RM-002_Security_Exception_Request_Form.md) and stays in the exception register with a linked risk entry when residual exposure exists. A residual-risk acceptance uses the [Risk Acceptance Request Form](../templates/CERG-TMPL-RM-004_Risk_Acceptance_Request_Form.md) and follows the authority table in §9.7. [`CERG-TMPL-RM-003`](../templates/CERG-TMPL-RM-003_Risk_Acceptance_Memo_Template.md) may be used only as a lightweight supporting memo or attachment to `TMPL-RM-004`; it does not create a separate acceptance path.

### 9.8 Risk Appetite and Tolerance

CERG's risk appetite is expressed in two complementary ways: a qualitative posture statement that informs every treatment decision, and a quantitative loss-exposure tolerance that anchors acceptance decisions at the Critical and High bands. The CISO maintains both; the Board reviews appetite annually.

**Qualitative posture.** CERG operates under a "Yes, And…" orientation: the default response to a business request is "yes, and here are the conditions that make this safe." Reflexive refusal is not an acceptable risk management strategy. At the same time, three categories receive a deliberately low appetite:

| Category | Appetite |
|---|---|
| Loss of life, physical safety, or grid reliability | **None.** Any credible scenario triggers immediate Critical treatment regardless of LEF or LM scoring. |
| Material loss of CUI or DFARS-regulated data | **Very Low.** Treatment defaults to Remediate; Accept requires CISO + Executive Sponsor + 90-day re-review. |
| Material misstatement of SOX-relevant financial data caused by ITGC failure | **Very Low.** Treatment defaults to Remediate; Accept requires CISO + Executive Sponsor + Audit Committee notification. |
| Operational disruption to enterprise IT services | Medium. Treatment chosen on a cost / business value basis. |
| Loss of low-sensitivity, broadly available data | Higher. Acceptance is appropriate where treatment cost exceeds loss magnitude. |

**Quantitative tolerance (preliminary calibration).** Annualized Loss Exposure (ALE = LEF x LM) is summed across the open risk register quarterly. The bands below are preliminary values calibrated for a mid-market organization ($500M-2B revenue, moderate regulatory exposure). The CISO updates these in coordination with the CFO at the next CERG/Finance joint review — see §9.8.1 for the calibration workbook.

| Posture Indicator | Value (Preliminary) | Recommended Range by Org Size | Action |
|---|---|---|---|
| Total open ALE (Critical + High) | <$5M | Small (<$100M rev): <$500K · Mid: <$5M · Large: <$25M | Within appetite; continue normal monitoring |
| Total open ALE (Critical + High) | $5M - $15M | Small: $500K-$2M · Mid: $5M-$15M · Large: $25M-$100M | Within tolerance; CISO briefs Cyber Oversight Group monthly |
| Total open ALE (Critical + High) | >$15M | Small: >$2M · Mid: >$15M · Large: >$100M | Above tolerance; CISO briefs Board at the next cycle; mandatory treatment plan within 60 days |
| Single-risk ALE | >$2M | Small: >$250K · Mid: >$2M · Large: >$10M | Mandatory CISO review at acceptance; auto-escalates to High at minimum |

> **Calibration is the work.** Values above are preliminary defaults for a mid-market organization; they are not approved appetites until Finance signs the calibration. The pattern — qualitative posture per category plus quantitative ALE bands — is the part that does not change. See §9.8.1 for the full calibration workbook with revenue-gated scaling.


#### 9.8.1 Risk Appetite Calibration Workbook

The risk appetite values in §9.8 are preliminary defaults calibrated to a mid-market organization ($500M-2B revenue). Calibrate them to your organization using the prompts below. Document the calibrated values in your Decision Log (IMP-002 §4).

**How to read the preliminary values:** The bands are derived from a simple ratio of revenue × risk factor. A small organization ($100M revenue) would set tolerance at ~5% of revenue for single-risk ALE bands; a large enterprise ($5B+) at ~2%. The mid-market defaults below use the midpoint of this range. The Risk pillar lead recalculates these annually when revenue is updated.

**Financial Calibration Inputs:**
- Annual revenue: $_________
- Critical service downtime cost (per hour): $_________
- Regulatory fine exposure (per incident): $_________
- Cyber insurance retention: $_________
- Cyber insurance coverage limit: $_________
- Board reporting materiality threshold: $_________

**Operational Calibration Inputs:**
- Maximum tolerable downtime for Tier 1 systems: _________ hours
- Maximum data loss tolerance (RPO): _________ hours
- Customer notification threshold: _________ records affected
- Operational safety threshold: [Describe safety impact that triggers Critical classification]

**Output — Calibrated Values:**

| Band | Mid-Market Preliminary | Your Calibrated Value |
|------|-----------------------|-----------------------|
| Total open ALE — OK | <$5M | $_________ |
| Total open ALE — Caution | $5M - $15M | $_________ - $_________ |
| Total open ALE — Escalate | >$15M | >$_________ |
| Single-risk ALE — CISO review | >$2M | >$_________ |
| Catastrophic single-event LM | >$10M | >$_________ |
| Major single-event LM | $1M - $10M | $_________ - $_________ |
| Medium single-event LM | $100K - $1M | $_________ - $_________ |
| Minor single-event LM | $10K - $100K | $_________ - $_________ |
| Negligible LM | <$10K | <$_________ |

> **Fallback:** If you cannot calibrate these values, document in the Decision Log that risk acceptance uses qualitative judgment until calibration occurs. Do not make acceptance decisions against uncalibrated values.

#### 9.8.2 Risk Acceptance Is Not Remediation

> **Risk acceptance does not make the risk disappear.** It is a deliberate decision to tolerate a known risk under specific conditions for a defined period. It does not:
>
> - Make the finding disappear from the risk register
> - Reset the remediation SLA without documented approval
> - Transfer accountability from the business owner to security
> - Satisfy a regulatory requirement by itself
> - Excuse the organization from monitoring the risk
>
> **A risk acceptance that is not reviewed on cadence is not a treatment — it is neglect.** Every acceptance must have: a named business owner, a documented rationale, compensating controls where applicable, an expiration date, and a review commitment.

### 9.9 Worked Example: Risk Register Entry

The example below shows a single register entry written in the canonical format. Fields not relevant to the scenario are marked n/a; everything else is filled in as it would appear in the live register.

```
Risk ID:                 CERG-RISK-2026-0142
Source:                  Pre-production assessment - substation modernization project
Affected System(s):      Substation Gateway "EAST-SS-04" (BES Cyber System, Medium Impact);
                         vendor remote-access path through the EACMS jump server.
Risk Statement:          Organized cybercriminal threat communities using ransomware
                         delivered via a compromised vendor remote-access path against the
                         EAST-SS-04 BES Cyber System could result in productivity loss,
                         response costs, replacement costs, and NERC reliability fines of
                         $1.2M - $3.5M - $8.0M, at an estimated frequency of
                         0.05 - 0.12 - 0.25 events per year.
Threat Community:        Organized cybercriminal (primary); third-party / supply chain (secondary)
Threat Action / Vector:  Ransomware via compromised vendor remote-access path
Loss Types:              Productivity, response, replacement, fines and judgments
Likelihood (LEF):        Score 3 (Medium) - 0.12 events / year most-likely
Impact (LM):             Score 4 (Major) - $3.5M most-likely
Overall Severity:        Score 12 - HIGH
Risk Owner:              VP, Transmission Operations
Treatment Decision:      Mitigate (vendor MFA hardening + session brokering + read-only
                         engineering connection until vendor remediation completes)
Compensating Controls:   PAM session recording on EACMS; deny-by-default on inbound
                         vendor address space outside maintenance windows; passive OT
                         detection on E/W traffic from EACMS
Target Remediation Date: 2026-09-30
Approval:                CISO per §9.7 (HIGH severity); acceptance recorded 2026-05-15
Status:                  In Remediation
Regulatory Implication:  NERC-CIP CIP-005 R2, CIP-013 supply chain; CIP deviation not
                         required because compensating controls maintain ESP integrity.
```

---


### 9.10 Event-Driven Re-Assessment Triggers

An accepted risk is automatically re-opened for re-assessment when any of the following trigger events occur. Re-assessment follows the full treatment evaluation process in §9.6 and may result in a changed severity score, a new treatment strategy, or re-confirmation of the existing acceptance.

| Trigger Event | Action | Rationale |
|--------------|--------|-----------|
| CVE added to CISA KEV catalog affecting the accepted vulnerability | Immediate re-score; treat as Critical if exploitation is active | KEV listing signals active exploitation; accepted risk tolerance is invalidated |
| Exploit observed in the wild for the accepted vulnerability (per Threat Intelligence) | Re-score within 5 business days; re-assess treatment urgency | Threat landscape has materially changed since acceptance |
| Affected asset changes criticality tier | Re-score within 30 days | Asset criticality is an input to the risk score; a tier change shifts the calculation |
| Regulatory change materially alters compliance impact | Re-score within 30 days of regulatory effective date | Regulatory non-compliance may make the risk unacceptable under any treatment |
| Related incident occurs involving the accepted vulnerability or affected asset | Immediate re-score as part of F-06 post-incident review | An incident proves the risk was underestimated |
| Acceptance renewed more than twice without treatment progress | Escalate one approval tier above original approver (per §9.7); create Finding Record | Repeated renewal without treatment signals acceptance complacency |
| Scenario pressure-test (per [`CERG-GOV-CJ-001`](CERG-GOV-CJ-001_Crown_Jewel_Register_and_Scenario_Library.md)) reveals an unbroken kill-chain on an asset in the scenario blast radius | Open Finding Record (F-04); re-score every register risk touching the affected crown jewel | A top-down test proved a chain the bottom-up register did not surface |

The Risk Register Owner is responsible for monitoring these triggers. Threat Intelligence (TI-001) supplies the exploit observation feed. The Evidence Librarian monitors KEV catalog changes. Governance Pillar Leader maintains the regulatory change watch. The Risk Pillar Leader supplies the scenario pressure-test feed per [`CERG-GOV-CJ-001`](CERG-GOV-CJ-001_Crown_Jewel_Register_and_Scenario_Library.md).

---

## 10. IT/OT Risk Management Considerations

### 10.1 Why OT Requires a Different Lens

IT and OT environments share the same fundamental risk equation - threats, vulnerabilities, and consequences - but OT environments introduce constraints that require deliberate adaptation of standard risk management practices. Availability is not a configuration preference in a power grid or a manufacturing line; it is a safety and reliability imperative that can carry regulatory, legal, and physical-world consequences.

CERG's RMF is designed from the ground up to respect this reality. OT-specific adaptations are documented below.

| RMF Phase | Standard IT Approach | OT Adaptation |
|---|---|---|
| **Categorize** | CIA-based impact ratings per FIPS 199 | Add Safety and Reliability as explicit impact dimensions. BES Cyber Systems classified per CIP-002 High/Medium/Low impact in addition to FIPS 199 ratings. |
| **Select** | [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) Moderate/High baseline | Apply OT Safety Overlay: IEC 62443 practices; [NIST 800-82](https://csrc.nist.gov/pubs/sp/800/82/r3/final) supplemental controls; vendor-specific hardening where CIS benchmarks don't apply. |
| **Implement** | Patch and configure to baseline | OT patch windows are defined by operational schedules (planned outages, maintenance windows). Compensating controls bridge the gap. No emergency patching without operations and safety sign-off. |
| **Assess** | Authenticated vulnerability scans; penetration testing | OT scans use passive/OT-safe methods to avoid disrupting process operations. Active scanning requires operations coordination and maintenance window scheduling. |
| **Authorize** | ATO/IATO per residual risk | OT authorization explicitly documents operational availability risk alongside cybersecurity risk. NERC-CIP deviation process runs in parallel for BES systems. |
| **Monitor** | Continuous automated monitoring | OT monitoring uses passive network visibility tools (e.g., Dragos, Claroty, Nozomi). Change management is stricter; unauthorized changes carry safety implications. |

> **The OT Risk Principle**
>
> An unpatched vulnerability in a BES Cyber System is a real risk. An unplanned outage of a BES Cyber System is also a real risk - one that carries NERC reliability implications, potential regulatory fines, and public safety consequences. CERG's risk management process treats both risks seriously and documents the tradeoff explicitly. The CISO owns the cybersecurity risk. Operations leadership owns the reliability risk. Both sign the authorization.

---

## 11. Regulatory Alignment Quick Reference

The CERG-RMF satisfies the risk management requirements of all applicable frameworks. The table below maps each framework's risk-specific requirements to the CERG-RMF phase and CERG pillar that addresses them.

| Framework | Risk Management Requirement | CERG-RMF Phase | Pillar |
|---|---|---|---|
| **NIST RMF** | Steps 1-6: Categorize, Select, Implement, Assess, Authorize, Monitor | All phases | All pillars |
| **[NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final)** | GOVERN: Risk strategy, risk appetite, accountability structures | Phase 5 (Authorize) | Governance |
| **[NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final)** | IDENTIFY: Asset management, risk assessment, improvement | Phases 1, 4, 6 | Risk + Governance |
| **[NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)** | RA-2, RA-3, RA-5, CA-2, CA-5, CA-7 (Categorization, Risk Assessment, Vuln Monitoring, Control Assessments, POA&M, Continuous Monitoring) | All phases | Risk + Governance |
| **[NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) Rev 3** | 03.11 Risk Assessment family; 03.12 Security Assessment family; all documentation requirements | Phases 1, 4, 5, 6 | Risk + Governance |
| **NERC-CIP** | CIP-002: BES Cyber System categorization; CIP-007 R2: Patch management cadence; CIP-010 R3: Vulnerability assessments; deviation and mitigation plan process | Phases 1, 4, 6 | Governance + Risk |
| **CMMC Level 2** | RA.L2-3.11.1, RA.L2-3.11.2; CA.L2-3.12.1; all 110 practices documented in SSP and POA&M | Phases 1, 4, 5, 6 | Risk + Governance |
| **SOX ITGC** | Change management controls; access controls; IT availability controls; ITGC control assessment and evidence | Phases 4, 5, 6 | Governance + Engineering |

---

## 12. Risk Appetite Calibration

Risk appetite is not a once-and-done statement. An Adaptive organization formally recalibrates its risk appetite based on business changes, incident experience, threat landscape shifts, and regulatory changes. This section defines when, how, and with what inputs the CISO and leadership recalibrate the organization's risk appetite.

### 12.1 Calibration Cadence

Risk appetite is reviewed:

- **Annually**, aligned with the annual planning cycle and the CISO Risk and Posture Review (per GOV-CAL-001)
- **When triggered** by any of the following events:
  - A major incident (Critical severity, or any incident requiring board notification)
  - Merger, acquisition, or divestiture activity
  - Entry into a new market, product line, or regulated domain
  - A material regulatory framework change (new regulation, major amendment, new enforcement posture)
  - CISO or board request
  - A peer benchmarking finding (PRC-TI-001 Section 10.2) that shows a significant gap from sector norms

### 12.2 Inputs to the Review

The annual risk appetite review is prepared by the Governance Pillar Leader with inputs from all pillars. The review package contains:

1. **Incident history (trailing 12 months):** frequency by severity, root cause clusters, control failures identified (per CEF-001), and incident trends
2. **Threat landscape assessment:** from the most recent quarterly assessment (PRC-TI-001 Section 9.1), including top threat actors, TTP changes, and exploited vulnerabilities
3. **Business strategy changes:** new markets, products, technologies, partnerships, or organizational changes from the executive planning cycle
4. **Regulatory changes:** new or modified compliance obligations, enforcement trends, upcoming assessment or audit milestones
5. **Peer and industry incident data:** from external incident learning (PRC-TI-001 Section 10.3) and peer benchmarking (PRC-TI-001 Section 10.2)
6. **Current risk register state:** risk concentration by pillar, OU, and control family; treatment effectiveness rate (RA-EFF-001); exception renewal rate (RA-EFF-002)
7. **Current metric threshold performance:** which thresholds are producing actionable signals vs. noise (per MTR-001 Section 10)

### 12.3 Calibration Decisions

The review produces one of two outputs:

**Option A: No change.** Current risk appetite remains appropriate. The decision is documented with the specific rationale and the data that supported it. "No change" is a deliberate conclusion, not a default.

**Option B: Risk appetite adjustment.** A revised risk appetite statement is produced, plus cascading changes:

| Cascade | Action | Owned By |
|---|---|---|
| Metric thresholds | Tighten or relax relevant thresholds in MTR-001 per the Threshold Calibration procedure (MTR-001 Section 10) | Governance Pillar Leader |
| Control baseline priorities | Controls protecting against newly elevated risks get increased review frequency and potentially tighter effectiveness thresholds | Pillar leader of affected controls |
| Exception authority | The severity band at which a pillar leader can approve vs. requires CISO vs. requires board is adjusted if the risk appetite change warrants it | CISO |
| Investment signals | If appetite tightens in an area, tooling, staffing, or capability gaps are identified and routed to budget planning | CISO |
| Improvement register | Each cascading change is recorded in IMPREG-001 (Type: Metric or threshold change, Control amendment, Staffing or budget) with the risk appetite review as the source | Governance Pillar Leader |

### 12.4 Approval

- The CISO approves the risk appetite statement and all cascading changes.
- If the change materially affects enterprise risk posture, the board or Cyber Oversight Group is informed or approves per the organization's governance charter.
- The approved risk appetite statement is published and becomes the authoritative reference for all subsequent risk decisions until the next calibration.

### 12.5 Cascade Tracking

Cascading changes from a risk appetite adjustment are tracked in the improvement register (IMPREG-001) until verified. A metric threshold change is verified when it produces one full quarter of actionable signals. A control priority change is verified when the control's effectiveness metric reflects the new posture. No cascading change is considered complete until it is verified Effective.

### 12.6 Worked Calibration Example: Mid-Market Utility

> **Purpose**
>
> This worked example shows how a fictitious organization — Contoso Energy Solutions ($1.2B revenue, NERC-CIP Low + SOX scope) — calibrates risk appetite bands from business inputs. First-time adopters can use this as a template for their own calibration.

#### 12.6.1 Business Profile

| **Parameter** | **Value** |
|---|---|
| Revenue | $1.2B (mid-market utility) |
| Regulatory scope | NERC-CIP (Low Impact BES), SOX ITGC |
| Cyber insurance retention | $500K (self-insured retention) |
| Estimated downtime cost per day (Tier 1) | $120K (billing + operations) |
| Estimated downtime cost per day (Tier 2) | $30K (internal systems) |
| IT/OT asset count | ~2,500 IT + ~300 OT/BES assets |
| Security team size | 8 people (CISO + 3 Engineering + 2 Risk + 2 Governance) |
| Maturity baseline | CERG MAT-001: Initial (3.2) |

#### 12.6.2 Inputs to Calibration

**A. Incident history (trailing 12 months):**
- 1 ransomware event (contained, cost: $350K within retention)
- 3 phishing-related credential theft events (no material loss)
- 2 OT patching gaps identified in CIP self-certification (no incident)
- Trend: incident frequency stable, severity increasing (ransomware was new)

**B. Threat landscape:**
- Sector: Energy/Utilities — targeted by state-sponsored and ransomware groups
- Top TTPs: Initial Access via VPN/vendor, Lateral Movement via RDP, Data Exfiltration via cloud storage
- KEV exploits targeting utility sector: 4 in trailing 12 months

**C. Business strategy:**
- Cloud migration program (Year 1–2): moving 40% of IT workloads to AWS
- OT/IT convergence pilot (Year 2): SCADA historian integration with cloud analytics
- Capital budget for cyber: $2.1M (flat vs. prior year)
- Revenue growth target: 5% organic, no M&A planned

#### 12.6.3 Calibration Calculations

**Step 1 — Establish ALE bands as % of revenue**

Using revenue-based calibration as the primary anchor:

| **Risk Band** | **ALE Range** | **% of Revenue** | **Rationale** |
|---|---|---|---|
| Low | < $120K | < 0.01% | Below insurance retention; routine operational cost |
| Medium | $120K – $1.2M | 0.01% – 0.10% | Within insurance retention; multiple events could exhaust retention |
| High | $1.2M – $6M | 0.10% – 0.50% | Exceeds insurance retention; would require capital reallocation |
| Critical | > $6M | > 0.50% | Material to earnings; board notification threshold |

**Step 2 — Single-risk ALE as function of insurance retention and downtime cost**

Single-risk ALE = (Exposure Frequency × Loss Event Value). For this calibration, the CISO and CFO agree:

| **Risk Scenario** | **Frequency (per year)** | **Loss Event** | **Single-Risk ALE** | **Band** |
|---|---|---|---|---|
| Ransomware encrypts Tier 1 billing system | 0.2 (1 in 5 years) | $350K (within retention) + $480K (4 days downtime at $120K/day) = $830K | $166K | Medium |
| CUI data breach via compromised vendor | 0.1 (1 in 10 years) | $2.1M (notification + legal + regulatory fines) | $210K | Medium |
| OT BES Cyber System compromise (loss of view) | 0.05 (1 in 20 years) | $5M (NERC fine + restoration + reliability coordinator penalties) | $250K | Medium-High |
| SOX ITGC control failure → material weakness | 0.15 (1 in 7 years) | $1.5M (audit + remediation + reporting delay costs) | $225K | Medium |
| Cloud misconfiguration → data exposure | 0.3 (1 in 3 years) | $200K (within retention) | $60K | Low |

**Step 3 — Example calibrated risk appetite bands for the 5×5 matrix**

Mapping the ALE bands to the existing 5×5 scoring framework for this example organization. These dollar bands are illustrative calibration output, not a replacement for the canonical severity bands in §9.5 or the acceptance authority in §9.7:

| **5×5 Score** | **Label** | **Corresponds to ALE** | **Appetite Position** |
|---|---|---|---|
| 1 | Informational | < $50K | Track for trend; no formal acceptance required unless a regulator, contract, or business owner requires it |
| 2–5 | Low | $50K – $120K | May be accepted under §9.7 with Business Owner + Risk Register Owner approval |
| 6–11 | Medium | $120K – $1.2M | May be accepted under §9.7 with Business Owner + Pillar Leader or Governance Pillar Leader approval |
| 12–19 | High | $1.2M – $6M | Exceptional; requires CISO + Business Owner approval under §9.7 |
| 20–25 | Critical | > $6M | Avoid or remediate by default; acceptance requires CISO + Executive Sponsor approval and board notification under §9.7 |

**Step 4 — Regulatory overlay adjustments**

| **Regulatory Scope** | **Adjustment to Bands** | **Rationale** |
|---|---|---|
| NERC-CIP (Low Impact BES) | Critical band triggers at > $4M (not $6M) | NERC penalty exposure + reliability risk lowers the threshold |
| SOX ITGC | High band lowered to $1M – $4M | Material weakness disclosure risk + audit costs compress the band |
| CUI / CMMC (not in scope) | Standard bands apply | Not applicable until CUI contracts exist |

#### 12.6.4 Calibration Output

**Risk Appetite Statement (adopted):**

> Contoso Energy Solutions accepts residual cybersecurity risk where:
> a) The estimated annualized loss exposure (ALE) per risk is below $1.2M (0.10% of revenue), AND
> b) The single-risk ALE does not exceed $6M (0.50% of revenue), AND
> c) The risk does not threaten NERC-CIP reliability obligations, SOX material weakness reporting, or safety-of-life systems.
>
> Risk that exceeds any of these thresholds must be treated, transferred, or avoided by default. If leadership proposes acceptance anyway, the approval path in §9.7 still governs; CFO approval and board notification are additional financial-governance requirements for this calibrated example, not substitutes for Business Owner or Executive Sponsor acceptance.

**Cascading changes triggered:**

| **Cascade** | **Action** | **Owner** |
|---|---|---|
| Metric thresholds | Tighten NERC-CIP vulnerability SLA from 90 days to 60 days for BES Cyber Systems | Governance Pillar Leader |
| Control priorities | Elevate cloud security posture management to High priority (cloud migration program underway) | Engineering Pillar Leader |
| Exception authority | Compliance manager may approve Low exceptions for NERC-CIP without pillar leader sign-off | CISO |
| Investment signal | Cloud security tooling and OT monitoring identified as budget candidates for next cycle | CISO |

#### 12.6.5 How to Use This Example for Your Organization

1. Replace the revenue figure and insurance retention with your organization's numbers.
2. Populate the incident history, threat landscape, and business strategy inputs from your own data.
3. Run the ALE band calculation using your revenue as the denominator.
4. Map single-risk ALEs for your top 5–10 risk scenarios to validate the bands produce actionable prioritization.
5. Add regulatory overlay adjustments for each regulator in your scope.
6. Document the risk appetite statement and cascade changes in the improvement register.

---

## 13. Document Control and Review

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-RMF-001 |
| **Version** | 1.33 |
| **Status** | Approved |
| **Effective Date** | 2026-06-14 |
| **Classification** | Public |
| **Document Owner** | Governance Pillar Leader |
| **Approved By** | CISO |
| **Review Cycle** | Annual; triggered by significant regulatory change or organizational change |
| **Next Scheduled Review** | 2027-05-26 |
| **Parent Document** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - CERG Cybersecurity Policy |
| **Related Documents** | [`CERG-GOV-FRM-001`](CERG-GOV-FRM-001_CERG_Framework.md) · [`CERG-GOV-TAX-001`](CERG-GOV-TAX-001_Risk_Taxonomy.md) · [`CERG-GOV-CMX-001`](CERG-GOV-CMX-001_Compliance_Matrix.md) · [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md) · [`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) · [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) · [`CERG-TMPL-RM-001`](../templates/CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md) · [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) · [`CERG-GOV-IMPREG-001`](CERG-GOV-IMPREG-001_Program_Improvement_Register.md) · [`CERG-PRC-TI-001`](../procedures/CERG-PRC-TI-001_Threat_Intelligence_Procedure.md) · System Security Plans (per system) · Plan of Action and Milestones (per system) |

### Revision History

| Version | Date | Author | Change Description |
|---|---|---|---|
| 1.33 | 2026-06-18 | Governance Pillar Leader | Clarified that RMF §9.5 and §9.7 remain canonical for scoring and acceptance authority, separated exception and risk-acceptance template routing, added PRC-VM exposure-SLA precedence, and constrained the calibration example so it cannot override Business Owner / Executive Sponsor acceptance. |
| 1.32 | 2026-06-18 | Governance Pillar Leader | Added §12.6 Worked Calibration Example for mid-market utility ($1.2B revenue, NERC-CIP+SOX scope) with ALE bands as % of revenue, single-risk ALE as function of insurance retention and downtime cost, calibrated 5x5 band mapping, regulatory overlay adjustments, and cascading changes. |
| 1.31 | 2026-06-14 | Governance Pillar Leader | Clarified canonical risk-acceptance authority, default acceptance durations, and the shortest-applicable-duration rule. |
| 1.0 | 2026-05-01 | Cyber Governance | Initial release. Establishes the CERG-RMF cycle, the FAIR-aligned risk statement format, the 5x5 likelihood/impact model, the canonical risk acceptance authority table, and the risk appetite and tolerance posture. Retires the parallel SLA table in favor of the single source of truth in CERG-PRC-VM-001. Adopts canonical ID CERG-GOV-RMF-001 per CERG-GOV-CAT-001 §5.2. |
| 1.3 | 2026-05-26 | Cyber Governance | Added Section 12 Risk Appetite Calibration: annual and triggered review cadence, structured input package, calibration decision framework with cascading changes (metric thresholds, control priorities, exception authority, investment signals), approval workflow, and cascade tracking through the improvement register. Renumbered Document Control to Section 13. |
