## LESSONS LEARNED AND PROGRAM IMPROVEMENT PROCEDURE
### After-Action Intake · Quarterly Aggregation · Improvement Pipeline · Verification · Improvement Register

---

| | |
|---|---|
| **Document ID** | CERG-PRC-LL-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Parent Policy** | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [`CERG-PRC-IR-002`](CERG-PRC-IR-002_Incident_Response_Playbook_Set.md) · [`CERG-PRC-AV-001`](CERG-PRC-AV-001_Adversarial_Validation_Procedure.md) · [`CERG-PRC-AUD-001`](CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md) · [`CERG-PLN-BC-001`](../plans/CERG-PLN-BC-001_Business_Continuity_and_Disaster_Recovery_Plan.md) · [`CERG-PRC-TI-001`](CERG-PRC-TI-001_Threat_Intelligence_Procedure.md) · [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Exposure_Management_Procedure.md) · [`CERG-GOV-MTR-001`](../governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) · [`CERG-GOV-IMPREG-001`](../governance/CERG-GOV-IMPREG-001_Program_Improvement_Register.md) |
| **Review Cycle** | Annual / After each quarterly lessons-aggregation cycle |
| **Frameworks** | [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (ID.IM, GOVERN) · [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) (CA, PM) · ISO/IEC 27001 A.10 |
| **Regulations** | Cross-cutting : applies to all CERG-supported frameworks |
| **Environments** | All CERG-managed processes, controls, and program functions |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Principles](#2-principles)
3. [Intake Sources and Triggers](#3-intake-sources-and-triggers)
4. [Lesson Triage and Classification](#4-lesson-triage-and-classification)
5. [Quarterly Lessons Aggregation](#5-quarterly-lessons-aggregation)
6. [Improvement Action Pipeline](#6-improvement-action-pipeline)
7. [Improvement Register Integration](#7-improvement-register-integration)
8. [Verification and Closure](#8-verification-and-closure)
9. [Roles and Responsibilities](#9-roles-and-responsibilities)
10. [Metrics](#10-metrics)
11. [Document Control](#11-document-control)

---

## 1. Purpose and Scope

The CERG Framework requires lessons learned to drive improvement. The risk register (PRC-RM-001) records specific risks: threats, vulnerabilities, likelihoods, and treatments. It is not designed to track program-level improvements, aggregate cross-cutting patterns, or verify that lessons were absorbed into the program. Those improvements are tracked in the Program Improvement Register (IMPREG-001), with cross-references to the originating risk where applicable.

This procedure defines how CERG collects, analyzes, and converts after-action findings into permanent program improvements. It applies to every CERG process, engagement, and control that generates a post-event review: incidents, penetration tests, red team exercises, audit findings, DR and BC exercises, tabletop exercises, near-miss events, metrics threshold breaches, and external intelligence shifts.

> **The Assessor Test**
>
> An assessor asks "How did last year's pen test change your program?" An organization that answers "We fixed the findings" with no evidence of structural change is operating at Repeatable maturity. An organization that answers "We fixed the findings, identified two systemic weaknesses, amended three standards, and verified the changes worked in this year's test" is operating at Adaptive maturity. This procedure is the machinery that produces the second answer.

---

## 2. Principles

1. **Every significant event produces a lesson.** After every incident, pen test, red team engagement, audit, exercise, and near-miss, a structured after-action artifact is produced. The default is to produce one; omitting one requires a documented rationale.
2. **Lessons are aggregated, not siloed.** A single incident review that stays in the IR team's folder is wasted. Lessons from all sources are collected into a single aggregation point for cross-cutting analysis.
3. **Lessons produce program changes, not just fixes.** The standard pattern : find a vulnerability, fix it, close the ticket : is operational hygiene, not program improvement. Program improvement is: "Why did four of six DMZ servers share the same misconfiguration, and what standard or procedure must change so the next six servers do not repeat it?"
4. **Every improvement is verified.** A change that is not verified to have worked is not complete. The next review cycle checks whether prior improvements had their intended effect.
5. **Improvements are tracked separately from risks.** The risk register tracks risks. The improvement register (CERG-GOV-IMPREG-001) tracks program changes. Conflating them creates noise in both.

---

### 2.1 Definition of a Significant Event

Principle 1 states "Every significant event produces a lesson." A "significant event" is defined as any event that meets one or more of the following criteria:

- Triggers a P1 or P2 incident response per [CERG-PRC-IR-002](CERG-PRC-IR-002_Incident_Response_Playbook_Set.md) Section 3.6
- Results in a Critical or High finding from adversarial validation per [CERG-PRC-AV-001](CERG-PRC-AV-001_Adversarial_Validation_Procedure.md)
- Produces a "Deficient" control rating from an audit or control test per [CERG-PRC-AUD-001](CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md)
- Involves a near-miss that could have resulted in any of the above (e.g., a control that failed silently but was caught before impact)
- Is directed by the CISO to produce a lesson regardless of the above criteria

#### Events Explicitly NOT Significant

The following do not require a lesson artifact unless they reveal systemic findings:

- Routine P3 or P4 incidents with no systemic findings and no new control gap identified
- Standard operational changes with no security impact
- Routine vulnerability remediation within SLA with no program implication
- Standard access reviews, recertifications, or metric reports that pass without exception

---

## 3. Intake Sources and Triggers

The following events trigger a lessons-learned artifact. Each source names the accountable role for producing the artifact and the target SLA for completion.

| Source | Trigger Event | Accountable Role | SLA (from event close) |
|---|---|---|---|
| Post-incident review | Incident closed per PRC-IR-002 | Incident Commander (IR team) or Governance Pillar Leader | 14 calendar days |
| Adversarial validation engagement | Pen test, red-team, cloud, application, OT-safe, or comparable engagement report delivered per PRC-AV-001 | Adversarial Testing Lead | 14 calendar days |
| Purple team exercise | Exercise completed per LM-001 or PRC-AV-001 | Detection Engineer | 14 calendar days |
| Audit finding (internal) | Audit report issued per PRC-AUD-001 | Governance Pillar Leader | 21 calendar days |
| Audit finding (external / regulator) | Final report received | Governance Pillar Leader | 21 calendar days |
| DR / BC exercise | Exercise AAR completed per PLN-BC-001 | Governance Pillar Leader | 14 calendar days |
| Tabletop exercise | Exercise AAR completed per PRC-IR-002 | Governance Pillar Leader | 14 calendar days |
| Near-miss event | Event contained before impact; documented | Risk Pillar Leader | 7 calendar days |
| Metrics threshold breach | Any metric in MTR-001 Section 3 exceeds red threshold for 2 consecutive periods | Metric owner | 7 calendar days |
| External intelligence shift | Threat landscape assessment identifies a material change per PRC-TI-001 | Threat Intelligence Analyst | 7 calendar days |
| CISO-directed review | CISO requests a lessons review | Assigned pillar leader | As directed |

> **Near-Miss Definition**
>
> A near-miss is an event that met detection thresholds but was contained before operational impact. Examples: a phishing campaign that reached user inboxes but was reported before any credential was harvested; an unauthorized lateral movement attempt that was blocked by network segmentation; a configuration change that would have created an exposure window but was caught by pre-production review before reaching production. Near-misses are the cheapest lessons the organization will ever get : the cost of analysis is orders of magnitude below the cost of the incident that did not happen.

### 3.1 Lesson Artifact Format

Every lesson artifact contains, at minimum:

- **Event summary:** what happened, when, scope, severity
- **Root cause:** what allowed the event to occur or nearly occur
- **What worked:** controls or processes that functioned as intended
- **What did not work:** controls or processes that failed, were bypassed, or were absent
- **Systemic assessment:** does this finding indicate a weakness that exists elsewhere? (yes / maybe / no, with rationale)
- **Improvement candidates:** specific, actionable program changes proposed
- **Immediate fixes taken:** what was fixed at the operational level

---

## 4. Lesson Triage and Classification

Each lesson artifact is triaged within 7 days of receipt by the Governance Pillar Leader, who assigns a severity classification.

| Severity | Criteria | Escalation |
|---|---|---|
| **Critical** | Threatens program effectiveness; indicates a control-family-wide weakness; or a finding that, if unaddressed, would cause an assessor to downgrade maturity. | Immediately briefed to CISO. Improvement action approved within 14 days. |
| **High** | A repeated pattern across multiple sources (same root cause found in a pen test, an audit, and an incident); a single-source finding with broad systemic implications. | Routed to quarterly aggregation with CISO visibility. |
| **Medium** | A single-source finding with improvement potential but no immediate cross-pillar impact. | Routed to quarterly aggregation. |
| **Low** | A minor process tweak or documentation clarification. | Owner implements directly; recorded in the improvement register for completeness but not tracked through full aggregation. |

> **Severity Is Not the Same as Incident Severity**
>
> An incident can be Low severity (single user, contained in minutes) but produce a Critical lesson (the root cause reveals a systemic weakness across an entire control family). Conversely, a Critical incident can produce a Low lesson (the controls worked; the root cause was a one-off human error with no systemic implications). Classify the lesson, not the event.

---


### 4.1 Escalation for Overdue Artifacts

SLAs for lesson artifact production and triage are defined in Section 3.1 (artifact production within 7-21 days of event closure) and Section 4 (triage within 7 days of receipt). When these SLAs are missed, the following escalation applies.

#### Escalation Triggers

| **Trigger** | **Action** |
|---|---|
| Lesson artifact not produced within SLA + 3 business days | Governance Pillar Leader notifies the event owner and requests status |
| Lesson artifact not produced within SLA + 10 business days | Governance Pillar Leader escalates to the responsible pillar leader |
| Lesson artifact not produced within SLA + 20 business days | Pillar leader escalates to CISO |
| Triage not completed within SLA + 3 business days | Governance Pillar Leader escalates internally; covered in monthly curation pass |

#### Escalation Ladder

Event Owner → Governance Pillar Leader → Responsible Pillar Leader → CISO

At each level, the responsible party must either (a) produce the artifact, (b) provide a documented rationale for why the event does not require an artifact (per Section 2.1), or (c) commit to a revised production date. Overdue artifacts are reported in the quarterly lessons aggregation summary and tracked as a metric.

#### Tracking

The Governance Pillar Leader maintains a register of overdue artifacts. The count and age of overdue artifacts is reported in the monthly CERG leadership review. More than 3 artifacts overdue at any time triggers a process review.

## 5. Quarterly Lessons Aggregation

Once per quarter, aligned with the CERG leadership review cadence (GOV-CAL-001 Section 5), the Governance Pillar Leader convenes a cross-pillar Lessons Aggregation Review.

### 5.1 Participants

- Governance Pillar Leader (convener, chair)
- Risk Pillar Leader (intelligence, vulnerability, adversarial inputs)
- Engineering Pillar Leader (design, architecture, configuration inputs)
- CISO (for Critical lesson dispositions)

### 5.2 Agenda

1. **Roll call of open lessons:** all lessons from the trailing quarter, grouped by severity
2. **Cross-source pattern analysis:** are the same root causes appearing across incident reviews, pen tests, and audits? This is the primary value of aggregation : patterns invisible to any single source become visible when all sources are analyzed together
3. **Root cause clustering:** group lessons by common root cause. Name the systemic weakness each cluster represents
4. **Improvement backlog ranking:** produce a ranked list of proposed program improvements. Ranking factors: number of source types that produced the pattern, potential impact if unaddressed, effort to implement, alignment with current CISO priorities
5. **Prior-quarter verification:** review improvements that were closed in the prior quarter's aggregation. For each: did the intended effect materialize? (See Section 8)
6. **Output:** a Lessons Aggregation Summary, published within 5 business days, containing: the ranked improvement backlog, prior-quarter verification results, and any Critical lessons that require immediate CISO action

### 5.3 Summary Format

The Lessons Aggregation Summary is a structured document, not meeting minutes. It contains:

- **Period:** QN YYYY
- **Total lessons intake:** count by source, count by severity
- **Pattern clusters identified:** named clusters with the source count and lesson IDs contributing to each
- **Ranked improvement backlog:** top 5-10 proposed improvements with: improvement ID (from IMPREG-001), description, accountable role, target quarter
- **Prior-quarter verification:** for each previously closed improvement: verified effective / partially effective / ineffective, with rationale
- **Escalations:** any Critical lessons not yet dispositioned

---

## 6. Improvement Action Pipeline

A lesson that produces an improvement action follows this pipeline from identification to program integration.

### 6.1 Improvement Action Types

| Type | Description | Example |
|---|---|---|
| Control baseline amendment | A new or modified control in CB-001 | Add a control requiring credential rotation enforcement at provisioning |
| Standard revision | A change to a CERG standard | Amend STD-CFG-001 to specify DMZ TLS configuration requirements |
| Procedure update | A change to an existing procedure | Add a pre-production checklist item to PRC-AR-001 |
| New capability | A new tool, platform, or process that does not currently exist | Deploy secrets scanning in CI/CD pipelines |
| Training gap flag | A knowledge or awareness gap that contributed to the finding | "Engineers were unaware of the new segmentation standard" : routed to Security Awareness team |
| Staffing or budget recommendation | A resource gap identified | "Current VM staffing cannot sustain the SLA with the expanded asset base" |
| Metric or threshold change | A change to MTR-001 metrics or thresholds | Tighten the drift-rate threshold after observing 6 consecutive green months |
| Retirement | Removal of a control, process, or tool that is no longer effective or relevant | Retire a legacy WAF rule set that no longer matches the threat landscape |

### 6.2 Routing

| Improvement Type | Routed To | Approval Authority |
|---|---|---|
| Control baseline amendment | Governance Pillar Leader | CISO |
| Standard revision | Governance Pillar Leader (Policy & Standards Manager) | Governance Pillar Leader |
| Procedure update | Procedure owner (per RAC-001) | Pillar owner |
| New capability | Relevant pillar leader | CISO (if budget required) |
| Training gap flag | Security Awareness team (adjacent program; CERG does not own) | Awareness program lead |
| Staffing or budget recommendation | CISO | CISO / Executive Sponsor |
| Metric or threshold change | Metric owner | Governance Pillar Leader |
| Retirement | Artifact owner | Per catalog authority (CAT-001 Section 4) |

### 6.3 Integration Points

Improvements that affect the control baseline or standards feed into the annual review cycle documented in GOV-CAL-001. Improvements that affect metrics feed into the threshold calibration procedure (MTR-001 Section 3.X). Improvements that require new tooling or staffing are routed to the CISO for the next budget cycle.

---

## 7. Improvement Register Integration

Every improvement action that reaches the "Approved" state in this procedure is recorded in the Program Improvement Register (CERG-GOV-IMPREG-001). The improvement register is the authoritative record of what changed, why, when, by whom, and with what result.

The relationship between this procedure and the improvement register is:

- This procedure defines the intake, triage, aggregation, and pipeline
- The improvement register is the durable record that tracks each improvement through its lifecycle to verified closure
- The risk register (PRC-RM-001) is NOT used for program improvements. When a risk treatment plan requires a program-level change (not just a control implementation or risk acceptance), the change is recorded in the improvement register, not the risk register

> **Risk vs. Improvement: A Bright Line**
>
> A risk register entry: "Vulnerability in SCADA firmware version 4.2 : CVSS 9.1 : treatment: patch within 90 days." This is a risk. It goes in the risk register.
>
> An improvement register entry: "Three of the last four critical vulnerabilities shared the same root cause: firmware versions were not tracked in the CMDB. Proposed improvement: add automated firmware-version discovery to the asset management platform, amend STD-AM-001 to require firmware version as a tracked attribute, and add firmware-age SLA to PRC-VM-001." This is a program improvement. It goes in the improvement register.
>
> The distinguishing question: "Is this a specific risk to a specific asset, or is it a change to how the program operates?" If the latter, it belongs in the improvement register.

---

## 8. Verification and Closure

No improvement is closed without verification. The verification step is not optional and is not deferred.

### 8.1 Verification Methods

| Improvement Type | Verification Method |
|---|---|
| Control baseline amendment | New or modified control is Implemented in CB-001 and evidence exists for one full review cycle |
| Standard revision | Revised standard is published; related procedures updated; compliance check confirms adoption |
| Procedure update | Procedure is executed under the new version at least once; operator confirms it works as intended |
| New capability | Tool deployed, configured, and producing output; operators trained |
| Training gap flag | Confirmation from Awareness team that content was delivered (CERG does not verify training effectiveness : that is the Awareness program's remit) |
| Metric or threshold change | New threshold produces actionable signals for one full reporting quarter |

### 8.2 Verification Cadence

Verification occurs at the quarterly Lessons Aggregation Review (Section 5). Improvements that were marked "Complete" in the prior quarter are verified. The output is one of three dispositions:

- **Effective:** the improvement produced the intended effect. Improvement is closed.
- **Partially effective:** the improvement helped but did not fully resolve the root cause. Improvement remains open with an amended approach.
- **Ineffective:** the improvement did not produce the intended effect. Improvement is re-opened with additional root cause analysis. The original approach is documented as "attempted and ineffective" : the lesson from the failed improvement is itself a lesson.

> **The Verification Honesty Rule**
>
> The program that marks every improvement "Effective" without evidence is performing, not improving. An ineffective improvement is not a failure : it is a data point that sharpens the next attempt. The scar tissue from a failed improvement is worth more than a dozen unverified claims of success. Record the failure honestly and move to the next approach.

### 8.3 Re-Opened Improvements

An improvement marked "Ineffective" or "Partially effective" is re-opened in the improvement register. A new analysis entry is added describing why the original approach failed and what the revised approach will be. The re-opened improvement follows the same pipeline: approval, implementation, verification.

---

## 9. Roles and Responsibilities

| Role | Responsibility |
|---|---|
| **Governance Pillar Leader** | Owns this procedure. Convenes and chairs the quarterly Lessons Aggregation Review. Triage authority for all incoming lesson artifacts. Maintains the improvement register (IMPREG-001). Reports aggregation results to the CISO. |
| **CISO** | Approval authority for Critical lessons and any improvement that requires budget, staffing, or control baseline amendment. Attends quarterly aggregation reviews. |
| **Risk Pillar Leader** | Produces lesson artifacts for vulnerability, adversarial, intelligence, and near-miss sources. Participates in quarterly aggregation. Accountable for improvement actions in the Risk pillar. |
| **Engineering Pillar Leader** | Produces lesson artifacts for architecture, configuration, and design-review sources. Participates in quarterly aggregation. Accountable for improvement actions in the Engineering pillar. |
| **Adversarial Testing Lead** | Produces the post-engagement systemic analysis per PRC-AV-001. Ensures pen test findings are analyzed for root cause patterns, not just remediated individually. |
| **Incident Commander (IR team)** | Produces post-incident lesson artifacts per PRC-IR-002. Governance Pillar Leader coordinates if the standing IR team does not produce them. |
| **Threat Intelligence Analyst** | Produces lesson artifacts for external intelligence shifts. Presents threat landscape changes at quarterly aggregation. |
| **Exposure Management Lead** | Produces lesson artifacts when VM metrics signal a systemic weakness. |
| **Evidence Librarian** | Archives all lesson artifacts, aggregation summaries, and verification records. Ensures auditability of the lessons-learned pipeline. |
| **Policy & Standards Manager** | Receives standard revision actions from the improvement pipeline. Manages the amendment process per the catalog (CAT-001). |

---

## 10. Metrics

The effectiveness of this procedure itself is measured. These metrics are reported to the CISO quarterly alongside the aggregation summary.

| ID | Name | Formula | Source | Refresh | G / A / R |
|---|---|---|---|---|---|
| LL-001 | Lesson Artifact Completeness | % of trigger events that produced a lesson artifact within SLA | Lesson intake log | Quarterly | >= 90% / 75-90% / < 75% |
| LL-002 | Improvement Closure Rate | % of improvements closed (Effective) within 2 quarters of approval | IMPREG-001 | Quarterly | >= 70% / 50-70% / < 50% |
| LL-003 | Verification Pass Rate | % of verified improvements rated Effective | IMPREG-001 | Quarterly | >= 80% / 60-80% / < 60% |
| LL-004 | Cross-Source Pattern Rate | Number of pattern clusters identified in quarterly aggregation that drew from 2+ distinct source types | Aggregation summary | Quarterly | n/a: informational; higher is better |
| LL-005 | Improvement Aging | % of open improvements older than 2 quarters | IMPREG-001 | Quarterly | <= 20% / 21-40% / > 40% |

---


---

## Appendix A: Lesson Artifact Template

The following template captures the 7 required fields for every lesson artifact.

```
LESSON ARTIFACT - LL-YYYY-NNNN

1. SOURCE EVENT
   Event Type: [Incident / Pen Test / Red Team / Audit / Exercise / Near-Miss / Metric Breach / CISO Directed]
   Event ID: [IR-YYYY-NNNN / AV-YYYY-NNNN / AUD-YYYY-NNNN / etc.]
   Event Date: [date event occurred or closed]
   Event Summary: [one paragraph describing what happened]

2. DATE
   Artifact Production Date: [date]
   Produced By: [name, role]

3. SUMMARY
   What Happened: [factual, concise - what was observed, what the finding was, what failed or succeeded]

4. ROOT CAUSE
   Direct Cause: [the immediate technical, procedural, or human factor]
   Systemic Cause: [the underlying standard, process, or control gap that allowed the direct cause]
   Was This Preventable? [Yes / Partially / No - with rationale]

5. IMPROVEMENT RECOMMENDATION
   What Should Change: [specific, actionable recommendation]
   What Standard, Procedure, or Control Is Affected: [document ID(s)]
   Expected Impact: [how the change prevents recurrence]

6. PRIORITY
   Severity: [Critical / High / Medium / Low - per Section 4]
   Urgency: [Immediate / This Quarter / This Year / Opportunistic]

7. OWNER
   Improvement Owner: [name, role - who will drive the change]
   Approver: [name, role - who approves the change]
   Target Completion Date: [date]
```

## Appendix B: Lessons Aggregation Summary Template

```
LESSONS AGGREGATION SUMMARY - LAS-YYYY-QN

PERIOD COVERED
   Quarter: [Q1 / Q2 / Q3 / Q4] [YYYY]
   Date Range: [start] to [end]

SOURCES REVIEWED
   | Source Type | Count Reviewed | Count with Artifacts |
   |---|---|---|
   | Incidents (P1/P2) | | |
   | Pen Tests / Red Teams | | |
   | Audits / Control Tests | | |
   | Exercises (TTX, DR, BC) | | |
   | Near-Miss Events | | |
   | Metric Breaches | | |
   | CISO-Directed | | |

   Total Artifacts Produced This Quarter: [N]
   Overdue Artifacts (from prior periods): [N]

KEY THEMES
   1. [Theme]: [description, frequency, affected controls/standards]
   2. [Theme]: [description, frequency, affected controls/standards]
   ...

IMPROVEMENT ACTIONS RECOMMENDED
   | Action ID | Description | Priority | Owner | Target Date |
   |---|---|---|---|---|
   | | | | | |

ACTIONS APPROVED
   | Action ID | Description | Approved By | Approved Date |
   |---|---|---|---|
   | | | | |

ACTIONS DEFERRED
   | Action ID | Description | Reason for Deferral | Next Review Date |
   |---|---|---|---|
   | | | | |

TREND ANALYSIS (if 4+ quarters available)
   - Artifact production trend: [increasing / stable / decreasing]
   - Top recurring theme: [theme] - appeared in [N] of last [M] quarters
   - Improvement closure rate: [X%] of actions from prior quarter(s) verified closed

Prepared by: [Governance Pillar Leader]
Date: [date]
Reviewed by: [CISO]
```

## 11. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-PRC-LL-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Effective Date** | 2026-05-26 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual / After each quarterly lessons-aggregation cycle |
| **Next Scheduled Review** | 2027-05-26 |
| **Frameworks** | NIST CSF 2.0 (ID.IM, GOVERN); NIST 800-53r5 (CA, PM); ISO/IEC 27001 A.10 |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed processes, controls, and program functions |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 | 2026-05-26 | Cyber Governance | Initial draft. Established the lessons-learned intake, triage, quarterly aggregation, improvement pipeline, verification, and improvement register integration procedure. Addresses NIST CSF Adaptive gap: closing the loop from after-action findings to verified program improvements. |
