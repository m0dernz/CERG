| | |
|---|---|
| **Document ID** | CERG-GOV-IMP-003 |
| **Version** | 1.01 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual |
| **Frameworks** | NIST CSF 2.0 |
| **Regulations** | Cross-cutting |
| **Environments** | Small-team CERG adopters (≤8 people) |

---

## Table of Contents

1. [Who This Is For](#1-who-this-is-for)
2. [The CERG Lite Package](#2-the-cerg-lite-package)
3. [Operating Rhythm for a 5-Person Team](#3-operating-rhythm-for-a-5-person-team)
4. [Role Consolidation Map](#4-role-consolidation-map)
5. [First 10 Records to Create](#5-first-10-records-to-create)
6. [First Month Success Criteria](#6-first-month-success-criteria)
7. [Manual Fallback Schemas](#7-manual-fallback-schemas)
8. [Minimum Viable Evidence Library](#8-minimum-viable-evidence-library)
9. [Document Control](#9-document-control)

---

## 1. Who This Is For

This guide is for teams of 8 people or fewer who want to run CERG as their operating model. It assumes you have read the [Adoption Safety Guide](CERG-GOV-IMP-002_Adoption_Safety_Guide.md) and confirmed the prerequisites in §1.

The full CERG corpus describes what a 60-person security team looks like at NIST CSF Adaptive maturity. That is the upper bound. This guide describes the lower bound — what a 5-person team can actually operate without burning out.

**The rule:** adopt fewer documents, run a lighter cadence, produce simpler evidence, and add complexity only when the team grows or the risk demands it.

---

## 2. The CERG Lite Package

These are the documents you actually need first. Everything else in the repo can wait.

### Adopt Immediately: MVC (8 documents)

| Document | Why |
|----------|-----|
| Cybersecurity Policy (POL-001) | Board/CISO must approve. One page. |
| CERG Framework (FRM-001) | Explains the three-pillar model every other document assumes. |
| Operating Model (OM-001) | Defines your consolidated roles. Read §6.1, skip the 60-person examples. |
| Document Catalog (CAT-001) | Inventory of what exists and what you have adopted. |
| Risk Management Framework (RMF-001) | How you score, treat, and accept risk. |
| Risk Register and Exception Process (PRC-RM-001) | Your operational risk workflow. |
| Risk Register Templates (TMPL-RM-001) | The spreadsheet/template layer that makes the register real. |
| Exposure Management Procedure (PRC-VM-001) | Your operational vulnerability workflow. |

### Use as adoption aids, not additional MVC requirements

| Document | Use |
|----------|-----|
| Implementation Guide (IMP-001) | How to adapt the corpus. Fill in your org profile. |
| Adoption Safety Guide (IMP-002) | How to avoid failure modes. |
| **This document** (IMP-003) | How to run CERG with a small team. |
| Role-Based Implementation Checklists (IMP-006) | What each consolidated role should do first. |
| Job Families Overview (JF-001) | Useful for hiring and consolidation, not required to run MVC. |
| NICE Crosswalk (JF-002) | Optional skills-gap and hiring reference. |

### Adopt When Ready (layered on as the team grows)

| When | Add These |
|------|-----------|
| You are ready to formalize controls | Unified Control Baseline (CB-001); start with the 6 families you can evidence. |
| You have cloud, SaaS, or managed infrastructure | Access, Asset, Configuration, IT/Cloud/SaaS, Logging, and Resilience standards as applicable. |
| You have a compliance requirement | The applicable regulatory package (CIP, CUI, SOX, ISO, Privacy). |
| You are onboarding vendors | Third-Party Risk Procedure (PRC-TPRM-001). |
| You have a detection capability | Threat Intelligence Procedure (PRC-TI-001) and Adversarial Validation Procedure (PRC-AV-001). |
| You have an incident response function | Cross-Pillar Flows (FLOW-001) for F-06 integration; IR remains owned by the standing IR team. |
| Team grows beyond 8 people | Per-role JD documents for hiring; full workforce planning. |

### Do Not Adopt Yet

The following are explicitly deferred for small teams. Document the deferral in your Decision Log:

- Full workforce planning (WFP-001)
- Succession planning (SUCC-001)
- Maturity self-assessment (MAT-001)
- Any regulatory package that does not apply
- Board/CISO reporting deck template — use a simple status report instead
- Per-role JD documents — JF-001 and JF-002 are sufficient
- Contractor integration guide (CON-001) — unless you have contractors
- Stakeholder perception survey (TMPL-GOV-001)

---

## 3. Operating Rhythm for a 5-Person Team

The full calendar (CAL-001) assumes a 60-person team. Scale it down.

### Weekly (1 hour)

| Activity | Who | Duration |
|----------|-----|----------|
| High/Critical risk review | CISO + whoever owns Risk that week | 20 min |
| Vulnerability remediation review | Risk person | 20 min |
| Open exceptions check (any expiring this month?) | Governance person | 10 min |
| New project intake review (any new requests?) | Engineering person | 10 min |

### Biweekly (1 hour)

| Activity | Who | Duration |
|----------|-----|----------|
| Vulnerability SLA review (any past due?) | Risk person | 15 min |
| Change review (any security-significant changes this period?) | Engineering person | 15 min |
| Evidence freshness check (any stale evidence?) | Governance person | 15 min |
| Cross-training check (did anyone do their 4 hours?) | Everyone | 15 min |

### Monthly (2 hours)

| Activity | Who | Duration |
|----------|-----|----------|
| Full risk register review | Everyone | 45 min |
| Exception review (renew, close, escalate) | Governance + Risk | 20 min |
| Vendor risk review (any new vendors? any expiring assessments?) | Risk person | 15 min |
| Metrics collection for monthly report | Governance person | 20 min |
| Improvement backlog review | Everyone | 20 min |

### Quarterly (half day)

| Activity | Who | Duration |
|----------|-----|----------|
| Executive risk brief preparation | CISO | 1 hour |
| Control evidence refresh (pick 2-3 control families) | Governance + Engineering | 1 hour |
| Access review (sample of privileged accounts) | Identity person | 1 hour |
| Policy/standards review (any changes needed?) | Governance | 30 min |
| Lessons learned from incidents or near-misses | Everyone | 30 min |

### Semi-Annual (1 day)

| Activity | Who | Duration |
|----------|-----|----------|
| Full access review | Identity person + system owners | 3 hours |
| Backup restore test (pick 2 critical systems) | Engineering person | 2 hours |
| Tabletop exercise (pick 1 scenario) | Everyone | 2 hours |
| Policy review and update | Governance | 1 hour |

### Annual (2-3 days)

| Activity | Who | Duration |
|----------|-----|----------|
| Full maturity self-assessment (optional for small teams) | Governance | 2 hours |
| Risk appetite calibration | CISO + executive sponsor | 1 hour |
| Full policy/standards review cycle | Governance | 4 hours |
| Annual report to executive leadership | CISO | 2 hours |
| Budget and resource planning | CISO | 2 hours |
| Team training and development planning | Everyone | 1 hour |

---

## 4. Role Consolidation Map

A 5-person team covers all 27 canonical roles by consolidating them. The map below is one example — adapt it to your team's skills. Document your actual assignments in the Decision Log.

| Person | Canonical Roles Consolidated | Primary Family |
|--------|------------------------------|----------------|
| **Person 1 — CISO / Governance Lead** | CISO, Governance Pillar Leader, Policy & Standards Manager, Risk Register Owner, Evidence Librarian | JF-EXEC / JF-GOVCOMP |
| **Person 2 — Risk Lead** | Risk Pillar Leader, Exposure Management Lead, Threat Intelligence Analyst, Detection Engineer, Vendor Risk Analyst | JF-RISKOPS |
| **Person 3 — Engineering Lead** | Engineering Pillar Leader, Cloud Security Engineer, Identity Engineer, Endpoint Engineer | JF-SECENG |
| **Person 4 — Security Engineer** | Application Security Engineer, Cryptography Engineer, OT Security Engineer (if applicable), Pre-production Reviewer | JF-SECENG |
| **Person 5 — Compliance / IR Liaison** | NERC-CIP Compliance Manager, CMMC/Federal Compliance Manager, SOX ITGC Lead, IR liaison (Incident Commander and Lead Investigator remain with standing IR team) | JF-GOVCOMP / JF-ADJUNCT |

**If you have 3 people:** Consolidate further using the map below. This is one example — adapt to your team's skills. Each consolidation concentrates risk; compensating controls are mandatory, not optional.

| Person | Canonical Roles Consolidated | Primary Family | Compensating Controls |
|--------|------------------------------|----------------|-----------------------|
| **Person 1 — CISO / Governance / Risk Register** | CISO, Governance Pillar Leader, Policy & Standards Manager, Risk Register Owner, Evidence Librarian | JF-EXEC / JF-GOVCOMP | Executive Sponsor reviews all High/Critical risk acceptances. Quarterly independent peer review of risk register completeness (external facilitator or adjacent team). No single-person approval for exceptions where Person 1 is the asset owner. |
| **Person 2 — Engineering / Cloud / Identity** | Engineering Pillar Leader, Cloud Security Engineer, Identity Engineer, Endpoint Engineer, Pre-production Reviewer | JF-SECENG | Architecture review disposition requires documented second-opinion check with Person 3. Emergency changes require post-hoc review within 48 hours by Person 1. Pre-production reviewer role rotates quarterly or annually. |
| **Person 3 — Risk / Compliance / VM** | Risk Pillar Leader, Exposure Management Lead, Compliance Manager (NERC, CUI, SOX as applicable), Threat Intelligence Analyst, Vendor Risk Analyst | JF-RISKOPS / JF-GOVCOMP | Compliance findings and exposure backlog cross-checked monthly by Person 1. Vendor risk assessments over a defined threshold (e.g., High/Critical) require joint sign-off with Person 2. |

Document every consolidation in the Decision Log per IMP-002 §4. The Role Collision Guide (IMP-002 §7) defines which consolidations require compensating controls. If any compensating control above conflicts with local policy, escalate to the CISO or equivalent security owner before adopting the consolidation.

**If you have 1 person:** You are not ready to adopt CERG as an operating model. Use CERG as a planning reference. Hire your second person before attempting adoption.

---

## 5. First 10 Records to Create

Before you run your first meeting, create these records. They prove the program is operational, not just documented.

### Record 1: Organization Profile (IMP-001)

Fill in the organization profile in the Implementation Guide. This is a single document, not a recurring record.

- Organization name
- Named CISO
- Named executive sponsor
- Defined system scope
- Known regulatory obligations
- Tooling inventory

### Record 2: Role Assignment Map

A simple table mapping your actual people to canonical roles. Example:

| Person | Canonical Roles | Email |
|--------|----------------|-------|
| Jane Smith | CISO, Governance Pillar Leader | jane@example.com |
| Alex Chen | Risk Pillar Leader, Exposure Management Lead, Threat Intel | alex@example.com |

### Record 3: Asset Inventory Extract

Do not build a full CMDB. Start with a spreadsheet. List every system you know about. If you do not know about it, write "unknown" in the owner column — that is your first finding.

| Asset | Type | Owner | Classification | Criticality | In Scope? |
|-------|------|-------|---------------|-------------|-----------|
| ExampleApp | SaaS | Jane Smith | Internal | High | Yes |

Aim for 80% coverage in month one. The remaining 20% is your asset discovery backlog.

### Record 4: Initial Top 10 Risks

Do not try to build a complete risk register in week one. Identify the 10 risks that keep you up at night. Score them. Assign owners. Schedule treatment.

| Risk ID | Risk Statement | Inherent | Residual | Owner | Treatment | Due |
|---------|---------------|----------|----------|-------|-----------|-----|
| RISK-2026-001 | Unpatched internet-facing systems could enable ransomware | High | Medium | Alex Chen | Remediate — patch cycle | 2026-07-15 |

### Record 5: Exposure Backlog

Export your vulnerability scanner results. Prioritize by severity and asset criticality. Assign the top 20 to owners.

| Finding ID | CVE/ID | Severity | Asset | Owner | Due |
|-----------|--------|----------|-------|-------|-----|
| FIND-2026-001 | CVE-2026-12345 | Critical | ExampleApp | Alex Chen | 2026-06-13 |

### Record 6: Exception Register (starts empty)

Create the structure. It will populate as you find things you cannot fix on schedule.

| Exception ID | Control | Rationale | Compensating Controls | Approver | Expires |
|-------------|---------|-----------|----------------------|----------|---------|

### Record 7: Evidence Index

Create the folder structure (see §8). Add one entry for each piece of evidence you already have.

| Evidence ID | Control | Description | Date | Source | Stored At |
|------------|---------|-------------|------|--------|-----------|

### Record 8: Control Implementation Snapshot

If CB-001 is not yet adopted, start with a preliminary snapshot for the obvious control families (AC, IA, CM, CP, RA, SI) and mark it preliminary. Once CB-001 is adopted, convert the snapshot to CB-001 control IDs and record its current status honestly.

| Control ID | Status | Evidence? | Notes |
|-----------|--------|-----------|-------|
| AC-2 | Partially Implemented | JML log collected | Access review not yet performed |
| IA-2 | Implemented | MFA enforced via IdP policy | Evidence: IdP config export 2026-06-01 |

### Record 9: Regulatory Applicability Decision

For each regulatory framework referenced in CERG, decide: Applicable? Deferred? Not applicable?

| Framework | Applies? | Decision | Rationale |
|-----------|---------|----------|-----------|
| NERC-CIP | No | Not applicable | Not a registered entity |
| CMMC | Yes | Deferred | Will adopt CUI package in Q3 |
| SOX | Yes | Applicable | Public company — ITGC scope defined |

### Record 10: 30-Day Improvement Backlog

Five things you will fix in the first 30 days. Be specific.

| ID | Action | Owner | Due |
|----|--------|-------|-----|
| IMP-001 | Complete asset inventory for cloud environments | Engineering Lead | 2026-07-11 |
| IMP-002 | Run first access review for privileged accounts | Identity person | 2026-07-11 |

---

## 6. First Month Success Criteria

After 30 days of operating CERG with a small team, you should be able to answer "yes" to these questions:

### Governance

- [ ] Policy approved by CISO and executive sponsor
- [ ] Organization profile completed
- [ ] Decision log created with at least: role consolidation decisions, regulatory applicability decisions, deferred document decisions
- [ ] Evidence library structure created with at least one piece of evidence per spine control family
- [ ] Document catalog reviewed — deferred documents noted

### Risk

- [ ] Top 10 risks identified, scored, and assigned to owners
- [ ] First risk register review held — decisions documented
- [ ] Exposure backlog triaged — criticals assigned, highs prioritized
- [ ] Exception process tested — at least one exception created or the register confirmed empty with rationale
- [ ] Vendor list compiled — high-risk vendors flagged for assessment

### Engineering

- [ ] Architecture review process tested — at least one project went through intake
- [ ] Pre-production review conducted for any new systems or major changes
- [ ] Control baseline snapshot completed — honest status for spine controls
- [ ] Asset inventory initiated — 80% coverage target set

### Operations

- [ ] First monthly report produced (can be a simple email, not a deck)
- [ ] Improvement backlog created with at least 5 items
- [ ] Team trained on their consolidated roles and handoffs
- [ ] Cross-training plan initiated — each person identified one skill to develop outside their primary pillar

### If You Cannot Answer Yes

- Do not declare CERG adopted. You are in the planning phase.
- Do not add more documents. Fix the gaps in the spine first.
- Do not skip the risk register review. It is the heartbeat of the program.
- Do not pretend "Partially Implemented" means "Implemented." Honest gaps are better than false claims.

---

## 7. Manual Fallback Schemas

If you do not have a GRC platform, ticketing system, or evidence management tool, use spreadsheets. These schemas define the minimum columns for each record type. Add columns as needed — do not remove the ones listed.

### Risk Register Spreadsheet

| Column | Example | Notes |
|--------|---------|-------|
| Risk ID | RISK-2026-001 | Use the format RISK-YYYY-NNN |
| Risk Statement | Unpatched internet-facing systems... | FAIR-aligned: threat actor, action, asset, effect, impact |
| Inherent Likelihood | 4 | 1-5 scale per RMF-001 |
| Inherent Impact | 4 | 1-5 scale per RMF-001 |
| Inherent Score | 16 | Likelihood × Impact |
| Residual Likelihood | 2 | After treatment |
| Residual Impact | 3 | After treatment |
| Residual Score | 6 | Residual Likelihood × Impact |
| Severity | Medium | Per RMF-001 §9.5 bands |
| Treatment Strategy | Mitigate | Avoid / Mitigate / Transfer / Accept |
| Treatment Plan | Implement WAF by Q3 | Specific, actionable |
| Business Owner | Jane Smith | Must be outside security |
| Risk Owner (Security) | Alex Chen | Security point of contact |
| Date Identified | 2026-06-15 | |
| Treatment Due | 2026-09-15 | |
| Status | In Treatment | New / In Treatment / Accepted / Closed |
| Last Reviewed | 2026-07-01 | |
| Next Review | 2026-08-01 | |

### Exception Register Spreadsheet

| Column | Example | Notes |
|--------|---------|-------|
| Exception ID | EXC-2026-001 | Format EXC-YYYY-NNN |
| Control ID | AC-2 | From CB-001 |
| Requirement | Quarterly access review for all systems | What is not being met |
| Affected Assets | ExampleApp, ExampleDB | |
| Business Justification | Access review tool not yet deployed | Why the exception is needed |
| Compensating Controls | Manual review of privileged accounts monthly | What is in place instead |
| Residual Risk | Medium | |
| Business Owner | Jane Smith | |
| Approver | CISO | |
| Approval Date | 2026-06-15 | |
| Expiration Date | 2026-09-15 | |
| Monitoring Cadence | Monthly | |
| Status | Active | Active / Expired / Closed |

### Evidence Index Spreadsheet

| Column | Example | Notes |
|--------|---------|-------|
| Evidence ID | EVD-2026-001 | Format EVD-YYYY-NNN |
| Control ID | AC-2 | From CB-001 |
| Control Name | Account Management | |
| Evidence Description | JML log export for June 2026 | What the evidence shows |
| Evidence Tier | E2 | E1/E2/E3 per FLOW-001 §16 |
| Source System | Azure AD / HRIS feed | Where the evidence came from |
| Generated Date | 2026-06-30 | When the evidence was produced |
| Collected Date | 2026-07-01 | When it was added to the library |
| Collection Method | Automated export | How it was obtained |
| Period Covered | June 2026 | What time period the evidence covers |
| Stored At | /evidence/02-access/jml-2026-06.csv | File path or URL |
| Retention | 3 years | |
| Expiration/Freshness | Refresh monthly | When this evidence becomes stale |
| Quality Status | Accepted | Pending / Accepted / Rejected / Stale |
| Reviewed By | Governance Lead | |

### Exposure Backlog Spreadsheet

| Column | Example | Notes |
|--------|---------|-------|
| Finding ID | FIND-2026-001 | Format FIND-YYYY-NNN |
| CVE / ID | CVE-2026-12345 | |
| CVSS Score | 9.8 | |
| KEV Listed? | No | Check CISA KEV catalog |
| Severity | Critical | Critical / High / Medium / Low |
| Asset | ExampleApp (public-facing) | |
| Asset Tier | Tier 1 | Per criticality model |
| Exploitability | Network-exploitable, no auth required | |
| Discovered Date | 2026-06-15 | |
| Triage Date | 2026-06-15 | |
| Triage SLA Met? | Yes | |
| Assigned To | Alex Chen | |
| Treatment | Patch to version 2.4.1 | |
| Due Date | 2026-06-17 | Critical = 48 hours |
| Closure Date | | |
| Validation Method | Authenticated re-scan | |
| Validated By | | |
| SLA Met? | | |
| Status | In Remediation | |

### Asset Inventory Spreadsheet

| Column | Example | Notes |
|--------|---------|-------|
| Asset ID | AST-001 | |
| Asset Name | ExampleApp | |
| Asset Type | SaaS Application | |
| Asset Class | Persistent | Persistent / Dynamic / Ephemeral |
| Environment | Production | |
| Business Owner | Jane Smith | |
| Technical Owner | Engineering Lead | |
| Data Classification | Internal | |
| Regulatory Scope | SOX | |
| Criticality | High | |
| Internet-Exposed? | Yes | |
| Scan Coverage | Yes — Tenable scan configured | |
| Logging Source | Yes — Splunk integration | |
| Backup Required? | Yes — vendor-managed | |
| Access Review Required? | Yes — quarterly | |
| Status | Fully Covered | |

### Vendor Inventory Spreadsheet

| Column | Example | Notes |
|--------|---------|-------|
| Vendor ID | VEN-001 | |
| Vendor Name | ExampleVendor Inc. | |
| Service Provided | Cloud hosting | |
| Data Accessed | Customer PII | |
| Data Classification | Confidential | |
| Criticality | High | |
| Risk Rating | Medium | |
| SOC 2 Available? | Yes — expires 2026-09 | |
| Contractual Security Requirements | MFA, encryption, incident notification 24h | |
| Last Assessment Date | 2026-03-15 | |
| Next Assessment Due | 2026-09-15 | |
| Business Owner | Jane Smith | |
| Status | Active | |

### Decision Log Spreadsheet

| Column | Example | Notes |
|--------|---------|-------|
| Decision ID | DEC-2026-001 | |
| Date | 2026-06-15 | |
| Decision | Defer ISO 27001 package | One sentence |
| Rationale | Not pursuing ISO certification | |
| Alternatives Considered | Adopt anyway — rejected | |
| Risk Created | Future ISO pursuit requires backfill | |
| Documents Affected | CAT-001, IMP-001 | |
| Approver | CISO | |
| Review Date | 2027-06-15 | |

---

## 8. Minimum Viable Evidence Library

Create this folder structure in your shared drive, document management system, or evidence repository. You do not need a GRC platform to start.

```
/evidence/
├── 00-program-governance/
│   ├── policy-approvals/
│   ├── org-profile/
│   └── decision-log/
├── 01-risk-register/
│   ├── risk-register-current.xlsx
│   ├── risk-acceptances/
│   └── exception-register-current.xlsx
├── 02-access-management/
│   ├── access-reviews/
│   ├── jml-evidence/
│   ├── privileged-access-reviews/
│   └── mfa-configuration/
├── 03-vulnerability-management/
│   ├── scan-reports/
│   ├── remediation-evidence/
│   └── exception-records/
├── 04-change-management/
│   ├── change-records/
│   └── security-impact-analyses/
├── 05-asset-inventory/
│   ├── asset-inventory-current.xlsx
│   └── network-diagrams/
├── 06-logging-monitoring/
│   ├── log-source-inventory.xlsx
│   └── detection-rule-evidence/
├── 07-backup-recovery/
│   ├── backup-configurations/
│   └── restore-test-results/
├── 08-vendor-risk/
│   ├── vendor-inventory-current.xlsx
│   └── vendor-assessments/
├── 09-incident-response/
│   ├── incident-records/
│   └── lessons-learned/
├── 10-regulatory/
│   ├── sox-evidence/        (if applicable)
│   ├── cmmc-evidence/       (if applicable)
│   └── cip-evidence/        (if applicable)
├── 11-audit/
│   └── audit-evidence-packages/
├── 12-board-reporting/
│   └── monthly-reports/
└── README.md                (explain what is stored where)
```

**Rules for the evidence library:**

- Every file in the library has an owner and a retention period.
- Evidence freshness is checked at the monthly review. Stale evidence is flagged.
- The evidence index spreadsheet (§7) maps every file to a control.
- Start with the folders you have evidence for. Empty folders remind you what is missing.
- If you have a GRC platform, migrate the spreadsheets into it when you outgrow manual management. The structure stays the same — the tool changes.

---

## 9. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-IMP-003 |
| **Version** | 1.01 |
| **Status** | Approved |
| **Effective Date** | 2026-06-14 |
| **Classification** | Public |
| **Owner** | Governance Pillar Leader |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual |
| **Next Scheduled Review** | 2027-06-11 |
| **Frameworks** | NIST CSF 2.0 |
| **Regulations** | Cross-cutting |
| **Environments** | Small-team CERG adopters (≤8 people) |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.01 | 2026-06-14 | Governance Pillar Leader | Aligned the CERG Lite package to the eight-document MVC and separated adoption aids from immediate requirements. |
| 1.0 | 2026-06-11 | Governance Pillar Leader | Initial release. CERG Lite package, reduced operating rhythm for 5-person teams, role consolidation map, first 10 records, first month criteria, spreadsheet schemas for 7 record types, minimum viable evidence library structure. |

### Review Triggers

- Feedback from small-team adopters
- Change to the canonical role roster
- Change to the control baseline
- Direction from the CISO

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| Implementation and Adaptation Guide | [`CERG-GOV-IMP-001`](CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) | How to adapt CERG |
| Adoption Safety Guide | [`CERG-GOV-IMP-002`](CERG-GOV-IMP-002_Adoption_Safety_Guide.md) | Prerequisites and safety rules |
| Operating Model | [`CERG-GOV-OM-001`](CERG-GOV-OM-001_CERG_Operating_Model.md) | Canonical roles and scaling map |
| Risk Management Framework | [`CERG-GOV-RMF-001`](CERG-GOV-RMF-001_Risk_Management_Framework.md) | Risk scoring and treatment |
| Cross-Pillar Operational Flows | [`CERG-GOV-FLOW-001`](CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md) | Evidence tiers and automation |
