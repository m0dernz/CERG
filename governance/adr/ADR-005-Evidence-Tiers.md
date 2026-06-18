# ADR-005: Evidence Tiers (E1/E2/E3)

| Field | Value |
|-------|-------|
| **Status** | Approved |
| **Date** | 2026-06-17 |
| **Author** | CERG Architecture |
| **Approvers** | CISO |

## Context

CERG needed an evidence quality classification that is simple enough for small teams using spreadsheets but rigorous enough for NERC-CIP, CMMC, and SOX audits. Options included: binary (Attested/Not), NIST SP 800-53A depth levels, three-tier qualitative, and a five-tier system with explicit testing methods per type.

## Decision

Adopt three evidence tiers (AUD-001 §4):

- **E1 — Self-Attestation:** A statement by the control owner. Acceptable only for Planned and Not Applicable statuses.
- **E2 — System-Generated:** An automated export, log extract, configuration snapshot, or tool report. The minimum acceptable tier for Implemented controls.
- **E3 — Independent Verification:** A test or observation performed by someone other than the control owner. Required for Critical/High overlay controls.

## Consequences

- **Positive:** Three tiers are teachable in five minutes and map directly to audit expectations (E2 = audit can inspect, E3 = auditor can rely).
- **Positive:** Low barrier to entry: a team using spreadsheets can produce E2 evidence (config exports, log extracts).
- **Trade-off:** E2 encompasses a wide range of evidence quality (from a screenshot to an automated daily attestation pipeline). CB-001 §4.1 refines this per control status.
- **Risk:** Teams may use E1 for Implemented controls. Mitigated by validator rule linking control status to minimum evidence tier (CB-001 §4.1).
