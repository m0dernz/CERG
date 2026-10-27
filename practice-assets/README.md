# Practice Assets Operating Guide

The materials in this directory are the cragin-security practice layer: an optional, MSP/MSSP-oriented implementation companion to CERG. They provide delivery patterns, tooling examples, and evidence-collection approaches. They do not replace the CERG operating model, applicable law, a client's technical judgment, or first-line ownership of systems and controls.

## Purpose and Boundary

Use these assets when a consulting practice or internal IT team needs a repeatable way to deliver security outcomes to multiple clients. Treat them as a starting point to tailor, not as a universal tool stack or a claim of compliance.

The boundary is deliberate:

- The CERG framework supplies control intent, decision rights, evidence quality expectations, and the Engineering, Risk, and Governance operating model.
- The practice assets supply a proposed delivery method, optional product examples, and implementer-facing checklists.
- Client system, service, and business owners remain accountable for their systems, operational decisions, and risk acceptance.
- A tool deployment, API export, or completed checklist is not by itself proof that a control is effective.

## Asset Map and Authority

| Need | Primary asset | Authority it provides |
|---|---|---|
| Control statement, applicability, named evidence, and release control IDs | [CB-002 Practitioner Control Baseline](../governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md) | The fork's practitioner control set. It is the source for the current release's control IDs and their detailed statements. |
| Product-selection rationale | [Opinionated Tool Matrix](tools/opinionated-tool-matrix-v1.md) | Product recommendations and their stated selection criteria. These are recommendations, not CERG requirements. |
| Tool deployment and implementer steps | [MSP/MSSP Runbook](msp-runbook-v1.md) | Delivery examples and operational checklists for the selected profile. |
| Evidence collection and integration | [Evidence Automation Mapping](tools/evidence-automation-mapping-v1.md) | Proposed collection routes, review cadence, and manual-evidence fallbacks. |
| GRC configuration | [GRC Rollout Guide](tools/grc-rollout-v1.md) | ServiceNow and Vanta implementation patterns; client configuration remains authoritative. |
| Client engagement and transition | [Engagement Playbook](engagement-playbook-v1.md) | Scoping, delivery, handoff, and commercial-operating guidance. |
| Threat-informed prioritization | [Threat-Intel-Validated Control Baseline](tools/threat-intel-validation-v1.md) | A time-bound analytical view of selected threats and control relationships. |
| Why this fork made a practice choice | [Architecture Decision Records](../governance/CERG-GOV-ADR-001_Architecture_Decision_Records.md) | The rationale and consequences of fork-specific decisions. |

When two assets appear to disagree, do not silently choose the more convenient interpretation. Open a practice-maintenance item, identify the controlling asset in the table above, and update dependent material together.

## Evidence Is Not One Thing

Every evidence mapping should identify which of these claims it supports:

| Evidence type | Question answered | Example | Does not establish by itself |
|---|---|---|---|
| Implementation evidence | Was the guardrail configured or deployed? | An IdP policy export or firewall configuration export. | That the configuration covered the right scope or worked during the period. |
| Operating evidence | Did the guardrail operate for the relevant scope and period? | Timestamped account-review results, backup-job history, or a signed change record. | That an attacker could not bypass the guardrail. |
| Effectiveness evidence | Did the guardrail achieve its security objective under relevant conditions? | A restore test, authorized attack simulation, control test, or adversarial validation result. | That all future conditions are covered. |

The evidence map may automate collection of the first two types. The service owner, Risk function, and applicable CERG procedures determine when effectiveness testing is needed and how results route into treatment or improvement.

## Safe Tailoring Rules

1. **Preserve first-line accountability.** The provider can operate tools or prepare evidence, but the client owner remains accountable for system decisions and treatment of material findings.
2. **Use tools as profiles, not requirements.** A client may select an equivalent product when it meets the stated security objective, integration needs, supportability, and evidence expectations.
3. **Keep tenant and client data isolated.** Multi-client administration, evidence repositories, API credentials, and administrative access require explicit client boundaries and access review.
4. **Do not publish secrets or live client details.** Examples use placeholders. Store credentials, tokens, exports, and customer-specific architecture information in an approved client record system, not in this repository.
5. **Treat regulatory mappings as scoped analysis.** A mapping can help prepare work; it does not establish legal applicability, certification readiness, or assessor acceptance.
6. **Route findings through the operating model.** Vulnerabilities, control weaknesses, detection gaps, and accepted risk use their established records and owners. A consulting report is not the system of record.

## Verification Standard for Product and Integration Claims

Tool, API, pricing, and integration claims change faster than the framework. Before publishing or relying on a claim, record:

- product name, edition, and supported version or service tier;
- vendor documentation URL and the date checked;
- whether the capability was vendor-documented, lab-validated, or client-validated;
- prerequisites, permissions, licensing, and known limitations;
- the exact evidence artifact and collection cadence; and
- an owner and next verification date.

Unsupported or unverified examples should be labeled as illustrative. A deployment command should be tested in a non-production environment before it is reused for a client.

## Release and Maintenance Discipline

The practitioner baseline has many dependent assets. A control change is complete only when the affected implementation, evidence, threat, and engagement materials have been reviewed.

Before releasing a practice-asset update:

1. Use the control headings in CB-002 as the authoritative set of control IDs for the release. Do not rely on a rounded control count in narrative text.
2. Reconcile any control ID, title, evidence, and cadence changed in CB-002 against the runbook, evidence map, threat analysis, GRC guide, and engagement playbook.
3. Check all vendor claims and refresh dates. Threat intelligence must not be presented as current after its stated refresh date.
4. Regenerate affected machine-readable artifacts and run the repository validator and integrity checker.
5. Record material practice decisions in the ADR log, including alternatives and consequences.
6. Reconcile the fork with upstream CERG before carrying forward an upstream document change. Keep fork-specific choices in `practice-assets/` or another clearly marked fork-only location.

## Suggested Client Record Set

Each client engagement should maintain records separate from this repository:

- scope, service ownership, and engagement authorization;
- selected tools, licenses, supported versions, and administrative-boundary design;
- control applicability and inherited-control decisions;
- evidence index and collection schedule;
- open findings, exceptions, risk decisions, and retest results;
- change, incident, and handoff records; and
- current contact, escalation, and renewal information.

The point of the practice layer is repeatable delivery with defensible evidence and clear ownership, not a fixed stack or a one-time compliance exercise.
