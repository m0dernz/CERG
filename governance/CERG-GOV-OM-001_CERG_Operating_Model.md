
# SURGE: Cyber Engineering, Risk & Governance

## CERG OPERATING MODEL
### Pillar Structure · Engagement Models · Staffing · Interaction Patterns

---

| | |
|---|---|
| **Document ID** | CERG-GOV-OM-001 |
| **Version** | 1.23 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Chief Information Security Officer |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual / Upon Organizational Change |
| **Frameworks** | [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) · [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · NIST RMF · ISO 27001 |
| **Audience** | All CERG personnel; business sponsors; IT and OT leadership; executive leadership |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Operating Premise](#2-operating-premise)
3. [The Three Pillars](#3-the-three-pillars)
4. [Authority, Reporting, and Decision Rights](#4-authority-reporting-and-decision-rights)
5. [Engagement Models](#5-engagement-models)
6. [Staffing and Roles](#6-staffing-and-roles)
7. [Coordination Cadence](#7-coordination-cadence)
8. [Interfaces With Other Functions](#8-interfaces-with-other-functions)
9. [RACI Patterns](#9-raci-patterns)
10. [Maturity, Metrics, and the Adaptive Target](#10-maturity-metrics-and-the-adaptive-target)
11. [Operating Model Control](#11-operating-model-control)

---

## 1. Purpose and Scope

This document describes the operating model for the Cyber Engineering, Risk, and Governance (CERG) function. It defines the three pillars, the authority and reporting structure, the engagement models through which CERG delivers value to the business, the staffing patterns that support those engagements, and the cadence by which CERG operates as one team rather than three silos.

This is not a policy. [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) is the policy. This document is the operating description that every CERG team member, business sponsor, and adjacent function partner can use to understand how the function works and how to engage it.

### 1.1 Scope

This document applies to:

- The CERG function itself, Engineering, Risk, and Governance pillars under CISO authority
- The interfaces between CERG and adjacent security functions (Awareness, Incident Response), IT and OT delivery teams, business owners, and executive leadership
- The engagement models by which CERG is consumed: project delivery, continuous service, advisory, and program oversight
- The staffing roles within each pillar and the rules of engagement among them

### 1.2 Relationship to Other Documents

This document is referenced by every CERG standard, procedure, and plan. Where another document assigns work to "Engineering," "Risk," or "Governance," this document defines what those terms operationally mean.

---

## 2. Operating Premise

### 2.1 Why CERG Exists

The traditional separation of cybersecurity into siloed functions, operational security here, GRC over there, engineering security as a third team, produces a predictable failure pattern. Engineering is asked to deliver, then security reviews it after the fact and asks for changes that are now expensive. Risk identifies findings that have no clear path back into engineering planning. Governance writes policy that operators interpret variously, or not at all. Audits and incidents reveal the seams.

CERG consolidates the three core security activities, building secure systems, managing exposure, and governing the program, into one function with one authority. The pillars are distinct in skill set and discipline, but they operate as one team with one CISO and one set of priorities.

### 2.2 The Yes-And Default

> **Governance Does Not Exist to Block the Business**
>
> CERG's default orientation is to enable the business with guardrails, not to close doors. When a risk cannot be eliminated, it is documented, owned, treated, and monitored, not refused on principle. Reflexive denial is not a risk management strategy. The hard work is making "yes" safe; "no" is the easy answer, and the wrong one.

### 2.3 Three Pillars, One Team

CERG operates as one team. The pillars provide structure for skill development, work intake, and accountability, not boundaries to hide behind. Cross-pillar collaboration is the norm. Every Engineering review involves Risk perspective. Every Risk finding has a Governance disposition. Every Governance policy is validated for operational practicability by Engineering and Risk before publication.

---

## 3. The Three Pillars

### 3.1 Cyber Engineering

**Mandate.** Build secure systems by design. Embed security into architecture, configuration, and operational baselines before production. Be the technical security partner to project delivery.

**Core activities.**

- Pre-production security architecture review for all in-scope projects
- Reference architectures, landing zones, and configuration baselines per platform class
- Security infrastructure-as-code, policy-as-code, and admission control
- IT/OT convergence advisory and Electronic Security Perimeter design
- Identity platform engineering (IdP, MFA, SSO, PAM, secrets management)
- Cryptography and key management platform engineering
- Endpoint, server, container, and cloud security tooling engineering
- Operational handoff documentation that supports Governance compliance evidence

**Engagement default.** Project-aligned engagement. Engineering is engaged early in project planning and follows the work through go-live.

### 3.2 Cyber Risk

**Mandate.** Maintain continuous visibility into organizational exposure. Drive the work that reduces it. Test that controls hold up under attack.

**Core activities.**

- Exposure management (scanning, prioritization, remediation tracking) per **[CERG-PRC-VM-001](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md)**
- Adversarial validation: penetration testing, red-team operations, purple-team detection validation
- Threat intelligence consumption and translation into detection and posture controls
- Vendor and third-party security risk assessment
- Cloud security posture management (CSPM) and SaaS security posture management (SSPM)
- Identity-threat detection and continuous identity-risk monitoring
- Risk-register intake from technical sources

**Engagement default.** Continuous service. Risk is always on; engagement is by exposure type, not by ticket.

### 3.3 Cyber Governance

**Mandate.** Own the policy library, the compliance posture, the risk register, and the evidence library. Translate regulation into actionable expectations. Coordinate regulator and auditor engagements.

**Core activities.**

- Policy, standards, and procedures library, including [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) and all subordinate documents
- Compliance program management: NERC-CIP, [CMMC](https://dodcio.defense.gov/CMMC/), [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC, and customer-contractual frameworks
- Risk register operation per **[CERG-PRC-RM-001](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md)**
- Evidence library curation; production of audit and assessment evidence
- Regulator and assessor liaison
- Awareness program coordination (program ownership rests with a separate Awareness function; Governance coordinates content alignment)
- Risk-register intake from policy, audit, and assessment sources
- Risk treatment data feeds into the standing Incident Response team (a separate function under CISO oversight - see §3.4)

**Engagement default.** Program oversight and advisory. Governance is engaged when policy interpretation, exception decisions, or regulatory implications enter the conversation.

### 3.4 What CERG Is Not Responsible For

The following functions are intentionally outside CERG and operate under separate charters:

- **Security Awareness program ownership.** A distinct function under CISO oversight, coordinated with Governance.
- **Incident Response operations and the IR plan itself.** A standing Incident Response team within Cybersecurity, reporting to the CISO, owns [`CERG-PLN-IR-001`](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md) and operates the IR capability. CERG feeds detection, vulnerability context, asset documentation, and post-incident risk-register entries into the IR team; CERG does not maintain the plan, run the exercises, or own the regulatory notification clocks. During an active incident, CERG pillars provide Lead Investigator, Engineering Lead, and Governance Lead roles per the IR team's call.
- **Physical Security (non-cyber).** Owned by Facilities; CERG coordinates for assets within CIP-006 / PE-family scope.
- **Privacy program.** A distinct function under Legal / Privacy leadership; coordinates with Governance for breach notification and Restricted-data handling.
- **Business Continuity (non-cyber).** Owned by Enterprise Risk / Operations; CERG coordinates for cyber-driven business continuity activations.

---

## 4. Authority, Reporting, and Decision Rights

### 4.1 Reporting Line

CERG reports to the CISO. The CISO reports per the organizational structure (typically to the CIO or directly to the CEO depending on org design) and has a defined reporting line to the board (Audit Committee, Risk Committee, or a dedicated Cyber/Technology Committee, per board protocol).

The three pillars report to the CISO through pillar leaders (Manager / Director / VP titles vary by organizational scale).

### 4.2 Decision Rights

| **Decision** | **Authority** |
|---|---|
| Policy approval ([CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) and subordinate standards) | CISO |
| Standards / procedure approval | Pillar leader; CISO for material changes |
| Risk acceptance - all severities | Per the canonical Risk Acceptance Authority table in [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.7 |
| Exception approval | Per [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) §8, which routes to RMF §9.7 for approval authority |
| Incident classification & containment | Incident Commander (CISO or designee), per the standing IR team (see §3.4) |
| External notification (regulator, public) | IC + CISO + Legal |
| Pre-production go/no-go for in-scope projects | Engineering pillar leader with Risk input; escalation to CISO if business and CERG disagree |
| Vendor onboarding approval (Tier 1) | Risk pillar leader; CISO for material risk exceptions |
| New SaaS / cloud service approval | Governance + Engineering; CISO for Restricted-data placements |
| Budget allocation across pillars | CISO |

### 4.3 Escalation Path

Disagreements that the pillars cannot resolve are escalated to the CISO. The CISO maintains a published escalation path that includes a stop-the-line capability for any CERG team member who believes a decision is being made that materially violates policy or creates regulatory exposure.

### 4.4 Cyber Oversight Group (COG)

The **Cyber Oversight Group (COG)** is the standing internal forum that reviews cyber risk posture between board cycles. It is chaired by the CISO.

**Standing core members (every meeting):**
- Chief Information Security Officer (CISO) — Chair
- Chief Information Officer (CIO) or designee
- Chief Operating Officer (COO) or operational equivalent
- General Counsel (GC) or designee
- Chief Financial Officer (CFO) or designee
- Enterprise Risk lead
- Governance Pillar Leader (secretariat)

**Dynamic members (per agenda):**
- Business Unit Risk Owner for any system, asset, or process appearing on the agenda — invited for the relevant agenda items
- Engineering Pillar Leader — invited when architecture decisions, cloud migration, or OT/IT convergence items are on the agenda
- Risk Pillar Leader — invited when risk acceptance review, threat landscape, or adversarial testing results are on the agenda
- Any additional subject matter expert whose presence is needed for informed discussion on a specific agenda item, identified by the CISO or Governance Pillar Leader during agenda preparation

**Dynamic membership rule:** Standing core members participate in every meeting. Dynamic members are invited when their scope of accountability appears on the agenda. The agenda, distributed at least 5 business days before each meeting, lists the attending dynamic members and the items for which their attendance is requested.

The COG meets monthly and serves three purposes:

1. **Posture review.** The CISO presents the open Risk Register summary, top KRIs from [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md), and any High or Critical risk acceptance decisions made since the last meeting.
2. **Cross-functional treatment alignment.** Risks whose treatment crosses business boundaries - e.g., a risk that requires Operations to change a maintenance practice, or Finance to fund a remediation - are surfaced for cross-functional decision or escalation.
3. **Pre-board review.** The COG serves as the dress rehearsal for board-cycle reporting; material risk decisions surface here first so the board reporting is informed by cross-functional perspective.

The COG is not a risk-acceptance authority. Acceptance authority lives in the [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.7 table. The COG is the forum where the right decision-makers are in the room, informed, and aligned. Downstream reports - including the metrics dashboard in [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) §9 and the risk-register reporting cadence in [`CERG-TMPL-RM-001`](../templates/CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md) §7.3 - have the COG as their primary audience.

#### COG Agenda Template

The Governance Pillar Leader (secretariat) prepares the agenda using the template below, distributes it at least 5 business days before the meeting, and identifies which dynamic members are requested for which items.

```
COG AGENDA - YYYY-MM-DD

MEETING INFORMATION
   Date       : YYYY-MM-DD
   Time       : [Time / Duration]
   Chair      : CISO
   Secretariat: Governance Pillar Leader

ATTENDEES
   Standing core: CISO, CIO, COO, GC, CFO, ER Lead, Governance Pillar Leader
   Dynamic invited: [BU Risk Owner for Item X], [Pillar Leader for Item Y], [SME as needed]

AGENDA ITEMS

1. ADMINISTRATIVE (5 min)
   - Approval of prior meeting minutes
   - Conflict of interest disclosure (if any)

2. POSTURE REVIEW (20 min) — Lead: CISO
   - Risk Register summary: open entries by severity, new entries since last meeting
   - Top KRIs from CERG-GOV-MTR-001: [list 3-5 KRIs with green/amber/red]
   - High / Critical risk acceptance decisions since last meeting
   - [If dynamic member invited:] [BU Owner] provides context on [relevant KRI or risk item]

3. CROSS-FUNCTIONAL TREATMENT ALIGNMENT (20 min)
   a) [Risk Item 1 — e.g., Cloud migration vendor API exposure] — Owner: [Name]
      - Risk statement, residual score, treatment options
      - Ask (funding / operations change / policy waiver)
      - Discussion / decision
   b) [Risk Item 2 — e.g., OT patching cadence gap] — Owner: [Name]
      - Risk statement, residual score, treatment options
      - Ask
      - Discussion / decision
   c) [Risk Item N]

4. REGULATORY AND AUDIT UPDATE (10 min) — Lead: Governance Pillar Leader
   - Regulatory change tracker: items affecting COG scope
   - Audit / assessment calendar: upcoming engagements
   - Open findings and POA&M status

5. PRE-BOARD REVIEW (10 min) — Lead: CISO
   - Board reporting package (draft) for upcoming cycle
   - Material risk items requiring board attention
   - Decision: approve / revise / hold for next meeting

6. ANY OTHER BUSINESS (5 min)

7. ACTION ITEM REVIEW (5 min)
   - Review action items from prior meeting
   - New action items with owner and target date

MATERIALS ATTACHED
   - Risk Register summary report
   - KRI dashboard (CERG-GOV-MTR-001 §9 extract)
   - Board reporting package draft (if applicable)
   - Risk acceptance records for review items
```

---

## 5. Engagement Models

CERG is consumed by the rest of the organization through four engagement models. Most major initiatives use more than one.

### 5.1 Project Engagement (Engineering-Led)

Used for new systems, major changes, and significant integrations.

CERG commits to architecture-review intake and disposition turnaround by project tier per [`CERG-GOV-SLC-001`](CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md); early engagement only works if engaging CERG is fast.

| **Phase** | **CERG Activity** | **Lead Pillar** |
|---|---|---|
| Concept | Lightweight architectural consult; data classification and environment-tier discussion. | Engineering |
| Design | Formal security architecture review; reference-architecture / landing-zone selection; threat-model session for novel components. | Engineering (+ Risk for threat modeling) |
| Build | Engineering partner embedded with the project team; pipeline gates configured; identity / cryptography / monitoring requirements implemented. | Engineering |
| Pre-production | Pre-production security review; vulnerability assessment; pen-test where warranted; risk-register entries for any acceptance sought. | Engineering + Risk |
| Production | Handoff to operations; baselines committed; ongoing CSPM / SSPM coverage; exposure management onboarding. | Engineering → Risk |
| Continuous | Continuous monitoring; periodic re-review; governance evidence integration. | Risk + Governance |

### 5.2 Continuous Service (Risk-Led)

Used for ongoing exposure management across the entire estate.

CERG commits to a time-to-coverage target for bringing a new asset under vulnerability and CSPM coverage after go-live, per [`CERG-GOV-SLC-001`](CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md).

- Exposure management operates as a standing service per [CERG-PRC-VM-001](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md).
- CSPM / SSPM operates continuously across approved cloud and SaaS.
- Threat intelligence consumption produces standing detection and posture work.
- Identity-threat detection operates continuously.

Continuous services do not require project tickets. Business teams are partners in remediation rather than initiators of the work.

### 5.3 Advisory (Cross-Pillar)

Used when a business unit, IT team, or OT team has a question, decision, or exploration that does not yet require a project.

- Architecture review office hours
- Cloud / SaaS service evaluation advisory
- M&A / divestiture cyber due diligence support
- Vendor selection advisory
- Policy interpretation advisory

Advisory engagements are intentionally low-friction, but low-friction does not mean unmeasured. They are tracked at the activity level, and CERG commits to a published response time for advisory requests per [`CERG-GOV-SLC-001`](CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md), so that "engage us early" is backed by a reciprocal commitment to respond quickly.

### 5.4 Program Oversight (Governance-Led)

Used for regulatory programs, audits, exam cycles, and board reporting.

- NERC-CIP self-certification cycle and CIP-014 / CIP-013 program management
- [CMMC](https://dodcio.defense.gov/CMMC/) pre-assessment and assessment management
- [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC evidence cycle (quarterly)
- Internal audit coordination
- Customer / partner assessment response

Program oversight engagements are time-bounded with defined entry, milestone, and exit criteria. They are led by Governance with Engineering and Risk supplying evidence and SMEs.

---

## 6. Staffing and Roles

CERG staffing is intentionally consistent across the pillars: a pillar leader, senior practitioners with platform / domain ownership, individual contributors who execute the standing work, and rotations or shared roles where the pillars converge.

The structure below is a pattern, not a fixed org chart. Smaller organizations consolidate roles; larger organizations expand them.

### 6.0 Core Capabilities — What Survives Reorgs

Before defining roles, CERG defines capabilities — the durable work that must get done regardless of headcount, org chart, or reporting structure. Capabilities survive reorgs. Roles are implementation detail.

CERG has 11 core capabilities:

| Capability | Description | Primary Pillar |
|-----------|-------------|---------------|
| **Security Architecture** | Design review, threat modeling, pre-production assessment, pre-approved patterns | Engineering |
| **Identity and Security Platform Engineering** | IdP architecture, PAM, secrets management, IaC, cloud landing zones, endpoint security platform | Engineering |
| **Exposure Management** | Observation collection, exposure path validation, classification, treatment tracking, verification | Risk |
| **Threat and Adversarial Validation** | Penetration testing, red team, purple team, threat intelligence production, detection validation | Risk |
| **Third-Party Edge Management** | Vendor tiering and assessment, SaaS governance, MSP/MSSP requirements, SBOM, supply chain compromise response | Risk |
| **Risk Register and Analysis** | Risk identification, scoring, treatment recommendation, appetite calibration, board reporting | Risk |
| **Policy and Standards** | Policy authorship, standard maintenance, style governance, version control, regulatory citation mapping | Governance |
| **Compliance and Evidence** | Evidence library management, control-to-evidence mapping, audit coordination, POA&M tracking, regulatory submissions | Governance |
| **Metrics and Reporting** | CISO dashboard, board reporting, KRI/KPI maintenance, maturity assessment, stakeholder perception | Governance |
| **Program Improvement** | Lessons learned, improvement register, control effectiveness testing, maturity advancement | Governance |
| **Executive Risk Decision Support** | Cyber Oversight Group preparation, risk appetite affirmation, executive escalation, budget defense | CISO / Governance |

In a small team, one person may hold several capabilities. In a large team, each capability splits into specialized roles. The canonical role roster in §6.1 shows the full specialization; the capability map shows the irreducible minimum.

**Role consolidation for small teams:**

| Small Team (≤5 people) | Capabilities Consolidated |
|------------------------|--------------------------|
| CISO / Security Lead | Executive Risk Decision Support + Risk Register + Program Improvement |
| Security Engineer | Security Architecture + Identity/Platform Engineering + Exposure Management |
| Risk Analyst | Threat/Adversarial Validation + Third-Party Edge Management |
| Governance Lead | Policy/Standards + Compliance/Evidence + Metrics/Reporting |

**Principle:** A 5-person CERG runs the same 11 capabilities as a 60-person CERG. The difference is headcount per capability, not the capabilities themselves. When headcount increases, roles split. When headcount decreases, roles consolidate. The capabilities remain.

### 6.1 Canonical Role Roster

This roster is the single source of truth for role names used throughout the CERG document library. When a standard, procedure, plan, or template refers to "the Risk Manager," it means the canonical name listed below. Documents that use a synonym (column 3) are calling the same role; the corrective action is to update the citing document to the canonical name on its next revision, not to invent a new role.

Roles are organized by pillar. Sub-role variants (e.g., Engineering Pillar Leader - Cloud vs. Engineering Pillar Leader - OT) are scaled out from the canonical name with a parenthetical domain qualifier.


> **See also:** [JF-001](../roles/CERG-GOV-JF-001_Job_Families_Overview.md) for job family grouping and level definitions that organize these roles for career development and hiring. The roster below (and the supporting §6.2-6.4 sections) remains authoritative for role names and pillar assignments.

| Canonical Role | Pillar / Group | Common Synonyms (Do Not Use) | Primary Responsibilities |
|---|---|---|---|
| **Chief Information Security Officer (CISO)** | Executive | - | Strategy, board reporting, final authority on High and Critical risk acceptance per [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.7. |
| **Executive Sponsor** | Business / Executive | "VP," "Executive Sponsor," "Leadership" | Concurrence for Critical risk acceptance per RMF §9.7; business representative on the COG; named per system in the categorization register. |
| **Engineering Pillar Leader** | Engineering | "Engineering Pillar Leader," "Engineering Manager" (when speaking of the pillar lead) | Pillar accountability; project intake; reference-architecture authority. |
| **Cloud Security Engineer** | Engineering | "Cloud Security Engineer" | Cloud platforms, IaC, CSPM gating, landing-zone authority. |
| **Identity Engineer** | Engineering | "Identity Engineer," "Identity Engineer" | IdP, MFA, SSO, PAM, secrets management, federation. |
| **OT Security Engineer** | Engineering | "OT Security Engineer," "OT Security Engineer" | IT/OT convergence, ESP/EAP design, BES Cyber System baselines. |
| **Application Security Engineer** | Engineering | "Application Security Engineer," "Application Security Engineer" | SAST/DAST, SDLC controls, threat modeling. |
| **Endpoint Engineer** | Engineering | "Endpoint Engineer" | Endpoint, EDR, OS baselines. |
| **Cryptography Engineer** | Engineering | "Cryptography Engineer" | Key management, CA hierarchy, TLS posture, FIPS compliance. |
| **Pre-production Reviewer** | Engineering (rotated) | - | Owns the pre-production checklist; signs off on go-live readiness. |
| **Risk Pillar Leader** | Risk | "Risk Pillar Leader" (when speaking of the lead), "Risk Manager" | Pillar accountability; exposure posture reporting; Medium severity risk-acceptance authority per RMF §9.7. |
| **Exposure Management Lead** | Risk | "Exposure Management Lead" | Operates [`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md); owns SLAs and posture metrics. |
| **Adversarial Testing Lead** | Risk | "Adversarial Testing Lead," "Adversarial Testing Lead" | Operates [`CERG-PRC-AV-001`](../procedures/CERG-PRC-AV-001_Adversarial_Validation_Procedure.md); pen test, red team, purple team. |
| **Threat Intelligence Analyst** | Risk | "Threat Intelligence Analyst" | Threat-actor tracking; advisories; intel-to-detection translation. |
| **Vendor Risk Analyst** | Risk | "Vendor Risk Analyst," "Vendor Risk Analyst" | Operates [`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md); SCCT participation. |
| **OT Risk Analyst** | Risk | - | OT-safe vuln assessment, ICS threat intelligence. |
| **Identity Risk Analyst** | Risk | - | UEBA, identity-threat detection, OAuth and token risk. |
| **Detection Engineer** | Risk | "Detection Engineer," "Detection Engineer" | Detection-rule authoring; ATT&CK coverage; tuning lifecycle. |
| **Governance Pillar Leader** | Governance | "Governance Pillar Leader," "Governance Pillar Leader" (when speaking of the lead) | Pillar accountability; regulator and auditor liaison; CISO reporting; Low and Informational severity risk-acceptance authority per RMF §9.7. |
| **NERC-CIP Compliance Manager** | Governance | "NERC-CIP Compliance Manager" | OT and BES Cyber System compliance posture. |
| **CMMC / Federal Compliance Manager** | Governance | "CMMC / Federal Compliance Manager" | CUI posture; SSP and POA&M maintenance. |
| **SOX ITGC Lead** | Governance | "SOX ITGC Lead" | ITGC control evidence and audit coordination. |
| **Policy & Standards Manager** | Governance | "Policy & Standards Manager" | Document library, version control, review cycles. |
| **Risk Register Owner** | Governance | "Risk Register Owner" | Operates [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md); curates the register; runs the Monthly Risk Register Review. |
| **Evidence Librarian** | Governance | - | Cross-framework evidence library curation. |
| **Incident Commander** | Adjacent (IR team) | "IC" | Single-decision authority during an active incident. |
| **Lead Investigator** | Adjacent (IR team) | - | Risk-side technical lead during an active incident. |

> **"CISO designee"**
>
> Several subordinate documents reference a "CISO designee" as an approval authority for tactical risk decisions. The CISO designee is whichever named pillar leader (Engineering, Risk, or Governance) the CISO has formally delegated to act on the CISO's behalf for a specific approval class. Designation is recorded in writing and reviewed at the CISO's discretion at least annually. Where a document needs to name a specific approver, use the canonical role name (e.g., "Risk Pillar Leader"); reserve "CISO designee" for cases where the delegation may rotate between pillars.

### 6.2 Cyber Engineering: Typical Roles

| **Role** | **Focus** |
|---|---|
| Engineering Pillar Leader | Pillar accountability; project intake; reference-architecture authority. |
| Cloud Security Engineer | Cloud platforms, landing zones, IaC, CSPM gating. |
| Identity Engineer | IdP, MFA, SSO, PAM, secrets management, federation. |
| OT Security Engineer | IT/OT convergence, ESP/EAP design, BES Cyber System baselines (see [CERG-STD-OT-001](../standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md)). |
| Application / Application Security Engineer | SAST/DAST integration, SDLC controls, threat modeling. |
| Endpoint / Endpoint Engineer | Endpoint controls, EDR engineering, OS baselines. |
| Cryptography Engineer | Key management, CA, TLS posture, FIPS compliance. |
| Pre-production Reviewer (often a rotated function) | Owns the pre-production checklist; signs off on go-live readiness. |

### 6.3 Cyber Risk: Typical Roles

| **Role** | **Focus** |
|---|---|
| Risk Pillar Leader | Pillar accountability; exposure posture reporting. |
| Exposure Management Lead | Operates [CERG-PRC-VM-001](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md); owns the SLAs and posture metrics. |
| Detection Engineer | CSPM / SSPM operations and detection rules. |
| Threat Intelligence Analyst | Source curation, internal advisories, detection translation. |
| Adversarial Testing Lead (Red Team) | Internal or partner-managed offensive validation. |
| Vendor / Third-Party Risk Analyst | Vendor assessment and continuous monitoring. |
| OT Risk Analyst | OT-safe vulnerability assessment; ICS threat intelligence. |
| Identity Risk Analyst | UEBA, identity-threat detection, OAuth / token risk. |

### 6.4 Cyber Governance: Typical Roles

| **Role** | **Focus** |
|---|---|
| Governance Pillar Leader | Pillar accountability; regulator and auditor liaison; CISO reporting. |
| NERC-CIP Compliance Manager | OT/BES compliance posture (see [CERG-STD-OT-001](../standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md)). |
| [CMMC](https://dodcio.defense.gov/CMMC/) / Federal Compliance Manager | CUI posture (see [CERG-STD-CUI-001](../standards/CERG-STD-CUI-001_CUI_Handling_Standard.md)). |
| [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC Lead | ITGC control evidence and audit coordination. |
| Policy & Standards Manager | Document library curation; review cycles. |
| Risk Register Owner | Operates [CERG-PRC-RM-001](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md); curates the register. |
| Evidence Librarian | Maintains the cross-framework evidence library. |
| Governance Pillar Leader (IR liaison) | Supports the standing IR team with evidence, reporting, regulatory context, and lessons-learned intake. The standing IR team, not CERG Governance, maintains [CERG-PLN-IR-001](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md), runs IR exercises, and owns notification clocks. |

### 6.5 Shared and Rotational Roles

Several roles intentionally sit between pillars and rotate:

- **Architecture Review Office Hours.** Engineering + Risk on rotation.
- **Incident Response support rotation.** CERG provides Engineering, Risk, and Governance support when activated by the standing IR team; the Incident Commander owns incident decisions and IR on-call operations.
- **Audit liaison.** Governance-led with Engineering and Risk SMEs.

---

## 7. Coordination Cadence

CERG operates as one team because it talks like one team. The standing cadence below is the minimum; teams add working sessions as needed.

| **Forum** | **Cadence** | **Participants** | **Purpose** |
|---|---|---|---|
| CERG Leadership Sync | Weekly | CISO + pillar leaders | Cross-pillar priorities, blockers, escalations. |
| Risk Posture Review (High / Critical items) | Weekly | Risk + Engineering + Governance | Top-of-list High and Critical risks, treatment progress, SLA breaches. Aligns with [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) §8.2 weekly cadence for High and Critical items. |
| Monthly Risk Register Review (full register) | Monthly | Risk Register Owner + Risk + Engineering + Governance | Full register pass, POA&M status, treatment closures, exception renewals. Aligns with [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) §8.2 monthly full cadence. |
| Pre-production Review Board | Twice weekly | Engineering + Risk + Governance | Pre-production go/no-go for in-scope projects. |
| Vulnerability Triage | Daily / standing | Risk team + Engineering rep | PPR / Critical / Internet-exposed findings per [`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) §5.2. |
| Threat Intelligence Brief | Weekly | Risk + Engineering + Governance | Relevant intel, posture implications. |
| Compliance Pulse | Bi-weekly | Governance + Engineering + Risk | Open compliance items, evidence gaps, regulator calendar. |
| CERG All-Hands | Monthly | All CERG | Program updates, recognition, knowledge sharing. |
| Cyber Oversight Group (COG) | Monthly | Per §4.4 | Cyber posture, cross-functional risk treatment alignment, pre-board review. |
|| CISO Risk & Posture Review | Quarterly | CISO + leadership | Material risks, posture trends, regulatory cycle, budget. |
|| Succession Readiness Review | Quarterly (concurrent with CISO Risk & Posture Review) | CISO + pillar leaders + HR business partner | Successor identification, readiness assessments per [`CERG-GOV-SUCC-001`](CERG-GOV-SUCC-001_Succession_Planning_and_Talent_Review_Framework.md), development plan progress, critical role risk. |
|| Board Cyber Brief | Quarterly (per board protocol) | CISO → Audit / Risk / Tech Committee | Posture, material incidents, top risks, program initiatives. |


> **Incident Response cadence**

---

## 8. Interfaces With Other Functions

CERG operates inside a broader organizational ecosystem. The following interfaces are explicit.

| **Function** | **Interface** |
|---|---|
| **Incident Response (standing team)** | Owns [`CERG-PLN-IR-001`](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md). CERG feeds detection telemetry, vulnerability context, asset documentation, and post-incident risk-register entries. During an active incident, CERG provides Lead Investigator (Risk), Engineering Lead, and Governance Lead roles per the IR team's call. |
| **Security Awareness** | Coordinated with Governance for content alignment; Risk provides phishing simulation operations and threat-actor context for targeted campaigns. |
| **Internal Audit** | Receives evidence from Governance; engages SMEs from Engineering and Risk; findings tracked in the risk register. |
| **Legal** | Engaged at activation for Sev 1/2 incidents; engaged for regulatory interpretation, breach notification, customer contractual obligations, and privilege judgments. |
| **Privacy / DPO** | Coordinates with Governance on Restricted-data handling and breach notification under GDPR / HIPAA / state laws. |
| **Enterprise Risk Management** | Receives quarterly cyber risk feed at the Cyber Oversight Group (§4.4); interface ensures cyber risks appear in enterprise risk reporting. |
| **Internal Communications / PR** | Engaged for material incident communications and major program announcements. |
| **Procurement / Vendor Management** | Coordinates third-party assessments and DFARS / CMMC flow-down; Governance is the security signatory. |
| **Human Resources** | Coordinates joiner / mover / leaver, personnel risk assessments (NERC-CIP CIP-004), and disciplinary referrals for willful non-compliance. |
| **IT Operations** | Executes Engineering-designed controls; jointly owns endpoint, server, network, and SaaS administration. |
| **OT Operations** | Co-owns CIP-008 incident response, CIP-007 patching cycles, and ESP/EAP architecture. CERG defers to operations on grid-impact judgments. |
| **Business Unit Owners** | Sponsor systems, approve treatments, own residual risk for systems in scope. Designated Executive Sponsors sit on the Cyber Oversight Group when systems in their scope are on the agenda. |
| **Executive Leadership and the Board** | Receive standing CISO reporting via the COG; engaged on Sev 1 incidents and material risk decisions. |

---

## 9. RACI Patterns

The following patterns illustrate how the pillars typically distribute work. Specific RACI matrices are maintained per process. This is a sample; each standard and procedure cited in [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) §10 has its own. Role names follow the canonical roster in §6.1.

### 9.1 New Cloud Workload Goes Live

| **Activity** | **Engineering** | **Risk** | **Governance** | **Business Owner** | **CISO** |
|---|---|---|---|---|---|
| Approve architecture and landing-zone selection | **R / A** | C | C | C | I |
| Implement IAM, network, monitoring controls | **R** | C | I | C | I |
| Pre-production vulnerability assessment | C | **R / A** | I | C | I |
| Approve go-live | **R** | C | C | **A** | I |
| Onboard to CSPM and exposure management | C | **R / A** | I | I | I |
| Add to compliance evidence library | C | I | **R / A** | I | I |

### 9.2 Open High Vulnerability Past SLA

| **Activity** | **Engineering** | **Risk** | **Governance** | **Business Owner** | **CISO** |
|---|---|---|---|---|---|
| Identify SLA breach and escalate | I | **R / A** | I | I | I |
| Recommend compensating controls | **R / A** | C | C | C | I |
| Decide treatment (remediate / mitigate / accept) | C | C | C | **A** | I (review for High+) |
| Approve risk acceptance (if High) | I | C | C | C | **A** |
| Record in risk register | I | C | **R / A** | I | I |

### 9.3 CMMC Pre-Assessment Cycle

CMMC pre-assessment work involves two acronyms that appear without prior explanation elsewhere in the suite:

- **SPRS** - Supplier Performance Risk System. The DoD-operated portal where contractors post their NIST 800-171 self-assessment score and basic assessment confirmation.
- **C3PAO** - CMMC Third-Party Assessment Organization. An accredited assessor authorized by the Cyber AB to conduct CMMC Level 2 certification assessments.

| **Activity** | **Engineering** | **Risk** | **Governance** | **Business Owner** | **CISO** |
|---|---|---|---|---|---|
| Maintain SSP and POA&M | C | C | **R / A** | I | I |
| Conduct self-assessment | C | **R** | **A** | C | I |
| Submit SPRS score | I | C | **R / A** | I | I |
| C3PAO engagement | I | C | **R / A** | I | C |
| Remediate POA&M items | **R** | C | **A** | C | I |

---

## 10. Maturity, Metrics, and the Adaptive Target

### 10.1 The Adaptive Target

CERG targets NIST Cybersecurity Framework **Tier 4, Adaptive** posture for the organization. Adaptive does not mean "constantly changing." It means the organization understands its risk environment, continuously adjusts its program based on what it learns, integrates cybersecurity into enterprise risk and business decisions, and treats lessons learned as a first-class input to the program.

### 10.2 Maturity Indicators

The following indicators are tracked by Governance and reported to the CISO and the Cyber Oversight Group. They are leading indicators of program maturity, not lagging measures of incident counts. Target values, green/amber/red thresholds, escalation triggers, and reporting cadence live in [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) §3; this section names the indicators only.

| **Indicator** | **What It Measures** | **Canonical Metric ID** |
|---|---|---|
| % of in-scope assets in real-time inventory | Visibility | MTR-001 ID-001 |
| % of new projects passing pre-production review on first attempt | Engineering quality and "shift left" effectiveness | MTR-001 CM-002 |
| Median time-to-remediate by severity | Risk responsiveness | MTR-001 RM-003 / VM-001 |
| % of findings within SLA | Risk discipline | MTR-001 VM-001 / VM-002 |
| Open exception count and median age | Governance discipline | MTR-001 RM-004 / RM-005 |
| % of risks reviewed within scheduled review date | Risk register health | MTR-001 RM-002 |
| % of identified High risks with active treatment plans | Treatment discipline | MTR-001 RM-001 |
| Time from incident detection to containment (Sev 1/2) | Response capability (IR team owns) | (IR-owned; coordinated with MTR-001) |
| % of IRT roles backstopped (no single point of failure) | Continuity | MTR-001 GV-003 |
| Audit / assessor findings (count and severity) per cycle | External validation | MTR-001 GV-001 / GV-002 |
| Phishing simulation susceptibility trend | Workforce posture (Awareness owns) | (Awareness-owned; coordinated with MTR-001) |
| % of vendor reassessments current | Third-party risk discipline | MTR-001 TP-001 / TP-002 |

### 10.3 Continuous Improvement

Every CERG activity produces feedback into the program backlog:

- Post-incident lessons → Engineering, Risk, Governance backlog items
- Audit findings → POA&M / risk register entries with treatment plans
- Exercise results → Plan and playbook updates
- Adversarial validation findings → Detection rules, posture controls, architectural changes
- Threat intelligence → Standing detection and control updates

The backlog is reviewed monthly. Items that age beyond planned dates without justification are flagged to the CISO and surfaced to the Cyber Oversight Group.

### 10.4 Knowledge Transfer and Cross-Training

The CERG Framework (FRM-001 Section 9.2) describes the "Left-Right Knowledge Model" as a mechanism for talent resilience: engineers learn Risk thinking, Risk analysts understand Governance, and Governance practitioners understand what is technically possible. Domain X5 in the maturity assessment (MAT-001) scores single-point-of-failure resilience. CERG claims critical roles are backstopped and knowledge is "in the system."

This section defines how the organization produces evidence that knowledge transfer is actually occurring, not just claimed.

#### 10.4.1 Cross-Training Log

Each pillar maintains a lightweight cross-training log. The log records cross-pillar knowledge activities:

| Field | Example |
|---|---|
| Date | 2026-03-15 |
| Participants | Cloud Security Engineer (Engineering), Threat Intelligence Analyst (Risk) |
| Activity Type | Shadowing / Joint review / Cross-pillar presentation / Rotation assignment |
| Topic | Threat modeling cloud architecture : Risk shares ATT&CK cloud matrix techniques; Engineering shares landing-zone design patterns |
| Duration (hours) | 2 |

The log is intentionally lightweight. It is not a training management system. Its purpose is to provide evidence that cross-pillar knowledge transfer is occurring on a regular cadence.

#### 10.4.2 Documentation Completeness

Knowledge "in the system" means knowledge that survives when the person who holds it is unavailable. Documentation completeness is measured by two metrics tracked in MTR-001:

- **KM-001: Procedure Documentation Currency.** Percentage of critical processes with current (less than or equal to 12-month) procedure documentation. A procedure is "critical" if it supports a control marked Implemented in CB-001.
- **KM-002: Role Backup Currency.** Percentage of canonical roles with a documented secondary or backup who has performed the role in an exercise or real event within 18 months. "Performed" means the backup has executed the role's core responsibility at least once, not just been named on an org chart.

#### 10.4.3 Cross-Training Expectations

The minimum cross-training expectation per team member is 4 hours per quarter of cross-pillar knowledge activity. This is tracked as metric KM-003 in MTR-001.

Cross-training activities that qualify:
- Shadowing a cross-pillar review or engagement
- Presenting cross-pillar content at a CERG All-Hands or pillar sync
- Participating in a joint review (architecture, threat model, risk assessment) where the participant is from a different pillar than the lead
- Rotation assignment of at least one week duration in a different pillar
- Participating in a tabletop exercise in a role different from the participant's day-to-day role

#### 10.4.4 Maturity Assessment Integration

At the annual maturity assessment (MAT-001), domain X5 (Single-Point-of-Failure Resilience) scoring is amended as follows:

A domain scores Adaptive in X5 only when:
- (a) Critical roles are backstopped (existing criterion), AND
- (b) At least one cross-training activity is documented per critical role per year, AND
- (c) Documentation currency metrics (KM-001, KM-002) are green

This ensures that "no single point of failure" is not just a claim about org-chart coverage but is backed by evidence of actual knowledge transfer and current documentation.

---

## 11. Operating Model Control

| | |
|---|---|
| **Document ID** | CERG-GOV-OM-001 |
| **Version** | 1.23 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Chief Information Security Officer |
| **Approved By** | CISO |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual / Upon Organizational Change |
| **Next Scheduled Review** | 2027-06-14 |
| **Frameworks** | NIST CSF 2.0 · NIST 800-53r5 · NIST RMF · ISO 27001 |
| **Environments** | All in-scope environments |


### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.24 | 2026-06-18 | Governance Pillar Leader | Updated §4.4 COG membership with explicit standing-core and dynamic-per-agenda members (Business Unit Risk Owner for systems on agenda, Engineering/Risk pillar leaders as needed). Added COG Agenda Template with dynamic attendee section. |
| 1.23 | 2026-06-14 | Governance Pillar Leader | Removed residual IR Plan Steward language and clarified that CERG provides IR support while the standing IR team owns the IR plan, exercises, notification clocks, and incident command. |
| 1.0 | 2026-05-01 | CISO + Cyber Governance | Initial release. Establishes the three pillars, decision rights, engagement models, the canonical role roster (§6.1), the Cyber Oversight Group (§4.4), the standing coordination cadence aligned with CERG-RMF §8.2, and the maturity indicator set cross-referenced to CERG-GOV-MTR-001. Clarifies that the Incident Response plan and capability are owned by a standing IR team outside CERG; CERG provides liaison roles and feeds data into the IR program. |
| 1.22 | 2026-05-26 | Cyber Governance | Added Section 10.4 Knowledge Transfer and Cross-Training: cross-training log schema, documentation completeness metrics (KM-001, KM-002), cross-training expectations (KM-003, minimum 4 hours/quarter), and maturity assessment integration for domain X5 Adaptive scoring. |

### Review Triggers

This operating model shall be reviewed annually and upon any of the following:

- Material organizational change affecting CERG structure or reporting
- Material change to scope (e.g., new regulated environment, major M&A)
- A Sev 1 incident or significant audit finding that reveals a structural gap
- CISO transition
- Direction from executive leadership or the board

The CISO owns this document. Cyber Governance maintains it on behalf of the CISO. Changes require CISO approval and broad CERG acknowledgment.

### Related Documents

The authoritative inventory is [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md). The references below are the V1 library at a glance, grouped by role within the operating model.

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | Parent policy - defines the CERG operating model at the principle level |
| Document Catalog and Naming Convention | [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Authoritative inventory of every CERG artifact |
| Unified Control Baseline | [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md) | Control spine, overlays, evidence mapping |
| Metrics, Dashboard, and CISO/Board Reporting | [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) | KRIs, KPIs, CISO dashboard |
| Risk Management Framework | [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) | Lifecycle, FAIR risk statement, canonical approval table, KRI definitions |
| Compliance Matrix | [`CERG-GOV-CMX-001`](CERG-GOV-CMX-001_Compliance_Matrix.md) | Cross-regulator control intent alignment |
| Risk Taxonomy | [`CERG-GOV-TAX-001`](CERG-GOV-TAX-001_Risk_Taxonomy.md) | Risk language and categorization |
| CERG Framework | [`CERG-GOV-FRM-001`](CERG-GOV-FRM-001_CERG_Framework.md) | Narrative framework document |
| Grid Control Systems Security Standard | [`CERG-STD-OT-001`](../standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) | OT pillar adaptations |
| IT (Hosted/Cloud/SaaS) Security Standard | [`CERG-STD-IT-001`](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) | IT, cloud, and SaaS pillar adaptations |
| CUI Handling Standard | [`CERG-STD-CUI-001`](../standards/CERG-STD-CUI-001_CUI_Handling_Standard.md) | CUI scope, SSP/POA&M, CMMC L2 |
| Access Management Standard | [`CERG-STD-AC-001`](../standards/CERG-STD-AC-001_Access_Management_Standard.md) | Identity lifecycle, MFA, access reviews |
| Secure Configuration Baseline Standard (DISH) | [`CERG-STD-CFG-001`](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) | DISH baselines |
| Logging, Monitoring, and Detection Standard | [`CERG-STD-LM-001`](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) | Log sources, retention, detection coverage |
| Cyber Resilience and Backup Standard | [`CERG-STD-RES-001`](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) | RTO/RPO, backup, recovery |
| Cryptography and Key Management Standard | [`CERG-STD-CR-001`](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) | Cipher, key, certificate lifecycle |
| Exposure Management Procedure | [`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) | Canonical vulnerability remediation SLAs |
| Risk Register and Exception Process | [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Risk register operating procedure |
| Architecture Review and Project Intake Procedure | [`CERG-PRC-AR-001`](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) | Pre-production engagement |
| Access Management Runbook | [`CERG-PRC-AC-002`](../procedures/CERG-PRC-AC-002_Access_Management_Runbook.md) | Identity lifecycle operations |
| Third-Party and Supply Chain Risk Procedure | [`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) | Vendor tiering, SCCT |
| Adversarial Validation Procedure | [`CERG-PRC-AV-001`](../procedures/CERG-PRC-AV-001_Adversarial_Validation_Procedure.md) | Pen test, red team, purple team |
| Incident Response Plan | [`CERG-PLN-IR-001`](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md) | Owned by the standing IR team; CERG provides liaison roles |
| CUI / CMMC Operational Package | [`CERG-PLN-CUI-001`](../plans/CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md) | CUI/CMMC operational bundle |
| NERC-CIP Operational Package | [`CERG-PLN-CIP-001`](../plans/CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md) | NERC-CIP operational bundle |
| SOX ITGC Operational Package | [`CERG-PLN-SOX-001`](../plans/CERG-PLN-SOX-001_SOX_ITGC_Operational_Package.md) | SOX ITGC operational bundle |
| Risk Register Templates and Reporting | [`CERG-TMPL-RM-001`](../templates/CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md) | Register schema, report templates |
