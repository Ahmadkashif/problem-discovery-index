# Lineage: Cloud Infrastructure Consultants

**Industry:** [[industries/cloud-infrastructure-consultants|Cloud Infrastructure Consultants]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** the AWS Well-Architected Framework — a fixed set of pillar-by-pillar review questions, published 2 October 2015, and the Well-Architected Tool (29 November 2018) that turns the questions into a scored workload review and improvement plan
**Builder:** Amazon
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

An architecture review used to be the most expensive hour a consultancy sold, because it lived in one person's head.

A senior architect walked into a client's estate, read the account structure, the network diagram and the bill, and said what was wrong: this database has no standby, this bucket is public, these instances are three sizes too large. There was no shared checklist to hand a junior, no common vocabulary with the client, and no way to say the review was *finished*. Two architects reviewing the same estate produced two different documents.

For a cloud provider the same bottleneck was worse. Its own solutions architects were the people customers asked to do these reviews, and their number did not scale with the number of accounts.

## What Got Built

A questionnaire with a name.

AWS published the Well-Architected Framework on **2 October 2015**, announced by Jeff Barr. It was organised into **four pillars — Security, Reliability, Performance Efficiency and Cost Optimization** — each defined in a sentence and broken into "foundational questions" against which a system could be measured. Operational Excellence was added as a fifth pillar before the tool launched; Sustainability later made six.

On **29 November 2018** AWS turned the document into software. The **Well-Architected Tool**, free in the console, let a user define a workload, answer the multiple-choice questions, and receive an improvement plan and a PDF report listing high-risk issues. AWS's launch post said the aim was to make reviews that had been "available only through AWS Solutions Architects" self-service, because demand for them outstripped supply.

The **Well-Architected Partner Program** then made the review a thing consultancies deliver: AWS's current page describes partners "conducting reviews" against the framework for their clients.

## Who Built It, And Why Them

Amazon, and the reason is headcount arithmetic.

AWS's launch post credits the framework to **AWS Solutions Architects distilling what they had learned from working with thousands of customers.** The people who built it were the people drowning in the requests. Codifying their judgement into questions let AWS do three things no consultancy could do alone: make the review repeatable, make it free, and make it a standard that every partner firm would teach and deliver.

That last move is the business case. A provider whose revenue depends on customers staying and growing needs estates that do not fall over, leak or overspend and then churn. Its own architects cannot reach every account; a field of partner consultancies can. **A published checklist is how a seller recruits a channel** — it gives every partner the same deliverable, the same vocabulary and a reason to be invited in.

A consultancy could not have authored it: no single firm had the cross-customer view, and none could have made a rival adopt its questions.

## What It Cost

**The review measures conformity to the seller's own best practice.** The questions are written by the party that sells the capacity, including the cost pillar. A workload can answer every question correctly and still be expensive in ways the questionnaire does not ask about.

The multiple-choice format also flattened the senior architect's skill into boxes. It made reviews scalable by making them generic — the same questions for a two-person startup and a regulated bank — and left ranking the findings by business impact to the consultant.

And it is single-provider by construction: an estate spread across three clouds gets three frameworks.

## What You Still Touch

Every consultancy's "Well-Architected Review" line on a statement of work, every high-risk-issue list handed to a client, and every generic finding a firm has to re-rank by hand descends from a checklist written to multiply one provider's architects.

- [[problems/cloud-infrastructure-consultants/high-impact|🔴 Cloud Cost Optimization & Right-Sizing Intelligence]] — the senior-architect judgement the questionnaire could not encode
- [[problems/cloud-infrastructure-consultants/low-impact-2|🟡 Multi-Cloud Compliance Posture Management]] — findings without client context, at scale
- [[niches/cloud-infrastructure-consultants/hyperscaler-partner-research/profile|Hyperscaler Partner & Solutions Research]]
- [[niches/cloud-infrastructure-consultants/enterprise-migration-partners/profile|Enterprise Migration Partners]]
- [[niches/cloud-infrastructure-consultants/multi-cloud-cost-optimizers/profile|Multi-Cloud Cost Optimizers]]

**Sources:** Jeff Barr, "Are You Well-Architected?", AWS News Blog, 2 October 2015 (four launch pillars; authored by AWS Solutions Architects from work with thousands of customers); Jeff Barr, "New – AWS Well-Architected Tool – Review Workloads Against Best Practices", AWS News Blog, 29 November 2018 (five pillars; questionnaire, improvement plan, PDF report; reviews previously available only through AWS SAs); AWS Well-Architected product page, fetched September 2026 (six pillars; Partner Program partners conduct reviews). ⚠️ **WebSearch was unavailable this session (session cap reached)**; research was by direct fetch only. ⚠️ **Not established:** the date Operational Excellence was added (between the 2015 and 2018 posts — no exact date confirmed); the launch date of the Well-Architected Partner Program; the names of the individual solutions architects who wrote the 2015 framework; and any AWS-funded partner review incentives, which I did not confirm and do not assert. Wikipedia, *Amazon Web Services*, dates the AWS Partner Network to 2014; I could not reconcile that against an AWS primary source and do not rely on it.
