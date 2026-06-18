| | |
|---|---|
| **Document ID** | CERG-GOV-ADR-006 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Review Cycle** | Annual |
| **Frameworks** | N/A (reference record) |
| **Regulations** | Cross-cutting |
| **Environments** | All CERG-managed documentation |

# ADR-006: Inheritance Evidence Package

| Field | Value |
|-------|-------|
| **Status** | Approved |
| **Date** | 2026-06-17 |
| **Author** | CERG Architecture |
| **Approvers** | CISO |

## Context

Cloud and SaaS adoption means many controls are inherited from providers. Without an inheritance evidence standard, "Inherited" becomes a black-box status that auditors reject. Options included: trust provider attestation as-is, require customer-side evidence only, require full provider audit report analysis, and define a six-element inheritance evidence package.

## Decision

Adopt a six-element Inheritance Evidence Package (CB-001 §5) for any control marked Inherited:

1. Provider attestation (SOC 2, ISO 27001, FedRAMP, PCI)
2. Shared responsibility mapping naming this control as the provider's
3. Customer-side evidence of configuration
4. Sub-service organization carve-outs
5. Currency check (attestation expiry + refresh calendar entry)
6. Re-papering trigger (what causes re-evaluation)

Without this package, the default status is Not Implemented and a finding is opened.

## Consequences

- **Positive:** Auditors accept "Inherited" status because the evidence package provides the same confidence as a directly implemented control.
- **Positive:** The package works for all provider types (IaaS, PaaS, SaaS, managed service, parent enterprise).
- **Trade-off:** The package requires periodic work (attestation expiry tracking, customer-side config checks). The re-papering trigger automates evaluation.
- **Risk:** Sub-service dependencies (e.g., AWS underlying Snowflake) are not captured in standard SOC reports. Mitigated by element 4 (sub-service carve-outs).
