## RISK REGISTER AND EXCEPTION PROCESS
### Identification · Treatment · Acceptance · Review

---

| | |
|---|---|
| **Document ID** | CERG-PRC-RM-001 |
| **Version** | 1.04 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Risk Register Owner |
| **Parent Policy** | [CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Standards** | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) · [CERG-STD-OT-001](../standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) · [CERG-STD-CUI-001](../standards/CERG-STD-CUI-001_CUI_Handling_Standard.md) · [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) |
| **Review Cycle** | Annual / Upon Significant Change / Major Tooling Change |
| **Frameworks** | [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (GOVERN) · [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST 800-171r3](https://csrc.nist.gov/pubs/sp/800/171/r2/final) · [NIST 800-30r1](https://csrc.nist.gov/pubs/sp/800/30/r1/final) · [NIST 800-39](https://csrc.nist.gov/pubs/sp/800/39/final) · NIST RMF · ISO 31000 |
| **Regulations** | NERC-CIP · [CMMC L2](https://dodcio.defense.gov/CMMC/) · [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC · |
| **Environments** | All in-scope assets - owned, hybrid, cloud, SaaS, OT |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Roles and Responsibilities](#2-roles-and-responsibilities)
3. [Risk Identification](#3-risk-identification)
4. [Risk Assessment and Scoring](#4-risk-assessment-and-scoring)
5. [Risk Treatment](#5-risk-treatment)
6. [The Risk Register](#6-the-risk-register)
7. [Exception Process](#7-exception-process)
8. [Approval Authority](#8-approval-authority)
9. [Review, Escalation, and Reporting](#9-review-escalation-and-reporting)
10. [Integration With Other Programs](#10-integration-with-other-programs)
11. [Regulatory and Framework Alignment Summary](#11-regulatory-and-framework-alignment-summary)
12. [Procedure Control](#12-procedure-control)

---

## 1. Purpose and Scope

This procedure operationalizes the risk management principle established in **[CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md) Principle 9**. It defines how the organization identifies, documents, scores, treats, reviews, and reports cybersecurity risks, and how exceptions to established controls are requested, approved, tracked, and reviewed.

The risk register is the single, authoritative record of organizational cybersecurity risk. The exception process is the single, authoritative record of intentional deviations from established controls. The two are coupled: every approved exception is itself a risk-register entry.

### 1.1 Scope

This procedure applies to:

- All cybersecurity risks affecting in-scope assets, data, or operations
- All deviations from controls established in [CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md) and its subordinate standards and procedures
- All risk-related decisions requiring documentation: acceptance, transfer, avoidance, and reduction
- All organizational personnel, every CERG team member, every asset owner, every business sponsor of a system or process that holds cybersecurity risk

### 1.2 The Operating Premise

> **Undocumented Risk Is Accepted Risk Without an Owner**
>
> Every organization has more risk than it has time to remediate. The question is not whether risk exists, it is whether the organization has a documented, owned, and reviewed posture toward each one. An undocumented risk that materializes into an incident leaves no audit trail of what was known, who knew it, or why nothing was done. CERG treats the risk register as evidence of program maturity, not as a chore.

---

### 1.3 Risk Appetite and Tolerance

The organization's risk appetite defines the amount and type of risk the organization is willing to accept in pursuit of its objectives. Without a stated appetite, "accept" decisions lack an objective anchor, and scoring discussions drift toward personal calibration.

#### Appetite Statement

The organization accepts residual risk only where (a) the cost or operational impact of further treatment demonstrably exceeds the residual risk, (b) compensating controls are in place and operating effectively, and (c) the risk does not threaten regulatory standing, customer trust, or safety. Risk that cannot satisfy all three conditions must be treated.

#### Quantitative Tolerance Thresholds

The durations below are scope-specific treatment horizons. They do not extend risk-acceptance authority or duration beyond the canonical limits in [`CERG-GOV-RMF-001`](../governance/CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.7; when more than one rule applies, the shortest applicable duration wins.

| **Tier / Scope** | **Maximum Acceptable Residual Risk Score** | **Maximum Acceptable Treatment Horizon** | **Notes** |
|---|---|---|---|
| BES Cyber Systems (NERC-CIP) | 6 (Medium-Low) | 90 days | Aligned to CIP mitigation plan timelines |
| CUI Environments (CMMC) | 6 (Medium-Low) | 90 days | Aligned to POA&M timelines; Critical not acceptable |
| SOX-Relevant Systems | 8 (Medium) | 180 days | ITGC compensating controls required |
| Production Tier 1 (Customer-Facing) | 8 (Medium) | 180 days | Critical not acceptable without CISO + Executive Sponsor |
| Production Tier 2 (Internal Business) | 10 (Medium-High) | 365 days | |
| Production Tier 3+ / Non-Production | 12 (High-Low) | 365 days | |
| SaaS / Third-Party | 10 (Medium-High) | Contract cycle | Driven by vendor tier per [CERG-PRC-TPRM-001](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) |

#### Tolerance by Business Unit

Tolerance thresholds may vary by business unit where the business unit operates under materially different regulatory, contractual, or operational risk profiles. Business unit tolerance adjustments are proposed by the Risk Owner in that unit, reviewed by the Governance Pillar Leader, and approved by the CISO. Adjustments are recorded in the risk register as a standing annotation on the business unit's scope.

#### Board and Leadership Engagement

The board or an authorized board committee reviews and affirms the organization's risk appetite annually. Material changes to risk appetite - including adjustments to quantitative thresholds or tolerance by business unit - are submitted to the CISO for recommendation and board approval. The CISO owns the annual appetite affirmation cycle and reports the organization's actual risk posture against appetite at each quarterly CISO-level review.

---

## 2. Roles and Responsibilities

| **Role** | **Risk Management Responsibility** |
|---|---|
| **Risk Register Owner** | Owns this procedure and the risk register tool. Maintains the data model, taxonomy, dashboards, and reporting. Coordinates the risk review cadence. Curates the register for quality and completeness. |
| **Risk Pillar Leader** | Identifies risks through exposure management, threat intelligence, vendor assessment, adversarial testing, and continuous monitoring. Records risks in the register and recommends scoring and treatment. |
| **Engineering Pillar Leader** | Identifies risks through architecture review and pre-production assessment. Recommends compensating controls. Implements risk-reduction treatments on assets it supports. |
| **Business / Asset Owners (Risk Owners)** | Accountable for the risks associated with the systems and processes they own. Authorize treatment decisions for their scope. Sign on risk acceptances. |
| **Approvers (Engineering Pillar Leader → CISO → Executive Sponsor)** | Apply the approval matrix in Section 8. Approvers do not own risks; they authorize the treatment decision against organizational policy. |
| **CISO** | Approves High and Critical risk acceptances and material exceptions. Owns escalation to executive leadership and the board. Owns the overall organizational risk posture. |
| **Internal Audit and Compliance Partners** | Consume the register as evidence of risk management activity. Verify integrity of the process through periodic audit. |

---

## 3. Risk Identification

A risk is a potential event that could adversely affect organizational assets, operations, or obligations. Risks may be technical (a vulnerability, a misconfiguration, a control gap), programmatic (a process gap, a staffing gap), or external (a regulatory change, a vendor failure, a threat actor's interest).

### 3.1 Sources of Risk

Risks are identified continuously from the following sources, each of which feeds the register:

| **Source** | **Examples** |
|---|---|
| Exposure management | Out-of-SLA findings, KEV exposures, structural patching limitations. |
| Engineering review | Architectural gaps identified in pre-production review, IT/OT convergence findings, technical debt with security implications. |
| Adversarial validation | Pen-test findings, red-team paths to crown-jewel assets, control-bypass discoveries. |
| Third-party / vendor risk | SOC 2 / ISO 27001 / FedRAMP exceptions, vendor incidents, supply-chain advisories. |
| Threat intelligence | Threats specifically targeting the organization's industry, technology, or geography. |
| Compliance monitoring | Findings from internal compliance reviews, regulator examination, external audit. |
| Incident review | Root causes from post-incident reviews. |
| Exception requests | Approved exceptions, which become risk-register entries. |
| Strategic / programmatic | Staffing shortfalls, tooling gaps, sunset of unsupported platforms. |
| Self-reporting | Risk submissions by any personnel through the documented intake. |

### 3.2 Intake

Any personnel may submit a candidate risk through the centralized intake. Submissions include the proposed risk statement, affected assets, observed or estimated impact, and supporting context. Governance triages submissions within 5 business days into one of: accept as new register entry, merge with existing entry, escalate to active investigation, or return with explanation.

---

## 4. Risk Assessment and Scoring

### 4.1 Risk Statement

Each risk is expressed in a consistent, declarative form:

> "**[Event / condition]** affecting **[asset class / scope]** could result in **[impact]** within **[likelihood window]** unless **[control / treatment]**."

Risk statements are specific enough to support scoring. "We need better cloud security" is not a risk statement; "Unauthorized changes to production cloud IAM roles could result in privilege escalation enabling exfiltration of customer data within the current control period unless drift detection and JIT elevation are enforced" is.

### 4.2 Scoring Framework

Risks are scored using the canonical 5×5 **Likelihood × Impact** model in [`CERG-GOV-RMF-001`](../governance/CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.5. This procedure operationalizes that model; it does not define a separate scoring scale. If this procedure and RMF-001 differ, RMF-001 governs.

The matrix produces a residual risk rating after considering controls in place. Inherent risk (controls hypothetically absent) is recorded but not the primary driver of treatment decisions.

#### Likelihood Summary

| **Score** | **RMF Label** | **Operational Meaning** |
|---|---|---|
| 1 | Very Low | No specific indicator; outside common attack or failure patterns for the organization. |
| 2 | Low | Occurs in the industry occasionally; no current indicator at the organization. |
| 3 | Medium | Realistic given the threat landscape; mitigating controls reduce likelihood. |
| 4 | High | Frequent in the industry; conditions present at the organization with limited mitigation. |
| 5 | Very High | Active or imminent; observed indicators, active exploitation, or minimal current mitigation. |

#### Impact Summary

| **Score** | **RMF Label** | **Operational Meaning** |
|---|---|---|
| 1 | Negligible | No regulatory, customer, financial, or operational impact beyond routine response. |
| 2 | Minor | Limited operational disruption or remediation cost; no regulatory or customer-visible impact. |
| 3 | Medium | Material remediation effort, leadership-reportable loss, or limited reputation impact. |
| 4 | Major | Significant regulatory exposure, material customer impact, Tier 1 disruption, or significant reputation damage. |
| 5 | Catastrophic | Material business / financial impact, broad customer harm, regulatory enforcement, safety or reliability consequence, or SEC-disclosable impact. |

#### Rating Bands

| **Score Product** | **Rating** | **Default Treatment Expectation** |
|---|---|---|
| 1 | **Informational** | Track for trend analysis; no formal acceptance required unless another obligation requires it. |
| 2–5 | **Low** | Track; treat as resources allow; acceptance follows RMF-001 §9.7. |
| 6–11 | **Medium** | Treat within a defined plan; review at standing cadence; acceptance follows RMF-001 §9.7. |
| 12–19 | **High** | Treat with priority; acceptance follows RMF-001 §9.7 and requires CISO + Business Owner approval. |
| 20–25 | **Critical** | Immediate treatment required; acceptance follows RMF-001 §9.7 and requires CISO + Executive Sponsor approval plus board notification. |

### 4.3 Quantitative Calibration Guide

Quantitative calibration is maintained in [`CERG-GOV-RMF-001`](../governance/CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.5 and §12. Local revenue, insurance, downtime, regulatory, and safety thresholds may be calibrated there, but calibrated thresholds do not override the acceptance authority in RMF-001 §9.7.

#### Using Calibration in Scoring Discussions

The calibration table is a coordination tool, not a precise calculator. When two analysts reach different scores:
1. Each states their rationale in terms of likelihood (what is the annualized frequency?) and impact (what is the estimated financial, operational, regulatory, safety, or customer consequence?).
2. The Governance Lead facilitates the discussion toward the better-supported score using RMF-001 §9.5.
3. If disagreement persists, the higher score is used and the rationale for both scores is recorded.

The goal is not perfect precision - it is consistent conversation that produces comparable risk rankings across the register.

### 4.4 Scoring Discipline

> **The 5×5 Trap**
>
> The 5×5 matrix is a coordination tool, not an oracle. Two analysts will reach different scores for the same risk; the value of the matrix is consistency of conversation, not precision of measurement. The Governance Lead enforces consistency within the register and reconciles outliers, but does not fight every score. The goal is comparable risks ranked comparably, not perfect calibration.

Re-score upon: material change in observed threat activity, completion of treatment work, new compensating controls, new exploitation indicators, or regulator / customer engagement that materially changes impact.

---

## 5. Risk Treatment

Each risk has one of four treatment decisions. Treatment is decided by the risk owner with input from CERG and approved per Section 8.

| **Treatment** | **Description** | **When Appropriate** |
|---|---|---|
| **Reduce (Mitigate)** | Implement or strengthen controls to reduce likelihood, impact, or both. The default treatment for most risks. | Almost always preferred where feasible and timely. |
| **Transfer** | Shift the financial or operational consequence to a third party (insurance, contractual indemnity, managed service). | When transfer is economically and operationally rational; not a substitute for treatment of the underlying technical risk. |
| **Avoid** | Cease or decline the activity producing the risk. | When the activity is not essential or when residual risk is unacceptable under any treatment. |
| **Accept** | Acknowledge the residual risk under documented conditions, owner accountability, expiration/review cadence, and monitoring. | When the cost or operational impact of treatment exceeds the residual risk, the residual is within the organization's tolerance, and the Business Owner or Executive Sponsor accepts the consequence under RMF-001 §9.7. |

### 5.1 Treatment Plan Elements

Every treatment decision records:

- The selected treatment.
- The plan, for Reduce: target end-state controls and the steps to get there; for Transfer: the instrument and counter-party; for Avoid: the cessation steps; for Accept: the rationale and conditions of acceptance.
- Owner, accountable for the plan's execution.
- Target dates, milestone and final.
- Compensating controls, in place now and required for the duration of the plan.
- Trigger conditions for re-evaluation, what would invalidate the current decision.

### 5.2 Funding or Capacity Decision Brief

When a treatment cannot proceed because funding, staffing, change-window capacity, vendor spend, or business prioritization is unavailable, the Risk Register Owner attaches a Control Funding Decision Brief using [`CERG-GOV-MTR-001`](../governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) §6.1. The brief records the decision needed, control/risk link, business capability affected, options, deadline, and consequence of deferral.

A funding or capacity deferral does not by itself accept residual risk. If residual risk remains after the decision, the Business Owner or required RMF-001 authority must complete [`CERG-TMPL-RM-004`](../templates/CERG-TMPL-RM-004_Risk_Acceptance_Request_Form.md), and the risk register records the acceptance, expiration, treatment owner, and next review date.

### 5.3 Risk Acceptance Has Two Forms

| **Form** | **Description** |
|---|---|
| **Standing acceptance** | The residual risk is within tolerance for an ongoing activity. Standing acceptance still requires a named Business Owner, periodic re-review, and a register entry; it is not irrevocable or ownerless. |
| **Time-bound acceptance** | The risk is accepted for a defined window during which compensating controls operate; treatment is expected to occur within the window. This is the predominant form of acceptance for control deficiencies awaiting remediation. Duration cannot exceed RMF-001 §9.7 or any shorter applicable regulatory/procedure limit. |

---

## 6. The Risk Register

### 6.1 Required Fields

| **Field** | **Description** |
|---|---|
| Risk ID | Unique identifier assigned at intake. |
| Risk Statement | The standardized risk statement (Section 4.1). |
| Risk Owner | Business or asset owner accountable for the risk. |
| Risk Category | Taxonomy classification (e.g., Identity & Access, OT / NERC-CIP, Cloud / SaaS, Third-Party / Supply Chain, CUI / Federal, Application Security, Data Protection, Insider, Resilience). |
| Affected Assets / Scope | Systems, data classes, environments. |
| Source | Where the risk was identified (Section 3.1). |
| Likelihood / Impact / Rating | Current scores and band. |
| Inherent Rating | Hypothetical rating absent controls (recorded once at intake; not re-scored each cycle). |
| Controls in Place | Existing controls reducing the risk. |
| Treatment Decision | Reduce / Transfer / Avoid / Accept. |
| Treatment Plan | Plan summary. |
| Target Dates | Milestone and final. |
| Approver | Approver name and approval date per Section 8. |
| Compliance Linkage | Associated regulation, framework, or contract (e.g., 800-171 control reference, CIP standard, [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC). |
| Linked Exceptions | Exception IDs created under this risk, if any. |
| Linked Incidents | Incident IDs that derived from or contributed to the risk, if any. |
| Status | Open / In Treatment / Accepted / Closed. |
| Review Date | Next scheduled review. |
| Audit Trail | History of changes - every score change, treatment change, approver change, status change. |

### 6.2 Quality and Integrity

The Governance Lead curates the register for quality. Specifically:

- Risks shall not be duplicated; new submissions are merged with existing entries when appropriate.
- Risk statements that are vague or unscope-able are returned for clarification.
- Risks that are no longer relevant (e.g., the underlying system has been decommissioned) are closed with rationale.
- Closed risks remain queryable; the register is append-only at the audit-trail level.

### 6.3 Risk Taxonomy

The following taxonomy is the controlled vocabulary for risk categorization. Every risk entry must be assigned exactly one category from this taxonomy. Consistent categorization enables trend analysis, ownership clarity, and regulatory mapping.

| **Category** | **Definition** | **Examples** |
|---|---|---|
| **Identity & Access** | Risks related to identity lifecycle, authentication, authorization, privilege management, and access control failures. | Standing privileged access, MFA gaps, orphaned accounts, over-privileged service principals, credential theft. |
| **OT / NERC-CIP** | Risks affecting Operational Technology, BES Cyber Systems, or NERC-CIP compliance posture. | Unpatched OT assets, IT/OT boundary weaknesses, CIP-007 deviation, BCSI exposure. |
| **Cloud / SaaS** | Risks arising from cloud platform misconfiguration, SaaS security posture, or cloud-native service exposure. | Open S3 bucket, excessive IAM roles, SaaS OAuth grant abuse, tenant isolation failure. |
| **CUI / Data Protection** | Risks to the confidentiality, integrity, or availability of Controlled Unclassified Information or other regulated data. | CUI stored outside authorized boundary, FIPS non-compliance, data spillage, missing encryption at rest. |
| **Third-Party / Vendor** | Risks introduced through vendor relationships, supply chain dependencies, or subcontractor access. | Vendor SOC 2 exception, subprocessor concentration, vendor breach with downstream impact. |
| **Endpoint** | Risks related to endpoint security, including workstations, servers, and mobile devices. | Missing EDR coverage, unpatched endpoint, local admin abuse, removable media exposure. |
| **Network** | Risks to network segmentation, perimeter controls, traffic inspection, or remote access. | Flat network, exposed management interface, missing segmentation between regulatory zones. |
| **Application Security** | Risks in custom or third-party application code, APIs, or application architecture. | SQL injection, broken authentication in custom app, API key exposure, SSRF vulnerability. |
| **Cryptography** | Risks related to cryptographic key management, algorithm selection, certificate lifecycle, or secrets handling. | Expired certificate, weak cipher suite, hard-coded secret, missing HSM for CA key. |
| **Governance / Compliance** | Risks from gaps in policy, process, regulatory alignment, or program maturity. | Missing policy review cycle, undocumented exception process, audit finding without remediation plan. |
| **Resilience** | Risks to business continuity, disaster recovery, backup integrity, or service restoration capability. | Untested backups, single-region dependency, RTO/RPO gap for Tier 1 system. |
| **Insider** | Risks from intentional or unintentional actions by authorized personnel. | Data exfiltration by departing employee, accidental PII exposure, privilege misuse. |
| **Physical / Environmental** | Risks from physical access, environmental controls, or facility security. | Unsecured data center access, missing CCTV coverage, inadequate fire suppression. |

Access and Confidentiality

Risk register access is role-based. Business owners see their scope by default; CERG personnel see organization-wide. Specific risk entries may be marked Restricted (e.g., active high-sensitivity exposure, insider matters) with limited visibility. The CISO has full visibility at all times.

---

## 7. Exception Process

### 7.1 Exception vs. Risk Acceptance — Which Path to Use

Per [`CERG-GOV-RMF-001`](../governance/CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.7a, CERG distinguishes two distinct decision paths. Using the wrong path bypasses the required approval authority.

| **Path** | **Description** | **Form** | **Approval** | **Register** |
|---|---|---|---|---|
| **Security Exception** (Governance-tracked) | A specific control or standard cannot be met as written. The deviation is temporary, with compensating controls, expiration, and a remediation plan. | [`CERG-TMPL-RM-002`](../templates/CERG-TMPL-RM-002_Security_Exception_Request_Form.md) — Security Exception Request Form | Governance approves within authority per §8. Assessment by Risk and Engineering. | Exception register; linked to risk register entry |
| **Risk Acceptance** (Business Owner + RMF-001 §9.7) | The residual risk after controls is within appetite. No further treatment is planned beyond monitoring. The Business Owner explicitly accepts the business consequence. | [`CERG-TMPL-RM-004`](../templates/CERG-TMPL-RM-004_Risk_Acceptance_Request_Form.md) — Risk Acceptance Request Form | Per RMF-001 §9.7 authority table: Business Owner at all levels; CISO for High; CISO + Executive Sponsor for Critical. | Risk register (accepted status) |

**Routing rule:** If the trigger is a control or standard that cannot be met → Security Exception (TMPL-RM-002). If the trigger is residual risk the organization chooses to live with → Risk Acceptance (TMPL-RM-004). When in doubt, route as Security Exception; the Risk Register Owner may reclassify during triage.

### 7.2 What Requires an Exception

An exception is required whenever a system, person, or process intentionally deviates from a control established in [CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md) or its subordinate standards. Examples include:

- A system that cannot meet a hardening baseline due to a vendor or operational constraint
- A user role that requires standing privileged access despite the JIT requirement
- A SaaS application not behind SSO due to a technical limitation
- A vulnerability remediation that cannot meet the SLA
- A vendor account configuration not meeting the access management standard
- An OT system that cannot satisfy a CIP-007 requirement on schedule (in addition to the CIP deviation process)

### 7.3 Exception Workflow

| **Step** | **Action** | **Owner** |
|---|---|---|
| 1 | Requester submits exception with: control reference, business / operational justification, affected systems, proposed compensating controls, risk owner, and proposed duration. | Requester |
| 2 | Engineering reviews proposed compensating controls. | Engineering |
| 3 | Risk assesses likelihood and impact of the residual risk; provides a written risk finding. | Risk |
| 4 | Governance applies the approval matrix (Section 8); routes for approval. Business owner approval is required for any exception carrying residual risk above Low. | Governance |
| 5 | Approver decides: approve, approve with conditions, deny, or return for additional information. | Approver |
| 6 | Approved exception is entered into the exception register and linked to the risk register when residual exposure exists; compensating controls are tracked. | Governance |
| 7 | At expiration, the exception is re-evaluated. Renewal requires a new approval cycle. Renewals shall not be granted by default. | Governance |

### 7.4 Exception Discipline

> **Renewals Are Where Programs Decay**
>
> The most common failure mode of an exception program is the silent renewal. An exception is approved with a six-month duration; six months later it is renewed with a single email; six months after that the original reviewers have left the organization, the compensating controls have drifted, and the underlying control gap has become permanent. Governance enforces re-evaluation at every renewal: confirm the compensating controls are still in place, confirm the business justification is still valid, confirm the requested duration is still reasonable.


### 7.4.1 Exception Expiration Warning Chain

Every exception carries an expiration date. The following warning chain ensures no exception expires silently:

| Timing | Action | Actor |
|--------|--------|-------|
| **30 days before expiration** | Automated notification to Exception Owner and Risk Register Owner | Governance (Evidence Librarian or automated calendar) |
| **14 days before expiration** | Escalation notification to Pillar Leader; Exception Owner must confirm renewal request submitted or closure planned | Risk Register Owner |
| **7 days before expiration** | Final escalation to Governance Pillar Leader; Exception Owner must have a disposition (renew, close, or convert to finding) | Governance Pillar Leader |
| **Post-expiration (Day 0)** | Auto-create Finding Record (severity: High); flag affected control as "gap open"; the exception is no longer valid | Risk Register Owner |
| **Post-expiration (Day 5)** | If no disposition: escalate to CISO | Governance Pillar Leader |

An exception renewed more than twice without material progress toward remediation escalates one approval tier above the original approver. If the renewal also accepts residual risk, the approval path follows RMF-001 §9.7. The renewal justification must document what has changed since the previous approval and what prevents closure.

### 7.5 Regulatory Overlays

For exceptions affecting regulated assets:

- **NERC-CIP (BES Cyber Systems):** A CIP deviation and mitigation plan is initiated in addition to this exception. Governance coordinates per [CERG-STD-OT-001](../standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) §11.
- **[CMMC](https://dodcio.defense.gov/CMMC/) / 800-171 (CUI environments):** A POA&M entry is opened in addition to this exception, per [CERG-STD-CUI-001](../standards/CERG-STD-CUI-001_CUI_Handling_Standard.md) §11.
- **[SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)-relevant systems:** Internal Audit and CFO designee are notified for ITGC control gaps. Compensating ITGC controls are documented for audit.
- **Customer / contractual:** Where the affected control supports a customer contractual commitment, Account Management and Legal are notified for customer-notification decisions.

---

### 7.6 Exception Request Form and Risk Acceptance Form Templates

The following templates shall be used for all exception and acceptance requests. Use the correct form per the routing rule in §7.1. Completed forms are submitted through the centralized risk intake and referenced in the risk register.

**For Security Exceptions** (policy/standard deviation, Governance-tracked): use [`CERG-TMPL-RM-002`](../templates/CERG-TMPL-RM-002_Security_Exception_Request_Form.md) — Security Exception Request Form.

**For Risk Acceptances** (Business Owner accepts residual risk, per-RMF-001 authority): use [`CERG-TMPL-RM-004`](../templates/CERG-TMPL-RM-004_Risk_Acceptance_Request_Form.md) — Risk Acceptance Request Form.

The Security Exception Request Form (TMPL-RM-002) template is reproduced below for reference. The Risk Acceptance Request Form (TMPL-RM-004) is a separate artifact. [`CERG-TMPL-RM-003`](../templates/CERG-TMPL-RM-003_Risk_Acceptance_Memo_Template.md) may be attached as a lightweight memo, but it does not replace TMPL-RM-004 or RMF-001 §9.7 approval authority.

```
EXCEPTION REQUEST FORM - EXC-YYYY-NNNN

1. REQUESTOR
   Name:
   Role / Title:
   Department / Business Unit:
   Date of Request:

2. CONTROL(S) TO BE EXCEPTED
   Control ID (from CERG-GOV-CB-001 or applicable standard):
   Control Description:
   Standard / Policy Reference:

3. AFFECTED SCOPE
   System(s) / Asset(s):
   Environment (IT / Cloud / SaaS / OT):
   Data Classification(s):
   Regulatory Scope (NERC-CIP / CUI / SOX / Other):
   Number of Users Impacted:

4. BUSINESS JUSTIFICATION
   Why is the exception necessary? What business outcome depends on it?

   What alternatives were considered and why were they rejected?

5. RISK ASSESSMENT OF THE EXCEPTION
   Inherent Risk (Likelihood × Impact):
   Description of the risk created by this exception:
   Existing Compensating Controls:
   Residual Risk after Compensating Controls (Very Low / Low / Medium / High / Very High):

6. COMPENSATING CONTROLS (detailed)
   | Control | Description | Owner | Implementation Date | Validation Method |
   |---|---|---|---|---|
   | | | | | |

7. DURATION
   Proposed Start Date:
   Proposed End Date:
   Renewal Expected? (Yes / No):
   If yes, what conditions must be met for renewal?

8. APPROVAL
   | Role | Name | Decision | Date |
   |---|---|---|---|
   | Business Owner (Risk Owner) | | Approve / Deny / Conditional | |
   | Engineering Pillar Leader | | Approve / Deny / Conditional | |
   | Governance Pillar Leader | | Approve / Deny / Conditional | |
   | CISO (if High or Critical) | | Approve / Deny / Conditional | |
   | Executive Sponsor (if Critical) | | Approve / Deny / Conditional | |

9. RISK REGISTER LINKAGE
   Risk Register Entry ID:
   Exception ID cross-reference:

10. CLOSURE
    Actual End Date:
    Closure Rationale:
    Closure Approver:
```

---

## 8. Approval Authority

Risk treatment decisions require documented approval from the authority matching the risk's severity. The canonical approval authority table — including the Business role at every level — is maintained in [CERG-GOV-RMF-001](../governance/CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.7. The table below summarizes approval authority for convenience; the RMF table is authoritative. Security assesses, recommends, and validates. The business owner owns the consequence.

| **Risk Rating / Treatment** | **Security Role** | **Business Role** | **Approval** |
|---|---|---|---|
| Low risk – Accept or exception | Governance: confirms procedural exception; Risk: confirms low residual risk if needed | Business Owner: owns local consequence | Business Owner + Risk Register Owner |
| Medium risk – Reduce / Transfer / Avoid | Risk: performs risk assessment; Engineering: validates treatment plan | Business Owner: signs off on treatment | Risk or Engineering Pillar Leader |
| Medium risk – Accept | Risk: performs risk assessment; Governance: documents conditions | Business Owner: accepts residual risk | Business Owner + Pillar Leader or Governance Pillar Leader |
| High risk – Accept | Risk: signs finding; Governance: structures package | Business Owner: accepts business consequence | CISO + Business Owner |
| Critical risk – Accept | Risk: signs finding; Governance: structures package | Executive Sponsor: accepts business consequence | CISO + Executive Sponsor; Board notified |
| Any exception affecting BES Cyber Systems | As above per severity | As above | As above + NERC-CIP deviation process |
| Any exception affecting CUI environment posture | As above per severity | As above | As above + POA&M entry |
| Any exception affecting [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC | As above per severity | As above | As above + CFO designee notification or approval where required by SOX governance |
| Emergency exception (operational necessity) | Risk Pillar Leader or Engineering Pillar Leader may authorize immediately to protect operations | Business Owner notified within 24 hours and required for any continuing residual-risk acceptance | CISO must approve or deny post-hoc within 24 hours. If denied, the action must be reversed or mitigated, and the residual risk is logged to the risk register with the denial rationale. Continuing acceptance follows RMF-001 §9.7. |

Approvers may delegate within their authority but shall document the delegation. The CISO retains final authority for any risk-related decision. Acceptance of residual risk at any tier follows the canonical authority table in [CERG-GOV-RMF-001](../governance/CERG-GOV-RMF-001_Risk_Management_Framework.md) §9.7. The business owner accepts the business risk — security does not accept business risk. No acceptance expires automatically; every acceptance at every tier requires a fresh approval cycle at expiration.

---

## 9. Review, Escalation, and Reporting

### 9.1 Review Cadence

| **Item** | **Cadence** | **Owner** |
|---|---|---|
| Risk owner self-review of open risks in their scope | Quarterly | Risk Owner |
| Governance curation pass (quality, duplicates, status) | Monthly | Governance |
| CERG leadership review (Engineering + Risk + Governance) | Monthly | Governance |
| CISO-level risk review with material movement and overdue items | Quarterly | CISO + Governance |
| Executive / board risk briefing | Quarterly (or per board protocol) | CISO |
| Standing exception re-review | At exception expiration; no automatic renewal | Governance |

### 9.2 Escalation Triggers

The following trigger escalation to the CISO outside the standing cadence:

- A new High or Critical risk
- A material score increase on any existing risk
- A risk acceptance approaching expiration without a credible treatment plan
- A material deterioration in compensating control performance
- Realization of a risk into an incident
- A regulator or auditor inquiry referencing a register entry
- A renewal request for an exception in its second consecutive cycle

### 9.3 Reporting

Standing reports (consumed by Governance dashboards):

| **Report** | **Audience** | **Cadence** |
|---|---|---|
| Top risks (by rating and by trend) | CISO | Monthly |
| Open exceptions by environment | CERG Leadership | Monthly |
| Overdue treatments / expired exceptions | Governance | Weekly |
| Risks by category trend (Identity, Cloud, OT, CUI, Third-Party, etc.) | CISO + executive | Quarterly |
| Risks linked to active incidents | IC + CISO | Continuous during active response |
| Regulatory-specific posture (CIP, [CMMC](https://dodcio.defense.gov/CMMC/), [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204)) | Governance + Regulatory partners | Per regulator cycle |

### 9.4 Quality Indicators

The Governance Lead monitors the register itself for health:

- Median age of open High and Critical risks
- % of treatment plans on schedule
- Exception re-evaluation rate (declined vs. renewed)
- % of risks with a documented owner
- % of risks reviewed within their scheduled review date

---

## 10. Integration With Other Programs

The risk register is the integration point for several other programs. Risk-register entries derive from and feed back into:

| **Program** | **Integration** |
|---|---|
| Exposure Management ([CERG-PRC-VM-001](CERG-PRC-VM-001_Exposure_Management_Procedure.md)) | Out-of-SLA findings and aggregate exposure feed risk entries; large remediation campaigns are tracked as treatments. |
| Incident Response ([CERG-PLN-IR-001](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md)) | Post-incident corrective actions are recorded as risks or risk-acceptance closures. |
| Vendor / Third-Party Risk | Vendor assessment findings open risks; vendor reassessment cadence reviews them. |
| Compliance - NERC-CIP, [CMMC](https://dodcio.defense.gov/CMMC/), [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) | Open compliance gaps map to risk entries; POA&M and CIP deviations link to register entries. |
| Architecture / Engineering Review | Pre-production review findings open risks where acceptance is sought to deploy. |
| Awareness & Insider Programs | Concentrated insider-risk indicators are recorded (with appropriate restricted visibility). |
| Audit | Internal Audit and external audit observations open or update risk entries. |

The register is not a parallel system to these programs. It is the connective tissue that lets each program point to the same set of facts.

---

## 11. Regulatory and Framework Alignment Summary

| **Process Area** | **[NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final)** | **[NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)** | **[NIST 800-171](https://csrc.nist.gov/pubs/sp/800/171/r3/final)** | **NIST RMF** | **NERC-CIP** | **[CMMC L2](https://dodcio.defense.gov/CMMC/)** | **[SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC** |
|---|---|---|---|---|---|---|---|
| Risk Strategy & Governance | GV.RM | PM-9 | 3.11.1 | Steps 1–2 | CIP-003 | RM.L2-3.11.1 | ERM interface |
| Risk Assessment / Scoring | ID.RA | RA-3 | 3.11.1 | Step 3 | CIP-002 / 007 | RM.L2-3.11.1 | - |
| Risk Treatment | GV.RM | PM-4, CA-5 | 3.11.3 | Steps 3–5 | CIP-003 | RM.L2-3.11.3 | - |
| Risk Acceptance | GV.RM | CA-6 | 3.12.2 | Step 5 | CIP-003 | CA.L2-3.12.2 | - |
| Exception / POA&M | GV.RR | CA-5 | 3.12.2 | Step 5 | CIP Mitigation Plans | CA.L2-3.12.2 | - |
| Continuous Monitoring of Risk | DE.CM, ID.IM | CA-7 | 3.12.3 | Step 6 | CIP-007 | CA.L2-3.12.3 | Monitoring |
| Reporting & Communication | GV.RR | PM-9, PM-31 | 3.12.3 | Step 6 | CIP-003 | CA.L2-3.12.3 | Reporting |

---

## 12. Procedure Control

| | |
|---|---|
| **Document ID** | CERG-PRC-RM-001 |
| **Version** | 1.04 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Risk Register Owner |
| **Approved By** | CISO |
| **Parent Policy** | [CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual |
| **Next Scheduled Review** | 2027-06-14 |
| **Frameworks** | NIST CSF 2.0 · NIST 800-53r5 · NIST RMF |
| **Regulations** | NERC-CIP · CMMC L2 · SOX ITGC |
| **Environments** | All in-scope environments |


### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.04 | 2026-06-18 | Governance Pillar Leader | Added funding/capacity decision brief routing and clarified that funding deferral does not itself accept residual risk. |
| 1.03 | 2026-06-18 | Governance Pillar Leader | Made RMF-001 the explicit source of truth for scoring and acceptance authority, removed competing local calibration thresholds, clarified Business Owner consequence acceptance, and constrained TMPL-RM-003 to a supporting memo role. |
| 1.02 | 2026-06-18 | Governance Pillar Leader | Added §7.1 Exception vs. Risk Acceptance routing table distinguishing Security Exception (→TMPL-RM-002, Governance-tracked) from Risk Acceptance (→TMPL-RM-004, Business Owner + RMF-001 authority). Renumbered subsequent subsections. Updated §7.6 template references. |
| 1.01 | 2026-06-14 | Governance Pillar Leader | Aligned scoring bands, approval summaries, and duration guidance to the canonical RMF authority table. |
| 1.0 | 2026-05-01 | CERG Governance | Initial release |

### Review Triggers

This procedure shall be reviewed annually and upon any of the following:

- Material change to risk taxonomy or scoring scheme
- Material change to risk-management tooling
- Material change to regulatory expectations affecting risk acceptance, POA&M, or CIP deviation processes
- A significant incident or audit finding affecting the program
- Direction from the CISO

Governance owns this procedure. The Risk Register Owner is responsible for revisions, ongoing maintenance, and obtaining CISO approval for material updates.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [CERG-POL-001](../governance/CERG-POL-001_Cybersecurity_Policy.md) | Parent policy - Principle 9 |
| Grid and Control System Standard | [CERG-STD-OT-001](../standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) | OT risk and CIP deviation overlay |
| IT / Cloud / SaaS Security Standard | [CERG-STD-IT-001](../standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) | IT/Cloud/SaaS risk scope, tier-based control expectations |
| CUI Handling Standard | [CERG-STD-CUI-001](../standards/CERG-STD-CUI-001_CUI_Handling_Standard.md) | CUI risk scope, POA&M tracking |
| Access Management Standard | [CERG-STD-AC-001](../standards/CERG-STD-AC-001_Access_Management_Standard.md) | Identity-related risk and access exception handling |
| Unified Control Baseline | [CERG-GOV-CB-001](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) | Control framework that risk entries reference |
| Exposure Management Procedure | [CERG-PRC-VM-001](CERG-PRC-VM-001_Exposure_Management_Procedure.md) | Vulnerability risk acceptance path |
| Adversarial Validation Procedure | [CERG-PRC-AV-001](CERG-PRC-AV-001_Adversarial_Validation_Procedure.md) | Adversarial testing finding risk acceptance |
| Third Party and Supply Chain Risk Procedure | [CERG-PRC-TPRM-001](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) | Vendor risk register entries and tier-based acceptance authority |
| Architecture Review and Project Intake Procedure | [CERG-PRC-AR-001](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) | Project review findings flow to risk register |
| CERG Operating Model | [CERG-GOV-OM-001](../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) | Pillar structure and risk governance |

---
>
> _Identify it. Score it. Record it. Own it._

---

_CERG-PRC-RM-001 · Version 1.01 · Public_
