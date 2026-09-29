# Lineage: Data Analytics Consultants

**Industry:** [[industries/data-analytics-consultants|Data Analytics Consultants]]
**Wave:** [[series/eras/wave-07-big-data|7 — Big Data]]
**The tool:** CRISP-DM 1.0 — the CRoss-Industry Standard Process for Data Mining, a six-phase project model (Business Understanding → Data Understanding → Data Preparation → Modeling → Evaluation → Deployment) with named deliverables at every task, published by its consortium in August 2000
**Builder:** CRISP-DM consortium
**Builder in vault:** **ABSENT**
**Verification:** verified — primary document, see Sources

## The Problem That Came First

In the mid-1990s data mining was a service before it was a discipline. The people doing it for clients had each, in their own words, "developed our approaches to data mining as we went along."

That was tolerable while the market was small. It stopped being tolerable when, as the authors put it, early interest was "showing signs of exploding into widespread uptake." A consultant selling a project to a new client could not point to any shared description of what the project would contain, how long each part would take, or what would be handed over at the end. **The buyer was being asked to trust a process that existed only in the seller's head** — and every new adopter looked set to learn it again "by trial and error."

## What Got Built

A process model with deliverables attached.

CRISP-DM breaks a project into six phases, each into generic tasks, each task into named outputs. Data Understanding alone ends in four reports — initial data collection, data description, data exploration and a **data quality report**, which is to "list the results of the data quality verification; if quality problems exist, list possible solutions." Deployment ends in a **final report** that "summarizes and organizes the results" of every previous deliverable.

The guide is explicit that the sequence "is not rigid," and it carries a planning rule of thumb that has outlived most of the document: it is "often postulated that 50-70 percent of the time and effort in a data mining project is used in the Data Preparation Phase and 20-30 percent in the Data Understanding Phase," with modeling at only 10–20 percent.

## Who Built It, And Why Them

A consortium of three data-mining suppliers and one user, and the foreword says why each was there.

**Daimler-Benz** was already applying data mining in its own operations. **ISL** — later SPSS — had sold data-mining services since 1990 and launched Clementine, which it calls the first commercial data mining workbench, in 1994. **NCR** had built teams of data mining consultants to add value for its Teradata warehouse customers. The Dutch insurer **OHRA** provided a live test bed. CRISP-DM was conceived in late 1996; a year later the group had a consortium, an acronym and European Commission funding, and Wikipedia records it as an ESPRIT project from 1997.

The business case is stated in the suppliers' own voice: "from a supplier's perspective, how could we demonstrate to prospective customers that data mining was sufficiently mature to be adopted as a key part of their business processes?" A standard, "non-proprietary and freely available," was a sales instrument for the whole category. That is why the builders were vendors and service arms rather than academics or a standards body: they were the ones whose pipeline depended on customers believing the work was repeatable. By August 2000 SPSS's and NCR's professional-services groups were using it on customer engagements, and it was turning up in RFPs.

## What It Cost

The model made the consulting engagement legible by making the slow part official.

Writing 50–70 percent into the plan for data preparation turned the most expensive phase into an expected cost rather than a problem to be engineered away. And because the model is tool-neutral by design, it says what the data quality report must contain and nothing about how to produce one — the profiling stays manual, engagement after engagement.

## What You Still Touch

A modern analytics engagement still opens with a data audit, still budgets most of its hours for cleaning a client's data, and still closes with a handoff document. Those are CRISP-DM's data quality report, its preparation estimate and its final report, rarely credited.

- [[problems/data-analytics-consultants/high-impact|🔴 Data Quality Assessment Autopilot]] — the data quality report, still hand-built
- [[problems/data-analytics-consultants/low-impact-2|🟡 Data Lineage Documentation Generator]] — the final report as a deliverable
- [[problems/data-analytics-consultants/worker-life-1|🟢 SQL/Python Debugging on Messy Client Data]]
- [[niches/data-analytics-consultants/analytics-maturity-benchmarking/profile|Analytics Maturity Benchmarking]]
- [[niches/data-analytics-consultants/large-si-data-practices/profile|Large Systems Integrator Data Practices]]

**Sources:** Chapman, Clinton, Kerber, Khabaza, Reinartz, Shearer and Wirth, *CRISP-DM 1.0: Step-by-step data mining guide* (the CRISP-DM consortium, © 1999–2000; foreword dated August 2000), read in full text from a university-hosted copy (uni-kassel.de) — the source for the consortium membership (NCR Systems Engineering Copenhagen, DaimlerChrysler AG, SPSS Inc., OHRA), the late-1996 conception, the supplier motive, the trials at Mercedes-Benz and OHRA, the 200-member SIG, the data quality and final report deliverables, and the 50–70 percent estimate; Wikipedia, *Cross-industry standard process for data mining* (ESPRIT funding from 1997; lists Teradata and ISL separately; later practitioner surveys; IBM's ASUM-DM in 2015). WebSearch was unavailable this session (budget exhausted). ⚠️ **Note:** the 50–70 percent figure is presented by the guide itself as a commonly "postulated" estimate, not a measurement; I found no study behind it. Keyed as the consortium because the document names the consortium, not any one member, as its owner.
