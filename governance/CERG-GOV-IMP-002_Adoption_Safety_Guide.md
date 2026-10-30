| | |
|---|---|
| **Document ID** | CERG-GOV-IMP-002 |
| **Version** | 1.5 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual |
| **Frameworks** | NIST CSF 2.0 |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG adopters |

---

## Table of Contents

1. [Before You Start](#1-before-you-start)
2. [What Not to Adopt Yet](#2-what-not-to-adopt-yet)
3. [Adoption Anti-Patterns](#3-adoption-anti-patterns)
4. [The Decision Log](#4-the-decision-log)
5. [Risk Acceptance Guardrails](#5-risk-acceptance-guardrails)
6. [Regulatory Honesty](#6-regulatory-honesty)
7. [Role Safety for Small Teams](#7-role-safety-for-small-teams)
8. [Safe vs. Dangerous Changes](#8-safe-vs-dangerous-changes)
9. [Document Control](#9-document-control)

---

## 1. Before You Start

CERG is an operating model and document corpus for standing up a cybersecurity program. It is not a control checklist, a compliance certificate, or a substitute for organizational commitment.

Before you fork, edit, or adopt any CERG artifact as authoritative, you must have:

- A named CISO or accountable security owner with executive authority
- A named executive sponsor outside the security team
- A defined scope of systems, business units, or environments
- Known regulatory obligations (even if you defer the regulatory packages)
- An asset inventory or CMDB source (even if incomplete)
- A vulnerability scanner or discovery method
- An identity source of truth (IdP, directory)
- A ticketing or work-tracking system
- A place to store evidence (shared drive, GRC tool, document management system)
- Approval authority for policy adoption
- Business owners who can accept risk for their systems
- An Incident Response owner identified (even if IR is separate from CERG)

If any of these are missing, do not adopt CERG as your authoritative operating model. Use it as a planning reference until they exist. Adopting CERG without these prerequisites will produce approved documents that nobody can actually operate.

Before adopting, read at least one [Day in the Life story](../examples/day-in-the-life/README.md). Stories are illustrative, not normative, but they show what the spine actually looks like when two or three people run it under real pressure. If the story's rhythm does not fit your organization, the spine will not either.

---

## 2. What Not to Adopt Yet

The full CERG corpus is designed for a mature, fully-staffed program. Adopting everything on day one is the most common failure mode. Start with the spine — the minimum set of documents needed to run a security program — and layer on the rest as your program matures.

### Adopt First (The Spine)

These documents form the minimum viable program. Every adopter needs them:

| Document | Why |
|----------|-----|
| Cybersecurity Policy (POL-001) | Anchors everything. Board/CISO must approve. |
| Operating Model (OM-001) | Defines roles, pillars, and handoffs. |
| Risk Management Framework (RMF-001) | How risk is identified, scored, treated, and accepted. |
| Risk Register and Exception Process (PRC-RM-001) | The operational risk workflow. |
| Exposure Management Procedure (PRC-VM-001) | The operational vulnerability workflow. |
| Unified Control Baseline (CB-001) | What controls you are implementing. |
| Document Catalog (CAT-001) | Inventory of what exists and what is planned. |
| Architecture Review Procedure (PRC-AR-001) | How projects get security review. |
| Implementation Guide (IMP-001) | How to adapt CERG to your organization. |
| **This document** (IMP-002) | How to avoid the common failure modes. |

### Defer Until the Spine Is Running

These documents add value but are not needed on day one. Adopt them after you have completed at least one full cycle of risk register review, exposure management, and project intake:

- Full workforce planning (WFP-001)
- Succession planning (SUCC-001)
- Full maturity self-assessment (MAT-001)
- ISO 27001 operational package (PLN-ISO-001)
- SOX ITGC operational package (PLN-SOX-001) — unless SOX applies
- CMMC operational package (PLN-CUI-001) — unless CMMC applies
- NERC-CIP operational package (PLN-CIP-001) — unless NERC-CIP applies
- Board and CISO reporting deck template (TMPL-MTR-001) — use a simple status report first
- Full role architecture with per-role JDs (roles/jf-*/) — the family overviews (JF-001, JF-002) are sufficient
- Cross-pillar operational flows (FLOW-001) — the procedures themselves (PRC-*) are sufficient for initial adoption

### Run at Month 2

The following artifacts are not adopted (they are templates or surveys), but they are run on a schedule starting at month 2 of adoption:

- **Stakeholder perception survey ([`CERG-TMPL-GOV-001`](../templates/CERG-TMPL-GOV-001_Stakeholder_Perception_Survey.md))** — administer the first survey at month 2 (after one full cadence cycle), then annually. Per [`CERG-GOV-SLC-001`](../governance/CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md), the annual-only cadence is intentionally paired with monthly Service Responsiveness metrics (SR-001 through SR-005 in [`CERG-GOV-MTR-001`](../governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md)) so friction is caught continuously, not only once a year.

### Never Adopt Blindly

- Never adopt a regulatory package unless the regulation actually applies to your organization.
- Never adopt a template without understanding the parent procedure it serves.
- Never mark a control "Implemented" without evidence.
- Never accept a risk without a named business owner.

---

## 3. Adoption Anti-Patterns

These are the ways CERG adoption fails. If you recognize your organization in any of these, stop and fix the pattern before continuing. The broader cross-domain anti-pattern reference is [`CERG-GOV-ANTI-001`](CERG-GOV-ANTI-001_CERG_Anti_Pattern_Catalog.md).

### Anti-Pattern 1: Fork-and-Declare

**What it looks like:** Fork the repo, change the organization name, declare the program complete. No evidence collected. No risk register populated. No vulnerability cadence running.

**Why it fails:** CERG is an operating model, not a compliance artifact. Forking the documents does not implement the controls. An auditor or assessor will ask for evidence, not a PDF of a policy.

**Fix:** Adopt the spine documents first. Run one cycle of risk register review, exposure management, and project intake before declaring adoption.

### Anti-Pattern 2: Delete Roles Instead of Consolidating

**What it looks like:** "We only have a small team, so we deleted the roles we cannot staff separately."

**Why it fails:** The canonical roles define the work that needs to be done, not the headcount. When you delete a role, you delete the accountability for that work. The work still exists — it just has no owner.

**Fix:** Consolidate roles onto fewer people, but keep the accountability assignments visible. Use the scaling map in RAC-001 §8. Document every consolidation in the Decision Log. Example: "Governance Pillar Leader also serves as Risk Register Owner and Evidence Librarian" — not "deleted Risk Register Owner."

### Anti-Pattern 3: Optimistic Control Status Inflation

**What it looks like:** Mark every control "Implemented" because a policy says it should exist. No evidence. No testing. No validation.

**Why it fails:** Control status without evidence is a claim, not a fact. When an incident or audit exposes the gap, the gap was always there — the status just hid it.

**Fix:** Use the control status decision tree: Applicable? → Designed? → Operating? → Evidenced? Mark "Partially Implemented" or "Planned" where evidence is absent. An honest gap is better than a false claim.

### Anti-Pattern 4: Security Absorbs All Risk

**What it looks like:** Every risk in the register has "Security" or "CISO" as the owner.

**Why it fails:** Security does not own the business processes, the revenue impact, the customer relationships, or the regulatory obligations. When security owns all risk, business owners have no incentive to make secure choices, and security becomes the department that says "no" because it carries all the liability.

**Fix:** Every risk must have a named business owner outside the security team. The Risk Register and Exception Process (PRC-RM-001) requires this. If a business owner refuses, escalate to the executive sponsor.

### Anti-Pattern 5: Governance as Blocker

**What it looks like:** Every project, change, and exception waits for Governance approval. Governance becomes the department that slows everything down.

**Why it fails:** CERG's operating philosophy is "yes, and here are the conditions that make this safe." When Governance becomes a gatekeeper instead of an enabler, teams route around it, and real risk goes unmanaged.

**Fix:** Use the timeout-bypass principle (FLOW-001 §2, principle 10). Define decision rights clearly. Delegate routine approvals to Pillar Leaders. Reserve Governance escalation for material risk decisions.

### Anti-Pattern 6: Risk as Vulnerability Scanning Only

**What it looks like:** The Risk function runs the vulnerability scanner. That is its entire job description.

**Why it fails:** Risk owns threat intelligence, adversarial validation, vendor risk, detection engineering, identity risk, OT risk, and the risk register. Reducing Risk to vulnerability scanning leaves most of the organization's exposure unmanaged.

**Fix:** Staff Risk for its full scope, or document which Risk functions are deferred and why. A small team may consolidate Risk roles, but the functions they cover should be explicit.

### Anti-Pattern 7: Engineering as Late-Stage Review Gate

**What it looks like:** Engineering is brought in at the end of a project to "review security" before go-live.

**Why it fails:** Architecture review that happens at the end catches problems when they are expensive to fix. Engineering should be in the design conversation early enough to change the design cheaply.

**Fix:** Integrate Engineering into project intake at concept stage, not at go-live. The Architecture Review Procedure (PRC-AR-001) defines this. A review that consistently surfaces "we have to redo the data flow now" came too late.

### Anti-Pattern 8: Uncalibrated Starter Values Become Operational

**What it looks like:** The risk appetite uses preliminary default dollar bands requiring organizational calibration ($2M, $5M, $10M). Nobody calibrates them. Risk acceptance decisions are made against uncalibrated thresholds.

**Why it fails:** Starter values are not your organization's actual risk tolerance. Accepting a $1.9M risk because "the uncalibrated default says $2M" is an arbitrary decision dressed as a framework.

**Fix:** Calibrate risk appetite values to your organization's actual revenue, downtime cost, regulatory exposure, and insurance retention. If you cannot calibrate, explicitly document that risk acceptance uses qualitative judgment until calibration occurs.

### Anti-Pattern 9: Running the Process Without Executive Sponsorship

**What it looks like:** The security team adopts CERG. The CISO is enthusiastic. Nobody above the CISO knows it exists.

**Why it fails:** CERG requires business owners to accept risk. It requires executive approval for Critical risk acceptance. It requires budget for tooling and staffing. Without an executive sponsor outside security, these decisions have no authority.

**Fix:** The executive sponsor must be named, briefed, and committed before adoption proceeds past the spine. Their name appears in the Implementation Guide's organization profile.

### Anti-Pattern 10: Creating a Risk Register That Is Never Reviewed

**What it looks like:** The risk register exists. It has entries. Nobody reviews it on cadence.

**Why it fails:** A risk register that is not reviewed is a tombstone, not a management tool. Risks age. Treatments stall. Acceptances expire. The register becomes a historical record instead of an operational instrument.

**Fix:** Schedule the first risk register review before creating the register. The review cadence is non-negotiable. If the review is missed, create a Finding Record (per FLOW-001 F-07 mandatory rules).

### Anti-Pattern 11: Buying Tools Instead of Building Capability

**What it looks like:** The organization buys a SIEM, scanner, GRC platform, CSPM, or ticketing workflow and declares the capability implemented.

**Why it fails:** A tool can support a capability, but it is not the capability. Detection requires tuned analytics, triage ownership, response paths, and validation. Exposure management requires asset coverage, prioritization, owner follow-up, SLA tracking, and risk treatment. Governance requires decision rights, evidence quality, review cadence, and accountable owners. Without the operating model around the tool, the purchase becomes another source of alerts, dashboards, and status meetings.

**Fix:** For every tool adopted, name the capability it supports, the procedure it feeds, the owner who acts on its output, and the evidence that proves the capability operates.

| Tool or Platform | Capability It May Support | Evidence the Capability Exists |
|---|---|---|
| Vulnerability scanner | Exposure management | Coverage report, triaged finding records, SLA dashboard, validated closure evidence |
| SIEM / detection platform | Detection and monitoring | Source inventory, detection coverage record, alert triage metrics, purple-team validation results |
| GRC platform | Governance and evidence management | Approved risk decisions, exception records, evidence index, retrieval test results |
| CSPM / SSPM | Cloud and SaaS posture management | Posture findings, assigned owners, remediation records, exception or acceptance decisions |
| Ticketing workflow | Work tracking | Linked owners, due dates, closure evidence, escalation history |

A capability exists only when the organization can perform the work, produce evidence, and improve from what it learns. If the tool is present but those outputs are absent, the capability is still Ad Hoc.

---

## 4. The Decision Log

Every tailoring decision — every document deferred, every role consolidated, every threshold changed — must be captured. Without a decision log, future team members, auditors, and assessors cannot understand why the program looks the way it does.

### Decision Log Template

| Field | Description |
|-------|-------------|
| **Decision ID** | DEC-YYYY-NNN (e.g., DEC-2026-001) |
| **Date** | When the decision was made |
| **Decision** | What was decided, in one sentence |
| **Rationale** | Why this decision was made |
| **Alternatives Considered** | What other options were evaluated and why they were rejected |
| **Risk Created** | What risk does this decision introduce? |
| **Documents Affected** | Which CERG documents were changed, deferred, or retired as a result? |
| **Approver** | Who approved this decision? |
| **Review Date** | When should this decision be re-evaluated? (Or "Permanent unless conditions change") |

### Example Decisions

**Example 1: Deferring a regulatory package**

| Field | Value |
|-------|-------|
| Decision ID | DEC-2026-001 |
| Date | 2026-06-15 |
| Decision | Defer adoption of the ISO/IEC 27001 Operational Package (PLN-ISO-001). The organization is not pursuing ISO 27001 certification. |
| Rationale | ISO 27001 certification is not a business requirement. The control baseline (CB-001) already maps to ISO controls for internal reference. |
| Alternatives Considered | (1) Adopt package anyway as best practice — rejected because it creates evidence obligations with no business driver. (2) Remove from repo — rejected because future business needs may change. |
| Risk Created | If the organization later pursues ISO 27001, the deferred package will need to be adopted and backfilled with evidence. |
| Documents Affected | CAT-001 §7 (mark PLN-ISO-001 as Deferred). IMP-001 organization profile. |
| Approver | CISO |
| Review Date | Annual, or upon business direction to pursue ISO 27001 |

**Example 2: Consolidating roles for a small team**

| Field | Value |
|-------|-------|
| Decision ID | DEC-2026-002 |
| Date | 2026-06-15 |
| Decision | Consolidate Governance Pillar Leader, Risk Register Owner, and Evidence Librarian into one person. |
| Rationale | 5-person security team. Cannot staff three separate governance roles. Workload assessment confirms one person can perform all three functions at current organizational scale. |
| Alternatives Considered | (1) Leave roles unfilled — rejected because register and evidence functions are critical. (2) Outsource evidence management — rejected due to cost. |
| Risk Created | Self-review risk: the same person manages the risk register and the evidence that supports risk decisions. Mitigated by CISO review and independent Business Owner / Executive Sponsor acknowledgement for risk acceptance decisions. |
| Documents Affected | OM-001 §6.1 role roster (annotated). RAC-001 accountability assignments (annotated). Per-role files for consolidated roles. |
| Approver | CISO |
| Review Date | Semi-annual; escalate if team grows beyond 8 people |

**Example 3: Calibrating risk appetite**

| Field | Value |
|-------|-------|
| Decision ID | DEC-2026-003 |
| Date | 2026-07-01 |
| Decision | Set single-risk ALE threshold at $500K based on annual revenue of $50M and cyber insurance retention of $250K. |
| Rationale | Board requested a materiality threshold aligned to financial reporting. Finance confirmed $500K as the threshold above which a single cyber event would be material to quarterly earnings. |
| Alternatives Considered | (1) Keep the uncalibrated $2M default - rejected as not calibrated to organization. (2) Set at $250K (insurance retention) - rejected as too conservative for a non-regulated entity. |
| Risk Created | Risks between $250K-$500K ALE will be accepted below the materiality threshold. Mitigated by quarterly review of all accepted High risks. |
| Documents Affected | RMF-001 §9.5 (risk appetite values). MTR-001 board reporting thresholds. |
| Approver | CISO with CFO concurrence |
| Review Date | Annual, or upon material change in revenue or insurance coverage |

---

## 5. Risk Acceptance Guardrails

Risk acceptance is a legitimate risk treatment strategy. It is not a way to make findings disappear. These guardrails prevent acceptance from becoming a paperwork exercise.

### Expiration Defaults

Every risk acceptance must have an expiration date. The defaults below apply unless a specific business justification supports a different duration:

| Risk Severity | Default Expiration | Approver | Renewal Rule |
|---------------|-------------------|----------|--------------|
| **Critical** | 30 days | CISO + Executive Sponsor | Cannot be renewed without material change in treatment plan |
| **High** | 90 days | CISO | Renewal requires documented progress toward remediation |
| **Medium** | 180 days | Pillar Leader or Governance Pillar Leader | Renewal requires confirmation that conditions have not worsened |
| **Low** | 365 days | Risk Register Owner | Annual review at minimum |

**Hard rules:**

- No acceptance is permanent. Every acceptance expires and requires re-approval.
- An acceptance renewed more than twice without movement on the treatment plan escalates one approval tier.
- An expired acceptance with no renewal creates a Finding Record (severity: High).
- The business owner must sign the acceptance. Security cannot accept risk on behalf of the business.
- Acceptance records must document: the risk scenario, the rationale for acceptance over treatment, the compensating controls in place (if any), the residual risk, the expiration date, and the named approver.

**Small-team separation rule:** role consolidation does not collapse business consequence acceptance into the security assessor. If the same person performs CISO, Risk, and Governance work in CERG Lite, an independent Business Owner or Executive Sponsor must still acknowledge the business consequence for accepted risk. If no independent business approver exists, CERG may be used as planning guidance but should not be declared authoritative for risk acceptance.

### Risk Acceptance Is Not Remediation

A risk acceptance:
- Records ownership and accountability
- Documents the rationale for not treating the risk
- Requires compensating controls where applicable
- Sets an expiration and review cadence
- Records residual risk

A risk acceptance does NOT:
- Make the finding disappear from the risk register
- Reset the remediation SLA without documented approval
- Transfer accountability from the business owner to security
- Satisfy a regulatory requirement by itself
- Excuse the organization from monitoring the risk

**If an accepted risk materializes** (exploit published, KEV listed, incident occurs), the acceptance is automatically reopened for re-assessment per RMF-001 §9.10.

---

## 6. Regulatory Honesty

CERG references NERC-CIP, CMMC, SOX, ISO 27001, and privacy regulations. These references are for integration mapping — they do not constitute compliance claims.

### General Rule

> **CERG documents do not equal regulatory compliance.** An organization may adopt every CERG artifact and still fail a regulatory assessment if controls are not implemented, evidenced, and tested against the specific regulatory requirement.

### Do Not Accidentally Claim

For each regulatory framework referenced in CERG:

- **Do not** claim compliance because CERG documents exist.
- **Do not** claim a control is implemented without evidence.
- **Do not** claim an inherited control (cloud/SaaS) without provider evidence and your own complementary controls.
- **Do not** treat a generic policy as a procedure that satisfies a prescriptive regulatory requirement.
- **Do not** treat risk acceptance as a regulatory waiver unless the regulator has explicitly accepted it.
- **Do not** treat a POA&M item as evidence that a control is operating.
- **Do not** treat a compensating control as equivalent to the required control without documented analysis.

### CMMC-Specific Realism

For organizations pursuing CMMC:

- CERG's SSP template and POA&M template are starting points. The SSP must be system-specific — describing your actual system boundary, your actual data flows, and your actual control implementation.
- POA&M acceptability has limits. Assessors evaluate whether POA&M items are credible, resourced, and scheduled. A POA&M with no owner and no due date is not acceptable under any framework.
- Evidence must prove practices are *performed*, not just *documented*. A policy that says "we do access reviews" is not evidence that you did one.
- CUI flow mapping is mandatory. You cannot scope CMMC without knowing where CUI enters, resides, and leaves your environment.
- External Service Providers (ESPs) affect your scope. If a cloud provider or MSP handles CUI, their CMMC status and your shared responsibility matrix are assessment inputs.

### NERC-CIP-Specific Caution

For registered entities subject to NERC-CIP:

- CERG is not a substitute for a registered entity's compliance determination. BES Cyber System classification must be entity-specific and performed by qualified personnel.
- CIP evidence must be retained per the applicable CIP standard's retention requirements — which may exceed CERG's general evidence retention guidance.
- Deviations from CIP requirements need formal handling per the applicable CIP standard, not just a CERG exception record. The CIP deviation process is a separate regulatory obligation.
- OT scanning must be operationally approved. Vulnerability scanning in OT environments can disrupt operations, trigger safety systems, or violate maintenance windows. CERG's exposure management procedure is written for IT environments; OT scanning requires additional controls.
- EACMS, PACS, and BCSI are CIP-specific asset classifications. Do not map these to CERG asset types without understanding the CIP definitions and scoping rules.

### SOX-Specific Caution

For organizations subject to SOX:

- ITGC control evidence must support the financial reporting control objectives. CERG's general control evidence may need to be supplemented with control-specific test results.
- Compensating ITGC controls must be documented and tested. A compensating control that is not tested is not a compensating control for SOX purposes.
- Internal Audit and the CFO designee must be notified of ITGC control gaps per PRC-RM-001 §7.4.

---

## 7. Role Safety for Small Teams

Small teams must consolidate roles — the scaling map in RAC-001 §8 defines how. But some consolidations create unacceptable conflicts. This section defines which combinations are safe and which require compensating controls.

### Usually Safe Consolidations

These role pairs can be performed by the same person with manageable conflict risk:

| Role A | Role B | Why It Is Usually Safe |
|--------|--------|------------------------|
| Policy & Standards Manager | Evidence Librarian | Policy work and evidence management are complementary, not conflicting |
| Exposure Management Lead | Threat Intelligence Analyst | Both are assessment functions; neither approves its own findings |
| Cloud Security Engineer | Identity Engineer | Different technical domains; cloud and identity controls are separable |
| Endpoint Engineer | Cryptography Engineer | Different technical domains; endpoint and crypto controls are separable |
| NERC-CIP Compliance Manager | CMMC/Federal Compliance Manager | Both are compliance assessment roles; different frameworks, same skillset |

### Risky Consolidations — Require Compensating Controls

These consolidations create conflicts that must be explicitly mitigated. If you must combine these roles, document the compensating control in the Decision Log:

| Role A | Role B | Conflict | Compensating Control |
|--------|--------|----------|---------------------|
| Risk Assessor (any Risk role) | Risk Acceptor (CISO) | Same person assesses and accepts the risk — no independent challenge | Require executive sponsor review for all High/Critical acceptances |
| Evidence Producer (Engineering) | Evidence Tester (Governance) | Same person produces and validates evidence — self-review | Require independent sampling of evidence by a different pillar |
| System Owner (Business) | Exception Approver (Governance) | Same person requests and approves the exception — no independent check | Require CISO approval for exceptions affecting systems the approver owns |
| Change Implementer (Engineering) | Change Approver (Governance) | Same person implements and approves the change — no segregation | Require peer review for changes affecting security controls |
| Vendor Sponsor (Business) | Vendor Risk Approver (Risk) | Same person sponsors and approves the vendor — conflict of interest | Require independent vendor risk assessment for high-risk vendors |
| Incident Commander (IR) | Post-Incident Corrective Action Validator | Same person runs the incident and validates the fix — self-review | Require post-incident review by a different pillar |

### Never Combine

These combinations create unacceptable risk under any circumstances. If your team is too small to separate these, the function must be outsourced, performed by a different department, or explicitly deferred with executive acknowledgement:

- **Risk assessor AND sole risk acceptor for the same risk** — requires at minimum an independent reviewer outside the security team.
- **Evidence producer AND evidence tester for the same control** — evidence must be independently validated.
- **Exception requester AND exception approver for the same exception** — approval must come from a different person.
- **Incident Commander AND post-incident lessons-learned approver for the same incident** — lessons learned require independent review.
- **Security operating the service AND asserting its independent effectiveness.** Where CERG or Security operates a service, it is first line for that scope: the independent technical-effectiveness claim is suspended until a named independent assessor verifies the outcome ([`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) §3.1). A team that cannot name an independent assessor cannot make that claim. State this boundary when you adopt, rather than discover it after the first assurance review.

### Minimum Separation of Duties

For each process, these functions must be performed by different people unless otherwise documented:

| Process | Requester | Assessor | Approver | Implementer | Validator |
|---------|-----------|----------|----------|-------------|-----------|
| Risk Acceptance | Any | Risk Pillar | CISO / Executive Sponsor | Engineering | Risk Pillar |
| Security Exception | Any | Risk Pillar | Governance Pillar Leader | Engineering | Risk Pillar |
| Access Approval | User/Manager | Identity Engineer | System Owner | Identity Engineer | Access Reviewer |
| Privileged Access | User/Manager | Identity Engineer | System Owner | Identity Engineer | PAM Audit |
| Firewall/Network Change | Requester | Engineering | Engineering Pillar Leader | Engineering | Risk |
| Production Release | Engineering | Engineering Pillar Leader | Change Advisory Board | Engineering | Operations |
| Vendor Approval | Business Owner | Vendor Risk Analyst | Governance Pillar Leader | Procurement | Vendor Risk Analyst |
| POA&M Closure | System Owner | Compliance Manager | Governance Pillar Leader | Engineering | Risk or Auditor |
| Control Evidence Testing | Evidence Librarian | Control Owner | Governance Pillar Leader | N/A | Independent Tester |

---

## 8. Safe vs. Dangerous Changes

When you tailor CERG, some changes are safe. Some are dangerous. This section defines the boundary.

### Safe to Change

You can (and should) change these without compromising the framework's integrity:

- **Organization name and branding** — use your organization's name, internal program label, and house style while preserving CERG document IDs where cross-references depend on them
- **Role assignments** — assign canonical roles to actual people or job titles
- **Tool names** — replace generic references with your actual tools
- **Regulatory scope** — adopt only the regulatory packages that apply; defer or remove the rest
- **Meeting cadences** — adjust schedules within the bounds defined by review cycles
- **Dollar thresholds** — calibrate risk appetite values to your organization's finances
- **Evidence repository locations** — specify where your evidence is actually stored
- **Illustrative examples and staffing profiles** — replace sector-specific examples and headcount assumptions with your actual operating context
- **Asset classification tiers** — define tiers that match your business criticality

### Dangerous to Change

Changing these breaks the operating model. If you must change them, document the deviation in the Decision Log and accept the resulting risk:

- **Risk acceptance approval separation** — do not allow the same person to assess and accept the same risk
- **Evidence requirements** — do not eliminate evidence requirements for implemented controls
- **Exception expiration** — do not make exceptions permanent or silently renewable
- **Role accountability** — do not delete canonical roles; consolidate them onto fewer people but keep the accountability assignment visible
- **Control status definitions** — do not redefine "Implemented" to mean "we have a policy"
- **Regulatory obligations** — do not remove regulatory requirements that actually apply to you
- **Asset inventory requirement** — do not skip asset registration; you cannot protect what you do not know you have
- **Risk register review cadence** — do not skip scheduled reviews; a stale register is worse than no register
- **Canonical role names** — do not rename roles; the name is the identifier that connects RACI assignments, procedures, and training
- **Document ID format** — do not change the ID scheme; it is the cross-reference backbone

---

## 9. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-IMP-002 |
| **Version** | 1.5 |
| **Status** | Approved |
| **Effective Date** | 2026-06-11 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual |
| **Next Scheduled Review** | 2027-06-11 |
| **Frameworks** | NIST CSF 2.0 |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG adopters |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.5 | 2026-10-30 | Governance Pillar Leader | Authority reconciliation (#280): states the adoption fit boundary for an organization where CERG or Security operates the service. It is first line for that scope, so the independent technical-effectiveness claim is suspended until a named independent assessor verifies the outcome, per OM-001 §3.1. The boundary is stated at adoption rather than discovered later. No new role, record, or decision right. |
| 1.4 | 2026-06-24 | Governance Pillar Leader | Linked the Adoption Safety Guide to the central Anti-Pattern Catalog for cross-domain failure-mode reference. |
| 1.3 | 2026-06-24 | Governance Pillar Leader | Added tool-versus-capability adoption anti-pattern and evidence test for capability claims. |
| 1.2 | 2026-06-24 | Governance Pillar Leader | Removed older example-specific language for utility branding, fixed hard-coded role and headcount examples, and updated adversarial-validation terminology. |
| 1.1 | 2026-06-18 | Governance Pillar Leader | Added explicit small-team separation rule for business-risk consequence acceptance when security roles are consolidated. |
| 1.0 | 2026-06-11 | Governance Pillar Leader | Initial release. Adoption pre-requisites, anti-patterns, decision log template, risk acceptance guardrails, regulatory honesty guidance, role collision guide, and safe/dangerous tailoring boundaries. |

### Review Triggers

- Adoption feedback identifying a new failure pattern
- Change to the role roster in OM-001 §6.1
- Change to regulatory requirements affecting any framework CERG references
- Direction from the CISO

Governance owns this document. The Governance Pillar Leader is responsible for initiating reviews, managing the revision cycle, and obtaining approval for all changes.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| Implementation and Adaptation Guide | [`CERG-GOV-IMP-001`](CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) | How to adapt CERG; this document defines the safety rules for doing so |
| Anti-Pattern Catalog | [`CERG-GOV-ANTI-001`](CERG-GOV-ANTI-001_CERG_Anti_Pattern_Catalog.md) | Cross-domain catalog of adoption, workforce, capability, evidence, and compliance failure modes |
| Operating Model | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) | Canonical role roster and scaling map |
| Risk Management Framework | [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) | Risk acceptance authority and expiration |
| Consolidated Roles and RACI | [`CERG-GOV-RAC-001`](CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) | Role accountability and separation of duties |
| Cross-Pillar Operational Flows | [`CERG-GOV-FLOW-001`](CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md) | Timeout-bypass principle and escalation paths |
