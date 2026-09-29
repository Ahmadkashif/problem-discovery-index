# History: Crowdsourcing Platforms

**Industry:** [[industries/crowdsourcing-platforms|Crowdsourcing Platforms]]
**Primary Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**Secondary Wave:** [[series/eras/wave-12-transformers|12 — Transformers]]
**Episode Tier:** 1
**Transferable Pattern:** The party holding the measurement withholds it from the person whose livelihood it governs — and where a worker builds their own patch for the gap, whether the platform helps or blocks it tells you whether you are looking at an oversight or a decision.

> **Origin Parent — omitted.** None of the eighteen `origins/` industries has a real claim. Distributed, uncompensated task-work has pre-digital antecedents — prize contests, the Victorian-era compilation of the Oxford English Dictionary from thousands of volunteer readers — but no single 20th-century corporate industry in the spine is this one's ancestor. It was built, named, and later re-purposed entirely within the span this vault already covers.

## Before

The pre-digital precedents were real but episodic: a prize competition, a call for volunteer readers, a one-off public appeal — never a continuous, monetised labour market that a person could work for hours a day. What digital crowdsourcing added was not the idea of distributed task-work; it was making it **continuous, priced per unit, and available on demand from a global pool of contractors with no employment relationship attached.**

## The Origin Event — a Platform Before It Had a Name

**Amazon Mechanical Turk launched on 2 November 2005.** The idea, credited to a 2001 patent disclosure by Venky Harinarayan and championed internally by Jeff Bezos, solved an unglamorous internal problem: Amazon's own product catalogue held large numbers of duplicate listings that software could not reliably detect, but a human glancing at two pages could tell in seconds.

The platform's name is a precise joke about what it does. The original **Mechanical Turk** was an 18th-century chess-playing automaton built by Wolfgang von Kempelen that appeared to think for itself — and in fact concealed a human chess master hidden in the cabinet beneath the board. Amazon's version does not hide the trick; it names it and sells it. A requester's task runs through an API and returns a result that looks machine-produced, and Amazon coined its own internal term for the process: **"artificial artificial intelligence."**

The category did not have its name yet when the platform launched. **"Crowdsourcing" was coined seven months later**, in a June 2006 *Wired* piece by Jeff Howe and Mark Robinson — meaning the platform that would come to define the category existed before the word describing it did. It is the same shape as this vault's own finding on "SaaS," coined in print in February 2001, two years after Salesforce had already founded the model it would go on to name.

## What Became Cheap

Hiring, for a task lasting seconds, at global scale, with no minimum engagement, no interview and no employment relationship — HITs ("Human Intelligence Tasks") posted by "requesters," completed by "Turkers" classified everywhere as independent contractors.

## How It Was Actually Solved, and Who Solved the Part the Platform Didn't

Quality control runs on gold-standard questions, inter-annotator agreement and approval-rate gating — all built and controlled by the requester or the platform. What is not built by the platform is everything a worker would need to protect themselves: which requesters pay reliably, which reject in bad faith, whether a task's stated time estimate is honest. Workers built that layer themselves. **Turkopticon**, launched in 2008 by Lilly Irani and Six Silberman, lets workers rate requesters — a reputation system running in the one direction the platform's own design left empty. **Dynamo** organised workers around campaigns including a "Guidelines for Academic Requesters" push and a public "Dear Jeff Bezos" letter.

**Amazon's own response to these tools is the sharpest, most concrete evidence in this entire batch that the asymmetric hold is a policy choice, not an engineering gap.** Rather than build the requester-reputation feature its own workforce had already proven was wanted and useful, Amazon changed its site in ways that broke the browser extensions Turkopticon and Dynamo relied on, and made it harder to enrol in Dynamo by closing the account mechanism that supplied a required code. The platform did not lack the capability to show workers a requester's history — it holds both halves of that data, for every requester, at all times. It chose to make the workers' own patch for the gap harder to run.

## Why the Rejection Problem Is a Design Choice, Not a Software Limit

This vault's own hub note calls rejection "the sharpest feature" of this market, and the mechanism deserves to be stated exactly: a requester may reject submitted work, which withholds payment for labour already performed, and on platforms where approval rate gates access to better-paid task pools, a rejection also damages future earning capacity — and it can arrive with no reason given and no appeal route to the platform itself.

Reported rejection rates are, in aggregate, low — worker surveys have put it as low as roughly 1% of submissions — but an aggregate rate is the wrong number to reason from. It says nothing about whether the rejections that do happen are concentrated among a small number of bad-faith requesters against whom a given worker has no recourse at all, and the worker-built tooling above exists precisely because the platforms never answered that question themselves. **Amazon could build an appeals process. It has not, and the likelier reason is liability, not capability** — a human-reviewed appeals system creates a cost and a dispute-adjudication obligation that the current unilateral-requester design avoids entirely.

## The Graveyard — a Thesis, Not a Company

Nothing here shut down the way Convoy did. What changed is the market's centre of gravity. **CrowdFlower**, founded 2007, rebranded as **Figure Eight** in 2017 and was acquired by **Appen** in 2019 — a straight line from "crowdsourced market-research and business-process tasks" toward "labelled training data for machine learning models," now the industry's dominant commercial reason to exist. **Prolific**, founded 2014, deliberately did not chase that shift; it built pay floors and participant-treatment standards specifically for academic research use, differentiating on the opposite axis from where the money was moving — a fact this vault's own hub note already records as "a meaningful differentiation in this market."

The general-purpose, market-research-era crowdsourcing platform is the thing that quietly died here — not a company, a use case, absorbed into a much larger and more lucrative one that [[series/eras/wave-12-transformers|Wave 12]] created.

## What's Still Open

- [[problems/crowdsourcing-platforms/high-impact|🔴 Pay Is Set Per Task by Someone Who Does Not Know How Long It Takes]]
- [[problems/crowdsourcing-platforms/worker-life-1|🟢 The Worker Whose Submission Was Rejected Without a Reason]]
- [[problems/crowdsourcing-platforms/worker-life-2|🟢 The Requester Who Cannot Tell Whether Their Data Is Any Good]]
- [[niches/crowdsourcing-platforms/pay-setting-and-rate/profile|Pay Setting & the Realised Rate]]
- [[niches/crowdsourcing-platforms/requester-reputation/profile|Requester Reputation & Trust]]
- [[niches/crowdsourcing-platforms/verification-and-fraud/profile|Worker Verification & Fraud Control]]
- [[niches/crowdsourcing-platforms/task-design-and-quality/profile|Task Design & Quality Enforcement]]
- [[niches/crowdsourcing-platforms/the-crowdworker/profile|The Crowdworker]]
- [[niches/crowdsourcing-platforms/the-requester/profile|The Requester]]

## The Transferable Pattern

> **The party holding the measurement withholds it from the person whose livelihood it governs — and where a worker builds their own patch for the gap, watch whether the platform helps or blocks it. The answer tells you whether you are looking at an oversight or a policy.**

This is the asymmetric hold in its most legible form anywhere in this vault, because the platform's reaction to Turkopticon and Dynamo removes the ambiguity other industries in this batch still carry. An FDE should treat "the platform could build this but hasn't" and "the platform noticed workers building this themselves and blocked it" as two very different findings. The first is a backlog. The second is a decision, and no ML model changes a decision.

**Sources:** Wikipedia, *Amazon Mechanical Turk*, *Crowdsourcing*; *Wired* (Jeff Howe and Mark Robinson, coining "crowdsourcing," June 2006); company histories, CrowdFlower / Figure Eight / Appen, Prolific; this vault's `industries/crowdsourcing-platforms.md` and `problems/crowdsourcing-platforms/*.md`.
