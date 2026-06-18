# ADR-003: FAIR-Aligned Risk Statements

| Field | Value |
|-------|-------|
| **Status** | Approved |
| **Date** | 2026-06-17 |
| **Author** | CERG Architecture |
| **Approvers** | CISO |

## Context

CERG needed a risk statement format that is reproducible, auditable, and maps to quantitative scoring. Options included: ISO 31000 free-text format (flexible but inconsistent), NIST SP 800-30 format (event-based), OCTAVE format (scenario-based), and FAIR (factor-based, quantitative-capable).

## Decision

Adopt FAIR-aligned risk statements using five elements: threat actor, action, asset, effect, and resulting impact. The format is:

> [Threat Actor] could [Action] against [Asset], resulting in [Effect], leading to [Impact].

This is a simplified FAIR approach — it captures the loss-event narrative without requiring full Monte Carlo simulation at every tier. The five elements map to FAIR factors (Loss Event Frequency, Loss Magnitude) without introducing FAIR's full taxonomy overhead.

## Consequences

- **Positive:** Consistent risk statements across the risk register (TMPL-RM-001), threat models (PRC-TM-001), and architecture review findings (PRC-AR-001).
- **Positive:** Five-element format is teachable in 15 minutes and produces audit-defensible records.
- **Trade-off:** Simplified FAIR does not produce numerical ALE or SLE without additional calculation. The risk appetite bands in RMF-001 §9.5 use inherent/residual scoring (Likelihood × Impact on 1-5 scale) for operational triage, reserving full FAIR analysis for High/Critical risks.
- **Risk:** Teams may write incomplete statements omitting one of the five elements. Mitigated by validator rule and template fields in TMPL-RM-001 and TMPL-RM-003.
