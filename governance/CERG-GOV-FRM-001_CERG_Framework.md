## The CERG Framework

### A Scalable, Adaptive Cybersecurity Operating Model

> Designed for Adaptive [NIST CSF 2.0](https://www.nist.gov/cyberframework) maturity. Applicable to IT and OT environments. Calibrated for [CMMC](https://dodcio.defense.gov/CMMC/), NERC-CIP, and [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204).
> 
> _Examples in this document reference a large enterprise at the upper bound of what CERG is designed to support — the framework is scaled to fit organizations from 5 people to large regulated entities. Readers should scale down to their environment. Sector-specific illustrative profiles are available in [`/examples/`](../examples/). See also [`CERG-GOV-VAR-001`](CERG-GOV-VAR-001_Organization_Adaptation_Profile.md) for mechanical adaptation._

---

| | |
|---|---|
| **Document ID** | CERG-GOV-FRM-001 |
| **Version** | 1.21 |
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
2.4. [Capabilities: What CERG Delivers](#24-capabilities-what-cerg-delivers)
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

CERG consolidates the core work of a mature cybersecurity function into three tightly coupled, clearly bounded pillars. Together they are pronounced **"Surge"**, because effective security is fast, powerful, and directional. Surge is not a support function. It is an operational force that enables the business to move confidently.

### Why Three Pillars

Most cybersecurity work, outside of Security Awareness and Incident Response, falls naturally into one of three activities:

- **Building and deploying secure technology** alongside the business
- **Assessing exposure and managing risk** continuously
- **Setting standards, ensuring compliance, and tracking conformance**

The CERG model names these activities explicitly, Engineering, Risk, and Governance, and assigns clear ownership, accountabilities, and interaction patterns so that work flows between them without dropping and without creating new silos.

### Design Principles

- **Scale up or down:** applicable to a 5-person team or a 500-person organization
- **Regulatory-ready:** designed to satisfy [CMMC](https://dodcio.defense.gov/CMMC/), NERC-CIP, [NIST CSF 2.0](https://www.nist.gov/cyberframework), 800-53, 800-171, and [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)
- **IT/OT aware:** principles apply equally to enterprise IT and operational technology environments
- **Talent resilient:** cross-pillar knowledge sharing means no single person is a point of failure
- **Adaptive-targeted:** the framework describes what operating at [NIST CSF 2.0](https://www.nist.gov/cyberframework) Adaptive maturity looks like in practice
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

Continuous assessment and management of the organization's exposure through exposure management, penetration testing, vendor risk assessment, and threat intelligence.

---

#### 📋 G: Cyber Governance

**Set the rules. Track the work. Enable the business to move with confidence.**

The rule-makers, compliance managers, and quality assurance function, responsible for policies, standards, implementation guidance, regulatory compliance, and control evidence.

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
|Ongoing compliance monitoring|Governance|Risk tracks patch status and emerging CVEs; Engineering supports remediation|
|Audit and evidence collection|Governance|Engineering and Risk produce artifacts from their daily work|
|Penetration test / red team|Risk|Engineering reviews findings for architectural impact; Governance logs findings|
|Regulatory exam or audit|Governance|All pillars provide evidence; Engineering and Risk support responses|

---


---

## 3. Capabilities: What CERG Delivers

A **control** is something an organization has (an access control, a configuration standard, an approved exception). A **capability** is something it can **do**. CERG is built around capabilities because controls on a shelf do not stop attacks. A program that can *detect*, *respond*, and *recover* under pressure is the goal; controls are the ingredients, not the dish.

### 3.1 Capability Hierarchy

Every CERG capability maps to a chain:

**Capability → Control(s) → Procedure(s) → Evidence**

- **Capability** declares *what the program can do* and how mature it is.
- **Control(s)** are the NIST or CERG-native requirements that enable it.
- **Procedure(s)** are the operational workflows that execute it.
- **Evidence** is the independently verifiable proof that it works.

Capabilities are multi-pillar by nature: detection requires Engineering (telemetry, logging standards), Risk (analytics, threat intelligence), and Governance (compliance attestation). The traceability model in [CERG-GOV-TRC-001](CERG-GOV-TRC-001_Control_to_Procedure_Traceability_Matrix.md) can be extended to include capability anchors.

### 3.2 CERG Capability Reference Set

The following illustrative capabilities establish the naming convention and pattern. Each entry follows the identifier scheme `CAP-{PILLAR}-{DOMAIN}-{SEQ}`.

| ID | Capability | Primary Owner | Anchor Controls | Procedures | Evidence | Test Method |
|---|---|---|---|---|---|---|
| CAP-ENG-SECIN-001 | Secure systems are designed and reviewed before production go-live | Cyber Engineering | SA-2, SA-11, CM-2 | AR-001 (Architecture Review), CM-001 (Configuration Mgmt) | Architecture decision record, pre-production checklist, risk acceptance package | Review: random sample of 20% of projects per quarter |
| CAP-ENG-CONFIG-001 | Approved configuration baselines are implemented and drift is detected across all in-scope systems | Cyber Engineering | CM-2, CM-3, CM-6 | CM-001, VM-001 (Exposure Management) | Baseline record, drift scan report, remediation ticket | Automated config scan; quarterly gap report |
| CAP-ENG-ISOLATE-001 | Compromised systems or identities can be contained automatically or within 15 minutes | Cyber Engineering | AC-4, AC-16, SC-7, IR-4 | IR-001 (Incident Response), AR-001 | IR timeline, containment action log, runbook execution record | Tabletop with 30-minute containment drill; measured elapsed time |
| CAP-RSK-DETECT-001 | Lateral movement and anomalous identity behavior are detected across on-prem and cloud environments | Cyber Risk + IR | AU-6, AU-12, SI-4 | VM-001, IR-001 | Detection coverage report, alert fidelity metrics, hunting report | Red team exercise; detection coverage gap analysis |
| CAP-RSK-VULN-001 | Critical and high vulnerabilities are remediated or risk-accepted within defined SLAs | Cyber Risk | RA-5, SI-2, PM-30 | VM-001, RMF-001 (Risk Management) | Vulnerability register, SLA adherence report, POA&M | Quarterly SLA audit against risk register |
| CAP-RSK-THI-INT-001 | Actionable threat intelligence is produced, distributed, and consumed by Engineering, Risk, and IR | Cyber Risk | PM-16, RA-3, IR-4 | TPRM-001 (Third Party / Supply Chain), IR-001 | Threat intelligence brief, distribution log, intake feedback loop | Quarterly review: intelligence sourced, actions taken, feedback recorded |
| CAP-GOV-EVID-001 | Control evidence is complete, organized, and independently verifiable at any time | Cyber Governance | CA-2, CA-7, PM-14 | AUD-001 (Evidence Quality) | Evidence library completeness score, audit trail | Unannounced evidence spot-check; score % complete by control |
| CAP-GOV-AUDIT-001 | External and internal audit findings are tracked, responded to, and closed within regulatory windows | Cyber Governance | CA-5, PM-5, PL-2 | RMF-001, AUD-001 | Finding register, remediation tracker, closure attestation | Audit track rate; open-finding aging report |
| CAP-XPN-IR-READY-001 | The organization can sustain operations through a significant cyber event with defined RTO and RPO | Cross-Pillar | CP-2, CP-9, CP-10, IR-4, IR-8 | BCDR-001, IR-001 | Recovery test results, DR runbook, post-test gap report | Annual tabletop + bi-annual technical recovery drill |

### 3.3 Capability Maturity Grading

Capability maturity is assessed against the evidence chain, not checklist completeness. The five levels:

| Level | Label | Operational Meaning |
|---|---|---|
| 1 | **Absent** | No documented capability; no evidence; no test performed. Even basic practice is ad hoc or absent. |
| 2 | **Ad Hoc** | Practice exists but is inconsistent; evidence is partial or not independently verifiable. |
| 3 | **Defined** | Capability is documented, owned, and has a named evidence artifact. Tested at least once in the past 12 months. |
| 4 | **Repeatable** | Practice is performed consistently across scope; evidence is organized and complete; test cadence is regular and results are tracked over time. |
| 5 | **Adaptive** | Capability improves based on test findings and threat intelligence; automation or continuous validation reduces manual effort; matures without external prompting. |

Scoring methodology: for a given capability, collect the evidence chain stated in §3.2. **Every pipeline stage** must produce acceptable evidence. A control that is implemented but untested stays at Defined; a control tested twice with remediation of findings moves toward Repeatable; a control with automation and continuous validation reaches Adaptive.

### 3.4 Why This Changes the Conversation

Tool-centric programs ask: *Which products do we own?* Capability-centric programs ask: *What can we demonstrate under pressure?*

The difference is visible in three places:

- **Budget requests.** "We need a SIEM" becomes "Our detection capability has a 40% visibility gap in cloud identity signals; closing it requires EDR telemetry + SIEM correlation + threat intel enrichment."
- **Board reporting.** "We passed the audit" becomes "Our containment capability is Defined and on track to Repeatable by Q3 based on quarterly drill metrics."
- **Maturity assessments.** Feature-count scoring becomes evidence-chain scoring. Repeatable means the evidence is organized and complete, not that twelve controls are marked 'implemented.'

Controls, standards, and procedures do not go away. They are the infrastructure that capabilities draw from. The Unified Control Baseline ([CERG-GOV-CB-001](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md)) is the control substrate. Capabilities are what the program builds on top of it.

---

## 4. Cyber Engineering

> **Mission:** Build securely. Deploy confidently. Consult continuously.

### 5.1 Mission

The Cyber Engineering team serves as the organization's internal security consulting practice. Engineers are assigned to enterprise and IT projects, often as the first security touch point in a project lifecycle, and carry security requirements, design review, and implementation guidance from concept through production handoff.

Engineers do not own the systems they help build. Their role is to ensure that security is designed in from the beginning, that pre-production findings are remediated or risk-accepted before go-live, and that the receiving operations team understands the security posture of what they are taking on.

### 5.2 Core Functions

- **Project intake and early engagement**: review of business requirements, solution architecture documents, and procurement specifications
- **Security architecture consultation**: participating in design reviews, advising on control selection aligned to [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) and organizational standards
- **Pre-production security review**: working with the Risk team to understand vulnerability scan findings and driving remediation with project teams before go-live
- **Risk treatment support**: assisting project teams in drafting risk acceptance documentation and treatment plans when a vulnerability cannot be remediated prior to launch
- **OT/IT convergence advisory**: guiding teams through the security implications of connecting or modernizing operational technology environments
- **Production handoff**: ensuring Governance and Risk have the configuration baseline, asset documentation, and control evidence needed to assume post-production oversight

### 5.3 Engagement Model

Engineering operates on a lightweight internal consulting model. The goal is to minimize administrative overhead and maximize time on engineering work.

|Element|Description|
|---|---|
|Intake|Engineers are engaged via a lightweight request - a brief summary of the project, timeline, and primary contact. No complex ticketing or lengthy intake forms.|
|Assignment|Each engagement is assigned a lead engineer. On large projects, multiple engineers may be assigned. Engineers manage their own capacity with CISO visibility.|
|Engagement scope|Engineers work alongside project teams, not above them. They advise, review, and recommend - the project team retains implementation accountability.|
|Pre-production gate|Before any system or tool goes live, Engineering confirms that open vulnerabilities have been remediated or formally risk-accepted. This is a lightweight confirmation, not a gate that stops work.|
|Handoff documentation|At production cutover, Engineering produces or confirms existence of: asset registration, configuration baseline, control mapping, and any open risk items.|
|Post-production|Once a system is in production, Engineering moves to the next project. Risk and Governance assume ongoing oversight. Engineering may be re-engaged for significant changes.|

### 5.4 Illustrative Example: Electrical Utility

> **Scenario: IT/OT Network Modernization**
> 
> The utility's operations team wants to add remote monitoring capability to its substation SCADA systems. An Engineering team member is engaged at the business requirements stage. They review the vendor's solution architecture, flag the absence of encrypted communications between the historian and the enterprise DMZ, and work with the project team to require TLS enforcement before go-live. The Risk team performs a pre-production scan and finds an unpatched firmware version. Engineering works with the vendor on a patch timeline. When the patch cannot be applied before the project deadline, Engineering helps draft a risk treatment plan with compensating controls, network segmentation, enhanced logging, that Governance reviews for NERC-CIP CIP-005 conformance. VP and CISO sign off. The system goes live with a 90-day remediation commitment documented.

### 5.5 NIST Framework Alignment: Engineering

|NIST Framework|Relevant Controls / Functions|Engineering Role|
|---|---|---|
|[NIST CSF 2.0](https://www.nist.gov/cyberframework)|GOVERN, IDENTIFY (Asset Mgmt, Risk Assessment), PROTECT (Identity Mgmt, Data Security, Platform Security)|Primary driver of PROTECT function; co-owner of IDENTIFY|
|[NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)|SA (System & Services Acquisition), CM (Configuration Mgmt), SI (System & Info Integrity)|Implements SA and CM controls during project delivery|
|[NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final)|3.13 System & Communications Protection, 3.14 System & Info Integrity|Ensures CUI protection controls are designed into systems handling federal data|
|NIST RMF|Steps 2 (Select), 3 (Implement), 4 (Assess - pre-production)|Leads control selection and implementation; supports pre-production assessment|
|NERC-CIP|CIP-005 (Electronic Security Perimeters), CIP-007 (Systems Security Mgmt), CIP-010 (Config Mgmt)|Designs systems to conform to CIP requirements from the start|
|[CMMC](https://dodcio.defense.gov/CMMC/)|Level 2: Access Control, Configuration Mgmt, Identification & Auth|Ensures [CMMC](https://dodcio.defense.gov/CMMC/) practices are implemented in applicable systems|

---

## 5. Cyber Risk

> **Mission:** Know your exposure. Manage it deliberately. Never be surprised.

### 6.1 Mission

The Cyber Risk team is responsible for understanding the organization's threat landscape and exposure at all times. Risk does not wait for problems to surface, it hunts for them. Through continuous exposure management, periodic penetration testing, vendor risk assessment, and threat intelligence, Risk produces the clearest possible picture of what is threatening the organization and how severe those threats are.

Risk serves both a pre-production function (finding issues before systems go live) and a post-production function (tracking drift, emerging CVEs, and changes in the threat environment after systems are in operation).

### 6.2 Core Functions

- **Exposure Management**: continuous scanning of IT and OT environments; prioritization of findings by criticality, exploitability, and asset value; tracking remediation to closure
- **Penetration Testing**: periodic adversarial testing of systems, networks, and applications; coordination of external red team engagements; findings fed back to Engineering and Governance
- **Threat Intelligence**: monitoring of threat actor activity, emerging CVEs, and sector-specific intelligence (including ICS/SCADA threats for OT environments); distribution of actionable intelligence to Engineering, IR, and Governance
- **Vendor and Third-Party Risk**: security review of vendor contracts, SaaS solutions, and third-party integrations; contract redline support for security requirements
- **Pre-Production Assessment**: vulnerability scanning and risk analysis of systems prior to go-live; classification of findings by severity; coordination with Engineering on remediation
- **Risk Treatment and Acceptance**: for findings that cannot be immediately remediated, Risk co-develops treatment plans with Engineering and provides analysis to support leadership sign-off decisions

### 6.3 Pre-Production vs. Post-Production Risk

> **An Important Distinction**
> 
> A vulnerability found in a pre-production system is not a realized risk, the system is not yet live and has not been exposed. The Risk team treats pre-production findings as engineering inputs, working with the Engineering team to drive remediation before launch. Post-production findings are realized risks to be managed, tracked, and reported. This distinction shapes how findings are communicated, prioritized, and escalated.

|Finding Type|Handling|
|---|---|
|Pre-production, Low/Medium severity|Engineering remediates with project team before go-live. Tracked to closure by Risk.|
|Pre-production, High/Critical severity|Engineering and Risk jointly assess. If unremediated, a risk treatment plan is required with VP+ sign-off before go-live.|
|Post-production, Low/Medium severity|Tracked in vulnerability register. Assigned to appropriate owner (IT/OT ops) with SLA. Governance monitors SLA compliance.|
|Post-production, High/Critical severity|Escalated immediately. CISO notified. Risk treatment plan required. Engineering may be re-engaged for architectural remediation. NERC-CIP and [CMMC](https://dodcio.defense.gov/CMMC/) deviation processes invoked as applicable.|
|Vendor/Third-party finding|Risk documents and includes in vendor risk register. Governance tracks contractual remediation commitments. Engineering consulted if architectural change is needed.|

### 6.4 Illustrative Example: Electrical Utility

> **Scenario: NERC-CIP Vulnerability in a BES Cyber System**
> 
> During monthly vulnerability scanning, the Risk team identifies that a critical relay management workstation, classified as a BES Cyber System under NERC-CIP CIP-002, is running an operating system version with a known critical vulnerability (CVSS 9.1). The asset cannot be patched within the standard 35-day window due to vendor testing requirements. Risk notifies Governance of a potential CIP-007-6 deviation. Governance initiates the deviation documentation process. Risk produces a threat analysis showing no current exploitation activity targeting this specific system type. Engineering is engaged to add network monitoring on the affected segment as a compensating control. The CISO and VP of Operations sign the deviation. Risk tracks the patch to closure within the extended timeline and provides attestation documentation to Governance for the compliance record.

### 6.5 NIST Framework Alignment: Risk

|NIST Framework|Relevant Controls / Functions|Risk Team Role|
|---|---|---|
|[NIST CSF 2.0](https://www.nist.gov/cyberframework)|GOVERN (Risk Strategy), IDENTIFY (Risk Assessment, Improvement), DETECT (Adverse Event Analysis)|Primary driver of IDENTIFY and DETECT; co-owner of GOVERN risk functions|
|[NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)|RA (Risk Assessment), CA (Assessment & Authorization), PM (Program Mgmt), SI-2 (Flaw Remediation)|Executes RA and CA controls; owns SI-2 for patch and vuln tracking|
|[NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final)|3.11 Risk Assessment|Performs periodic assessments of CUI-handling environments|
|NIST RMF|Step 4 (Assess), Step 6 (Monitor)|Primary executor of continuous monitoring; supports periodic assessments|
|NERC-CIP|CIP-007 (Patch Mgmt), CIP-010 (Vuln Assessments), CIP-011 (Info Protection)|Manages CIP-007 patch tracking; conducts CIP-010 annual vuln assessments|
|[CMMC](https://dodcio.defense.gov/CMMC/)|Level 2: Risk Assessment (RA), Audit & Accountability (AU)|Performs [CMMC](https://dodcio.defense.gov/CMMC/) risk assessments; supports audit log review program|

---

## 6. Cyber Governance

> **Mission:** Set the rules. Track the work. Enable the business to move with confidence.

### 7.1 Mission

The Cyber Governance team is the rule-making, compliance management, and quality assurance function of the CERG model. Governance defines what good looks like, through policies, standards, and implementation guidance, and then ensures the organization actually gets there through compliance tracking, audit support, and control evidence management.

Governance operates from a **"yes, and..."** philosophy. The goal is never to block the business but to ensure that when the business accepts risk, that risk is documented, owned, and managed. Governance provides the framework within which Engineering and Risk do their best work.

### 7.2 Core Functions

- **Policy and Standard Development**: creating, maintaining, and retiring cybersecurity policies, standards, and procedures aligned to [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final), 800-171, [CSF](https://www.nist.gov/cyberframework), and applicable regulations
- **Implementation Guidance**: translating policy requirements into practical, actionable guidance for IT and OT teams; bridging the gap between regulatory language and operational reality
- **Compliance Management**: tracking the organization's compliance posture against NERC-CIP, [CMMC](https://dodcio.defense.gov/CMMC/), [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204), and other applicable requirements; managing the compliance calendar
- **Control Evidence Management**: setting standards for what constitutes acceptable evidence; collecting, organizing, and maintaining the control evidence library; coordinating audit responses
- **Risk Treatment Tracking**: maintaining the organization's risk register; tracking open risk treatment plans to completion; escalating overdue or deteriorating items to the CISO
- **Quality Assurance**: periodic review of Engineering deliverables and Risk outputs to ensure conformance with organizational standards; not an adversarial audit but a collaborative QA function
- **Regulatory Liaison**: serving as the primary point of contact for regulators and external auditors; managing examination logistics; coordinating response to findings and enforcement actions

### 7.3 The "Yes, And..." Standard

Governance reserves the right to say no, particularly for significant NERC-CIP deviations or [CMMC](https://dodcio.defense.gov/CMMC/) non-conformances where regulatory exposure is material. But the default orientation is enabling the business with guardrails, not closing doors. CERG publishes and reports against its own service-level commitments ([`CERG-GOV-SLC-001`](CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md)), so that a fast, safe yes is a measured obligation: a slow yes is a no the business routes around.

|Situation|"Yes, And..." Response|
|---|---|
|Project team cannot patch within standard SLA|Yes, you can extend the patching window - and we need a risk treatment plan, documentation of affected systems, compensating controls, and VP sign-off within 5 business days.|
|New SaaS tool handles CUI but lacks FedRAMP authorization|Yes, you can evaluate this vendor - and Risk needs to complete a vendor security assessment before procurement, and we'll need contractual security requirements in the agreement.|
|OT team needs remote access to SCADA during maintenance window|Yes, remote access is possible - and it must route through the approved jump server, use MFA, be logged, and the session record retained per CIP-007.|
|Business unit wants to skip architecture review to meet deadline|Yes, we can compress the review timeline - and Engineering must complete at minimum a 2-hour express review, and any open items become tracked exceptions with a remediation commitment.|
|NERC-CIP deviation required for emergency maintenance|Yes, the deviation can proceed - and we'll invoke the CIP deviation process: document the circumstances, notify as required, implement compensating measures, and close the deviation within the regulatory window.|

### 7.4 Evidence Standards

Governance sets the evidence standard, what constitutes acceptable proof that a control is operating effectively. Each pillar collects evidence appropriate to its work:

- **Engineering produces:** architecture review documentation, pre-production checklists, risk acceptance packages, handoff documentation, configuration baselines
- **Risk produces:** vulnerability scan reports, penetration test findings, threat intelligence reports, vendor risk assessments, patch tracking records
- **Governance produces:** policy documents, compliance matrices, audit reports, risk register entries, regulatory correspondence, exception approvals

Governance maintains the evidence library and ensures that evidence is organized, dated, attributed, and retained per regulatory requirements, NERC-CIP requires evidence retention for specified periods; [CMMC](https://dodcio.defense.gov/CMMC/) requires evidence available for assessment.

### 7.5 Illustrative Example: Electrical Utility

> **Scenario: [CMMC](https://dodcio.defense.gov/CMMC/) Level 2 Assessment Preparation**
> 
> The utility has a contract with the Department of Energy that requires [CMMC](https://dodcio.defense.gov/CMMC/) Level 2 compliance. Governance leads the preparation effort. They map all 110 [NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final) practices to the organization's existing controls, identifying 14 gaps. Governance works with Engineering to remediate 9 of the gaps through technical implementation. Three gaps are addressed through policy and procedure updates that Governance drafts. Two gaps require Risk to perform additional scanning and document compensating controls. Governance manages the evidence package, pulling architecture review records from Engineering, vulnerability reports from Risk, and policy documents from its own library. When the C3PAO assessment team arrives, Governance coordinates the logistics, manages the information requests, and tracks findings to closure post-assessment.

### 7.6 NIST Framework Alignment: Governance

|NIST Framework|Relevant Controls / Functions|Governance Role|
|---|---|---|
|[NIST CSF 2.0](https://www.nist.gov/cyberframework)|GOVERN (all functions), IDENTIFY (Improvement), RESPOND (Improvements)|Primary owner of the GOVERN function across all six sub-functions|
|[NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)|PL (Planning), PM (Program Mgmt), CA (Assessment), PS (Personnel Security)|Owns PL and PM control families; coordinates CA; sets PS standards|
|[NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final)|3.12 Security Assessment, all documentation requirements|Manages 800-171 assessment readiness and documentation compliance|
|NIST RMF|Step 1 (Categorize), Step 2 (Select - policy), Step 5 (Authorize), Step 6 (Monitor - compliance)|Leads categorization; co-leads authorization; owns compliance monitoring|
|NERC-CIP|CIP-003 (Security Mgmt Controls), CIP-004 (Personnel Training), CIP-014 (Physical Security Policy)|Primary owner of CIP-003; coordinates CIP-004 with Awareness team; maintains all deviation records|
|[CMMC](https://dodcio.defense.gov/CMMC/)|All documentation and evidence requirements across all domains|Manages assessment readiness, evidence collection, and C3PAO coordination|
|[SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC|IT General Controls documentation, change management evidence|Maintains ITGC control library; coordinates with external auditors|

---

## 7. Targeting [NIST CSF 2.0](https://www.nist.gov/cyberframework) Adaptive Maturity

### 8.1 What Adaptive Means

The NIST Cybersecurity Framework defines four tiers of organizational maturity: Partial, Informed, Repeatable, and Adaptive. Most organizations operating a mature security program reach Repeatable, processes are defined, practiced, and reviewed. Adaptive goes further.

At the Adaptive tier, an organization does not just respond to the threat environment, it anticipates it. Risk management is integrated into the fabric of business decision-making. Cybersecurity considerations are part of every significant investment, acquisition, and operational change. The security function continuously learns from internal events and external intelligence, and updates its practices accordingly.

|[CSF](https://www.nist.gov/cyberframework) Tier|What It Looks Like in Practice|
|---|---|
|**Partial (Tier 1)**|Ad hoc processes. Risk decisions made reactively. Limited awareness of threats. No consistent policy or evidence collection.|
|**Informed (Tier 2)**|Policies exist but are not consistently applied. Risk management happens in silos. Some awareness of threat environment. Inconsistent evidence.|
|**Repeatable (Tier 3)**|Defined, documented, and practiced processes. Risk management is consistent. Compliance calendar exists. Evidence is collected systematically. Teams understand their roles.|
|**Adaptive (Tier 4)**|Cybersecurity is integrated into organizational decision-making. Threat intelligence actively shapes priorities. Lessons learned drive continuous improvement. Risk appetite is clearly defined and applied. The business views security as a value driver, not a cost center.|

### 8.2 How CERG Produces Adaptive Behavior

The CERG model is designed to produce Adaptive-tier behavior through its structure, not just its aspirations.

|Adaptive Criterion|CERG Mechanism|Pillar(s)|
|---|---|---|
|Risk management is integrated into business decisions|Engineering engages at the business requirements stage - before designs are set or budgets committed. Security cost is a design input, not an afterthought.|Engineering|
|Threat intelligence informs priorities|Risk maintains a live threat intelligence function including ICS/OT-specific sources. Intelligence is distributed to Engineering (design decisions), IR (detection), and Governance (policy updates).|Risk|
|Lessons learned drive improvement|Post-incident reviews, penetration test retrospectives, and audit findings are tracked in the Governance risk register with assigned owners and improvement actions.|Governance, Risk|
|Risk appetite is defined and applied consistently|Governance maintains a documented risk appetite and tolerance framework. The "yes, and..." model applies this consistently across all risk treatment decisions.|Governance|
|Continuous improvement of the security program|Governance conducts periodic QA reviews of Engineering and Risk outputs. The CISO reviews CERG performance metrics quarterly.|Governance, All|
|Cybersecurity is viewed as a value driver|Engineering's consulting model and "yes, and..." Governance orientation build organizational trust. The business experiences security as an enabler, not an obstacle.|All|
|Cross-pillar knowledge transfer prevents single points of failure|CERG roles are designed with deliberate left-right knowledge sharing. Engineers learn Risk thinking; Risk analysts understand Governance requirements; Governance understands operational constraints.|All|

### 8.3 [CSF](https://www.nist.gov/cyberframework) Core Function Coverage

The [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) Core consists of six functions. CERG provides primary or strong supporting ownership for all six.

|[CSF](https://www.nist.gov/cyberframework) Function|Primary Owner|CERG Coverage|
|---|---|---|
|**GOVERN**|Governance|Governance owns the risk strategy, policy, roles, and accountability structures. Risk contributes risk appetite data. Engineering ensures operational compliance.|
|**IDENTIFY**|Risk + Engineering|Risk owns asset, risk, and improvement identification. Engineering contributes asset documentation through project handoffs.|
|**PROTECT**|Engineering|Engineering designs and implements protective controls. Governance sets the standard. Risk validates effectiveness through vuln management.|
|**DETECT**|Risk + IR (adjacent)|Risk owns vuln and threat detection. Incident Response owns event detection and SOC. Risk feeds intelligence to IR.|
|**RESPOND**|IR (adjacent) + Governance|IR leads response execution. Governance owns the playbook library and post-incident documentation. Risk provides threat context during incidents.|
|**RECOVER**|IR (adjacent) + Governance|IR leads recovery. Governance manages lessons-learned documentation and improvement tracking. Engineering supports system restoration where architectural changes are needed.|

---

## 8. Regulatory Alignment

### 9.1 NERC-CIP

NERC-CIP is the primary regulatory framework for bulk electric system (BES) cybersecurity. For an electrical utility, NERC-CIP requirements are non-negotiable and carry significant enforcement risk.

|CIP Standard|CERG Ownership and Application|
|---|---|
|**CIP-002:** BES Cyber System Categorization|Governance leads the annual categorization process. Engineering provides technical input on system connectivity and function. Risk validates the asset inventory.|
|**CIP-003:** Security Management Controls|Governance owns all CIP-003 policies and senior manager approval processes. Risk provides threat context for policy updates.|
|**CIP-004:** Personnel & Training|Governance sets training requirements and coordinates with the Security Awareness team for delivery. Engineering and Risk fulfill their own training obligations.|
|**CIP-005:** Electronic Security Perimeters|Engineering designs and implements ESPs and EAPs. Governance maintains ESP documentation. Risk validates perimeter integrity through scanning.|
|**CIP-006:** Physical Security|Governance maintains physical security policy. Engineering reviews physical security requirements for new OT deployments.|
|**CIP-007:** Systems Security Management|Risk owns patch management tracking and vulnerability assessment. Engineering implements port/service controls during deployment. Governance tracks compliance.|
|**CIP-010:** Configuration Management & Vuln Assessments|Engineering produces and maintains configuration baselines. Risk performs CIP-010 annual vulnerability assessments. Governance retains assessment records.|
|**CIP-011:** Information Protection|Governance defines BES Cyber System Information (BCSI) handling requirements. Engineering implements technical protections. Risk validates through scanning.|
|**CIP-013:** Supply Chain Risk Management|Risk leads vendor risk assessment. Governance maintains the supply chain risk management plan. Engineering applies controls to vendor-supplied systems.|
|**CIP-014:** Physical Security (Transmission)|Governance maintains risk assessment documentation. Engineering consults on physical-cyber interdependencies.|

### 9.2 [CMMC](https://dodcio.defense.gov/CMMC/): Cybersecurity Maturity Model Certification

[CMMC](https://dodcio.defense.gov/CMMC/) Level 2 requires implementation and assessment of all 110 practices in [NIST SP 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final). For organizations handling Controlled Unclassified Information (CUI) on behalf of the federal government, [CMMC](https://dodcio.defense.gov/CMMC/) certification is a contract requirement. CERG provides the operational backbone for [CMMC](https://dodcio.defense.gov/CMMC/) compliance.

- **Engineering** implements the technical controls across the 14 [CMMC](https://dodcio.defense.gov/CMMC/) domains, access control, configuration management, system and communications protection, and others, during project delivery
- **Risk** performs the periodic assessments required by [CMMC](https://dodcio.defense.gov/CMMC/) practice CA.2.157 and manages the Plan of Action & Milestones (POA&M) for open findings
- **Governance** maintains the System Security Plan (SSP), manages the evidence library, coordinates C3PAO assessment logistics, and tracks POA&M items to closure

### 9.3 [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)

For organizations subject to [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC requirements, CERG provides the structural foundation for compliance without requiring a separate compliance team.

- **[SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC:** Governance owns the IT General Controls framework and evidence library. Engineering ensures change management controls are embedded in deployment processes. Risk monitors access and configuration integrity in financial systems.

> **The Regulatory Advantage of CERG**
> 
> Organizations with multiple regulatory obligations, a utility managing NERC-CIP, [CMMC](https://dodcio.defense.gov/CMMC/), and [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) simultaneously, typically struggle with duplicated effort and conflicting timelines. CERG centralizes the regulatory function in Governance while ensuring that Engineering and Risk produce compliance evidence as a byproduct of their daily work, not as a separate compliance exercise. One team, one evidence library, one compliance posture.

---

## 9. IT/OT Considerations

### 10.1 The Air-Gapped Starting Point

Most organizations with OT environments today maintain a degree of air-gap separation between their operational technology networks and enterprise IT. For an electrical utility, this typically means:

- SCADA systems, energy management systems (EMS), and substation automation on isolated OT networks
- Historian servers in a DMZ acting as the data bridge between OT and IT
- Jump servers or data diodes controlling any permitted data flows
- Physical controls limiting access to OT environments

CERG is designed to operate in this context. The air-gap is a security control, Governance documents it, Risk validates it, and Engineering designs to preserve it while enabling the operational visibility the business needs.

### 10.2 The Modernization Pressure

The push to modernize OT infrastructure is real. Utilities are evaluating advanced metering infrastructure (AMI), remote monitoring, predictive maintenance, and grid modernization initiatives that all require some level of IT/OT integration. CERG's role is to ensure that modernization happens securely, not to prevent it.

> **Engineering's Role in IT/OT Convergence**
> 
> When the business initiates an IT/OT convergence project, Engineering must be engaged before the vendor is selected and before the architecture is set. The engineering team reviews whether the proposed integration can be achieved while maintaining the electronic security perimeters required by CIP-005, the configuration management discipline required by CIP-010, and the segmentation required to limit the blast radius of a cyber event in either direction. This is far more effective and far less expensive than retrofitting security after the system is installed.

### 10.3 OT-Specific Risk Considerations

The Risk team's approach to OT environments differs from IT in several important ways:

- **Scanning must be OT-safe:** active network scanning of OT environments can disrupt control processes. Risk uses passive monitoring, vendor-provided scan tools, and approved active scanning windows coordinated with OT operations.
- **Patch windows are constrained:** OT systems often cannot be patched on standard IT timelines due to vendor testing requirements, operational windows, and redundancy limitations. Risk tracks OT patch compliance separately and initiates NERC-CIP deviation processes when SLAs cannot be met.
- **Availability is the primary objective:** in OT environments, availability often outranks confidentiality in the risk calculus. Risk team members must understand this trade-off and communicate findings in terms of operational impact, not just CVSS scores.
- **Threat intelligence must include ICS-specific sources:** Risk maintains subscriptions to ICS-CERT advisories, E-ISAC threat intelligence, and vendor-specific security bulletins for all OT platforms in use.

### 10.4 Governance in OT Environments

NERC-CIP creates a distinct compliance obligation for BES Cyber Systems that sits alongside, and sometimes in tension with, broader IT governance. Governance manages this by:

- Maintaining separate but linked policy structures for IT and OT, common principles, tailored implementation requirements
- Tracking CIP-002 categorized assets separately in the risk and compliance registers with their specific regulatory requirements
- Managing NERC-CIP deviation and mitigation plan processes as a distinct workflow with defined escalation paths to the CISO and, where required, regulatory notification
- Coordinating with the reliability operations team to ensure that security controls and compliance actions do not inadvertently introduce reliability risk

---

## 10. Team Structure and Talent Model

### 11.1 Illustrative Team Structure

The illustrative organization for this framework is a large enterprise with several thousand employees and a substantial contractor workforce. The total protected population — identities, devices, and access relationships — approaches 28,000. CERG for this organization is a 60-person team reporting to the CISO, operating alongside Security Awareness and Incident Response.

This is an intentionally large example. The goal is to show what CERG looks like at full scale, with real operational velocity and complexity, so that teams of any size can see the complete model and trim to fit their environment. A 6-person CERG running this framework looks different in headcount, not in structure.

At this scale, the workload is substantial across all three pillars. Engineering carries approximately 125 active project engagements per year with roughly 40 running concurrently, spanning infrastructure, enterprise applications, cloud migrations, and third-party integrations. Engineers are aligned to specific business verticals and develop fluency in the systems they support, not just the security controls that apply to them.

Risk operates at equivalent velocity. The vendor risk program may cover thousands of active vendors and an extended workforce of remote contractors. Exposure management may span 100,000+ assets across enterprise IT, OT networks, and cloud environments. Penetration testing and red team operations run on continuous cycles. Threat intelligence is a production function producing actionable intelligence distributed to Engineering, Incident Response, and leadership.

Governance operates as a domain-expert function. Subject matter experts carry deep technical knowledge — network security, identity and access management, cloud security, OT/ICS security, cryptography — and translate expertise into implementation guidance that engineering and operations teams use. The compliance portfolio may span multiple regulatory frameworks simultaneously. The evidence library is a living system, not a pre-audit scramble. The policy and standards catalog is actively maintained, version-controlled, and tied to regulatory citation.

A representative staffing structure for a CERG of this scale:

|Role|Pillar|Key Responsibilities|
|---|---|---|
|CISO|Executive|Strategy, CERG leadership, board and executive reporting, regulatory escalation, budget authority|
|Engineering Pillar Leader|Engineering|Engagement portfolio oversight; vertical alignment model; OT/IT convergence program lead; senior architecture decisions; team development|
|Senior Cyber Engineer - OT/ICS (×3)|Engineering|Generation, transmission, and distribution vertical leads; SCADA and substation security architecture; CIP-005/CIP-010 design consultation; OT modernization advisory|
|Senior Cyber Engineer - IT/Cloud (×3)|Engineering|Enterprise IT and cloud vertical leads; application and infrastructure security architecture; identity and access design; pre-production assessment leadership|
|Cyber Engineer (×8)|Engineering|Project-level security consultation across assigned verticals; pre-production coordination with Risk; vendor solution review; risk treatment plan drafting; handoff documentation|
|Risk Pillar Leader|Risk|Program ownership across vuln management, pen testing, threat intel, and vendor risk; OT risk strategy; executive risk reporting|
|Senior Risk Analyst - Exposure Management (×3)|Risk|Enterprise vuln scan operations; OT-safe scanning program; finding prioritization and triage; SLA tracking and escalation; remediation verification|
|Threat Intelligence Analyst (×2)|Risk|Threat actor tracking; ICS/OT-specific intelligence production; E-ISAC and ICS-CERT liaison; intelligence distribution to Engineering and IR|
|Senior Risk Analyst - Vendor & Third-Party Risk (×2)|Risk|Vendor security assessment program; contractor access risk; contract redline support; supply chain risk reporting|
|Risk Analyst - Penetration Testing & Red Team (×3)|Risk|Internal pen test execution; external red team coordination; OT adversarial testing; findings documentation and tracking|
|Risk Analyst (×5)|Risk|Day-to-day vuln tracking and owner follow-up; vendor assessment support; threat feed monitoring; finding remediation documentation|
|Governance Pillar Leader|Governance|Policy and standard ownership; NERC-CIP compliance program leadership; regulatory and audit liaison; risk register governance; Governance team development|
|NERC-CIP Compliance Manager (×3)|Governance|BES Cyber System compliance; CIP deviation and mitigation management; NERC-CIP evidence library; regulatory exam coordination; reliability-security interface|
|Senior Governance Analyst - Technical Domains (×4)|Governance|Domain SME coverage across network security, IAM, cloud, and cryptography; implementation guidance production; standard development; Engineering QA reviews|
|CMMC / Federal Compliance Manager (×3)|Governance|[CMMC](https://dodcio.defense.gov/CMMC/) SSP and POA&M management; 800-171 control tracking; C3PAO coordination; federal contract compliance calendar|
|Governance / Compliance Analyst - Commercial Frameworks (×3)|Governance|and [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC compliance; external audit coordination; evidence collection and library management; compliance calendar|
|Policy & Standards Manager (×3)|Governance|Policy and procedure documentation; version control and review cycles; cross-pillar QA reviews; training content support for Security Awareness|

This distributes the 60-person team across approximately 14 Engineering staff, 15 Risk staff, and 13 Governance staff, with the CISO and pillar managers rounding out the team. The specific allocation will shift based on organizational priorities: a cloud migration program will weight Engineering more heavily; a regulatory audit cycle will weight Governance.

> **Scaling the Model**
> 
> Most organizations will run a smaller CERG than this example, and that is by design. A municipal utility with a 6-person cyber team might place 2 engineers, 2 risk analysts, and 2 governance analysts in CERG, with each person carrying the full scope of their pillar. A regional cooperative with a single cybersecurity hire might have that person operate across all three pillars with the CISO providing strategic direction. The framework is the same at every size. The roles compress; the responsibilities do not disappear, they concentrate. Understanding the full-scale model helps smaller teams identify what they are covering, what they are deferring, and where they need to prioritize as they grow.

### 11.2 The Left-Right Knowledge Model

One of CERG's explicit design goals is talent resilience, the ability to absorb the loss of any single team member without stopping work. The mechanism for achieving this is deliberate left-right knowledge sharing within and across pillars.

- Within each pillar, team members document their work in a shared and accessible way, not as bureaucratic overhead but as operational artifacts that others can follow
- Governance's policies and standards serve as the knowledge base for Engineering and Risk, new arrivals can orient themselves by reading what Governance has documented
- Risk's vulnerability reports and threat intelligence give Engineering context for why certain design decisions matter
- Engineering's architecture and handoff documents give Risk a current map of what is in the environment and how it is configured

In practice, this means that a new Cyber Engineer can learn the organization's standards from Governance, understand the current threat environment from Risk, and have context for every major system from Engineering's project documentation. Onboarding accelerates. Knowledge is in the system, not in someone's head.

### 11.3 CERG and the Adjacent Teams

|Interaction|Description|
|---|---|
|CERG → Security Awareness|Governance provides policy and procedure content for awareness training. Risk provides threat intelligence for targeted awareness campaigns (e.g., spear-phishing scenarios relevant to ICS/OT). Engineering feeds real-world examples from project work into training scenarios.|
|CERG → Incident Response|Risk provides threat intelligence and vulnerability context during incidents. Engineering provides architecture and configuration documentation to support containment and recovery. Governance provides playbooks and manages post-incident documentation.|
|Security Awareness → CERG|Awareness provides metrics on training completion and phishing simulation results - inputs for Governance's compliance tracking and risk register.|
|Incident Response → CERG|IR provides post-incident findings and lessons learned - inputs for Risk (threat landscape updates), Engineering (architectural improvements), and Governance (policy and playbook updates).|

---

## 11. Getting Started: The Path to Adaptive

### 12.1 Phase 1: Establish (Months 1–3)

The first priority is standing up the CERG structure and establishing the baseline work products each pillar needs to function.

- **Engineering:** Document the active project portfolio. Identify any in-flight projects that should receive a retroactive engineering review. Establish the lightweight intake process.
- **Risk:** Stand up or audit the exposure management program. Ensure IT and OT environments are covered with appropriate scanning approaches. Inventory threat intelligence feeds.
- **Governance:** Conduct a policy gap assessment against [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) and applicable regulatory frameworks. Identify the three to five most critical missing or out-of-date policies. Build or inherit the risk register.

### 12.2 Phase 2: Operate (Months 4–9)

With the structure in place, the focus shifts to operating CERG as a team and building the cross-pillar working rhythms.

- Establish a regular CERG operating cadence, weekly pillar syncs, monthly cross-pillar review, quarterly CISO briefing
- Engineering begins processing the project intake queue and building the first round of handoff documentation
- Risk begins producing regular vulnerability reports with prioritized findings and tracking remediation to SLA
- Governance completes the first compliance self-assessment against NERC-CIP and [CMMC](https://dodcio.defense.gov/CMMC/); begins building the evidence library
- All pillars begin practicing the "yes, and..." model on real business requests

### 12.3 Phase 3: Mature (Months 10–18)

The CERG model begins demonstrating Repeatable behavior. The path to Adaptive requires building the continuous improvement and integration functions.

- Risk begins producing structured threat intelligence reports distributed to Engineering, IR, and leadership
- Governance launches a formal QA cycle, quarterly reviews of Engineering and Risk work products against defined standards
- Engineering demonstrates consistent early engagement on projects, present at business requirements stage, not called in at go-live
- First external validation: coordinate a NERC-CIP compliance audit or [CMMC](https://dodcio.defense.gov/CMMC/) readiness assessment to measure progress and identify gaps
- Begin building the metrics program, vulnerability SLA adherence, time-to-engage on new projects, evidence collection completeness, policy currency

### 12.4 Adaptive Indicators

An organization operating at Adaptive maturity will demonstrate these observable behaviors:

- The security team is engaged in business planning conversations before projects are funded, not after they are designed
- Threat intelligence from Risk actively changes Engineering design decisions and Governance policy priorities
- When a significant vulnerability or threat emerges, the organization has a clear, practiced process for assessing impact, communicating status, and executing response, within hours, not days
- External auditors and regulators find organized, complete, and timely evidence, because evidence collection is a byproduct of daily work, not a pre-audit scramble
- New team members become productive faster because the CERG knowledge base, policies, standards, architecture documents, risk reports, is current, accessible, and well-organized
- The CISO can credibly report the organization's risk posture to the board using data from the risk register and compliance program, not gut feel

---

## 12. Compliance as Exhaust — Evidence Factories

Regulatory alignment is a byproduct of running the program well. Evidence is produced once, from operational work, then reused across frameworks. These "evidence factories" show the mapping: Capabilities declare what the program can do; evidence factories produce the independently verifiable proof; compliance consumers reuse that proof across regulators without re-work.

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
| **Version** | 1.21 |
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
|| 1.22 | 2026-06-23 | CISO + Cyber Governance | Added capability taxonomy (§3), capability reference set, maturity grading, and evidence-factory linkage. |
|---|---|---|---|
| 1.0 | 2026-05-01 | CISO + Cyber Governance | Initial release. Narrative description of the CERG framework, pillars, and operating model. |
| 1.21 | 2026-05-22 | Cyber Governance | Updated framework references and pillar descriptions. |

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
