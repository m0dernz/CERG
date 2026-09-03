## EXPOSURE MANAGEMENT PROCEDURE
### From Scanner Observation to Managed Risk · Six-Step Model · Patch Hygiene

---

| | |
|---|---|
| **Document ID** | CERG-PRC-VM-001 |
| **Version** | 2.02 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Exposure Management Lead |
| **Parent Policy** | [CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Standards** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) · [CERG-STD-OT-001](../standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) · [CERG-STD-CUI-001](../standards/CERG-STD-CUI-001_CUI_Handling_Standard.md) · [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) · [CERG-STD-CFG-001](../standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) |
| **Review Cycle** | Annual / Upon Significant Change / Major Tooling Change |
| **Frameworks** | [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) · [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST 800-171r3](https://csrc.nist.gov/pubs/sp/800/171/r3/final) · NIST 800-40r4 · NIST RMF |
| **Regulations** | NERC-CIP CIP-007 R2 · CMMC RA.L2 · SOX ITGC |
| **Environments** | All in-scope assets - owned, hybrid, cloud, SaaS, OT |

---

## Table of Contents

1. [Purpose and Philosophy](#1-purpose-and-philosophy)
2. [The Exposure State Model](#2-the-exposure-state-model)
3. [Roles and Responsibilities](#3-roles-and-responsibilities)
4. [Step 1 — Collect Observations](#4-step-1--collect-observations)
5. [Step 2 — Validate Asset and Condition](#5-step-2--validate-asset-and-condition)
6. [Step 3 — Validate Exposure Path](#6-step-3--validate-exposure-path)
7. [Step 4 — Classify](#7-step-4--classify)
8. [Step 5 — Select Treatment](#8-step-5--select-treatment)
9. [Step 6 — Verify Closure](#9-step-6--verify-closure)
10. [Patch Hygiene](#10-patch-hygiene)
11. [Risk Acceptance and Exceptions](#11-risk-acceptance-and-exceptions)
12. [Adversarial Validation](#12-adversarial-validation)
13. [Reporting and Metrics](#13-reporting-and-metrics)
14. [Regulatory and Framework Alignment](#14-regulatory-and-framework-alignment-summary)
15. [Procedure Control](#15-procedure-control)

---

## 1. Purpose and Philosophy

This procedure establishes CERG's exposure management program — the discipline of understanding which weaknesses actually threaten the organization, not which ones a scanner reports.

### 1.1 The Operating Premise

> **A scanner report is inventory data. It is not the exposure management program.**
>
> CERG does not measure its security posture by how many vulnerabilities a scanner finds. It measures posture by confirmed reachable exposure, by how quickly observations are triaged into decisions, and by whether treatment actually closes the exposure path. A program that reduces total findings while leaving Internet-exposed critical exposures open is not improving — it is reorganizing failure.

This procedure operationalizes Principle 5 of [CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md) through a fundamentally different lens than traditional scanner-driven vulnerability programs. The program does not start with "scan, score, SLA, patch/accept." It starts with the observation that most scanner output is noise, and the signal worth acting on is confirmed reachable exposure.

### 1.2 What This Procedure Replaces

This is version 2.0 of `CERG-PRC-VM-001`. The move to Exposure Management is deliberate. The core model has shifted from:

| Old Model | New Model |
|-----------|-----------|
| Scan → Score → SLA → Patch/Accept | Collect observations → Validate exposure → Classify → Treat → Verify |
| CVSS bands drive priority | Exposure path + asset criticality + KEV drive priority |
| "Critical" means CVSS ≥ 9.0 | "Material risk" means confirmed reachable exposure on a crown jewel |
| Patching is the default treatment | Treatment is selected from remove/block/config/patch/compensate/redesign/accept/transfer |
| Scanner report = vulnerability program | Scanner report = input signal requiring triage |

### 1.3 Scope

This procedure governs all in-scope assets: enterprise IT, cloud, SaaS, OT, CUI environments. Environment-specific overlays implement operational-safety adaptations for OT and evidence requirements for regulated environments.

---

## 2. The Exposure State Model

Every observation moves through a defined state pipeline. Progress between states is gated by explicit validation, not by elapsed time.

### 2.1 State Definitions

| State | Definition | Example |
|-------|-----------|---------|
| **Observed** | A tool-reported condition. No validation has occurred. | Scanner reports Apache CVE-2024-XXXX, CVSS 9.9, on host `web-07`. |
| **Validated** | The asset is confirmed real, in scope, and the affected software is present. | Host `web-07` is in inventory. Apache 2.4.51 is installed. |
| **Reachability Assessed** | The exposure path has been evaluated: is the service running? Reachable? Authenticated? Segmented? | Apache on `web-07` listens on port 8080, which is blocked at the firewall; only accessible from internal admin subnet. |
| **Exposure Confirmed** | A reachable, useful exploitation path exists. | The service is Internet-reachable, no WAF, authenticated API endpoint with known bypass. |
| **Treatment Selected** | A specific treatment has been chosen and assigned. | Engineering will apply patch ASF-2024-03 within 48 hours. |
| **Closure Verified** | The treatment has been applied and independently verified. | Re-scan confirms Apache 2.4.52. Reachability test confirms path closed. |

### 2.2 The Apache Example

> A CVSS 9.9 Apache finding on a host where Apache is not running, ports 80/443 are blocked, and no reachable service path exists is not a material vulnerability. It is a scanner observation until exposure is confirmed.
>
> A scanner can be technically correct — Apache 2.4.51 is installed, and CVE-2024-XXXX applies to that version — and still not identify exploitable exposure. The word "false positive" is the wrong bucket for many of these cases. The scanner was right about the software version. It was wrong about the risk.
>
> Use states, not a binary "real/false" toggle.

### 2.3 The "False Positive" Problem

A finding classed as a "false positive" in a traditional VM program may actually be:

| Reality | Traditional Label | CERG State |
|---------|------------------|------------|
| Software present, not running | False positive | Validated, not reachable |
| Software present, blocked at firewall | False positive | Validated, reachability assessed — not exposed |
| Software present, compensating control prevents exploitation | False positive | Validated, reachable — compensated |
| Scanner version-only match, fix backported | False positive | Scanner artifact — non-issue |
| Feature not in use | False positive | Validated, not applicable |

Each of these has different operational and audit implications. Collapsing them all into "false positive" loses the signal that distinguishes "this is fine" from "this isn't fine but we have a control."

---

## 3. Roles and Responsibilities

| Role | Exposure Management Responsibility |
|------|-----------------------------------|
| **Exposure Management Lead** | Owns this procedure. Operates observation collection, triage, classification, and tracking. Publishes exposure posture. Drives treatment cadence. Owns SLAs. |
| **Engineering Pillar Leader** | Implements treatments on assets it owns or supports. Defines secure configuration baselines. Provides architectural guidance for compensating controls. |
| **System / Asset Owners** | Accountable for treatment of exposures on assets they own. Approve maintenance windows, accept residual risk. |
| **IT / OT Operations Teams** | Execute treatment actions. Coordinate maintenance windows. Validate restoration. |
| **CISO** | Approves High and Critical risk acceptances where required by the canonical RMF authority table. Reviews exposure posture on defined cadence. |

---

## 4. Step 1 — Collect Observations

Observations arrive from many sources. They are aggregated into a single pipeline but are NOT called "findings" until validated. An observation is a signal that requires triage; it is not yet a fact.

### 4.1 Observation Sources

| Source | Description | Owner |
|--------|------------|-------|
| Authenticated vulnerability scans | Network-based scans of servers, endpoints, network devices | Risk |
| Container & image scans | Build-time and registry scans | Risk / Engineering |
| Cloud posture (CSPM) | Cloud control-plane misconfigurations | Risk |
| SaaS posture (SSPM) | Tier 1 SaaS configuration drift | Risk |
| Software composition analysis (SCA) | Open-source and library vulnerabilities | Engineering / Risk |
| SAST / DAST | Source-code and runtime application findings | Engineering / Risk |
| OT passive monitoring | Vulnerabilities from passive OT network analysis | Risk |
| Vendor advisories | Patches, fixes, bulletins | Risk |
| ISAC / regulator feeds | E-ISAC, CISA, ICS-CERT | Risk |
| Adversarial validation | Pen test, red-team, purple-team, cloud, OT-safe, or other authorized adversarial findings | Risk |
| Bug bounty / external researcher | Responsible disclosure | Risk |
| Incident-driven discovery | Vulnerabilities identified during/after incidents | Risk / Engineering |
| SBOM | Vulnerabilities in third-party components | Risk |

### 4.2 Observation Intake

All observations enter the pipeline with source metadata, a timestamp, and the raw severity/score reported by the tool. No SLA clock starts at this point. The clock starts at confirmation (Step 4).

### 4.3 External Reports and Supply Chain

External researcher reports and supply-chain advisories follow the same pipeline. See Sections 3.1 and 3.2 of the prior version for detailed intake workflows — those processes are unchanged and remain in force as operational sub-procedures.

---

## 5. Step 2 — Validate Asset and Condition

Before asking "is this dangerous," ask "is this real?"

### 5.1 Validation Criteria

| Question | Owner | Action if No |
|----------|-------|-------------|
| Is the asset in the authoritative inventory? | Risk | Escalate to CMDB owner; observe until inventory resolved |
| Is the asset in scope for exposure management? | Risk | Close as out-of-scope with rationale |
| Is the reported software/service/configuration present on the asset? | Risk / Engineering | Close as scanner artifact |
| Is the reported version accurate? (Check for backported fixes) | Engineering | Adjust version; re-evaluate |

### 5.2 Validation Timing

| Observation Severity | Validation Required Within |
|---------------------|--------------------------|
| KEV-listed or actively exploited | 4 hours |
| CVSS ≥ 9.0 | 24 hours |
| CVSS 7.0–8.9 | 3 business days |
| CVSS < 7.0 | 5 business days |

---

## 6. Step 3 — Validate Exposure Path

A validated condition is not automatically an exposure. This step asks: can an attacker actually reach this?

### 6.1 Exposure Path Assessment

| Question | Signals |
|----------|---------|
| Is the service running? | Process list, port scan, service status |
| Is it reachable? | Network path from Internet, from user population, from adjacent trust zones |
| Is authentication required? | Anonymous access vs. authenticated-only |
| Is the asset segmented? | Network ACLs, microsegmentation, jump-host-only access |
| Does a compensating control materially interrupt exploitation or impact? | Relevant CB-001 control ID; current CEF-001 and/or adversarial-validation evidence; evidence date and scope; known degradation conditions |
| Is there a plausible path to data, privilege, disruption, or lateral movement? | Data classification on asset, privilege level, blast radius |

When a compensating control is used to lower an exposure classification, defer treatment, or support residual-risk analysis, the Exposure Management record shall cite the relevant CB-001 control, current control-effectiveness or adversarial-validation evidence, evidence date, scope, and any known degradation or failure condition relevant to the path.

A claimed control is not sufficient. Absent, stale, irrelevant, failed, or degraded evidence cannot support a compensated disposition. The applicable control owner addresses a failed or degraded control through the relevant control-effectiveness, adversarial-validation, Governance, and treatment processes; Exposure Management consumes that result as path context. This does not change the risk-acceptance authority in RMF-001.

### 6.2 KEV Acceleration

If the observation matches a CISA Known Exploited Vulnerabilities (KEV) entry and the asset is confirmed real, the exposure path assessment is accelerated regardless of CVSS score. A KEV entry means active exploitation exists in the wild — the assessment shifts from "is this exploitable" to "is this already being exploited against us."

---

## 7. Step 4 — Classify

After validation and reachability assessment, every observation is classified into exactly one category. This classification drives treatment priority, not CVSS score.

### 7.1 Classification Taxonomy

| Classification | Definition | Treatment Approach | SLA Driver |
|---------------|-----------|-------------------|------------|
| **Non-issue / Scanner Artifact** | The observation does not represent a real condition (backported fix, version-only match, scanner error) | Close with evidence | N/A |
| **Hygiene Debt** | A real weakness exists but no reachable exposure path has been confirmed | Track; address in patch cycle | Patch hygiene cadence |
| **Confirmed Flaw, Not Currently Exposed** | The flaw exists on a reachable asset but a compensating control, supported by current and relevant evidence, blocks exploitation or materially interrupts impact | Monitor control; plan remediation | Next maintenance window |
| **Confirmed Exposure** | A reachable, exploitable path exists | Treat per SLA | Severity-tiered SLA (see §7.2) |
| **Material Risk** | Confirmed exposure on a crown jewel, regulated system, or asset with Restricted data; OR active exploitation observed | Emergency treatment | PPR tier |

### 7.2 Treatment SLAs (Canonical)

SLAs are measured from classification to verified closure. The SLA tier is driven by classification and exposure context, not by raw CVSS.

| Classification | Context | SLA |
|---------------|---------|-----|
| **Material Risk — PPR** | KEV-listed, active exploitation, or crown-jewel exposure | **48 hours** (Internet-facing) / **72 hours** (internal) |
| **Confirmed Exposure — Critical** | Internet-reachable, no compensating control | **3 days** |
| **Confirmed Exposure — High** | Internal reachable, or Internet-reachable with limited impact | **15 days** |
| **Confirmed Exposure — Medium** | Limited reachability or impact | **30 days** |
| **Confirmed Flaw, Not Exposed** | Compensated or segmented | **90 days** (align with maintenance) |
| **Hygiene Debt** | No confirmed exposure path | Per patch hygiene cadence (§10) |

### 7.3 Environment Overlays

| Environment | Overlay |
|-------------|---------|
| **OT — BES Cyber Systems** | CIP-007 R2 governs (35-day evaluation cadence). Operational windowing flexibility; deviations managed per [CERG-STD-OT-001](../standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md). |
| **OT — non-BES** | Default SLAs with ≤25% windowing flexibility. Extensions require Risk acceptance (§11). |
| **CUI Environment** | SLA breaches require POA&M entry per [CERG-STD-CUI-001](../standards/CERG-STD-CUI-001_CUI_Handling_Standard.md). |
| **SOX-Relevant Systems** | Remediation evidence captured for ITGC. |
| **Tier 1 SaaS Posture Drift** | Provider-responsible: finding stays open against provider; escalation via vendor incident channel. |

### 7.4 OT/BES Patch Deferral Routing

OT patch deferral is a routing decision, not a blanket waiver from exposure treatment. Use the table below when a vendor-tested patch, operational maintenance window, safety constraint, or reliability concern prevents treatment within the governing SLA.

| Scenario | Required route | Required records / evidence | Approval and review |
|---|---|---|---|
| **Non-BES OT, operational window needed** | Schedule treatment in the next approved OT maintenance window; preserve compensating controls until completion. | Finding Record or Exposure Backlog Item; maintenance-window date; compensating-control validation; owner attestation. | Risk Pillar Leader may approve windowing within the ≤25% flexibility. Longer deferral requires Risk Acceptance Record under RMF-001 §9.7. |
| **BES Cyber System, CIP compliance unaffected** | Confirm that the deferral does not create or extend a CIP compliance gap; track treatment and evidence in the NERC-CIP evidence library. | Finding Record; BES asset identifier; CIP applicability note; compensating-control evidence; Evidence Index Entry. | CISO approval with Governance/NERC-CIP Compliance Manager concurrence; review at least every 30 days until closure. |
| **BES Cyber System, CIP compliance impacted** | Initiate CIP deviation / mitigation plan in addition to the exposure record. Do not treat the risk acceptance path as a substitute for CIP deviation. | Finding Record; NERC-CIP deviation or mitigation plan; Risk Register Entry; compensating-control validation; regulatory evidence package. | CISO + NERC-CIP Compliance Manager; milestones follow the mitigation plan and any applicable regulatory deadline. |
| **Emergency operational exception** | Operations may delay or alter treatment only to prevent safety, reliability, or grid disturbance. Document immediately and formalize within 24 hours. | Emergency decision log; Finding Record; operational impact rationale; post-hoc Security Exception Record or Risk Acceptance Record if residual risk continues. | CISO post-hoc approval within 24 hours; maximum 30-day review window unless converted to the BES/CIP route above. |

For every OT deferral, document why a non-patch treatment (path block, segmentation, configuration change, monitoring, vendor isolation, or service removal) cannot close the exposure sooner. Deferral does not close the finding; closure requires verified treatment or a valid, reviewed risk/exception posture.

---

## 8. Step 5 — Select Treatment

Treatment is chosen based on the most effective path to close confirmed exposure, not the most familiar one. Patching is one tool among many.

### 8.1 Treatment Options

| Treatment | When to Use | Example |
|-----------|------------|---------|
| **Remove service** | The vulnerable component is not needed | Uninstall unused Apache instance |
| **Block path** | The exposure is reachable but the service must stay | Firewall rule, ACL, WAF |
| **Change configuration** | A config change eliminates the exposure without a patch | Disable TLS 1.0, restrict cipher suite |
| **Patch / update** | A vendor fix is available and tested | Apply OS security update |
| **Add compensating control** | Patching is not feasible (legacy, OT, vendor delay) | EDR rule, MFA requirement, network isolation |
| **Redesign** | The architecture itself creates the exposure | Move admin interface to jump-host-only network |
| **Accept residual risk** | Treatment is infeasible or disproportionate | Documented risk acceptance per §11 |
| **Transfer** | The risk belongs to a vendor/partner | Contractual obligation, shared responsibility matrix |

### 8.2 Patching Is Not the Center

> Patching is important. It is not the same as risk reduction.
>
> A program that patches everything on schedule but leaves an Internet-exposed, unauthenticated API on a crown jewel is failing. A program that cannot patch a legacy OT controller but has verified that the controller is air-gapped, monitored, and on a replacement roadmap is succeeding.
>
> Measure outcomes, not activity.

---

## 9. Step 6 — Verify Closure

A treatment is not complete until independently verified.

### 9.1 Verification Methods

| Method | When Required |
|--------|--------------|
| Authenticated re-scan | All Confirmed Exposures (Critical, High) |
| Configuration evidence | Configuration changes, blocking rules |
| Reachability test | When treatment was "block path" |
| Compensating control validation | When treatment involved compensating controls |
| Owner attestation | Hygiene debt resolution |

### 9.2 Verification Timing

Verification must occur within 5 business days of treatment completion. Unverified treatments are treated as open exposures. A treatment that passes verification but the exposure re-appears within 90 days triggers a root-cause review.

---

## 10. Patch Hygiene

Patch hygiene is a distinct discipline from exposure management. It is necessary. It is not sufficient.

### 10.1 What Patch Hygiene Is

Patch hygiene keeps platforms supportable, reduces configuration drift, prevents known-weakness accumulation, and satisfies compliance requirements that mandate currency. It is a maintenance function — like oil changes for a vehicle. It prevents future problems; it does not fix today's exposures.

### 10.2 Patch Hygiene Cadence

| Platform Class | Cadence | Owner |
|---------------|---------|-------|
| Windows Server | Monthly (Patch Tuesday + 14 days) | IT Operations |
| Linux Server | Monthly | IT Operations |
| Network devices | Quarterly (or vendor advisory-driven) | Network Operations |
| Endpoints | Monthly (auto-update) | Endpoint Engineering |
| OT — BES Cyber Systems | Per CIP-007 R2 (35-day evaluation) | OT Operations |
| Cloud PaaS / managed services | Provider-managed; verify currency monthly | Cloud Engineering |

### 10.3 Patch Hygiene Metrics

| Metric | Definition |
|--------|-----------|
| Patch currency rate | % of assets within their platform-class cadence window |
| Platform end-of-support count | Assets running software past vendor end-of-support |
| Hygiene debt by platform | Count of unresolved observations classified as Hygiene Debt, by platform |

These are reported separately from exposure management metrics. Conflating patch hygiene with exposure reduction produces vanity metrics.

---

## 11. Risk Acceptance and Exceptions

### 11.1 Policy Exception vs. Risk Acceptance

These are different things and follow different paths.

| Scenario | Type | Path |
|----------|------|------|
| "We cannot meet password length because legacy system maxes at 12 characters" | Policy / control exception | Governance-owned exception workflow |
| "The legacy system is Internet-reachable, privileged, and has weak auth" | Risk | Risk-owned residual risk analysis |
| "We will isolate it, broker access, monitor sessions, and retire by Q3" | Treatment | Engineering + Risk |
| "The VP of Operations accepts the residual risk until Q3" | Business risk acceptance | Business owner accepts |

Governance owns the exception workflow. Risk owns residual risk analysis. Business owns the consequence. Security does not own the business consequence.

### 11.2 Risk Acceptance Process

When treatment cannot meet SLA, the owning team requests risk acceptance through [CERG-PRC-RM-001](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md). Documentation must include:

- Observation identifier, asset, environment, classification
- Reason treatment is not feasible within SLA
- Compensating controls in place and their verified status
- Risk owner (business) and approver
- Expiration date and re-evaluation triggers

**PPR-tier exposures are not eligible for ordinary risk acceptance.** The only exception is OT operational windowing under §7.4. For BES Cyber Systems, the CIP deviation / mitigation route is mandatory when compliance is impacted and cannot be replaced by a generic acceptance memo.

---

## 12. Adversarial Validation

Scanning identifies what is misconfigured or unpatched. Adversarial validation tests whether controls actually function under attack. Findings from adversarial engagements enter the observation pipeline at Step 1 and follow the full state model.

| Activity | Cadence | Scope |
|----------|---------|-------|
| Internal penetration test | Annual minimum | Representative production |
| External penetration test | Annual minimum | Internet-facing attack surface |
| Cloud red-team / attack simulation | Annual minimum | Production cloud accounts |
| Application penetration test | Pre-release + annual | Tier 1 applications |
| OT adversarial assessment | Per STD-OT-001 | OT environments |
| Purple-team detection validation | Quarterly minimum | Detection rule validation |

---

## 13. Reporting and Metrics

### 13.1 Exposure Management Metrics (Primary)

These metrics measure exposure reduction, not scanner activity.

| ID | Metric | Definition | G / A / R |
|----|--------|-----------|-----------|
| EM-001 | Confirmed Reachable Critical Exposure | Count of exposures in state "Exposure Confirmed" with Critical/PPR classification AND Internet-facing reachability | 0 / 1–3 / > 3 |
| EM-002 | Scanner Observations Not Yet Triaged | Count of observations in "Observed" state past validation SLA | ≤ 5% / 6–15% / > 15% |
| EM-003 | Observations Downgraded After Context | % of Critical/High CVSS observations reclassified to Hygiene Debt or lower after Steps 2-3 | Informational; no control target |
| EM-004 | KEV with Reachable Path | Count of KEV-matched observations in "Exposure Confirmed" or "Material Risk" state | 0 / 1–5 / > 5 |
| EM-005 | KEV Blocked by Verified Control | Count of KEV-matched observations classified as "Confirmed Flaw, Not Exposed" due to verified compensating controls | Watchlist; no control target |
| EM-006 | Exposures on Crown Jewels | Count of confirmed exposures on crown-jewel-classified assets | 0 / 1–2 / > 2 |
| EM-007 | SLA Misses with Compensating Controls | Exposures past SLA where a verified compensating control exists | ≤ 5 / 6–15 / > 15 |
| EM-008 | SLA Misses with No Controls | Exposures past SLA with no compensating control | 0 / 1–3 / > 3 |
| EM-009 | Median Time: Observation to Exposure Decision | Median days from observation intake to classification | ≤ 3d / 4–7d / > 7d |
| EM-010 | Median Time: Exposure Decision to Treatment Decision | Median days from classification to treatment selection | ≤ 2d / 3–5d / > 5d |

### 13.2 Patch Hygiene Metrics (Secondary)

| ID | Metric | Definition | G / A / R |
|----|--------|-----------|-----------|
| PH-001 | Patch Currency Rate | % of assets within platform-class patch cadence window | ≥ 95% / 85–95% / < 85% |
| PH-002 | Hygiene Debt by Platform | Count of Hygiene Debt observations, grouped by platform class | Trend-only; no control target |
| PH-003 | End-of-Support Count | Assets on software past vendor end-of-support date | 0 / 1–10 / > 10 |

### 13.3 Reporting Cadence

| Report | Audience | Cadence |
|--------|----------|---------|
| Exposure posture — Confirmed Exposure + Material Risk, SLA status, KEV exposure | CISO + executive leadership | Monthly |
| Observation triage backlog — observations awaiting validation, by age | Exposure Management Lead | Weekly |
| Asset-owner treatment queue | Asset owners / Engineering managers | Weekly |
| OT exposure posture | OT operations + CISO | Monthly |
| CUI environment posture (POA&M support) | Governance | Monthly |
| Patch hygiene dashboard | IT/OT Operations | Monthly |
| Adversarial validation findings | CISO + board (annual summary) | Per engagement; annual aggregate |

### 13.4 Escalation Triggers

Immediate escalation to CISO:

- Active exploitation observed against an in-scope asset (auto-promotes to Material Risk — PPR)
- Any PPR-tier exposure open beyond its SLA
- A confirmed exposure on a BES Cyber System that risks NERC-CIP non-compliance
- A confirmed exposure in a CUI environment that materially affects SSP posture
- Adversarial validation finding demonstrating a successful path to Restricted-tier data or operational disruption

---

## 14. Regulatory and Framework Alignment Summary

| Regulation / Framework | Where in This Procedure |
|------------------------|------------------------|
| NIST CSF 2.0 IDENTIFY, PROTECT, RESPOND | Steps 1–9; observation collection through verification |
| NIST 800-53r5 RA-5, SI-2, SI-3, SI-4, SI-5 | Steps 4–9; discovery, prioritization, treatment, verification |
| NIST 800-171r3 3.11, 3.14 | Steps 4–11; risk assessment, system integrity |
| NIST 800-40r4 (Patch Management) | Section 10; patch hygiene |
| NIST RMF | Steps 7–11; risk-based classification, treatment, acceptance |
| NERC-CIP CIP-007 R2 | Steps 7.3, 10; OT overlay, patch evaluation |
| CMMC RA.L2 | Steps 7, 11; risk assessment, acceptance |
| SOX ITGC | Steps 8–9, 11; treatment, verification, acceptance |

---

## 15. Procedure Control

| | |
|---|---|
| **Document ID** | CERG-PRC-VM-001 |
| **Version** | 2.02 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Exposure Management Lead |
| **Approved By** | CISO |
| **Parent Policy** | [CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Semi-Annual |
| **Next Scheduled Review** | 2026-12-17 |
| **Frameworks** | NIST CSF 2.0 · NIST 800-53r5 |
| **Regulations** | NERC-CIP · CMMC L2 · SOX ITGC |
| **Environments** | All in-scope environments |


### Revision History

| Version | Date | Author | Change Summary |
|---------|------|--------|---------------|
| 2.02 | 2026-06-18 | Governance Pillar Leader | Added OT/BES patch deferral routing for non-BES OT, BES compliance-unaffected deferrals, BES compliance-impacting deviations, and emergency operational exceptions. |
| 2.01 | 2026-06-14 | Governance Pillar Leader | Aligned CISO risk-acceptance role language to the canonical RMF authority table. |
| 2.0 | 2026-06 | CERG Risk | Major revision: shift from exposure management to exposure management. Introduced 6-step state model (Observed→Verified), classification taxonomy (Non-issue/Hygiene Debt/Confirmed Flaw/Confirmed Exposure/Material Risk), separation of patch hygiene from exposure management, new exposure-focused metrics. |
| 1.0 | 2026-05 | CERG Risk | Initial release |

### Review Triggers

Annual review or upon: material tooling change, regulatory SLA change, internal audit finding, CISO direction, or significant change to asset tiering.

### Related Documents

| Document | ID | Relationship |
|----------|-----|-------------|
| Cybersecurity Policy | CERG-POL-001 | Parent policy — Principle 5 |
| Grid and Control System Standard | CERG-STD-OT-001 | OT overlays |
| IT/Cloud/SaaS Security Standard | CERG-STD-IT-001 | IT/Cloud/SaaS scope |
| CUI Handling Standard | CERG-STD-CUI-001 | CUI environment overlays |
| Access Management Standard | CERG-STD-AC-001 | Identity-related exposures |
| Secure Configuration Baseline | CERG-STD-CFG-001 | DISH baseline drift |
| Risk Register and Exception Process | CERG-PRC-RM-001 | Risk acceptance workflow |
| Third-Party and Supply Chain Risk | CERG-PRC-TPRM-001 | Vendor/supply-chain observations |
| Threat Intelligence | CERG-PRC-TI-001 | Threat intel feed into observations |
| CERG Operating Model | CERG-GOV-OM-001 | Pillar structure |
| Metrics Dashboard | CERG-GOV-MTR-001 | EM and PH metrics |

---
>
> _A scanner report is inventory data. Confirmed exposure is what matters._

---

_CERG-PRC-VM-001 · Version 2.02 · PUBLIC_
