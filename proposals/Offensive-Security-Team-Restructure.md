# Offensive Security Team Restructure

> **Type:** Change proposal / RFC
>
> **Status:** Draft - seeking maintainer feedback
>
> **Author:** Mason (GitHub: Cytax65)
>
> **Affected pillar:** Risk
>
> **Primary documents:** `CERG-PRC-AV-001`, `CERG-PRC-TM-001`, `CERG-GOV-FRM-001`, `CERG-GOV-JD-RISKOPS-002`, `CERG-GOV-RAC-001`, `CERG-GOV-CAT-001`, and `cerg-org-profile.yml`
>
> **Nature:** Workforce and operating-model adaptation; two targeted procedure clarifications

## 1. Decision Requested

Establish a standing, in-house Offensive Security function within the Risk pillar. The function combines penetration testing, red-team operations, purple-team validation, and OT-safe adversarial assessment under one operating cadence.

This RFC separates two decisions that should not be conflated:

1. **The local operating model:** establish and staff a nine-person team for this organization's grid and OT-heavy demand.
2. **Potential framework improvements:** make the capability boundaries, engagement handoffs, OT safety conditions, and scaling choices explicit enough for another organization to adapt.

The proposed local establishment is not a prescribed CERG headcount or a claim that every organization needs an Offensive Security team.

## 2. Problem Statement

Offensive work is currently split across a four-person penetration-testing group, a two-to-three-person red team, and contractors who perform much of the hands-on execution. That structure fragments the testing calendar, makes ownership of retests and purple-team follow-through unclear, and leaves uncommon OT specialties dependent on informal vendor relationships.

The intended change is not to merge Exposure Management and adversarial work. Exposure Management continues to own observation, validation, prioritization, treatment tracking, and remediation coordination. Offensive Security tests whether relevant controls, detections, and response paths hold against authorized adversary behavior.

## 3. Offensive Security Capability Charter

### 3.1 Mission

The team produces decision-ready evidence about whether important attack paths are possible, detected, contained, and corrected. It is not a vulnerability-scanning team, an incident command function, or the owner of first-line remediation.

### 3.2 Services and Deliverables

| Service | What the team does | Required output | Primary handoff |
|---|---|---|---|
| Penetration testing | Tests authorized network, application, cloud, identity, or internal attack paths within an approved scope. | Engagement report, reproducible findings, evidence, severity rationale, remediation guidance, and retest plan. | System owner; Engineering; Exposure Management or Risk Register as applicable. |
| Red-team exercise | Runs a time-bound, objective-driven adversary simulation against a defined business or technical objective. | Charter, Rules of Engagement (RoE), exercise narrative, evidence, control and detection observations, and executive debrief. | CISO, system/business owner, Detection Engineering, and Engineering. |
| Purple-team validation | Emulates selected techniques with Detection Engineering to determine whether telemetry, analytic logic, routing, and response work. | Validation record with technique, data-source condition, outcome, tuning action, owner, and retest date. | Detection Engineer and the detection backlog. |
| OT adversarial assessment | Assesses authorized IT-to-OT paths, boundary controls, remote access, monitoring, or a lab/digital twin without compromising safety. | OT-specific RoE, safety plan, assessment record, findings, and operations debrief. | OT system owner, OT Security Engineer, OT Safety Officer, and Risk Register where material. |
| Threat-model adversary perspective | Contributes abuse cases, attack-path assumptions, and testability criteria during architecture review. | Threat-model inputs and a testable validation hypothesis; it does not replace architecture facts or the project decision record. | Threat-model record and Architecture Review action log. |
| External-test coordination | Scopes, qualifies, supervises, and accepts specialist external testing where internal capability is not appropriate. | Supplier due diligence, RoE, deliverable acceptance record, and finding-routing evidence. | Vendor Risk, system owner, and the relevant first-line team. |

### 3.3 Explicit Boundaries

| The team does | The team does not do |
|---|---|
| Independently validate control behavior through authorized testing. | Own the vulnerable system, implement production changes, or accept residual risk for the first line. |
| Produce evidence that can change a control, detection, risk, or improvement decision. | Replace continuous scanning, exposure prioritization, or routine remediation tracking. |
| Escalate a real or suspected incident under the RoE. | Command an incident, operate notification clocks, or replace the standing Incident Response team. |
| Bring adversary perspective into threat modeling. | Unilaterally define the system architecture, data classification, business tolerance, or go-live decision. |

## 4. Engagement Lifecycle

Every service follows the same control loop. The depth varies by engagement, but the decision points do not disappear for lower-risk work.

### 4.1 Plan and Authorize

Before execution, name the business objective and affected systems; set the scope, dates, test methods, stop conditions, data-handling rules, contacts, and authority to act; and record an RoE approved by the appropriate system or business owner.

An engagement cannot start merely because a security team wants to test. The system owner supplies first-line authorization and operational context. OT, red-team, and cloud-control-plane work receive the higher approvals already required by the Adversarial Validation Procedure.

### 4.2 Prepare Safely

The test lead confirms that accounts, test infrastructure, logging contacts, emergency contacts, and evidence handling are ready. The team validates that the scope is current and pauses if a material change, operational event, or safety condition makes the original authorization unsafe.

### 4.3 Execute and Observe

Testing stays inside the RoE. The team records material actions and evidence needed to reproduce a finding or explain a negative result. A suspected real incident, uncontrolled service impact, or safety concern triggers the stop/escalation path in the RoE; the exercise does not continue merely to achieve its objective.

### 4.4 Route Decisions and Findings

The team distinguishes among:

- an asset or software weakness that belongs in the Exposure Management workflow;
- a control or design weakness requiring risk treatment;
- a detection gap requiring a detection-backlog item and, when material, a risk entry;
- an OT concern requiring the OT exposure workflow and operations review; and
- a systemic pattern requiring a program-improvement record.

A report is not closure. Each material finding has an accountable owner, due date, treatment route, and retest condition.

### 4.5 Retest and Improve

The team verifies the fix or compensating control under conditions relevant to the original finding. Repeated patterns feed control-baseline, architecture, detection, procedure, training, or capacity improvements rather than generating a succession of isolated reports.

## 5. Cross-Pillar and First-Line Interfaces

| Party | Accountability in the model |
|---|---|
| System or business owner | Authorizes scope, provides business context and operational constraints, owns first-line treatment, and accepts residual risk only through the established risk process. |
| Offensive Security Team | Plans and executes authorized validation, preserves evidence, explains exploitability and control impact, routes findings, and performs retests. |
| Engineering | Supplies design and environmental context; implements or supports technical treatment; receives actionable design, configuration, and detection feedback. |
| Detection Engineering | Partners during purple validation; owns analytic and telemetry improvements after handoff. |
| Exposure Management | Owns exposure validation, classification, treatment tracking, and associated treatment clocks. It consumes testing evidence but is not replaced by testing. |
| Risk Pillar Leader | Is accountable for capability quality, prioritization, independence, and escalation of material outcomes. |
| Governance | Defines evidence expectations, assures conformance, preserves decision records, and routes systemic improvement. |
| Standing Incident Response Team | Owns incident command and the operational incident record whenever a test uncovers or becomes a real incident. |

## 6. Proposed Team Shape

The proposed local team reports to the Risk Pillar Leader.

| Role | Local level | Primary purpose |
|---|---:|---|
| Team Lead | M1 | People leadership, capacity, delivery health, stakeholder management, and budget input. |
| Senior Advisor Testing Lead | S4 | Technical authority, methodology quality, complex engagement leadership, and coaching. |
| Technical Project Manager | Organization-calibrated | Intake, scheduling, documentation readiness, scoping coordination, and estimate preparation. |
| Principal Penetration Tester (2) | S3 | Leads complex engagements; at least one demonstrates red-team tradecraft. |
| Penetration Tester (2) | S2 | Independently executes the core testing workload and leads defined workstreams. |
| Penetration Tester (2) | S1 | Executes scoped work with supervision; does not perform OT work alone. |

This design intentionally separates people management from the highest technical authority. It also creates an individual-contributor path without implying that every experienced tester must become a manager.

The generic workforce lesson is a scaling pattern, not a demand for new canonical titles. Smaller organizations may keep the responsibilities consolidated in the Adversarial Testing Lead role. Larger organizations may split management, technical authority, coordination, and testing execution when workload and span of control justify it.

## 7. Demand and Capacity Model

The nine-person local establishment is driven by demand, not a generic team ratio. Capacity planning should maintain an engagement ledger that records at least:

- planned and completed tests by service type, system criticality, and environment;
- concurrent engagement windows and their safety constraints;
- scoping, execution, reporting, retest, and stakeholder time separately;
- external-specialist demand and lead time;
- purple-team technique coverage and follow-through workload; and
- unplanned demand from incidents, material changes, or high-risk findings.

A capacity decision should account for the full engagement lifecycle. Counting only active test days understates the work required to plan safely, synthesize evidence, coordinate remediation, and retest effectively.

For this organization, the planning assumption is two concurrent grid/OT tests, or those two tests plus an external web assessment, while sustaining red-team, purple-team, and regulatory testing cycles. The assumption must be recalibrated against actual throughput and quality data at least annually.

## 8. OT and Specialist-Testing Safeguards

Safety overrides any testing objective.

1. Every OT engagement has a named OT Safety Officer with authority to stop work immediately.
2. A Safety Officer may cover simultaneous work only when the work is co-located or occurs in one documented, coordinated operating window; otherwise each engagement requires its own named officer.
3. The RoE records prohibited actions, operational blackout periods, communications paths, safety stop conditions, and the transition path to Incident Response.
4. Junior testers do not perform OT work alone. The team records the qualified lead and operational escort for each OT activity.
5. Niche specialties, such as RF or radio testing, may remain external when the capability is infrequent or safety-critical. The need, qualifications, scope, acceptance criteria, and evidence route are documented before award.
6. The existing vendor-rotation requirement remains the default. When a suitably qualified specialist market is too narrow, the CISO may approve and record a time-bound exception through the existing risk process rather than silently relaxing the rule.

## 9. Threat Modeling Position

The team should be a strong contributor to threat modeling, especially for high-value, internet-facing, AI, or OT systems. It contributes realistic abuse cases, observed attack paths, testability criteria, and threat-emulation insight.

Threat modeling should nevertheless remain a cross-pillar, decision-oriented activity:

- the Risk Pillar Leader remains accountable for the quality of threat-model outputs;
- Offensive Security may facilitate the adversary-perspective portion where it has the relevant expertise;
- Engineering and the project technical lead supply architecture, data-flow, identity, and deployment facts and implement resulting design changes; and
- system owners and the established risk process retain decision and risk-acceptance authority.

This keeps the adversarial perspective strong without converting threat modeling into a disconnected security exercise or obscuring first-line ownership.

## 10. Measures of a Healthy Capability

The team should measure outcomes and quality, not volume of findings or successful exploitation. Candidate measures include:

| Measure | Why it matters |
|---|---|
| Risk-based validation coverage | Shows whether the most important systems and attack paths receive appropriate testing. |
| Finding route and owner completeness | Confirms that testing produces actionable records rather than orphaned reports. |
| Retest completion for material findings | Shows whether remediation is verified rather than assumed. |
| Purple-validation pass rate and follow-through | Measures detection quality and whether tuning work closes the loop. |
| Recurrent finding themes | Identifies control, architecture, or process failures that need systemic correction. |
| Safety exceptions, unplanned impact, and stop events | Makes safety performance visible, especially for OT work. |
| External-specialist dependency and lead time | Tests whether the internal/external capability mix remains appropriate. |

The team should not use raw finding counts as a performance target. A high count can reflect better scope or reporting; a low count can reflect weak testing, narrow scope, or stronger controls.

## 11. Adoption Sequence

1. **Set the charter.** Confirm scope boundaries, first-line authorization, incident interface, and finding routes.
2. **Create the engagement ledger.** Establish demand and capacity data before treating headcount assumptions as permanent.
3. **Pilot the operating loop.** Run one IT/cloud engagement, one purple cycle, and one OT-safe assessment using the common lifecycle.
4. **Calibrate the team shape.** Split management, technical authority, and coordination only where demand and span of control support it.
5. **Formalize specialist coverage.** Document the external-specialist roster, qualification bar, and exception process.
6. **Review annually.** Use throughput, quality, safety, and recurring findings to adjust capacity and the control-improvement agenda.

## 12. Document Implications

### 12.1 Local Adoption Changes

- Record the local team structure, grades, and capacity assumptions in the organization adaptation profile and workforce plan.
- Use the existing Adversarial Validation Procedure for RoE, safety, findings, retests, and the Incident Response interface.
- Maintain the engagement ledger and supporting evidence in the organization's chosen record system.

### 12.2 Potential Upstream Discussion Topics

If a future upstream contribution is desired, propose only framework-neutral changes:

- a scalable pattern for separating testing management and technical authority;
- clearer OT Safety Officer concurrency language;
- explicit handling of niche specialist testing through the existing exception process; and
- a cross-pillar description of Offensive Security's threat-model contribution.

Any upstream proposal should preserve canonical role and record authority, update the applicable catalog and dependent artifacts, regenerate machine-readable outputs, and pass `python3 tools/cerg-validate.py` with zero errors.

## 13. Open Questions

1. Which services are mandatory for the first operating year, and which remain demand-driven?
2. What evidence and quality threshold must be met before an external engagement is accepted as complete?
3. Which OT test types may ever run concurrently, and who approves that concurrency?
4. At what sustained workload, span of control, and quality threshold should the team split the M1 and S4 responsibilities?
5. Which threat-model sessions benefit from Offensive Security facilitation, and when is a Threat Intelligence or Engineering-led session more appropriate?
