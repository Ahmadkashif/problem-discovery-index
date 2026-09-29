# Policy Change Propagated Across an Open Caseload

**Niche:** [[niches/legal-practice-software/immigration-practice-platforms/profile|Immigration Practice Platforms]]
**Industry:** [[industries/legal-practice-software|Legal Practice Software]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** When immigration policy changes, a firm with 400 open cases works out which ones are affected using a spreadsheet and institutional memory, because no platform models a case's procedural posture as something a policy can be evaluated against.
**Tags:** #large-language-models #bert #graph-theory #evaluation-metrics #confidence-intervals #compliance #workflow-orchestration #automation
**Contested on:** Every serious competitor in immigration case management is fighting to keep an open case's forms, evidence set and procedural posture correct when the policy underneath it changes mid-case — and whoever propagates a policy change across an active caseload fastest takes the account.

## The Problem
A policy manual update, a court injunction or a change in adjudicative practice lands. It affects some categories of pending case and not others, depending on filing date, benefit type, the applicant's status and where the case sits in its lifecycle. The firm's response is a partner reading the change, forming a view of who is affected, and a paralegal filtering a case list on the closest available fields — which are case type and status, neither of which captures the distinctions the policy draws. The filtering is approximate in both directions, and both directions are harmful: a client wrongly told they are affected, and a client affected who was never contacted.

## Why Nobody Has Built This
Case management systems model a case as a type plus a status, which is enough for a workflow and insufficient for a policy evaluation. Representing posture properly means modelling filing dates, benefit categories, prior filings, the applicant's status history, dependants, and jurisdiction as structured facts — a data model nobody has built because no product ever needed it. On the other side, the policy corpus is genuinely messy: the authoritative sources are a policy manual, a federal register, agency memoranda and court orders, none published in a form designed for machine consumption. Doing this well requires holding both halves, and vendors have held neither.

## What to Build
Two structures and the join between them. A case posture model that records the facts a policy can discriminate on, maintained as dated state rather than as current status, so a case's posture at filing and its posture today are both recoverable. And a policy model in which each change is expressed as a scope — which benefit categories, which filing date ranges, which postures — plus an effect. Applying a policy to the caseload is then a query, returning the affected cases with the reasoning shown, ranked by urgency. Extraction from the source documents proposes the scope for a lawyer to confirm; it never applies a change unreviewed, because an incorrect scope silently misinforms hundreds of people about their immigration status. The system also keeps the history, so a firm can answer what policy governed a case at each point in its life — which is the question that arises in litigation.

## Target Customer
Immigration case management vendors, mid-size and large immigration firms, and the nonprofit legal service providers who carry the highest caseloads per lawyer in the practice area.

## Impact If Built
The first affected-case query that takes minutes instead of a week changes how a firm can respond to a policy change at all — the difference between contacting affected clients within days and finding them over a month. The dated posture model is also the foundation for everything else in this niche, since evidence sufficiency and RFE prediction both depend on knowing what standard applied when.
