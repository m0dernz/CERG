# SURGE: Cyber Engineering, Risk & Governance

## THREAT MODELING PROCEDURE
### Design Review · ATT&CK Mapping · Abuse Cases · Control Decisions · Architecture Review Input

---

| | |
|---|---|
| **Document ID** | CERG-PRC-TM-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Risk Pillar Leader |
| **Parent Policy** | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Documents** | [`CERG-GOV-OM-001`](../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) · [`CERG-PRC-AR-001`](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) · [`CERG-GOV-CB-001`](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) · [`CERG-STD-SDL-001`](../standards/CERG-STD-SDL-001_Secure_Software_Development_and_Application_Security_Standard.md) · [`CERG-STD-AI-001`](../standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md) · [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) |
| **Review Cycle** | Annual / On material change to architecture review or threat modeling methods |
| **Frameworks** | [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) (RA, SA, PL, SC) · [NIST 800-160](https://csrc.nist.gov/pubs/sp/800/160/v1/final) · [NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) · [MITRE ATT&CK](https://attack.mitre.org/) · [MITRE ATT&CK for ICS](https://attack.mitre.org/matrices/ics/) · [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) |
| **Regulations** | CMMC L2 / 800-171r3 · NERC-CIP · SOX ITGC where applicable |
| **Environments** | All projects subject to CERG architecture review and all material changes to in-scope systems |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Principles](#2-principles)
3. [When Threat Modeling Is Required](#3-when-threat-modeling-is-required)
4. [Inputs](#4-inputs)
5. [Method](#5-method)
6. [Outputs](#6-outputs)
7. [Integration With Architecture Review](#7-integration-with-architecture-review)
8. [Finding Severity and Treatment](#8-finding-severity-and-treatment)
9. [Scaling the Procedure](#9-scaling-the-procedure)
10. [Roles and Responsibilities](#10-roles-and-responsibilities)
11. [Metrics](#11-metrics)
12. [Regulatory and Framework Alignment Summary](#12-regulatory-and-framework-alignment-summary)
13. [Document Control](#13-document-control)

---

## 1. Purpose and Scope

The CERG README states that during architecture and design review, Engineering leads and Risk performs threat modeling. [`CERG-PRC-AR-001`](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) makes threat modeling part of Phase 2. Until this procedure, the method, triggers, inputs, outputs, and handoff rules were implicit. This procedure makes them executable.

Threat modeling is the design-time discipline of asking how a system can be abused before it is built or changed. It is not a paperwork exercise. It is how CERG turns threat knowledge into architecture decisions, control requirements, and risk register entries early enough that the project can still change cheaply.

This procedure applies to every project subject to CERG architecture review, every material change to an in-scope system, and every new or materially changed use of AI, cloud, SaaS, OT, identity, regulated data, or internet exposure.

> **Threat Modeling Is Risk's Design Contribution**
>
> Engineering reviews whether the design can be built and operated securely. Risk asks how an adversary will try to break it. Those are different questions, and a serious project needs both. Threat modeling is where Cyber Risk earns its seat in the design conversation: not by saying no, but by naming the attack paths early enough that Engineering can design them out.

---

## 2. Principles

1. **Model early.** The threat model happens while design decisions are still changeable. A threat model performed after go-live is a postmortem with nicer formatting.
2. **Model the system, not the diagram.** Diagrams are inputs. The model is about how data, identities, trust boundaries, and attackers move through the real system.
3. **Use threat intelligence, but do not wait for perfect intelligence.** Known threat actors, MITRE ATT&CK techniques, and recent incidents improve the model. Absence of a named actor is not absence of threat.
4. **Produce decisions.** A threat model that does not change a design, add a control, create a finding, or record an accepted risk did not do its job.
5. **Keep it proportional.** A low-risk SaaS configuration change does not need a three-hour workshop. A new internet-facing application touching Restricted data does.
6. **No orphan findings.** Every threat-model output has a disposition: designed out, mitigated by a control, accepted through the risk process, or tracked to remediation.

---

## 3. When Threat Modeling Is Required

Threat modeling is required when a project meets any of the mandatory architecture review triggers in [`CERG-PRC-AR-001`](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) §4.1 and also meets any of the following threat-modeling triggers.

| **Trigger** | **Why It Matters** |
|---|---|
| New internet-facing service or external API | Expands attacker-reachable surface. |
| Processing or storing Confidential or Restricted data | Raises impact of disclosure, alteration, and loss. |
| New identity, access, privilege, or federation pattern | Changes who can reach what and how compromise propagates. |
| New third-party integration or data exchange | Adds supply chain and trust-boundary risk. |
| New cloud, SaaS, or multi-tenant architecture | Changes control responsibility and isolation assumptions. |
| OT, BES Cyber System, or safety-impacting environment | Changes consequence and tolerance for active testing. |
| New AI system or AI feature | Introduces prompt injection, data leakage, excessive agency, and model supply chain risks. |
| Material change to an existing high-value system | Existing controls may no longer match the design. |
| Significant incident, finding, or threat intelligence affecting the design | New information changes the threat picture. |

A project below these thresholds may still receive a lightweight threat model at the discretion of the Risk Pillar Leader.

---

### 3.1 Legacy and Brownfield Systems

The triggers in Section 3.1 focus on new systems and material changes. For existing (brownfield) systems that have never been threat-modeled, the following prioritization framework applies.

#### Prioritization for Retroactive Threat Modeling

| **Priority** | **Criteria** | **Target Completion** |
|---|---|---|
| Priority 1 | Systems handling CUI, BCSI, or SOX-relevant data; BES Cyber Systems; systems with Critical or High open risk register entries; internet-facing Tier 1 systems | Within 6 months |
| Priority 2 | Internal Tier 1 or Tier 2 systems with Medium risk entries; systems supporting customer-facing services | Within 12 months |
| Priority 3 | Tier 2 or Tier 3 systems with Low risk entries; internal-only non-production systems | Within 24 months |
| Out of Scope | Tier 4+ systems; systems scheduled for decommissioning within 12 months; pure SaaS services where the vendor provides an equivalent threat model | - |

#### Lightweight Threat Model for Legacy Systems

For legacy systems where full threat modeling is infeasible (e.g., undocumented architecture, no original design artifacts), a lightweight approach is acceptable:

- **Scope**: Document known boundaries, data flows, and integrations rather than attempting to reconstruct the entire architecture.
- **Focus**: Concentrate on trust boundaries, external interfaces, and data classification paths rather than internal component detail.
- **Output**: A reduced threat model covering abuse cases for the top 5 risks identified from the risk register, exposure backlog, and incident history.
- **Acceptance**: The lightweight model is accepted as "sufficient for current risk posture" with a note that a full model will be produced at the next material change or system redesign.

---

## 4. Inputs

The Threat Intelligence Analyst and the project team provide inputs before the session. Missing inputs do not automatically stop the model, but missing critical inputs are recorded as assumptions.

| **Input** | **Source** | **Required For** |
|---|---|---|
| Business purpose and scope | Project sponsor or technical lead | Every model |
| Architecture diagram | Project technical lead | Every model |
| Data flow diagram | Project technical lead | Any system moving data across trust boundaries |
| Data classification | Asset Owners, per [`CERG-STD-DG-001`](../standards/CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md) | Any system processing data |
| Identity and access model | Identity Engineer | Any system with user, service, or privileged access |
| External dependencies and vendors | Vendor Risk Analyst | Any third-party integration |
| Deployment model and network paths | Cloud Security Engineer, OT Security Engineer, Endpoint Engineer as applicable | Cloud, OT, endpoint, and networked systems |
| Known vulnerabilities and prior findings | Exposure Management Lead, Adversarial Testing Lead | Existing systems and material changes |
| Relevant threat intelligence | Threat Intelligence Analyst, OT Risk Analyst where OT is in scope | Every model |
| Applicable control requirements | Governance Pillar Leader, compliance manager as applicable | Regulated or audited systems |
| Crown jewel scenarios | Crown Jewel Register ([CJ-001](../governance/CERG-GOV-CJ-001_Crown_Jewel_Register_and_Scenario_Library.md)) | Assets on the Crown Jewel Register. Import associated loss scenarios as mandatory threat model scenarios. Model attack paths to each chain-breaking control (CJ-001 §3.3). Record the imported scenario ID in the threat model record |

---

### 4.1 Threat Actor Identification

The abuse-case format includes a threat actor field. The following framework guides consistent actor identification.

| **Actor Category** | **Description** | **Capability** | **Motivation** |
|---|---|---|---|
| Nation-state | State-sponsored actors with advanced capabilities | Advanced (custom tools, zero-days) | Espionage, disruption, strategic advantage |
| Cybercriminal | Financially motivated organized groups | Intermediate to Advanced | Financial gain, data theft |
| Hacktivist | Ideologically motivated individuals or groups | Low to Intermediate | Publicity, political statement |
| Insider - Disgruntled | Employee/contractor with authorized access, malicious intent | Variable (access-dependent) | Revenge, financial gain |
| Insider - Negligent | Employee/contractor who unintentionally causes harm | Low (accidental) | None (error, negligence) |
| Competitor | Business competitor seeking advantage | Low to Intermediate | IP theft, market advantage |
| Script Kiddie | Low-skill actor using publicly available tools | Low | Curiosity, notoriety |

#### Actor Scoping

Actors are scoped based on data classification, industry sector, system exposure, and threat intelligence from [CERG-PRC-TI-001](CERG-PRC-TI-001_Threat_Intelligence_Procedure.md). Nation-state and competitor actors are in scope for CUI, BCSI, and strategic IP. Internet-facing systems include cybercriminal and hacktivist actors. Internal-only systems emphasize insider actors.

#### Actor-to-ATT&CK Mapping

| **Actor** | **Typical ATT&CK Techniques** |
|---|---|
| Nation-state | T1190, T1078, T1021, T1003, T1041 |
| Cybercriminal | T1566, T1203, T1486, T1048 |
| Insider | T1078, T1530, T1048, T1485 |
| Hacktivist | T1498, T1499, T1485, T1491 |

---

## 5. Method

CERG uses a practical hybrid method. It combines asset and data-flow review, trust-boundary analysis, abuse-case generation, and MITRE ATT&CK mapping. The method is intentionally simple enough to run in a one-hour working session but complete enough to produce durable findings.

### 5.1 Step 1: Define What Is Being Protected

The facilitator identifies the system's valuable assets and outcomes:

- data and its classification;
- identities and privileges;
- service availability and recovery expectations;
- financial, operational, safety, and regulatory impact;
- business process the system enables.

The goal is to state plainly what harm matters. A system cannot be threat-modeled well until the team knows what it is trying to protect.

### 5.2 Step 2: Draw Trust Boundaries

The facilitator marks trust boundaries on the architecture and data-flow diagrams. A trust boundary exists wherever control assumptions change: internet to internal, user to service, tenant to tenant, corporate to vendor, IT to OT, identity provider to application, or AI model to tool execution.

Every trust-boundary crossing is reviewed for authentication, authorization, encryption, logging, and validation.

### 5.3 Step 3: Generate Abuse Cases

The group asks how a motivated attacker, malicious insider, compromised vendor, or mistaken user could abuse the system. The facilitator records abuse cases in the form:

```text
As a [threat actor], I can [action] so that [impact].
```

Examples:

- As a phisher, I can steal a user's token and use it to call the application API so that I can export customer data.
- As a compromised vendor integration, I can send malformed payloads so that I can trigger unauthorized actions.
- As an attacker controlling prompt input, I can override the AI system's instructions so that it leaks restricted context.

### 5.4 Step 4: Map to ATT&CK

The Threat Intelligence Analyst maps plausible abuse cases to MITRE ATT&CK techniques. For OT systems, the OT Risk Analyst uses MITRE ATT&CK for ICS. Mapping is not done to decorate the document; it is done to check whether the model reflects real adversary behavior and to feed detection and control decisions.

### 5.5 Step 5: Decide the Control Response

For each abuse case, the team decides one of four dispositions:

| **Disposition** | **Meaning** |
|---|---|
| **Design out** | Change the architecture so the abuse case is no longer plausible. |
| **Mitigate** | Add or strengthen a preventive, detective, or recovery control. |
| **Accept** | Record and approve residual risk through [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md). |
| **Defer with owner and date** | Temporarily defer action, with an owner, due date, and review point. Deferment is not a parking lot. |

### 5.6 Step 6: Record Findings

Findings are written as control-relevant statements, not vague concerns. A good finding names the attack path, the affected asset, the missing or weak control, the likely impact, and the recommended treatment.

---

### 5.7 Structured Threat Classification (STRIDE)

STRIDE is the default threat classification framework for all CERG threat models. During abuse-case brainstorming (Section 5.3), the facilitator uses STRIDE categories as prompts to ensure comprehensive coverage.

| **STRIDE** | **Question** | **Example** |
|---|---|---|
| **S**poofing | Can an actor impersonate an identity? | Attacker authenticates as admin using stolen credentials |
| **T**ampering | Can an actor modify data? | Attacker modifies API payload to change authorization scope |
| **R**epudiation | Can an actor deny an action without proof? | User deletes sensitive record; audit log insufficient |
| **I**nformation Disclosure | Can an actor access data they should not see? | Attacker enumerates S3 bucket and downloads data |
| **D**enial of Service | Can an actor degrade or deny service? | Attacker exhausts API rate limits |
| **E**levation of Privilege | Can an actor gain unauthorized permissions? | Attacker exploits misconfigured IAM role to escalate |

#### STRIDE-to-ATT&CK Mapping

| **STRIDE** | **ATT&CK Tactics** | **Example Techniques** |
|---|---|---|
| Spoofing | Credential Access | T1078, T1550 |
| Tampering | Impact | T1565, T1485 |
| Repudiation | Defense Evasion | T1070, T1562 |
| Information Disclosure | Collection, Exfiltration | T1530, T1048 |
| Denial of Service | Impact | T1498, T1499 |
| Elevation of Privilege | Privilege Escalation | T1068, T1078 |

For OT systems, add **L**ateral Movement as a seventh category (STRIDE-LM).

### 5.6.1 AI-Specific Abuse Case Categories

When threat modeling systems that incorporate AI or ML capabilities, the following abuse case categories supplement the standard STRIDE framework. Detailed controls are defined in CERG-STD-AI-001.

| **Category** | **Description** | **Example Abuse Case** |
|---|---|---|
| Prompt Injection | Attacker crafts input that overrides system instructions or safety constraints | User injects "ignore previous instructions" to bypass content filtering |
| Model Poisoning | Attacker contaminates training data to influence model behavior | Attacker submits poisoned data to a model that learns from user feedback |
| Data Leakage | Model reveals training data, sensitive prompts, or system configuration | Attacker uses prompt engineering to extract PII from model responses |
| Excessive Agency | Model performs actions beyond its authorized scope due to plugin or tool access | Model autonomously executes a DELETE operation on a production database |
| Supply Chain for AI Models | Compromised pre-trained model, dataset, or dependency introduces backdoor or vulnerability | Attacker publishes a malicious model on a public hub that includes a backdoor trigger |
| Adversarial Input | Input designed to cause misclassification or unexpected behavior | Slightly perturbed image that causes a classifier to misidentify a stop sign |
| Model Inversion / Extraction | Attacker queries the model to reconstruct training data or replicate the model | Attacker makes thousands of API calls to extract model weights or training distribution |

#### AI Threat Model Checklist

When an AI component is in scope, the threat model additionally:
- Identifies the model's data sources (training, fine-tuning, RAG, user input) and their trust levels
- Maps the model's agency boundary: what can the model do without human approval?
- Assesses the model supply chain: pre-trained weights, fine-tuning datasets, model-serving infrastructure
- References [CERG-STD-AI-001] for detailed control requirements for each abuse case category

### 5.8 Facilitation Guide

#### Pre-Session Preparation

| **Activity** | **Timing** |
|---|---|
| Distribute inputs (diagrams, data classification, asset inventory, threat intelligence) | 5 business days before |
| Confirm participants (system owner, architect, security engineer) | 5 business days before |
| Pre-read threat intelligence per [CERG-PRC-TI-001](CERG-PRC-TI-001_Threat_Intelligence_Procedure.md) | 2 business days before |

#### Session Time-Boxing

| **Step** | **Activity** | **Time** |
|---|---|---|
| 1 | Define assets, data, scope | 30 min |
| 2 | Identify actors and entry points | 30 min |
| 3 | Generate abuse cases using STRIDE prompts | 60 min |
| 4 | Map existing controls | 30 min |
| 5 | Assess residual risk, assign severity | 30 min |
| 6 | Document findings, dispositions, control updates | 15 min |

#### Handling Disagreements

Disagreements during threat modeling indicate that a trust assumption or design decision needs clarification. The facilitator records disputed items, defaults to the higher severity when severity is disputed, and escalates to the Risk Pillar Leader for resolution if disagreements block session progress. Items are not allowed to derail the session; unresolved items are captured for follow-up.

#### Brainstorming Techniques

- **STRIDE prompts**: Use each category as a prompt per trust boundary
- **Attack trees**: Start with the attacker's goal and work backward
- **Kill chain mapping**: Map abuse cases to Recon → Weaponization → Delivery → Exploitation → Installation → C2 → Actions
- **"What if" scenarios**: "What if this API key is leaked? What if this admin account is compromised?"

#### Post-Session Activities

| **Activity** | **Timing** |
|---|---|
| Distribute draft threat model | 2 business days after session |
| Participants review | 5 business days |
| Finalize threat model | 10 business days |
| Enter findings in risk register per [CERG-PRC-RM-001](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | 3 business days after finalization |
| Archive with review record per [CERG-PRC-AR-001](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) | At finalization |

---

## 6. Outputs

Every completed threat model produces the following outputs.

| **Output** | **Description** | **Destination** |
|---|---|---|
| Threat model summary | Scope, date, participants, assumptions, diagrams reviewed, and high-level conclusion. | Project review record in [`CERG-PRC-AR-001`](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md). |
| Abuse-case table | Abuse cases, ATT&CK mappings, impacted assets, and disposition. | Project review record; reused in secure development. |
| Findings list | Specific design, control, or risk findings with owner and due date. | Architecture review action log. |
| Risk entries | Residual risks that are not remediated before go-live. | [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md). |
| Control updates | Needed changes to standards, baselines, detection, or evidence requirements. | Relevant document owner or control owner. |
| Detection leads | ATT&CK-informed detection ideas arising from the model. | Detection Engineer. |

> **The Output Is Not the Workshop Notes**
>
> Workshop notes are raw material. The output is the decision record. A project team should be able to read the final threat model and know exactly what must change, what risk remains, who owns each action, and what must be true before go-live. If the notes are interesting but the decisions are unclear, the model is unfinished.

---

## 7. Integration With Architecture Review

Threat modeling is embedded in Phase 2 of [`CERG-PRC-AR-001`](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md), not run as an unrelated side process.

| **Architecture Review Phase** | **Threat Modeling Role** |
|---|---|
| Phase 1, Intake | Determine whether threat modeling is required and set expected depth. |
| Phase 2, Architecture Review and Threat Model | Run this procedure; produce abuse cases and findings. |
| Phase 3, Build-Time Engagement | Validate that design-out and mitigation actions are implemented. |
| Phase 4, Pre-Production Security Review | Confirm unresolved threat-model findings are remediated or risk-accepted. |
| Phase 5, Production Handoff and Go-Live | Include residual threat-model findings in the handoff package and risk register. |

A go-live recommendation is not complete if required threat-model findings are unresolved and have no approved risk disposition.

---

## 8. Finding Severity and Treatment

Threat-model findings are scored using the risk and exception process in [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md). Severity considers both likelihood and impact, including the data classification from [`CERG-STD-DG-001`](../standards/CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md), the asset criticality from [`CERG-STD-AM-001`](../standards/CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md), and the system's regulatory scope.

A finding may be closed only when one of the following is true:

1. the design changed and the abuse case no longer applies;
2. a control was implemented and verified;
3. the finding was recorded as residual risk and accepted by the correct authority;
4. the finding was proven invalid by new evidence and the Threat Intelligence Analyst or Risk Pillar Leader agrees.

---

## 9. Scaling the Procedure

Threat modeling scales by depth, not by skipping accountability.

| **Project Type** | **Threat Model Depth** | **Minimum Participants** |
|---|---|---|
| Low-risk change with no new trust boundary | Lightweight review, checklist plus assumptions. | Threat Intelligence Analyst or Risk Pillar Leader, project technical lead. |
| Normal application or SaaS integration | Standard session, 60 to 90 minutes. | Threat Intelligence Analyst, Application Security Engineer or Cloud Security Engineer, project technical lead. |
| High-value, regulated, internet-facing, AI, or OT system | Full session, may require multiple workshops. | Risk Pillar Leader, Threat Intelligence Analyst, relevant Engineering role, relevant compliance manager, project technical lead. |
| Material post-incident redesign | Full session focused on the failed control path. | Risk Pillar Leader, Lead Investigator, relevant Engineering role, Risk Register Owner. |

A five-person team still performs all four depths. One person may hold multiple roles under [`CERG-GOV-RAC-001`](../governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md), but the record still names the canonical role responsible for each decision.

---

### 9.1 Quality Assurance

The Risk Pillar Leader is accountable for threat model quality. The following process ensures consistency and completeness.

#### Peer Review

All threat models receive a peer review by a second qualified analyst before finalization. The peer reviewer validates:

- All trust boundaries are identified and documented
- All data flows are mapped
- All STRIDE categories are considered per trust boundary
- All abuse cases have severity ratings and dispositions
- All deferred or accepted items have named owners and target dates
- The threat model references current threat intelligence from [CERG-PRC-TI-001](CERG-PRC-TI-001_Threat_Intelligence_Procedure.md)

#### Calibration Sessions

Quarterly calibration sessions are conducted using a sample threat model reviewed by all analysts. The purpose is to align severity ratings, ensure consistent abuse-case generation across analysts, and identify systematic gaps in the threat modeling process. The Risk Pillar Leader facilitates calibration and documents outcomes.

#### Quality Checklist

| **Check** | **Criteria** |
|---|---|
| Scope | System boundaries are clearly defined; out-of-scope items are documented with rationale |
| Assets | All data classifications and critical assets are identified |
| Diagrams | Context, data flow, network, identity, trust boundary diagrams are complete |
| Threats | All STRIDE categories are considered; abuse cases are specific and testable |
| Controls | Existing controls are mapped to each threat; control gaps are identified |
| Findings | All findings have severity, disposition, owner, and due date |
| Residual risk | Residual risk is assessed and documented; accepted risk has approval |

#### Escalation

Quality disputes that cannot be resolved between the analyst and peer reviewer are escalated to the Risk Pillar Leader for final determination.

---

## 10. Roles and Responsibilities

Roles below are canonical role names from [`CERG-GOV-OM-001`](../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1.

| **Role** | **Threat Modeling Responsibility** |
|---|---|
| **Risk Pillar Leader** | Accountable for this procedure and for the quality of threat-model outputs. Determines required depth for high-risk projects. |
| **Threat Intelligence Analyst** | Facilitates most threat models; supplies threat actor, campaign, and ATT&CK context; records abuse cases and ATT&CK mappings. |
| **Application Security Engineer** | Supplies application security context; ensures findings feed secure development gates. |
| **Cloud Security Engineer** | Supplies cloud, SaaS, network, and platform context for cloud-based systems. |
| **Identity Engineer** | Supplies identity, privilege, federation, token, and access-path context. |
| **OT Risk Analyst** | Supplies OT threat context and ATT&CK for ICS mapping where OT is in scope. |
| **OT Security Engineer** | Supplies OT architecture and boundary-control context where OT is in scope. |
| **Vendor Risk Analyst** | Supplies third-party and supply chain context for vendor integrations. |
| **Detection Engineer** | Receives detection leads arising from threat models and translates them into detection backlog items where in scope. |
| **Risk Register Owner** | Ensures residual risk from threat-model findings is recorded and tracked. |
| **Governance Pillar Leader** | Ensures regulated-scope implications are captured and evidence requirements are identified. |
| **Pre-production Reviewer** | Confirms threat-model findings are remediated or risk-accepted before go-live. |

---

## 11. Metrics

| **KPI** | **Formula** | **Source** | **Refresh** | **Green** | **Amber** | **Red** |
|---|---|---|---|---|---|---|
| Threat models completed | Count of threat models finalized | Threat model repository | Quarterly | Baseline Y1 | | |
| Average time per threat model | Mean calendar days from session to finalization | Threat model tracker | Quarterly | ≤ 15 days | 16–20 days | > 20 days |
| Findings designed out | % of findings with disposition "Designed Out" vs. "Accepted" | Threat model repository | Quarterly | ≥ 40% | 20–39% | < 20% |
| Deferred findings past due | Count of deferred findings with past-due target dates | Risk register | Monthly | 0 | 1–3 | > 3 |
| Recurrence rate | % of findings that recur in subsequent threat models for the same system | Threat model repository | Annually | ≤ 10% | 11–25% | > 25% |
| Threat model coverage rate | % of in-scope systems (per PRC-AR-001 Section 4.1) with current threat models | Asset inventory + TM repo | Quarterly | ≥ 90% | 75–89% | < 75% |

> Baseline: "Baseline Y1" indicates the metric is collected for 12 months before Green/Amber/Red thresholds are established.

---

## 12. Regulatory and Framework Alignment Summary

| **Regulation / Framework** | **Reference** | **Where in This Procedure** |
|---|---|---|
| NIST 800-53r5 | RA-3, RA-5, SA-8, SA-11, PL-8, SC family | Sections 3, 5, 6, 8 |
| NIST 800-160 | Systems security engineering and design-time risk analysis | Sections 5, 7 |
| NIST SSDF | PW.1, PW.2, RV.1, RV.2 | Sections 5, 7, 8 |
| MITRE ATT&CK | Technique-informed adversary behavior | Sections 5, 6 |
| MITRE ATT&CK for ICS | OT and ICS threat behavior | Sections 5, 10 |
| OWASP ASVS | Application security verification context | Sections 5, 8 |
| CMMC L2 / NIST 800-171r3 | Security assessment and risk assessment practices | Sections 3, 8 |
| NERC-CIP | Design implications for BES Cyber System scope and boundary controls | Sections 3, 5, 10 |
| SOX ITGC | Change-risk analysis for financially relevant systems | Sections 7, 8 |

---


---

## Appendix A: Threat Model Template

```
THREAT MODEL - TM-YYYY-NNNN

1. SYSTEM OVERVIEW
   System Name:
   System Owner:
   Data Classification(s):
   Regulatory Scope (CUI / SOX / NERC-CIP / None):
   Environment (IT / Cloud / SaaS / OT):
   Architecture Review Reference (AR-YYYY-NNNN):

2. SCOPE AND BOUNDARIES
   In Scope:
   Out of Scope (with rationale):
   Trust Boundaries:
     - [Boundary Name]: [between X and Y]

3. DATA FLOW DIAGRAM
   [Pending — create a data flow diagram (DFD) for the system under review. The diagram should identify all system components, external entities, data stores, and data flows with direction labels. Store in the `threat-model-diagrams/` directory alongside this threat model document. Recommended formats: Draw.io (.drawio), Excalidraw (.excalidraw), or Lucidchart exported as PDF. See CERG PRC-TM-001 §3.1 for minimum diagram requirements.]

4. TRUST BOUNDARY DIAGRAM
   [Pending — create a trust boundary diagram identifying all trust boundaries between system components, processes, and external entities. Highlight boundaries where data crosses between different trust levels (e.g., Internet ↔ DMZ, DMZ ↔ Internal, Internal ↔ OT, SaaS provider ↔ On-prem). Store in the `threat-model-diagrams/` directory. See CERG PRC-TM-001 §3.2 for minimum diagram requirements.]

5. ASSET INVENTORY
   | Asset | Classification | Owner | Environment |
   |---|---|---|---|
   | | | | |

6. ABUSE CASES
   | ID | Threat Actor | Abuse Case | STRIDE | ATT&CK | Severity | Disposition |
   |---|---|---|---|---|---|---|
   | TM-001 | | | | | | |

   Disposition values: Designed Out / Mitigated / Transferred / Accepted / Deferred

7. FINDINGS
   | ID | Description | Severity | Disposition | Owner | Due Date |
   |---|---|---|---|---|---|
   | | | | | | |

8. CONTROL UPDATES REQUIRED
   | Control ID (CB-001) | Current State | Required State | Owner | Due Date |
   |---|---|---|---|---|
   | | | | | |

9. RESIDUAL RISK
   [Summary of residual risk after controls; link to risk register entries]

10. SIGN-OFF
    Threat Modeling Facilitator: [name, date]
    Peer Reviewer: [name, date]
    Risk Pillar Leader: [name, date]
```

## 13. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-PRC-TM-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Effective Date** | 2026-05-22 |
| **Classification** | Public |
| **Owner** | Risk Pillar Leader |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on material change to architecture review or threat modeling methods |
| **Next Scheduled Review** | 2027-05-22 |
| **Frameworks** | NIST 800-53r5 (RA, SA, PL, SC); NIST 800-160; NIST SSDF; MITRE ATT&CK; MITRE ATT&CK for ICS; OWASP ASVS |
| **Regulations** | CMMC L2 / 800-171r3; NERC-CIP; SOX ITGC where applicable |
| **Environments** | All projects subject to CERG architecture review and material changes to in-scope systems |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 Draft | 2026-05-22 | Cyber Risk | Initial release. Establishes the procedure for threat modeling during architecture review, including triggers, inputs, a practical hybrid method using abuse cases and MITRE ATT&CK mapping, required outputs, integration with CERG-PRC-AR-001, finding treatment, scaling guidance, and canonical role responsibilities. |

### Review Triggers

- Change to [`CERG-PRC-AR-001`](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md)
- Change to the CERG secure development or AI security standards
- Revision to MITRE ATT&CK, MITRE ATT&CK for ICS, NIST SSDF, or relevant NIST 800-53 controls
- Significant incident showing threat-modeling gaps
- Direction from the CISO

Cyber Risk owns this document. The Risk Pillar Leader is responsible for initiating reviews, managing the revision cycle, and obtaining Governance Pillar Leader approval, with CISO endorsement, for all changes.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| CERG Operating Model | [`CERG-GOV-OM-001`](../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) | Establishes the pillar handoff and canonical roles |
| Architecture Review and Project Intake Procedure | [`CERG-PRC-AR-001`](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) | Threat modeling is Phase 2 input and output |
| Unified Control Baseline | [`CERG-GOV-CB-001`](../governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) | Control requirements considered during modeling |
| Secure Software Development and Application Security Standard | [`CERG-STD-SDL-001`](../standards/CERG-STD-SDL-001_Secure_Software_Development_and_Application_Security_Standard.md) | Threat-model findings feed secure development gates |
| Artificial Intelligence Security Standard | [`CERG-STD-AI-001`](../standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md) | AI-specific threat classes and required modeling |
| Risk Register and Exception Process | [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Residual threat-model findings are recorded and treated |
| Data Governance and Classification Standard | [`CERG-STD-DG-001`](../standards/CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md) | Data classification input |
| Asset Management and Inventory Standard | [`CERG-STD-AM-001`](../standards/CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md) | Asset criticality input |
| Consolidated Roles, Responsibilities, and RACI Instrument | [`CERG-GOV-RAC-001`](../governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) | Scaling and role accountability reference |
| Document Catalog and Naming Convention | [`CERG-GOV-CAT-001`](../governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Registers this artifact and the `TM` domain |
