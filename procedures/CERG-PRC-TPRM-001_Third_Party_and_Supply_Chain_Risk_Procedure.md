## THIRD-PARTY AND SUPPLY CHAIN RISK PROCEDURE
### Vendor Tiering · Evidence by Tier · Contract Clauses · SBOM · International Access · Supply Chain Compromise Team (SCCT)

---

| | |
|---|---|
| **Document ID** | CERG-PRC-TPRM-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Vendor Risk Analyst |
| **Parent Policy** | [CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [CERG-GOV-CB-001](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) · [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) · [CERG-STD-OT-001](../standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) · [CERG-STD-CUI-001](../standards/CERG-STD-CUI-001_CUI_Handling_Standard.md) · [CERG-STD-CR-001](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) · [CERG-PRC-RM-001](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) · [CERG-PRC-AR-001](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) · [CERG-PLN-IR-001](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md) |
| **Review Cycle** | Annual / On major TPRM platform change |
| **Frameworks** | [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) (SR) · NIST 800-161r1 · [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (GV.SC) · ISO 27036 · CSA STAR · NTIA SBOM minimum elements |
| **Regulations** | NERC-CIP CIP-013 · DFARS / [CMMC L2](https://dodcio.defense.gov/CMMC/) · SOX ITGC · FedRAMP equivalency |
| **Environments** | All third-party-touched scopes - SaaS · IaaS/PaaS · OT vendors · CUI subcontractors · MSPs · software suppliers · hardware suppliers |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Roles and Interface to Procurement / ERM / BR](#2-roles-and-interface-to-procurement--erm--br)
3. [Vendor Tiering](#3-vendor-tiering)
4. [Cyber-Specific Score Adjustment](#4-cyber-specific-score-adjustment)
5. [Evidence by Tier](#5-evidence-by-tier)
6. [Differences by Vendor Type](#6-differences-by-vendor-type)
7. [Approved Provider and SaaS Catalog](#7-approved-provider-and-saas-catalog)
8. [Contract Security Clause Library](#8-contract-security-clause-library)
9. [Shared Responsibility Matrix](#9-shared-responsibility-matrix)
10. [International Access, Denied by Default](#10-international-access--denied-by-default)
11. [SBOM and Software Integrity](#11-sbom-and-software-integrity)
12. [CIP-013 Supply Chain Plan](#12-cip-013-supply-chain-plan)
13. [CUI Subcontractor Flow-Down](#13-cui-subcontractor-flow-down)
14. [FedRAMP Equivalency Evidence](#14-fedramp-equivalency-evidence)
15. [Supply Chain Compromise Team (SCCT)](#15-supply-chain-compromise-team-scct)
16. [Continuous Monitoring and Re-Assessment](#16-continuous-monitoring-and-re-assessment)
17. [Regulatory and Framework Alignment Summary](#17-regulatory-and-framework-alignment-summary)
18. [Document Control](#18-document-control)

---

## 1. Purpose and Scope

The policy makes third-party and supply-chain security Principle 8. Subordinate standards each impose specific requirements: IT/cloud/SaaS approval and attestation tracking, OT vendor assessment and CIP-013, CUI flow-down and FedRAMP equivalency, SBOM and software integrity. Until this procedure, those obligations had no shared operating model.

This procedure defines how CERG engages with the broader enterprise vendor program, where CERG's cyber-specific work begins and ends, what evidence is collected at each tier, and how the program responds when a vendor is compromised. It operationalizes the edge types defined in the [Edge Register](../governance/CERG-GOV-EDG-001_Edge_Register.md) — specifically the Vendor, SaaS, and Software Supply edges.

> **CERG Doesn't Own Vendor Management, It Owns the Cyber Slice**
>
> Procurement, Enterprise Risk Management, and Business Resiliency typically own vendor tiering, contract lifecycle, and business continuity. CERG accepts the business tier as the starting point and adjusts only where cyber-specific concerns are material enough to alter it. This boundary is the difference between a TPRM program that ships and one that drowns in vendors.

---

## 2. Roles and Interface to Procurement / ERM / BR

| **Function** | **Owns** | **CERG Interface** |
|---|---|---|
| **Procurement** | Vendor onboarding, contracts, master vendor record. | CERG reviews proposed contracts for security clauses; SCCT escalation routes through Procurement for contractual remedies. |
| **Enterprise Risk Management (ERM)** | Enterprise vendor tier, criticality, business-impact rating. | CERG accepts the business tier as input; adjusts only per Section 4. |
| **Business Resiliency** | Vendor continuity, exit plans. | CERG cyber-recovery expectations feed BR vendor recovery plans. |
| **Legal (external)** | Contract negotiation, regulatory flow-down, privacy notices. | CERG provides cyber clauses (Section 8); Legal owns negotiation. |
| **Vendor Risk Analyst** | This procedure. Vendor cyber assessments, SCCT, evidence-by-tier, continuous monitoring. | - |
| **Governance Pillar Leader** | Cyber audit interface; regulator-facing artifacts ([CMMC](https://dodcio.defense.gov/CMMC/) SSP, CIP-013 plan). | - |
| **Business / Asset Owners** | Vendor relationship; business-side acceptance of vendor-related risk. | Sign off on residual cyber risk per [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md). |

---

## 3. Vendor Tiering

CERG uses a 5-tier vendor model that maps to the typical enterprise model. Business rating sets the baseline; CERG adjusts only via Section 4.

| **Tier** | **Description** | **Examples** |
|---|---|---|
| **T1 - Critical** | Failure or compromise has material business, safety, regulatory, or financial impact. | Core ERP SaaS, primary cloud provider, OT vendor with operator presence, IDP, EDR. |
| **T2 - Significant** | Failure or compromise materially disrupts operations or exposes Restricted/CUI data. | CRM SaaS, Tier 1 SaaS holding sensitive data, financial-system MSP. |
| **T3 - Standard** | Failure or compromise is operationally inconvenient but recoverable in days. | Productivity SaaS, secondary tooling. |
| **T4 - Limited** | Minor business impact; no Restricted data; bounded blast radius. | Marketing tools, training providers. |
| **T5 - Transactional** | One-off purchase, commodity goods, no system access, no data access. | Office supplies, conference services. |

### 3.1 Tiering Inputs

CERG accepts the **business tier** from ERM / Procurement as the starting point. Inputs include data classification handled, system access granted, regulatory scope, blast radius, and operational dependency.

---

## 4. Cyber-Specific Score Adjustment

CERG adjusts the vendor tier *up* only when one or more cyber-specific concerns are material. Adjustments down (vendor "isn't as critical as Business says") are not permitted, Business owns criticality.

### 4.1 Adjustment Triggers

| **Cyber Concern** | **Adjustment** |
|---|---|
| Vendor has privileged access to in-scope systems | +1 tier |
| Vendor processes / stores Restricted, CUI, or BCSI data | +1 tier (to T1 if CUI/BCSI) |
| Vendor handles OT integration or BES Cyber System interaction | +1 tier (to T1 if BCS) |
| Vendor has a recent (≤ 12 months) material breach affecting its customers | +1 tier with case-by-case review |
| Vendor is operating below the evidence floor for its proposed tier | hold at lower tier until evidence is current |
| Vendor's product / service supports a SOX-relevant business process | +1 tier if not already T2+ |
| Vendor product is software shipped to be deployed in our environment with execution privilege, network reach, update authority, and ability to impact enterprise operations| +1 tier |
| Vendor relationship requires non-US access to in-scope systems / data | +1 tier (and see Section 10) |

> **Adjustments Are Documented, Not Negotiated**
>
> Every cyber-driven tier adjustment is recorded in the TPRM tool with the trigger, evidence, and reviewer. If a Business Owner disagrees, the resolution path is [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) Section 8, never an off-record handshake.

---

## 5. Evidence by Tier

Evidence requirements grow with tier. The table below names the cyber evidence required *at minimum*; specific subordinate standards may require more (e.g., FedRAMP for CUI scope).

| **Evidence** | **T5** | **T4** | **T3** | **T2** | **T1** |
|---|---|---|---|---|---|
| SOC 2 Type II (or ISO 27001) attestation, current | - | optional | required | required | required |
| SOC 2 carve-outs and CUECs reviewed | - | - | - | required | required |
| ISO 27001 certificate (where SOC 2 not applicable) | - | optional | required | required | required |
| FedRAMP authorization (Moderate or High) for CUI / federal scope | - | - | - | required (CUI) | required (CUI) |
| FedRAMP equivalency documentation per Section 14 | - | - | - | required (CUI, where applicable) | required (CUI, where applicable) |
| [CMMC](https://dodcio.defense.gov/CMMC/) Level (1 or 2) status for CUI subcontractor | - | - | - | required (CUI) | required (CUI) |
| Penetration test summary (sanitized) | - | - | - | required | required |
| SIG / CAIQ questionnaire (or CERG equivalent) | - | - | optional | required | required |
| SBOM for software products in use | - | - | required (software) | required | required |
| Hardware Bill of Materials (HBOM) | - | - | - | optional | required (OT / hardware in BES scope) |
| Subprocessor list and CUEC review | - | - | required (SaaS) | required | required |
| Right-to-audit clause | - | - | optional | required | required |
| Breach / incident notification commitment (timing, scope) | - | required | required | required | required |
| Insurance: cyber liability, E&O, where contract-appropriate | - | optional | required | required | required |
| OT vendor: NERC-CIP CIP-013 plan participation | - | - | - | required (OT) | required (OT / BES) |
| Inheritance Evidence Package (per [`CERG-GOV-CB-001`](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) Section 5) for inherited controls | - | - | - | required | required |
| Country-of-access disclosure and country-risk rating | - | - | required | required | required |

### 5.1 Evidence Currency

- T1 evidence is reviewed annually, no later than 30 days before attestation expiry.
- T2 evidence is reviewed annually.
- T3 evidence is reviewed every 24 months unless conditions change.
- T4/T5 evidence is reviewed on contract renewal.

Material vendor events (breach, ownership change, regulator action) trigger an out-of-cycle review regardless of tier.

---

## 6. Differences by Vendor Type

Requirements differ by what the vendor *is*. The table below summarizes the most-different requirements; subordinate standards govern detail.

| **Vendor Type** | **Distinctive Requirements** |
|---|---|
| **SaaS provider** | Approved Provider Catalog (Section 7); shared responsibility matrix (Section 9); CSPM/SSPM coverage on the consumer side; tenant configuration baseline per [`CERG-STD-CFG-001`](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md). |
| **IaaS / PaaS provider** | Landing zone baseline; CMK or BYOK per [`CERG-STD-CR-001`](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md); provider attestation including service-in-scope reconciliation; sub-service organization carve-outs. |
| **OT vendor** | CIP-013 plan participation; SBOM; firmware integrity verification; 24-hour incident notification commitment; engineering-controlled remote access; on-site presence vetting. |
| **CUI subcontractor** | DFARS / 252.204-7012 flow-down; [CMMC L2](https://dodcio.defense.gov/CMMC/) status; incident notification cooperation (DC3); CUI handling commitment with same controls as us. |
| **Managed Service Provider (MSP)** | Privileged access via PAM ([`CERG-STD-AC-001`](../standards/CERG-STD-AC-001_Access_Management_Standard.md)); session recording; named-individual accounts; geographic-access controls; tenant separation evidence. |
| **Software supplier (commercial / open source)** | SBOM (NTIA minimum elements); CVE / advisory subscription; software integrity (signed releases); patch / EOL commitments. |
| **Hardware supplier (esp. OT)** | HBOM where in BES scope; chain-of-custody; firmware integrity; tamper-evidence; secure delivery. |


### 6.1 Low-Control / High-Dependency Operating Model

Not every provider relationship allows the organization to configure, monitor, patch, or test. CERG recognizes four control levels that determine what can be required of a provider and how residual risk is managed.

| Control Level | What the Org Can Do | Examples | CERG Approach |
|---------------|---------------------|----------|---------------|
| **Direct Control** | Configure, monitor, patch, test | Owned servers, self-managed cloud workloads, on-premise network | Standard CERG controls: baselines, scanning, change management, evidence collection |
| **Shared Control** | Configure tenant, require evidence, validate logs | SaaS tenants (M365, Salesforce), IaaS/PaaS (AWS, Azure) | Customer-side evidence: IdP exports, KMS inventory, SIEM source inventory, backup config, tenant configuration scans |
| **Contractual Control** | Negotiate clauses, notification, audit rights | MSPs, managed security providers, subprocessors | Contract language, annual evidence collection (SOC 2, ISO 27001), incident notification commitments, tested kill-switch |
| **Opaque Dependency** | Track residual risk, exit plan, kill switch, compensating monitoring | SaaS vendor's underlying infrastructure, open-source library maintainers, upstream cloud provider outages | Documented residual risk acceptance, exit/migration plan, compensating monitoring (CSPM/SSPM for visible surface), documented assumption register |

The control level is recorded per provider in the Approved Provider Catalog and re-assessed at each annual review. A provider at Contractual or Opaque levels must have a documented kill-switch procedure tested at least annually.

> **CERG does not pretend to control what it cannot control.** The distinction between "we require this" and "we hope this" is not a compliance failure — it is operational honesty. Document the gap, monitor what is visible, plan the exit.

### 6.2 MSP and MSSP Hard Requirements

Managed Service Providers and Managed Security Service Providers operate inside the organization's trust boundary with elevated access. The following requirements apply to every MSP/MSSP relationship, regardless of tier:

| Requirement | Description | Verification |
|-------------|-------------|-------------|
| **Named accounts only** | Every provider user accessing organizational systems operates under a uniquely identifiable, named account. Shared, generic, or role-based accounts are prohibited. | Quarterly access review; IdP audit log |
| **PAM or brokered access** | Provider access is brokered through a Privileged Access Management (PAM) solution per [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md). Direct RDP, SSH, or VPN with standing credentials is prohibited. | PAM session logs; monthly access review |
| **No standing global admin** | No provider account holds standing global administrator, domain admin, or equivalent superuser privilege. Privilege is elevated per-session, per-task, with justification logged. | PAM elevation log; quarterly privileged group audit |
| **Customer-owned logs** | All provider activity logs are owned by the customer organization and stored in customer-controlled infrastructure. The provider shall not delete, modify, or restrict access to logs of their own activity. | SIEM source verification; quarterly log completeness check |
| **Break-glass process** | A documented break-glass procedure exists for emergency provider access that cannot follow the normal PAM path. Break-glass use triggers immediate notification to the CISO and is reviewed within 24 hours. | Break-glass event log; quarterly review of all break-glass activations |
| **Kill-switch procedure tested quarterly** | A documented procedure exists to revoke all provider access within 60 minutes of activation. The procedure is tested at least quarterly and test results are logged. The machine-readable kill-switch schema in [`machine-readable/`](../machine-readable/) provides the artifact format. | Quarterly test log; time-to-revoke measurement |
| **Provider access reviewed like privileged internal access** | Provider access is subject to the same access review cadence, recertification requirements, and anomalous-access detection as internal privileged users per [CERG-PRC-AC-002](CERG-PRC-AC-002_Access_Management_Runbook.md). | Access review records; recertification status |
| **Separate incident path for provider compromise** | A documented incident response path exists for "provider compromise with uncertain blast radius." This path is distinct from standard incident response — it assumes the attacker may have visibility into the organization's incident coordination channels if the provider's systems are compromised. | SCCT activation records; annual tabletop exercise |

**MSP/MSSP onboarding requires:** contract language covering all eight requirements, evidence of the provider's own security posture (SOC 2 Type II or equivalent), a completed shared responsibility matrix, and a successful kill-switch test before production access is granted.

**MSP/MSSP offboarding requires:** revocation of all access within 24 hours of contract termination, confirmation that provider-owned artifacts (logs, configurations, credentials) have been returned or destroyed, and a final access review confirming no residual access paths remain.


---

## 7. Approved Provider and SaaS Catalog

CERG maintains an Approved Provider and SaaS Catalog as the system-of-record for which third-party services may be procured for which scope.

| **Field** | **Definition** |
|---|---|
| Provider Name / Service | - |
| Vendor Tier | Per Section 3 + Section 4 adjustments |
| Approved Scopes | None / Public / Internal / Restricted / CUI / BCSI / SOX-relevant / BES-relevant |
| Data Residency Constraints | Approved regions / regions explicitly prohibited |
| Last Evidence Review | Date and reviewer |
| Next Required Review | - |
| Outstanding Risks | Risk register IDs |
| Inheritance Evidence | Y/N - link |
| Status | Approved · Approved-with-Conditions · Conditional Use Only · Sunset · Prohibited |

Procurement consults the catalog at intake; CERG updates it at each evidence cycle and after each SCCT closure.

---

## 8. Contract Security Clause Library

CERG provides Legal with a clause library; Legal owns negotiation. Clauses below are the minimums to seek; alternative language with equivalent intent is acceptable.

| **Clause** | **Required For** | **Substantive Content** |
|---|---|---|
| Security controls baseline | T2+ | Vendor commits to maintain controls aligned to a named standard ([NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final), [NIST CSF 2.0](https://www.nist.gov/cyberframework), ISO 27001) for the data and access in scope. |
| Incident notification | All accessing data/systems | Notification within 24 hours (T1/OT/BES) or 72 hours (T2) of confirmed incident affecting customer data or services. |
| Right to audit | T2+ | Documented audit rights, including evidence on request, with reasonable notice; alternatives include current SOC 2/ISO/FedRAMP report. |
| Subprocessor consent | SaaS T2+ | Customer-facing list of sub-processors; notification on change. |
| Data location | All processing Restricted/CUI/BCSI | Defined regions; no data movement to non-approved regions without consent. |
| Encryption | All processing Restricted/CUI | TLS in transit; FIPS-validated where required; CMK / BYOK rights documented per [`CERG-STD-CR-001`](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md). |
| Return / destruction of data | All processing customer data | On termination; documented method and timeline; certification. |
| Vulnerability and patch | Software / hardware suppliers | Vendor commits to remediation SLAs aligned to severity; advisory publication. |
| SBOM | Software suppliers (T1/T2) | SBOM at NTIA minimum elements at delivery and at material update. |
| Background checks | MSPs / vendors with privileged access | Background screening; named-individual access; geographic-access controls. |
| Insurance | T2+ | Cyber liability and E&O at industry-appropriate levels. |
| Cooperation | All accessing data/systems | Cooperation in incident investigations and regulator inquiries. |
| Flow-down | CUI subcontractors | DFARS 252.204-7012 / [CMMC](https://dodcio.defense.gov/CMMC/) requirements flowed to sub-tier. |
| CIP-013 | OT vendors in BES scope | Participation in supply chain security plan including software integrity, incident notification, coordination of access controls. |
| International access | T2+ where international access proposed | Country-of-access disclosure; right to refuse non-approved geographies. |

---

## 9. Shared Responsibility Matrix

Every T2+ cloud / SaaS provider has a Shared Responsibility Matrix on file. Where the vendor publishes one, CERG annotates it; where they don't, CERG produces it and seeks vendor confirmation.

| **Control Area** | **Provider Owns** | **Customer Owns** | **Customer-Side Evidence Reference** |
|---|---|---|---|
| Physical security | Provider | - | - |
| Hypervisor / base platform | Provider | - | - |
| Tenant isolation | Provider | Configuration | DISH scan / SSPM |
| Identity / authentication | Provider provides; Customer configures | Customer configures | IdP policy export |
| Encryption (rest / transit) | Provider provides; Customer chooses CMK/BYOK | Customer configures | KMS inventory |
| Logging | Provider provides; Customer routes | Customer routes | SIEM source inventory |
| Detection | Provider provides limited; Customer extends | Customer extends | Detection coverage |
| Recovery / backup | Provider depending on service | Customer-driven for CUI / SOX / Tier 1 | Backup config |
| Configuration management | Provider for service; Customer for tenant | Customer | DISH scan |
| Subprocessor management | Provider | Customer accepts / refuses | Sub-processor list |

The matrix is the single source of truth for cross-team conversations about "who handles X."

---

## 10. International Access: Denied by Default

International access to in-scope systems and data is **denied by default**. Where business need requires it, access is treated as a documented exception with conditions.

### 10.1 Operating Model

- A **Country Risk Register** classifies each country into tiers: Permitted · Restricted · Conditional · Prohibited.
- Permitted countries are those with established trust relationships, low geopolitical risk, and acceptable law-enforcement / data-protection regimes; access is allowed without exception (logged, monitored).
- Restricted countries require an exception per [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md), with named controls (managed-device-only, session recording, enhanced detection routing).
- Conditional countries require additional senior exec / CISO approval, time-boxed access windows, and possible per-session approval.
- Prohibited countries do not get access; business need is resolved by alternative means (US-based delivery, alternate vendor).
- The Country Risk Register is reviewed at least quarterly; geopolitical events can trigger reclassification at any time.
- All international access is logged to SIEM with country-of-access metadata; the SOC routing pack includes country-tier as a fast-triage field.

### 10.2 Vendor Implications

- Vendors must disclose all proposed countries of access at onboarding and at any change.
- Vendor international-access tier above the country's permitted level triggers a contract addendum and exception.
- Vendor non-disclosure of country-of-access discovered post-onboarding is a material event triggering SCCT.

---

## 11. SBOM and Software Integrity

### 11.1 SBOM Collection — Tiered Requirements

| **Requirement** | **T1 Vendor** | **T2 Vendor** | **T3 Vendor (Software)** | **T3 Vendor (Non-Software)** | **Internal Builds** |
|---|---|---|---|---|---|
| SBOM at delivery (NTIA minimum elements) | Required | Required | Required | N/A | Required (CI-generated) |
| SBOM at material update | Required | Required | Required | N/A | Required (CI-generated) |
| SBOM format | CycloneDX or SPDX | CycloneDX or SPDX | CycloneDX or SPDX | N/A | CycloneDX (preferred) |
| SBOM scan for known vulnerabilities | Required (on receipt + quarterly) | Required (on receipt + semi-annual) | Required (on receipt) | N/A | Required (pipeline gate) |
| VEX for findings | Required for Critical/High | Required for Critical/High | Recommended | N/A | Required for Critical/High |
| License risk review | Required | Required | Recommended | N/A | Required (policy gate) |
| Embedded secrets scan | Required | Required | Recommended | N/A | Required (pipeline gate) |
| SBOM recorded in CERG registry (machine-readable/cerg-sbom-schema.yaml) | Required | Required | Required | N/A | Required |
| Evidence link in TPRM tool | Required | Required | Required | N/A | Required |

**Material update** = new minor/major version, security patch release, or dependency change affecting >10% of components.

**SBOM delivery method:** Vendor provides via secure channel (TPRM portal, signed email, or API). Internal builds generate in CI/CD per Section 11.3.

### 11.2 SBOM Processing Pipeline

1. **Ingest:** SBOM received → validate format (CycloneDX/SPDX) → parse components
2. **Scan:** Cross-reference components against NVD, GHSA, vendor advisories → findings → PRC-VM-001 pipeline
3. **Enrich:** Map to `machine-readable/cerg-sbom-schema.yaml` fields → store in SBOM registry
4. **VEX:** Request/validate VEX from vendor for Critical/High findings → record `vex_status`
5. **Approve:** Governance reviews → `approval_status` set → evidence linked in TPRM tool
6. **Monitor:** Quarterly re-scan for T1/T2; pipeline scan on every build for internal

### 11.3 Internal SBOM Generation (CI/CD Integration)

All internal production builds shall generate an SBOM as a pipeline artifact:

- **Build-time:** Generate CycloneDX SBOM from lockfiles / dependency graph (Syft, Trivy, or language-native tool)
- **Scan:** Immediate vulnerability scan against generated SBOM — fail build on Critical/High without VEX
- **Sign:** Cosign/Sigstore sign the SBOM artifact
- **Publish:** Push SBOM to artifact registry and CERG SBOM registry (machine-readable consumer)
- **Gate:** Production promotion requires `approval_status = approved` for the build's SBOM

Pipeline snippet reference: `tools/sbom-generate.sh` (see below).

### 11.4 Software Integrity

- Releases signed by the vendor; signatures verified before deployment.
- Container images signed (cosign / sigstore); admission gate per [`CERG-STD-CFG-001`](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) Section 7.
- Firmware (OT) verified per [`CERG-STD-OT-001`](../standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md); firmware updates follow CIP-010 process per [`CERG-PLN-CIP-001`](../plans/CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md).

---

## 12. CIP-013 Supply Chain Plan

For BES Cyber Systems, CERG maintains a CIP-013 Supply Chain Risk Management Plan as a [CERG-PLN-CIP-001](../plans/CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md) component, satisfying CIP-013-2 R1. The plan includes:

- Identification of supply chain risks across procurement and installation.
- Vendor security controls expectations (incident notification, coordination of access controls, software integrity, vendor remote access management, disclosure of known vulnerabilities).
- Procurement controls, clauses, evaluation, approvals.
- Implementation and verification, how controls are verified at installation and over time.
- Coordination with this procedure: vendor records here are CIP-013 records.

---

## 13. CUI Subcontractor Flow-Down

| **Requirement** | **Source** |
|---|---|
| DFARS 252.204-7012 flow-down to subcontractors handling CUI | DFARS |
| [CMMC](https://dodcio.defense.gov/CMMC/) Level 2 third-party assessment status verification | DoD / [CMMC](https://dodcio.defense.gov/CMMC/) |
| Incident notification cooperation, including DC3 reporting | DFARS |
| Same encryption / handling requirements as the prime | [`CERG-STD-CUI-001`](../standards/CERG-STD-CUI-001_CUI_Handling_Standard.md) + [`CERG-STD-CR-001`](../standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) |
| CUI Subcontractor Register maintained | [`CERG-PLN-CUI-001`](../plans/CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md) |

---

## 14. FedRAMP Equivalency Evidence

Where a CUI-relevant SaaS / cloud service is not FedRAMP-authorized but is proposed for use, CERG requires a documented FedRAMP-equivalency package:

- SOC 2 Type II with [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) Moderate baseline mapping.
- 3PAO-equivalent assessment letter or independent assessor attestation.
- Customer-side configuration commitments (CUI label, region, key control).
- Sub-service organization carve-outs reconciled.
- Re-papering trigger documented (FedRAMP authorization issued, attestation lapses, scope change).

The package is recorded in the TPRM tool as the vendor's Inheritance Evidence Package for the CUI overlay.

---

## 15. Supply Chain Compromise Team (SCCT)

When a vendor reports, or is publicly disclosed as having, a material cybersecurity incident affecting their service or product, CERG activates the **Supply Chain Compromise Team (SCCT)**.

### 15.1 SCCT Membership

At minimum:

- **SOC / Incident Response lead**: coordinates investigation and customer-side detection / containment.
- **CERG, Risk (TPRM)**: vendor liaison; assembles vendor-supplied facts; updates TPRM record.
- **CERG, Governance**: regulator notification path; CUI / NERC-CIP / SOX reporting if applicable.
- **Legal**: contractual remedies, regulator interface, communications review.
- **Procurement**: vendor relationship; commercial leverage.
- **Business Owner of the affected service**: operational decision authority; user / customer communications.

Other invitees as needed: CISO (declared briefing), Privacy (PII implications), Engineering, OT operations (OT vendors), Communications.

### 15.2 SCCT Activation Triggers

- Confirmed vendor breach affecting our data, systems, or service.
- Material vulnerability in a deployed vendor product (e.g., critical CVE, supply-chain implant).
- Vendor's regulator action affecting our reliance on their service.
- Public reporting of a vendor compromise where our exposure is plausible.
- Vendor non-disclosure of country-of-access discovered.
- Discovery of unauthorized vendor sub-processor handling our data.

### 15.3 SCCT Workflow

1. **Activate.** TPRM declares SCCT, notifies membership within 4 business hours of trigger (1 business hour for T1 vendors).
2. **Assemble facts.** Vendor advisory, public reporting, internal exposure analysis (which systems, which data, which scopes).
3. **Contain.** Coordinate with SOC / IR on containment, credentials rotation, vendor session termination, IOC sweep, detection tuning.
4. **Decide.** Disposition: continue use with conditions / suspend use / terminate. Documented and owned by Business + CISO.
5. **Communicate.** Internal user / customer notification per Legal; regulator notification where required (CUI DC3, NERC-CIP O&P, SOX disclosure committee).
6. **Remediate.** Risk register entries, exception updates, contract addenda, monitoring uplift.
7. **Close.** SCCT after-action with lessons learned; feeds threat intelligence and detection.

### 15.4 SCCT Evidence

Every SCCT activation produces an SCCT record with: trigger, membership, timeline, decisions, notifications, risk register updates, vendor-side commitments. Records are retained for the longer of the vendor relationship + 3 years or the regulatory retention requirement.

> **Why a Named Team Instead of "We'll Pull People In"**
>
> Naming the team in advance, with a roster, a trigger, and a 4-hour clock, converts vendor compromise from a panicked phone-tree exercise into a procedure. The first SolarWinds-class event tests every assumption about your TPRM program; SCCT is how that test doesn't surprise you.

---

## 16. Continuous Monitoring and Re-Assessment

### 16.1 Automated Monitoring Signals

CERG continuously monitors the vendor landscape using automated signals. The following sources are integrated into the TPRM monitoring pipeline:

| **Signal Type** | **Source** | **Frequency** | **Action on Alert** |
|---|---|---|---|
| Security ratings service | Third-party security ratings provider | Continuous | Alert Vendor Risk Analyst for any score drop > 50 points or below tier threshold |
| Dark web monitoring | Threat intelligence platform | Continuous | Alert if organization credentials, source code, or PII attributed to a vendor appear on dark web sources |
| Certificate transparency logs | CT log monitors | Daily | Alert on anomalous certificate issuance for vendor domains |
| Vendor breach notifications | Direct notification, media monitoring, ISAC feeds | Continuous | Trigger SCCT activation per Section 15 if the breach affects services consumed by the organization |
| Sanctions and adverse media | Sanctions list providers, news monitoring | Weekly | Alert Vendor Risk Analyst; trigger Country Risk Register review if jurisdiction-related |
| Financial health indicators | Business credit monitoring | Quarterly | Alert for vendors with deteriorating financial posture (downgrade, bankruptcy filing, going concern opinion) |

### 16.2 Periodic Re-Assessment Triggers

Vendors are re-assessed on the following cadence based on tier:

| **Tier** | **Re-Assessment Cadence** | **Trigger Events (override cadence)** |
|---|---|---|
| T1 (Critical) | Annual | Vendor breach, material change in service, M&A activity, regulatory action against vendor |
| T2 (High) | Annual | Vendor breach, material change in service, M&A activity |
| T3 (Moderate) | 24 months | Vendor breach affecting the service consumed |
| T4 (Low) | Renewal-driven | Re-assess at contract renewal; trigger if service scope expands |
| T5 (Business Default) | Renewal-driven | Re-assess if usage crosses into T4 territory |

### 16.3 Vendor Performance Metrics

The Vendor Risk Analyst tracks the following metrics for each T1 and T2 vendor:

| **Metric** | **Description** | **Review Cadence** |
|---|---|---|
| Evidence currency | % of required evidence artifacts that are current (within validity period) | Quarterly |
| Assessment completion timeliness | Whether re-assessments complete within the scheduled window | Quarterly |
| Finding remediation velocity | Mean time from finding issuance to closure, by severity | Quarterly |
| SCCT activation frequency | Number of SCCT activations involving the vendor | Quarterly |
| Contractual compliance | Adherence to security obligations, RTO/RPO commitments, and notification SLAs | Annual |

### 16.4 Escalation Paths for Deteriorating Vendor Posture

| **Condition** | **Escalation** | **Action** |
|---|---|---|
| Security rating drops below tier threshold | Vendor Risk Analyst | Immediate review; request remediation plan from vendor within 10 business days |
| Vendor breach with potential organizational impact | SCCT Lead per Section 15 | Activate SCCT; assess containment and exposure |
| Critical finding open > 90 days without remediation plan | Vendor Risk Analyst → Governance Pillar Leader | Escalate to vendor executive; consider contract remedies |
| Vendor refuses to provide required evidence | Vendor Risk Analyst → Engineering Pillar Leader → CISO | Risk acceptance required; if unacceptable, initiate vendor transition planning |
| Financial distress indicators | Vendor Risk Analyst → Governance Pillar Leader | Develop contingency plan; identify alternative vendors |

### 16.5 Integration with Approved Provider Catalog

Continuous monitoring results directly affect the Approved Provider Catalog (APC) status values:

- **Green (Approved)**: All monitoring signals within acceptable thresholds; evidence current.
- **Amber (Conditional)**: One or more signals outside Green threshold; remediation plan accepted. Automatic review at 90 days.
- **Red (Restricted)**: Critical finding or breach unresolved; new engagements restricted until status returns to Amber or Green.
- **Black (Prohibited)**: Vendor determined to pose unacceptable risk; existing services transitioned off per the offboarding procedure.

### 16.6 Integration with Threat Intelligence

Vendor monitoring is integrated with [CERG-PRC-TI-001](CERG-PRC-TI-001_Threat_Intelligence_Procedure.md) for threat intelligence specific to vendors:

- The Threat Intelligence Analyst produces a **Vendor Risk Note** (per PRC-TI-001 §6.5) when threat intelligence reveals TTPs, CVEs, or campaign activity relevant to a vendor in the APC.
- Vendor-specific IOCs from threat intelligence are deployed to detection tooling per PRC-TI-001 §4.6.
- Quarterly threat briefings to the Vendor Risk Analyst summarize the threat landscape affecting the vendor portfolio.

### 16.7 Vendor Offboarding

When a vendor relationship ends, a structured offboarding process ensures access is revoked, data is retrieved or destroyed, and residual obligations are met.

#### Offboarding Triggers

| **Trigger** | **Description** |
|---|---|
| Contract expiration | Normal end of contract term; vendor not renewed |
| Termination for cause | Vendor breach of contract, security incident, or performance failure |
| Vendor bankruptcy / dissolution | Vendor ceases operations |
| Strategic replacement | Organization transitions to an alternative vendor |

#### Offboarding Checklist

| **Step** | **Action** | **Owner** | **Timing** |
|---|---|---|---|
| 1 | Notify vendor; confirm effective date | Business Sponsor | Immediately |
| 2 | Disable all vendor user accounts | Identity Engineer | Effective date or within 24 hours |
| 3 | Revoke vendor API keys, OAuth grants, service principals | Identity Engineer / Cloud Security Engineer | Effective date |
| 4 | Rotate shared secrets vendor had access to | Cryptography Engineer | Within 5 business days |
| 5 | Deauthorize SSO / federation | Identity Engineer | Effective date |
| 6 | Remove vendor from Approved Provider Catalog (status = Offboarded) | Vendor Risk Analyst | Within 5 business days |
| 7 | Confirm data retrieval or destruction per contract | Business Sponsor + Legal | Per contract |
| 8 | Update TPRM record | Vendor Risk Analyst | Within 10 business days |

#### Post-Termination

Surviving contractual clauses (confidentiality, data handling, audit rights) remain in effect. Evidence is retained per [CERG-PRC-AUD-001](CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md). Offboarding completion is signed off by the Vendor Risk Analyst and Business Sponsor.

### 16.8 Fourth-Party Risk Management

Fourth-party risk arises when a critical vendor relies on subcontractors (sub-processors) the organization does not have a direct relationship with.

#### Disclosure Requirements

- T1 and T2 vendors must disclose all critical sub-processors
- Vendors must notify the organization of sub-processor changes at least 30 days before the change
- The organization reserves the right to object; the vendor must provide an alternative or allow contract termination without penalty

#### Evidence for Critical Sub-Processors

| **Evidence** | **When Required** |
|---|---|
| SOC 2 Type II report | Sub-processors hosting or processing the organization's data |
| ISO 27001 certification | Acceptable alternative for international sub-processors |
| Inheritance evidence | Vendor's own assessment, if methodology is reviewed and approved |

#### Concentration Risk

The Vendor Risk Analyst monitors for multiple vendors relying on the same sub-processor. If a single sub-processor supports ≥ 3 T1/T2 vendors, a formal concentration risk assessment is conducted.

---

### 16.9 Business Continuity and Disaster Recovery (BCDR) for Vendors

Critical and high-tier vendors must demonstrate BCDR capability proportional to the criticality of the service they provide.

#### BCDR Requirements by Tier

| **Tier** | **BCDR Requirement** | **Evidence** |
|---|---|---|
| T1 (Critical) | Documented BCDR plan; RTO ≤ 4 hours; RPO ≤ 1 hour; annual functional BCDR test | BCDR plan summary; test results |
| T2 (High) | Documented BCDR plan; RTO ≤ 24 hours; RPO ≤ 4 hours; annual tabletop or functional test | BCDR plan summary; test results |
| T3 (Moderate) | BCDR plan or equivalent; RTO/RPO appropriate to service | BCDR plan acknowledgment |
| T4 (Low) | BCDR capability acknowledged in contract | Contractual commitment |
| T5 (Business Default) | None required beyond standard terms | - |

#### RTO/RPO Expectations

RTO (Recovery Time Objective) and RPO (Recovery Point Objective) expectations are set based on the organization's dependency on the vendor:

- If the organization's own Tier 1 service depends on the vendor, the vendor's RTO must be ≤ the organization's RTO for that service.
- If the vendor processes regulated data (CUI, SOX), RPO must be ≤ 1 hour.
- RTO/RPO commitments are documented in the contract and reviewed at each vendor re-assessment.

#### BCDR Assessment

During vendor assessment, the Vendor Risk Analyst evaluates:
- Does the vendor have a documented BCDR plan?
- Has the plan been tested? When? What was the outcome?
- Are RTO/RPO commitments compatible with the organization's requirements?
- Does the vendor's BCDR plan account for dependencies on its own critical sub-processors?

Assessment results are recorded in the TPRM tool and reviewed at each re-assessment cycle.

### 16.10 Metrics

| **KPI** | **Formula** | **Source** | **Refresh** | **Green** | **Amber** | **Red** |
|---|---|---|---|---|---|---|
| Vendors assessed on time | % of vendors with assessment completed within scheduled window | TPRM tool | Quarterly | ≥ 95% | 85–94% | < 85% |
| Average assessment time | Mean calendar days from assessment start to completion | TPRM tool | Quarterly | ≤ 30 days | 31–45 days | > 45 days |
| Vendors by tier | Count of active vendors per tier (T1–T5) | TPRM tool | Monthly | - | - | - |
| Active exceptions | Count of open vendor-related risk exceptions | Risk register | Monthly | 0 | 1–5 | > 5 |
| Vendor risk trend | % of vendors with improving / stable / declining risk posture | TPRM tool | Quarterly | ≥ 80% stable or improving | 60–79% | < 60% |
| Evidence currency | % of T1/T2 vendors with all required evidence current | TPRM tool | Monthly | ≥ 95% | 85–94% | < 85% |
| SCCT activation frequency | Count of SCCT activations | SCCT log | Quarterly | 0 | 1 | ≥ 2 |
| Fourth-party concentration | Count of sub-processors supporting ≥ 3 T1/T2 vendors | TPRM tool | Quarterly | 0 | 1 | ≥ 2 |

## 17. Regulatory and Framework Alignment Summary

| **Regulation / Framework** | **Where in This Procedure** |
|---|---|
| [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) SR family | All sections |
| NIST 800-161r1 | All sections; especially 11–15 |
| [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (GV.SC) | Sections 2–6, 15 |
| ISO 27036 | Sections 5, 8, 9 |
| DFARS 252.204-7012 / [CMMC L2](https://dodcio.defense.gov/CMMC/) | Sections 13, 14 |
| NERC-CIP CIP-013 | Section 12 |
| FedRAMP / FedRAMP equivalency | Section 14 |
| NTIA SBOM minimum elements | Section11 |
| SOX ITGC | Cross-cutting; vendor SOC 1 reuse where applicable |

---

## 18. Document Control

| | |
|---|---|
| **Document ID** | CERG-PRC-TPRM-001 |
| **Version** | 1.0 |
| **Approved By** | CISO |
| **Next Review** | Annual / TPRM platform change |
| **Change Log** | 1.0 - Initial publication. Tiering, evidence by tier, shared responsibility, international access denial-by-default, SBOM, CIP-013, CUI flow-down, FedRAMP equivalency, SCCT. |
