## LOGGING, MONITORING, AND DETECTION STANDARD
### Mandatory Log Sources · SIEM Onboarding · Day-One Detection Set · OT and CUI Overlays · Triage and Tuning

---

| | |
|---|---|
| **Document ID** | CERG-STD-LM-001 |
| **Version** | 1.23 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Risk Pillar Leader (Detection Engineering) |
| **Parent Policy** | [CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Standards** | [CERG-STD-IT-001](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) · [CERG-STD-OT-001](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) · [CERG-STD-CUI-001](CERG-STD-CUI-001_CUI_Handling_Standard.md) · [CERG-STD-AC-001](CERG-STD-AC-001_Access_Management_Standard.md) · [CERG-STD-CFG-001](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) · [CERG-STD-CR-001](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) |
| **Supporting Procedures** | [CERG-PRC-VM-001](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) · [CERG-PRC-AV-001](../procedures/CERG-PRC-AV-001_Adversarial_Validation_Procedure.md) · [CERG-PRC-RM-001](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) |
| **Review Cycle** | Annual / On SIEM platform change / On MITRE ATT&CK matrix update |
| **Frameworks** | [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (DETECT) · [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) (AU, SI) · [NIST 800-92](https://csrc.nist.gov/pubs/sp/800/92/final) · MITRE ATT&CK Enterprise / Cloud / ICS · MITRE D3FEND |
| **Regulations** | NERC-CIP CIP-007 R4 · [CMMC L2](https://dodcio.defense.gov/CMMC/) (3.3.x) · SOX ITGC (Operations) · CIP-015 (forward-looking) |
| **Environments** | All in-scope assets - IT · cloud · SaaS · OT · CUI · identity · network |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Operating Principles](#2-operating-principles)
3. [Mandatory Log Sources](#3-mandatory-log-sources)
4. [Log Routing, Protection, and Retention](#4-log-routing-protection-and-retention)
5. [SIEM Onboarding](#5-siem-onboarding)
6. [Day-One Detection Set](#6-day-one-detection-set)
7. [Detection Lifecycle and Validation](#7-detection-lifecycle-and-validation)
8. [Alert Triage and Tuning](#8-alert-triage-and-tuning)
9. [OT Monitoring Overlay](#9-ot-monitoring-overlay)
10. [CUI Monitoring Overlay](#10-cui-monitoring-overlay)
11. [Identity Detection Use Case Pack](#11-identity-detection-use-case-pack)
12. [Regulatory and Framework Alignment Summary](#12-regulatory-and-framework-alignment-summary)
13. [Document Control](#13-document-control)

---

## 1. Purpose and Scope

The policy requires privileged-access logging, log protection, retention, SIEM (or equivalent) monitoring, OT-safe collection methods, and threat-intelligence integration. The IT, OT, CUI, and Access standards each impose more specific log and detection requirements. Until this standard, those requirements existed in fragments, no consolidated list of mandatory log sources, no day-one detection set, no triage procedure.

This standard consolidates those requirements. It defines the log sources every in-scope environment must onboard, how those logs are routed and retained, the detection set the SIEM must implement on day one, and how detections are validated and tuned over time. It applies to every in-scope asset and every CERG-managed detection platform.

> **Detection Coverage Is a Product, Not a Project**
>
> Onboarding a SIEM is a project. Detection coverage is the ongoing measurement of whether the detections that should be firing actually do, for the threats that matter to *this* environment. CERG instruments coverage as a metric (`DT-001` in [`CERG-GOV-MTR-001`](../governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md)) and treats anything below the target as an incident-readiness gap.

---

## 2. Operating Principles

1. **MITRE ATT&CK is the threat reference.** Detection scope and prioritization use ATT&CK Enterprise (IT/cloud/SaaS), ATT&CK for ICS (OT), and ATT&CK for Cloud sub-matrices.
2. **Day-One Set is non-negotiable.** Every in-scope environment has the minimum detection set in Section 6 enabled within 30 days of onboarding (`CERG-X-05`).
3. **Coverage over count.** A SIEM with 4,000 rules and 35% real ATT&CK coverage is worse than a SIEM with 400 rules and 80% real ATT&CK coverage.
4. **Tune to signal, not silence.** A muted alert that should have fired is an incident. Tuning suppresses noise, not findings.
5. **Logs are immutable.** No production identity can edit or delete a log inside its retention period.
6. **OT collection is passive by default.** Collection methods that risk OT availability are prohibited without engineering approval.

---

## 3. Mandatory Log Sources

The list below is the minimum every CERG-managed environment must onboard. Anything not listed may still be required by a subordinate standard; nothing in this list may be waived without an approved exception per [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md).

### 3.1 Identity, Endpoint, and Application

| **Source** | **What Must Be Collected** |
|---|---|
| Identity Provider (IdP) | All authentication events (success/fail), MFA events, conditional access decisions, admin actions on tenants/users/roles, federation/trust events. |
| IGA / Identity Governance | Account lifecycle (create/modify/disable/delete), entitlement assignments, recertification events. |
| Privileged Access Management (PAM) | Vault retrieve, session start/stop, command execution metadata, break-glass usage, policy changes. |
| Directory Services (AD, Entra ID, etc.) | Authentication, privileged group changes, GPO / policy changes, DCSync / DCShadow indicators. |
| OAuth / OIDC application logs | Consent grants, token issuance, scope changes, suspicious app installs (M365 / Workspace). |
| Endpoint Detection and Response (EDR) | Process events, persistence indicators, lateral-movement indicators, EDR tamper events. |
| Email / collaboration platform | Sign-in events, mailbox/forwarding rule changes, suspicious attachment / link events, anomalous OAuth grants. |
| MDM / device compliance | Compliance status, enrollment / un-enrollment events, posture changes. |

### 3.2 Cloud and SaaS

| **Source** | **What Must Be Collected** |
|---|---|
| Cloud control plane (CloudTrail / Activity Log / Audit Logs) | All admin events org-wide; tenant-isolation, IAM, networking, KMS, logging-config changes. |
| Cloud workload | OS audit, container runtime, function invocation logs (where in scope). |
| CSPM / SSPM | Misconfiguration findings, drift, posture changes. |
| Tier 1 SaaS admin/auth logs | Per [`CERG-STD-IT-001`](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) Section 9; minimally: admin actions, auth events, data export, sharing events. |
| KMS / HSM | Key administrative events, policy changes, usage events for keys protecting Restricted/CUI. |
| Secrets manager | Retrieval, write, policy change events. |

### 3.3 Network, Vulnerability, and Telemetry

| **Source** | **What Must Be Collected** |
|---|---|
| Firewall (edge and segment) | Session metadata, threat events, rule changes. |
| Network device (switch/router) | Configuration changes, AAA events. |
| DNS resolver | Query logs (sampled or full per environment), tunneling indicators. |
| Web proxy / SSE / SWG | URL/category, blocked actions, file upload/download. |
| NDR / network sensor | Detection events; metadata flows where retained. |
| VPN / remote access gateway | Session start/stop, posture decisions, geographic anomalies. |
| Vulnerability scanner | DISH scan output, scan run metadata, exception annotations. |

### 3.4 OT (See Also §9)

| **Source** | **What Must Be Collected** |
|---|---|
| OT passive monitoring (e.g., span/tap-fed sensor) | Asset inventory deltas, protocol anomalies, baseline deviations. |
| SCADA / HMI | Authentication, configuration changes, alarm history, operator console actions. |
| Historian | Authentication, admin actions, integrity-relevant events. |
| OT jump server | Session events, file transfer, command history. |
| OT firewall / EAP enforcement device | Session, rule change, denied flow events. |
| Engineering workstation | Authentication, USB / removable media events, application execution. |

### 3.5 CUI (See Also §10)

| **Source** | **What Must Be Collected** |
|---|---|
| CUI workstation / VDI | Auth, file access events for CUI, USB/media activity, EDR. |
| CUI file repositories | Access events, share/permission changes, large or anomalous export. |
| CUI cloud enclave (GCC High / FedRAMP equivalent) | Tenant audit, DLP findings. |
| CUI DLP | Policy match events, blocked/allowed transfers, override events. |

---

## 4. Log Routing, Protection, and Retention

### 4.1 Routing

- IT/cloud/SaaS logs route to the enterprise SIEM via supported native connectors or log shippers.
- OT logs route via the **one-way** transfer pattern specified in [`CERG-STD-OT-001`](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) and Section 9 below. No bidirectional pulls from OT.
- CUI logs route to a SIEM tenancy / index that aligns with the CUI boundary and supports FIPS-validated transport ([`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md)).

### 4.2 Protection

- Logs are written to immutable / WORM storage for the retention period.
- Administrative actions on logs (delete, retention change, export) are themselves logged and reviewed.
- Log access follows least privilege per [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md); privileged log access uses PAM.

### 4.3 Retention

| **Scope** | **Hot / Searchable** | **Cold / Archive** |
|---|---|---|
| Default | 13 months | 7 years (or per regulatory requirement, whichever longer) |
| BES Cyber Systems | 90 days searchable minimum | 12 months total minimum (CIP-007 R4.3); CERG default exceeds |
| CUI | 13 months hot | 7 years per [CMMC L2](https://dodcio.defense.gov/CMMC/) / DFARS |
| SOX-relevant | 13 months hot | 7 years per SOX requirement |

---

## 5. SIEM Onboarding

Onboarding follows a fixed checklist. The output is a SIEM Onboarding Record per environment.

### 5.1 SIEM Onboarding Checklist

| **Step** | **Done When** |
|---|---|
| Source inventory | Every mandatory source per Section 3 is named and accounted for. |
| Connector deployed | Native connector or log shipper deployed in supported configuration. |
| Parsing validated | Logs are parsed to the expected schema and timestamp normalized to UTC. |
| Field mapping | Identity, asset, action, source/destination fields mapped to the SIEM's data model. |
| Volume baselined | Steady-state volume known; alert on volume drop > X% (Section 5.2). |
| Retention configured | Hot and cold retention per Section 4.3. |
| Access controlled | RBAC for analysts; PAM for admins. |
| Day-One detections enabled | Per Section 6 for the environment type. |
| Detection coverage report generated | Per [`CERG-GOV-MTR-001`](../governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) metric DT-001. |
| Operations handoff | Triage runbook (Section 8) in place; on-call rotation aware. |

### 5.2 Source Health Monitoring

Each onboarded source is itself monitored. CERG alerts on:

- Source silence (no events for > expected interval).
- Volume drop > 30% week-over-week (configurable per source).
- Parsing failure rate > 1%.
- Connector error or authentication failure.

These alerts are treated as high-priority operational items, not as detections in their own right.

---

## 6. Day-One Detection Set

The Day-One Detection Set is the minimum coverage required in any in-scope environment within 30 days of onboarding. The set is curated against MITRE ATT&CK with ATT&CK Enterprise as the IT spine, ATT&CK for Cloud sub-techniques for cloud/SaaS scopes, and ATT&CK for ICS for OT scopes.

### 6.1 Day-One: IT / Cloud / SaaS / Identity

| **Category** | **Detection Intent** | **ATT&CK Mapping (examples)** |
|---|---|---|
| Initial Access | Anomalous geographic sign-in; impossible-travel; suspicious OAuth consent | T1078, T1566, T1199 |
| Execution | Suspicious script execution; PowerShell encoded commands | T1059.001, T1204 |
| Persistence | Mailbox forwarding / inbox rule additions; new scheduled task; new local admin | T1098, T1136, T1547 |
| Privilege Escalation | Local privilege escalation indicators; cloud role assumption anomalies | T1068, T1078.004 |
| Defense Evasion | EDR tamper events; cloud trail / activity log disable; security group change | T1562, T1027 |
| Credential Access | Brute force; password spray; ASREP roast / Kerberoasting | T1110, T1558 |
| Discovery | Cloud account / role enumeration; AD reconnaissance from low-priv account | T1087, T1069 |
| Lateral Movement | Pass-the-hash / pass-the-ticket indicators; remote service exploitation | T1550, T1021 |
| Collection | Mass mailbox download; high-volume SharePoint / Drive download | T1114, T1213 |
| Exfiltration | Anomalous outbound volume; new exfil destinations | T1041, T1567 |
| Impact | Mass file modification (ransomware indicators); resource deletion in cloud | T1485, T1486 |

### 6.2 Day-One: OT

| **Category** | **Detection Intent** | **ATT&CK for ICS Mapping** |
|---|---|---|
| Initial Access | External engineering-tool connection; jump-server anomaly | T0817, T0822 |
| Execution | New process on HMI / SCADA server; engineering-tool execution off-hours | T0871 |
| Persistence | New service / scheduled task on OT host; firmware change | T0857 |
| Lateral Movement | Cross-segment traffic between ESPs; new flow patterns | T0883 |
| Inhibit Response Function | Alarm suppression; logging disabled | T0878, T0837 |
| Impair Process Control | Setpoint changes off normal range; relay setting group change | T0855 |

### 6.3 Day-One: CUI

CUI overlay (see Section 10) adds CUI-specific detections (export, share, label changes, classified-data movement to non-CUI destinations).

### 6.4 Coverage Reporting

- Coverage is computed as the % of ATT&CK techniques within the in-scope sub-matrix that have at least one detection authored, tested, and operating. Reported as DT-001 in [`CERG-GOV-MTR-001`](../governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md).
- **CERG coverage target: 70% of in-scope ATT&CK sub-matrix techniques with at least one operating detection.** Below 70% is reported red on the CISO dashboard and treated as an incident-readiness gap until closed.
- The detection inventory is exported monthly and reviewed quarterly against the in-scope sub-matrix.

---

## 7. Detection Lifecycle and Validation

Every detection has a lifecycle from `Proposed` through `Retired`. Detection metadata is recorded in the detection inventory.

| **State** | **Means** |
|---|---|
| Proposed | Drafted by detection engineer. |
| In Test | Running in non-prod; tuning underway. |
| In Production | Active; routed to triage queue. |
| Suspended | Temporarily disabled (data-quality issue, tool change); time-boxed. |
| Retired | Removed; rationale captured. |

### 7.1 Detection Metadata

Each production detection has:

- ID and name
- ATT&CK technique(s) and tactic(s)
- Data sources used
- Logic summary (no proprietary leakage outside detection eng)
- Severity / triage queue routing
- Expected fire rate (per env)
- False-positive notes and tuning history
- Last purple-test validation date and result
- Owner

### 7.2 Validation

- Detections are validated quarterly via the purple-team procedure in [`CERG-PRC-AV-001`](../procedures/CERG-PRC-AV-001_Adversarial_Validation_Procedure.md) §6.
- Validation result feeds metric DT-002.
- Failed validations open a risk register entry per [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) until restored.

---

## 8. Alert Triage and Tuning

### 8.1 Triage Queue Model

- **P1, Critical:** business impact suspected; SOC engages immediately and pages IR per [`CERG-PLN-IR-001`](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md).
- **P2, High:** likely true positive worth examining within hours.
- **P3, Medium:** worth examining within the shift.
- **P4, Low:** examined for trends; bulk-tuned where appropriate.

### 8.2 Triage SLA

| **Priority** | **Acknowledge** | **First Action** | **Disposition** |
|---|---|---|---|
| P1 | ≤ 15 minutes | ≤ 30 minutes | per IR |
| P2 | ≤ 2 hours | ≤ 4 hours | within shift |
| P3 | within shift | within 24 hours | within 48 hours |
| P4 | within 48 hours | within 5 business days | within 10 business days |

### 8.3 Tuning Discipline

- Tuning suppresses noise; tuning never suppresses findings.
- Every tuning change records: detection ID, reason, suppressed condition, expiration / review date.
- Tuning changes are reviewed monthly; expired tunings are reinstated unless renewed with justification.

> **The Bar for Suppressing an Alert**
>
> If a tuning suppresses a condition that has ever yielded a real finding in this environment, peer organization, or current threat intelligence, the tuning needs a different shape, a different field condition, a different threshold, not a blanket suppression.

---

## 9. OT Monitoring Overlay

OT monitoring adds to the IT pattern; it does not replace it.

- **Passive monitoring is the default.** Span / tap / mirror-fed sensors capture protocol-aware traffic for asset inventory, anomaly, and detection.
- **Engineering-supervised authenticated checks** allowed in defined windows for endpoint health, configuration capture.
- **One-way transfer to SIEM.** Data diodes or filtered one-way pipelines per [`CERG-STD-OT-001`](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md).
- **OT-specific detection set** per Section 6.2.
- **OT alerts route through a queue that the SOC and OT operations both see** to avoid loss of fidelity in handoff.
- **No active scanning** of live OT surfaces without an approved scope and time window per [`CERG-PRC-AV-001`](../procedures/CERG-PRC-AV-001_Adversarial_Validation_Procedure.md).
- **CIP-015 (forward-looking).** As CIP-015 finalizes, the BES INSM detection set in Section 6.2 is the foundation; additional CIP-015 detections are added when the standard is approved.

---

## 10. CUI Monitoring Overlay

- **CUI labeling enforcement.** Data classified as CUI is labeled in source systems; movement of labeled data is monitored.
- **CUI exfiltration alerts.** Outbound transfers of CUI to non-CUI destinations trigger P2 minimum.
- **CUI workspace boundary** alerts on any cross-boundary access attempts.
- **EDR on CUI endpoints** has CUI-aware policies (USB lockdown, application allowlist).
- **Threat advisories** relevant to CUI (DFARS / DC3 advisories) are routed to detection engineering and incorporated where applicable.

---

## 11. Identity Detection Use Case Pack

Identity is the most common attack surface; CERG names a use case pack explicitly.

| **Use Case** | **Signal** |
|---|---|
| Phishing-resistant MFA bypass | Successful auth via legacy MFA when phishing-resistant policy applies. |
| OAuth consent grant abuse | Unusual or risky app consent in M365 / Workspace; high-scope consent outside approved workflow. |
| Privilege escalation in IdP | Unexpected addition to high-privilege groups, privileged role activation outside change window, or new standing admin entitlement. |
| MFA factor manipulation | New authenticator registration, MFA reset, or recovery-method change followed by high-risk access. |
| Service account / NHI anomaly | Service account, service principal, workload identity, or API token auth from new ASN, new endpoint, new workload, or unexpected geography. |
| CI/CD identity abuse | Pipeline token, deploy key, code-signing identity, build agent credential, or repository-to-cloud federation used outside expected pipeline, branch, runner, release window, or source environment. |
| Code-signing anomaly | Signing key use outside approved release process, unexpected signer, signing from non-build infrastructure, failed timestamping, or certificate change outside change window. |
| Session token theft indicators | Auth from new device with valid refresh token; impossible travel without fresh MFA; repeated token replay / invalid token attempts. |
| Federation tampering | Trust / claim / certificate changes in IdP federation; new external IdP trust; signing certificate replacement outside change window. |
| Conditional access policy change | Any change to CA policy in M365 / Entra, especially policy disablement, exclusion expansion, or legacy-auth exception. |
| Break-glass account use | Any successful auth on a break-glass account. |
| Dormant account reactivation | Auth on a disabled / dormant account; guest or vendor account active after expiration. |
| External identity anomaly | Guest, vendor, MSP, or federated account accessing outside approved window, geography, device posture, or scoped application set. |
| Impossible travel / geo anomalies | Two successful auths from geographically inconsistent locations. |

---
## 12. Regulatory and Framework Alignment Summary

| **Regulation / Framework** | **Section** | **Where in This Standard** |
|---|---|---|
| [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) AU / SI | AU-2, AU-6, AU-9, AU-11, SI-4 | All sections |
| [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) DETECT | DE.CM, DE.AE | All sections |
| [NIST 800-92](https://csrc.nist.gov/pubs/sp/800/92/final) | All | Sections 3–4 |
| MITRE ATT&CK Enterprise / Cloud / ICS | All | Sections 6, 7 |
| NERC-CIP CIP-007 R4 | Security Event Monitoring | Sections 3.4, 4.3, 9 |
| NERC-CIP CIP-015 (draft) | INSM | Section 9 |
| [CMMC L2](https://dodcio.defense.gov/CMMC/) / 800-171r3 | 3.3.x | Section 10 |
| SOX ITGC | Operations / Monitoring | Sections 3, 4 |

---

## 13. Document Control

| | |
|---|---|
| **Document ID** | CERG-STD-LM-001 |
| **Version** | 1.23 |
| **Approved By** | CISO |
| **Next Review** | Annual / SIEM platform change / ATT&CK matrix update |
| **Change Log** | 1.23 - Added CI/CD identity abuse and code-signing anomaly use cases to the identity detection pack. 1.22 - Expanded identity detection use cases for OAuth consent, MFA factor manipulation, NHI anomalies, session-token theft, federation tampering, and external identity misuse. 1.0 - Initial publication. Mandatory log sources, retention, SIEM onboarding, day-one detection set anchored to MITRE ATT&CK, OT/CUI/identity overlays, triage and tuning. |

