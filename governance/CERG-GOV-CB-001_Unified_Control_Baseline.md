## UNIFIED CONTROL BASELINE
### Organizational Baseline · Overlay Matrix · Implementation, Evidence, and Inheritance Model

---

| | |
|---|---|
| **Document ID** | CERG-GOV-CB-001 |
| **Version** | 2.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Control Baseline) |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Standards** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) · [CERG-STD-OT-001](../standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) · [CERG-STD-CUI-001](../standards/CERG-STD-CUI-001_CUI_Handling_Standard.md) · [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) · [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) · [CERG-STD-LM-001](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) · [CERG-STD-RES-001](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) · [CERG-STD-CR-001](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) · [CERG-STD-AI-001](../standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md) |
| **Review Cycle** | Annual - and on framework version change ([NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) rev, [CMMC](https://dodcio.defense.gov/CMMC/) rev, NERC-CIP version, AI governance framework change) |
| **Frameworks** | [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST 800-171r3](https://csrc.nist.gov/pubs/sp/800/171/r3/final) · [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) · CIS Controls v8 · ISO/IEC 27001 A.5–A.8 · CSA CCM v4 · NIST AI RMF 100-1 · ISO/IEC 42001 |
| **Regulations** | NERC-CIP v7 (and CIP-015 draft) · [CMMC L2](https://dodcio.defense.gov/CMMC/) · [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC |
| **Environments** | All in-scope assets - owned, hybrid, cloud, SaaS, OT, CUI, AI-enabled systems |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Design Principles](#2-design-principles)
3. [The CERG Control Family Spine](#3-the-cerg-control-family-spine)
4. [Implementation Statuses](#4-implementation-statuses)
5. [Inheritance Model](#5-inheritance-model)
6. [Organizational Baseline (Core)](#6-organizational-baseline-core)
7. [Control Status Decision Tree](#7-control-status-decision-tree)
8. [Overlay Matrix](#8-overlay-matrix)
9. [Control-to-Evidence Mapping](#9-control-to-evidence-mapping)
10. [Regulatory Crosswalks](#10-regulatory-crosswalks)
11. [Governance, Change, and Versioning](#11-governance-change-and-versioning)
12. [Document Control](#12-document-control)

---

## 1. Purpose and Scope

The Unified Control Baseline turns the principles in [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md), the requirements in subordinate standards, and the philosophy in the [CERG Risk Management Framework](CERG-GOV-RMF-001_Risk_Management_Framework.md) into an implementation-ready control set. It is the document a control owner, an internal auditor, a [CMMC](https://dodcio.defense.gov/CMMC/) C3PAO, a NERC-CIP auditor, or a [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) auditor opens first.

It applies to every in-scope asset and every CERG-owned control. Where a subordinate standard imposes a more specific requirement, the standard controls and is referenced from the relevant entry here.

> **One Baseline, Many Audiences**
>
> Most programs maintain a separate control library per regulator, one for NIST, one for [CMMC](https://dodcio.defense.gov/CMMC/), one for NERC-CIP, one for [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204), and then spend a quarter of every audit reconciling them. CERG inverts that: one baseline is implemented once and evidenced once. The crosswalks in Section 9 translate the same evidence into the language each regulator expects.

---

## 2. Design Principles

The baseline is built on five non-negotiable principles. Anything that violates them is not in the baseline.

1. **NIST is the spine.** [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) control families are the organizing structure. CERG-native controls are layered onto that spine, never the reverse. When a NIST family fully covers an intent, CERG inherits the NIST language and identifier rather than coining a new one.
2. **Each control has one accountable CERG pillar.** Engineering, Risk, or Governance, never "shared." Supporting roles are listed separately. Accountability without ambiguity is the prerequisite to evidence.
3. **Each control has named evidence.** A control without a named evidence artifact is a control without proof; it does not enter the baseline.
4. **Overlays add, they do not redefine.** CUI, BES, [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204), and Safety overlays add controls or tighten parameters of base controls. They never silently relax the base.
5. **Inheritance is documented or it does not exist.** Inheritance from cloud/SaaS providers requires the artifact named in Section 5. "We assume the provider handles it" is not inheritance.

---

## 3. The CERG Control Family Spine

CERG uses [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) control families as the top-level grouping. Each family has a one-line CERG intent and a primary owning pillar.

| **Family** | **NIST Code** | **CERG Intent (one line)** | **Primary Owner** |
|---|---|---|---|
| Access Control | AC | Identity-bound, least-privilege access enforced consistently across IT, cloud, SaaS, OT, and CUI. | Engineering |
| Awareness and Training | AT | Role-relevant security training; CERG defines the cyber content, Awareness function delivers. | Governance (content) |
| Audit and Accountability | AU | Log every consequential action; protect, retain, and review the logs. | Risk (detection) |
| Assessment, Authorization, and Monitoring | CA | Continuous, evidence-driven assurance that controls operate as intended. | Governance |
| Configuration Management | CM | Approved baselines, change control, and drift detection across every platform. | Engineering |
| Contingency Planning | CP | Cyber recovery and backup that survive ransomware, region failure, and OT event. | Engineering (cyber side) |
| Identification and Authentication | IA | Strong, phishing-resistant identity for humans and machines. | Engineering |
| Incident Response | IR | CERG-side requirements that IR depends on (telemetry, identity, baselines, recovery, evidence). | Risk (interface) |
| Maintenance | MA | Controlled, evidenced maintenance; tighter in OT and BES scope. | Engineering |
| Media Protection | MP | CUI and Restricted-data media handling. | Governance |
| Physical and Environmental | PE | Cyber dependency on physical controls (data center, OT, CUI work area). | Governance (interface) |
| Planning | PL | SSPs, security plans, authorization packages, architecture documentation. | Engineering / Governance |
| Personnel Security | PS | Screening and access-tied personnel controls. | Governance (interface to HR) |
| Risk Assessment | RA | Continuous risk identification, scoring, and treatment. | Risk |
| System and Services Acquisition | SA | Security in procurement, vendor risk, SBOMs, secure SDLC. | Risk (TPRM) / Engineering (SDLC) |
| System and Communications Protection | SC | Network segmentation, cryptography, OT boundary protection. | Engineering |
| System and Information Integrity | SI | Vulnerability, malware, monitoring, advisories, integrity. | Risk |
| Supply Chain Risk Management | SR | Software, hardware, and service supply chain integrity. | Risk (TPRM) |
| Program Management | PM | The CERG program itself - policy, metrics, board reporting. | Governance |

---

## 4. Implementation Statuses

Every control entry in the baseline carries one of the following statuses. The set is intentionally small, it survives audits in every framework CERG must support.

| **Status** | Published | **Evidence Expected** |
|---|---|---|
| `Implemented` | Control is in place, tested, and operating as designed. | Named evidence artifact for the current cycle. |
| `Partially Implemented` | Control is in place for some scope or is operating at reduced effectiveness. | Evidence of what is in place plus a POA&M entry. |
| `Inherited` | Implementation is provided by another party - cloud provider, SaaS provider, parent enterprise control, IAM team. | Inheritance Evidence Package (Section 5). |
| `Planned` | Control is planned with an owner and target date. | POA&M entry with date and owner. |
| `Risk Accepted` | Deviation is approved and tracked via [CERG-PRC-RM-001](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) Section 7. | Risk register entry, exception ID, approver. |
| `Not Applicable` | Control does not apply to this scope. | Documented N/A rationale (system type, no in-scope data, etc.). |

> **What's Not on the List**
>
> "In Progress," "Undetermined," "Working On It," and "Vendor Says Yes" are not statuses. Every entry in the baseline maps to one of the six above. Honesty about Partially Implemented and Planned is worth far more than optimism about Implemented.

---

## 5. Inheritance Model

`Inherited` is the most-abused status in cloud-era control libraries. CERG requires the following Inheritance Evidence Package for any control marked `Inherited`. Without it, the status defaults to `Not Implemented` and a finding is opened.

The package has six elements:

1. **Provider attestation**, current SOC 2 Type II / ISO 27001 / FedRAMP / PCI report containing the inherited control.
2. **Shared responsibility mapping**, the section of the provider's shared responsibility matrix that names this control as the provider's.
3. **Customer-side evidence of configuration**, proof the customer-side prerequisites are configured (e.g., logging enabled, region selected, IAM lockdown applied) that allow the inherited control to actually protect the customer's tenancy.
4. **Sub-service organization carve-outs**, explicit notation if the inherited control depends on a sub-service organization (e.g., AWS underlying Snowflake) and how that dependency is covered.
5. **Currency check**, attestation expiry date and the calendar entry that re-runs this check.
6. **Re-papering trigger**, what would cause CERG to re-evaluate inheritance (provider control failure, attestation lapse, scope change, customer-side prerequisite drift).

This package is the basis of every "we inherit it from AWS / Azure / GCP / M365 / Salesforce / ServiceNow / our [CMMC](https://dodcio.defense.gov/CMMC/) enclave provider" claim CERG makes.

---

## 6. Organizational Baseline (Core)

The organizational baseline applies to every in-scope asset. Overlays in Section 7 add or tighten controls for High-Impact, CUI, BES, [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204), and OT Safety scopes.

The full implementation-ready control set is captured by family in the sections that follow. Each entry has: Control ID · Action Statement · System Applicability · Owning Pillar · Named Evidence · Frequency · Subordinate Standard.

System Applicability uses one or more of the following values: Hardware, Software, Network, Cloud, Data, Process.

Section 6 entries below are organized by family and reference the subordinate standard for parameter detail. Where parameter detail differs by environment (IT/cloud/SaaS, OT, CUI), the subordinate standard is authoritative; the baseline names the control once.

### 6.1 Access Control (AC)

| **Control**                      | **Statement**                                                                                                                                                                                                   | **System Applicability**                          | **Owner**   | **Evidence**                      | **Min Freq**           | **Std**                 |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | ----------- | --------------------------------- | ---------------------- | ----------------------- |
| AC-3 Access Enforcement          | Make sure your system uses approved authentication and authorization controls for all access, and that local, shared, hard-coded, or static credentials cannot bypass them.                                     | Hardware, Software, Network, Cloud, Data          | Engineering | IdP/PAM policy export             | Annual                 | STD-AC-001              |
| AC-7 Unsuccessful Logon Attempts | Configure failed-login thresholds, lockouts, and identity-attack alerts according to STD-AC-001 and verify they are operating.                                                                                  | Hardware, Software, Network, Cloud                | Engineering | IdP policy export, detection rule | Annual                 | STD-AC-001 / STD-LM-001 |
| AC-19 Mobile / BYOD              | Allow mobile or BYOD access only when the device is enrolled, compliant, and approved by conditional-access policy.                                                                                             | Hardware                                          | Engineering | MDM compliance report             | Quarterly              | STD-AC-001              |
| AC-20 Account Provisioning         | Verify every account has an approved request, named owner, defined access level, and current JML record    | Hardware, Software, Network, Cloud, Data, Process | Engineering | JML log, quarterly recert report  | Continuous / Quarterly | STD-AC-001              |
| AC-21 Account Management         | Revoke access or privileges when roles change or access is no longer required    | Hardware, Software, Network, Cloud, Data, Process | Engineering | JML log, quarterly recert report  | Continuous / Quarterly | STD-AC-001              |
| AC-22 Least Privilege             | Grant users, administrators, services, and vendors only the access needed for their role                                     | Hardware, Software, Network, Cloud, Data, Process | Engineering | PAM session logs, role inventory  | Quarterly              | STD-AC-001              |
| AC-23 Priveleged Accounts          | Enforce time-bounded and/or just-in-time access for priveleged accounts and record sessions where technically feasible                                    | Hardware, Software, Network, Cloud, Data, Process | Engineering | PAM session logs, role inventory  | Quarterly              | STD-AC-001              |
| AC-24 Remote Access              | Prohibit all remote access unless access is through approved gateways with MFA and session logging enabled    | Network, Cloud                                    | Engineering | Gateway logs, MFA policy export   | Continuous             | STD-AC-001              |


### 6.2 Audit and Accountability (AU)

| **Control**                          | **Statement**                                                                                                                                                               | **System Applicability**                          | **Owner** | **Evidence**                                    | **Min Freq** | **Std**    |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | --------- | ----------------------------------------------- | ------------ | ---------- |
| AU-2 Event Logging                   | Log security, administrative, and authentication actions and any other relevant activity logs in a centralized SIEM or approved OT one-way collection point.                       | Hardware, Software, Network, Cloud, Data          | Risk      | SIEM source inventory, gap report               | Monthly      | STD-LM-001 |
| AU-6 Audit Review                    | Review and respond to alerts generated from your system logs                                                       | Hardware, Software, Network, Cloud, Data, Process | Risk      | Detection coverage report, triage queue metrics | Continuous   | STD-LM-001 |
| AU-9 Protection of Audit Information | Protect your system's audit logs from alteration or deletion and log all administrative changes to logging.                                             | Software, Cloud, Data, Process                    | Risk      | Storage policy, admin-action review             | Quarterly    | STD-LM-001 |
| AU-11 Audit Record Retention         | Retain audit records for the required retention period, including 13 months hot / 7 years cold by default and BES minimums when applicable | Hardware, Software, Network, Cloud, Data, Process | Risk      | Retention policy, sample retrieval              | Annual       | STD-LM-001 |
| AU-12 Audit Record Generation        | Generate required security, administrative, authentication, and privileged-activity audit records. | Hardware, Software, Network, Cloud, Data          | Risk      | Log generation configuration | Annual       | STD-LM-001 |
| AU-13 Audit Record Generation        | Test required records for retrievability and parsibility prior to system commissioning and annually thereafter        | Risk      | Log generation configuration, sample event test, sample retrieval | Annual       | STD-LM-001 |

### 6.3 Configuration Management (CM)

| **Control**                     | **Statement**                                                                                                                                                                                         | **System Applicability**                          | **Owner**          | **Evidence**                               | **Min Freq** | **Std**                 |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | ------------------ | ------------------------------------------ | ------------ | ----------------------- |
| CM-2 Baseline Configuration     | Apply the correct DISH baseline for your platform class and keep evidence showing the baseline was applied.                                                                                           | Hardware, Software, Network, Cloud                | Engineering        | DISH baseline catalog, scan report         | Continuous   | STD-CFG-001             |
| CM-3 Change Control             | Submit production changes through change management before implementation and include security review when required.                                                                                  | Hardware, Software, Network, Cloud, Data, Process | Engineering        | CAB minutes, change records                | Continuous   | STD-IT-001 / STD-OT-001 |
| CM-5 Access Restrictions for Change | Restrict who can make production changes or modify approved baselines; review elevated change authority and emergency-change use for appropriateness.                                                  | Hardware, Software, Network, Cloud, Data, Process | Engineering        | Change-authority roster, emergency-change review | Quarterly | STD-CFG-001 / PRC-CHG-001 |
| CM-6 Configuration Settings     | Create and confirm a system baseline so cyber can detect and remediate drift; document and route exceptions through Section 4.                                                                        | Hardware, Software, Network, Cloud                | Engineering        | Drift report, exception register           | Continuous   | STD-CFG-001             |
| CM-7 Least Functionality        | Disable unnecessary services and ports, and make sure only approved software is installed.                                                                                                            | Hardware, Software, Network, Cloud                | Engineering        | App allowlist, port scan report            | Quarterly    | STD-CFG-001             |
| CM-8 System Component Inventory | Make sure your hardware, software, cloud resources, network devices, data stores, and process owners are recorded in the correct CMDB or authoritative inventory with all applicable fields complete. | Hardware, Software, Network, Cloud, Data, Process | Engineering / Risk | Asset inventory export, reconciliation log | Monthly      | STD-IT-001 / STD-OT-001 |

### 6.4 Contingency Planning (CP)

| **Control**                       | **Statement**                                                                                                                                            | **System Applicability**                          | **Owner**   | **Evidence**                                 | **Min Freq**                | **Std**     |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | ----------- | -------------------------------------------- | --------------------------- | ----------- |
| CP-2 Contingency Plan             | Make sure your system has a current cyber recovery plan mapped to its tier and coordinated with enterprise BCP requirements.                             | Hardware, Software, Network, Cloud, Data, Process | Engineering | Plan document, BCP interface record          | Annual                      | STD-RES-001 |
| CP-4 Contingency Plan Testing     | Test the recovery plan on the required cadence, document lessons learned, and update RTO/RPO assumptions when results show gaps.                         | Hardware, Software, Network, Cloud, Data, Process | Engineering | Test report, lessons learned, register entry | Annual / BES Annual         | STD-RES-001 |
| CP-9 System Backup                | Make sure backups for your system and data are immutable, isolated, and restorable; for OT, include configurations, firmware, logic, and historian data. | Hardware, Software, Network, Cloud, Data          | Engineering | Backup report, immutability evidence         | Continuous / Annual restore | STD-RES-001 |
| CP-10 Information System Recovery | Run recovery tests that prove your system can meet its defined RTO and RPO, and retain restoration evidence.                                             | Hardware, Software, Network, Cloud, Data, Process | Engineering | Restoration test evidence                    | Annual                      | STD-RES-001 |

### 6.5 Identification and Authentication (IA)

| **Control**                                                   | **Statement**                                                                                                                                           | **System Applicability**                          | **Owner**   | **Evidence**                    | **Min Freq** | **Std**                 |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | ----------- | ------------------------------- | ------------ | ----------------------- |
| IA-2 Identification and Authentication (Organizational Users) | Make sure all interactive human access to your system requires phishing-resistant MFA and does not allow legacy authentication.                         | Hardware, Software, Network, Cloud, Data          | Engineering | IdP policy, exception register  | Quarterly    | STD-AC-001              |
| IA-3 Device Identification and Authentication                 | Make sure your system, device, or service presents the identifiers needed for IdP, NAC, CAP, or other network controls to recognize it where supported. | Hardware, Network, Cloud                          | Engineering | NAC / conditional-access policy | Annual       | STD-AC-001              |
| IA-5 Authenticator Management                                 | Store and rotate credentials, secrets, API keys, and certificates in approved tools and follow the STD-CR-001 lifecycle.                                | Hardware, Software, Network, Cloud, Data, Process | Engineering | Secrets manager, cert inventory | Continuous   | STD-CR-001 / STD-AC-001 |

### 6.6 Risk Assessment, System and Information Integrity, Supply Chain (RA / SI / SR)

| **Control**                                | **Statement**                                                                                                                                                                                                  | **System Applicability**                          | **Owner**          | **Evidence**                              | **Min Freq** | **Std**                  |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | ------------------ | ----------------------------------------- | ------------ | ------------------------ |
| RA-3 Risk Assessment                       | Identify risks for your system, data, or process; document impact and likelihood; assign treatment; and keep the risk register current.                                                                        | Hardware, Software, Network, Cloud, Data, Process | Risk / Governance  | Risk register                             | Continuous   | PRC-RM-001               |
| RA-5 Vulnerability Monitoring and Scanning | Make sure your system is assessed on the required cadence using authenticated scanning and the applicable DISH profile, or an approved passive/alternative method where active scanning is not allowed.        | Hardware, Software, Network, Cloud                | Risk               | Scan reports, SLA dashboard               | Continuous   | PRC-VM-001 / STD-CFG-001 |
| SI-2 Flaw Remediation                      | Remediate Critical and High findings within SLA, or document an approved exception or risk acceptance before the SLA is missed.                                                                                | Hardware, Software, Network, Cloud, Process       | Risk / Engineering | SLA report, exception register            | Continuous   | PRC-VM-001               |
| SI-4 System Monitoring                     | Make sure the required monitoring tools for your environment cover your system and that SIEM, EDR, NDR, CSPM/SSPM, or OT-passive monitoring gaps are documented.                                               | Hardware, Software, Network, Cloud, Data          | Risk               | Coverage report                           | Continuous   | STD-LM-001               |
| SR-2 Supply Chain Risk Management Plan     | Make sure each vendor or service supporting your system or process is tiered, tier-specific evidence requirements are understood, contract clauses match the tier, and required SCCT information is collected. | Hardware, Software, Network, Cloud, Data, Process | Risk (TPRM)        | TPRM register, SCCT roster                | Continuous   | PRC-TPRM-001             |
| SR-3 Supply Chain Controls and Processes   | Do not allow international access unless the country-risk exception is approved and documented.                                                                                                                | Software, Network, Cloud, Data, Process           | Risk (TPRM)        | Country-risk register, exception register | Quarterly    | PRC-TPRM-001             |

### 6.7 System and Communications Protection (SC)

| **Control** | **Statement** | **System Applicability** | **Owner** | **Evidence** | **Min Freq** | **Std** |
|---|---|---|---|---|---|---|
| SC-7 Boundary Protection | Make sure network boundaries, cloud security groups, OT ESP/EAP boundaries, and inter-zone paths are explicitly defined, approved, filtered, logged, and reviewed; direct bypass paths are prohibited. | Network, Cloud, Data, Process | Engineering | Segmentation diagram, firewall rule review, cloud security group export | Quarterly / On change | STD-NET-001 / STD-OT-001 |
| SC-8 Transmission Confidentiality and Integrity | Protect sensitive data and administrative traffic in transit with approved cryptographic protocols; prohibit cleartext protocols for Restricted, CUI, and administrative paths unless formally risk accepted. | Network, Cloud, Data | Engineering | TLS / certificate scan, exception register | Continuous / Annual | STD-CR-001 / STD-CUI-001 |
| SC-28 Protection of Information at Rest | Encrypt Restricted, CUI, backup, and crown-jewel data at rest using approved platform controls or customer-managed keys where required; document inheritance when provider encryption is used. | Hardware, Software, Cloud, Data | Engineering | Encryption configuration export, KMS key inventory, inheritance package | Quarterly | STD-CR-001 / STD-DG-001 / STD-CUI-001 |

### 6.8 Assessment, Authorization, and Monitoring (CA)

| **Control** | **Statement** | **System Applicability** | **Owner** | **Evidence** | **Min Freq** | **Std** |
|---|---|---|---|---|---|---|
| CA-2 Control Assessment | Assess implemented controls on the defined cadence using self-assessment, evidence review, and independent validation where required; record findings, owners, and remediation due dates. | Hardware, Software, Network, Cloud, Data, Process | Governance / Risk | Maturity scorecard, control test worksheet, findings register | Annual / Quarterly high-risk | GOV-MAT-001 / TMPL-AUD-001 |
| CA-8 Penetration Testing | Conduct adversarial validation for in-scope systems per risk tier; document scope, rules of engagement, findings, remediation ownership, and validation retest. | Hardware, Software, Network, Cloud, Data, Process | Risk | Test plan, findings report, retest evidence | Annual / After material change | PRC-AV-001 |

### 6.9 Awareness and Training (AT)

| **Control** | **Statement** | **System Applicability** | **Owner** | **Evidence** | **Min Freq** | **Std** |
|---|---|---|---|---|---|---|
| AT-2 Literacy Training and Awareness | Make sure workforce members with cyber-relevant access complete role-appropriate security training before access and on the required refresh cadence; track exceptions to closure. | Process, Data, Cloud, Software | Governance | Training completion report, role curriculum mapping | Annual / On role assignment | GOV-TRN-001 / GOV-ONB-001 |

### 6.10 Incident Response (IR)

| **Control** | **Statement** | **System Applicability** | **Owner** | **Evidence** | **Min Freq** | **Std** |
|---|---|---|---|---|---|---|
| IR-2 Incident Response Training | Train incident-response participants and CERG support roles on escalation, evidence handling, communications, and playbook execution before they are assigned incident duties. | Process, Data, Cloud, Network | Risk / Governance | Exercise attendance, role training completion | Annual / Per exercise | PLN-IR-001 / PRC-IR-002 |
| IR-4 Incident Handling | Triage, contain, investigate, eradicate, recover, and communicate incidents using approved playbooks while preserving evidence and recording decisions. | Hardware, Software, Network, Cloud, Data, Process | Risk | Incident case record, timeline, evidence package | Continuous | PLN-IR-001 / PRC-IR-002 |
| IR-8 Incident Response Plan | Maintain an approved incident-response plan, playbook set, contacts, severity model, and escalation path; update after exercises, material incidents, or organizational changes. | Process, Data, Cloud, Network | Risk / Governance | Approved IR plan, playbook review, after-action report | Annual / After material incident | PLN-IR-001 / PRC-IR-002 |

### 6.11 Physical and Environmental Protection (PE)

| **Control** | **Statement** | **System Applicability** | **Owner** | **Evidence** | **Min Freq** | **Std** |
|---|---|---|---|---|---|---|
| PE-2 Physical Access Authorizations | Maintain authorized physical access lists for cyber-relevant facilities, OT PSPs, and CUI work areas; grant and remove physical access through an approved workflow. | Hardware, Network, Data, Process | Governance / Engineering | Badge access roster, PSP access list | Quarterly | STD-OT-001 / PLN-CIP-001 |
| PE-3 Physical Access Control | Enforce, log, and review physical entry to cyber-relevant facilities; require visitor escort and investigate unauthorized or anomalous access attempts. | Hardware, Network, Data, Process | Governance / Engineering | Badge logs, visitor logs, PSP inspection record | Monthly / Quarterly | STD-OT-001 / PLN-CIP-001 |

### 6.12 Planning (PL)

| **Control** | **Statement** | **System Applicability** | **Owner** | **Evidence** | **Min Freq** | **Std** |
|---|---|---|---|---|---|---|
| PL-1 Policy and Procedures | Maintain the approved policy, standard, procedure, plan, and template hierarchy with named owners, review cycles, status, and change history. | Process | Governance | Document catalog, review record, approval history | Annual / On major change | GOV-CAT-001 / GOV-STY-001 |

### 6.13 Program Management (PM)

| **Control** | **Statement** | **System Applicability** | **Owner** | **Evidence** | **Min Freq** | **Std** |
|---|---|---|---|---|---|---|
| PM-1 Information Security Program Plan | Maintain the CERG operating model, program scope, accountable pillars, service commitments, and reporting model so leadership can understand how the program is run. | Process | Governance | Operating model, service commitments, board report | Quarterly | GOV-OM-001 / GOV-MTR-001 / GOV-SLC-001 |
| PM-9 Risk Management Strategy | Maintain the risk management strategy, taxonomy, appetite/tolerance guidance, and treatment workflow; ensure risk decisions are visible to accountable leadership. | Process, Data, Cloud, Network | Governance / Risk | RMF, risk taxonomy, risk register summary | Annual / Quarterly | GOV-RMF-001 / GOV-TAX-001 / PRC-RM-001 |
| PM-14 Testing, Training, and Monitoring | Maintain an integrated calendar for control tests, evidence refresh, training, assessments, reporting, and regulatory milestones; track overdue actions to closure. | Process | Governance | Annual calendar, completion tracker, compliance review minutes | Monthly / Annual planning | GOV-CAL-001 / GOV-MTR-001 |

### 6.14 Personnel Security (PS)

| **Control** | **Statement** | **System Applicability** | **Owner** | **Evidence** | **Min Freq** | **Std** |
|---|---|---|---|---|---|---|
| PS-2 Position Risk Designation | Designate role and position risk based on privileged access, CUI/BES scope, regulatory responsibility, and crown-jewel impact; verify required screening and authorization before access. | Process, Data, Cloud, Network | Governance | Role risk designation matrix, access precondition record | Annual / Before access | GOV-JA-001 / GOV-ONB-001 |

### 6.15 System and Services Acquisition (SA)

| **Control** | **Statement** | **System Applicability** | **Owner** | **Evidence** | **Min Freq** | **Std** |
|---|---|---|---|---|---|---|
| SA-9 External System Services | Make sure external systems and service providers meet documented security requirements, shared-responsibility obligations, evidence requirements, incident-notification terms, and flow-down clauses before use. | Software, Network, Cloud, Data, Process | Risk (TPRM) | Contract security clauses, vendor assessment, shared responsibility matrix | Continuous / Annual reassessment | PRC-TPRM-001 |

## 7. Control Status Decision Tree

Use this decision tree to assign honest control implementation statuses. Optimistic status inflation is the most common control failure mode — marking a control "Implemented" without evidence hides the gap from everyone, including yourself.

```
Is the control applicable to your environment?
  ├─ No  → Not Applicable (document rationale)
  └─ Yes → Is the control fully designed?
              ├─ No  → Planned (design in progress) or Not Implemented (no design)
              └─ Yes → Is it operating consistently?
                          ├─ No  → Partially Implemented (operating gap)
                          └─ Yes → Is there current evidence of operation?
                                      ├─ No  → Partially Implemented (evidence gap)
                                      └─ Yes → Implemented
```

### Status Definitions

| Status | Definition | When to Use |
|--------|-----------|-------------|
| **Not Applicable** | The control does not apply to your environment. | Document the rationale. Example: "OT-specific controls are not applicable — no OT environment exists." |
| **Not Implemented** | No design exists. The control is not in place. | Be honest. A gap you acknowledge is manageable. A gap you hide is not. |
| **Planned** | Design exists or is in progress. Not yet operating. | Use when there is a committed implementation plan with a target date and owner. |
| **Partially Implemented** | Designed and operating, but with gaps. | Specify the gap: evidence missing, inconsistent operation, incomplete scope, or inherited without verification. |
| **Implemented** | Designed, operating, and evidenced. | Evidence must meet the tier required for this control (E2 minimum per AUD-001). |
| **Inherited** | Relies on a provider, partner, or parent organization. | Requires provider evidence (SOC 2, ISO cert, etc.) AND organization-side complementary controls. See §7.1. |

### 7.1 Control Inheritance and Shared Responsibility

Cloud, SaaS, MSP, and OT vendor relationships create shared control environments. "Inherited" is not a free pass — it requires provider evidence AND your own complementary controls.

| Responsibility | Who Does What | Evidence Required |
|---------------|--------------|-------------------|
| **Provider-Only** | The provider is fully responsible. The customer cannot influence the control. | Provider attestation (SOC 2, ISO 27001, FedRAMP). Customer verifies scope covers their environment. |
| **Customer-Only** | The customer is fully responsible. The provider has no role. | Customer-produced evidence per this standard. |
| **Shared** | Both provider and customer have responsibilities. Failure by either party constitutes a control gap. | Provider evidence + customer evidence for customer-side controls. Document the shared responsibility matrix. |

#### Inheritance Examples

| Scenario | Inherited? | What You Still Need |
|----------|-----------|---------------------|
| Physical security of cloud data center | Yes — provider attestation acceptable | Confirm data center scope covers your region. SOC 2 physical security control testing. |
| Logging for SaaS application | No — platform logging capability is inherited, but you must configure, collect, and monitor | Enable audit logging in the SaaS app. Configure log export to your SIEM. Verify logs are flowing. |
| MFA for SaaS application | Maybe — if IdP enforces and app trusts IdP | Verify IdP policy enforces MFA. Verify app is configured to require IdP authentication. Check for bypass paths (local accounts, API keys). |
| Backup for SaaS data | Maybe — platform availability backup is inherited, but customer-level recovery may not be | Review SaaS provider's backup SLA. Export critical data to customer-controlled backup. Test restore. |
| Encryption at rest for cloud storage | Maybe — provider manages infrastructure encryption, but key ownership and configuration vary | Confirm encryption is enabled. Determine who controls the keys. If provider-managed, document the shared responsibility. |
| Patch management for PaaS | Yes — provider patches the platform | Verify the PaaS SLA covers patching. Monitor for CVEs in the platform. Plan for migration if the provider's patch SLA is insufficient. |
| OT vendor remote access | No — you control the access path and monitoring | Require MFA. Log all sessions. Approve access per session. Disable when not in use. The vendor's security posture is an input, not a substitute. |

#### Shared Responsibility Decision Table

For every control that crosses an organizational boundary, complete this table and retain it with the control evidence:

| Field | Value |
|-------|-------|
| Control ID | [From CB-001] |
| Provider/Vendor | [Name] |
| Provider Responsibility | [What the provider does] |
| Provider Evidence | [SOC 2 report reference, contract clause, architecture doc] |
| Customer Responsibility | [What you must do] |
| Customer Evidence | [Your evidence of customer-side controls] |
| Residual Risk If Provider Evidence Is Unavailable | [What risk remains] |
| Reviewed By | [Name] |
| Review Date | [Date] |

#### Provider Evidence Gap Workflow

When provider attestation is missing, expired, or does not cover the customer's scope, follow this workflow:

| Step | Action | Owner | Output | SLA |
|------|--------|-------|--------|-----|
| 1. **Document the gap** | Describe what evidence is missing: control ID, provider, date expected vs. received, scope gap. | Control Owner / Risk (TPRM) | Gap record in Shared Responsibility Decision Table | Within 5 business days of discovering the gap |
| 2. **Assess residual risk** | If provider evidence is unavailable, how does the control gap affect the customer environment? Quantify the exposure using FAIR-aligned risk statement format per RMF-001 §9.2. | Risk Pillar Leader | Risk assessment with LEF/LM bands | Within 10 business days of step 1 |
| 3. **Select treatment path** | Choose one: Compensating control (customer-side control achieving same objective), Risk acceptance (per RMF-001 §9.7), or Provider remediation (contractual timeline). | Control Owner + Risk Pillar Leader | Treatment decision documented in risk register | Within 10 business days of step 2 |
| 4. **Set re-evaluation trigger** | Define the event that will trigger gap re-evaluation: contract renewal, attestation expiry, scope change, or provider breach notification. | Governance Pillar Leader | Re-evaluation trigger entry in evidence index | Within 5 business days of step 3 |
| 5. **Escalate if Critical/High** | If the gap affects a Critical or High overlay control (per §8), escalate to the CISO within 24 hours of step 2. CISO determines whether an immediate compensating control is required or whether the gap is being tracked through the risk register. | Risk Pillar Leader | CISO notification and disposition | 24 hours (Critical/High) |

> **Provider Evidence Gap vs. Control Finding.** A provider evidence gap is not automatically a control failure. It means the inheritance claim cannot be verified. The control status should be `Partially Implemented` (evidence gap) or `Inherited — Unverified` until the workflow is resolved. If the gap persists beyond the re-evaluation trigger without a documented compensating control or risk acceptance, the control defaults to `Not Implemented`.

## 8. Overlay Matrix

Overlays add to the organizational baseline. They never silently relax it.

| **Overlay** | **Applies To** | **Adds / Tightens** | **Source Standard** |
|---|---|---|---|
| **High-Impact** | Systems whose loss would materially impact the business or safety | Tighter remediation SLAs, CIS L2 baseline, expanded monitoring, MFA for all non-human identities. | STD-CFG-001 + STD-LM-001 |
| **CUI** | Any system that stores/processes/transmits CUI | [NIST 800-171r3](https://csrc.nist.gov/pubs/sp/800/171/r3/final) controls; SSP + POA&M + SPRS; FIPS-validated cryptography; DFARS flow-down; [CMMC L2](https://dodcio.defense.gov/CMMC/) assessment readiness. | STD-CUI-001 + PLN-CUI-001 |
| **BES** | Medium/High Impact BES Cyber Systems | NERC-CIP v7 controls including CIP-007, CIP-010, CIP-013; ESP/EAP topology; 90-day searchable / 12-month total log retention; annual recovery exercise; CIP-015 INSM where applicable. | STD-OT-001 + PLN-CIP-001 |
| **SOX ITGC** | Systems supporting financial reporting | Access, change, operations, backup, interface, and report ITGC controls; quarterly SoD review; SOC 1 reuse for hosted financial systems. | STD-IT-001 + PLN-SOX-001 |
| **OT Safety** | OT systems whose disruption can cause safety impact | Stricter change/maintenance windows, no active scanning, mandatory engineering review for any policy/standard parameter relaxation. | STD-OT-001 |
| **Crown-Jewel** | Tier 0 / Tier 1 crown-jewel assets (per [`CERG-GOV-CJ-001`](CERG-GOV-CJ-001_Crown_Jewel_Register_and_Scenario_Library.md)) | Verified minimum control profile: tested recovery with backup outside the blast radius, phishing-resistant identity, enumerated segmentation, ATT&CK-mapped day-one detection, and adversarial validation at enhanced frequency. Verified, not assumed. | CJ-001 §3.3 |
| **AI** | Consumed AI services, AI-enabled vendor features, embedded AI, built AI systems, AI agents, model-serving platforms, and retrieval-augmented systems | AI intake and sanctioning; maximum approved data classification; sanctioned-tools register; model/system inventory; model provenance; prompt/data egress controls; human oversight; AI-specific threat modeling; agency and least-privilege boundaries; vendor reassessment on AI feature changes. | [`CERG-STD-AI-001`](../standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md) + [`CERG-TMPL-AI-001`](../templates/CERG-TMPL-AI-001_AI_Intake_and_Sanctioning_Template.md) / [`CERG-TMPL-AI-002`](../templates/CERG-TMPL-AI-002_Sanctioned_AI_Tools_Register_Template.md) / [`CERG-TMPL-AI-003`](../templates/CERG-TMPL-AI-003_AI_System_and_Model_Register_Template.md) |

> **Multiple Overlays at Once**
>
> A given system may sit under more than one overlay (a BES system that also processes CUI; a financial system in a CUI enclave). When overlays overlap, the most stringent parameter wins for each individual control. Overlays do not "average."

---

## 9. Control-to-Evidence Mapping

Every control entry in §6 names an evidence artifact in its `Evidence` column. This section consolidates those artifacts into a single mapping with the repository where the evidence lives, the refresh cadence, and the owning pillar. It is the lookup an auditor opens first.

The discipline rule is unchanged from §2: a control without a named evidence artifact does not enter the baseline; an evidence artifact without a named repository does not satisfy the control. "It's in someone's email" is not an evidence repository.

### 9.1 Evidence Catalog

| **Control** | **Evidence Artifact** | **Repository / Tool** | **Refresh Cadence** | **Owner** |
|---|---|---|---|---|
| AC-2 Account Management | JML log, quarterly recertification report | IGA / IdP audit log + Governance access-review portal | Continuous (JML); Quarterly (recert) | Engineering (Identity) |
| AC-3 Access Enforcement | IdP / PAM policy export | IdP + PAM admin export | Annual | Engineering (Identity) |
| AC-6 Least Privilege | PAM session logs; role inventory | PAM platform; IGA role catalog | Continuous (sessions); Quarterly (role inventory) | Engineering (Identity) |
| AC-7 Unsuccessful Logon Attempts | IdP policy export; identity-attack detection rule | IdP admin export; SIEM detection inventory | Annual | Engineering (Identity) |
| AC-17 Remote Access | Gateway logs; MFA policy export | Remote-access gateway logs in SIEM; IdP policy export | Continuous (logs); Annual (policy) | Engineering (Network + Identity) |
| AC-19 Mobile / BYOD | MDM compliance report | MDM admin console export | Quarterly | Engineering (Endpoint) |
| AU-2 Event Logging | SIEM source inventory; coverage gap report | SIEM / detection-eng inventory | Monthly | Risk (Detection) |
| AU-6 Audit Review | Detection coverage report; triage queue metrics | MTR-001 DT-001 dashboard; SOC ticketing | Continuous | Risk (Detection) |
| AU-9 Protection of Audit Information | Storage policy; admin-action review | SIEM admin audit log; storage configuration export | Quarterly | Risk (Detection) |
| AU-11 Audit Record Retention | Retention policy; sample retrieval evidence | Storage configuration export; quarterly sample-retrieval ticket | Annual | Risk (Detection) |
| AU-12 Audit Record Generation | Log generation configuration; sample event test | System logging configuration; SIEM sample event evidence | Annual; Continuous monitoring | Risk (Detection) |
| CM-2 Baseline Configuration | DISH baseline catalog; DISH scan report | CERG-STD-CFG-001 baseline catalog; DISH scan results in CMDB | Continuous (scan); Annual (baseline review) | Engineering (Platforms) |
| CM-3 Change Control | CAB minutes; change records | Change-management system export | Continuous | Engineering |
| CM-5 Access Restrictions for Change | Change-authority roster; emergency-change review | Change-management system; IGA / PAM role export | Quarterly | Engineering |
| CM-6 Configuration Settings | Drift report; exception register | DISH drift detection; CERG-TMPL-RM-001 exception register | Continuous | Engineering (Platforms) |
| CM-7 Least Functionality | Application allowlist; port-scan report | EDR / allowlist platform; vuln scanner port view | Quarterly | Engineering |
| CM-8 System Component Inventory | Asset inventory export; reconciliation log | CMDB / authoritative inventory; reconciliation tickets | Monthly | Engineering / Risk |
| CP-2 Contingency Plan | Plan document; BCP interface record | CERG-STD-RES-001 plan template; enterprise BCP register | Annual | Engineering (Resilience) |
| CP-4 Contingency Plan Testing | Test report; lessons learned; register entry | Recovery-test ticket; CERG-PRC-RM-001 register | Annual; BES per CIP-009 R2.1 (15 months) | Engineering (Resilience) |
| CP-9 System Backup | Backup report; immutability evidence | Backup platform admin export | Continuous (operations); Quarterly (immutability spot-check) | Engineering (Resilience) |
| CP-10 Information System Recovery | Restoration test evidence | Recovery-test ticket package | Annual | Engineering (Resilience) |
| IA-2 Identification and Authentication | IdP policy; exception register | IdP admin export; CERG-PRC-RM-001 exception register | Quarterly | Engineering (Identity) |
| IA-3 Device Identification and Authentication | NAC / conditional-access policy | NAC admin export; IdP conditional-access export | Annual | Engineering (Identity) |
| IA-5 Authenticator Management | Secrets manager export; cert inventory | KMS / secrets manager; certificate inventory | Continuous | Engineering (Cryptography) |
| RA-3 Risk Assessment | Risk register | CERG-PRC-RM-001 risk register (per CERG-TMPL-RM-001 schema) | Continuous | Risk / Governance |
| RA-5 Vulnerability Monitoring and Scanning | Scan reports; SLA dashboard | Vulnerability scanner; MTR-001 VM-001 / VM-002 dashboard | Continuous | Risk (Exposure Management) |
| SI-2 Flaw Remediation | SLA report; exception register | MTR-001 dashboard; CERG-PRC-RM-001 exception register | Continuous | Risk / Engineering |
| SI-4 System Monitoring | Coverage report | MTR-001 DT-001 ATT&CK coverage report | Continuous | Risk (Detection) |
| SR-2 Supply Chain Risk Management Plan | TPRM register; SCCT roster | CERG-PRC-TPRM-001 register; SCCT membership roster | Continuous | Risk (TPRM) |
| SR-3 Supply Chain Controls and Processes | Country-risk register; exception register | CERG-PRC-TPRM-001 §10 register; CERG-PRC-RM-001 exception register | Quarterly | Risk (TPRM) |
| SC-7 Boundary Protection | Segmentation diagram; firewall rule review; cloud security group export | Network management platform; cloud control plane; OT ESP/EAP evidence repository | Quarterly; On change | Engineering (Network / OT) |
| SC-8 Transmission Confidentiality and Integrity | TLS / certificate scan; exception register | Certificate inventory; scanner output; CERG-PRC-RM-001 exception register | Continuous; Annual validation | Engineering (Cryptography / Network) |
| SC-28 Protection of Information at Rest | Encryption configuration export; KMS key inventory; inheritance package | Cloud console export; KMS / HSM; Inheritance Evidence Package | Quarterly | Engineering (Cryptography / Data) |
| CA-2 Control Assessment | Maturity scorecard; control test worksheet; findings register | CERG-GOV-MAT-001 scorecard; CERG-TMPL-AUD-001 worksheet; findings tracker | Annual; Quarterly high-risk | Governance / Risk |
| CA-8 Penetration Testing | Test plan; findings report; retest evidence | CERG-PRC-AV-001 engagement package; findings tracker | Annual; After material change | Risk (Adversarial Validation) |
| AT-2 Literacy Training and Awareness | Training completion report; role curriculum mapping | LMS export; onboarding record; role reader path | Annual; On role assignment | Governance (Training) |
| IR-2 Incident Response Training | Exercise attendance; role training completion | Exercise roster; LMS / onboarding record | Annual; Per exercise | Risk / Governance |
| IR-4 Incident Handling | Incident case record; timeline; evidence package | Case-management platform; evidence repository | Continuous | Risk (Incident Interface) |
| IR-8 Incident Response Plan | Approved IR plan; playbook review; after-action report | CERG-PLN-IR-001; CERG-PRC-IR-002; exercise repository | Annual; After material incident | Risk / Governance |
| PE-2 Physical Access Authorizations | Badge access roster; PSP access list | Badge system; NERC-CIP evidence repository | Quarterly | Governance / Engineering |
| PE-3 Physical Access Control | Badge logs; visitor logs; PSP inspection record | Badge system; visitor-management system; NERC-CIP evidence repository | Monthly; Quarterly review | Governance / Engineering |
| PL-1 Policy and Procedures | Document catalog; review record; approval history | CERG-GOV-CAT-001; document repository; approval workflow | Annual; On major change | Governance (Document Control) |
| PM-1 Information Security Program Plan | Operating model; service commitments; board report | CERG-GOV-OM-001; CERG-GOV-SLC-001; reporting deck | Quarterly | Governance |
| PM-9 Risk Management Strategy | RMF; risk taxonomy; risk register summary | CERG-GOV-RMF-001; CERG-GOV-TAX-001; risk register | Annual; Quarterly review | Governance / Risk |
| PM-14 Testing, Training, and Monitoring | Annual calendar; completion tracker; compliance review minutes | CERG-GOV-CAL-001; CERG-GOV-MTR-001; governance review minutes | Monthly; Annual planning | Governance |
| PS-2 Position Risk Designation | Role risk designation matrix; access precondition record | Job architecture; onboarding record; access approval workflow | Annual; Before access | Governance / HR interface |
| SA-9 External System Services | Contract security clauses; vendor assessment; shared responsibility matrix | TPRM platform; contract repository; SCCT register | Continuous; Annual reassessment | Risk (TPRM) |

### 9.2 Evidence Discipline

Three rules apply to every entry above:

1. **Currency (Adoption-Gate Tiered).** Evidence captured in the prior refresh cycle is current. Evidence older than **one refresh cycle plus 30 days** is stale; staleness is a finding in its own right and routes to the owning pillar for action. Examples per cadence:
   - **Annual controls** (e.g., CP-4 annual test, CM-3 annual review): evidence is current for 13 months; stale at 13 months + 1 day.
   - **Quarterly controls** (e.g., CM-7 least functionality, AC-6 role inventory): evidence is current for 4 months; stale at 4 months + 1 day.
   - **Continuous controls** (e.g., AU-2 event logging, CM-6 drift detection): evidence is current for 30 days; stale at 31 days.
2. **Attribution.** Every evidence artifact carries the named owning role from the canonical roster in [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1. "Owned by the team" is not attribution.
3. **Retrievability (Adoption-Gate Tiered).** Evidence shall be retrievable within the following SLA, tiered by adoption gate:
   - **Gate 1 (Spine, 0–90 days):** Within 15 business days of an auditor request. Manual collection is acceptable.
   - **Gate 2 (Operating, 90–180 days):** Within 10 business days. Structured evidence index required.
   - **Gate 3 (Governed, 180+ days):** Within 5 business days. Tool-supported evidence pipeline.
   - **Gate 4 (Adaptive, mature):** Within 2 business days. Automated evidence pipeline.
Anything that takes longer than the applicable gate SLA is a process finding regardless of whether the underlying control is operating.

> **Inheritance Evidence**
>
> Controls marked `Inherited` in §6 use the Inheritance Evidence Package defined in §5 rather than the artifacts above. The Inheritance Evidence Package replaces - it does not supplement - the customer-side evidence artifact for the inherited portion of the control.

---

## 10. Regulatory Crosswalks

This section translates each baseline control into the regulator-facing identifier or expectation. It is the read-once map for cross-framework audits: NERC-CIP auditors, CMMC C3PAOs, and SOX external auditors each look at the same controls under different names.

The [`CERG-GOV-CMX-001`](CERG-GOV-CMX-001_Compliance_Matrix.md) Compliance Matrix is the broader cross-regulator map (intent-level); the table below is the implementation-level crosswalk, control-by-control. Where the two disagree, the Compliance Matrix governs intent and this baseline governs implementation.

### 10.1 NIST 800-53 → 800-171 r3 / NERC-CIP / CMMC L2 / SOX ITGC

| **Baseline Control** | **NIST 800-171 r3** | **NERC-CIP** | **CMMC L2** | **SOX ITGC** |
|---|---|---|---|---|
| AC-2 Account Management | 03.01.01, 03.01.02 | CIP-004 R4, CIP-007 R5 | AC.L1-3.1.1, AC.L2-3.1.5 | Access |
| AC-3 Access Enforcement | 03.01.01, 03.01.05 | CIP-005 R1, CIP-007 R5 | AC.L1-3.1.1 | Access |
| AC-6 Least Privilege | 03.01.05, 03.01.06 | CIP-004 R4, CIP-007 R5 | AC.L2-3.1.5 | Access |
| AC-7 Unsuccessful Logon Attempts | 03.01.08 | CIP-007 R5.7 | AC.L2-3.1.8 | n/a |
| AC-17 Remote Access | 03.01.12, 03.13.07 | CIP-005 R2 | AC.L2-3.1.12 | Access |
| AC-19 Mobile / BYOD | 03.01.18, 03.01.19 | n/a | AC.L2-3.1.18 | n/a |
| AU-2 Event Logging | 03.03.01, 03.03.02 | CIP-007 R4 | AU.L2-3.3.1, AU.L2-3.3.2 | Operations |
| AU-6 Audit Review | 03.03.03 | CIP-007 R4 | AU.L2-3.3.5 | Operations |
| AU-9 Protection of Audit Information | 03.03.05, 03.03.06 | CIP-007 R4 | AU.L2-3.3.8, AU.L2-3.3.9 | Operations |
| AU-11 Audit Record Retention | 03.03.04 | CIP-007 R4.3 | AU.L2-3.3.4 | Operations |
| AU-12 Audit Record Generation | 03.03.01, 03.03.02 | CIP-007 R4 | AU.L2-3.3.1, AU.L2-3.3.2 | Operations |
| CM-2 Baseline Configuration | 03.04.01, 03.04.02 | CIP-010 R1 | CM.L2-3.4.1, CM.L2-3.4.2 | Change |
| CM-3 Change Control | 03.04.03 | CIP-010 R1, R2 | CM.L2-3.4.3 | Change |
| CM-5 Access Restrictions for Change | 03.04.05 | CIP-010 R1, R2 | CM.L2-3.4.5 | Change |
| CM-6 Configuration Settings | 03.04.06 | CIP-010 R1 | CM.L2-3.4.6 | Change |
| CM-7 Least Functionality | 03.04.06, 03.04.07 | CIP-007 R1 | CM.L2-3.4.7 | n/a |
| CM-8 System Component Inventory | 03.04.10 | CIP-002, CIP-010 R1 | CM.L2-3.4.10 | Operations |
| CP-2 Contingency Plan | 03.06.01, 03.06.02 | CIP-008, CIP-009 R1 | IR.L2-3.6.1 | Operations |
| CP-4 Contingency Plan Testing | 03.06.03 | CIP-009 R2 | IR.L2-3.6.3 | Operations |
| CP-9 System Backup | 03.08.09 | CIP-009 R1 | MP.L2-3.8.9 | Operations |
| CP-10 Information System Recovery | 03.06.02, 03.06.03 | CIP-009 R2, R3 | IR.L2-3.6.2 | Operations |
| IR-2 Incident Response Training | 03.06.02 | CIP-008 R2 | IR.L2-3.6.2 | Operations |
| IR-4 Incident Handling | 03.06.01, 03.06.03 | CIP-008 R1, R2, R3 | IR.L2-3.6.1, IR.L2-3.6.3 | Operations |
| IR-8 Incident Response Plan | 03.06.01 | CIP-008 R1 | IR.L2-3.6.1 | Operations |
| IA-2 Identification and Authentication | 03.05.03, 03.05.04 | CIP-005 R2.3, CIP-007 R5 | IA.L1-3.5.1, IA.L1-3.5.2, IA.L2-3.5.3 | Access |
| IA-3 Device Identification and Authentication | 03.05.02 | CIP-005, CIP-007 | IA.L2-3.5.5 | n/a |
| IA-5 Authenticator Management | 03.05.07-03.05.12 | CIP-007 R5 | IA.L2-3.5.7 through IA.L2-3.5.10 | Access |
| RA-3 Risk Assessment | 03.11.01 | CIP-003, CIP-014 | RA.L2-3.11.1 | n/a |
| CA-2 Control Assessment | 03.12.01, 03.12.02 | CIP-003, CIP-010 R3 | CA.L2-3.12.1, CA.L2-3.12.2 | Operations |
| CA-8 Penetration Testing | 03.12.01, 03.11.02 | CIP-007 R2, CIP-010 R3 | CA.L2-3.12.1 | n/a |
| RA-5 Vulnerability Monitoring and Scanning | 03.11.02, 03.11.03 | CIP-007 R2, CIP-010 R3 | RA.L2-3.11.2, RA.L2-3.11.3 | n/a |
| SI-2 Flaw Remediation | 03.14.01 | CIP-007 R2 | SI.L1-3.14.1 | Change |
| SI-4 System Monitoring | 03.14.06, 03.14.07 | CIP-007 R4 | SI.L2-3.14.6, SI.L2-3.14.7 | n/a |
| SR-2 Supply Chain Risk Management Plan | 03.17.01 | CIP-013 R1 | SR.L2 family | n/a |
| SR-3 Supply Chain Controls and Processes | 03.17.02, 03.17.03 | CIP-013 R2 | SR.L2 family | n/a |
| SA-9 External System Services | 03.16.01, 03.16.02, 03.16.03 | CIP-013 R1 | SR.L2 family | Vendor / SOC report reliance |
| SC-7 Boundary Protection | 03.13.01, 03.13.05 | CIP-005 R1, R2 | SC.L2-3.13.1, SC.L2-3.13.5 | Network / Access |
| SC-8 Transmission Confidentiality and Integrity | 03.13.08 | CIP-005 R2, CIP-011 R1 | SC.L2-3.13.8 | n/a |
| SC-28 Protection of Information at Rest | 03.13.16 | CIP-011 R1 | SC.L2-3.13.16 | n/a |
| AT-2 Literacy Training and Awareness | 03.02.01, 03.02.02 | CIP-004 R2 | AT.L2-3.2.1, AT.L2-3.2.2 | n/a |
| PE-2 Physical Access Authorizations | 03.10.01 | CIP-006 R1 | PE.L1-3.10.1 | Data center / facility access |
| PE-3 Physical Access Control | 03.10.01, 03.10.03 | CIP-006 R1, R2 | PE.L1-3.10.1, PE.L2-3.10.3 | Data center / facility access |
| PL-1 Policy and Procedures | 03.12.04 | CIP-003 R1 | CA.L2-3.12.4 | Policy / governance |
| PM-1 Information Security Program Plan | Organization-defined | CIP-003 R1 | CA.L2-3.12.4 | Entity-level control |
| PM-9 Risk Management Strategy | 03.11.01 | CIP-003, CIP-014 | RA.L2-3.11.1 | Entity-level risk |
| PM-14 Testing, Training, and Monitoring | 03.12.01, 03.12.03 | CIP-003, CIP-004, CIP-010 | CA.L2-3.12.1, CA.L2-3.12.3 | Compliance monitoring |
| PS-2 Position Risk Designation | 03.09.01 | CIP-004 R3, R4 | PS.L2-3.9.1 | n/a |

> **Reading the Crosswalk**
>
> A cell marked `n/a` means the regulator does not have an explicit identifier for the intent; it does **not** mean the regulator is uninterested. SOX auditors do not have a numbered identifier for unsuccessful-logon thresholds, but they will absolutely ask about brute-force protections on financial-system access. The crosswalk maps named controls, not audit scope.

### 10.2 Overlay-to-Regulator Mapping

The §8 overlays carry additional crosswalks. Subordinate operational packages own the detail; the table below is the entry point.

| **Overlay** | **Primary Regulator Lens** | **Operational Package** |
|---|---|---|
| High-Impact | NIST 800-53 High baseline; tightened DISH | [`CERG-STD-CFG-001`](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) + [`CERG-STD-LM-001`](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |
| CUI | NIST 800-171 r3; DFARS 252.204-7012; CMMC L2 | [`CERG-STD-CUI-001`](../standards/CERG-STD-CUI-001_CUI_Handling_Standard.md) + [`CERG-PLN-CUI-001`](../plans/CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md) |
| BES | NERC-CIP v7 (CIP-002 through CIP-014; CIP-015 INSM where applicable) | [`CERG-STD-OT-001`](../standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) + [`CERG-PLN-CIP-001`](../plans/CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md) |
| SOX ITGC | SOX §404 ITGC (Access, Change, Operations) | [`CERG-PLN-SOX-001`](../plans/CERG-PLN-SOX-001_SOX_ITGC_Operational_Package.md) |
| OT Safety | IEC 62443; NIST 800-82r3 | [`CERG-STD-OT-001`](../standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) |
| AI | NIST AI RMF 100-1; ISO/IEC 42001; privacy, CMMC, SOX, and sector obligations where AI processes regulated data or supports regulated decisions | [`CERG-STD-AI-001`](../standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md) + [`CERG-TMPL-AI-001`](../templates/CERG-TMPL-AI-001_AI_Intake_and_Sanctioning_Template.md) / [`CERG-TMPL-AI-002`](../templates/CERG-TMPL-AI-002_Sanctioned_AI_Tools_Register_Template.md) / [`CERG-TMPL-AI-003`](../templates/CERG-TMPL-AI-003_AI_System_and_Model_Register_Template.md) |

---

### 10.3 Compliance Matrix Intent-to-Control Bridge

[`CERG-GOV-CMX-001`](CERG-GOV-CMX-001_Compliance_Matrix.md) (the Compliance Matrix) is organized by 22 cross-regulator **intents** ("Know what you own," "Manage vendor risk," etc.). This baseline is organized by **controls** (AC-2, AC-3, CM-8, etc.). The table below resolves each Compliance Matrix intent to the §6 controls that implement it. Where an intent is implemented outside the §6 control set, the table names the authoritative subordinate document instead.

| **CMX Intent** | **Title** | **CB-001 §6 Controls** | **Where Else Implementation Lives** |
|---|---|---|---|
| 1 | Know what you own: authoritative asset inventory | CM-8 | [`CERG-STD-IT-001`](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md); [`CERG-STD-OT-001`](../standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) (CIP-002 categorization) |
| 2 | Identify and remediate vulnerabilities on schedule | RA-5, SI-2 | [`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) §5.2 (canonical SLAs) |
| 3 | Control who can access what: least privilege | AC-2, AC-3, AC-6, AC-7, AC-19 | [`CERG-STD-AC-001`](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |
| 4 | Authenticate users and systems | IA-2, IA-3, IA-5 | [`CERG-STD-AC-001`](../standards/CERG-STD-AC-001_Access_Management_Standard.md); [`CERG-STD-CR-001`](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) (authenticators) |
| 5 | Harden systems | CM-2, CM-6, CM-7 | [`CERG-STD-CFG-001`](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) (DISH baselines) |
| 6 | Protect data in transit and at rest | SC-8, SC-28, IA-5 | [`CERG-STD-CR-001`](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md); [`CERG-STD-CUI-001`](../standards/CERG-STD-CUI-001_CUI_Handling_Standard.md); [`CERG-STD-DG-001`](../standards/CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md) |
| 7 | Segment networks | SC-7, AC-17 | [`CERG-STD-NET-001`](../standards/CERG-STD-NET-001_Network_Security_and_Segmentation_Standard.md); [`CERG-STD-OT-001`](../standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) (ESP/EAP) |
| 8 | Manage vendor and third-party risk | SA-9, SR-2, SR-3 | [`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) |
| 9 | Control and log privileged / remote access | AC-6, AC-17, AU-2, AU-6, AU-12 | [`CERG-STD-AC-001`](../standards/CERG-STD-AC-001_Access_Management_Standard.md); [`CERG-STD-LM-001`](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |
| 10 | Conduct adversarial testing | CA-8, RA-5 | [`CERG-PRC-AV-001`](../procedures/CERG-PRC-AV-001_Adversarial_Validation_Procedure.md) |
| 11 | Train and background-check personnel | AT-2, PS-2 | [`CERG-GOV-TRN-001`](CERG-GOV-TRN-001_Training_Development_and_Certification_Framework.md); [`CERG-GOV-ONB-001`](CERG-GOV-ONB-001_Onboarding_and_Integration_Program.md) |
| 12 | Write and maintain policies | PL-1, PM-1 | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md); [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md); [`CERG-GOV-STY-001`](CERG-GOV-STY-001_Document_Authoring_and_Style_Guide.md) |
| 13 | Manage configuration changes | CM-3, CM-5 | [`CERG-STD-CFG-001`](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md); [`CERG-PRC-CHG-001`](../procedures/CERG-PRC-CHG-001_Security_Change_Management_Procedure.md); [`CERG-PRC-AR-001`](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) |
| 14 | Collect, protect, and retain audit evidence | AU-2, AU-6, AU-9, AU-11, AU-12; this doc §9 evidence catalog | [`CERG-STD-LM-001`](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) (retention) |
| 15 | Assess your own security posture | CA-2, RA-3 | [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md); [`CERG-GOV-MAT-001`](CERG-GOV-MAT-001_Maturity_Self_Assessment_and_Scorecard.md); [`CERG-TMPL-AUD-001`](../templates/CERG-TMPL-AUD-001_Control_Evidence_and_Test_Worksheet.md) |
| 16 | Manage risk formally | RA-3, PM-9, SI-2 (exception register) | [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md); [`CERG-TMPL-RM-001`](../templates/CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md); [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.7 |
| 17 | Protect physical access | PE-2, PE-3 | [`CERG-STD-OT-001`](../standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) (CIP-006 PSP); [`CERG-PLN-CIP-001`](../plans/CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md) |
| 18 | Monitor threats continuously | SI-4, AU-6, IR-4 | [`CERG-STD-LM-001`](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) (Day-One Detection Set; 70% ATT&CK target) |
| 19 | Plan and practice incident response | IR-2, IR-4, IR-8 | [`CERG-PLN-IR-001`](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md); [`CERG-PRC-IR-002`](../procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md) |
| 20 | Manage recovery | CP-2, CP-4, CP-9, CP-10 | [`CERG-STD-RES-001`](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) |
| 21 | Manage accounts through lifecycle | AC-2, AC-7, IA-2, IA-5 | [`CERG-STD-AC-001`](../standards/CERG-STD-AC-001_Access_Management_Standard.md); [`CERG-PRC-AC-002`](../procedures/CERG-PRC-AC-002_Access_Management_Runbook.md) (JML runbook) |
| 22 | Define and enforce a compliance calendar | PM-14, PM-9, CA-2 | [`CERG-GOV-CAL-001`](CERG-GOV-CAL-001_Annual_Security_and_Governance_Calendar.md); [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md); [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) |

> **Reading the Bridge**
>
> The bridge is intentionally implementation-oriented. Every Compliance Matrix intent now points to at least one §6 baseline control row, and the final column points to the documents that carry the deeper operational parameters.

### 10.4 Family Coverage Note

The CERG control family spine in §3 lists 19 NIST 800-53 families. §6 now includes explicit baseline rows for every family needed by the 22 Compliance Matrix intents, while still keeping environment-specific parameter depth in subordinate standards and procedures.

| **Family** | **Baseline Role in §6** | **Authoritative Implementation Detail** |
|---|---|---|
| AC, IA | Identity, access enforcement, least privilege, remote access, account lifecycle, and authenticators. | [`CERG-STD-AC-001`](../standards/CERG-STD-AC-001_Access_Management_Standard.md); [`CERG-PRC-AC-002`](../procedures/CERG-PRC-AC-002_Access_Management_Runbook.md) |
| AT, PS | Training and position-risk designation are baseline controls because access and CUI/BES scope depend on them. | [`CERG-GOV-TRN-001`](CERG-GOV-TRN-001_Training_Development_and_Certification_Framework.md); [`CERG-GOV-ONB-001`](CERG-GOV-ONB-001_Onboarding_and_Integration_Program.md) |
| AU, SI | Logging, audit review, retention, event generation, monitoring, and flaw remediation. | [`CERG-STD-LM-001`](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md); [`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) |
| CA, RA | Control assessment, adversarial validation, risk assessment, and exposure management. | [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md); [`CERG-PRC-AV-001`](../procedures/CERG-PRC-AV-001_Adversarial_Validation_Procedure.md); [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) |
| CM | Baselines, configuration settings, change control, change authority, least functionality, and inventories. | [`CERG-STD-CFG-001`](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md); [`CERG-PRC-CHG-001`](../procedures/CERG-PRC-CHG-001_Security_Change_Management_Procedure.md) |
| CP, IR | Recovery planning, backup, restoration, incident handling, training, and playbooks. | [`CERG-STD-RES-001`](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md); [`CERG-PLN-IR-001`](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md); [`CERG-PRC-IR-002`](../procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md) |
| PE | Physical access authorization and control for cyber-relevant facilities, PSPs, and CUI spaces. | [`CERG-STD-OT-001`](../standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md); [`CERG-PLN-CIP-001`](../plans/CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md) |
| PL, PM | Policy hierarchy, operating model, risk strategy, calendar, metrics, testing, training, and monitoring. | [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md); [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md); [`CERG-GOV-CAL-001`](CERG-GOV-CAL-001_Annual_Security_and_Governance_Calendar.md) |
| SA, SR | External services, supply chain risk management, third-party evidence, and country-risk controls. | [`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md); [`CERG-PRC-AR-001`](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) |
| SC | Boundary protection, cryptographic protection in transit, and data-at-rest protection. | [`CERG-STD-NET-001`](../standards/CERG-STD-NET-001_Network_Security_and_Segmentation_Standard.md); [`CERG-STD-OT-001`](../standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md); [`CERG-STD-CR-001`](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) |

> **Baseline vs. Parameter Detail**
>
> §6 names the auditable control, owner, evidence, cadence, and implementation document. Subordinate standards and procedures carry the detailed parameter values, workflows, and environment-specific exceptions. If there is a conflict, the stricter requirement applies unless Governance approves a documented exception.

## 11. Governance, Change, and Versioning

### 11.1 Ownership

The Governance Pillar Leader owns this baseline. Material changes (additions, removals, parameter changes that affect remediation SLAs or evidence requirements) require CISO approval; non-material changes (clarifications, typo fixes, additional implementation notes) require Governance Pillar Leader approval.

Pillar leaders may propose changes at any time. The Governance Pillar Leader runs an open intake at the monthly Compliance Pulse forum (per [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §7).

### 11.2 Change Triggers

The baseline is reviewed and updated upon any of the following:

- **Framework version change.** A new version of NIST 800-53, NIST 800-171, NIST CSF, NERC-CIP, CMMC, or any in-scope framework triggers a delta review and, where appropriate, an overlay or control update.
- **Regulator action.** A new rule, advisory, or enforcement action that changes expectations.
- **Material program change.** Adoption of a new platform class, retirement of an existing one, or significant change to the asset tiering scheme.
- **Audit / assessment finding.** A finding from internal audit, external auditor, NERC-CIP audit, CMMC assessment, or C3PAO that points at a baseline gap.
- **Sev 1 incident.** A confirmed incident whose root cause traces to a missing or weak baseline control.
- **Annual review.** Even in the absence of triggers, Governance conducts a full annual review.

### 11.3 Change Workflow

1. **Proposal.** Submitted to the Governance Pillar Leader with: control(s) affected, change rationale, impact on overlays, evidence implications, and any regulator-facing implications.
2. **Assessment.** Engineering and Risk review for operational practicability and exposure implications. Comments returned within 10 business days.
3. **Decision.** Material changes go to CISO at the next Monthly Risk Register Review or sooner if time-sensitive. Non-material changes are approved by the Governance Pillar Leader.
4. **Publication.** Approved changes are merged into the source markdown with a revision history entry. Subordinate documents that cite the changed control are flagged for refresh in their next review cycle.
5. **Notification.** Pillar leaders communicate the change at the next CERG All-Hands and at the next Cyber Oversight Group meeting.

### 11.4 Versioning Rules

This baseline follows semantic-ish versioning:

| Version Bump | When | Examples |
|---|---|---|
| **Major** (`x.0`) | Whole-baseline restructure, framework retirement (e.g., 800-53r5 → r6 migration), introduction of a new overlay class | Future r6 migration; addition of an overlay class such as AI |
| **Minor** (`1.x`) | New control, new overlay parameter, change to evidence catalog (§9), new crosswalk entry (§10) | Adding a new ATT&CK-derived detection control to AU family |
| **Patch** (`1.0.x`) | Clarifying language, typo fix, cross-reference correction, no semantic change | Hyperlink fix, role-name normalization |

A change log entry is written for every version bump; the change-log table lives in §12 Revision History.

### 11.5 Subordinate-Document Synchronization

When a control in §6 or an overlay in §8 changes, Governance issues a "ripple list" naming every subordinate document that references the changed control. The owning pillar leaders are responsible for refreshing those documents within 30 calendar days of the baseline change being approved. The Compliance Pulse forum tracks ripple-list closure each cycle.

---

## 12. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-CB-001 |
| **Version** | 2.0 |
| **Status** | Approved |
| **Effective Date** | 2026-06-17 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader (Control Baseline) |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on framework version change (NIST 800-53 rev, CMMC rev, NERC-CIP version, AI governance framework change) |
| **Next Scheduled Review** | 2027-05-01 |
| **Frameworks** | NIST 800-53r5; NIST 800-171r3; NIST CSF 2.0; CIS Controls v8; ISO/IEC 27001 A.5-A.8; NIST AI RMF 100-1; ISO/IEC 42001 |
| **Regulations** | NERC-CIP v7 (and CIP-015 draft); CMMC L2; SOX ITGC |
| **Environments** | All in-scope assets - owned, hybrid, cloud, SaaS, OT, CUI, AI-enabled systems |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 2.0 | 2026-06-17 | Cyber Governance | Added the AI overlay to the overlay matrix and regulator mapping, linking AI control evidence to STD-AI-001 and the AI intake, sanctioned-tools, and system/model register templates. |
| 1.21 | 2026-05-22 | Cyber Governance | Updated framework references and normalized section numbering to align with the current corpus structure. |
| 1.0 | 2026-05-01 | Cyber Governance | Initial release. Establishes the design principles, control family spine, organizational baseline (§6 control set), control status decision tree (§7), overlay matrix (§8), control-to-evidence mapping (§9), regulatory crosswalks (§10), governance/change/versioning rules (§11), and document control (§12). Aligned to NIST 800-171 r3 and the canonical IDs in CERG-GOV-CAT-001 §5.2. |

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| Document Catalog and Naming Convention | [`CERG-GOV-CAT-001`](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Authoritative artifact inventory |
| CERG Operating Model | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) | Pillar / role definitions cited by §9 evidence owners |
| Risk Management Framework | [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) | Risk treatment, approval authority, and FAIR risk format |
| Metrics, Dashboard, and Reporting | [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) | Hosts the dashboards cited in §9 evidence catalog |
| Compliance Matrix | [`CERG-GOV-CMX-001`](CERG-GOV-CMX-001_Compliance_Matrix.md) | Intent-level cross-regulator map (this doc is implementation-level) |
| Risk Taxonomy | [`CERG-GOV-TAX-001`](CERG-GOV-TAX-001_Risk_Taxonomy.md) | Risk categorization that feeds RA-3 register entries |
| Exposure Management Procedure | [`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) | Canonical SLAs cited by SI-2 |
| Risk Register and Exception Process | [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Exception register cited by §6 and §9 |
| Secure Configuration Baseline Standard (DISH) | [`CERG-STD-CFG-001`](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) | Underlying baselines cited by CM-2 |
| Logging, Monitoring, and Detection Standard | [`CERG-STD-LM-001`](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) | Underlying detection set cited by AU-* and SI-4 |
| Cyber Resilience and Backup Standard | [`CERG-STD-RES-001`](../standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md) | Underlying recovery posture cited by CP-* |
| Cryptography and Key Management Standard | [`CERG-STD-CR-001`](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) | Underlying crypto posture cited by IA-5 |
| Access Management Standard | [`CERG-STD-AC-001`](../standards/CERG-STD-AC-001_Access_Management_Standard.md) | Underlying access posture cited by AC-* and IA-2 |
| Artificial Intelligence Security Standard | [`CERG-STD-AI-001`](../standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md) | Source standard for the AI overlay |
| AI Intake and Sanctioning Template | [`CERG-TMPL-AI-001`](../templates/CERG-TMPL-AI-001_AI_Intake_and_Sanctioning_Template.md) | Intake evidence for proposed AI use under the AI overlay |
| Sanctioned AI Tools Register Template | [`CERG-TMPL-AI-002`](../templates/CERG-TMPL-AI-002_Sanctioned_AI_Tools_Register_Template.md) | Register evidence for approved AI tools and maximum data classification |
| AI System and Model Register Template | [`CERG-TMPL-AI-003`](../templates/CERG-TMPL-AI-003_AI_System_and_Model_Register_Template.md) | Inventory evidence for built and embedded AI systems, models, data sources, and agency boundaries |
