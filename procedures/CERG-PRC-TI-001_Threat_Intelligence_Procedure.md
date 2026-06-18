1|1|# SURGE: Cyber Engineering, Risk & Governance
2|2|
3|3|## THREAT INTELLIGENCE PROCEDURE
4|4|### Sources · Intake · Relevance · Dissemination · Action Tracking · Program Reprioritization · External Collaboration
5|5|
6|6|---
7|7|
8|8|| | |
9|9||---|---|
10|10|| **Document ID** | CERG-PRC-TI-001 |
11|11|| **Version** | 1.1 |
12|12|| **Status** | Approved |
13|13|| **Classification** | Public |
14|14|| **Owner** | Risk Pillar Leader |
15|15|| **Parent Policy** | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
16|16|| **Supporting Documents** | [`CERG-GOV-OM-001`](../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) · [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Exposure_Management_Procedure.md) · [`CERG-PRC-TM-001`](CERG-PRC-TM-001_Threat_Modeling_Procedure.md) · [`CERG-PRC-TPRM-001`](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) · [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) · [`CERG-STD-LM-001`](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) · [`CERG-PRC-LL-001`](CERG-PRC-LL-001_Lessons_Learned_and_Program_Improvement_Procedure.md) · [`CERG-GOV-IMPREG-001`](../governance/CERG-GOV-IMPREG-001_Program_Improvement_Register.md) · [`CERG-GOV-CAL-001`](../governance/CERG-GOV-CAL-001_Annual_Security_and_Governance_Calendar.md) |
17|17|| **Review Cycle** | Annual / On material change to threat landscape or intelligence sources |
18|18|| **Frameworks** | [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) (RA-3, RA-5, SI-5, PM-16) · [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (ID.RA, DE.CM, ID.IM, GOVERN) · [MITRE ATT&CK](https://attack.mitre.org/) · [MITRE ATT&CK for ICS](https://attack.mitre.org/matrices/ics/) |
19|19|| **Regulations** | CMMC L2 / 800-171r3 · NERC-CIP · SOX ITGC where threat intelligence affects scoped systems |
20|20|| **Environments** | All CERG-managed environments and risk decisions informed by threat intelligence |
21|21|
22|22|---
23|23|
24|24|## Table of Contents
25|25|
26|26|1. [Purpose and Scope](#1-purpose-and-scope)
27|27|2. [Principles](#2-principles)
28|28|3. [Intelligence Sources](#3-intelligence-sources)
29|29|4. [Intake and Triage](#4-intake-and-triage)
30|30|5. [Relevance and Priority](#5-relevance-and-priority)
31|31|6. [Products and Dissemination](#6-products-and-dissemination)
32|32|7. [Action Tracking](#7-action-tracking)
33|33|8. [Integration With CERG Processes](#8-integration-with-cerg-processes)
34|34|9. [Intelligence-Driven Program Reprioritization](#9-intelligence-driven-program-reprioritization)
35|35|10. [External Collaboration and Information Sharing](#10-external-collaboration-and-information-sharing)
36|36|11. [Metrics](#11-metrics)
37|37|12. [Roles and Responsibilities](#12-roles-and-responsibilities)
38|38|13. [Regulatory and Framework Alignment Summary](#13-regulatory-and-framework-alignment-summary)
39|39|14. [Document Control](#14-document-control)
40|40|
41|41|---
42|42|
43|43|## 1. Purpose and Scope
44|44|
45|45|The README names threat intelligence as a Cyber Risk function. The Operating Model names the Threat Intelligence Analyst as the role that tracks threat actors, advisories, and intelligence-to-detection translation. Existing procedures consume threat intelligence, but no procedure defined how intelligence is sourced, triaged, prioritized, disseminated, or tracked to action. This procedure closes that gap.
46|46|
47|47|Threat intelligence in CERG is operational. Its purpose is not to publish interesting reports. Its purpose is to help the organization make better decisions sooner: patch the right thing faster, change a design before it ships, warn the right owner, tune a detection, reassess a vendor, or record a risk.
48|48|
49|49|This procedure applies to all threat intelligence used by CERG to inform exposure management, threat modeling, architecture review, third-party risk, OT risk, detection priorities, and risk-register decisions.
50|50|
51|51|> **Intelligence That Does Not Change Action Is Trivia**
52|52|>
53|53|> A threat feed can produce thousands of indicators and still produce no security outcome. CERG does not measure intelligence by volume. It measures whether intelligence reached the right owner in time to change a decision: patch this, block that, model this abuse case, watch this vendor, raise this risk. If a piece of intelligence has no decision path, it is context, not work.
54|54|
55|55|---
56|56|
57|57|## 2. Principles
58|58|
59|59|1. **Relevance beats volume.** Intelligence is judged by its relationship to the organization's assets, technologies, vendors, data, and threat exposure.
60|60|2. **Timeliness matters.** A perfect advisory delivered after exploitation is history, not intelligence.
61|61|3. **Every actionable item has an owner.** If an intelligence item requires action, the action is assigned to a canonical role and tracked to disposition.
62|62|4. **Use multiple source types.** No single feed or vendor provides the full threat picture. CERG uses government, commercial, open-source, sector, vendor, and internal sources.
63|63|5. **Internal telemetry is intelligence.** Vulnerability trends, incidents, phishing reports, and adversarial testing findings are intelligence inputs, not just local events.
64|64|6. **Dissemination is tailored.** The CISO needs posture and decision impact. Engineering needs concrete action. Governance needs evidence and regulatory implication. Risk needs exposure and priority.
65|65|
66|66|---
67|67|
68|68|## 3. Intelligence Sources
69|69|
70|70|The Threat Intelligence Analyst maintains a source register. Sources are reviewed at least annually for relevance, reliability, and usefulness.
71|71|
72|72|| **Source Type** | **Examples** | **Primary Use** |
73|73||---|---|---|
74|74|| Government and sector advisories | CISA, FBI, MS-ISAC, ES-ISAC, NCSC, sector regulators | High-confidence alerts, exploited vulnerabilities, sector campaigns. |
75|75|| Vendor advisories | Cloud, SaaS, endpoint, identity, OT, and security vendors | Product-specific vulnerabilities and mitigations. |
76|76|| Commercial intelligence | Paid intelligence platforms or managed-intelligence feeds | Actor tracking, campaign context, enriched indicators. |
77|77|| Open-source intelligence | Public research, blogs, GitHub advisories, abuse reports | Fast context, exploit availability, community findings. |
78|78|| Internal telemetry | Vulnerability data, phishing reports, incident lessons, adversarial testing findings | Organization-specific exposure and observed behavior. |
79|79|| Peer and trust groups | ISACs, industry groups, trusted peer exchanges | Sector targeting, early warning, practical mitigations. |
80|80|| Regulatory and legal updates | Regulator alerts, new requirements, enforcement activity | Governance and compliance implications. |
81|81|
82|82|Restricted-source or sensitive intelligence is handled according to its classification under [`CERG-STD-DG-001`](../standards/CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md).
83|83|
84|84|---
85|85|
86|86|## 4. Intake and Triage
87|87|
88|88|### 4.1 Intake Channels
89|89|
90|90|Threat intelligence enters through approved channels: source registers, email subscriptions, vendor portals, ISAC channels, internal reports, incident lessons, adversarial validation reports, and vulnerability advisories. Informal inputs are allowed, but once an item is actionable it is recorded in the intelligence intake log.
91|91|
92|92|### 4.2 Minimum Intake Fields
93|93|
94|94|Every actionable item records:
95|95|
96|96|| **Field** | **Purpose** |
97|97||---|---|
98|98|| Source | Where the item came from. |
99|99|| Date received | Timeliness and review tracking. |
100|100|| Summary | Plain-language statement of what changed. |
101|101|| Affected technologies, vendors, or sectors | Relevance check. |
102|102|| Associated vulnerabilities, techniques, or indicators | Links to CVEs, ATT&CK techniques, IOCs, or behaviors. |
103|103|| Known exploitation | Whether exploitation is observed, likely, or theoretical. |
104|104|| Initial priority | Critical, High, Medium, Low. |
105|105|| Action owner | Canonical role responsible for next step. |
106|106|| Disposition | Monitor, disseminate, create action, create risk, close. |
107|107|
108|108|### 4.3 Triage Outcomes
109|109|
110|110|| **Outcome** | **Meaning** |
111|111||---|---|
112|112|| **Close as not relevant** | No affected asset, vendor, technology, sector, or plausible exposure. |
113|113|| **Monitor** | Relevant but no immediate action. Review when conditions change. |
114|114|| **Disseminate** | Useful context for one or more owners, but no tracked action required. |
115|115|| **Create action** | Requires patching, configuration, detection, review, vendor follow-up, or project change. |
116|116|| **Create risk** | Residual exposure requires tracking through [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md). |
117|117|
118|118|---
119|119|
120|120|### 4.4 Analysis Methodology
121|121|
122|122|Raw intelligence is analyzed before dissemination. The following frameworks and standards ensure consistent, defensible analysis.
123|123|
124|124|#### Analysis Frameworks
125|125|
126|126|| **Framework** | **Application** | **Description** |
127|127||---|---|---|
128|128|| Diamond Model | Intrusion analysis | Maps adversary, capability, infrastructure, and victim for each intrusion event. Used to identify adversary campaigns and infrastructure patterns. |
129|129|| Intelligence Cycle | Production workflow | Planning → Collection → Processing → Analysis → Dissemination → Feedback. Each intelligence product follows this cycle. |
130|130|| Kill Chain Analysis | Attack reconstruction | Maps observed activity to Recon → Weaponization → Delivery → Exploitation → Installation → C2 → Actions. Used to identify where defenses failed or succeeded. |
131|131|
132|132|#### Confidence Levels
133|133|
134|134|Every intelligence product includes a confidence assessment:
135|135|
136|136|| **Confidence** | **Definition** | **Criteria** |
137|137||---|---|---|
138|138|| Confirmed | Independently corroborated by multiple reliable sources | ≥ 3 corroborating sources; no conflicting information |
139|139|| Probable | Supported by reliable sources with minor gaps | 2 corroborating sources or 1 highly reliable source |
140|140|| Possible | Plausible but single source or limited corroboration | 1 source of moderate reliability; limited supporting evidence |
141|141|| Unlikely | Contradicted by more reliable information | Primary source contradicted; low reliability |
142|142|| Doubtful | Highly improbable based on available information | Single low-reliability source; significant contradicting evidence |
143|143|
144|144|#### Source Reliability Assessment
145|145|
146|146|| **Rating** | **Definition** |
147|147||---|---|
148|148|| A - Completely Reliable | History of complete reliability; no doubt of authenticity |
149|149|| B - Usually Reliable | Minor doubts; history of valid information with occasional errors |
150|150|| C - Fairly Reliable | Some doubts; information used but not confirmed through other sources |
151|151|| D - Not Usually Reliable | Significant doubts; information used only when corroborated |
152|152|| E - Unreliable | History of invalid information; not used |
153|153|| F - Cannot Be Judged | No basis for reliability assessment |
154|154|
155|155|The Threat Intelligence Analyst assesses both confidence in the analyzed intelligence and reliability of the source. Products clearly state the confidence level and source reliability rating.
156|156|
157|157|---
158|158|
159|159|### 4.5 IOC Lifecycle Management
160|160|
161|161|Indicators of Compromise (IOCs) have a lifecycle from ingestion through deployment to retirement.
162|162|
163|163|#### IOC Confidence Scoring
164|164|
165|165|| **Score** | **Criteria** |
166|166||---|---|
167|167|| High | Confirmed malicious by ≥ 2 independent sources; observed in production attacks |
168|168|| Medium | Reported by a trusted source; limited independent confirmation |
169|169|| Low | Single report; unverified; or context-dependent (e.g., IP that is also used legitimately) |
170|170|
171|171|#### IOC Expiration
172|172|
173|173|IOCs auto-expire after 90 days unless refreshed. The Threat Intelligence Analyst reviews expiring IOCs and either:
174|174|- Refreshes: IOC is still active and confirmed; expiration clock resets
175|175|- Retires: IOC is no longer active, has been remediated, or is no longer relevant
176|176|
177|177|Expired IOCs are removed from active detection tooling but retained in the intelligence archive for historical analysis.
178|178|
179|179|#### False Positive Management
180|180|
181|181|| **Step** | **Action** |
182|182||---|---|
183|183|| 1 | Detection Engineer identifies a false positive IOC (alert fires on benign activity) |
184|184|| 2 | IOC is suppressed in detection tooling with a note and timestamp |
185|185|| 3 | Threat Intelligence Analyst reviews within 5 business days |
186|186|| 4 | If confirmed false positive: IOC is retired with rationale. If disputed: IOC remains active; detection rule is tuned instead |
187|187|
188|188|False positive rate is tracked as a metric. A sustained false positive rate > 20% on any IOC source triggers a source quality review.
189|189|
190|190|#### Integration with Detection Tooling
191|191|
192|192|IOCs are deployed to detection tooling (SIEM, EDR, NGFW) through an automated or semi-automated pipeline. IOC retirement is synchronized: when an IOC is retired in the intelligence platform, it is automatically removed from detection tooling within 24 hours.
193|193|
194|194|---
195|195|
196|196|## 5. Relevance and Priority
197|197|
198|198|Priority is based on relevance, exposure, exploitation, and potential impact. A dramatic threat report with no relationship to the environment is lower priority than a quiet advisory for a product the organization runs on the internet.
199|199|
200|200|| **Priority** | **Criteria** | **Expected Handling** |
201|201||---|---|---|
202|202|| **Critical** | Active exploitation against technology the organization uses, especially internet-facing, identity, OT, or Restricted-data systems. | Same-day owner notification; action or risk entry opened immediately. |
203|203|| **High** | Likely exploitation or high-impact technique affecting used technology, a key vendor, or a regulated environment. | Owner notification within one business day; tracked action opened. |
204|204|| **Medium** | Plausible relevance, limited exposure, or no known exploitation. | Disseminate to relevant owner; monitor or schedule action. |
205|205|| **Low** | General context, weak relevance, or awareness-only item. | Record if useful; no action required. |
206|206|
207|207|Priority does not replace vulnerability severity or risk scoring. It informs them. Vulnerability remediation still follows [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Exposure_Management_Procedure.md), and residual risk still follows [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md).
208|208|
209|209|---
210|210|
211|211|## 6. Products and Dissemination
212|212|
213|213|The Threat Intelligence Analyst produces only products with a clear audience and decision purpose.
214|214|
215|215|| **Product** | **Audience** | **Purpose** |
216|216||---|---|---|
217|217|| Flash advisory | Engineering, Risk, Governance, CISO as needed | Time-sensitive item requiring immediate awareness or action. |
218|218|| Weekly intelligence digest | Risk and Engineering owners | Relevant trends, exploited vulnerabilities, sector activity, and follow-up reminders. |
219|219|| Threat-model input brief | Threat modeling participants | Actor, technique, and abuse-case context for design review. |
220|220|| Vulnerability context note | Exposure Management Lead | Exploitation status, weaponization, and prioritization context. |
221|221|| Vendor risk note | Vendor Risk Analyst | Supplier compromise, product vulnerability, or service-risk context. |
222|222|| Executive threat brief | CISO and Executive Sponsor | Material changes to threat exposure and decisions needed. |
223|223|
224|224|Dissemination is targeted. Sending every item to everyone trains everyone to ignore the channel.
225|225|
226|226|> **Broadcast Is Not Dissemination**
227|227|>
228|228|> Dumping every advisory into a shared chat is not a threat intelligence program. It is noise with timestamps. CERG dissemination names the audience, the decision, and the requested action. If the recipient cannot tell what to do with the intelligence, the message failed.
229|229|
230|230|---
231|231|
232|232|## 7. Action Tracking
233|233|
234|234|Actionable intelligence is tracked to disposition. The Threat Intelligence Analyst does not necessarily do the remediation, but owns the intelligence-to-action handoff until the receiving owner accepts it.
235|235|
236|236|| **Action Type** | **Receiving Owner** | **Tracking Path** |
237|237||---|---|---|
238|238|| Patch or mitigate vulnerability | Exposure Management Lead | [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Exposure_Management_Procedure.md). |
239|239|| Change design or control requirement | Engineering Pillar Leader or relevant Engineering role | [`CERG-PRC-AR-001`](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md) or relevant standard. |
240|240|| Add threat-model abuse case | Threat Intelligence Analyst | [`CERG-PRC-TM-001`](CERG-PRC-TM-001_Threat_Modeling_Procedure.md). |
241|241|| Reassess supplier | Vendor Risk Analyst | [`CERG-PRC-TPRM-001`](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md). |
242|242|| Create or tune detection | Detection Engineer | Detection backlog governed by [`CERG-STD-LM-001`](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md). |
243|243|| Record residual exposure | Risk Register Owner | [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md). |
244|244|| Brief leadership | Risk Pillar Leader | CISO dashboard or executive threat brief. |
245|245|
246|246|An item is closed only when the receiving owner records disposition: completed, accepted risk, not applicable with reason, or superseded.
247|247|
248|248|---
249|249|
250|250|## 8. Integration With CERG Processes
251|251|
252|252|Threat intelligence feeds the program through defined channels.
253|253|
254|254|| **CERG Process** | **How Intelligence Feeds It** |
255|255||---|---|
256|256|| Architecture review | Supplies threat context and abuse cases for design decisions. |
257|257|| Threat modeling | Supplies actor, technique, and campaign context. |
258|258|| Exposure management | Adds exploitation, weaponization, and environmental relevance to remediation priority. |
259|259|| Third-party risk | Identifies supplier compromise, vendor product vulnerabilities, and sector vendor campaigns. |
260|260|| Asset management | Helps identify crown-jewel systems and technologies under active targeting. |
261|261|| AI security | Tracks prompt-injection, model supply chain, and AI-service data-risk developments. |
262|262|| OT risk | Uses ICS-specific intelligence and ATT&CK for ICS where OT is in scope. |
263|263|| Risk register | Converts sustained exposure into tracked risk. |
264|264|| Metrics and reporting | Provides threat-context narrative for posture reporting. |
265|265|
266|266|---
267|267|
268|268|## 9. Intelligence-Driven Program Reprioritization
269|269|
270|270|Threat intelligence that is collected, triaged, and disseminated but never changes the program is a reporting exercise, not an Adaptive capability. The CERG Framework (FRM-001 Section 6.2) states that "Threat intelligence actively shapes Engineering design decisions and Governance policy priorities." An Adaptive assessor expects to see evidence that intelligence has actually changed the program, not just informed it.
271|271|
272|272|This section defines the quarterly cadence and decision framework by which intelligence drives program-level reprioritization.
273|273|
274|274|### 9.1 Quarterly Threat Landscape Assessment
275|275|
276|276|Once per quarter, aligned with the CERG leadership review cadence (GOV-CAL-001 Section 5), the Risk Pillar Leader presents a Threat Landscape Assessment to the CISO and pillar leaders. The assessment is a structured briefing, not a raw intelligence dump.
277|277|
278|278|The assessment covers:
279|279|
280|280|- **Top 3 threat actors** targeting the organization's sector, with observed TTPs and campaign context
281|281|- **TTP changes** observed in the last quarter that differ from the prior assessment
282|282|- **Changes in targeting patterns:** are new sectors, technologies, or organization types being targeted?
283|283|- **Vulnerabilities actively exploited in the wild** (CISA KEV or vendor-confirmed exploitation), with mapping to CERG assets
284|284|- **Intelligence gaps identified:** what should CERG know about the threat landscape that it does not currently know?
285|285|- **External incident impact assessment:** any major breach at a peer or in-sector organization, with implications for CERG
286|286|
287|287|### 9.2 Reprioritization Decision Framework
288|288|
289|289|The assessment MUST produce at least one of the following reprioritization decisions, each recorded with rationale in the improvement register (IMPREG-001):
290|290|
291|291|| Decision | Trigger Condition | Example |
292|292||---|---|---|
293|293|| **No program change** | Current posture is adequate for the assessed threat landscape. | Must state specifically why : not "we are fine" but "our current network segmentation (STD-NET-001 Section 5) blocks the lateral movement technique observed in the campaign." |
294|294|| **Control baseline adjustment** | A new TTP or exploitation pattern is not addressed by the current control baseline. | "Ransomware groups are now exploiting RMM tools for initial access. Proposed: add a CB-001 control requiring RMM tool inventory and approved-tool policy." |
295|295|| **Project intake priority shift** | A class of project or technology now carries elevated risk. | "API-first architectures are being targeted. Proposed: elevate API gateway projects to mandatory architecture review." |
296|296|| **Detection rule update** | Observed TTPs are not covered by current detection rules. | "The campaign uses a specific LOLBin chain not in our detection set. Proposed: add detection rules for the observed chain." |
297|297|| **Tooling or capability gap** | The threat landscape requires a capability CERG does not currently have. | "Adversaries are abusing OAuth token attacks at scale. Proposed: evaluate OAuth threat detection tooling." |
298|298|| **Staffing or training recommendation** | A sustained threat pattern requires specialized expertise. | "ICS-targeting activity has increased 300% year-over-year. Proposed: add an OT Threat Analyst position." |
299|299|| **External sharing action** | Intelligence is relevant to an ISAC, peer group, or regulator. | "Observed novel ICS technique. Proposed: share sanitized TTP with E-ISAC." |
300|300|
301|301|> **The "No Change" Decision Requires Proof**
302|302|>
303|303|> "No program change" is a valid output of the quarterly assessment, but it must be a deliberate conclusion with specific rationale, not a default. An assessor reviewing two years of quarterly assessments where every single one concluded "no change needed" will correctly conclude either that the intelligence program is not producing actionable intelligence or that the program is not listening to it. Both conclusions are Adaptive-fatal.
304|304|
305|305|### 9.3 Decision Record
306|306|
307|307|Each reprioritization decision is recorded in the improvement register (IMPREG-001) with:
308|308|
309|309|- Source: "Intelligence-Driven Reprioritization, QN YYYY"
310|310|- The intelligence trigger (specific threat actor, TTP, campaign, or vulnerability)
311|311|- The decision and accountable role
312|312|- A verification checkpoint (reviewed at the next quarterly assessment)
313|313|
314|314|### 9.4 Verification
315|315|
316|316|At each quarterly assessment, the prior quarter's reprioritization decisions are verified:
317|317|
318|318|- Was the control adjusted? Is the new or modified control in CB-001?
319|319|- Was the detection rule deployed? Is it producing alerts?
320|320|- Was the capability gap funded? Is the tool procured or the hire in progress?
321|321|- Incomplete actions are escalated to the CISO.
322|322|
323|323|Verification outcomes (Effective, Partially Effective, Ineffective) are recorded in IMPREG-001 per the improvement lifecycle.
324|324|
325|325|### 9.5 Integration with Lessons Learned
326|326|
327|327|The quarterly Threat Landscape Assessment is an intake source for the Lessons Learned procedure (PRC-LL-001). Intelligence-driven patterns that persist across multiple quarters are analyzed alongside incident, audit, and adversarial validation patterns at the quarterly Lessons Aggregation Review.
328|328|
329|329|---
330|330|
331|331|## 10. External Collaboration and Information Sharing
332|332|
333|333|Adaptive maturity expects bidirectional information sharing : not just consuming threat intelligence, but contributing back, participating in communities, and learning from peers' incidents. This section defines the external collaboration requirements for CERG.
334|334|
335|335|### 10.1 ISAC / ISAO Membership
336|336|
337|337|CERG must maintain membership in at least one sector-appropriate Information Sharing and Analysis Center (ISAC) or Information Sharing and Analysis Organization (ISAO). For organizations with IT and OT footprints, dual membership in the sector IT ISAC and E-ISAC (electricity) or equivalent OT ISAC is recommended.
338|338|
339|339|| Requirement | Detail |
340|340||---|---|
341|341|| Minimum participation | Attend quarterly member calls and respond to Requests for Information (RFIs) within the ISAC's published SLA |
342|342|| Designated liaison | Threat Intelligence Analyst or Risk Pillar Leader |
343|343|| Escalation | Material intelligence received through ISAC channels follows the same triage and prioritization as Section 4-5 |
344|344|
345|345|### 10.2 Peer Benchmarking
346|346|
347|347|At least annually, the Threat Intelligence Analyst collects and analyzes peer benchmarking data where available.
348|348|
349|349|Sources include:
350|350|- ISAC member threat reports and statistics
351|351|- Industry surveys (DBIR, SANS, sector-specific reports)
352|352|- Regulatory aggregate data where published
353|353|- Trusted peer exchanges
354|354|
355|355|The benchmarking analysis compares CERG's posture against peer norms:
356|356|- Vulnerability closure rates compared to sector peers
357|357|- Incident frequency and type compared to sector peers
358|358|- Control coverage compared to recommended sector baselines
359|359|
360|360|Significant deviations from peer norms trigger a program review. Example: if peer organizations close Critical vulnerabilities in a mean of 30 days and CERG's mean is 90 days, the gap must be explained and either accepted with rationale or converted to an improvement action.
361|361|
362|362|### 10.3 External Incident Learning
363|363|
364|364|When a major breach at a peer or in-sector organization is publicly reported, CERG conducts a structured External Incident Review within 14 calendar days. The review is led by the Threat Intelligence Analyst with participation from the affected pillar.
365|365|
366|366|The review answers four questions:
367|367|
368|368|1. **Could this happen here?** Does the affected technology, configuration, vendor, or process exist in CERG's environment?
369|369|2. **Are the relevant controls present and effective?** Map the attack chain to CERG's control baseline (CB-001). Are all relevant controls Implemented? Have their effectiveness metrics (CEF-001) been measured?
370|370|3. **What would our detection and response look like?** If the same attack chain were executed against CERG, would it be detected? Would the response be effective?
371|371|4. **What changes, if any, are warranted?** The output is either:
372|372|   - "No change needed" with specific rationale (e.g., "the affected technology is not deployed; the attack vector is blocked by STD-NET-001 Section 5")
373|373|   - An improvement register entry (IMPREG-001) for each warranted change
374|374|
375|375|### 10.4 Community Contribution
376|376|
377|377|At least annually, CERG contributes back to the ISAC or security community. Minimum contribution: sanitized lessons learned, threat observations, or control effectiveness data. This is both an Adaptive indicator in NIST CSF assessments and a professional obligation.
378|378|
379|379|Acceptable contributions include:
380|380|- Sanitized incident lessons (what happened, what worked, what did not : without attribution or sensitive detail)
381|381|- Novel threat observations or TTPs
382|382|- Control effectiveness insights ("we found that control X was consistently ineffective in Y scenario")
383|383|- Tool or technique evaluations
384|384|
385|385|### 10.5 Information Sharing Boundaries
386|386|
387|387|Not everything can be shared. Before any external contribution, the following classification rules apply:
388|388|
389|389|| Classification | Sharing Rule |
390|390||---|---|
391|391|| Sanitized, non-attributable observations | Share freely with ISAC / peer groups |
392|392|| Specific vulnerabilities before remediation | Do not share externally until remediated |
393|393|| Customer, patient, or citizen data | Never share; regulated |
394|394|| Attorney-client privileged material | Never share without legal review |
395|395|| Competitive or business-strategy information | Never share |
396|396|| Incident details during active incident | Share only with official response partners (ISAC, CISA, law enforcement as appropriate) |
397|397|
398|398|When in doubt, the CISO and legal counsel review before sharing.
399|399|
400|400|---
401|401|
402|402|### 10.6 Traffic Light Protocol (TLP) Handling
403|403|
404|404|CERG uses the Traffic Light Protocol (TLP) for all intelligence sharing with external partners, ISACs, and industry groups.
405|405|
406|406|| **TLP Level** | **Definition** | **Handling Requirement** |
407|407||---|---|---|
408|408|| TLP:RED | For the eyes and ears of named recipients only; no further distribution | Not shared beyond named recipients. Stored with access restricted to the Threat Intelligence Analyst and named recipients. Not included in any wider-distribution product. |
409|409|| TLP:AMBER | Limited distribution within the organization and named partners | May be shared within CERG and with named partner organizations on a need-to-know basis. Not posted on publicly accessible platforms. Products containing TLP:AMBER information are clearly marked. |
410|410|| TLP:GREEN | Distribution within the community | May be shared with peer organizations, ISAC members, and trusted partners within the same sector or community. Not released publicly. |
411|411|| TLP:CLEAR | Unlimited distribution | May be shared freely. No restrictions on distribution. |
412|412|
413|413|#### TLP Marking
414|414|
415|415|Every intelligence product that contains TLP-classified information is marked with the highest applicable TLP level. The marking appears in the product header. When a product combines intelligence from multiple TLP sources, the most restrictive level applies.
416|416|
417|417|#### Source TLP Compliance
418|418|
419|419|The Threat Intelligence Analyst ensures that intelligence received under a TLP designation is handled per that designation. Intelligence received as TLP:RED is never sourced in a TLP:AMBER or lower product. Intelligence received under Chatham House Rule is paraphrased and not attributed to a specific organization or individual.
420|420|
421|421|---
422|422|
423|423|### 10.7 Consumer Feedback Loop
424|424|
425|425|Intelligence products are assessed by the consumers who use them. This feedback loop drives continuous improvement in intelligence production.
426|426|
427|427|#### Feedback Mechanism
428|428|
429|429|| **Mechanism** | **Description** |
430|430||---|---|
431|431|| Product rating | Recipients of intelligence products are invited to rate each product on usefulness (1–5) and accuracy (1–5) |
432|432|| Structured feedback | Quarterly, the Threat Intelligence Analyst solicits feedback from the top 5 consumers of intelligence products (e.g., Exposure Management Lead, Vendor Risk Analyst, Detection Engineer, CISO) |
433|433|| Ad-hoc feedback | Any consumer may provide feedback at any time through the intelligence intake channel |
434|434|
435|435|#### Feedback Review Process
436|436|
437|437|The Threat Intelligence Analyst reviews all feedback quarterly:
438|438|- Products rated < 3 on usefulness are analyzed: was the wrong audience targeted? Was the analysis insufficient? Was the timing poor?
439|439|- Products rated < 3 on accuracy are re-examined; if confirmed inaccurate, a correction is issued and the source reliability rating is adjusted
440|440|- Patterns in feedback inform source selection, product format changes, and dissemination list adjustments
441|441|
442|442|#### Program Improvements from Feedback
443|443|
444|444|Feedback that identifies a systematic gap in intelligence production (e.g., "we consistently lack context on vulnerabilities affecting our tech stack" or "the weekly digest is too long to read") is routed to the improvement register per [CERG-PRC-LL-001](CERG-PRC-LL-001_Lessons_Learned_and_Program_Improvement_Procedure.md).
445|445|
446|446|---
447|447|
448|448|## 11. Metrics
449|449|
450|450|Threat intelligence metrics measure relevance and action, not raw feed volume.
451|451|
452|452|| **Metric** | **Why It Matters** |
453|453||---|---|
454|454|| Actionable intelligence items received | Measures useful signal, not total noise. |
455|455|| Items closed as not relevant | Shows filtering discipline and source quality. |
456|456|| Time from receipt to owner notification for Critical and High items | Measures timeliness. |
457|457|| Percent of actionable items with assigned owner | Measures handoff quality. |
458|458|| Percent of actions closed by disposition | Measures follow-through. |
459|459|| Intelligence items feeding vulnerability priority | Shows connection to exposure reduction. |
460|460|| Intelligence items feeding threat models | Shows design-stage use. |
461|461|| Intelligence items resulting in risk-register entries | Shows residual exposure capture. |
462|462|
463|463|---
464|464|
465|465|## 12. Roles and Responsibilities
466|466|
467|467|Roles below are canonical role names from [`CERG-GOV-OM-001`](../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1.
468|468|
469|469|| **Role** | **Threat Intelligence Responsibility** |
470|470||---|---|
471|471|| **Risk Pillar Leader** | Accountable for this procedure and for intelligence quality, prioritization, and escalation. |
472|472|| **Threat Intelligence Analyst** | Operates the procedure; maintains sources; triages intelligence; produces intelligence products; tracks intelligence-to-action handoffs. |
473|473|| **Exposure Management Lead** | Consumes intelligence for vulnerability prioritization and remediation decisions. |
474|474|| **Adversarial Testing Lead** | Uses intelligence to shape adversarial validation scope and scenarios. |
475|475|| **Vendor Risk Analyst** | Consumes supplier and vendor intelligence; performs reassessment where needed. |
476|476|| **OT Risk Analyst** | Supplies and consumes OT and ICS threat intelligence. |
477|477|| **Detection Engineer** | Receives detection leads and maps intelligence to detection backlog where in scope. |
478|478|| **Engineering Pillar Leader** | Receives design and architecture-impacting intelligence and assigns relevant Engineering owners. |
479|479|| **Governance Pillar Leader** | Receives intelligence with compliance, audit, or executive reporting implications. |
480|480|| **Risk Register Owner** | Records sustained exposure or accepted residual risk from intelligence-driven findings. |
481|481|| **Chief Information Security Officer (CISO)** | Receives material threat briefings and makes program-level decisions based on intelligence. |
482|482|
483|483|---
484|484|
485|485|## 13. Regulatory and Framework Alignment Summary
486|486|
487|487|| **Regulation / Framework** | **Reference** | **Where in This Procedure** |
488|488||---|---|---|
489|489|| NIST 800-53r5 | RA-3, RA-5, SI-5, PM-16 | Sections 3, 4, 5, 7, 8 |
490|490|| NIST CSF 2.0 | ID.RA, DE.CM | Sections 5, 7, 8 |
491|491|| MITRE ATT&CK | Adversary technique mapping | Sections 5, 6, 8 |
492|492|| MITRE ATT&CK for ICS | OT and ICS threat context | Sections 3, 8, 10 |
493|493|| CMMC L2 / NIST 800-171r3 | Risk assessment and flaw remediation support | Sections 5, 7, 8 |
494|494|| NERC-CIP | OT threat awareness and BES Cyber System implications | Sections 3, 8, 10 |
495|495|| SOX ITGC | Threat context for financially relevant systems | Sections 7, 8 |
496|496|
497|497|---
498|498|
499|499|
500|500|---
501|501|
502|502|## Appendix A: Intelligence Product Templates
503|503|
504|504|### A.1 Flash Advisory
505|505|
506|506|```
507|507|FLASH ADVISORY - TI-YYYY-NNNN
508|508|TLP: [AMBER / GREEN]
509|509|Date: [date]
510|510|Priority: [CRITICAL / HIGH / MEDIUM]
511|511|
512|512|Title:
513|513|Summary: [one paragraph - what happened, what to do]
514|514|
515|515|Affected Technology: [vendor, product, version]
516|516|Recommended Actions:
517|517|  1. [action]
518|518|  2. [action]
519|519|
520|520|IOCs (Confidence: [High/Medium/Low]):
521|521|  - [type]: [value]
522|522|
523|523|ATT&CK Mapping: [technique IDs]
524|524|Source: [source type, reliability rating]
525|525|Analyst: [name]
526|526|```
527|527|
528|528|### A.2 Weekly Digest
529|529|
530|530|```
531|531|WEEKLY THREAT DIGEST - TI-WD-YYYY-WNN
532|532|TLP: GREEN
533|533|Period: [start] to [end]
534|534|
535|535|Key Developments:
536|536|  1. [development]
537|537|  2. [development]
538|538|
539|539|New IOCs: [count] - [summary of types]
540|540|Upcoming Threats: [what to watch for in the next 7 days]
541|541|Recommended Reading: [links to relevant advisories, reports]
542|542|Analyst: [name]
543|543|```
544|544|
545|545|### A.3 Threat Model Input Brief
546|546|
547|547|```
548|548|THREAT MODEL INPUT BRIEF - TI-TM-YYYY-NNNN
549|549|TLP: AMBER
550|550|System: [system name]
551|551|Architecture Review: [AR-YYYY-NNNN]
552|552|
553|553|Threat Actors in Scope:
554|554|  | Actor | Capability | Relevance |
555|555|  |---|---|---|
556|556|  | | | |
557|557|
558|558|Relevant TTPs:
559|559|  | TTP | Description | Relevance to System |
560|560|  |---|---|---|
561|561|  | | | |
562|562|
563|563|Relevant CVEs (last 90 days):
564|564|  | CVE | CVSS | Affected Product | Exploit Available? |
565|565|  |---|---|---|---|
566|566|  | | | | |
567|567|
568|568|Recommended Abuse Cases:
569|569|  1. [abuse case]
570|570|  2. [abuse case]
571|571|
572|572|Analyst: [name]
573|573|```
574|574|
575|575|### A.4 Vulnerability Context Note
576|576|
577|577|```
578|578|VULNERABILITY CONTEXT NOTE - TI-VC-YYYY-NNNN
579|579|TLP: GREEN
580|580|Date: [date]
581|581|CVE: [CVE-ID]
582|582|CVSS: [score]
583|583|
584|584|Exploit Status:
585|585|  [ ] Not observed in wild
586|586|  [ ] PoC available
587|587|  [ ] Actively exploited
588|588|
589|589|Affected Assets (from CMDB): [list or "None identified"]
590|590|Recommended Priority: [Immediate / 72hr / 30-day / Patch-cycle]
591|591|Context: [why this matters to the organization]
592|592|Analyst: [name]
593|593|```
594|594|
595|595|### A.5 Vendor Risk Note
596|596|
597|597|```
598|598|VENDOR RISK NOTE - TI-VR-YYYY-NNNN
599|599|TLP: AMBER
600|600|Date: [date]
601|601|Vendor: [name]
602|602|Vendor Tier: [T1/T2/T3]
603|603|
604|604|Finding: [description of threat intelligence]
605|605|Risk Implication: [what this means for the organization's use of this vendor]
606|606|Recommended Action: [specific action for Vendor Risk Analyst]
607|607|Related: [CERG-PRC-TPRM-001 reference]
608|608|Analyst: [name]
609|609|```
610|610|
611|611|### A.6 Executive Threat Brief
612|612|
613|613|```
614|614|EXECUTIVE THREAT BRIEF - TI-EX-YYYY-QN
615|615|TLP: AMBER
616|616|Period: [quarter] [year]
617|617|
618|618|Top Threats:
619|619|  1. [threat] - [impact to organization] - [likelihood]
620|620|  2. [threat] - [impact] - [likelihood]
621|621|  3. [threat] - [impact] - [likelihood]
622|622|
623|623|Program Impact: [how the threat landscape affects CERG program priorities]
624|624|Recommended Decisions: [specific decisions for CISO/executive consideration]
625|625|Analyst: [name]
626|626|Reviewer: [CISO]
627|627|```
628|628|
629|629|## 14. Document Control
630|630|
631|631|| Field | Value |
632|632||---|---|
633|633|| **Document ID** | CERG-PRC-TI-001 |
634|634|| **Version** | 1.1 |
635|635|| **Status** | Approved |
636|636|| **Effective Date** | 2026-05-26 |
637|637|| **Classification** | Public |
638|638|| **Owner** | Risk Pillar Leader |
639|639|| **Approved By** | CISO |
640|640|| **Parent Policy** | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
641|641|| **Review Cycle** | Annual; and on material change to threat landscape or intelligence sources |
642|642|| **Next Scheduled Review** | 2027-05-26 |
643|643|| **Frameworks** | NIST 800-53r5 (RA-3, RA-5, SI-5, PM-16); NIST CSF 2.0 (ID.RA, DE.CM, ID.IM, GOVERN); MITRE ATT&CK; MITRE ATT&CK for ICS |
644|644|| **Regulations** | CMMC L2 / 800-171r3; NERC-CIP; SOX ITGC where applicable |
645|645|| **Environments** | All CERG-managed environments and risk decisions informed by threat intelligence |
646|646|
647|647|#
648|## 16. Identity Threat Detection
649|
650|This section provides procedures for detecting identity-based threats across human and non-human identities (NHI). It operationalizes the Identity Risk Analyst role defined in CERG-GOV-OM-001 §6.1 and supports the Privileged Account Anomaly Rate metric (PL-007 in CERG-GOV-MTR-001).
651|
652|### 16.1 Data Sources
653|
654|| Source Type | Specific Sources | Identity Signals |
655||-------------|-----------------|------------------|
656|| Identity Provider (IdP) | Entra ID / Active Directory, Okta, Ping | Logon failures, MFA prompts, password changes, group membership changes, device enrollments |
657|| Privileged Access Management (PAM) | CyberArk, BeyondTrust, Delinea | Session recordings, credential checkouts, elevation requests, vault access |
658|| Cloud Infrastructure | CloudTrail, Azure Monitor, GCP Cloud Logging | API calls from human and service principals, IAM role assumptions, service account key creation |
659|| SaaS Applications | OAuth logs, app consent grants, admin audit logs | Delegated permissions, app role assignments, anomalous API call volumes |
660|| Endpoint | EDR, syslog IdP agent logs | Token theft indicators, session replay, credential dumping |
661|| Network | Authentication proxy, VPN, CASB | Geographic anomalies, impossible travel, device posture changes |
662|
663|### 16.2 Baseline Establishment
664|
665|For each identity population (user, service account, workload identity, CI/CD pipeline token), establish baselines:
666|
667|| Baseline | Method | Refresh |
668||----------|--------|---------|
669|| Login times and frequency | 90-day rolling window of successful authentications | Monthly |
670|| Geo-locations | VPN/ CASB regional data | Quarterly |
671|| API call volume (service accounts) | Count of API calls per 24h window | Weekly |
672|| Privilege elevation frequency | PAM elevation requests per identity per week | Monthly |
673|| SaaS OAuth consent patterns | New app consents per user per month | Weekly |
674|| Device profile | Device IDs per user | Weekly |
675|
676|### 16.3 Alert Thresholds
677|
678|| Alert | Threshold | Severity | Triage SLA |
679||-------|-----------|----------|------------|
680|| Impossible travel | Login from >500 km within time window impossible by transit | Critical | 15 min |
681|| Service account API burst | >3σ above baseline volume in 1-hour window | High | 1 hour |
682|| MFA fatigue burst | >5 MFA deny prompts per user in 10 min | Critical | 15 min |
683|| New service principal key creation | Any creation outside change window | High | 1 hour |
684|| OAuth consent to high-risk app | App with publisher not in sanctioned list | Medium | 4 hours |
685|| Privilege elevation outside window | Elevation outside defined change window | Critical | 30 min |
686|| Stale credential use | Credential >90 days old used for authentication | Medium | 4 hours |
687|
688|### 16.4 Triage Playbook
689|
690|```
691|1. COLLECT
692|   - Gather all identity signals for the affected identity (IdP, PAM, Cloud, SaaS)
693|   - Check threat intelligence for known IOCs matching the anomaly pattern
694|   - Open identity threat record in risk register
695|
696|2. SCOPING
697|   - Determine which resources the identity accessed in the alert window
698|   - Check for data exfiltration signals (unusual downloads, API responses)
699|   - Validate whether the behavior matches known patterns (maintenance window, deployment)
700|
701|3. CONTAIN
702|   - If confirmed malicious: disable identity, rotate credentials, revoke sessions
703|   - If suspicious: require re-authentication with MFA, lower privileges temporarily
704|   - Notify identity owner / service account manager
705|
706|4. ESCALATE
707|   - Critical severity → notify CISO within 15 min
708|   - High severity → notify Identity Risk Analyst + Pillar Lead within 1 hour
709|   - Medium severity → track in risk register for next triage cycle
710|```
711|
712|### 16.5 Integration with Incident Response
713|
714|Identity threat records feed into:
715|
716|- **IR escalation** (per CERG-PLN-IR-001): confirmed compromise of privileged identity triggers full IR activation
717|- **Risk register** (per CERG-PRC-RM-001): residual risk of identity threats with compensating controls
718|- **Exposure management** (per CERG-PRC-VM-001): identity-related vulnerabilities (stale credentials, excessive permissions)
719|- **Metric PL-007** (per CERG-GOV-MTR-001): privileged account anomaly rate reported quarterly
720|
721|
722|## Revision History
723|648|
724|649|| **Version** | **Date** | **Author** | **Change Summary** |
725|650||---|---|---|---|
726|651|| 1.0 Draft | 2026-05-22 | Cyber Risk | Initial release. Establishes source management, intake fields, triage outcomes, relevance-based prioritization, tailored intelligence products, action tracking, integration with CERG processes, metrics, and canonical role responsibilities for threat intelligence. |
727|652|| 1.1 Draft | 2026-05-26 | Cyber Risk | Added Section 9 (Intelligence-Driven Program Reprioritization): quarterly threat landscape assessment, reprioritization decision framework, decision record, verification, and integration with lessons learned. Added Section 10 (External Collaboration and Information Sharing): ISAC/ISAO membership requirements, peer benchmarking, external incident learning, community contribution, and information sharing boundaries. Renumbered subsequent sections. Updated supporting documents to include PRC-LL-001, IMPREG-001, and GOV-CAL-001. Addresses NIST CSF Adaptive gaps in intelligence-driven program change and bidirectional information sharing. |
728|653|
729|654|### Review Triggers
730|655|
731|656|- Material change to the organization's threat landscape
732|657|- Significant change to threat intelligence sources
733|658|- Significant incident showing an intelligence gap
734|659|- Change to exposure management, threat modeling, third-party risk, or risk-register processes
735|660|- Direction from the CISO
736|661|
737|662|Cyber Risk owns this document. The Risk Pillar Leader is responsible for initiating reviews, managing the revision cycle, and obtaining Governance Pillar Leader approval, with CISO endorsement, for all changes.
738|663|
739|664|### Related Documents
740|665|
741|666|| **Document** | **ID** | **Relationship** |
742|667||---|---|---|
743|668|| Cybersecurity Policy | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
744|669|| CERG Operating Model | [`CERG-GOV-OM-001`](../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) | Defines Threat Intelligence Analyst role |
745|670|| Exposure Management Procedure | [`CERG-PRC-VM-001`](CERG-PRC-VM-001_Exposure_Management_Procedure.md) | Consumes vulnerability intelligence |
746|671|| Threat Modeling Procedure | [`CERG-PRC-TM-001`](CERG-PRC-TM-001_Threat_Modeling_Procedure.md) | Consumes threat actor and abuse-case context |
747|672|| Third-Party and Supply Chain Risk Procedure | [`CERG-PRC-TPRM-001`](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) | Consumes supplier and vendor intelligence |
748|673|| Risk Register and Exception Process | [`CERG-PRC-RM-001`](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Tracks residual risk from intelligence-driven findings |
749|674|| Logging, Monitoring, and Detection Standard | [`CERG-STD-LM-001`](../standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) | Receives detection leads from intelligence |
750|675|| Lessons Learned and Program Improvement Procedure | [`CERG-PRC-LL-001`](CERG-PRC-LL-001_Lessons_Learned_and_Program_Improvement_Procedure.md) | Intelligence assessments feed the quarterly aggregation |
751|676|| Program Improvement Register | [`CERG-GOV-IMPREG-001`](../governance/CERG-GOV-IMPREG-001_Program_Improvement_Register.md) | Records intelligence-driven program changes |
752|677|| Annual Security and Governance Calendar | [`CERG-GOV-CAL-001`](../governance/CERG-GOV-CAL-001_Annual_Security_and_Governance_Calendar.md) | Aligns quarterly assessment cadence |
753|678|| Document Catalog and Naming Convention | [`CERG-GOV-CAT-001`](../governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Registers this artifact and the `TI` domain |
754|679|
