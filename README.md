# CERG (surge) · Cybersecurity Operating Model

**An operating model for teams that need security to actually run.**

CERG helps security teams replace paper GRC with technical assurance. Cyber Engineering builds guardrails with the business. Cyber Risk tests whether those guardrails hold under real conditions. Cyber Governance records decisions, evidence, and accountability so risk can be managed and defended.

Old GRC asks, "Is the control documented?" CERG asks sharper questions:

- What security objective is this control supposed to achieve?
- How is it enforced in the environment?
- What evidence proves it operated for the right scope and period?
- Has anyone tried to bypass it through testing, adversarial validation, or incident analysis?
- What changed when the evidence showed weakness?

The goal is operating leverage: clearer decisions, fewer ad hoc meetings, less duplicated effort, better handoffs, and evidence created as work happens. A well-run security program should scale through clarity, technical guardrails, and validation, not by throwing more bodies or paperwork at every new requirement.

CERG is not a control framework, certification shortcut, or tooling project. Compliance alignment matters, but it is exhaust from operating well, not the engine.

---

## The CERG assurance loop

CERG turns security work into a repeatable loop:

1. **Build the guardrail** — standards, architecture patterns, configuration baselines, and secure implementation support.
2. **Test the guardrail** — exposure validation, threat modeling, penetration testing, red-team, purple-team, control testing, and incident lessons learned.
3. **Record the decision** — owner, evidence, exception, acceptance, treatment, or escalation.
4. **Improve the system** — update the control, architecture, procedure, metric, or staffing model when validation shows weakness.

That loop is the difference between a program that can prove security works and a program that can only prove paperwork exists.

---

## What CERG helps you build

CERG is built around three accountable pillars:

- **Cyber Engineering**: build security in early through standards, architecture review, secure development, resilience, logging, identity, cloud, SaaS, AI, and OT guardrails.
- **Cyber Risk**: understand exposure, track risk decisions, manage exceptions, and drive treatment.
- **Cyber Governance**: set clear rules, record decisions, define ownership, and keep evidence usable.

Use CERG to:

- make security ownership explicit;
- turn tribal knowledge into repeatable workflows;
- give engineering teams clear guardrails instead of vague security asks;
- reduce toil from recurring reviews, audits, exceptions, and reporting;
- create reusable evidence as work happens;
- build a security function that can grow without making every problem a staffing problem.

---

## Start here

| If you are... | Start with |
|---|---|
| New to CERG | [START-HERE.md](START-HERE.md) |
| A CISO / CSO evaluating CERG | [CISO / CSO Executive Briefing Pack](adoption-packs/ciso-cso-briefing/README.md) |
| New to GitHub or Markdown | [BEGINNER-GUIDE.md](BEGINNER-GUIDE.md) |
| Using an AI assistant or coding agent | [ADOPT-WITH-AN-AGENT.md](ADOPT-WITH-AN-AGENT.md) |
| A small team adopting the minimum spine | [CERG Lite adoption pack](adoption-packs/cerg-lite/README.md) |
| Looking for operational examples | [Day in the Life examples](examples/day-in-the-life/README.md) |
| Comparing adoption paths | [Adoption Decision Tree](governance/CERG-GOV-IMP-005_Adoption_Decision_Tree_and_Dependency_Matrix.md) |
| Contributing | [CONTRIBUTING.md](CONTRIBUTING.md) |
| Community contributors | [CONTRIBUTORS.md](CONTRIBUTORS.md) |

---

## Adoption modes

You do not adopt the full library in week one. Start with the spine, prove the operating rhythm, then add depth where the organization actually needs it.

- **CERG Lite**: the minimum viable program for a small or early security function.
- **CERG Standard**: the core operating model for an established security team.
- **CERG Regulated**: Standard plus overlays for regulated, audited, privacy, OT, or critical infrastructure scope.

The minimum viable CERG spine is eight documents: Policy, Framework, Operating Model, Document Catalog, Risk Management Framework, Risk Register Procedure, Risk Register Templates, and Exposure Management Procedure.

---

## What is in the repo

CERG includes:

- `governance/`: policy, operating model, risk framework, RACI, metrics, maturity, workforce governance, and program structure.
- `standards/`: technical standards that define what good looks like across major security domains.
- `procedures/`: repeatable workflows for risk, exposure, architecture review, TPRM, audit/evidence, change, threat modeling, and related work.
- `plans/`: operational packages for regulated or specialized scopes.
- `templates/`: practical forms, registers, and records teams can use directly.
- `roles/`: workforce architecture, job families, job descriptions, competencies, and onboarding.
- `machine-readable/`: indexes, manifests, schemas, flow models, and agent-friendly metadata.
- `examples/`: adoption examples and day-in-the-life walkthroughs.

The authoritative inventory is the [Document Catalog](governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md).

---

## LLM and automation use

Use these entry points before loading the full corpus:

- [`machine-readable/cerg-llm-index.json`](machine-readable/cerg-llm-index.json): complete local corpus map.
- [`machine-readable/cerg-document-tiers.yaml`](machine-readable/cerg-document-tiers.yaml): adoption tiers and recommended loading order.
- [`llms.txt`](https://cerg.nexus/llms.txt): public LLM index.
- [`llms-full.txt`](https://cerg.nexus/llms-full.txt): full public corpus mirror.

The GitHub repository is authoritative. The website is a convenience mirror and may lag the repo.

---

## When CERG is not a good fit

Do not adopt CERG yet if there is no named security owner, no executive support for guardrails and evidence, unclear scope, or no willingness to track decisions and exceptions.

Start lighter, establish ownership and evidence discipline, then return when the organization is ready to operate security as a real function.

CERG does not determine legal obligations or certification readiness. Validate regulatory applicability with qualified counsel, compliance leadership, and assessors.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · Fork freely - adapt openly - attribute generously :)
