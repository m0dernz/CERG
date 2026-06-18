
# SURGE: Cyber Engineering, Risk & Governance

## ARTIFICIAL INTELLIGENCE SECURITY STANDARD
### AI Governance · Acceptable Use · Model and Data Risk · Prompt Injection · Shadow AI

---

| | |
|---|---|
| **Document ID** | CERG-STD-AI-001 |
| **Version** | 1.1 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Engineering Pillar Leader (Application Security) |
| **Parent Policy** | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Standards** | [`CERG-STD-DG-001`](CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md) · [`CERG-STD-SDL-001`](CERG-STD-SDL-001_Secure_Software_Development_and_Application_Security_Standard.md) · [`CERG-STD-IT-001`](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) · [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md) · [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) |
| **Supporting Templates** | [`CERG-TMPL-AI-001`](../templates/CERG-TMPL-AI-001_AI_Intake_and_Sanctioning_Template.md) · [`CERG-TMPL-AI-002`](../templates/CERG-TMPL-AI-002_Sanctioned_AI_Tools_Register_Template.md) · [`CERG-TMPL-AI-003`](../templates/CERG-TMPL-AI-003_AI_System_and_Model_Register_Template.md) |
| **Review Cycle** | Annual / On material change to AI use or AI regulation |
| **Frameworks** | [NIST AI RMF 100-1](https://www.nist.gov/itl/ai-risk-management-framework) · [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) · ISO/IEC 42001 |
| **Regulations** | CMMC L2 / 800-171r3 (where AI processes CUI) · SOX ITGC (where AI supports financial processes) · privacy regimes where applicable |
| **Environments** | All CERG-managed use of AI systems: third-party AI services, embedded AI features, and in-house AI applications |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Principles](#2-principles)
3. [AI Use Categories](#3-ai-use-categories)
4. [Acceptable Use of AI](#4-acceptable-use-of-ai)
5. [Data and AI](#5-data-and-ai)
6. [In-House and Embedded AI Systems](#6-in-house-and-embedded-ai-systems)
7. [AI-Specific Threats](#7-ai-specific-threats)
8. [Third-Party AI Services](#8-third-party-ai-services)
9. [Shadow AI](#9-shadow-ai)
10. [Roles and Responsibilities](#10-roles-and-responsibilities)
11. [Regulatory and Framework Alignment Summary](#11-regulatory-and-framework-alignment-summary)
12. [Document Control](#12-document-control)

---

## 1. Purpose and Scope

This standard defines security requirements for AI systems, AI-enabled SaaS, and built AI features within the CERG operating model.

**Integration points.** This standard does not stand alone. AI risk is managed through the following cross-references:
- **Vendor risk** — AI-enabled SaaS and AI vendor assessments follow PRC-TPRM-001, supplemented by AI-specific assessment criteria in this standard.
- **Threat modeling** — AI-specific threats (prompt injection, model extraction, data poisoning, excessive agency) are modeled using PRC-TM-001 with the AI abuse case categories in PRC-TM-001 §5.6.1.
- **Detection** — AI-specific detection rules (model behavior anomalies, prompt injection patterns, data exfiltration via model API) are defined in STD-LM-001 and referenced from the control overlay in CB-001 §8.
- **Evidence** — Model cards, training data provenance, and AI-specific controls are evidenced per CB-001 §4.1 evidence tier requirements.

The AI Overlay in CB-001 §8 defines which baseline controls are tightened or augmented for AI scope.
Artificial intelligence entered the organization faster than any technology before it, and it entered mostly without asking. Employees use AI assistants. Vendors embed AI features into software already in use. Teams build applications on top of AI models. Each of these creates security exposure that none of the existing CERG standards squarely owns: data leaving the organization in a prompt, decisions made by a model no one validated, an application vulnerable to attacks that did not exist three years ago.

This standard establishes the requirements for the secure use of AI across CERG-managed environments: acceptable use, how data and AI interact, the security of in-house and embedded AI systems, the AI-specific threats the program must defend against, the assessment of third-party AI services, and the control of unsanctioned AI use.

It applies to every use of AI by CERG-managed teams and systems: third-party AI services and assistants, AI features embedded in other software, and AI applications the organization builds itself. It is technology-neutral and is written to survive the rapid change in the AI field.

> **AI Is Not Exempt From the Rest of CERG**
>
> An AI system is software. It runs on infrastructure, it processes data, it is accessed by identities, and it is built by developers. Everything CERG already requires still applies: an in-house AI application is governed by the secure development standard, the data it touches is governed by the data governance standard, its access is governed by the access standard. This standard does not replace those. It adds the requirements that are genuinely specific to AI, and it makes explicit that AI does not get a pass on the requirements that already exist.

---

## 2. Principles

1. **AI use is sanctioned use.** AI is used through services and tools the program has assessed and approved. Unsanctioned AI is shadow IT and is treated as such (Section 9).
2. **A prompt is an export.** Data placed into an AI system, especially a third-party one, has left the organization's control boundary as surely as if it were emailed out. It is governed by the data classification scheme.
3. **AI output is reviewed, not trusted.** AI output can be wrong, biased, or manipulated. A human reviews AI output before it is used for a consequential decision. Accountability for the decision stays with the human.
4. **AI does not decide alone where it matters.** An AI system does not make a final consequential decision, about a person, a safety action, a control system, without a human in the loop.
5. **AI risk is assessed before adoption.** An AI service or AI feature is risk-assessed before it is used, like any other technology, and reassessed as its capability changes.
6. **The same rules scale.** A five-person team and a sixty-person team both sanction AI tools, classify what goes into them, and review what comes out. The rigor scales; the principles do not.

---

## 3. AI Use Categories

CERG governs three categories of AI use. The requirements differ by category.

| **Category** | **What It Is** | **Primary Governing Sections** |
|---|---|---|
| **Consumed AI services** | Third-party AI assistants and services used as tools: chat assistants, coding assistants, content tools. | Sections 4, 5, 8, 9 |
| **Embedded AI** | AI features built into other software the organization already uses. | Sections 5, 7, 8 |
| **Built AI** | AI applications and integrations the organization develops itself, including systems built on third-party models. | Sections 5, 6, 7 |

---

## 4. Acceptable Use of AI

1. **Use sanctioned AI tools.** Employees use the AI services and tools the program has assessed and approved. The list of sanctioned AI tools is maintained by Governance using [`CERG-TMPL-AI-002`](../templates/CERG-TMPL-AI-002_Sanctioned_AI_Tools_Register_Template.md) or an equivalent local register and is visible to staff.
2. **Classify before you prompt.** Before data is placed into an AI tool, the user considers its classification per [`CERG-STD-DG-001`](CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md). Section 5 governs what may go where.
3. **Review AI output before relying on it.** AI-generated content, code, analysis, or recommendations are reviewed by a competent person before being used. AI-generated code additionally passes the gates in [`CERG-STD-SDL-001`](CERG-STD-SDL-001_Secure_Software_Development_and_Application_Security_Standard.md); AI is not an exception to code review.
4. **Do not use AI to make prohibited decisions unaided.** AI does not unilaterally make decisions about employment, safety, control system operation, or anything else where Principle 4 applies.
5. **Attribute and disclose where required.** Where a regulator, a contract, or a customer requires disclosure that AI was used, that disclosure is made.

---

## 5. Data and AI

This section applies the data classification scheme to AI use. It is the most important operational section of the standard.

1. **A prompt to a third-party AI service is treated as external sharing.** Placing data into a consumed AI service is governed by the external-sharing rules of [`CERG-STD-DG-001`](CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md) §6.
2. **Classification limits on AI input:**
   - **Public and Internal data** may be placed into sanctioned AI tools.
   - **Confidential data** may be placed only into AI services that have been assessed and approved for Confidential data, with contractual assurance that input is not used to train the provider's models and is handled to the program's bar.
   - **Restricted data**, including CUI and BES Cyber System Information, is not placed into a third-party AI service unless that service is explicitly authorized for that regulated category and an authorization is recorded. For CUI this means the service satisfies [`CERG-STD-CUI-001`](CERG-STD-CUI-001_CUI_Handling_Standard.md).
3. **Training data is classified data.** Data used to train, fine-tune, or ground an in-house or embedded AI system carries its classification, and the resulting model is treated as carrying the classification of its most sensitive training data.
4. **AI interactions are logged where they touch sensitive data.** Use of AI systems that process Confidential or Restricted data is logged per [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md).

> **The Prompt Is the Leak**
>
> The most common AI security failure is mundane: an employee pastes a sensitive document into a public AI assistant to summarize it. The data is now on a third party's infrastructure, possibly used to train a model, possibly retained indefinitely, and entirely outside the organization's control. No model was hacked. No clever attack occurred. Someone simply typed. CERG governs AI primarily by governing what goes into the prompt, because the prompt is where the data actually leaves.

---

## 6. In-House and Embedded AI Systems

An AI application the organization builds is software and is fully governed by [`CERG-STD-SDL-001`](CERG-STD-SDL-001_Secure_Software_Development_and_Application_Security_Standard.md). In addition:

1. **AI applications go through architecture review.** An AI application or integration is subject to project intake and architecture review per [`CERG-PRC-AR-001`](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md), with the AI-specific threats in Section 7 explicitly in scope of the threat model.
2. **The model is an inventoried component.** A model, whether trained in-house or a third-party model the application depends on, is a component recorded in the asset inventory per [`CERG-STD-AM-001`](CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md), the AI system and model register using [`CERG-TMPL-AI-003`](../templates/CERG-TMPL-AI-003_AI_System_and_Model_Register_Template.md) or an equivalent local record, and, where applicable, in the software bill of materials per [`CERG-STD-SDL-001`](CERG-STD-SDL-001_Secure_Software_Development_and_Application_Security_Standard.md) §8.
3. **Model provenance is known.** The source of any third-party or open model used is known and trusted. A model from an unverified source is a supply chain risk.
4. **AI applications enforce least privilege.** An AI system, and any agent or tool-using capability it has, operates with the least privilege required. An AI agent does not run with broad standing access on the assumption it will behave.
5. **AI output that triggers action is bounded.** Where an AI system can trigger an action, send a message, change a record, call an API, the actions it can take are constrained and high-consequence actions require human confirmation.

---

## 7. AI-Specific Threats

CERG-built and embedded AI systems are designed and tested against the AI-specific threat classes below, aligned to the OWASP Top 10 for LLM Applications. These threats are explicitly in scope of the threat model required by [`CERG-STD-SDL-001`](CERG-STD-SDL-001_Secure_Software_Development_and_Application_Security_Standard.md).

| **Threat** | **What It Is** | **Required Mitigation Direction** |
|---|---|---|
| Prompt injection | Untrusted input manipulates the model into ignoring its instructions or acting maliciously. | Treat all model input as untrusted; separate instructions from data; constrain what the model can do. |
| Sensitive information disclosure | The model reveals sensitive data from its training, context, or another user's session. | Control what data reaches the model; isolate sessions; filter output. |
| Insecure output handling | Downstream systems trust model output as if it were safe code or commands. | Treat model output as untrusted input to anything downstream; validate and encode it. |
| Excessive agency | An agent or tool-using model is granted more capability than needed and is induced to misuse it. | Least privilege for the model; bound and confirm consequential actions (Section 6). |
| Training-data and model poisoning | Tampered training data or a tampered model produces attacker-influenced behavior. | Known model provenance; control and classify training data; validate model integrity. |
| Supply chain risk in the model stack | A compromised model, dataset, or AI library enters the system. | Assess models and AI dependencies like any other component (Sections 6, 8). |

---

## 8. Third-Party AI Services

1. **AI services are assessed before adoption.** A consumed AI service or an AI-enabled vendor feature is risk-assessed before use through [`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) and recorded through [`CERG-TMPL-AI-001`](../templates/CERG-TMPL-AI-001_AI_Intake_and_Sanctioning_Template.md) or an equivalent local intake. The assessment covers, at minimum: what the provider does with input data, whether input trains the provider's models, data retention and location, and the provider's own security posture.
2. **Embedded AI features are assessed when they appear.** A vendor adding an AI feature to existing software is a material change to that vendor's risk profile and triggers reassessment. AI features that arrive silently in an update are caught by the reassessment cadence in [`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md).
3. **Approval is by data classification.** A service is approved for a maximum data classification per Section 5. Approval for Internal use is not approval for Confidential or Restricted use.
4. **The sanctioned list is maintained.** The outcome of assessment is the sanctioned AI tools list, maintained using [`CERG-TMPL-AI-002`](../templates/CERG-TMPL-AI-002_Sanctioned_AI_Tools_Register_Template.md) or an equivalent local register, which states each tool and the maximum classification it is approved for.

---

## 9. Shadow AI

Shadow AI is the use of AI services that the program has not assessed or approved. It is the dominant AI risk in most organizations.

1. **Shadow AI is shadow IT.** Unsanctioned AI use is treated as unsanctioned technology under [`CERG-STD-IT-001`](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md). It is discovered, assessed, and then either sanctioned or stopped.
2. **Discovery looks for it.** The program actively looks for unsanctioned AI use, through network and SaaS discovery and through expense and procurement signals. AI use that is invisible cannot be governed.
3. **The response is a path to sanctioned use, not only a block.** When shadow AI is found, the program assesses whether the underlying need can be met by a sanctioned tool and provides one. A pure block with no sanctioned alternative drives the use further underground. This is the "yes, and..." model of [`CERG-GOV-FRM-001`](../governance/CERG-GOV-FRM-001_CERG_Framework.md) applied to AI: enable the need, on safe ground.
4. **Repeated or high-risk shadow AI is a risk register entry.** A pattern of shadow AI, or a single instance involving Confidential or Restricted data, is recorded and tracked per [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md).

> **Banning AI Does Not Work. Governing It Does.**
>
> An organization that responds to AI by banning it does not eliminate AI use; it eliminates its visibility into AI use. Employees who see a genuine productivity gain will use AI on personal devices and personal accounts, where the organization has no assessment, no contract, and no control at all. The defensible position is the CERG position everywhere else: provide sanctioned tools that meet a real need, govern what data goes into them, and treat the unsanctioned use that remains as a finding to be brought into the light.

---

## 10. Roles and Responsibilities

Roles below are the canonical role names from [`CERG-GOV-OM-001`](../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1.

| **Role** | **AI Security Responsibility** |
|---|---|
| **Application Security Engineer** | Owns this standard. Owns AI threat modeling, the security of built and embedded AI systems, the AI system and model register, and the AI-specific gate content in secure development. |
| **Engineering Pillar Leader** | Accountable for AI security across the pillar; owns architecture review of AI applications. |
| **Governance Pillar Leader** | Owns AI intake and sanctioning, the sanctioned AI tools list, the acceptable-use position, and AI governance reporting. |
| **Vendor Risk Analyst** | Assesses third-party AI services and AI-enabled vendor features per [`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md). |
| **Cloud Security Engineer** | Owns discovery of shadow AI through SaaS and network signals. |
| **Detection Engineer** | Owns detection content for shadow AI use and for anomalous AI-system behavior. |
| **Policy & Standards Manager** | Maintains this document; maintains the sanctioned AI tools list as a living reference. |
| **CMMC / Federal Compliance Manager** | Confirms AI use touching CUI satisfies [`CERG-STD-CUI-001`](CERG-STD-CUI-001_CUI_Handling_Standard.md). |
| **Risk Register Owner** | Records shadow AI and AI-risk findings in the register. |

---

## 11. Regulatory and Framework Alignment Summary

| **Regulation / Framework** | **Reference** | **Where in This Standard** |
|---|---|---|
| NIST AI RMF 100-1 | Govern, Map, Measure, Manage functions | Sections 2, 6, 7, 8 |
| OWASP Top 10 for LLM Applications | LLM01-LLM10 risk categories | Section 7 |
| NIST 800-53r5 | RA-3 (risk assessment), SA-family (system and services acquisition), AC-family | Sections 6, 8 |
| ISO/IEC 42001 | AI management system | Sections 2, 4, 9 |
| NIST 800-171r3 / CMMC L2 | Where AI processes CUI | Section 5 |
| SOX ITGC | Where AI supports financial processes | Sections 4, 6 |

---

## 12. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-STD-AI-001 |
| **Version** | 1.1 |
| **Status** | Approved |
| **Effective Date** | 2026-06-17 |
| **Classification** | Public |
| **Owner** | Engineering Pillar Leader (Application Security) |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on material change to AI use or AI regulation |
| **Next Scheduled Review** | 2027-05-21 |
| **Frameworks** | NIST AI RMF 100-1; NIST 800-53r5; OWASP Top 10 for LLM Applications; ISO/IEC 42001 |
| **Regulations** | CMMC L2 / 800-171r3 where applicable; SOX ITGC where applicable; privacy regimes where applicable |
| **Environments** | All CERG-managed use of AI systems |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.1 | 2026-06-17 | Cyber Engineering | Added references to the AI intake and sanctioning template, sanctioned AI tools register, and AI system and model register as the operational records that implement AI governance. |
| 1.0 | 2026-05-21 | Cyber Engineering | Initial release. Establishes three AI use categories, acceptable use of AI, the data-classification limits on AI input (a prompt is an export), security requirements for in-house and embedded AI, the AI-specific threat set aligned to the OWASP LLM Top 10, third-party AI service assessment, and the governance of shadow AI through a path to sanctioned use rather than a pure block. |

### Review Triggers

- Material change to how the organization uses AI
- New or changed AI regulation
- Revision of the NIST AI Risk Management Framework or the OWASP LLM Top 10
- A significant AI-related security incident
- Direction from the CISO

Cyber Engineering owns this document. The Engineering Pillar Leader (Application Security) is responsible for initiating reviews, managing the revision cycle, and obtaining Governance Pillar Leader approval, with CISO endorsement, for all changes.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| Data Governance and Classification Standard | [`CERG-STD-DG-001`](CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md) | Classification scheme that governs AI input |
| Secure Software Development and Application Security Standard | [`CERG-STD-SDL-001`](CERG-STD-SDL-001_Secure_Software_Development_and_Application_Security_Standard.md) | Built and embedded AI systems are governed software |
| IT / Cloud / SaaS Security Standard | [`CERG-STD-IT-001`](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md) | Shadow AI treated as shadow IT |
| Access Management Standard | [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md) | Least privilege for AI systems and agents |
| Logging, Monitoring, and Detection Standard | [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) | Logging of AI use touching sensitive data; shadow-AI detection |
| Asset Management and Inventory Standard | [`CERG-STD-AM-001`](CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md) | Models as inventoried components |
| CUI Handling Standard | [`CERG-STD-CUI-001`](CERG-STD-CUI-001_CUI_Handling_Standard.md) | AI use touching CUI |
| Architecture Review and Project Intake Procedure | [`CERG-PRC-AR-001`](../procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) | Architecture review of AI applications |
| Third-Party and Supply Chain Risk Procedure | [`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) | Assessment of third-party AI services |
| Risk Register and Exception Process | [`CERG-PRC-RM-001`](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Shadow AI and AI-risk findings |
| AI Intake and Sanctioning Template | [`CERG-TMPL-AI-001`](../templates/CERG-TMPL-AI-001_AI_Intake_and_Sanctioning_Template.md) | Intake and approval record for proposed AI use |
| Sanctioned AI Tools Register Template | [`CERG-TMPL-AI-002`](../templates/CERG-TMPL-AI-002_Sanctioned_AI_Tools_Register_Template.md) | Operational register for approved AI tools and data-classification limits |
| AI System and Model Register Template | [`CERG-TMPL-AI-003`](../templates/CERG-TMPL-AI-003_AI_System_and_Model_Register_Template.md) | Inventory record for built and embedded AI systems, models, data sources, and agency boundaries |
| Document Catalog and Naming Convention | [`CERG-GOV-CAT-001`](../governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Registers this artifact and the `AI` domain |
