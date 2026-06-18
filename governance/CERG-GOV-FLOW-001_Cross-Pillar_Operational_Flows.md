| | |
|---|---|
| **Document ID** | CERG-GOV-FLOW-001 |
| **Version** | 1.1 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual |
| **Frameworks** | NIST CSF 2.0 |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed operations |

---

## Table of Contents

1. [Operating Principles](#2-operating-principles)
2. [Canonical Roles](#2-canonical-roles)
3. [Authoritative Record Types](#3-authoritative-record-types)
4. [Common Required Fields](#4-common-required-fields)
5. [Default SLA Policy](#5-default-sla-policy)
6. [Allowed Decision Classes](#6-allowed-decision-classes)
7. [Shared State Models](#7-shared-state-models)
8. [Flow F-01: Control Intent to Implementation](#8-flow-f-01--control-intent-to-implementation)
9. [Flow F-02: Project Intake, Architecture Review, and Threat Modeling](#9-flow-f-02--project-intake-architecture-review-and-threat-modeling)
10. [Flow F-03: Asset Registration and Coverage Validation](#10-flow-f-03--asset-registration-and-coverage-validation)
11. [Flow F-04: Finding to Remediation, Exception, or Residual Risk](#11-flow-f-04--finding-to-remediation-exception-or-residual-risk)
12. [Flow F-05: Change and Release Security Routing](#12-flow-f-05--change-and-release-security-routing)
13. [Flow F-06: Incident to Recovery to Standards Feedback](#13-flow-f-06--incident-to-recovery-to-standards-feedback)
14. [Flow F-07: Metrics, Oversight, and Improvement Routing](#14-flow-f-07--metrics-oversight-and-improvement-routing)
15. [LLM Execution Directives](#15-llm-execution-directives)
16. [Minimum Record Templates](#16-minimum-record-templates)
17. [Recommended Implementation Sequence](#17-recommended-implementation-sequence)
18. [Document Control](#18-document-control)

---



## 1. Flow Structure Conventions

Every flow in this document follows a consistent structure. When implementing a flow, use these conventions to ensure completeness.

### Entry and Exit Criteria

| Flow | Trigger (Entry) | Exit Criteria |
|------|----------------|---------------|
| F-01 Control Intent | Policy/standard/baseline change, audit finding, recurring incident, regulatory requirement, CISO directive | Implementation completed + Risk validated + Evidence linked + Dashboard updated |
| F-02 Project Intake | New application/service/change, cloud/SaaS adoption, new integration, regulated/AI/OT project | Security disposition issued + pre-go-live remediation done + post-go-live risks recorded + owners confirmed + handoff delivered |
| F-03 Asset Registration | Go-live approval, new asset, major change, ownership change, decommission | Owner confirmed + classification complete + coverage validated + gaps resolved as finding/risk |
| F-04 Finding → Remediation | Vulnerability, adversarial test, threat intel, third-party, incident, audit, architecture review | Treatment executed + validated + exception/acceptance recorded if used + evidence linked + reporting updated |
| F-05 Change & Release | Normal/major/emergency change, release candidate, config/identity/encryption change | Change executed + control continuity checked + SIA reviewed + emergency bypass recorded + evidence linked |
| F-06 Incident → Recovery | Validated incident, material event, third-party incident, active exploitation, regulatory notification | Containment/recovery done + timeline/investigation produced + lessons learned recorded + corrective actions assigned + evidence delivered |
| F-07 Metrics & Oversight | Monthly/quarterly cycle, threshold breach, missed SLA, maturity assessment, board request | Metrics collected + thresholds evaluated + actions assigned for outliers + CISO review done + report published |

### Minimum Process Records

After each flow executes, these records must exist. If a record is missing, the flow is incomplete.

| Flow | Required Records | Minimum Fields Documented |
|------|-----------------|--------------------------|
| F-01 Control Intent | Control Change Record | Control ID, source reason, affected environments, implementation deadline, evidence plan, validation result |
| F-02 Project Intake | Project Intake Record, Architecture Review Record, Threat Model Record | Project name, owners, go-live date, asset class, data classification, regulatory scope, review findings, disposition |
| F-03 Asset Registration | Asset Record | Asset ID, type, owners, environment, classification, criticality, coverage status |
| F-04 Finding → Remediation | Finding Record; Risk Record if promoted; Exception Record if used | Finding ID, source, severity, assets, owners, treatment, due date, validation result |
| F-05 Change & Release | Change Record | Change ID, type, assets, SIA, implementation window, rollback plan, control continuity result |
| F-06 Incident → Recovery | Incident Record, Improvement Record | Incident ID, severity, timeline, containment actions, investigation summary, lessons learned, corrective actions |
| F-07 Metrics & Oversight | Reporting Metric Record | Metric name, definition, source, period, threshold, actual value, action assigned |

### SLA Exception Logic

The severity-tiered SLAs in each flow are the default. The following exceptions are recognized:

| Exception | Applies To | Rule |
|-----------|-----------|------|
| **False Positive** | F-04 (Findings) | Close with rationale and evidence of false-positive determination. No SLA penalty. Document the determination method. |
| **Compensating Control in Place** | F-04 (Findings) | Downgrade severity by one level if compensating control is documented, tested, and operating. Create Exception Record. Original SLA clock stops; compensating control review clock starts. |
| **Vendor Patch Unavailable** | F-04 (Findings), F-01 (Control Intent) | Create Exception Record. Document vendor communication (ticket/case number). Set review date based on vendor's committed patch timeline. SLA clock pauses until vendor delivers or 90 days, whichever is shorter. |
| **OT Maintenance Window** | F-04 (Findings), F-05 (Change) | Remediation SLA extends to next approved maintenance window. Document the window date. If the window is more than 90 days out, create Risk Record. |
| **Business Outage Risk** | F-04 (Findings), F-05 (Change) | Create Risk Record. Business owner must acknowledge the risk of both the vulnerability AND the outage. CISO approves the deferral. Set a review date no more than 90 days out. |
| **Emergency Remediation** | F-04 (Findings) | Execute remediation immediately. Create Change Record post-hoc per F-05 emergency change rules. Document rationale. SLA is measured from detection to execution, not to paperwork. |
| **Reopened Finding** | F-04 (Findings) | SLA resets to the severity-tiered clock from the reopen date. Increment recurrence counter. Escalate per recurring finding rules. |
| **Accepted Risk Expiration** | F-04 (Findings), RMF-001 | Auto-create Finding Record (severity: High) if acceptance expires without renewal. Original acceptance approver is notified. |
| **KEV / Active Exploitation Override** | F-04 (Findings) | Override the existing severity. Treat as Critical regardless of CVSS score. Apply Critical SLA (48 hours). |

## 2. Operating Principles


### Record Type Definitions

These terms appear throughout the flows. Consistent usage prevents confusion during operations and audits.

| Term | Definition | Record Type | Converts To |
|------|-----------|-------------|-------------|
| **Finding** | An observed condition requiring disposition — discovered through scanning, testing, audit, or review | Finding Record | May promote to Risk Record if SLA exceeded, business decision required, or crown jewel affected |
| **Risk** | A loss-event scenario with a named owner, treatment strategy, and acceptance decision | Risk Record | May create Exception Record if control deviation is involved |
| **Exception** | An approved deviation from a control or requirement, with compensating controls, expiration, and named approver | Exception Record | Expired exceptions without renewal become Findings (severity: High) |
| **Vulnerability** | A technical weakness in an asset — the raw input to a Finding | (fields within Finding Record) | Becomes a Finding when triaged; may be directly remediated without becoming a Risk |
| **Control Gap** | A missing or ineffective control — a systemic condition, not a single finding | Finding Record or Risk Record | Usually becomes a Risk due to systemic impact |
| **Incident** | A declared security event requiring active response | Incident Record | Lessons learned may create Findings, Risks, or Control Change Records |

**Conversion Rules:**

- A Finding promotes to a Risk Record when: SLA is exceeded, the affected asset is Tier 0/Tier 1, exploitation is active, remediation requires a business decision, or compensating controls are needed.
- A Risk that involves a control deviation creates an Exception Record.
- An Exception that expires without renewal auto-creates a Finding (severity: High).
- A recurring Finding in the same control family triggers a Control Change Record (F-01).

1. **One material event creates one primary record and one accountable owner.** CERG repeatedly emphasizes authoritative records and explicit ownership as the basis for mature execution.
2. **Pre-production security work is Engineering-led unless explicitly escalated.** CERG positions Engineering as the embedded consulting and architecture-review function for projects before production.
3. **Post-production findings are Risk-led unless they are active incident-response actions.** CERG assigns Risk responsibility for continuous exposure identification through exposure management, adversarial testing, vendor assessment, and monitoring.
4. **Governance owns control intent, conformance scope, exception authority routing, evidence rules, and reporting.** CERG's governance layer includes the control system for the program: baseline, calendar, evidence, metrics, compliance mapping, and oversight artifacts.
5. **No issue may remain in an undefined state.** Every issue must become one of: remediation, compensating control, exception, accepted residual risk, or incident action.
6. **Evidence must be created during execution and linked to the primary record.** CERG's annual calendar and reporting model both assume evidence-producing activities generate or refresh evidence as part of the operating rhythm.
7. **Missed review cadence, missing ownership, or missing evidence creates a finding or risk record.** The CERG annual calendar explicitly states that missed activities are tracked as program findings or risk-register entries.

8. **Routing thresholds prevent ceremony creep.** Not every workflow requires all three pillars. The default is not "all three pillars must agree." The default is: Engineering handles known patterns, Risk engages when exposure is novel or elevated, Governance owns policy and evidence, and Business owns the consequence. Handoffs are good. Endless consensus is not.

| Work Type | Required Pillars | Rationale |
|-----------|-----------------|-----------|
| Low-risk known pattern (e.g., capacity increase, DISH-conformant config change, standard user provisioning) | Engineering only; auto-evidence | Known-safe changes do not require governance or risk review. Evidence is generated automatically. |
| Moderate known pattern (e.g., approved SaaS with no sensitive data, pre-approved architecture pattern) | Engineering + Governance conformance check | Governance confirms the pattern is still valid; no Risk engagement unless the checklist flags a risk concentration threshold. |
| Novel architecture (e.g., new technology stack, first-of-its-kind integration, citizen-development platform) | Engineering + Risk threat model | Risk performs threat modeling; Governance is informed but does not gate. |
| Regulated / OT / Crown Jewel (e.g., BES Cyber System change, CUI environment modification, SOX-relevant system) | All three pillars | Regulatory, safety, or material-financial impact requires full cross-pillar engagement. |
| High residual risk (e.g., accepted Critical risk, exception past SLA with no compensating control) | Risk-led package + Business acceptance | Risk owns the finding and treatment recommendation; Business accepts the residual risk per RMF-001. |
| Policy deviation only, low residual risk (e.g., password length exception, SSO bypass with documented compensating control) | Governance-owned exception | Governance owns the exception workflow, confirms compensating controls, and tracks expiration. |
9. **Every major event must produce a standards/process/metrics feedback decision.** CERG's RMF, incident plan, maturity model, and metrics apparatus all imply that mature operation requires monitoring and response to feed continuous improvement.

10. **If a required actor does not respond within SLA, the primary owner may proceed with documented rationale.** When Governance, Engineering, or Risk fails to act within the flow-defined SLA, the primary owner documents the default decision, proceeds with the next workflow step, and creates a Finding Record noting the missed SLA. No flow may stall indefinitely waiting for a single actor.
---

## 3. Canonical Roles

Use the following canonical role names consistently across all records and flows:

- **Engineering Pillar**
- **Risk Pillar**
- **Governance Pillar**
- **CISO**
- **Business Owner**
- **Asset Owner**
- **Technical Owner**
- **Risk Register Owner**
- **Evidence Librarian**
- **Incident Commander**
- **Control Owner**

---

## 4. Authoritative Record Types

Every material workflow must resolve to one primary system-of-record object:

- **Project Intake Record**
- **Architecture Review Record**
- **Threat Model Record**
- **Asset Record**
- **Finding Record**
- **Risk Record**
- **Exception Record**
- **Change Record**
- **Incident Record**
- **Evidence Record**
- **Improvement Record**
- **Control Change Record**
- **Reporting Metric Record**
- **Delegation Record** — Records a formal delegation of authority from a principal (e.g., CISO) to a delegate. Required for every "CISO designee" reference. Fields: delegation_id, principal_role, delegate_role, delegated_authorities, effective_date, expiry_date, CISO_approval_ref.
- **Stop-the-Line Record** — Records an escalation raised by any CERG team member who believes a decision materially violates policy or creates regulatory exposure. Fields: stl_id, trigger, originating_pillar, decision_challenged, policy_or_regulatory_citation, CISO_disposition, disposition_timestamp.

---

## 5. Common Required Fields

Every authoritative record should contain the following minimum fields:

- `record_id`
- `source_event`
- `current_state`
- `accountable_role`
- `supporting_roles`
- `business_owner`
- `technical_owner`
- `in_scope_assets`
- `data_classification`
- `regulatory_scope`
- `evidence_links`
- `due_date`
- `escalation_date`
- `closure_criteria`
- `feedback_destination`

---

## 6. Default SLA Policy

| Activity | SLA |
|----------|-----|
| Triage due | 5 business days |
| Assignment due | 5 business days |
| Validation due | 5 business days |
| Evidence link due | 3 business days |
| Escalate if past due | Yes |

---

## 7. Allowed Decision Classes

All workflows should terminate in one of the following decision classes:

- **Remediate pre-production**
- **Remediate post-production**
- **Compensating control**
- **Exception required**
- **Risk acceptance required**
- **Block release**
- **Monitor only**
- **Incident response**
- **Standards update required**
- **Metrics update required**

---

## 8. Shared State Models

### 7.1 Project Security Review State Model

Allowed states:

- Intake open
- Scope defined
- Architecture review in progress
- Threat model in progress
- Remediation required pre-go-live
- Approved for go-live
- Approved with post-go-live risk
- Blocked pending prerequisite
- Closed

### 7.2 Finding Lifecycle State Model

Allowed states:

- New
- Triage
- Assigned
- Treatment planned
- In engineering work
- Exception review
- Risk acceptance review
- Validation pending
- Residual monitoring
- Closed

### 7.3 Asset Coverage Lifecycle

Allowed states:

- Discovered
- Registered
- Owner confirmed
- Classified
- Control coverage pending
- Fully covered
- Coverage gap open
- Decommissioned

### 7.4 Incident Lifecycle

Allowed states:

- Detected
- Validated
- Classified
- Containment active
- Investigation active
- Recovery active
- Lessons learned pending
- Corrective action open
- Closed

### 7.5 Control Change Lifecycle

Allowed states:

- Proposed
- Approved for design
- Implementation designed
- Validation defined
- Rollout in progress
- Validation pending
- Evidenced
- Reported
- Closed

---

## 9. Flow F-01 — Control Intent to Implementation

### Purpose
Convert governance-originated control intent into implementable technical change and risk-validated outcomes.

### Primary Owner
**Governance Pillar**

### Supporting Owners
- Engineering Pillar
- Risk Pillar

### Trigger Events
- Policy changed
- Standard changed
- Control baseline changed
- Material audit finding
- Recurring incident pattern
- Repeated exception in same control family
- Regulatory requirement added
- Board or CISO directive

### Primary Record
**Control Change Record**

### Required Inputs
- Control ID
- Source reason (policy change, standard change, audit finding, etc.)
- Affected environments
- Affected asset classes
- Implementation deadline
- Required evidence
- Reporting metric target
- Exception path
- Preventive / detective / corrective classification


### Workflow
1. Governance creates the **Control Change Record**.
2. Governance defines **control intent and conformance scope**.
3. Engineering produces the **implementation design**.
4. Risk defines **validation criteria before rollout**.
5. Governance approves the **evidence plan**.
6. Engineering executes rollout and records implementation evidence.
7. Risk validates effectiveness.
8. Governance updates dashboard/reporting and closes or reopens the record.

### Decision Logic
- If validation is effective, close the record.
- If validation is ineffective, reopen or create Engineering action.
- If the control cannot be met as written or by deadline, route to exception workflow.

### Evidence Required
- Implementation design package
- Validation plan
- Control test or outcome evidence
- Updated reporting metric record
- Linked evidence record

### SLA
- Governance publishes package: 5 business days
- Engineering design: 10 business days
- Risk validation plan: 5 business days
- Evidence link: 3 business days

### Escalation
- Missing Engineering design after SLA → escalate to CISO and create finding
- Missing validation → do not allow closure; create risk record

### Closure Criteria
- Implementation completed
- Risk validated
- Evidence linked
- Dashboard updated

---

## 10. Flow F-02 — Project Intake, Architecture Review, and Threat Modeling

### Purpose
Ensure that new systems and major changes enter production with known scope, required controls, and explicit security disposition.

### Primary Owner
**Engineering Pillar**

### Supporting Owners
- Risk Pillar
- Governance Pillar

### Trigger Events
- New application
- New service
- Major change
- New cloud or SaaS adoption
- New integration
- Internet-exposed component
- Regulated-scope project
- AI system introduction
- IT/OT convergence change

### Primary Record
**Project Intake Record**


### Required Inputs
- Project name
- Business owner
- Technical owner
- Intended go-live date
- Asset class
- Data classification
- Regulatory scope
- AI use category, model/provider, and proposed agency boundary where AI is in scope
- Hosting environment
- External dependencies
- Privilege model
- Logging plan
- Backup / recovery plan

### Review Tiers

Projects are triaged into one of three review tiers based on risk characteristics. The tier determines review depth, not whether a review occurs. PRC-AR-001 provides the detailed procedure for each tier.

| Tier | Criteria | Review Depth | Architecture Review | Threat Model | Governance Conformance |
|------|----------|-------------|---------------------|--------------|------------------------|
| **T1 — Full Review** | Internet-exposed, regulated-scope, sensitive data, OT/safety impact, new platform pattern, high-risk third-party, complex privileged path | Full Phase 2-4 per PRC-AR-001 | Full architecture review | Full threat model | Governance issues Conformance Scope Statement |
| **T2 — Lightweight Review** | Internal service on reviewed platform, reuse of approved architecture pattern, capacity addition to reviewed system, non-sensitive data, no regulatory scope | Checklist review per PRC-AR-001 §4 | Checklist-based architecture review | Threat model review (confirm existing model covers change) | Governance confirms existing conformance applies |
| **T3 — Automated-Only** | Pre-approved change pattern (e.g., config update within baseline, dependency bump within allowed range), citizen-development platform app, pipeline already enforces SAST/policy-as-code/CSPM gates | Automated gates only; no manual review | Automated SAST + policy-as-code pass = architecture review satisfied | N/A (platform-level threat model covers) | Automated CSPM posture check = conformance satisfied |

### AI Routing Rules

When AI is in scope, the Project Intake Record links to an AI intake record using [`CERG-TMPL-AI-001`](../templates/CERG-TMPL-AI-001_AI_Intake_and_Sanctioning_Template.md) or an equivalent local record. Routing is based on the AI use case, data classification, and agency boundary:

- **Consumed AI services** may follow T2 or a pre-approved architecture pattern when the use case, user population, and maximum data classification match the sanctioned AI tools register.
- **Built AI, embedded AI, AI agents, model-serving platforms, RAG systems, or AI with consequential action capability** default to T1 unless Engineering documents why an approved pattern fully covers the use.
- **AI processing Confidential, Restricted, CUI, BES Cyber System Information, SOX-relevant data, personal data at material scale, or safety-impacting data** requires Governance conformance review and Risk participation.
- **AI-enabled vendor features** trigger third-party reassessment when the feature changes data use, training, retention, subprocessors, user population, or decision impact.
- Approved consumed AI tools update the sanctioned AI tools register using [`CERG-TMPL-AI-002`](../templates/CERG-TMPL-AI-002_Sanctioned_AI_Tools_Register_Template.md). Built or embedded AI systems update the AI system and model register using [`CERG-TMPL-AI-003`](../templates/CERG-TMPL-AI-003_AI_System_and_Model_Register_Template.md).

### Workflow (by Tier)

**T1 — Full Review:**
1. Engineering opens **Project Intake Record** and assigns T1.
2. Engineering performs initial security scoping.
3. Engineering performs full **Architecture Review** (PRC-AR-001 Phase 2).
4. Engineering performs full **Threat Model** (PRC-AR-001 Phase 2).
5. Governance issues **Conformance Scope Statement**.
6. Risk participates per risk concentration thresholds.
7. Engineering classifies issues as pre-go-live or post-go-live.
8. Engineering issues final security disposition.

**T2 — Lightweight Review:**
1. Engineering opens **Project Intake Record** and assigns T2.
2. Engineering completes the T2 checklist (PRC-AR-001 §4).
3. Engineering confirms existing threat model covers the change; documents any delta.
4. Governance confirms existing conformance scope applies.
5. Engineering issues disposition. Risk participates only if checklist flags a risk concentration threshold.

**T3 — Automated-Only:**
1. Engineering opens **Project Intake Record** and assigns T3.
2. Automated gates execute: SAST scan, policy-as-code validation, CSPM posture check.
3. If all gates pass: Engineering issues disposition. No manual review required.
4. If any gate fails: revert to T2 and flag the failure for Engineering review.

### Risk Concentration Thresholds
Risk participation is required when one or more of the following are true:
- Sensitive data present
- Regulated scope present
- Internet exposure present
- High-risk third-party dependency present
- Complex privileged path present
- OT or safety impact present
- AI system has autonomous or tool-using agency beyond draft/recommendation
- AI use expands beyond the sanctioned tool's approved use case, user population, or maximum data classification

### Allowed Dispositions
- Approved for go-live
- Approved with pre-go-live remediation
- Approved with post-go-live risk record
- Blocked pending prerequisite

### Mandatory Rules
- Every identified issue must be classified as **pre-production remediation** or **post-production managed risk**, not both.
- Any issue deferred beyond go-live must create a **Risk Record** and, where nonconformance exists, an **Exception Record candidate**.
- No go-live proceeds without named business and technical owners.
- If the project touches or creates a Tier 0/Tier 1 crown jewel (per [`CERG-GOV-CJ-001`](CERG-GOV-CJ-001_Crown_Jewel_Register_and_Scenario_Library.md)), the crown-jewel minimum control profile (CJ-001 §3.3) is a pre-go-live requirement, and the relevant loss scenarios become threat-model design targets per [`CERG-PRC-TM-001`](../procedures/CERG-PRC-TM-001_Threat_Modeling_Procedure.md).


### Closure Criteria
- Security disposition issued (approved, approved-with-remediation, approved-with-risk, or blocked)
- All pre-go-live remediation completed and validated
- Post-go-live risk records created for deferred issues
- Named business and technical owners confirmed
- Production Handoff Security Summary delivered

### Evidence Required
- Architecture Review Record
- Threat Model Record
- Conformance Scope Statement
- Production Handoff Security Summary
- AI Intake and Sanctioning Record where AI is in scope
- Sanctioned AI Tools Register entry or AI System and Model Register entry where AI is approved

### Escalation
- Go-live requested while blocked → escalate to CISO
- Missing ownership or scope → hold project and create finding

---

## 11. Flow F-03 — Asset Registration and Coverage Validation

### Purpose
Ensure every in-scope asset has ownership, classification, regulatory designation, and required control coverage.

### Primary Owner
**Engineering Pillar**

### Supporting Owners
- Risk Pillar
- Governance Pillar

### Trigger Events
- Project approved for go-live
- New asset discovered
- Major asset change
- Ownership change
- Environment change
- Regulatory scope change
- Asset decommission request

### Primary Record
**Asset Record**


### Asset Classes and Registration Requirements

Assets are classified by lifecycle to determine registration depth. Ephemeral and auto-scaling assets are registered via automated discovery, not manual entry.

| Asset Class | Examples | Registration Method | Required Fields |
|------------|----------|-------------------|-----------------|
| **Persistent** | Physical servers, VMs, databases, network appliances, SaaS platforms | Manual or automated via CMDB integration | All 14 fields below |
| **Dynamic** | Long-lived cloud instances (EC2, GCE), Kubernetes nodes, PaaS services | Automated via cloud API / CSPM discovery | Asset ID, type, environment, classification, owner, scan coverage, logging source. Remaining fields derived from tags or platform defaults. |
| **Ephemeral** | Auto-scaling instances, spot instances, containers, serverless functions, batch jobs | Automated via cloud API / orchestrator; registered at the *workload level*, not per-instance | Workload ID (e.g., ECS service name, Lambda function name, Deployment name), type, environment, classification, owner, scan coverage (inherited from platform). Individual instances tracked as members of the workload group. |

**Workload-level registration** means that a Kubernetes Deployment, an ECS Service, or a Lambda function is registered once. Individual pods, tasks, or invocations are tracked as members of that workload group. Coverage validation (§ Coverage Requirements) is assessed at the workload level, not the instance level.

### Required Inputs
- Asset ID
- Asset type
- Asset owner
- Business owner
- Technical owner
- Environment
- Data classification
- Regulatory scope
- Criticality
- Support team
- Logging source expected
- Scanning required
- Backup required
- Access review required

### Workflow
1. Engineering creates or updates **Asset Record**.
2. Engineering confirms owner and classification.
3. Risk validates scan coverage and exposure visibility.
4. Governance maps asset to control and calendar obligations.
5. Governance determines whether any coverage gap is a finding or risk.

### Coverage Requirements
- Owner assigned
- Classification complete
- Regulatory flag present if applicable
- Scan coverage established if required
- Logging source established if required
- Backup assignment established if required
- Access review population assigned if required
- For crown-jewel assets (Tier 0/Tier 1 per [`CERG-GOV-CJ-001`](CERG-GOV-CJ-001_Crown_Jewel_Register_and_Scenario_Library.md)), the CJ-001 §3.3 minimum control profile is present and verified, not merely scanned


### Closure Criteria
- Asset owner assigned and confirmed
- Classification complete
- Regulatory flag set if applicable
- Scan coverage established if required
- Logging source established if required
- Backup assignment established if required
- Access review population assigned if required
- Any coverage gap resolved as finding or risk record
- Crown-jewel minimum control profile verified for Tier 0/Tier 1 assets (per [`CERG-GOV-CJ-001`](CERG-GOV-CJ-001_Crown_Jewel_Register_and_Scenario_Library.md))

### Evidence Required
- Asset Record
- Coverage validation result
- Governance obligation map

### Metrics Generated
- Asset coverage completeness %
- Assets missing owner %
- Assets missing scan coverage %
- Assets missing logging %

---

## 12. Flow F-04 — Finding to Remediation, Exception, or Residual Risk

### Purpose
Convert discovered exposure into a deterministic treatment path: remediation, compensating control, exception, formal risk acceptance, or incident handling.

### Primary Owner
**Risk Pillar**

### Supporting Owners
- Engineering Pillar
- Governance Pillar

### Trigger Events
- Vulnerability discovered
- Adversarial validation result
- Threat intelligence match
- Third-party risk result
- Incident follow-on issue
- Audit finding
- Architecture review deferred issue

### Primary Record
**Finding Record**


### Required Inputs
- Finding ID
- Finding source (vulnerability, adversarial, threat intel, third-party, incident, audit, architecture review)
- Severity (Critical, High, Medium, Low)
- Exploitability assessment
- Affected assets
- Business owner
- Technical owner
- Regulatory scope
- Recommended treatment class
- Due date

### Workflow
1. Risk creates **Finding Record** and triages.
2. Risk identifies exposure path and treatment options.
3. Engineering assesses technical feasibility of treatment.
4. Governance determines whether exception or acceptance process is required.
5. Engineering executes remediation or compensating control if approved.
6. Risk validates closure or establishes residual monitoring.
7. Governance updates reporting and escalates recurring patterns.


### Severity-Tiered SLA

| Severity | Triage SLA | Remediation SLA | KEV / Active Exploit SLA |
|----------|-----------|----------------|--------------------------|
| **Critical** | 4 hours | 48 hours | 24 hours |
| **High** | 24 hours | 14 days | 7 days |
| **Medium** | 5 business days | 30 days | N/A |
| **Low** | 10 business days | 90 days | N/A |


### Risk Promotion Rules — When a Finding Becomes a Risk Register Entry

Not every finding needs a risk register entry. Promote a Finding to a Risk Record when any of these conditions are met:

| Condition | Action | Rationale |
|-----------|--------|-----------|
| SLA for remediation is exceeded | Create Risk Record with severity based on original finding | An overdue finding represents active, unmanaged exposure |
| Affected asset is Tier 0 (Crown Jewel) or Tier 1 (Critical) | Create Risk Record regardless of severity | High-criticality assets warrant formal risk tracking |
| Active exploitation confirmed (KEV-listed, exploit in wild) | Create Risk Record; treat as Critical | Active exploitation invalidates the original severity assessment |
| Remediation requires a business decision (budget, outage window, vendor coordination) | Create Risk Record with business owner assigned | Business decisions require business accountability |
| Compensating controls are needed | Create Risk Record and Exception Record | Compensating controls represent a deviation from the control baseline |
| Repeated finding — same vulnerability class, same system, more than twice | Create Risk Record; escalate to root cause analysis | Recurrence signals a systemic issue, not a one-time miss |
| Regulatory deviation required (CIP, CMMC, SOX) | Create Risk Record and initiate regulatory deviation process | Regulatory implications require formal tracking |

A Finding that does not meet any promotion condition is closed through the standard remediation → validation → closure path.

### Closure Validation Rules

Who can close a finding, and what evidence is required, depends on severity and source:

| Severity | Who Can Close | Minimum Evidence | Retest Required? |
|----------|--------------|-----------------|-----------------|
| **Critical** | Risk Pillar (must validate) | E3 evidence per AUD-001; authenticated re-scan or adversarial re-test | Yes — mandatory |
| **High** | Risk Pillar (must validate) | E3 evidence; authenticated re-scan or equivalent validation | Yes — mandatory |
| **Medium** | Engineering may self-close with automated validation | E2 minimum; authenticated re-scan or SAST re-scan | Yes — automated re-scan acceptable |
| **Low** | Engineering may self-close with automated validation | E2 minimum; scan report or equivalent | At discretion of closer |

**Additional closure rules:**

- Engineering may not close a Critical or High finding unilaterally. Risk must validate.
- Self-service closure (Medium/Low) requires the automated validation to reference a specific pipeline run, scan job, or test execution with a timestamp.
- If closure validation fails (retest shows finding still present): reopen the finding, increment the recurrence counter, and escalate per the recurring finding rules below.
- Closure must include a statement of what changed: "Patched to version X," "Parameterized query at line Y," "Added WAF rule Z." "Fixed" is insufficient.

### Recurring Finding Escalation

A finding that reappears after closure is different from a new finding. Escalate recurring findings as follows:

| Recurrence | Action | Escalation |
|-----------|--------|-----------|
| 1st recurrence (same vulnerability class, same system) | Reopen with "Recurring" flag; verify original closure evidence was valid | Notify Pillar Leader |
| 2nd recurrence | Root cause analysis required; document why the fix did not hold | Escalate to Pillar Leader; create Finding Record for the root cause |
| 3rd recurrence | Treat as systemic control failure | Create Risk Record; escalate to CISO; consider Control Change Record (F-01) |

Recurring findings across multiple systems in the same control family trigger a Control Change Record regardless of recurrence count per system.

### Allowed Treatment Paths
- Immediate remediation
- Planned remediation
- Redesign
- Compensating control
- Exception request
- Formal risk acceptance
- Incident response (if active exploitation exists)

### Mandatory Rules
- No finding may remain undefined beyond triage SLA.
- Engineering may not close a Critical or High finding unilaterally; Risk must validate.
- **Self-Service Closure (Medium/Low):** Engineering may close Medium and Low findings when automated validation confirms the fix. Automated validation includes: authenticated vulnerability re-scan (findings from scanning), SAST re-scan passing (findings from code review), CSPM posture check passing (findings from cloud posture), or policy-as-code gate passing (findings from IaC review). Risk validates Medium/Low findings by exception — spot-checking a sample rather than re-validating every closure.
- Any control not met as written or on time routes to exception review.
- Accepted residual risk requires named approver, rationale, review cadence, and expiration if applicable.

### Mandatory Rules
- No finding may remain undefined beyond triage SLA.
- Engineering may not close a finding unilaterally; Risk must validate.
- Any control not met as written or on time routes to exception review.
- Accepted residual risk requires named approver, rationale, review cadence, and expiration if applicable.



### Validation Method by Finding Source

| Finding Source | Minimum Validation Method | Sufficient Evidence |
|----------------|--------------------------|---------------------|
| Vulnerability scan | Authenticated re-scan of affected asset | Scan report showing finding resolved |
| Adversarial test | Targeted re-test of the specific finding | Test report confirming closure |
| Code review (SAST) | Re-scan + code diff review for High/Critical | Scan report + reviewer sign-off |
| Architecture review | Architecture Review Record updated | Signed disposition from Engineering |
| Threat intelligence | IOC search across environment | Negative search result |
| Audit finding | Evidence package per auditor specification | Auditor acceptance confirmation |
| Third-party risk | Vendor attestation or re-assessment | Updated vendor assessment |

### Closure Criteria
- Treatment executed (remediation, compensating control, exception, or risk acceptance)
- Risk validation confirms closure or establishes residual monitoring
- Exception or risk-acceptance record created if used
- Evidence linked to finding record
- Reporting updated

### Evidence Required
- Triage result
- Engineering treatment plan
- Remediation or compensating-control evidence
- Validation result
- Exception or risk-acceptance record if used

### Escalation

| Trigger | Escalation Target | Action |
|----------|------------------|--------|
| Critical finding unassigned after **4 hours** | CISO | Immediate notification; CISO may invoke incident response |
| Critical finding past remediation SLA (48 hours) | CISO | Mandatory review; create risk record for delayed remediation |
| High finding unassigned after **24 hours** | Pillar Leader (Risk) | Pillar Leader must assign or explain |
| High finding past remediation SLA (14 days) | Governance Pillar Leader | Create exception record or escalate to CISO |
| Medium finding past SLA (30 days) | Risk Pillar Leader | Included in monthly roll-up report; risk of SLA drift |
| Low finding past SLA (90 days) | Risk Pillar Leader | Included in quarterly review |
| Repeated exception in same control family | Governance Pillar Leader | Create Control Change Record (F-01) |
| Engineering refuses or stalls treatment | Pillar Leader (Risk → Engineering) | Cross-pillar escalation; CISO if unresolved after 5 business days |

---

## 13. Flow F-05 — Change and Release Security Routing

### Purpose
Ensure that security-significant changes receive consistent cross-pillar handling.

### Primary Owner
**Engineering Pillar**

### Supporting Owners
- Risk Pillar
- Governance Pillar

### Trigger Events
- Normal change requested
- Major change requested
- Emergency change requested
- Release candidate created
- Production configuration change
- Identity model change
- Encryption or key change
- New external dependency

### Primary Record
**Change Record**


### Required Inputs
- Change ID
- Change type (normal, major, emergency)
- Affected assets
- Implementation window
- Rollback plan
- Security impact analysis
- Data classification
- Regulatory scope
- Testing plan

### Change Classification and Required Activities

Not all changes carry the same security risk. The table below defines what each change class requires. "SIA" = Security Impact Analysis. "CC" = Control Continuity check.

| Change Class | Examples | SIA Required | SIA Depth | Control Continuity Scope | Risk Review | Fast-Lane Eligible |
|-------------|----------|-------------|-----------|--------------------------|-------------|--------------------|
| **Pre-Approved** | Documentation update, dashboard color change, log format adjustment, non-security config change within approved baseline, dependency bump within allowed semver range | No | N/A | None — change has no security surface | No | Yes — deploy immediately, record change post-hoc |
| **Standard** | New feature deployment, scaling adjustment, routine cert rotation, IAM role addition within existing policy, database schema change | Yes | Lightweight — confirm change does not alter security boundary | Verify specific controls affected by the change (e.g., cert rotation → CR-001 controls; IAM change → AC-2 controls) | No, unless risk-significant criteria met | No — standard flow |
| **Major** | New service introduction, architecture change, firewall rule change, encryption protocol change, identity model restructure, new external dependency | Yes | Full — assess impact across all control families | Verify all controls on affected assets; confirm no control regression | Yes — mandatory Risk review | No — requires full review |
| **Emergency** | Active incident remediation, zero-day patch, critical service restoration | Yes — post-execution within 24 hours | Full — documented after execution | Verify as soon as practical; automate where possible | Post-execution; linked risk or exception required for any deviation | Yes — bypass normal gates; document rationale and create post-hoc record |

**Control Continuity Scope by Change Class:**
- **Pre-Approved:** No control continuity check required.
- **Standard:** Verify the specific controls directly affected by the change. A cert rotation verifies CR-001 controls. An IAM role addition verifies AC-2 controls for the new role. Do not re-verify unrelated controls.
- **Major:** Verify all controls mapped to the affected assets (per CB-001). Confirm no control has regressed.
- **Emergency:** Verify as soon as practical. Automated CSPM/CNAPP scanning is acceptable as control continuity evidence. Document any gaps as a finding.

### Workflow
1. Engineering classifies the change per the table above and opens **Change Record**.
2. For Pre-Approved: deploy immediately; create Change Record post-hoc. Skip to step 6.
3. For Standard: Engineering completes lightweight SIA. For Major/Emergency: Engineering completes full SIA.
4. Risk reviews if change is risk-significant (Standard) or mandatory (Major/Emergency).
5. Governance applies conformance and evidence requirements (Standard/Major/Emergency).
6. Engineering executes the change.
7. Engineering performs control continuity checks per the scope defined above.
8. Governance verifies evidence and closes or reopens the change.

### Risk-Significant Change Criteria
- Internet exposure changed
- Privileged access changed
- Logging coverage impacted
- Backup or recovery path changed
- Encryption or key handling changed
- Third-party dependency added or materially modified
- Regulated-scope asset impacted
- Emergency bypass used

### Mandatory Rules
- Emergency security deviations require linked risk or exception review.
- Change closure requires control continuity verification, not only service success.
- Missing rollback strategy blocks major-change approval.


### Closure Criteria
- Change executed successfully
- Control continuity checks passed
- Security Impact Analysis completed and reviewed
- Risk or exception record created if emergency bypass used
- Evidence linked to change record
- Governance verification complete

### Evidence Required
- Security Impact Analysis
- Test evidence
- Control continuity result
- Linked risk or exception if applicable

---

## 14. Flow F-06 — Incident to Recovery to Standards Feedback

### Purpose
Handle incidents consistently across environments while forcing lessons learned into engineering controls, risk posture, and governance artifacts.

> **IR Ownership:** The standing Incident Response team owns incident operations, the IR plan, regulatory notification clocks, and exercise management. CERG is not responsible for IR operations. This flow defines CERG's *supporting role* during incidents — evidence collection, reporting, and ensuring lessons learned feed back into CERG controls, standards, and metrics. The Incident Commander's authority during an active incident supersedes any CERG workflow step.

### Primary Owner
**Risk Pillar**

### Supporting Owners
- Engineering Pillar
- Governance Pillar
- CISO

### Trigger Events
- Alert validated as incident
- Material security event declared
- Third-party incident with internal impact
- Active exploitation of known issue
- Regulatory notifiable event

### Primary Record
**Incident Record**


### Required Inputs
- Incident ID
- Severity
- Detected time
- Affected assets
- Suspected scope
- Business owner
- Incident commander
- Regulatory scope
- Legal / notification requirements
- Containment strategy


### Incident Severity Classification and Response Times

| Severity | Description | IC Assignment | Containment Target | Lessons Learned Due |
|----------|------------|--------------|-------------------|---------------------|
| **P1 — Critical** | Active threat to life safety, grid reliability, or material business disruption | 15 minutes | 4 hours | 5 business days |
| **P2 — High** | Confirmed compromise of regulated data, privileged access, or crown jewel system | 1 hour | 24 hours | 10 business days |
| **P3 — Medium** | Suspected compromise, policy violation with exposure, or third-party incident with internal impact | 24 hours | 5 business days | 30 days |
| **P4 — Low** | Isolated policy violation, informational alert, or routine incident | 5 business days | Next business day after triage | 90 days |

### Workflow
1. Risk validates and classifies incident.
2. CISO assigns or confirms Incident Commander.
3. Engineering executes containment, eradication, and recovery changes.
4. Governance manages notifications, evidence, and reporting obligations.
5. Risk completes scope analysis and root cause assessment.
6. Governance opens lesson-learned and feedback decision record.
7. Engineering implements required corrective actions.
8. Governance determines standards, procedure, and metrics updates.

### Mandatory Post-Incident Outputs
- Root cause class
- Control failure class
- Standards/procedure change decision
- Metrics/KRI update decision
- Corrective-action owner
- Review due date

### Mandatory Rules
- Incident closure requires a lessons-learned decision, not only technical recovery.
- If an incident exposes previously accepted risk, the acceptance rationale must be reviewed.
- Recurring incident pattern in the same control family creates a Control Change Record.


### Closure Criteria
- Containment, eradication, and recovery completed
- Incident timeline and investigation summary produced
- Root cause class and control failure class determined
- Lessons-learned decision recorded (standards, procedure, or metrics update — or no-change-with-rationale)
- Corrective actions assigned with owner and due date
- Notification and evidence package delivered
- Previously accepted risk reviewed if incident exposed it

### Evidence Required
- Incident timeline
- Recovery action log
- Investigation summary
- Notification and evidence package
- Improvement record

---

## 15. Flow F-07 — Metrics, Oversight, and Improvement Routing

### Purpose
Convert operational data into management action, improvement backlog, standards review, risk escalation, and board-grade reporting.

### Primary Owner
**Governance Pillar**

### Supporting Owners
- Risk Pillar
- Engineering Pillar
- CISO

### Trigger Events
- Monthly reporting cycle
- Quarterly reporting cycle
- Metric threshold breach
- Repeated missed SLA
- Maturity assessment run
- Board or executive request
- Repeated control failure pattern

### Primary Record
**Reporting Metric Record**


### Required Inputs
- Metric name
- Metric definition
- Source system
- Reporting period
- Threshold (green / amber / red)
- Actual value
- Evidence link
- Accountable role
- Interpretation note

### Workflow
1. Governance collects metrics per canonical dictionary.
2. Risk supplies exposure and residual-risk metrics.
3. Engineering supplies implementation and quality metrics.
4. Governance evaluates thresholds and trends.
5. Governance assigns action type for each outlier.
6. CISO reviews material outliers and escalations.
7. Governance publishes monthly or quarterly report.

### Allowed Action Types
- Engineering action
- Risk escalation
- Governance standards review
- Exception review
- No action with rationale

### Baseline Cross-Pillar Metrics
- % of new assets fully covered within SLA
- % of pre-production findings closed before go-live
- % of post-production findings assigned within 5 business days
- % of exceptions with active compensating controls
- Median time from discovery to validated closure
- % of incidents resulting in standards or procedure update
- % of board metrics backed by direct evidence

- % of Critical/High findings where validation method was E3 (adversary-facing test or authenticated re-scan) vs. E2 (process artifact only)
- % of accepted risks re-opened due to threat landscape change within 12 months of acceptance
- weighted sum of (open findings × 1) + (open exceptions × 3) + (accepted risks × 2) per NIST control family
- % of exceptions within 30 days of expiration without a renewal or closure decision
- % of flow steps where a pillar missed its SLA, reported monthly per pillar
- **Review cycle time by tier**: median hours/days from F-02 intake to security disposition, reported by review tier (T1/T2/T3) — measures whether review depth is proportional to project risk
- **Deployment frequency of reviewed projects**: number of deployments per week for projects that passed F-02 review — measures whether security review enables or impedes delivery velocity
- **Pre-approved change ratio**: % of F-05 changes classified as Pre-Approved vs. Standard/Major — measures whether the change classification model is appropriately tuned; a ratio below 30% suggests over-classification
- **Automated closure rate**: % of F-04 Medium/Low findings closed via self-service automated validation vs. manual Risk validation — measures automation adoption
- **SLA breach rate by pillar**: % of flow steps where a pillar missed its SLA, reported monthly per pillar — identifies bottlenecks across Engineering, Risk, and Governance
### Mandatory Rules
- Every threshold breach must produce an action type or explicit no-action rationale.
- Metrics without evidence links are not board-reportable.
- Repeated outlier in same control family creates a Control Change Record or Improvement Record.

---


### Closure Criteria
- Metrics collected from all three pillars per canonical dictionary
- Thresholds and trends evaluated
- Action type assigned for every outlier (engineering action, risk escalation, standards review, exception review, or no-action-with-rationale)
- Material outliers reviewed by CISO
- Monthly or quarterly report published
- Repeated outliers in same control family escalated to Control Change Record or Improvement Record



## 16. Automation Integration Points

The flows in this document describe human-driven steps, but automated security controls can satisfy or accelerate many of them. The table below defines where automation is accepted as valid execution and what evidence is required.

| Flow Step | Automated Equivalent | Evidence Required | Tier Equivalent |
|-----------|---------------------|-------------------|-----------------|
| F-02 Architecture Review | SAST scan passes in CI/CD pipeline; policy-as-code gates pass at apply time | Pipeline run ID + scan results | T3 (Automated-Only) for pre-approved patterns; supports T2 (Lightweight) for internal services |
| F-02 Threat Model | Platform-level threat model on file; change within modeled scope | Reference to existing threat model + delta analysis | T2/T3 |
| F-03 Asset Registration | Cloud API / CSPM auto-discovery; tag-based owner/classification assignment | CSPM inventory export; tag audit log | Automated for Dynamic and Ephemeral classes |
| F-04 Finding Validation | Authenticated vulnerability re-scan; SAST re-scan; CSPM posture re-check; policy-as-code gate re-run | Scan report + finding ID correlation | E3 for code/vulnerability findings; E2 for config findings |
| F-05 Security Impact Analysis | IaC diff analysis; policy-as-code evaluation of proposed change; blast radius assessment from CMDB | Automated SIA report; policy evaluation result | Standard/Major — augments but does not replace human SIA for Major changes |
| F-05 Control Continuity Check | CSPM/CNAPP posture scan post-deployment; automated control test suite | Posture scan report; test suite results | Acceptable for Standard changes; augments Major change CC |
| F-07 Metric Collection | API integration with scanning tools, pipeline analytics, CSPM dashboards | API response or dashboard export with timestamp | Fully automated |

**Automation Evidence Standard:** Automated evidence must be traceable to a specific pipeline run, scan job, or API call with a timestamp and a unique identifier. A link to the pipeline run (e.g., CI/CD run #1247) is sufficient; screenshots are not required when a programmatic reference is available.

**When Automation Satisfies a Step Entirely:** For T3 (Automated-Only) projects and Pre-Approved changes, automated gate passage satisfies the requirement with no human review. For T2 and Standard changes, automation satisfies evidence requirements but a human reviewer confirms it. For T1 and Major changes, automation augments but does not replace human review.

---

## 17. Evidence Quality Tiers

Not all evidence proves the same thing. Flows reference evidence by tier so that operators know what level of proof is required.

| Tier | Name | What It Proves | Example | Required For |
|------|------|---------------|---------|--------------|
| **E1** | Control Exists | The artifact that implements the control is present | JML log file exists in the evidence library | Routine governance checks (F-03, F-07) |
| **E2** | Control Operates | The control processed a transaction successfully | JML log shows 3 leavers processed this month; access review spreadsheet completed | Standard evidence collection; Medium/Low finding closure (F-04) |
| **E3** | Control Is Effective | An adversary-facing test, independent verification, or automated re-validation confirms the control works as intended | Automated authenticated vulnerability re-scan confirming fix; SAST re-scan passing with no regressions; policy-as-code gate passing for IaC change; CSPM posture check confirming drift remediation. Full penetration test is E3+ and reserved for adversarial-sourced findings (pen test, red team) or when automated validation is architecturally impossible. | Critical/High finding closure (F-04); control test results (F-01); incident post-mortem validation (F-06) |

Flows that specify "Evidence Required" should note the minimum tier. Where E3 is not feasible (e.g., architecturally impossible to test), the rationale must be documented in the record.

---

## 18. LLM Execution Directives


These instructions tell an LLM how to execute the flows without ambiguity:

1. **Always identify the primary record before taking action.** If no primary record exists, create it first.
2. **Always assign exactly one accountable role.** Supporting roles may be many; accountability must be singular.
3. **If an issue is pre-production, default owner is Engineering.** If post-production, default owner is Risk. If it concerns standards, exceptions, evidence, or reporting, include Governance.
4. **Never close a finding based on implementation evidence alone.** Require validation from Risk.
5. **Never treat control deviation informally.** If deadline or control intent cannot be met, route to an Exception Record.
6. **If required owner, classification, or evidence is missing, mark the item blocked or gap-open and create a finding or risk as defined by the relevant flow.**
7. **At closure of any major event, require a feedback destination:** standards, procedure, metric, backlog, risk register, or no-change-with-rationale.
8. **If SLA breach occurs, escalate according to the flow; do not silently continue.**
9. **Use canonical CERG role names and record names consistently.**
10. **Prefer evidence generation during execution over retrospective evidence collection.**

---

## 19. Minimum Record Templates

### 16.1 Finding Record

Required fields:
- Finding ID
- Source
- Severity
- Exploitability
- Affected assets
- Business owner
- Technical owner
- Regulatory scope
- Treatment class
- Current state
- Due date
- Evidence links

### 16.2 Exception Record

Required fields:
- Exception ID
- Control ID
- Affected asset
- Rationale
- Compensating controls
- Residual risk
- Approver
- Expiration date
- Monitoring cadence
- Linked risk ID
- Evidence links

### 16.3 Risk Record

Required fields:
- Risk ID
- Risk statement
- Inherent risk
- Residual risk
- Owner
- Treatment strategy
- Review cadence
- Linked findings
- Linked exceptions
- Status

### 16.4 Asset Record

Required fields:
- Asset ID
- Asset type
- Owner
- Business owner
- Technical owner
- Environment
- Classification
- Regulatory scope
- Criticality
- Scan coverage
- Logging coverage
- Backup assignment
- Access review population
- Status

### 16.5 Incident Record

Required fields:
- Incident ID
- Severity
- Incident commander
- Affected assets
- Current state
- Notification obligations
- Containment actions
- Investigation summary
- Recovery actions
- Lessons-learned decision
- Corrective-action owner

---

## 20. Recommended Implementation Sequence

### Phase 1
Implement:
- Global contract (§1-6)
- Shared state models (§7)
- Flow F-02 (Project Intake / Architecture Review / Threat Model)
- Flow F-03 (Asset Registration / Coverage Validation)
- Flow F-04 (Finding to Remediation / Exception / Risk)

### Phase 2
Implement:
- Flow F-05 (Change and Release Security Routing)
- Flow F-06 (Incident to Recovery to Standards Feedback)

### Phase 3
Implement:
- Flow F-01 (Control Intent to Implementation)
- Flow F-07 (Metrics, Oversight, and Improvement Routing)

---

## 21. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-FLOW-001 |
| **Version** | 1.1 |
| **Status** | Approved |
| **Effective Date** | 2026-06-17 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual |
| **Next Scheduled Review** | 2027-06-11 |
| **Frameworks** | NIST CSF 2.0 |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed operations |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.1 | 2026-06-17 | Governance Pillar Leader | Added AI routing rules to F-02, including AI intake, sanctioned-tool register, system/model register, and escalation criteria for sensitive data, regulated scope, consequential decisions, and autonomous agency. |
| 1.0 | 2026-06-11 | Governance Pillar Leader | Initial release. Seven cross-pillar operational flows, five shared state models, five minimum record templates, LLM execution directives, and recommended implementation sequence. |

### Review Triggers

- Change to the CERG Operating Model (OM-001)
- Change to the Risk Management Framework (RMF-001)
- Change to the Control Baseline (CB-001)
- Material incident or audit finding that exposes a flow gap
- Direction from the CISO

Governance owns this document. The Governance Pillar Leader is responsible for initiating reviews, managing the revision cycle, and obtaining approval for all changes.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| CERG Operating Model | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) | Canonical roles and pillar structure |
| Risk Management Framework | [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) | Risk treatment, exception, and acceptance rules |
| Unified Control Baseline | [`CERG-GOV-CB-001`](CERG-GOV-CB-001_Unified_Control_Baseline.md) | Control inventory and evidence standards |
| Compliance Matrix | [`CERG-GOV-CMX-001`](CERG-GOV-CMX-001_Compliance_Matrix.md) | Regulatory and framework mapping |
| Metrics and Reporting | [`CERG-GOV-MTR-001`](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) | Metric definitions and reporting cadence |
| Annual Calendar | [`CERG-GOV-CAL-001`](CERG-GOV-CAL-001_Annual_Security_and_Governance_Calendar.md) | Operating rhythm and cadence |
| Architecture Review Procedure | [`CERG-PRC-AR-001`](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) | Project intake and architecture review process |
| Artificial Intelligence Security Standard | [`CERG-STD-AI-001`](../standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md) | Governs AI use categories, AI-specific threats, sanctioned tools, and shadow AI |
| AI Intake and Sanctioning Template | [`CERG-TMPL-AI-001`](../templates/CERG-TMPL-AI-001_AI_Intake_and_Sanctioning_Template.md) | Required AI intake record for F-02 where AI is in scope |
| Sanctioned AI Tools Register Template | [`CERG-TMPL-AI-002`](../templates/CERG-TMPL-AI-002_Sanctioned_AI_Tools_Register_Template.md) | Register updated when consumed AI tools are approved |
| AI System and Model Register Template | [`CERG-TMPL-AI-003`](../templates/CERG-TMPL-AI-003_AI_System_and_Model_Register_Template.md) | Register updated when built or embedded AI systems are approved |
| Risk Register and Exception Process | [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Exception and risk acceptance workflow |
| Incident Response Plan | [`CERG-PLN-IR-001`](../plans/CERG-PLN-IR-001_Incident_Response_Plan.md) | Standing IR procedures |
