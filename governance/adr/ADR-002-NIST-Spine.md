| | |
|---|---|
| **Document ID** | CERG-GOV-ADR-002 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Review Cycle** | Annual |
| **Frameworks** | N/A (reference record) |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed documentation |

# ADR-002: NIST 800-53 as Control Spine

| Field | Value |
|-------|-------|
| **Status** | Approved |
| **Date** | 2026-06-17 |
| **Author** | CERG Architecture |
| **Approvers** | CISO |

## Context

CERG needed a control framework that serves as the organizing structure for the Unified Control Baseline (CB-001). Candidates included: CIS Controls v8 (operational but narrow), NIST CSF 2.0 (strategic, not control-level), ISO/IEC 27001 (annex-based, not a full control catalog), NIST 800-53r5 (comprehensive, framework-agnostic), and a custom CERG-native taxonomy.

## Decision

Adopt NIST 800-53r5 control families as the organizing structure for CB-001. NIST 800-53r5 was chosen because: (1) it is the most widely cross-referenced control catalog in regulatory frameworks, (2) it maps to CSF 2.0, CIS, ISO, CMMC, and NERC-CIP via existing crosswalks, (3) its family structure (AC, AU, AT, etc.) is stable across revisions, and (4) it is the spine NERC-CIP audit teams already use.

CERG-native controls are layered onto the NIST spine, never the reverse. When a NIST family fully covers an intent, CERG inherits the NIST language and identifier.

## Consequences

- **Positive:** One baseline serves multiple regulatory audiences (NERC-CIP, CMMC, SOX, ISO). Crosswalks in CB-001 §10 translate the same evidence into each regulator's language.
- **Positive:** NIST revision history provides a stable change mechanism. CERG versioning follows NIST release cadence for the spine.
- **Risk:** NIST 800-53 may not cover OT-specific, AI-specific, or cloud-native controls natively. Mitigated by overlay layers in CB-001 §8 (OT overlay, AI overlay, cloud overlay).
- **Trade-off:** The NIST catalog is large (~400 controls). CERG selects a subset as the organizational baseline. The full catalog is available for regulated overlay scope.
