# CERG · Cybersecurity Operating Model

## cragin-security fork — practice-hardened for MSP/MSSP delivery

**This is the [cragin-security](https://github.com/cragin-security/CERG) fork of [m0dernz/CERG](https://github.com/m0dernz/CERG).**

We contribute upstream — bug fixes, doc improvements, framework enhancements — and this fork carries the **practice layer** that turns CERG from a framework into a service delivery model.

---

### The upstream relationship

CERG is Ron Brown's cybersecurity operating model. It gives security teams the policy spine, roles, standards, procedures, and evidence habits needed to run a real program. Read the [upstream README](https://github.com/m0dernz/CERG) for the canonical description.

This fork extends the architecture into something an MSP technician can follow:

| Dimension | Upstream (m0dernz/CERG) | This Fork (cragin-security/CERG) |
|-----------|------------------------|----------------------------------|
| **Controls** | ~18 schematic entries | **87 controls** with copy-paste MSP instructions per control |
| **Tools** | Framework-level | **Opinionated tool matrix** — primary/acceptable/avoid per category |
| **Audience** | Program architects, auditors | **MSPs, MSSPs, IT generalists** — entry-level IT staff can follow the runbook |
| **Evidence** | Named evidence in control spec | **Tool-to-evidence pipeline mapping** — API endpoints, GRC integration, collection frequency per control |
| **GRC anchor** | Architecture reference | **ServiceNow GRC + Vanta rollout guide** with control import scripts and evidence automation |
| **Delivery** | CERG Lite / Standard / Regulated adoption paths | **Full engagement playbook** with fixed-fee + MRR pricing, SOW templates, delivery phases |
| **Consulting** | Implicit | **Explicit** — engagement anti-patterns, SOW essentials, pricing reference, handoff procedures |
| **Architecture** | CERG framework decisions | **ADR log** documenting why each opinionated choice was made |

**Boundary:** Everything in `practice-assets/` uses the `OPN` domain prefix. These are fork-only. They never go upstream. Framework improvements to `governance/`, `standards/`, and `procedures/` are contributed back.

---

## What this fork adds

### Practice Assets (`practice-assets/`)

| Document | What it does |
|----------|--------------|
| [Opinionated Tool Matrix](practice-assets/tools/opinionated-tool-matrix-v1.md) | 12 security tool categories — every recommendation scored on integration surface, MSP multi-tenancy, and IT generalist usability. Integration map shows how the stack wires together. |
| [GRC Rollout Guide](practice-assets/tools/grc-rollout-v1.md) | Step-by-step ServiceNow GRC control import, evidence automation, MSP multi-tenancy. Vanta fallback for SMB. |
| [Evidence Automation Mapping](practice-assets/tools/evidence-automation-mapping-v1.md) | Every control mapped to its evidence pipeline: which tool collects it, what API endpoint, how it feeds into GRC. 56 of 87 controls auto-evidenced. |
| [MSP/MSSP Runbook](practice-assets/msp-runbook-v1.md) | 5-phase delivery playbook: client intake → tool deployment (copy-paste commands for SentinelOne, Wazuh, Tenable, Wiz, Veeam) → per-control implementation → evidence collection → client reporting. |
| [Engagement Playbook](practice-assets/engagement-playbook-v1.md) | Full consulting lifecycle: Discover → Assess → Plan → Deploy → Operate → Handoff. Pricing for SMB through enterprise. Anti-patterns and SOW essentials. |

### 87-Core Control Baseline

The [100-Core Control Baseline](governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md) (now 87 controls after culling overlap) extends upstream's schematic control matrix into full enumerated controls across all 19 NIST 800-53r5 families. Every control has:

- A declarative action statement an IT generalist can implement
- Named evidence with collection method and minimum frequency
- A subordinate standard cross-reference
- An MSP implementation note with copy-paste commands
- A tool binding tied to the opinionated tool matrix

### Recommends specific tools, not categories

Instead of "deploy a SIEM" or "use a GRC platform," this fork says:

- **SIEM:** Wazuh (SMB), Elastic Security (enterprise)
- **EDR:** SentinelOne (best MSP console, ServiceNow integration)
- **GRC:** ServiceNow GRC (enterprise), Vanta (SMB)
- **Identity:** Okta (multi-tenant), Entra ID (M365 shops)
- **Network:** Fortinet (best MSP program, best value)
- **CSPM:** Wiz (agentless, multi-cloud)
- **AppSec:** Trivy + Semgrep (free, CLI-first, CI/CD-native)
- **Backup:** Veeam (immutable backups, Service Provider Console)
- **Avoid:** spreadsheets, Archer, DIY ELK, QRadar, SonicWall — with reasons why

Every recommendation is backed by documented criteria in [ADR-002](governance/CERG-GOV-ADR-001_Architecture_Decision_Records.md#adr-002-tool-stack-opinionation).

### Architecture Decision Records

The [ADR log](governance/CERG-GOV-ADR-001_Architecture_Decision_Records.md) captures why each fork-specific choice was made:

- **ADR-001:** Why OPN domain boundary (practice assets vs framework)
- **ADR-002:** Why each tool won over its alternatives
- **ADR-003:** Why CB-002 has 87 controls (culling criteria)
- **ADR-004:** Why evidence automation is a separate document
- **ADR-005:** Why MSP delivery model over enterprise consulting

---

## Start here

| If you are... | Start with |
|---|---|
| An MSP/MSSP delivering CERG to clients | [MSP/MSSP Runbook](practice-assets/msp-runbook-v1.md) |
| Picking tools for a CERG deployment | [Opinionated Tool Matrix](practice-assets/tools/opinionated-tool-matrix-v1.md) |
| Setting up automated compliance evidence | [Evidence Automation Mapping](practice-assets/tools/evidence-automation-mapping-v1.md) |
| Setting up a GRC platform | [GRC Rollout Guide](practice-assets/tools/grc-rollout-v1.md) |
| Scoping or pricing a CERG engagement | [Engagement Playbook](practice-assets/engagement-playbook-v1.md) |
| Looking for the full control set | [100-Core Control Baseline](governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md) |
| Understanding why specific choices were made | [Architecture Decision Records](governance/CERG-GOV-ADR-001_Architecture_Decision_Records.md) |
| Tailoring or maintaining the practice layer | [Practice Assets Operating Guide](practice-assets/README.md) |
| New to CERG (upstream) | [START-HERE.md](START-HERE.md) |
| Using an AI assistant | [ADOPT-WITH-AN-AGENT.md](ADOPT-WITH-AN-AGENT.md) |
| Contributing upstream | [CONTRIBUTING.md](CONTRIBUTING.md) |

---

## When this fork is right for you

**Use cragin-security/CERG** when you:

- Are an MSP, MSSP, or IT generalist delivering security to small/mid-sized clients
- Want specific tool recommendations, not categories to evaluate
- Need copy-paste deployment instructions your entry-level techs can follow
- Want a consulting practice wrapper around the CERG operating model
- Need automated evidence pipelines that feed into ServiceNow or Vanta

**Use upstream m0dernz/CERG** when you:

- Want the canonical framework architecture without opinionated tool choices
- Are building your own tool strategy and just need the program structure
- Prefer the lighter, schematic control set for organizational calibration

---

## What is in the repo

Everything upstream carries, plus:

| Directory | Content |
|-----------|---------|
| `governance/` | Policy, operating model, risk framework, RACI, metrics, maturity — plus the fork's [87-Core Control Baseline](governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md) and [ADR log](governance/CERG-GOV-ADR-001_Architecture_Decision_Records.md) |
| `standards/` | Technical security standards (15 docs) |
| `procedures/` | Repeatable workflows for risk, exposure, architecture review, TPRM, audit, change, threat modeling |
| `plans/` | Operational packages for regulated or specialized scopes |
| `templates/` | Forms, registers, and records |
| `roles/` | Workforce architecture — job families, JDs, competencies, onboarding |
| `practice-assets/` | **Fork-only**: tool matrix, GRC rollout, evidence mapping, MSP runbook, engagement playbook |
| `machine-readable/` | Indexes, manifests, schemas, LLM metadata |
| `examples/` | Adoption examples and day-in-the-life walkthroughs |

The authoritative inventory is the [Document Catalog](governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md).

---

## LLM and automation use

- [`machine-readable/cerg-llm-index.json`](machine-readable/cerg-llm-index.json): complete local corpus map
- [`machine-readable/cerg-document-tiers.yaml`](machine-readable/cerg-document-tiers.yaml): adoption tiers and loading order
- [`AGENTS.md`](AGENTS.md): guidance for AI coding agents working in this repo

---

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · Fork freely — adapt openly — attribute generously.

Upstream: [m0dernz/CERG](https://github.com/m0dernz/CERG) · Fork: [cragin-security/CERG](https://github.com/cragin-security/CERG)
