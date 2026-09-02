## The CERG Framework

### A Scalable, Adaptive Cybersecurity Operating Model

> Designed for Adaptive [NIST CSF 2.0](https://www.nist.gov/cyberframework) maturity. Applicable to IT and OT environments. Calibrated for [CMMC](https://dodcio.defense.gov/CMMC/), NERC-CIP, and [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204).
> 
> _Examples in this document reference a large enterprise at the upper bound of what CERG is designed to support — the framework is scaled to fit organizations from 5 people to large regulated entities. Readers should scale down to their environment. Sector-specific illustrative profiles are available in [`/examples/`](../examples/). See also [`CERG-GOV-VAR-001`](CERG-GOV-VAR-001_Organization_Adaptation_Profile.md) for mechanical adaptation._

---

| | |
|---|---|
| **Document ID** | CERG-GOV-FRM-001 |
| **Version** | 1.23 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | CISO |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on material change to framework |
| **Frameworks** | NIST CSF 2.0; NIST 800-53r5; NIST 800-171r3; NIST RMF |
| **Regulations** | NERC-CIP; CMMC L2; SOX ITGC |
| **Environments** | All in-scope environments |
---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [The CERG Operating Model](#2-the-cerg-operating-model)
3. [Capability Taxonomy: What CERG Builds](#3-capability-taxonomy-what-cerg-builds)
4. [Cyber Engineering](#4-cyber-engineering)
5. [Cyber Risk](#5-cyber-risk)
6. [Cyber Governance](#6-cyber-governance)
7. [Targeting NIST CSF Adaptive Maturity](#7-targeting-nist-csf-20-adaptive-maturity)
8. [Regulatory Alignment](#8-regulatory-alignment)
9. [IT/OT Considerations](#9-itot-considerations)
10. [Team Structure and Talent Model](#10-team-structure-and-talent-model)
11. [Getting Started, The Path to Adaptive](#11-getting-started-the-path-to-adaptive)
12. [Compliance as Exhaust — Evidence Factories](#12-compliance-as-exhaust-evidence-factories)
13. [Document Control](#13-document-control)

---

## 1. Executive Summary

Cybersecurity teams of all sizes have struggled with the same structural problem for two decades: fragmented tools, siloed teams, and a culture of "no" that slows the business without meaningfully reducing risk. The CERG framework, Cyber Engineering, Risk, and Governance, is a deliberate answer to that problem.

CERG consolidates the core work of a mature cybersecurity function into three tightly coupled, clearly bounded pillars. It is not a support-function label or a document set; it is an operating model that helps the business move confidently while security work stays owned, evidenced, and repeatable.

### Why Three Pillars

Most cybersecurity work, outside of Security Awareness and Incident Response, falls naturally into one of three activities:

- **Building and deploying secure technology** alongside the business
- **Assessing exposure and managing risk** continuously
- **Setting standards, assuring conformance, and tracking improvement**

The CERG model names these activities explicitly, Engineering, Risk, and Governance, and assigns clear ownership, accountabilities, and interaction patterns so that work flows between them without dropping and without creating new silos.

### Design Principles

- **Scale up or down:** applicable to small teams, mature enterprise functions, and regulated organizations
- **Regulatory-ready:** designed to satisfy CMMC, NERC-CIP, NIST CSF 2.0, 800-53, 800-171, and SOX
- **IT/OT aware:** principles apply equally to enterprise IT and operational technology environments
- **Talent resilient:** cross-pillar knowledge sharing means no single person is a point of failure
- **Adaptive-targeted:** the framework describes what operating at NIST CSF 2.0 Adaptive maturity looks like in practice
- **"Yes, and..." oriented:** Governance enables the business through risk treatment, not reflexive refusal
- **Definition of Done:** A CERG task is not done when a meeting happened, a document was approved, a ticket moved columns, a scanner showed fewer highs, or someone said "accepted risk." A CERG task is done when all of the following are true: (1) an owner is named, (2) a decision is recorded, (3) evidence is linked and independently verifiable, (4) residual risk is understood and documented, (5) the control state or register entry is updated, (6) a next review date exists, and (7) the system of record agrees with the operational reality. This standard applies to every CERG-managed workflow, finding, exception, risk acceptance, architecture review, and metric. If the Definition of Done cannot be satisfied because the organization lacks the tooling or discipline, CERG adoption is not complete.

---

## 2. The CERG Operating Model

### 2.1 The Full Cybersecurity Team

CERG operates as one of three functional groups within the Cybersecurity department, all reporting to the Chief Information Security Officer (CISO). The full structure is:

|Function|Teams / Scope|
|---|---|
|**CERG**|Engineering · Risk · Governance|
|**Security Awareness**|Training programs · Phishing simulations · Culture campaigns|
|**Incident Response**|SOC / detection · Threat hunting · IR planning & execution|
|**CISO**|Strategy & vision · Executive & board reporting · Budget & resource authority|

> **CERG Scope Note:** This framework focuses on the CERG pillars. Security Awareness and Incident Response are adjacent, equally critical functions with distinct operating models. CERG coordinates closely with both, Engineering embeds security requirements that IR and Awareness depend on; Risk produces threat intelligence that feeds both; Governance sets the standards all three operate under.

### 2.2 The Three Pillars at a Glance

---

#### 🔧 E: Cyber Engineering

**Build securely. Deploy confidently. Consult continuously.**

Internal security consultants who partner with IT and business leaders to design, build, and deploy secure technology across the enterprise, in both IT and OT environments.

---

#### 🔍 R: Cyber Risk

**Know your exposure. Manage it deliberately. Never be surprised.**

Continuous assessment and management of the organization's exposure through exposure management, adversarial validation, vendor risk assessment, and threat intelligence.

---

#### 📋 G: Cyber Governance

**Set the rules. Track the work. Enable the business to move with confidence.**

The second-line authority for policies, standards, control assurance, evidence quality, decisions, and program improvement.

---

### 2.3 How the Pillars Interact

CERG pillars are not sequential. They operate simultaneously and continuously, with structured handoffs and shared accountability for outcomes.

|Lifecycle Stage|Primary Pillar|Supporting Pillars|
|---|---|---|
|Business requirement / new project|Engineering|Governance sets standards; Risk flags vendor/solution concerns|
|Design and architecture review|Engineering|Risk performs threat modeling and vendor assessment|
|Pre-production vulnerability scan|Risk|Engineering remediates findings pre-launch|
|Risk acceptance (if vuln unresolvable)|Engineering + Risk|Governance provides risk treatment plan template; CISO/leadership signs off on High/Critical|
|Production deployment|Engineering|Governance and Risk assume post-production monitoring|
|Ongoing standards conformance assurance|Governance|Risk validates exposure and control weakness; Engineering and accountable owners remediate gaps|
|Evidence assurance and audit readiness|Governance|First-line owners, Engineering, and Risk produce artifacts from their daily work|
|Adversarial validation: pen test / red team / purple team|Risk|Engineering reviews findings for architectural impact; Governance logs findings|
|Regulatory exam or audit|Governance|All pillars provide evidence; Engineering and Risk support responses|

---

## 3. Capability Taxonomy: What CERG Builds

CERG is capability-centered. A **control** is something an organization has: a requirement, configuration, approval, or safeguard. A **capability** is something the organization can reliably **do** under real conditions. Tools, standards, and controls matter because they support capability; they are not the capability by themselves.

This taxonomy gives leaders and practitioners a way to ask better questions:

- Can we design secure systems before they go live?
- Can we find and treat exposure before it becomes an incident?
- Can we prove control operation without an audit scramble?
- Can we sustain operations during a cyber event?

### 3.1 Capability Model

Every CERG capability follows the same evidence chain:

**Capability → Owner → Controls and standards → Procedure → Evidence → Validation method**

- **Capability** declares what the program can do.
- **Owner** names the accountable pillar or adjacent function.
- **Controls and standards** define the security bar.
- **Procedure** defines how the work is executed.
- **Evidence** proves the capability operated.
- **Validation method** shows the capability works under expected conditions.

This model keeps CERG from becoming a document library or tool inventory. If a capability cannot produce evidence and survive validation, it is not mature yet, even if supporting documents exist.

### 3.2 Core Capability Reference Set

The following reference set establishes the capability naming pattern. Capability IDs use `CAP-{PILLAR}-{DOMAIN}-{SEQ}`. The list is not a separate control framework; it is the operating-outcome view of CERG's existing controls, standards, procedures, and records.

| ID | Capability | Primary Owner | Anchors | Evidence | Validation Method |
|---|---|---|---|---|---|
| CAP-ENG-SECIN-001 | Secure systems are reviewed before production go-live. | Cyber Engineering | [PRC-AR-001](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md), [PRC-TM-001](../procedures/CERG-PRC-TM-001_Threat_Modeling_Procedure.md), [CB-001](CERG-GOV-CB-001_Unified_Control_Baseline.md) SA controls | Architecture review record, threat model record, pre-production checklist, risk acceptance package when needed | Quarterly sample of project records and go-live decisions |
| CAP-ENG-CONFIG-001 | Approved configuration baselines are implemented and drift is detected. | Cyber Engineering | [STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md), [STD-AM-001](../standards/CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md), [PRC-CHG-001](../procedures/CERG-PRC-CHG-001_Security_Change_Management_Procedure.md) | Baseline record, asset coverage report, drift finding, change record | Automated configuration scan and quarterly drift review |
| CAP-ENG-RES-001 | Critical systems can be restored within defined recovery expectations. | Cyber Engineering + IR / BCDR | [STD-RES-001](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md), [PLN-BC-001](../plans/CERG-PLN-BC-001_Business_Continuity_and_Disaster_Recovery_Plan.md), [PLN-IR-001](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md) | Backup evidence, restore test record, DR exercise package, recovery gap report | Restore test and DR exercise cadence by recovery tier |
| CAP-RSK-EXP-001 | Critical and High exposure is triaged, treated, or accepted within defined SLAs. | Cyber Risk | [PRC-VM-001](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md), [GOV-RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework.md), [PRC-RM-001](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Finding record, SLA report, treatment plan, risk acceptance or exception record | Monthly SLA review and quarterly risk-register sample |
| CAP-RSK-ADV-001 | Controls are validated under adversary-like conditions. | Cyber Risk | [PRC-AV-001](../procedures/CERG-PRC-AV-001_Adversarial_Validation_Procedure.md), [STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md), [GOV-CB-001](CERG-GOV-CB-001_Unified_Control_Baseline.md) CA-8 | Rules of engagement, engagement report, detection validation results, retest evidence | Annual adversarial validation plan with pen test, red-team, purple-team, cloud, application, or OT-safe activities as in scope |
| CAP-RSK-DET-001 | Required telemetry and detections cover priority attack paths. | Cyber Risk + Incident Response | [STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md), [PRC-TI-001](../procedures/CERG-PRC-TI-001_Threat_Intelligence_Procedure.md), [PRC-AV-001](../procedures/CERG-PRC-AV-001_Adversarial_Validation_Procedure.md) | Detection coverage record, source inventory, tuning record, ATT&CK coverage gap | Purple-team validation or automated adversary emulation |
| CAP-RSK-TPRM-001 | Third-party and supply-chain risk is tiered, evidenced, and tracked. | Cyber Risk | [PRC-TPRM-001](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md), [GOV-EDG-001](CERG-GOV-EDG-001_Edge_Register.md), [CB-001](CERG-GOV-CB-001_Unified_Control_Baseline.md) SR controls | Vendor assessment record, tiering record, contract clauses, shared-responsibility matrix | Vendor sample review and critical-vendor refresh cadence |
| CAP-GOV-RISK-001 | Risk decisions are recorded with owners, treatment, authority, and review dates. | Cyber Governance | [GOV-RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework.md), [PRC-RM-001](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md), [TMPL-RM-001](../templates/CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md) | Risk record, acceptance memo, exception record, review history | Monthly register review and overdue-risk escalation |
| CAP-GOV-EVID-001 | Control evidence is complete, organized, attributable, and retrievable. | Cyber Governance | [PRC-AUD-001](../procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md), [GOV-AUD-001](CERG-GOV-AUD-001_Evidence_Quality_Standard.md), [GOV-CAT-002](CERG-GOV-CAT-002_Record_Catalog.md) | Evidence index, evidence quality score, retrieval log, audit request package | Unannounced evidence spot-check by control family |
| CAP-GOV-REG-001 | Regulated scopes are mapped once and operated through normal CERG workflows. | Cyber Governance | [PLN-CIP-001](../plans/CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md), [PLN-CUI-001](../plans/CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md), [PLN-SOX-001](../plans/CERG-PLN-SOX-001_SOX_ITGC_Operational_Package.md), [GOV-CMX-001](CERG-GOV-CMX-001_Compliance_Matrix.md) | Scope record, control mapping, evidence calendar, POA&M or deviation record | Regulatory calendar review and evidence-package sample |
| CAP-XPN-IR-READY-001 | CERG can support incident response with asset, exposure, evidence, and recovery context. | Cross-pillar + standing IR team | [PLN-IR-001](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md), [PRC-IR-002](../procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md), [PRC-LL-001](../procedures/CERG-PRC-LL-001_Lessons_Learned_and_Program_Improvement_Procedure.md) | Incident action log, asset context package, exposure summary, lessons-learned record | Tabletop or functional exercise with CERG liaison participation |

### 3.3 Capability Maturity Grading

Capability maturity is scored by evidence and validation, not by whether a document exists.

| Level | Label | Operational Meaning |
|---|---|---|
| 1 | **Absent** | No documented capability, named owner, evidence chain, or test. Work is ad hoc or absent. |
| 2 | **Ad Hoc** | Practice exists but varies by person or team. Evidence is partial, inconsistent, or not independently verifiable. |
| 3 | **Defined** | Capability is documented, owned, and produces named evidence. It has been tested or sampled at least once in the past 12 months. |
| 4 | **Repeatable** | Capability operates consistently across its intended scope. Evidence is complete, retrievable, and reviewed on a defined cadence. Findings drive tracked improvement. |
| 5 | **Adaptive** | Capability improves from threat intelligence, incidents, exercises, adversarial validation, and operational metrics. Automation or continuous validation reduces manual effort. |

The scoring rule is simple: the capability maturity level is capped by the weakest link in the evidence chain. A strong tool with no owner is not mature. A documented process with no evidence is not mature. A control that works once but is never retested is not adaptive.

### 3.4 Using Capabilities for Planning

Capability taxonomy gives CERG adopters a practical planning language:

- **For leaders:** fund the capability gap, not just the product request.
- **For small teams:** decide which capabilities must be live now and which are explicitly deferred.
- **For engineering partners:** explain security asks as outcomes, not bureaucracy.
- **For auditors:** show how evidence is produced by normal operations.
- **For hiring:** add people only when the capability cannot be made repeatable through clearer ownership, procedure, automation, or scope reduction.

A tool can support a capability. A document can define a capability. A person can own a capability. But the capability exists only when the organization can perform the work, produce evidence, and improve from what it learns.

---

## 4. Cyber Engineering

> **Mission:** Build securely. Deploy confidently. Consult continuously.

### 4.1 Mission

The Cyber Engineering team serves as the organization's internal security consulting practice. Engineers are assigned to enterprise and IT projects, often as the first security touch point in a project lifecycle, and carry security requirements, design review, and implementation guidance from concept through production handoff.

Engineers do not own the systems they help build. Their role is to ensure that security is designed in from the beginning, that pre-production findings are remediated or risk-accepted before go-live, and that the receiving operations team understands the security posture of what they are taking on.

### 4.2 Core Functions

- **Project intake and early engagement**: review of business requirements, solution architecture documents, and procurement specifications
- **Security architecture consultation**: participating in design reviews, advising on control selection aligned to [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) and organizational standards
- **Pre-production security review**: working with the Risk team to understand vulnerability scan findings and driving remediation with project teams before go-live
- **Risk treatment support**: assisting project teams in drafting risk acceptance documentation and treatment plans when a vulnerability cannot be remediated prior to launch
- **OT/IT convergence advisory**: guiding teams through the security implications of connecting or modernizing operational technology environments
- **Production handoff**: ensuring Governance and Risk have the configuration baseline, asset documentation, and control evidence needed to assume post-production oversight

### 4.3 Engagement Model

Engineering operates on a lightweight internal consulting model. The goal is to minimize administrative overhead and maximize time on engineering work.

|Element|Description|
|---|---|
|Intake|Engineers are engaged via a lightweight request - a brief summary of the project, timeline, and primary contact. No complex ticketing or lengthy intake forms.|
|Assignment|Each engagement is assigned a lead engineer. On large projects, multiple engineers may be assigned. Engineers manage their own capacity with CISO visibility.|
|Engagement scope|Engineers work alongside project teams, not above them. They advise, review, and recommend - the project team retains implementation accountability.|
|Pre-production gate|Before any system or tool goes live, Engineering confirms that open vulnerabilities have been remediated or formally risk-accepted. This is a lightweight confirmation, not a gate that stops work.|
|Handoff documentation|At production cutover, Engineering produces or confirms existence of: asset registration, configuration baseline, control mapping, and any open risk items.|
|Post-production|Once a system is in production, Engineering moves to the next project. Risk and Governance assume ongoing oversight. Engineering may be re-engaged for significant changes.|

### 4.4 Illustrative Example: Electrical Utility

> **Scenario: IT/OT Network Modernization**
> 
> The utility's operations team wants to add remote monitoring capability to its substation SCADA systems. An Engineering team member is engaged at the business requirements stage. They review the vendor's solution architecture, flag the absence of encrypted communications between the historian and the enterprise DMZ, and work with the project team to require TLS enforcement before go-live. The Risk team performs a pre-production scan and finds an unpatched firmware version. Engineering works with the vendor on a patch timeline. When the patch cannot be applied before the project deadline, Engineering helps draft a risk treatment plan with compensating controls, network segmentation, enhanced logging, that Governance reviews for NERC-CIP CIP-005 conformance. VP and CISO sign off. The system goes live with a 90-day remediation commitment documented.

### 4.5 NIST Framework Alignment: Engineering

|NIST Framework|Relevant Controls / Functions|Engineering Role|
|---|---|---|
|NIST CSF 2.0|GOVERN, IDENTIFY (Asset Mgmt, Risk Assessment), PROTECT (Identity Mgmt, Data Security, Platform Security)|Primary driver of PROTECT function; co-owner of IDENTIFY|
|NIST 800-53|SA (System & Services Acquisition), CM (Configuration Mgmt), SI (System & Info Integrity)|Implements SA and CM controls during project delivery|
|NIST 800-171|3.13 System & Communications Protection, 3.14 System & Info Integrity|Ensures CUI protection controls are designed into systems handling federal data|
|NIST RMF|Steps 2 (Select), 3 (Implement), 4 (Assess - pre-production)|Leads control selection and implementation; supports pre-production assessment|
|NERC-CIP|CIP-005 (Electronic Security Perimeters), CIP-007 (Systems Security Mgmt), CIP-010 (Config Mgmt)|Designs systems to conform to CIP requirements from the start|
|CMMC|Level 2: Access Control, Configuration Mgmt, Identification & Auth|Ensures CMMC practices are implemented in applicable systems|

---

## 5. Cyber Risk

> **Mission:** Know your exposure. Manage it deliberately. Never be surprised.

### 5.1 Mission

The Cyber Risk team is responsible for understanding the organization's threat landscape and exposure at all times. Risk does not wait for problems to surface, it hunts for them. Through continuous exposure management, adversarial validation, vendor risk assessment, and threat intelligence, Risk produces the clearest possible picture of what is threatening the organization and how severe those threats are.

Risk serves both a pre-production function (finding issues before systems go live) and a post-production function (tracking drift, emerging CVEs, and changes in the threat environment after systems are in operation).

### 5.2 Core Functions

- **Exposure Management**: continuous scanning of IT and OT environments; prioritization of findings by criticality, exploitability, and asset value; tracking remediation to closure
- **Adversarial Validation**: authorized testing of controls under adversary-like conditions, including penetration testing, red-team operations, purple-team detection validation, cloud attack simulation, and OT-safe assessment where in scope; findings fed back to Engineering and Governance
- **Threat Intelligence**: monitoring of threat actor activity, emerging CVEs, and sector-specific intelligence (including ICS/SCADA threats for OT environments); distribution of actionable intelligence to Engineering, IR, and Governance
- **Vendor and Third-Party Risk**: security review of vendor contracts, SaaS solutions, and third-party integrations; contract redline support for security requirements
- **Pre-Production Assessment**: vulnerability scanning and risk analysis of systems prior to go-live; classification of findings by severity; coordination with Engineering on remediation
- **Risk Treatment and Acceptance**: for findings that cannot be immediately remediated, Risk co-develops treatment plans with Engineering and provides analysis to support leadership sign-off decisions

### 5.3 Pre-Production vs. Post-Production Risk

> **An Important Distinction**
> 
> A vulnerability found in a pre-production system is not a realized risk, the system is not yet live and has not been exposed. The Risk team treats pre-production findings as engineering inputs, working with the Engineering team to drive remediation before launch. Post-production findings are realized risks to be managed, tracked, and reported. This distinction shapes how findings are communicated, prioritized, and escalated.

|Finding Type|Handling|
|---|---|
|Pre-production, Low/Medium severity|Engineering remediates with project team before go-live. Tracked to closure by Risk.|
|Pre-production, High/Critical severity|Engineering and Risk jointly assess. If unremediated, a risk treatment plan is required with VP+ sign-off before go-live.|
|Post-production, Low/Medium severity|Tracked in vulnerability register. Assigned to the appropriate owner (IT/OT operations) with an SLA. Governance assures conformance to the treatment process and escalates overdue items.|
|Post-production, High/Critical severity|Escalated immediately. CISO notified. Risk treatment plan required. Engineering may be re-engaged for architectural remediation. NERC-CIP and CMMC deviation processes invoked as applicable.|
|Vendor/Third-party finding|Risk documents and includes in vendor risk register. Governance tracks contractual remediation commitments. Engineering consulted if architectural change is needed.|

### 5.4 Illustrative Example: Electrical Utility

> **Scenario: NERC-CIP Vulnerability in a BES Cyber System**
> 
> During monthly vulnerability scanning, the Risk team identifies that a critical relay management workstation, classified as a BES Cyber System under NERC-CIP CIP-002, is running an operating system version with a known critical vulnerability (CVSS 9.1). The asset cannot be patched within the standard 35-day window due to vendor testing requirements. Risk identifies a potential CIP-007-6 deviation and validates the residual exposure. The system owner documents the deviation and treatment plan; Engineering adds network monitoring as a compensating control. Governance assures that the exception path, evidence, approval, and escalation requirements are met. The CISO and VP of Operations sign the deviation. Risk tracks the patch to closure within the extended timeline and validates the compensating-control evidence.

### 5.5 NIST Framework Alignment: Risk

|NIST Framework|Relevant Controls / Functions|Risk Team Role|
|---|---|---|
|NIST CSF 2.0|GOVERN (Risk Strategy), IDENTIFY (Risk Assessment, Improvement), DETECT (Adverse Event Analysis)|Primary driver of IDENTIFY and DETECT; co-owner of GOVERN risk functions|
|NIST 800-53|RA (Risk Assessment), CA (Assessment & Authorization), PM (Program Mgmt), SI-2 (Flaw Remediation)|Executes RA and CA controls; owns SI-2 for patch and vuln tracking|
|NIST 800-171|3.11 Risk Assessment|Performs periodic assessments of CUI-handling environments|
|NIST RMF|Step 4 (Assess), Step 6 (Monitor)|Primary executor of continuous monitoring; supports periodic assessments|
|NERC-CIP|CIP-007 (Patch Mgmt), CIP-010 (Vuln Assessments), CIP-011 (Info Protection)|Manages CIP-007 patch tracking; conducts CIP-010 annual vuln assessments|
|CMMC|Level 2: Risk Assessment (RA), Audit & Accountability (AU)|Performs CMMC risk assessments; supports audit log review program|

---

## 6. Cyber Governance

> **Mission:** Set the rules. Track the work. Enable the business to move with confidence.

### 6.1 Mission

Cyber Governance is CERG's second-line authority. Governance defines the cybersecurity rules, standards, control outcomes, evidence expectations, and decision paths that let the business operate safely. It assesses conformance, challenges weak or missing evidence, directs accountable owners to correct deficiencies, and improves the system when assurance shows that a guardrail is not working.

Governance operates from a **"yes, and..."** philosophy. The goal is never to block the business but to ensure that when the business accepts risk, that risk is documented, owned, and managed. Governance provides the framework within which Engineering and Risk do their best work.

### 6.2 Core Functions

- **Policy, Standards, and Control Intent**: creating, maintaining, and retiring the cybersecurity rules and control outcomes that define what good looks like
- **Guardrail and Implementation Guidance**: translating required outcomes into practical patterns and guidance that Engineering and first-line teams can implement across IT and OT
- **Standards Conformance and Control Assurance**: assessing whether controls operate to the required standard, challenging gaps, and directing accountable owners to correct deficiencies
- **Evidence Architecture and Quality**: defining what acceptable evidence looks like; assuring that evidence is attributable, current, retrievable, and fit for decisions or external scrutiny
- **Decision, Exception, and Treatment Governance**: maintaining the risk-register process, exception paths, decision records, and escalation of overdue or deteriorating treatment
- **Deficiency, Corrective-Action, and Program Improvement Oversight**: tracking recurring weaknesses through remediation and improving standards, procedures, controls, metrics, or capability when assurance identifies a systemic gap

Applicable regulatory obligations are mapped into CERG standards, controls, and overlays. Regulatory alignment is evidence that the operating model works; it is not a separate workstream or a substitute for control assurance.

### 6.3 The "Yes, And..." Standard

Governance reserves the right to say no, particularly for significant NERC-CIP deviations or CMMC non-conformances where regulatory exposure is material. But the default orientation is enabling the business with guardrails, not closing doors. CERG publishes and reports against its own service-level commitments ([`CERG-GOV-SLC-001`](CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md)), so that a fast, safe yes is a measured obligation: a slow yes is a no the business routes around.

|Situation|"Yes, And..." Response|
|---|---|
|Project team cannot patch within standard SLA|Yes, you can extend the patching window - and we need a risk treatment plan, documentation of affected systems, compensating controls, and VP sign-off within 5 business days.|
|New SaaS tool handles CUI but lacks FedRAMP authorization|Yes, you can evaluate this vendor - and Risk needs to complete a vendor security assessment before procurement, and we'll need contractual security requirements in the agreement.|
|OT team needs remote access to SCADA during maintenance window|Yes, remote access is possible - and it must route through the approved jump server, use MFA, be logged, and the session record retained per CIP-007.|
|Business unit wants to skip architecture review to meet deadline|Yes, we can compress the review timeline - and Engineering must complete at minimum a 2-hour express review, and any open items become tracked exceptions with a remediation commitment.|
|NERC-CIP deviation required for emergency maintenance|Yes, the deviation can proceed - and we'll invoke the CIP deviation process: document the circumstances, notify as required, implement compensating measures, and close the deviation within the regulatory window.|

### 6.4 Evidence Standards

Governance sets the evidence standard: acceptable proof that a control is designed, implemented, operating, and validated for its required scope. Evidence is created as work happens, by the people who perform or validate that work:

- **First-line system and business owners produce:** operational records, owner attestations, implementation decisions, and remediation evidence for systems they operate
- **Engineering produces:** architecture review documentation, pre-production checklists, configuration baselines, guardrail implementation records, and technical handoff evidence
- **Risk produces:** vulnerability scan reports, penetration test findings, threat intelligence assessments, vendor risk assessments, and exposure-validation records
- **Governance produces:** policies, standards, control and evidence criteria, decision records, exception approvals, assurance results, and improvement records

Governance assures the evidence library rather than performing every collection activity. It tests whether evidence is organized, dated, attributable, retrievable, and retained for the required period; accountable owners correct evidence gaps or control deficiencies.

### 6.5 Illustrative Example: Electrical Utility

> **Scenario: CMMC Level 2 Assessment Preparation**
> 
> The utility has a contract with the Department of Energy that requires CMMC Level 2 compliance. Governance maps the 110 NIST 800-171 practices to the organization's existing standards, controls, and evidence criteria, identifying 14 gaps. Accountable system owners and Engineering remediate 9 gaps through technical implementation; Governance updates three policy and procedure requirements; Risk performs additional scanning and validates compensating controls for two gaps. Governance assures the evidence package by testing the records produced through normal work: architecture reviews from Engineering, vulnerability reports from Risk, owner attestations, and policy records. When the C3PAO assessment team arrives, the organization can answer from that operating evidence and Governance tracks resulting deficiencies to closure.

### 6.6 NIST Framework Alignment: Governance

|NIST Framework|Relevant Controls / Functions|Governance Role|
|---|---|---|
|NIST CSF 2.0|GOVERN (all functions), IDENTIFY (Improvement), RESPOND (Improvements)|Primary owner of the GOVERN function across all six sub-functions|
|NIST 800-53|PL (Planning), PM (Program Mgmt), CA (Assessment), PS (Personnel Security)|Owns PL and PM control families; coordinates CA; sets PS standards|
|NIST 800-171|3.12 Security Assessment, all documentation requirements|Ensures the standards, control, and evidence model supports assessment readiness|
|NIST RMF|Step 1 (Categorize), Step 2 (Select - policy), Step 5 (Authorize), Step 6 (Monitor - assurance)|Leads categorization; co-leads authorization; owns standards conformance assurance|
|NERC-CIP|CIP-003 (Security Mgmt Controls), CIP-004 (Personnel Training), CIP-014 (Physical Security Policy)|Maintains CIP policy mapping and assurance criteria; accountable owners operate controls and provide evidence|
|CMMC|All documentation and evidence requirements across all domains|Maps requirements to normal controls and evidence; assures assessment readiness from operating records|
|SOX ITGC|IT General Controls documentation, change management evidence|Maintains control and evidence criteria; assures readiness from operational records|

---

## 7. Targeting NIST CSF 2.0 Adaptive Maturity

### 7.1 What Adaptive Means

The NIST Cybersecurity Framework defines four tiers of organizational maturity: Partial, Informed, Repeatable, and Adaptive. Most organizations operating a mature security program reach Repeatable, processes are defined, practiced, and reviewed. Adaptive goes further.

At the Adaptive tier, an organization does not just respond to the threat environment, it anticipates it. Risk management is integrated into the fabric of business decision-making. Cybersecurity considerations are part of every significant investment, acquisition, and operational change. The security function continuously learns from internal events and external intelligence, and updates its practices accordingly.

|CSF Tier|What It Looks Like in Practice|
|---|---|
|**Partial (Tier 1)**|Ad hoc processes. Risk decisions made reactively. Limited awareness of threats. No consistent policy or evidence collection.|
|**Informed (Tier 2)**|Policies exist but are not consistently applied. Risk management happens in silos. Some awareness of threat environment. Inconsistent evidence.|
|**Repeatable (Tier 3)**|Defined, documented, and practiced processes. Risk management is consistent. An assurance calendar exists. Evidence is created systematically through normal work. Teams understand their roles.|
|**Adaptive (Tier 4)**|Cybersecurity is integrated into organizational decision-making. Threat intelligence actively shapes priorities. Lessons learned drive continuous improvement. Risk appetite is clearly defined and applied. The business views security as a value driver, not a cost center.|

### 7.2 How CERG Produces Adaptive Behavior

The CERG model is designed to produce Adaptive-tier behavior through its structure, not just its aspirations.

|Adaptive Criterion|CERG Mechanism|Pillar(s)|
|---|---|---|
|Risk management is integrated into business decisions|Engineering engages at the business requirements stage - before designs are set or budgets committed. Security cost is a design input, not an afterthought.|Engineering|
|Threat intelligence informs priorities|Risk maintains a live threat intelligence function including ICS/OT-specific sources. Intelligence is distributed to Engineering (design decisions), IR (detection), and Governance (policy updates).|Risk|
|Lessons learned drive improvement|Post-incident reviews, adversarial-validation retrospectives, and audit findings are assessed as lessons. Specific risks remain in the risk register; systemic program improvements are tracked in IMPREG-001.|Governance, Risk|
|Risk appetite is defined and applied consistently|Governance maintains a documented risk appetite and tolerance framework. The "yes, and..." model applies this consistently across all risk treatment decisions.|Governance|
|Continuous improvement of the security program|Governance conducts periodic QA reviews of Engineering and Risk outputs. The CISO reviews CERG performance metrics quarterly.|Governance, All|
|Cybersecurity is viewed as a value driver|Engineering's consulting model and "yes, and..." Governance orientation build organizational trust. The business experiences security as an enabler, not an obstacle.|All|
|Cross-pillar knowledge transfer prevents single points of failure|CERG roles are designed with deliberate left-right knowledge sharing. Engineers learn Risk thinking; Risk analysts understand Governance requirements; Governance understands operational constraints.|All|

### 7.3 CSF Core Function Coverage

The NIST CSF 2.0 Core consists of six functions. CERG provides primary or strong supporting ownership for all six.

|CSF Function|Primary Owner|CERG Coverage|
|---|---|---|
|**GOVERN**|Governance|Governance owns cybersecurity tolerance, policy, standards, and accountability structures. Risk contributes exposure and validation data. Engineering enables first-line teams to implement the required guardrails.|
|**IDENTIFY**|Risk + Engineering|Risk owns asset, risk, and improvement identification. Engineering contributes asset documentation through project handoffs.|
|**PROTECT**|Engineering|Engineering designs and implements protective controls. Governance sets the standard. Risk validates effectiveness through vuln management.|
|**DETECT**|Risk + IR (adjacent)|Risk owns vuln and threat detection. Incident Response owns event detection and SOC. Risk feeds intelligence to IR.|
|**RESPOND**|IR (adjacent) + Governance|IR leads response execution. Governance owns the playbook library and post-incident documentation. Risk provides threat context during incidents.|
|**RECOVER**|IR (adjacent) + Governance|IR leads recovery. Governance manages lessons-learned documentation and improvement tracking. Engineering supports system restoration where architectural changes are needed.|

---

## 8. Regulatory Alignment

### 8.1 NERC-CIP

NERC-CIP is the primary regulatory framework for bulk electric system (BES) cybersecurity. For an electrical utility, NERC-CIP requirements are non-negotiable and carry significant enforcement risk.

|CIP Standard|CERG Ownership and Application|
|---|---|
|**CIP-002:** BES Cyber System Categorization|Governance leads the annual categorization process. Engineering provides technical input on system connectivity and function. Risk validates the asset inventory.|
|**CIP-003:** Security Management Controls|Governance owns all CIP-003 policies and senior manager approval processes. Risk provides threat context for policy updates.|
|**CIP-004:** Personnel & Training|Governance sets training requirements and coordinates with the Security Awareness team for delivery. Engineering and Risk fulfill their own training obligations.|
|**CIP-005:** Electronic Security Perimeters|Engineering designs and implements ESPs and EAPs. Governance maintains ESP documentation. Risk validates perimeter integrity through scanning.|
|**CIP-006:** Physical Security|Governance maintains physical security policy. Engineering reviews physical security requirements for new OT deployments.|
|**CIP-007:** Systems Security Management|Risk owns patch management tracking and vulnerability assessment. Engineering implements port/service controls during deployment. Governance assures standards conformance and evidence quality.|
|**CIP-010:** Configuration Management & Vuln Assessments|Engineering produces and maintains configuration baselines. Risk performs CIP-010 annual vulnerability assessments. Governance retains assessment records.|
|**CIP-011:** Information Protection|Governance defines BES Cyber System Information (BCSI) handling requirements. Engineering implements technical protections. Risk validates through scanning.|
|**CIP-013:** Supply Chain Risk Management|Risk leads vendor risk assessment. Governance maintains the supply chain risk management plan. Engineering applies controls to vendor-supplied systems.|
|**CIP-014:** Physical Security (Transmission)|Governance maintains risk assessment documentation. Engineering consults on physical-cyber interdependencies.|

### 8.2 CMMC: Cybersecurity Maturity Model Certification

[CMMC](https://dodcio.defense.gov/CMMC/) Level 2 requires implementation and assessment of all 110 practices in [NIST SP 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final). For organizations handling Controlled Unclassified Information (CUI) on behalf of the federal government, CMMC certification is a contract requirement. CERG provides the operating controls, evidence, and assurance from which CMMC compliance is demonstrated.

- **Engineering** implements the technical controls across the 14 CMMC domains, access control, configuration management, system and communications protection, and others, during project delivery
- **Risk** performs the periodic assessments required by CMMC practice CA.2.157 and manages the Plan of Action & Milestones (POA&M) for open findings
- **Governance** maintains the System Security Plan (SSP), manages the evidence library, coordinates C3PAO assessment logistics, and tracks POA&M items to closure

### 8.3 SOX

For organizations subject to [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC requirements, CERG provides the structural foundation for compliance without requiring a separate compliance team.

- **SOX ITGC:** Governance owns the IT General Controls framework and evidence library. Engineering ensures change management controls are embedded in deployment processes. Risk monitors access and configuration integrity in financial systems.

> **The Regulatory Advantage of CERG**
> 
> Organizations with multiple regulatory obligations, a utility managing NERC-CIP, CMMC, and SOX simultaneously, typically struggle with duplicated effort and conflicting timelines. CERG uses one governance model, one control set, and one evidence library, while Engineering and Risk produce operating evidence as a byproduct of daily work. Regulatory alignment is demonstrated from that evidence, not through a parallel compliance exercise.

---

## 9. IT/OT Considerations

### 9.1 The Air-Gapped Starting Point

Most organizations with OT environments today maintain a degree of air-gap separation between their operational technology networks and enterprise IT. For an electrical utility, this typically means:

- SCADA systems, energy management systems (EMS), and substation automation on isolated OT networks
- Historian servers in a DMZ acting as the data bridge between OT and IT
- Jump servers or data diodes controlling any permitted data flows
- Physical controls limiting access to OT environments

CERG is designed to operate in this context. The air-gap is a security control, Governance documents it, Risk validates it, and Engineering designs to preserve it while enabling the operational visibility the business needs.

### 9.2 The Modernization Pressure

The push to modernize OT infrastructure is real. Utilities are evaluating advanced metering infrastructure (AMI), remote monitoring, predictive maintenance, and grid modernization initiatives that all require some level of IT/OT integration. CERG's role is to ensure that modernization happens securely, not to prevent it.

> **Engineering's Role in IT/OT Convergence**
> 
> When the business initiates an IT/OT convergence project, Engineering must be engaged before the vendor is selected and before the architecture is set. The engineering team reviews whether the proposed integration can be achieved while maintaining the electronic security perimeters required by CIP-005, the configuration management discipline required by CIP-010, and the segmentation required to limit the blast radius of a cyber event in either direction. This is far more effective and far less expensive than retrofitting security after the system is installed.

### 9.3 OT-Specific Risk Considerations

The Risk team's approach to OT environments differs from IT in several important ways:

- **Scanning must be OT-safe:** active network scanning of OT environments can disrupt control processes. Risk uses passive monitoring, vendor-provided scan tools, and approved active scanning windows coordinated with OT operations.
- **Patch windows are constrained:** OT systems often cannot be patched on standard IT timelines due to vendor testing requirements, operational windows, and redundancy limitations. Risk tracks OT patch exposure and validates the residual risk when a standard cannot be met; Governance assures the exception path and evidence requirements.
- **Availability is the primary objective:** in OT environments, availability often outranks confidentiality in the risk calculus. Risk team members must understand this trade-off and communicate findings in terms of operational impact, not just CVSS scores.
- **Threat intelligence must include ICS-specific sources:** Risk maintains subscriptions to ICS-CERT advisories, E-ISAC threat intelligence, and vendor-specific security bulletins for all OT platforms in use.

### 9.4 Governance in OT Environments

NERC-CIP obligations are implemented through the same CERG assurance loop, with OT-specific control parameters and safety constraints. Governance maintains the IT and OT policy structure, required control outcomes, evidence criteria, and exception paths. It does not operate OT systems or perform remediation for their owners.

- **BES system and control owners** maintain CIP-002 asset records, operate required controls, and provide implementation and remediation evidence.
- **Engineering** designs and implements OT guardrails within reliability and maintenance constraints.
- **Risk** assesses exposure, validates compensating controls, and evaluates the cybersecurity and reliability tradeoff.
- **Governance** assures conformance to the applicable standards, records decisions and exceptions, directs corrective action for deficiencies, and escalates through the CISO where required.

Governance coordinates with reliability operations so security requirements and corrective actions do not introduce unacceptable reliability risk.

---

## 10. Team Structure and Talent Model

### 10.1 Illustrative Team Structure

The illustrative organization for this framework is a large regulated enterprise with substantial employee, contractor, cloud, SaaS, and operational-technology scope. CERG for this organization is a fully staffed function reporting to the CISO and operating alongside Security Awareness and Incident Response.

This is an intentionally large example. The goal is to show what CERG looks like at full scale, with real operational velocity and complexity, so that teams of any size can see the complete model and trim to fit their environment. A small CERG running this framework looks different in headcount, not in structure.

At this scale, the workload is substantial across all three pillars. Engineering carries approximately 125 active project engagements per year with roughly 40 running concurrently, spanning infrastructure, enterprise applications, cloud migrations, and third-party integrations. Engineers are aligned to specific business verticals and develop fluency in the systems they support, not just the security controls that apply to them.

Risk operates at equivalent velocity. The vendor risk program may cover thousands of active vendors and an extended workforce of remote contractors. Exposure management may span 100,000+ assets across enterprise IT, OT networks, and cloud environments. Adversarial validation runs on continuous cycles across pen test, red-team, purple-team, cloud, and OT-safe activities where in scope. Threat intelligence is a production function producing actionable intelligence distributed to Engineering, Incident Response, and leadership.

Governance operates as a domain-expert function. Subject matter experts carry deep technical knowledge in network security, identity and access management, cloud security, OT/ICS security, and cryptography, then translate expertise into implementation guidance that engineering and operations teams use. The regulated scope may span multiple frameworks simultaneously, but the rules and evidence remain one operating model. The evidence library is a living system, not a pre-audit scramble. The policy and standards catalog is actively maintained, version-controlled, and tied to applicable obligations.

A representative staffing structure for a CERG of this scale:

|Role|Pillar|Key Responsibilities|
|---|---|---|
|CISO|Executive|Strategy, CERG leadership, board and executive reporting, regulatory escalation, budget authority|
|Engineering Pillar Leader|Engineering|Engagement portfolio oversight; vertical alignment model; OT/IT convergence program lead; senior architecture decisions; team development|
|Senior Cyber Engineer - OT/ICS (×3)|Engineering|Generation, transmission, and distribution vertical leads; SCADA and substation security architecture; CIP-005/CIP-010 design consultation; OT modernization advisory|
|Senior Cyber Engineer - IT/Cloud (×3)|Engineering|Enterprise IT and cloud vertical leads; application and infrastructure security architecture; identity and access design; pre-production assessment leadership|
|Cyber Engineer (×8)|Engineering|Project-level security consultation across assigned verticals; pre-production coordination with Risk; vendor solution review; risk treatment plan drafting; handoff documentation|
|Risk Pillar Leader|Risk|Program ownership across vuln management, adversarial validation, threat intel, and vendor risk; OT risk strategy; executive risk reporting|
|Senior Risk Analyst - Exposure Management (×3)|Risk|Enterprise vuln scan operations; OT-safe scanning program; finding prioritization and triage; SLA tracking and escalation; remediation verification|
|Threat Intelligence Analyst (×2)|Risk|Threat actor tracking; ICS/OT-specific intelligence production; E-ISAC and ICS-CERT liaison; intelligence distribution to Engineering and IR|
|Senior Risk Analyst - Vendor & Third-Party Risk (×2)|Risk|Vendor security assessment program; contractor access risk; contract redline support; supply chain risk reporting|
|Risk Analyst - Adversarial Testing (×3)|Risk|Internal pen test execution; external red team coordination; purple-team support; OT adversarial testing; findings documentation and tracking|
|Risk Analyst (×5)|Risk|Day-to-day vuln tracking and owner follow-up; vendor assessment support; threat feed monitoring; finding remediation documentation|
|Governance Pillar Leader|Governance|Policy, standards, and control-assurance ownership; regulated-overlay assurance; risk-register governance; Governance team development|
|NERC-CIP Compliance Manager (×3)|Governance|BES Cyber System standards conformance; CIP exception and mitigation assurance; NERC-CIP evidence quality; reliability-security interface|
|Senior Governance Analyst - Technical Domains (×4)|Governance|Domain SME coverage across network security, IAM, cloud, and cryptography; implementation guidance production; standard development; Engineering QA reviews|
|CMMC / Federal Compliance Manager (×3)|Governance|CMMC evidence readiness; 800-171 control and evidence mapping; SSP and POA&M assurance; federal contract overlay calendar|
|Governance / Compliance Analyst - Commercial Frameworks (×3)|Governance|SOX ITGC control and evidence mapping; assurance readiness; evidence-library quality; regulated-overlay calendar|
|Policy & Standards Manager (×3)|Governance|Policy and procedure documentation; version control and review cycles; cross-pillar QA reviews; training content support for Security Awareness|

This representative structure distributes staff across Engineering, Risk, and Governance, with the CISO and pillar managers rounding out the team. The specific allocation will shift based on organizational priorities: a cloud migration program will weight Engineering more heavily; a regulated-scope assurance cycle will weight Governance.

> **Scaling the Model**
> 
> Most organizations will run a smaller CERG than this example, and that is by design. A small regulated operator might assign one person to each pillar, with each person carrying multiple canonical roles. A single-security-owner organization might have that person operate across all three pillars with the Executive Sponsor providing independent risk-decision support. The framework is the same at every size. The roles compress; the responsibilities do not disappear, they concentrate. Understanding the full-scale model helps smaller teams identify what they are covering, what they are deferring, and where they need to prioritize as they grow.

### 10.2 The Left-Right Knowledge Model

One of CERG's explicit design goals is talent resilience, the ability to absorb the loss of any single team member without stopping work. The mechanism for achieving this is deliberate left-right knowledge sharing within and across pillars.

- Within each pillar, team members document their work in a shared and accessible way, not as bureaucratic overhead but as operational artifacts that others can follow
- Governance's policies and standards serve as the knowledge base for Engineering and Risk, new arrivals can orient themselves by reading what Governance has documented
- Risk's vulnerability reports and threat intelligence give Engineering context for why certain design decisions matter
- Engineering's architecture and handoff documents give Risk a current map of what is in the environment and how it is configured

In practice, this means that a new Cyber Engineer can learn the organization's standards from Governance, understand the current threat environment from Risk, and have context for every major system from Engineering's project documentation. Onboarding accelerates. Knowledge is in the system, not in someone's head.

### 10.3 CERG and the Adjacent Teams

|Interaction|Description|
|---|---|
|CERG → Security Awareness|Governance provides policy and procedure content for awareness training. Risk provides threat intelligence for targeted awareness campaigns (e.g., spear-phishing scenarios relevant to ICS/OT). Engineering feeds real-world examples from project work into training scenarios.|
|CERG → Incident Response|Risk provides threat intelligence and vulnerability context during incidents. Engineering provides architecture and configuration documentation to support containment and recovery. Governance provides playbooks and manages post-incident documentation.|
|Security Awareness → CERG|Awareness provides metrics on training completion and phishing simulation results - inputs for Governance's assurance tracking and risk register.|
|Incident Response → CERG|IR provides post-incident findings and lessons learned - inputs for Risk (threat landscape updates), Engineering (architectural improvements), and Governance (policy and playbook updates).|

---

## 11. Getting Started: The Path to Adaptive

### 11.1 Phase 1: Establish (Months 1–3)

The first priority is standing up the CERG structure and establishing the baseline work products each pillar needs to function.

- **Engineering:** Document the active project portfolio. Identify any in-flight projects that should receive a retroactive engineering review. Establish the lightweight intake process.
- **Risk:** Stand up or audit the exposure management program. Ensure IT and OT environments are covered with appropriate scanning approaches. Inventory threat intelligence feeds.
- **Governance:** Conduct a policy gap assessment against NIST 800-53 and applicable regulatory frameworks. Identify the three to five most critical missing or out-of-date policies. Build or inherit the risk register.

### 11.2 Phase 2: Operate (Months 4–9)

With the structure in place, the focus shifts to operating CERG as a team and building the cross-pillar working rhythms.

- Establish a regular CERG operating cadence, weekly pillar syncs, monthly cross-pillar review, quarterly CISO briefing
- Engineering begins processing the project intake queue and building the first round of handoff documentation
- Risk begins producing regular vulnerability reports with prioritized findings and tracking remediation to SLA
- Governance completes the first standards-conformance assessment against NERC-CIP and CMMC overlays; begins assuring the evidence library
- All pillars begin practicing the "yes, and..." model on real business requests

### 11.3 Phase 3: Mature (Months 10–18)

The CERG model begins demonstrating Repeatable behavior. The path to Adaptive requires building the continuous improvement and integration functions.

- Risk begins producing structured threat intelligence reports distributed to Engineering, IR, and leadership
- Governance launches a formal QA cycle, quarterly reviews of Engineering and Risk work products against defined standards
- Engineering demonstrates consistent early engagement on projects, present at business requirements stage, not called in at go-live
- First external validation: coordinate a NERC-CIP compliance audit or CMMC readiness assessment to measure progress and identify gaps
- Begin building the metrics program, vulnerability SLA adherence, time-to-engage on new projects, evidence collection completeness, policy currency

### 11.4 Adaptive Indicators

An organization operating at Adaptive maturity will demonstrate these observable behaviors:

- The security team is engaged in business planning conversations before projects are funded, not after they are designed
- Threat intelligence from Risk actively changes Engineering design decisions and Governance policy priorities
- When a significant vulnerability or threat emerges, the organization has a clear, practiced process for assessing impact, communicating status, and executing response, within hours, not days
- External auditors and regulators find organized, complete, and timely evidence, because evidence collection is a byproduct of daily work, not a pre-audit scramble
- New team members become productive faster because the CERG knowledge base, policies, standards, architecture documents, risk reports, is current, accessible, and well-organized
- The CISO can credibly report the organization's risk posture to the board using data from the risk register, control assurance, and operating evidence, not gut feel

---

## 12. Compliance as Exhaust — Evidence Factories

Regulatory alignment is a byproduct of running the program well. Evidence is produced once, from operational work, then reused across frameworks. Capabilities declare what the program can do; evidence factories produce the independently verifiable proof; compliance consumers reuse that proof without a parallel scramble. These evidence factories show the mapping:

| Operational Work | Evidence Produced | Compliance Consumers |
|-----------------|-------------------|---------------------|
| Architecture review ([AR-001](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md)) | Design decision, data flow, control scope, pre-approved pattern match | NIST 800-53 (SA/PL), CMMC (SC), SOX ITGC, NERC-CIP CIP-005/010 |
| Exposure management ([VM-001](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md)) | Finding state, exposure classification, treatment, verification | NIST 800-53 (RA/SI), CMMC (RA), NERC-CIP CIP-007, SOX ITGC |
| SaaS onboarding ([TPRM-001](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md)) | Shared responsibility matrix, vendor evidence, contract clauses, SSPM posture | CMMC (SR), SOX ITGC, privacy regulations, NERC-CIP CIP-013 |
| Access review ([AC-002](../procedures/CERG-PRC-AC-002_Access_Management_Runbook.md)) | Population reviewed, reviewer, exceptions, recertification status | SOX ITGC, CMMC (AC), NERC-CIP CIP-004 |
| Change security routing ([FLOW-001](CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md) F-05) | Impact analysis, approval, test result, CAB record | SOX ITGC, NERC-CIP CIP-010, NIST 800-53 (CM) |
| Risk acceptance ([RMF-001](CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.7) | Risk assessment, compensating controls, business owner acceptance | NIST 800-53 (RA), CMMC (RM), NERC-CIP deviation process |
| Incident response ([IR Plan](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md)) | Timeline, investigation, lessons learned, corrective actions | NIST 800-53 (IR), CMMC (IR), NERC-CIP CIP-008 |
| Asset registration ([FLOW-001](CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md) F-03) | Owner confirmed, classification, coverage validated | NIST 800-53 (CM-8), CMMC (AM), NERC-CIP CIP-002 |

This is where CERG can beat traditional GRC: compliance becomes exhaust from good operations, not a parallel workstream. Evidence packages are generated from operational records, not assembled from scratch before an audit. The [Compliance Calendar](CERG-GOV-CAL-001_Annual_Security_and_Governance_Calendar.md) maps each evidence factory to its production cadence.

## 13. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-FRM-001 |
| **Version** | 1.23 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | CISO |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on material change to framework |
| **Next Scheduled Review** | 2027-05-01 |
| **Frameworks** | NIST CSF 2.0; NIST 800-53r5; NIST 800-171r3; NIST RMF |
| **Regulations** | NERC-CIP; CMMC L2; SOX ITGC |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.23 | 2026-09-01 | Cyber Governance | Clarified Cyber Governance as CERG's second-line authority: it sets standards and assurance expectations, while first-line owners, Engineering, and Risk produce operating evidence and remediate or validate control gaps. Reframed regulatory alignment as an output of the normal CERG assurance loop. |
| 1.0 | 2026-05-01 | CISO + Cyber Governance | Initial release. Narrative description of the CERG framework, pillars, and operating model. |
| 1.21 | 2026-05-22 | Cyber Governance | Updated framework references and pillar descriptions. |
| 1.22 | 2026-06-24 | CISO + Cyber Governance | Added capability taxonomy, capability reference set, maturity grading, and evidence-factory linkage. |

### Review Triggers

- Material change to CERG structure or operating model
- Framework version change
- Direction from the CISO or executive leadership

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| CERG Operating Model | [CERG-GOV-OM-001](CERG-GOV-OM-001_CERG_Operating_Model.md) | Operating model detail |
| Document Catalog | [CERG-GOV-CAT-001](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Master document inventory |
| Unified Control Baseline | [CERG-GOV-CB-001](CERG-GOV-CB-001_Unified_Control_Baseline.md) | Control spine |
| Implementation Cards | [CERG-GOV-IMP-004](CERG-GOV-IMP-004_Implementation_Cards.md) | Intent-to-implementation guidance |
| Edge Register | [CERG-GOV-EDG-001](CERG-GOV-EDG-001_Edge_Register.md) | Organizational edge management |

---
