# Buy: Engineering Analytics Turned Outward

**Niche:** Technical Assessment
**Industry:** [[industries/fractional-cto-services|Fractional CTO Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Engineering analytics platforms already compute most of what an assessment needs and are built for teams measuring themselves continuously, not for an outsider with two weeks and no admin rights.
**Tags:** #gradient-boosting #time-series-forecasting #evaluation-metrics #confidence-intervals #data-integration #automation #workflow-orchestration
**Contested on:** Whether the advisor's picture of the system is built from evidence the organisation already produces or from reading and asking.

## The Problem

The metrics a fractional CTO needs are not exotic. Change concentration, defect localisation, cycle time, review latency, work-in-progress, deployment frequency, recovery time — these are the standard outputs of a mature engineering analytics category with well-funded vendors and years of refinement. The advisor is not short of a metric definition. They are short of a way to get any of it in the eight weeks they are present.

So the metrics go uncomputed. An advisor who suggests installing an analytics platform for the duration of an assessment is asking a client mid-crisis to procure software, grant repository and tracker access to a third-party vendor, pass a security review, and wait a quarter for enough data to mean anything. The engagement is over before the trial ends. The practitioner reads the code instead.

The result is a category whose entire output would improve an adjacent profession, sitting behind an adoption model that profession cannot use.

## What Already Exists

Engineering intelligence platforms — LinearB, Swarmia, Jellyfish, Code Climate Velocity, DX, Haystack and the metrics layers inside GitHub, GitLab and Atlassian — compute DORA metrics, cycle time breakdowns, review dynamics, investment allocation across work types, and in some cases code-level hotspot analysis. Several are genuinely good. CodeScene deserves separate mention because its behavioural-code-analysis approach — hotspots from change frequency, temporal coupling from co-change, knowledge distribution from authorship — is the closest existing thing to an assessment instrument and is sold to teams rather than to advisors.

Static analysis platforms cover structural quality. Dependency and supply-chain scanners cover a slice of risk. Issue tracker reporting covers flow, badly. Repository mining research has produced a well-validated literature on defect prediction and coupling detection that almost none of these products fully exploit.

## The Customization Gap

**Cold start against a warm-start product.** Every platform in the category assumes continuous operation: install the agent, connect the accounts, watch trends emerge over months. The advisory use is a single deep read of history already recorded, delivered in days. The technical work is mostly reinterpretation — a platform that can compute a rolling four-week cycle time can compute an eighteen-month retrospective, and simply does not present one, because that is not the product.

**Tenancy is inverted.** These are client-tenanted products. The advisor needs a practitioner-tenanted one: many client estates, each isolated, each disposable at engagement end, all under a single practice account. The access model, the billing model and the data lifecycle all point the wrong way.

**The output is a dashboard, not an exhibit.** A team improving itself wants a live view. An advisor wants a defensible artefact: the finding, the evidence behind it, the period it covers, the caveats, formatted to sit inside a report that a board or an investment committee will read. Nothing in the category exports an assessment exhibit; the screenshot-into-slides workflow is universal and awful.

**Benchmarks are the missing half.** A number without a reference point is not a finding. Platforms that have benchmarks derive them from their installed base of client teams, which is a different population from the mid-market companies an advisor typically assesses, and they are not exposed in a form an advisor can cite.

**Access rights the advisor does not have.** Most platforms require an org-level integration the client's security team must approve. An assessment instrument has to work from a clone and an export — artefacts a client engineering lead can produce personally in an afternoon under an existing NDA.

**No place for what the advisor knows.** Interview evidence, architectural context, the strategic question driving the engagement — none of it has anywhere to live. The measurements sit in one system and the judgement they inform sits in a document, which is exactly why the two are never reconciled.

## Target Customer

The vendor with the most to gain is CodeScene or a similar behavioural-analysis specialist, whose core technique is already the right one and whose commercial position — a strong tool in a crowded team-analytics market — would be improved by a channel that puts it in front of a new company every eight weeks.

On the buy side, boutique advisory practices and private equity technical operating groups, who will pay per-engagement rates that look extravagant next to per-seat SaaS pricing because the alternative is another week of a senior practitioner's time.

## Impact If Solved

An advisor arrives, requests a clone and an export under the existing NDA, and has hotspots, temporal coupling, knowledge concentration and flow measurements before the first full day of interviews — which turns the interviews into tests of specific hypotheses rather than an open fishing expedition.

For the vendor, the advisory channel is a demonstration engine. Every assessment shows a company its own engineering data for the first time, in a moment of maximum receptiveness, and some meaningful fraction of those companies become direct customers of the continuous product afterwards.
