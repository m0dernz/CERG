## ARCHITECTURE REVIEW AND PROJECT INTAKE PROCEDURE
### Intake · Review · Threat Model · Pre-Production · Handoff · Go-Live Risk Acceptance

---

| | |
|---|---|
| **Document ID** | CERG-PRC-AR-001 |
| **Version** | 1.7 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Engineering Pillar Leader |
| **Parent Policy** | [CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [CERG-GOV-CB-001](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) · [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) · [CERG-STD-OT-001](../standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) · [CERG-STD-CUI-001](../standards/CERG-STD-CUI-001_CUI_Handling_Standard.md) · [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) · [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) · [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) · [CERG-STD-RES-001](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) · [CERG-STD-CR-001](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) · [CERG-PRC-TM-001](CERG-PRC-TM-001_Threat_Modeling_Procedure.md) · [CERG-PRC-RM-001](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) · [CERG-PRC-TPRM-001](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) |
| **Review Cycle** | Annual / On platform or process change |
| **Frameworks** | [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) · [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) (PL, SA, SC) · NIST 800-160 · NIST SSDF · CSA STAR |
| **Regulations** | [CMMC L2](https://dodcio.defense.gov/CMMC/) · NERC-CIP CIP-005/CIP-010 · SOX ITGC (Change) |
| **Environments** | All in-scope projects - IT, cloud, SaaS, OT, hybrid |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Roles and Responsibilities](#2-roles-and-responsibilities)
3. [The Five-Phase Engagement Model](#3-the-five-phase-engagement-model)
4. [Who Needs a Review, and Who Doesn't](#4-who-needs-a-review-and-who-doesnt)
5. [Phase 1, Intake](#5-phase-1-intake)
6. [Phase 2, Architecture Review and Threat Model](#6-phase-2-architecture-review-and-threat-model)
7. [Phase 3, Build-Time Engagement](#7-phase-3-build-time-engagement)
8. [Phase 4, Pre-Production Security Review](#8-phase-4-pre-production-security-review)
9. [Phase 5, Production Handoff and Go-Live](#9-phase-5-production-handoff-and-go-live)
10. [Required Diagrams](#10-required-diagrams)
11. [Templates](#11-templates)
12. [Metrics](#12-metrics)
13. [Regulatory and Framework Alignment Summary](#13-regulatory-and-framework-alignment-summary)
14. [Pre-Approved Architecture Patterns](#14-pre-approved-architecture-patterns)
15. [Document Control](#15-document-control)

---

## 1. Purpose and Scope

The Operating Model makes Engineering project engagement a core CERG delivery model. The RMF Phase 3 describes concept, design, build, pre-production, and production handoff outputs. Until this procedure, the intake forms, review checklists, threat modeling guidance, signoff criteria, and handoff packages those phases require existed implicitly.

This procedure defines how a project enters CERG attention, how Engineering reviews it, how Risk threat-models it, how findings flow to remediation or risk acceptance, and how the system enters production with the right documentation, baselines, monitoring, and accepted exceptions.

The standalone [`CERG-TMPL-AR-001`](../templates/CERG-TMPL-AR-001_Architecture_and_Project_Intake_Form.md) is the canonical front-door intake form for Phase 1. This procedure remains authoritative for the Phase 2 architecture review record, Phase 4 pre-production security review record, Phase 5 production handoff package, and go-live risk acceptance packet.

> **Engineering's Job Is to Be in the Room Early**
>
> Architecture review is not a gate that bolts security onto a project at the end. It is the discipline of having Engineering in the design conversation early enough to change the design cheaply. A review that consistently surfaces "we have to redo the data flow now" is a review that came too late.

---

## 2. Roles and Responsibilities

| **Role** | **Responsibility** |
|---|---|
| **Project Sponsor / Business Owner** | Submits intake; names the internal Service Owner before handoff where the project creates a service; owns the project's residual risk. The named accountable business or service owner holds the go-live decision ([`RAC-001`](../governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) §6.1). |
| **Project / Technical Lead** | Produces architecture artifacts and answers reviewer questions. The named first-line operator deploys, operates, and remediates the resulting service through its change process. |
| **CERG - Pre-production Reviewer** | Conducts the technical review, records findings, and states a technical disposition. Does not approve go-live. |
| **Application Security Engineer** | Provides application, API, SDLC, and software-architecture review input; defines candidate test content; and independently tests within approved scope. Does not operate the pipeline, scanner, release gate, or production deployment. |
| **Risk Pillar Leader / assigned Risk reviewer** | Leads threat modeling per [`CERG-PRC-TM-001`](CERG-PRC-TM-001_Threat_Modeling_Procedure.md), contributes adversary context, and ensures threat-model findings receive a disposition. |
| **Vendor Risk Analyst** | Performs third-party and supply-chain assessment per [`CERG-PRC-TPRM-001`](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) when vendors, SaaS providers, MSPs, software suppliers, or external integrations are involved. |
| **Governance Pillar Leader** | Maps the project into the regulatory scope (CUI / BES / SOX) and triggers the relevant overlay reviewers. |
| **Engineering Pillar Leader** | Reviews the Engineering technical disposition and proposed compensating controls; escalates material disagreement. The business or service owner initiates any residual-risk route, and only the authority named in [`CERG-GOV-RMF-001`](../governance/CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.7 accepts it. |
| **CISO** | Settles escalated technical dispositions. A CERG or CISO escalation cannot itself authorize, deny, or compel a go-live decision, which remains the accountable owner's. Accepts residual risk only where the canonical authority table names the CISO. |
| **IT Change Advisory Board (CAB)** | Hosts the go-live conversation; CERG review status is a CAB input, not a substitute for change management. |

---

## 3. The Five-Phase Engagement Model

CERG engagement with a project follows five phases. Not every project hits every phase, Section 4 names the carve-outs.

1. **Intake**, register the project; classify scope; determine review depth.
2. **Architecture Review and Threat Model**, design-stage review; threats and controls aligned to [`CERG-GOV-CB-001`](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md).
3. **Build-Time Engagement**, secure SDLC checks, IaC review, baseline conformance.
4. **Pre-Production Security Review**, readiness against the review findings, baselines, monitoring, and recovery.
5. **Production Handoff and Go-Live**, handoff package complete, risk acceptances approved, asset added to inventory and recurring controls.

---

## 4. Who Needs a Review: and Who Doesn't

Reviewing every Power App or low-code workflow is how Engineering loses a quarter to busywork. Waving them all through is how Shadow IT eats the enterprise. CERG's answer is: **review the platform once, then trust the guardrails the platform enforces.**

### 4.1 Mandatory Review

CERG Architecture Review is mandatory for projects that meet any of the following:

- Introduces a new IaaS / PaaS / cloud account, subscription, or project.
- Introduces a new SaaS service (any tier) handling business data.
- Touches OT / BES Cyber Systems or the IT/OT boundary (per [`CERG-STD-OT-001`](../standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md)).
- Handles CUI (storage, processing, transmission) or changes the CUI boundary.
- Handles SOX-relevant financial data or process flows.
- Introduces or changes a third-party network connection.
- Modifies the production identity provider, federation, or PAM topology.
- Introduces a new authentication path to a system holding Restricted data.
- Crosses a trust boundary (network, identity, tenant, region, organization).
- Introduces a new data classification or regulatory scope into the environment.

### 4.2 Lightweight Review (Engineering Self-Service)

A lightweight, self-service review pattern (intake form + checklist + Engineering technical review without full Phase 2) is acceptable for projects that:

- Reuse an already-reviewed pattern (e.g., new microservice on an already-reviewed Kubernetes cluster).
- Add capacity to an already-reviewed system.
- Use a pre-approved IaC module or service catalog template.

### 4.3 Citizen-Development Carve-Out

Citizen-development platforms (Power Platform, low-code app builders, business-managed automation) are not reviewed *per app*. They are reviewed once, at platform onboarding, with the assessment focused on the platform's guardrails, then trusted to police the apps that run on it.

| **Citizen-Dev Platform Assessment** | **Required at Platform Onboarding** |
|---|---|
| Identity and access | SSO + MFA + role-based admin model + audit log to SIEM |
| Data egress | Data Loss Prevention policy on connectors; sensitive connectors restricted |
| Data classification awareness | Sensitivity labels surfaced to citizen developers; export restrictions enforced |
| External sharing | Disabled by default; named exception path |
| Lifecycle | App lifecycle policy: ownership required, dormant apps culled, transfer-on-departure |
| Telemetry | Audit log forwarded to SIEM; admin actions monitored |
| Detection set | Day-one detections per [`CERG-STD-LM-001`](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |

Apps built on the platform are governed by these guardrails. Where an app needs to step outside the guardrails (e.g., a new connector, an unusual data classification), it triggers Mandatory Review per Section 4.1.

> **The Test**
>
> If a citizen-development app cannot do anything outside the platform's guardrails, CERG does not need to review it. If a platform's guardrails are weaker than CERG's standards, the platform is unsuitable for the data classification it's hosting. Apps get reviewed only when they need to step outside the boundary.

### 4.4 What Does Not Need CERG Review

- Pure UX or visual changes to an existing system that don't touch authentication, data classification, scope, or interfaces.
- Routine patching covered by [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Exposure_Management_Procedure.md).
- Routine configuration changes within the DISH-conformant pattern that don't change trust boundaries.

### 4.5 Approved Pattern Register

Lightweight review depends on knowing which patterns are already approved. Engineering maintains an Approved Pattern Register as part of the architecture review record set. A pattern may be a reference architecture, IaC module, landing-zone template, CI/CD pipeline profile, SaaS configuration pattern, citizen-development guardrail set, or service-catalog template.

Each approved pattern records:

| **Field** | **Purpose** |
|---|---|
| Pattern ID and name | Stable reference used by intake and project records. |
| Pattern owner | Engineering role accountable for keeping the pattern current. |
| Approved use cases | What the pattern may be used for without full re-review. |
| Approved data classifications / regulatory scopes | Maximum data and regulatory scope allowed under the pattern. |
| Required controls and evidence | Baselines, guardrails, logging, detection, recovery, and evidence links. |
| Known limitations | Conditions that trigger mandatory review instead of reuse. |
| Last review / next review | Currency of the approval. |
| Review triggers | Events that require re-review: major platform change, control failure, new regulatory scope, material finding, or threat intelligence change. |

A project claiming lightweight review must cite the approved pattern it reuses and confirm it stays inside the pattern's approved scope. If the project changes the pattern, extends it to a higher data classification, crosses a new trust boundary, or disables a required guardrail, it becomes Mandatory Review.

---

## 5. Phase 1: Intake

Intake is fast (< 5 business days) and produces a Scope Determination that drives every subsequent phase.

### 5.1 Security Project Intake Form (Template)

Use [`CERG-TMPL-AR-001`](../templates/CERG-TMPL-AR-001_Architecture_and_Project_Intake_Form.md) for the authoritative Phase 1 intake form. The structure below is retained as the procedure-level minimum content model and for adopters embedding intake directly into a ticketing system.

```
SECURITY PROJECT INTAKE - AR-YYYY-NNNN

A. PROJECT IDENTITY
   Project Name             :
   Sponsor (named role)     :
   Technical Lead           :
   Business Outcome         :
   Target Production Date   :

B. SCOPE
   Data Classifications Handled : Public / Internal / Restricted / CUI / BCSI
   Regulatory Scope             : None / CUI / BES / SOX (multi-select)
   Operating Units Impacted     :
   Environments                 : IT / Cloud / SaaS / OT / Hybrid
   Geographies                  : (countries; flag non-US access)
   Trust Boundaries Crossed     : (network / identity / tenant / org)

C. TECHNOLOGY
   New SaaS introduced?         : Y/N - name(s) - vendor(s)
   New cloud account/sub/proj?  : Y/N
   New OT touch / IT/OT bridge? : Y/N
   New external connection?     : Y/N
   New identity / federation?   : Y/N

D. THIRD PARTIES
   Vendors involved             : list
   Vendor tier (per TPRM)       :
   International access?        : Y/N - countries

E. CHANGE CONTEXT
   New build / migrate / retire / extend
   Existing CERG-tracked asset IDs (if extension)

F. INITIAL SECURITY CONCERNS (from project team)
   What worries us most         :
   What we know is unresolved   :

G. ASKS
   What CERG help do we need at design stage?
```

### 5.2 Scope Determination Output

The Intake reviewer (CERG Engineering) determines:

- Review path: **Mandatory** (Phase 2 full), **Lightweight** (self-service checklist), or **Out of Scope**.
- Overlay reviewers required: CUI, BES, SOX, OT, each named by [`CERG-GOV-CB-001`](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md).
- Threat modeling required: Y/N (default Y for Mandatory; conditional for Lightweight).
- TPRM engagement required: Y/N (default Y if any vendor is new or tier > business default).
- Estimated Phase 2–5 effort and target dates.

A Scope Determination is recorded against the project and visible to the team within five business days.

### 5.3 Review Path and SLC Tier Crosswalk

The review path determines how much review is required. The SLC tier determines the response clock published to the business in [`CERG-GOV-SLC-001`](../governance/CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md). Intake records both values.

| **AR Review Path** | **Default SLC Tier** | **Examples** | **Notes** |
|---|---|---|---|
| Mandatory | Tier 1 | OT / BES, CUI, Restricted-data SaaS, new cloud account, new internet-facing service, AI with sensitive data | Use Tier 2 only if the mandatory trigger is narrow, low-blast-radius, and non-regulated. |
| Mandatory | Tier 2 | Standard internal application, material change to an existing non-regulated system, new vendor integration without Restricted data | Full review required, but lower urgency / complexity than Tier 1. |
| Lightweight | Tier 3 | Reuse of approved pattern, pre-approved IaC module, added capacity to reviewed system | Checklist and evidence review; no full Phase 2 unless the reviewer escalates. |
| Out of Scope | N/A | Pure UX change, routine patching, configuration change within approved baseline | Record disposition only; no SLC review clock beyond intake acknowledgement. |

Where the review path and SLC tier appear to disagree, the Engineering Pillar Leader records the rationale. Regulated scope, new trust boundaries, and Restricted-data placement always bias upward.

---

## 6. Phase 2: Architecture Review and Threat Model

### 6.1 Architecture Review Checklist

The reviewer works through the checklist below; findings are recorded with severity and routed per [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md).

| **Area** | **Review Item** | **Standard Reference** |
|---|---|---|
| Identity | SSO + MFA + role model + JIT for privileged + service account pattern | STD-AC-001 |
| Authorization | Least privilege; SoD where applicable; tenant / record / field scoping | STD-AC-001 / GOV-CB-001 AC-5 |
| Data classification | Classification recorded; controls match classification | STD-CUI-001 / STD-IT-001 |
| Cryptography | Algorithms approved; CMK where required; secrets pattern; FIPS where applicable | STD-CR-001 |
| Network | Segmentation; default deny; logging; trust boundaries marked | STD-IT-001 / STD-OT-001 |
| Configuration | DISH tier; baseline applied; drift detection | STD-CFG-001 |
| Logging | Mandatory sources onboarded; retention; immutability | STD-LM-001 |
| Detection | Day-one detection set committed for environment | STD-LM-001 |
| Exposure management | Observation sources and authenticated scanning in scope; classification and treatment SLAs agreed | PRC-VM-001 |
| Resilience | RTO/RPO tier; backup; restoration test plan | STD-RES-001 |
| Third party | Vendor tier; evidence by tier; SCCT in workflow; international access guardrail | PRC-TPRM-001 |
| OT (if applicable) | Active scan rules; passive monitoring; safety review; CIP applicability | STD-OT-001 / PLN-CIP-001 |
| CUI (if applicable) | Boundary marked; FIPS crypto; flow-down; FedRAMP equivalency captured | STD-CUI-001 / PLN-CUI-001 |
| SOX (if applicable) | ITGC mapping; evidence reuse | PLN-SOX-001 |
| Citizen-dev (if applicable) | Built on approved platform with guardrails; data classification compatible | This procedure §4.3 |
| Diagrams provided | Context · Data flow · Network · Identity · Trust boundary · OT boundary (where applicable) | This procedure §10 |
| Risk register entries | All findings entered; treatment proposed | PRC-RM-001 |

### 6.2 Threat Model

The threat model is owned by CERG Risk in collaboration with the project. It uses STRIDE as the default decomposition for IT and a STRIDE-LM (with Lateral Movement) variant for OT. The format is a short Markdown document with the following structure:

```
THREAT MODEL - <Project Name>            AR-YYYY-NNNN - TM-001

1. ASSETS AND DATA - what's worth protecting, with classification
2. ACTORS AND ENTRY POINTS - humans, machines, external services
3. TRUST BOUNDARIES - drawn on the diagram; named in text
4. THREATS BY BOUNDARY - STRIDE per boundary; OT add Lateral Movement
5. EXISTING CONTROLS - what mitigates each threat
6. RESIDUAL - what remains, mapped to risk register entries
7. ATTACK SIMULATION CANDIDATES - for purple / red engagements (PRC-AV-001)
```

> **The Threat Model Earns Its Keep When It Changes the Design**
>
> A threat model that documents what was already decided is paperwork. A threat model that surfaces a control the design missed, a missing boundary, a misplaced trust, is the reason the review exists.

### 6.3 Phase 2 SLA

Phase 2 review (Architecture Review and Threat Model) follows the SLC tier assigned at intake: Tier 1 within 10 business days, Tier 2 within 7 business days, and Tier 3 within 5 business days where Phase 2 is required. Extensions may be granted by the Engineering Pillar Leader for complex systems (e.g., multi-cloud, OT-integrated, or CUI-scope systems with novel architecture). The project team is notified of any extension with rationale within the original SLA window.

### 6.4 Phase 2 Output

- Architecture Review record with technical disposition `Ready` / `Ready-with-Conditions` / `Not Ready`. These three are the **Phase 2 design dispositions**; the Phase 4 pre-production dispositions in §8.3 are a different set recording a different moment.
  - **Ready**: the review names no condition to carry into build.
  - **Ready-with-Conditions**: the review names conditions the project carries into build, including findings that must be remediated before the Phase 4 review.
  - **Not Ready**: the design has unresolved conditions that cannot be carried into build. The business or service owner decides whether to proceed; unresolved validated residual risk follows the acceptance route in `RMF-001` §9.7, not a Phase 2 record.
- Threat model attached.
- Findings in the risk register, scored.
- Build-time conditions for Phase 3.

A technical disposition is not a go-live decision. The business or service owner decides whether to proceed after considering it; unresolved validated residual risk follows the existing risk-acceptance authority.

---

## 7. Phase 3: Build-Time Engagement

Build-time engagement is the period between design review and pre-production. CERG differentiates between routine and novel builds.

### 7.1 Routine vs. Novel Builds

| **Build Type** | **Definition** | **CERG Posture** |
|---|---|---|
| Routine | Deploys a pre-approved architecture pattern or IaC module without modification; uses an existing pipeline with all gates active; no new trust boundary, data path, or integration | Light-touch: CERG does not actively review unless pipeline gate failures trigger review |
| Novel | Introduces a new IaC module, a new service pattern, a new integration, or a material change from the Phase 2 architecture; or is the first deployment of a new application stack | CERG actively reviews the build artifacts |

The Engineering Pillar Leader determines whether a build is routine or novel based on the Phase 2 architecture review record and the project's pipeline configuration.

### 7.2 CERG Review Checklist for Novel Builds

| **Check** | **Pass Criteria** | **Evidence** |
|---|---|---|
| IaC conformance | IaC modules match the approved architecture per Phase 2; no material deviations | IaC diff or module reference |
| Pipeline gates active | DISH baseline scan, container image signing, SBOM generation, and vulnerability scan are all enforced (not optional) in the CI/CD pipeline | Pipeline configuration |
| Secrets scanning | No secrets detected in repository, build artifacts, or container images; secrets manager integration is wired and tested | Secrets scan output |
| SBOM generated | Software Bill of Materials is produced for every build; SBOM is stored with the build artifact | SBOM artifact |
| Image signing | Container images are signed per [CERG-STD-CR-001](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) | Image signature verification |
| Exposure scan gate | Build fails if Critical or High application or dependency exposures are detected; Medium and below are flagged for tracking | Pipeline scan output |

### 7.3 Acceptance Criteria for Build-Time Gates

| **Gate** | **Blocking** | **Non-Blocking** |
|---|---|---|
| DISH baseline conformance | Non-conformance on Critical or High severity settings | Low severity or informational deviations (flagged) |
| Exposure scan | Critical or High application dependency exposures | Medium or Low findings (tracked in exposure backlog) |
| Secrets scanning | Any confirmed secret detected | False positive (documented and suppressed) |
| Image signing | Unsigned image in a pipeline that requires signing | - |

### 7.4 Escalation for Build-Time Findings

Build-time findings are escalated within the development team first, then to CERG:

| **Trigger** | **Action** |
|---|---|
| Pipeline gate failure (Critical/High) | Development team must resolve before build proceeds; CERG notified |
| Repeated gate failure (≥ 3 builds) | CERG reviews; may trigger conditional re-review under Phase 2 |
| Disabling or bypassing a security gate | Treated as a security incident; CISO notified |

### 7.5 SLA for Build-Time Review

CERG completes novel-build review within 3 business days of notification. If the review cannot be completed within SLA, Engineering documents the delay, schedules the follow-up review, and notifies the project team. The first-line pipeline operator enforces blocking gates. If the accountable owner proposes proceeding with unresolved validated residual risk, it follows the existing risk-acceptance process; Engineering does not accept business risk on behalf of the owner.

The artifacts produced during build include: IaC review for new modules and patterns; pipeline gates enforcing DISH baseline conformance, container image signing, SBOM generation, and exposure scanning; secrets checking; and conditional re-review if material design changes happen between Phase 2 and Phase 4.

---

## 8. Phase 4: Pre-Production Security Review

Pre-Production review is a focused, time-boxed readiness check. It produces a Pre-Production Security Review Record.

### 8.1 Pre-Production Checklist

| **Check** | **Pass Criteria** | **Evidence** |
|---|---|---|
| DISH baseline applied | Pass against the asset's tier in [`CERG-STD-CFG-001`](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) | DISH scan output |
| Exposure posture | No unremediated, unaccepted Critical exposures; High open ≤ approved exception count from Phase 2 | Exposure pipeline report |
| Identity wired | SSO + MFA enforced; PAM model in place; service accounts via approved pattern | IdP / PAM policy export |
| Logging | Mandatory sources onboarded; SIEM ingest verified; retention configured | SIEM source inventory |
| Detection | Day-one detection set enabled in the environment | Detection coverage report |
| Cryptography | TLS configuration matches [`CERG-STD-CR-001`](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md); CMK where required; secrets pattern in use | Configuration evidence |
| Resilience | Backups configured per tier; first restoration test scheduled | Backup config; resilience register entry |
| Vendor / TPRM | Vendor records current; evidence-by-tier complete; SCCT in workflow | TPRM tool entries |
| Regulatory overlay artifacts | CUI / BES / SOX artifacts populated per relevant package | Per overlay |
| Phase 2 conditions cleared | All conditions either met or accepted through the risk process | Phase 2 record annotations |
| Asset inventory | System added; ownership recorded | Asset inventory |
| Run-book / on-call | Service has documented on-call and run-book | Run-book reference |
| Change management | Go-live aligned with CAB cadence | Change record |

### 8.2 Phase 4 SLA

Pre-Production Security Review is completed within 5 business days of the project team submitting the Pre-Production checklist evidence. Extensions may be granted by the Risk Pillar Leader where evidence review requires additional subject matter expertise.

### 8.3 Outcome

These three are the **Phase 4 pre-production dispositions**. They are not the Phase 2 design dispositions in §6.4: a design review carries build conditions forward, while a pre-production review records whether acceptances exist before go-live.

- **Ready**: the technical review identifies no unresolved blocking condition.
- **Ready-with-Risk-Acceptance**: outstanding findings have risk register entries with approval under the existing risk-acceptance authority.
- **Not Ready**: the technical review identifies conditions that remain unresolved. The business or service owner decides whether to proceed; unresolved validated residual risk follows the existing risk-acceptance authority, and CERG may escalate disagreement.

---

## 9. Phase 5: Production Handoff and Go-Live

### 9.1 Production Handoff Package

The handoff package is the single artifact that goes into the asset's record. It is a Markdown bundle with the contents below.

```
PRODUCTION HANDOFF PACKAGE - <System Name>     AR-YYYY-NNNN - PHP-001

1. SYSTEM IDENTITY
   Asset ID(s)  · Tier · Owners · Regulatory scope

2. CERG REVIEW RECORD
   Phase 1 Intake reference
   Phase 2 Architecture Review record (link)
   Phase 2 Threat Model (link)
   Phase 3 build conditions cleared (yes/no)
   Phase 4 Pre-Production record (link)

3. CONTROL POSTURE AT GO-LIVE
   Control-by-control state per [CERG-GOV-CB-001](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) (Implemented / Partial / Inherited / Planned / Risk Accepted / N/A)
   Inheritance Evidence Packages on file (cloud / SaaS providers)

4. EVIDENCE POINTERS
   DISH scan output (latest)
   Exposure scan / pipeline output (latest)
   Identity / detection / logging configuration
   Backup configuration and first restoration test plan

5. RISK ACCEPTANCES AT GO-LIVE
   Exception IDs and approvers
   Treatment plans and expiration dates

6. ONGOING CONTROL OBLIGATIONS
   Recurring controls (scan cadence, recert cadence, restoration test cadence)
   Owners for each recurring control

7. RUN-BOOK AND ON-CALL
   References

8. REVIEW AND DECISION
   Engineering Reviewer (technical disposition)
   Risk Reviewer (technical input)
   Governance (overlay) Reviewer(s) - CUI / BES / SOX as applicable
   Engineering Pillar Leader (technical escalation where used)
   Business or Service Owner (go-live decision)
   Risk Acceptance authority, if residual risk remains (per RMF-001 §9.7)
```

### 9.2 Go-Live Risk Acceptance Packet

A separate packet is produced only if go-live ships with one or more risk acceptances. It is the document the Business Owner and required approvers sign per the canonical authority table.

```
GO-LIVE RISK ACCEPTANCE PACKET - <System Name>     AR-YYYY-NNNN - GLR-001

Each accepted risk:
   - Risk Statement (per [CERG-TMPL-RM-001](../templates/CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md))
   - Linked control(s)
   - Compensating controls in place at go-live
   - Residual score and band
   - Expiration / re-review date
   - Treatment plan that retires the acceptance
   - Approver (per PRC-RM-001 §8)

Aggregate:
   - Combined residual score
   - Top three watch-list items
   - First post-go-live review date (≤ 90 days for Critical / High)
```

### 9.3 Phase 5 SLA

Production Handoff is completed within 3 business days of the Phase 4 technical disposition. The handoff package informs the business or service owner's go-live decision; it is not a CERG approval gate. Go-live with unresolved validated residual risk requires the existing RMF acceptance authority.

### 9.4 Post-Go-Live Watch Period

- Critical / High risk acceptances trigger a post-go-live watch period of ≤ 90 days with a scheduled re-review.
- Detection telemetry is reviewed at 30 days for unexpected behavior tied to the accepted risk.
- Findings from the watch period feed back into the risk register and, where appropriate, the threat model.

---

### 9.5 Dispute and Appeal Process

If a project team disagrees with a finding, disposition, or outcome from any phase of the architecture review, the following appeal path is available.

#### Appeal Triggers

An appeal may be filed for:
- A finding the project team believes is inaccurate, inapplicable, or overstated
- A `Not Ready` technical disposition on a Phase 2 review
- A "Not Ready" disposition on a Phase 4 pre-production review
- A go-live condition the project team believes is unreasonable or infeasible

#### Appeal Process

| **Step** | **Action** | **Timing** |
|---|---|---|
| 1 | Project team submits written appeal to the CERG Pre-Production Reviewer, stating the specific finding or disposition being appealed, the rationale, and any supporting evidence | Within 5 business days of the original decision |
| 2 | CERG Pre-Production Reviewer re-evaluates with the project team; may consult additional subject matter experts | Within 5 business days |
| 3 | If resolved: decision is updated and recorded. If not resolved: escalates to Risk Pillar Leader. | - |
| 4 | Risk Pillar Leader reviews the appeal and the CERG position; makes a determination or escalates to CISO | Within 5 business days |
| 5 | CISO makes the final technical determination, which is binding as the CERG disposition. It settles the technical question and is recorded in the review record; it does not itself authorize or prevent go-live, and any residual risk the owner carries follows `RMF-001` §9.7. | Within 10 business days of escalation |

#### Criteria for Overturning a Decision

A decision may be overturned if:
- New or overlooked evidence demonstrates the finding is inapplicable
- The project team proposes an alternative compensating control that achieves equivalent or superior risk reduction
- The original decision was based on a misinterpretation of a standard or control requirement
- The business impact of the decision is disproportionate to the risk it addresses

#### Documentation

Every appeal is documented in the review record, including: the appealed finding or disposition, the appellant's rationale, the resolution, and the final decision-maker. Appeal outcomes inform program improvement per [CERG-PRC-LL-001](CERG-PRC-LL-001_Lessons_Learned_and_Program_Improvement_Procedure.md).

---

## 10. Required Diagrams

Every Mandatory Review delivers the diagram set below. Diagrams are produced in a tool that exports to durable formats; the latest version lives with the review record.

| **Diagram** | **Required For** | **Shows** |
|---|---|---|
| **Context** | All | The system, its users, and the systems it depends on. One page. |
| **Data Flow** | All | What data moves where, classified; arrows annotated with protocol and trust boundary crossings. |
| **Network** | All non-pure-SaaS | Network paths, segmentation, ingress/egress, public exposure. |
| **Identity** | All | Identity sources, federation, SSO, MFA enforcement points, service accounts and machine identities. |
| **Trust Boundary** | All | Drawn over the data flow / network diagrams: tenant, network, identity, regulatory boundaries. |
| **OT Boundary** | OT or IT/OT bridge | ESP, EAP, BCS, BCSI flows, control room/operator interface. |
| **CUI Boundary** | CUI scope | Where CUI is processed, stored, and transmitted; FedRAMP-equivalent service edge. |
| **Backup / Recovery** | Tier 1/2 and any BES/CUI scope | Backup source, target, immutability boundary, restoration target. |

Where a diagram is implicit (e.g., a pure SaaS service has no on-prem network), the review record notes "Not Applicable" with rationale rather than omitting silently.

---

## 11. Templates

Architecture review uses one standalone intake template and several procedure-owned record patterns. Authority is split as follows:

| **Artifact** | **Authoritative Source** | **Purpose** |
|---|---|---|
| Phase 1 Architecture and Project Intake Form | [`CERG-TMPL-AR-001`](../templates/CERG-TMPL-AR-001_Architecture_and_Project_Intake_Form.md) | Opens the engagement, records scope determination, and routes follow-on records. |
| Phase 2 Architecture Review Record | This procedure §6.4 and worked example Appendix A | Records findings, conditions, and Engineering disposition. |
| Phase 2 Threat Model Record | This procedure §6.2 and [`CERG-PRC-TM-001`](CERG-PRC-TM-001_Threat_Modeling_Procedure.md) | Records threats, assumptions, residual risks, and simulation candidates. |
| Phase 4 Pre-Production Security Review Record | This procedure §8 | Confirms readiness evidence and records Ready / Ready-with-Risk-Acceptance / Not Ready disposition. |
| Phase 5 Production Handoff Package | This procedure §9.1 | Consolidates review records, control posture, evidence pointers, recurring obligations, and sign-offs for the asset record. |
| Go-Live Risk Acceptance Packet | This procedure §9.2 and [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Documents accepted residual risk at go-live when required by the canonical risk authority path. |

A completed [`CERG-TMPL-AR-001`](../templates/CERG-TMPL-AR-001_Architecture_and_Project_Intake_Form.md) is not evidence that Phase 2, Phase 4, or Phase 5 has been completed. It is the intake and routing record that starts the chain.

---

## 12. Metrics

| **KPI** | **Formula** | **Data Source** | **Refresh** | **Green** | **Amber** | **Red** |
|---|---|---|---|---|---|---|
| **Average Time - Phase 1 (Intake)** | Mean business days from intake submission to Scope Determination recorded | Intake tracker | Monthly | ≤ 3 days | 4–5 days | > 5 days |
| **Average Time - Phase 2 (Arch Review)** | Mean business days from Phase 2 start to review record disposition | Review tracker | Monthly | ≤ 7 days | 8–10 days | > 10 days |
| **Average Time - Phase 3 (Build-Time)** | Mean business days per build-time review cycle | Pipeline / review tracker | Monthly | ≤ 2 days | 3 days | > 3 days |
| **Average Time - Phase 4 (Pre-Prod)** | Mean business days from Phase 4 start to disposition (Ready / Ready-with-Risk-Acceptance / Not Ready) | Review tracker | Monthly | ≤ 4 days | 5 days | > 5 days |
| **Average Time - Phase 5 (Handoff)** | Mean business days from Pre-Prod Ready to handoff package signed | Review tracker | Monthly | ≤ 2 days | 3 days | > 3 days |
| **Review Backlog Count** | Number of open reviews past their target disposition date | Review tracker | Weekly | ≤ 2 | 3–5 | > 5 |
| **Finding Severity Distribution** | Count of findings by severity (Critical / High / Medium / Low / Info) recorded across all active reviews | Risk register | Monthly | Baseline to be established in first year of operation | | |
| **Threat Model Coverage Rate** | % of Mandatory Review projects with completed threat model attached to the review record | Review tracker + TM repo | Quarterly | ≥ 95% | 85–94% | < 85% |
| **Handoff Package Completion Rate** | % of projects in Phase 5 with all handoff package sections complete at go-live | Review tracker | Quarterly | ≥ 100% | 90–99% | < 90% |
| **Risk Acceptance Aging** | Mean and maximum age (days) of open risk acceptances raised through the review process | Risk register | Monthly | Mean ≤ 90 days, Max ≤ 180 days | Mean 91–180 days, Max 181–270 days | Mean > 180 days, Max > 270 days |
| **Review SLA Compliance Rate** | % of reviews meeting the SLA for their review path (Mandatory / Lightweight) | Review tracker | Monthly | ≥ 90% | 80–89% | < 80% |

> **Baseline Establishment**
>
> Where a metric is marked "Baseline to be established in first year of operation," the CERG Risk Pillar collects 12 months of data and proposes Green/Amber/Red thresholds at the next annual review. Prior to baseline, the metric is reported without RAG coloring.

---
## 13. Regulatory and Framework Alignment Summary

| **Regulation / Framework** | **Where in This Procedure** |
|---|---|
| [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) PL / SA / SC | All phases |
| NIST 800-160 (Systems Security Engineering) | Phases 2–5 |
| NIST SSDF | Phase 3 |
| NERC-CIP CIP-005 / CIP-010 | Phase 2 OT scope, Phase 4 baseline |
| [CMMC L2](https://dodcio.defense.gov/CMMC/) | CUI scope determination in Phase 1; FIPS check in Phase 2/4 |
| SOX ITGC | SOX scope in Phase 1; change-management interface in Phase 5 |

---

## 14. Pre-Approved Architecture Patterns

Good governance makes projects faster because teams can design correctly before vendor selection. The patterns below are available for a "Light-Touch" technical review if the described conditions are met. Engineering confirms technical conformance; Governance and Risk are not required to engage unless the project exceeds the pattern's boundaries.

| Pattern | Required Controls | Evidence | Expected Review Time | When to Escalate |
|---------|------------------|----------|-------------------|------------------|
| **New SaaS — no sensitive data** | SSO via IdP; OAuth app review; data classification verified as Internal or lower | IdP config, OAuth grant list, data classification record | 1 business day | Data classification changes; CUI/Restricted data discovered; vendor fails SSPM baseline |
| **New SaaS — SSO only** | SSO enforced; no local accounts; OAuth scope review; tenant admin account secured via PAM | IdP config, PAM configuration | 2 business days | SaaS holds sensitive data; provider lacks SOC 2; tenant admin not under PAM |
| **SaaS with Restricted / CUI data** | Full TPRM pipeline per [TPRM-001](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md); FedRAMP equivalency evidence; CUI flow-down; shared responsibility matrix | SSP report, FedRAMP package, contract clauses, SRM | 10 business days | FedRAMP not available; CUI stored outside authorized boundary |
| **Public web app** | WAF; DDoS protection; TLS 1.3; authenticated scan coverage; external pen test before go-live | WAF config, TLS scan, pen test report | 5 business days | App handles authentication; app stores Restricted data; app is customer-facing Tier 1 |
| **Internal API** | mTLS or API gateway auth; rate limiting; input validation; logging to SIEM | API gateway config, SIEM source verification | 3 business days | API is Internet-facing; API handles payments; API accesses crown-jewel data |
| **Vendor remote access** | PAM-brokered only per [STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md); session recording; named accounts; kill-switch tested; no standing access | PAM config, session logs, kill-switch test record | 5 business days | Vendor requires standing access; vendor is OT/ICS; vendor accesses BES Cyber Systems |
| **MSP privileged access** | Full MSP hard requirements per [TPRM-001](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) §6.2: PAM, named accounts, no global admin, customer-owned logs, break-glass, kill-switch | All eight MSP requirement verifications | 10 business days | Any MSP requirement cannot be met; MSP is primary IT operations provider |
| **OT remote maintenance** | First-line service-owner-controlled remote access; session recording; operational approval per maintenance window; CIP-007 alignment | Access log, session record, operational approval | Per maintenance window | Vendor requires always-on connection; BES Cyber System without CIP overlay |
| **AI assistant with internal data** | Data classification verified; AI acceptable use policy acknowledged; prompt injection mitigations; data egress monitored per [STD-AI-001](../standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md) | AI policy acknowledgment, DLP configuration, data classification | 3 business days | AI tool ingests Restricted/CUI data; AI tool is customer-facing; model training on org data |
| **CI/CD integration** | Pipeline access control; secrets management; signed commits; SBOM generation; build-time SCA/SAST | Pipeline config, secret store audit, SBOM, scan results | 3 business days | Integration touches production deployment; integration has external contributors |
| **Cloud workload with Internet ingress** | WAF or cloud-native equivalent; TLS 1.3; DDoS protection; authenticated external scan; CSPM continuous monitoring | WAF config, TLS scan, CSPM posture, external scan report | 5 business days | Workload handles authentication directly; workload is in regulated scope |

**Common exceptions across patterns:**

| Exception | Compensating Control | Review Path |
|-----------|---------------------|-------------|
| SSO not available (legacy SaaS) | IP restriction; session monitoring; quarterly access review | Governance exception workflow |
| PAM not feasible (vendor tool limitation) | Session recording; named accounts; quarterly access review; kill-switch | Risk assessment + CISO approval |
| Pen test cannot be completed pre-launch | Scheduled within 30 days of go-live; compensating monitoring active during gap | Governance exception with expiration |
| WAF bypass required (application compatibility) | Layer-7 monitoring; IPS rule; quarterly pen test of bypass path | Engineering review + Governance exception |

**Governance principle:** Pre-approved patterns reduce review time by eliminating the discovery phase. If a project fits a pattern exactly, Engineering confirms technical conformance and the business or service owner may proceed. If it deviates in any material way, it escalates to the review tier specified by the deviation. Patterns are reviewed annually and updated when standards change.

---

## 15. Document Control

| | |
|---|---|
| **Document ID** | CERG-PRC-AR-001 |
| **Version** | 1.7 |
| **Approved By** | CISO |
| **Next Review** | Annual / on platform or process change |
| **Change Log** | 1.3 - Reconciled technical review, go-live, gate, and first-line operating authority. 1.2 - Clarified standalone intake template authority and procedure-owned closure records. 1.1 - Added Appendix A worked example. 1.0 - Initial publication. Establishes intake, review, threat-model, build-time, pre-prod, and handoff phases with the citizen-development carve-out. |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.7 | 2026-10-30 | Governance Pillar Leader | Patch (#285): repaired 6 table-of-contents anchors whose slugs no longer matched their headings. No content change. |
| 1.6 | 2026-10-30 | Governance Pillar Leader | Authority reconciliation (#280): CISO escalation settles the technical disposition and cannot itself authorize, deny, or compel go-live, which is the accountable owner's decision. Appendix A.7 sign-offs now route the KMS key type acceptance to the Business Owner co-signed per RMF-001 §9.7, matching A.4 and A.6. |
| 1.5 | 2026-10-30 | Engineering Pillar Leader | Reconciled the go-live decision with the canonical RACI. The roles table claimed the Project Sponsor / Business Owner owns the go-live decision unconditionally, while §6.4, §8.3, the §9 sign-off list and OM-001 §9 all say the business or service owner decides, and RAC-001 §6.1 assigns the accountable role to the First-Line Service Owner. The roles table now names the residual-risk ownership only and defers the go-live decision to RAC-001 §6.1. No authority changed; one claim stopped contradicting four others. |
| 1.4 | 2026-10-30 | Engineering Pillar Leader | Named the two disposition sets by phase: §6.4 now defines its three Phase 2 design dispositions beside §8.3's three Phase 4 pre-production dispositions, so one set can no longer be read for the other. §6.4's definitions no longer use "blocking", which §7.3 uses for a severity rating. Corrected the third spelling `Ready-with-Acceptance` in the §12 Phase 4 metric. Moved two example artifacts off reviewer authority and onto `RMF-001` §9.7: finding F04 in the Phase 2 example routes a Medium finding for Business Owner acceptance, co-signed, instead of recording the reviewer accepting it, while the Phase 4 example records the KMS acceptance as completed so its `Ready-with-Risk-Acceptance` disposition is supported by its own evidence row. |
| 1.3 | 2026-10-28 | Engineering Pillar Leader | Reconciled technical review with first-line service operation: CERG review states technical dispositions and escalates; named business or service owners decide go-live; first-line operators enforce gates and make releases; residual risk follows RMF authority. |
| 1.2 | 2026-06-18 | Engineering Pillar Leader | Reconciled TMPL-AR-001 as the Phase 1 front-door intake form and clarified that PRC-AR-001 owns Phase 2-5 review, handoff, and go-live risk records. |
| 1.1 | 2026-06-13 | Engineering Pillar Leader | Added Appendix A worked example. |
| 1.0 | 2026-05-22 | Cyber Governance | Initial publication. Establishes intake, review, threat-model, build-time, pre-prod, and handoff phases with the citizen-development carve-out. |

### Review Triggers

- Change to architecture review intake, routing, or SLC tiers.
- Change to the standalone intake template or procedure-owned review record structure.
- Change to go-live risk acceptance authority.
- Audit, assessment, or tabletop finding related to project review evidence.

### Related Documents

- [`CERG-TMPL-AR-001`](../templates/CERG-TMPL-AR-001_Architecture_and_Project_Intake_Form.md) - Architecture and Project Intake Form
- [`CERG-PRC-TM-001`](CERG-PRC-TM-001_Threat_Modeling_Procedure.md) - Threat Modeling Procedure
- [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) - Risk Register and Exception Process
- [`CERG-PRC-TPRM-001`](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) - Third Party and Supply Chain Risk Procedure

---

## Appendix A. Worked Example: CloudApp Migration

> **Purpose**
>
> This appendix walks a fictitious project — "CloudApp Migration" — through all five phases of the architecture review process. It shows what each artifact looks like when populated, so first-time adopters have a concrete reference.

### A.1 Scenario

**Profile:** Contoso Energy Solutions, a mid-market utility ($1.2B revenue). NERC-CIP Low impact, SOX ITGC scope.

**Project:** Migrate the internal billing application ("CloudApp") from on-premises to AWS. CloudApp processes customer billing data (Internal classification), interfaces with the financial ERP (SOX-scoped), and exposes a REST API to an external collections vendor.

**Team:** 1 Cloud Security Engineer (reviewer), 1 Risk Analyst (threat model), 1 Governance Pillar Leader (SOX overlay), 1 Project Technical Lead, 1 Business Owner (CFO designee).

### A.2 Completed Intake Form (Phase 1)

```
SECURITY PROJECT INTAKE - AR-2026-0001

A. PROJECT IDENTITY
   Project Name             : CloudApp Migration to AWS
   Sponsor (named role)     : CFO Designee (Business Owner)
   Technical Lead           : Sr. Cloud Engineer, IT Operations
   Business Outcome         : Reduce datacenter footprint, enable auto-scaling
   Target Production Date   : 2026-09-30

B. SCOPE
   Data Classifications Handled : Internal (billing records)
   Regulatory Scope             : SOX (via ERP integration)
   Operating Units Impacted     : Finance, IT Operations
   Environments                 : Cloud (AWS)
   Geographies                  : US only
   Trust Boundaries Crossed     : Network (on-prem to cloud), Identity (IdP federation), Organization (vendor API)

C. TECHNOLOGY
   New SaaS introduced?         : Y - Twilio SendGrid (transactional email vendor) - tier assessment needed
   New cloud account/sub/proj?  : Y - new AWS production account
   New OT touch / IT/OT bridge? : N
   New external connection?     : Y - collections vendor API (Tier 2 per TPRM)
   New identity / federation?   : Y - AWS IAM Identity Center federation with Azure AD

D. THIRD PARTIES
   Vendors involved             : AWS, Twilio SendGrid, Collections Vendor (ABC Collect Inc.)
   Vendor tier (per TPRM)       : AWS = Tier 1, SendGrid = Tier 2, ABC Collect = Tier 2
   International access?        : N

E. CHANGE CONTEXT
   New build / migrate / retire / extend : Migrate + Extend (vendor API integration is new)
   Existing CERG-tracked asset IDs       : On-prem billing server (ASSET-00101)

F. INITIAL SECURITY CONCERNS (from project team)
   What worries us most         : SOX evidence continuity during migration; vendor API authentication
   What we know is unresolved   : ERP integration will use a private link; encryption cert renewal timeline

G. ASKS
   What CERG help do we need at design stage? : VPC design review, identity federation pattern, SOX evidence requirements
```

### A.3 Scope Determination Output

| **Field** | **Determination** |
|---|---|
| Review Path | **Mandatory** — new cloud account, external connection, SOX scope |
| Overlay Reviewers | SOX ITGC Lead (ERP integration), Vendor Risk Analyst (SendGrid + ABC Collect) |
| Threat Modeling Required | Yes |
| TPRM Engagement Required | Yes — SendGrid (Tier 2) and ABC Collect (Tier 2) need assessment |
| SLC Tier | Tier 2 (standard urgency, non-regulated project with SOX adjacency) |
| Estimated Effort | Phase 2: 7 business days; Phase 4: 5 business days |

### A.4 Architecture Review Record (Phase 2)

**Technical Disposition:** Ready-with-Conditions

| **Finding ID** | **Area** | **Finding** | **Severity** | **Disposition** |
|---|---|---|---|---|
| AR-2026-0001-F01 | Identity | AWS IAM Role for ERP integration grants full DynamoDB access instead of least-privilege per table | High | Fix before go-live: scope IAM policy to specific DynamoDB tables |
| AR-2026-0001-F02 | Network | VPC flow logs enabled but not shipped to SIEM; retention set to 7 days instead of 365 | High | Fix before go-live: configure VPC flow log delivery to SIEM; set retention to 365 days |
| AR-2026-0001-F03 | Logging | Application logs write to CloudWatch with 14-day retention; no forwarding to central SIEM | Medium | Fix within 30 days of go-live: configure CloudWatch subscription filter to SIEM; extend retention to 1 year |
| AR-2026-0001-F04 | Cryptography | KMS key for RDS encryption uses automatic key rotation but no CMK; key material is AWS-managed | Medium | Route for risk acceptance (Business Owner, co-signed per `RMF-001` §9.7), with condition: document SOX-relevant controls to confirm CMK not required; reassess at SOX evidence cycle |
| AR-2026-0001-F05 | Third Party | SendGrid API key stored in application config file, not secrets manager | High | Fix before go-live: migrate to AWS Secrets Manager with automatic rotation |

**Conditions attached to the Phase 2 disposition:**
- High findings (F01, F02, F05) must be remediated before Phase 4 pre-production review
- Medium findings (F03, F04) must have treatment plan with owner and target date by go-live

### A.5 Threat Model Record (Phase 2)

```
THREAT MODEL - CloudApp Migration               AR-2026-0001 - TM-001

1. ASSETS AND DATA
   - Customer billing records (Internal classification)
   - ERP financial transaction data (SOX-scoped)
   - AWS IAM roles, KMS keys, CloudTrail audit logs

2. ACTORS AND ENTRY POINTS
   - Internal users (Finance team) via Azure AD SSO
   - Collections vendor (ABC Collect) via REST API + API key
   - AWS managed services (RDS, DynamoDB, S3) - provider trust model

3. TRUST BOUNDARIES
   - On-premises Azure AD <-> AWS IAM Identity Center (identity boundary)
   - AWS VPC <-> On-premises ERP via AWS PrivateLink (network boundary)
   - CloudApp API <-> ABC Collect (external organizational boundary)

4. THREATS BY BOUNDARY
   Identity Boundary: [Spoofing] Compromised Azure AD account could assume AWS role
     -> Control: Conditional Access MFA, JIT elevation via PAM
   Network Boundary: [Tampering] Man-in-the-middle on PrivateLink connection
     -> Control: TLS 1.2 minimum, mutual TLS for ERP integration
   External Boundary: [Info Disclosure] ABC Collect API key leak could expose billing data
     -> Control: API key in Secrets Manager, IP whitelisting, rate limiting

5. EXISTING CONTROLS
   - Azure AD MFA for all internal users
   - AWS CloudTrail enabled across all accounts
   - AWS Config rules for baseline drift detection
   - VPCs with default-deny routing, limited egress

6. RESIDUAL RISKS (to risk register)
   - TM-R01: Vendor API compromise could allow data exfiltration [Medium]
   - TM-R02: SOX evidence chain depends on CloudTrail integrity [Low]

7. ATTACK SIMULATION CANDIDATES
   - Purple team: "Assume API key compromised — can attacker pivot to cloud control plane?"
```

### A.6 Pre-Production Security Review (Phase 4)

**Disposition:** Ready-with-Risk-Acceptance

| **Check** | **Result** | **Evidence** |
|---|---|---|
| DISH baseline applied | Pass — AWS account scans at DISH Enhanced tier; no Critical/High deviations | DISH scan AR-2026-0001-001 |
| Exposure posture | 2 Medium findings open (both accepted with risk register entries) | Exposure pipeline report |
| Identity wired | SSO + MFA enforced; AWS IAM Identity Center synced from Azure AD; PAM not required for this asset class | IdP policy export |
| Logging | CloudTrail + VPC Flow Logs + CloudWatch shipped to SIEM; retention 365 days | SIEM source inventory |
| Detection | CloudApp added to detection coverage: GuardDuty + Security Hub + custom CIS rules | Detection coverage report |
| Cryptography | TLS 1.2 minimum on ALB; KMS with automatic key rotation; Secrets Manager for all secrets | TLS scan, KMS key config |
| Resilience | RTO 4h / RPO 1h via multi-AZ RDS; restoration test scheduled for Day +14 post-go-live | Backup config, resilience register |
| Vendor / TPRM | AWS Tier 1 evidence current; SendGrid Tier 2 assessment complete — SOC 2 accepted with CUEC mapping; ABC Collect assessment in progress — conditional acceptance granted with 90-day re-review | TPRM tool entries |
| SOX overlay artifacts | ERP integration controls mapped to ITGC CM-2, CM-3, CM-4; compensating control memo for KMS key type accepted by the Business Owner, co-signed per `RMF-001` §9.7, with SOX ITGC Lead compliance input | SOX control mapping |
| Phase 2 conditions cleared | F01 (IAM scoping) resolved — IAM policy updated; F02 (flow logs) resolved — SIEM delivery confirmed; F05 (Secrets Manager) resolved — SendGrid key migrated; F03 (logging retention) on track for 30-day target | Phase 2 record annotations |
| Asset inventory | CloudApp added as ASSET-00201 (AWS): owner = IT Operations, tier = Production Tier 2, SOX scope = yes | Asset inventory |

### A.7 Production Handoff Summary (Phase 5)

| **Section** | **Status** |
|---|---|
| System Identity | ASSET-00201 — CloudApp (AWS); Tier: Production Tier 2; Owner: IT Operations; Regulatory: SOX |
| Review Records | Intake AR-2026-0001, Architecture Review AR-2026-0001-F01–F05, Threat Model TM-001, Pre-Production Record PP-2026-0001 |
| Control Posture | 30 controls Implemented, 2 Partial (logging retention, vendor assessment), 1 Risk Accepted (KMS key type) |
| Evidence Pointers | DISH scan, SIEM source list, Secrets Manager audit, Backup config, CloudTrail integrity verification |
| Risk Acceptances | RA-2026-0001 (KMS key type — expiration 2027-06-30); RA-2026-0002 (SendGrid assessment conditional — re-review 2026-12-31) |
| Ongoing Controls | Weekly exposure scan, monthly access review, quarterly SOX control evidence refresh, annual pen test |
| Run-book | Confluence link: RUN-CloudApp-001; On-call: IT Ops rotation via PagerDuty |
| Sign-offs | Engineering Reviewer: Cloud Security Engineer; Risk Reviewer: Risk Analyst; Governance (SOX): SOX ITGC Lead; Engineering Pillar Leader; CISO (co-sign per `RMF-001` §9.7); Business Owner: CFO Designee (KMS key type acceptance) |

### A.8 Key Takeaways for First-Time Adopters

1. **Start early.** The intake form surfaced the SOX evidence concern on day one, which gave Governance time to map controls before go-live.
2. **Threat modeling changed the design.** The vendor API risk (TM-R01) prompted adding IP whitelisting and rate limiting that were not in the original architecture.
3. **Pre-approved patterns reduce Phase 2 time.** The AWS VPC landing-zone pattern was pre-approved; the team skipped the VPC design review and focused on application-layer controls.
4. **Risk acceptance is not failure.** The KMS key type acceptance was a deliberate decision after documented analysis — SOX auditibility was preserved via compensating controls.
5. **Evidence continuity from day one.** CloudTrail was configured before the first workload deployment, ensuring no gap in SOX evidence during migration.
