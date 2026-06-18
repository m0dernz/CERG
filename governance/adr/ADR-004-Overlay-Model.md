| | |
|---|---|
| **Document ID** | CERG-GOV-ADR-004 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Review Cycle** | Annual |
| **Frameworks** | N/A (reference record) |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed documentation |

# ADR-004: Overlay Control Model

| Field | Value |
|-------|-------|
| **Status** | Approved |
| **Date** | 2026-06-17 |
| **Author** | CERG Architecture |
| **Approvers** | CISO |

## Context

CERG serves multiple environments (IT, OT, Cloud, CUI) and regulatory regimes (NERC-CIP, CMMC, SOX) within a single organization. A single flat control baseline would either be too broad (everyone gets OT controls) or require multiple parallel baselines. Alternatives included: flat baseline (all controls for all assets), per-regulator separate baselines, inheritance-only model, and overlay model.

## Decision

Adopt an overlay model: one organizational baseline (CB-001 §6) applies to all assets. Environment- or regulation-specific additions and tightening are applied as overlays (CB-001 §8). Overlays are additive or tightening-only — they never remove baseline controls. Where an overlay conflicts with a baseline requirement, the stricter applies and is documented in the overlay matrix.

## Consequences

- **Positive:** Single control inventory. One "Implemented" finding satisfies all applicable overlays.
- **Positive:** Adding a new regulatory regime creates an overlay, not a fork of the baseline.
- **Risk:** Overlay stacking (e.g., NERC-CIP + CMMC + SOX on the same asset) creates cumulative control requirements that may be impractical. Mitigated by CB-001 §8.1 stacking guidance and RMF-001 §9.7 risk acceptance path for impossible control combinations.
- **Risk:** Teams may apply overlays without assessing the compliance delta. Mitigated: overlay application is a documented decision in the Adoption Decision Tree (IMP-005).
