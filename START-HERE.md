# START HERE · Adopting CERG

You just found CERG. You have a repo full of Markdown. What do you actually do on Monday morning?

**This page is your first 48 hours.** Read it before you read anything else.

## If you were just assigned to CERG

Use your first ten minutes to orient yourself in these three documents; do not try to finish them.

1. **[Cybersecurity Policy](governance/CERG-POL-001_Cybersecurity_Policy.md) §§1, 2, and 5**: the authority, operating model, and policy accountabilities. The CISO approves the policy; the Executive Sponsor endorses it.
2. **[CERG Framework](governance/CERG-GOV-FRM-001_CERG_Framework.md) §2.2**: the three pillars and where you sit.
3. **[Operating Model](governance/CERG-GOV-OM-001_CERG_Operating_Model.md) §§2.4 and 4.2**: the first-line/CERG boundary and decision rights.

Then answer four questions about your own scope. The one you cannot answer is the next thing you read.

- **Decision.** Which decisions are yours to make, and which are not yours at all? The [RAC-001 §6](governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md#6-master-raci-standing-processes) process matrices name the accountable decision role; [OM-001 §6.1](governance/CERG-GOV-OM-001_CERG_Operating_Model.md#61-canonical-role-roster) names the canonical CERG roles.
- **Owner.** Who is accountable for the outcome when it is not you? Name the role, not the person doing the work.
- **Boundary.** CERG defines requirements, reviews evidence, independently validates, and escalates. First-line owners and operators deploy, operate, monitor, and remediate.
- **Exception path.** If a control cannot be met as written, or residual risk is within appetite, start at the [Risk Register and Exception Process](procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md#1-purpose-and-scope) §1. Its §7.1 distinguishes the two paths, its §8 summarises who signs at each rating, and [RMF-001 §9.7](governance/CERG-GOV-RMF-001_Risk_Management_Framework.md#97-risk-acceptance-authority-canonical) is the canonical acceptance authority.

If you have been handed a risk to accept or an exception to grant, start at §1.

---

## Step 0: Is CERG right for you right now?

CERG requires organizational commitment. Answer honestly:

- Do you have a named person who will own security? (Even part-time, even informal.)
- Does leadership support establishing guardrails — not just buying tools?
- Can you name the systems, business units, and regulators in your scope?
- Will you track versions, record decisions, and produce evidence?

If you answered **no** to any of these, start with NIST CSF or CIS Controls. Come back to CERG when you're ready.

If you answered **yes** to all four, do not start by reading the whole repository. Pick one entry point, read only the documents needed for that decision, and let the operating cadence pull in the rest.

---

## First rule: do not boil the ocean

CERG is intentionally complete, but first adoption is intentionally narrow. Your first hour should answer one question: **what problem are we trying to operate better?**

Use these rules:

- **Read for a job, not for completeness.** Open the documents tied to your role, snag, regulator, or environment.
- **Adopt the spine before the library.** The Minimum Viable CERG set is enough to start producing decisions, risks, exposure records, and evidence.
- **Defer what you do not operate.** Do not read OT, CUI, SOX, AI, or workforce-depth documents unless that scope exists now.
- **Prefer one worked example over ten abstractions.** Read a Day in the Life story that matches your problem before reading every standard.
- **Stop reading when you can name the owner, record, decision path, and next action.** CERG is an operating model, not a reading challenge.

### Pick your entry point

| If your immediate question is... | Start with | Stop when you can... |
|---|---|---|
| “What is CERG and should I care?” | [CISO / CSO Executive Briefing Pack](adoption-packs/ciso-cso-briefing/README.md) | Explain the operating problem CERG solves in five minutes. |
| “We are a small team and need the minimum viable program.” | [CERG Lite adoption pack](adoption-packs/cerg-lite/README.md) and [Small Team Adoption Path](governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md) | Name the eight-document spine and first 10 records. |
| “I own vulnerabilities or exposure.” | [Exposure Management Procedure](procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) and [critical vulnerability story](examples/day-in-the-life/README.md#story-2-critical-vulnerability) | Move an observation from scanner output to treatment or accepted risk. |
| “Security reviews happen too late.” | [Architecture Review Procedure](procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) and [new SaaS story](examples/day-in-the-life/README.md#story-1-new-saas-application) | Route a project through intake, review, disposition, and handoff. |
| “We bought tools but cannot prove controls work.” | [Control Effectiveness Framework](governance/CERG-GOV-CEF-001_Control_Effectiveness_Framework.md), [Adversarial Validation Procedure](procedures/CERG-PRC-AV-001_Adversarial_Validation_Procedure.md), and [Metrics](governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) §3.6a | Distinguish implementation evidence from operating effectiveness evidence. |
| “Audit evidence is chaos.” | [Evidence Quality Standard](governance/CERG-GOV-AUD-001_Evidence_Quality_Standard.md), [Audit and Evidence Procedure](procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md), and [Record Catalog](governance/CERG-GOV-CAT-002_Record_Catalog.md) | Identify the record, owner, period, and evidence quality bar. |
| “We have CUI, NERC-CIP, SOX, ISO, privacy, OT, or AI scope.” | The relevant overlay in [Path 3: CERG Regulated](#path-3-cerg-regulated-nerc-cip-cmmc-sox-ot-environments) | Name which conditional documents apply and which can be deferred. |
| “I am designing roles or hiring.” | [Job Families Overview](roles/CERG-GOV-JF-001_Job_Families_Overview.md) and [Workforce Planning](governance/CERG-GOV-WFP-001_Workforce_Planning_and_Capacity_Model.md) | Map responsibilities to roles without hiding accountabilities. |
| “I am a business owner or system sponsor.” | [Risk Register and Exception Process](procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md#1-purpose-and-scope) §1, then the [Business Owner / System Sponsor Reader Path](governance/CERG-GOV-IMP-007_Role_Reader_Paths.md#6-business-owner--system-sponsor-reader-path) | Understand what decisions and evidence the business owner must provide. |
| “My service is approaching go-live.” | [Architecture Review and Project Intake Procedure §4](procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md#4-who-needs-a-review-and-who-doesnt), then [§8.3](procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md#83-outcome) and [§9](procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md#9-phase-5-production-handoff-and-go-live) | Name whether review applies, your Phase 4 disposition, who holds the go-live decision, and what happens if it is Not Ready. |
| “I operate systems, or I am a provider, and CERG sent me requirements.” | [Operating Model §2.4](governance/CERG-GOV-OM-001_CERG_Operating_Model.md#24-lines-of-accountability-and-assurance) and [Risk Register and Exception Process §7.1](procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md#71-exception-vs-risk-acceptance--which-path-to-use) | Name what you operate, what CERG validates, and the exception route for a requirement you cannot meet. |
| “Someone has handed me a risk to accept or an exception to grant.” | [Risk Register and Exception Process §1](procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md#1-purpose-and-scope) and [Risk Management Framework §9.7](governance/CERG-GOV-RMF-001_Risk_Management_Framework.md#97-risk-acceptance-authority-canonical) | Name which of the two decisions you are being asked for, who co-signs it, when it expires, and what happens if you decline. |
| “I am using an AI or coding agent.” | [ADOPT-WITH-AN-AGENT.md](ADOPT-WITH-AN-AGENT.md) and [`machine-readable/cerg-llm-index.json`](machine-readable/cerg-llm-index.json) | Load only the documents needed for the task. |

If you are still unsure where to begin, use these helpers before diving into the full library:

- [CISO / CSO Executive Briefing Pack](adoption-packs/ciso-cso-briefing/README.md) - slide-style executive introduction for leaders who need the hook, operating boundaries, anti-patterns, and “who does what” before reading the corpus.
- [Framework System Map](governance/CERG-GOV-FRM-002_Framework_System_Map.md) - how the documents, pillars, records, evidence, and improvement loops fit together.
- [Adoption Decision Tree and Dependency Matrix](governance/CERG-GOV-IMP-005_Adoption_Decision_Tree_and_Dependency_Matrix.md) - which path and overlays apply, plus what must be adopted together.
- [Role-Based Implementation Checklists](governance/CERG-GOV-IMP-006_Role_Based_Implementation_Checklists.md) - what the CISO, Governance, Risk, and Engineering leads do first.
- [Record Catalog](governance/CERG-GOV-CAT-002_Record_Catalog.md) - the records and minimum evidence that prove the program is operating.
- [Day in the Life examples](examples/day-in-the-life/README.md) - twelve narrative walkthroughs showing how the three pillars produce real work during incidents, audits, intake, AI rollouts, access reviews, new-CISO adoption, and OT patch deferral. Read one before you read the standards.
- [Role Reader Paths](governance/CERG-GOV-IMP-007_Role_Reader_Paths.md) - a sequenced 25-35 minute reading order for the CISO, Risk Lead, Engineering Lead, and Business Owner / System Sponsor if you are taking on a CERG role for the first time.

### Adoption suite map

| If you need to... | Use |
|---|---|
| Pick the right adoption path in the first hour | This START-HERE page |
| Brief a CISO / CSO before asking them to read the corpus | [CISO / CSO Executive Briefing Pack](adoption-packs/ciso-cso-briefing/README.md) |
| Understand the narrative rollout model | [IMP-001 Implementation and Adaptation Guide](governance/CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) |
| Avoid unsafe tailoring and authority collapse | [IMP-002 Adoption Safety Guide](governance/CERG-GOV-IMP-002_Adoption_Safety_Guide.md) |
| Run CERG with 2-8 people | [IMP-003 Small Team Adoption Path](governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md) |
| Decide Lite / Standard / Regulated and dependencies | [IMP-005 Decision Tree and Dependency Matrix](governance/CERG-GOV-IMP-005_Adoption_Decision_Tree_and_Dependency_Matrix.md) |
| Convert reading into action | [IMP-006 Role-Based Implementation Checklists](governance/CERG-GOV-IMP-006_Role_Based_Implementation_Checklists.md) |
| Onboard a specific role quickly | [IMP-007 Role Reader Paths](governance/CERG-GOV-IMP-007_Role_Reader_Paths.md) |

---

## Path 1: CERG Lite (small security team, 2-8 people)

**You have:** A small team with at least two named participants in cyber risk decisions. No existing framework, or a framework that is not yet operational.

If you are a one-person security function, use CERG as a planning reference and adopt the MVC documents only after you have an Executive Sponsor and an independent approver for High/Critical risk decisions.

**Your goal:** Stand up a real program without drowning in documents.

### First 48 hours

1. **Read the [Cybersecurity Policy](governance/CERG-POL-001_Cybersecurity_Policy.md).** This is the spine. The CISO approves it; the Executive Sponsor endorses it.
2. **Read the [CERG Framework](governance/CERG-GOV-FRM-001_CERG_Framework.md)** — the three-pillar model. You'll consolidate roles heavily; that's expected.
3. **Read the [Small Team Adoption Path](governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md).** This is your primary guide. It covers the CERG Lite package, small-team operating rhythm, role consolidation map, first 10 records, and spreadsheet schemas.
4. **Read the [Role-Based Implementation Checklists](governance/CERG-GOV-IMP-006_Role_Based_Implementation_Checklists.md).** Use the small-team consolidated checklist if one person holds multiple roles.
5. **Read the [Implementation Guide](governance/CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md)** §4 (MVC). Follow the Minimum Viable CERG sequence.
6. **Fork the repo.** Do not cherry-pick individual files. The documents are interconnected.
7. **Fill in the [Organization Adaptation Profile](governance/CERG-GOV-VAR-001_Organization_Adaptation_Profile.md).** Set your headcount, sector, and regulators. Do NOT leave the default values.
8. **Start the Risk Register.** Open [the template](templates/CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md). Create your first entry. It can be simple.
9. **Create the first records from the [Record Catalog](governance/CERG-GOV-CAT-002_Record_Catalog.md).** Start with role assignment, evidence index, asset extract, top risks, exposure backlog, and exception register.
10. **Run the first exposure management cycle.** Even if it starts with one Nessus scan on your production subnet, open [PRC-VM-001](procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) and follow the observe → validate → assess reachability → classify → treat → verify flow.

### Your MVC set

Adopt these eight documents first:

1. Cybersecurity Policy
2. CERG Framework
3. Operating Model (focus on §6, role consolidation)
4. Document Catalog (update it as you go)
5. Risk Management Framework
6. Risk Register & Exception Process
7. Risk Register Templates
8. Exposure Management Procedure

Use the Record Catalog, Adoption Safety Guide, Small Team Adoption Path, and Role-Based Implementation Checklists as adoption aids. They help you adopt the MVC; they are not additional MVC requirements.

**Read one story.** The [CERG Lite day-in-the-life walkthrough](examples/day-in-the-life/story-8-cerg-lite-maria.md) shows what your first month of running the MVC actually looks like when two people own everything.

### What you can defer

- All 15 standards (bring in individually as needed)
- Most procedures beyond VM and Risk Register
- Operational packages (unless you're regulated — see Path 3)
- Workforce architecture docs (start with JF-001, defer per-role JDs)
- Machine-readable artifacts
- Detailed job descriptions

---

## Path 2: CERG Standard (existing security team, 6-30 people)

**You have:** A functioning security team. Policies exist but are fragmented. Tools are deployed but processes are ad hoc.

**Your goal:** Replace the pile of disconnected documents with a unified operating model.

### First 48 hours

1. **Read the [CERG Framework](governance/CERG-GOV-FRM-001_CERG_Framework.md).** Map your existing team to the three pillars. Identify gaps.
2. **Read the [Implementation Guide](governance/CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md)** §4-5. Follow the MVC sequence plus core standards.
3. **Map your current documents to CAT-001.** What do you already have that maps to a CERG artifact? What's missing?
4. **Adopt the spine (8 MVC docs) first.** Adapt them to your organization — not the other way around.
5. **Layer core standards next:** Access Management, Asset Management, Configuration Baseline (DISH), IT/Cloud/SaaS where applicable, Logging/Monitoring, and Resilience/Backup.
6. **Add Architecture Review and TPRM procedures.** These are the two procedures that prevent the most future pain.

### Your starting set

MVC (all 8) + Access, Asset, Config Baseline, IT/Cloud/SaaS where applicable, Logging/Monitoring, and Resilience/Backup standards + Architecture Review Procedure, TPRM Procedure.

---

## Path 3: CERG Regulated (NERC-CIP, CMMC, SOX, OT environments)

**You have:** Regulatory obligations. Auditors. Critical infrastructure. An existing security team.

**Your goal:** Map CERG to your regulatory framework without duplicating work.

### First 48 hours

1. **Read the [CERG Framework](governance/CERG-GOV-FRM-001_CERG_Framework.md).** Understand the three-pillar model.
2. **Read the [Implementation Guide](governance/CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md)** §4-5.
3. **Adopt the MVC spine.**
4. **Identify your regulatory overlay.** Open the relevant operational package:
   - NERC-CIP → [PLN-CIP-001](plans/CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md)
   - CMMC / CUI → [PLN-CUI-001](plans/CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md)
   - SOX ITGC → [PLN-SOX-001](plans/CERG-PLN-SOX-001_SOX_ITGC_Operational_Package.md)
   - ISO 27001 → [PLN-ISO-001](plans/CERG-PLN-ISO-001_ISO_IEC_27001_Operational_Package.md)
5. **Map your evidence requirements.** Each operational package links evidence to specific CERG procedures. Understanding this linkage is the key to making compliance a byproduct of operations.
6. **See the [Compliance Matrix](governance/CERG-GOV-CMX-001_Compliance_Matrix.md).** 22 security intents mapped to every framework simultaneously.

### Your starting set

MVC + all 15 standards + Architecture Review, TPRM, Change Management, Audit/Evidence procedures + your regulatory operational packages.

---

## What CERG adoption is NOT

- **Not a certification.** You can adopt CERG and still fail a regulatory assessment if controls aren't implemented and evidenced.
- **Not a substitute for judgment.** CERG provides structure. You provide decisions, owners, scope, and risk appetite.
- **Not a one-time exercise.** A program runs on cadence. If you're not producing evidence from real work every month, you're not running CERG.
- **Not shelfware.** If you fork the repo, rename the company, approve everything, and walk away, you have produced exactly nothing.

## What good adoption should feel like

CERG should create operating leverage. After the first cycle, the work should feel clearer, not heavier:

- owners and decision rights are easier to name;
- recurring reviews produce records instead of status theater;
- evidence is easier to retrieve because it was created during the work;
- engineering teams receive clearer guardrails;
- fewer problems depend on the same hero person;
- leaders can see whether the bottleneck is capability, scope, tooling, or staffing.

If adoption mostly adds meetings, manual chasing, or ambiguity, stop adding documents and fix the workflow.

### Schedule your first stakeholder survey at month 2

After one full cadence cycle (approximately 60 days), administer the [Stakeholder Perception Survey](templates/CERG-TMPL-GOV-001_Stakeholder_Perception_Survey.md). The survey is how you measure whether the program is reducing drag and confusion for the business, which is the program's stated mission. Run annually thereafter. Survey results below 3.0 on a Likert scale, or a year-over-year decline of 0.5 points or more, become entries in the [Program Improvement Register](governance/CERG-GOV-IMPREG-001_Program_Improvement_Register.md). The survey is paired with monthly [Service Responsiveness metrics](governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) (SR-001 through SR-005) so friction is caught continuously, not only once a year.

---

## When you get stuck

**Before you ask for help:**
1. Re-read the [Implementation Guide](governance/CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) §9 (Common Adoption Pitfalls).
2. Check your org profile in [VAR-001](governance/CERG-GOV-VAR-001_Organization_Adaptation_Profile.md) — are you still using the default values?
3. Run `python3 tools/cerg-validate.py` — broken links or catalog mismatches will surface mechanical problems.
4. Look at the [examples/](examples/) directory for sample profiles that match your sector and size.

---

## After the first 30 days

Once MVC is running, layer the remaining documents as needed. The sequence matters less after the spine is in place. Prioritize based on what's causing the most operational friction.

Before broad standard-layer adoption, use the Gate 2 to Gate 3 transition test in the [Adoption Decision Tree and Dependency Matrix](governance/CERG-GOV-IMP-005_Adoption_Decision_Tree_and_Dependency_Matrix.md). Do not advance just because the calendar says day 60 or day 90. Advance when the MVC has produced risk, exposure, intake, evidence, pillar-accountability, and adoption-plan records.

**[Back to README](README.md)** · **[Full catalog](governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md)** · **[Implementation Guide](governance/CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md)**
