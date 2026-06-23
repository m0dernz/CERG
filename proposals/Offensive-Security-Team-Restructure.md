Proposal: Offensive Security Team Restructure

TypeChange Proposal / RFC (for discussion)StatusDraft - seeking maintainer feedbackAuthorMason (GitHub: Cytax65)Affects pillarRiskPrimary documents touchedCERG-PRC-AV-001, CERG-PRC-TM-001, CERG-GOV-FRM-001, CERG-GOV-JD-RISKOPS-002, CERG-GOV-RAC-001, CERG-GOV-CAT-001, cerg-org-profile.ymlNatureStructural (workforce + scope), plus two small procedure additions


1. Summary

This proposal formalizes a standing, in-house Offensive Security function within the Risk pillar. It keeps CERG's existing separation of Adversarial Testing from Exposure Management, and builds the Adversarial Testing function out into a complete team with its own management layer, a coordination role, an individual-contributor career ladder, and an expanded scope that includes threat modeling.

Two parts are intended for different destinations:


Generic model improvements (Sections 4-6, 8A) are offered as candidates to upstream into CERG, because they fill real gaps in the current model.
Organization-specific establishment (Section 7) is our own headcount and grade selection, recorded in our org profile, not proposed for the upstream framework.


2. How CERG handles this today

CERG already separates the two offensive-adjacent functions as peer roles under the Risk Pillar Leader: the Exposure Management Lead (CERG-GOV-JD-RISKOPS-001) owns scanning and remediation tracking, and the Adversarial Testing Lead (CERG-GOV-JD-RISKOPS-002) owns pen testing, red team, and purple team via the Adversarial Validation Procedure (CERG-PRC-AV-001). The reference establishment in CERG-GOV-FRM-001 Section 9 allocates three combined "Penetration Testing and Red Team" analysts within a roughly fifteen-person Risk pillar.

So the split we want already exists. This proposal does not re-split anything; it defines the function as a fully staffed team and resolves several points the current model leaves implicit.

3. Current state in our organization

Today our offensive work is fragmented: a pen test group of four (including its manager), a separate red team of two to three, and external contractors performing much of the actual test execution. We are consolidating these into one in-house team and insourcing the contractor-performed execution, retaining contractors only for genuinely niche specialties.

4. Proposed structure

A single Offensive Security team within the Risk pillar. The team manager reports to the Risk Pillar Leader (CERG-GOV-JD-RISKOPS-008).

RoleGradeNotesTeam LeadM1 (Manager)People manager for the function. Reports to Risk Pillar Leader.Sr. Advisor Testing LeadS4 (Sr. Advisor)Senior technical authority and deepest tester.Technical Project Manager(coordination role)Owns intake pipeline, scheduling, documentation gathering, and estimate drafting.Penetration Tester (Principal) x2S3 (Advisor)Senior testers; lead engagements.Penetration Tester (Mid) x2S2 (Sr. Specialist)Core testers.Penetration Tester (Junior) x2S1 (Specialist)Early-career; pair on engagements (no solo OT work).

Total: nine. Individual contributors carry the role title "Penetration Tester"; grade is the level, consistent with CERG-GOV-JA-001's separation of role title from grade title.

Skill requirement: at least one of the two Principal (S3) testers must hold demonstrated red team experience (adversary emulation, evasion and OPSEC, command-and-control tradecraft). This is a hard hiring criterion, because pen testing competence does not automatically confer red team competence.

5. Scope of the function

One coherent team that performs, in-house:


Penetration testing (network, web and application, cloud)
Red team operations and purple team detection validation
OT and grid adversarial assessment (the core of our risk)
Threat modeling (see Section 6)


Niche specialties within OT (for example RF and radio testing) are contracted on a per-need basis, because holding those rare skills on staff full-time is not cost-effective. This keeps CERG-PRC-AV-001 Section 2.1 (external tester management) relevant but scoped to niche engagements only, and warrants a relaxation of the three-year vendor-rotation rule where the qualified pool is small.

6. Threat modeling ownership

This team owns threat modeling (CERG-PRC-TM-001). Engineering does not perform threat modeling; Engineering performs architecture review and consumes the threat-model output. This is broadly consistent with CERG, which already treats threat modeling as a Risk-side activity feeding Engineering's architecture review. The change is to pin ownership explicitly to this Offensive Security team.

7. Sizing rationale (organization-specific)

We size by demand, per CERG-GOV-WFP-001 Section 6.2, not by an org-chart ratio.

Our capacity target is two concurrent grid (OT) penetration tests, and potentially those two plus one external web test, sustained continuously alongside red team and purple cycles and NERC-CIP-mandated testing. That program sits in the top WFP band. Because pure execution of three concurrent engagements needs only about three hands, the surplus in a six-IC team is the pipeline: scoping, report writing, retest, and purple work that run alongside live tests. Folding in red team (already offensive headcount) and insourcing contractor execution justifies the build, and threat-modeling ownership and multi-week red team campaigns both argue that nine is the floor rather than the ceiling.

This headcount and grade selection is recorded in our org profile and is not proposed for the upstream reference model.

8. Proposed document changes

8A. Generic (candidates to upstream)


Split the single Adversarial Testing Lead (CERG-GOV-JD-RISKOPS-002) into two roles: an M1 Team Lead (people management) and an S4 Sr. Advisor Testing Lead (technical authority), for organizations large enough to separate them.
Add a "Penetration Tester" individual-contributor job description spanning S1 to S3, with the red team experience requirement on one Principal (S3) seat.
Add a "Technical Project Manager" job description for the intake, scheduling, documentation, and estimate-drafting function.
CERG-PRC-AV-001 additions: (a) an OT Safety Officer concurrency condition - one officer may cover two simultaneous OT tests only when they are co-located or in a shared coordinated window, otherwise one officer per test; (b) a niche-specialty contracting provision within OT, with a vendor-rotation relaxation clause.
CERG-PRC-TM-001, CERG-GOV-FRM-001 Section 2.3, and CERG-GOV-RAC-001: record that the Offensive Security function owns threat modeling and that Engineering does not perform it.


8B. Organization-specific (stays on our fork)


Encode the nine-person establishment and grade mapping in cerg-org-profile.yml and our adaptation profile, justified by the WFP-001 demand band.


Plumbing for any change

Register new document IDs in CERG-GOV-CAT-001, regenerate the machine-readable mirrors and the LLM index, and pass tools/cerg-validate.py with zero errors.
