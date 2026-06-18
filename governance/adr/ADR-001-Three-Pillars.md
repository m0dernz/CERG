| | |
|---|---|
| **Document ID** | CERG-GOV-ADR-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Review Cycle** | Annual |
| **Frameworks** | N/A (reference record) |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed documentation |

# ADR-001: Three-Pillar Operating Model

| Field | Value |
|-------|-------|
| **Status** | Approved |
| **Date** | 2026-06-17 |
| **Author** | CERG Architecture |
| **Approvers** | CISO |

## Context

CERG needed an organizational structure for the cybersecurity program that separates accountabilities cleanly enough for audit, small-team role consolidation, and cross-functional workflows. Alternatives included: a single security team (flat), a detect-respond-prevent triage model, a CIP compliance-driven structure, and a full risk-and-control matrix organization.

## Decision

Adopt three pillars — Cyber Engineering, Cyber Risk, and Cyber Governance — as the canonical operating model. Each pillar has a named leader with defined decision rights in FLOW-001 and distinct accountability for specific RMF phases (RMF-001 §2.1). The pillars are not departments; they are accountability sets that may be consolidated in small teams.

## Consequences

- **Positive:** Clear audit lines. Each control in CB-001 has exactly one accountable pillar. Small teams (IMP-003) can consolidate roles without changing the accountability model.
- **Positive:** The three-pillar model maps naturally to the RMF lifecycle (RMF-001) and the seven cross-pillar flows (FLOW-001).
- **Risk:** Teams may interpret pillars as departments and create organizational silos. Mitigated by cross-pillar rotation (OM-001 §6.5) and flow-level handoff definitions in FLOW-001.
- **Risk:** Very small teams (1-2 people) cannot staff three pillars safely. Mitigated: IMP-003 §4 defines safe consolidation rules and compensating controls.
