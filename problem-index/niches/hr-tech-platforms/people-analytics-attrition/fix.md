# Internal Mobility Nobody Measures

**Niche:** [[niches/hr-tech-platforms/people-analytics-attrition/profile|People Analytics & Attrition]]
**Industry:** [[industries/hr-tech-platforms|HR Tech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Internal movement is the strongest retention lever an organisation fully controls, every move is recorded in the system of record, and almost no company measures its own internal mobility rate or knows which paths are open and which are closed.
**Tags:** #descriptive-statistics #graph-theory #survival-analysis #evaluation-metrics #confidence-intervals #hypothesis-testing #quick-win #worker-facing
**Contested on:** Every serious competitor in people analytics is fighting to diagnose the structural conditions that produce attrition months before the resignations — and whoever names the condition rather than scoring the person takes the account.

## The Problem
An employee three years into a role wants something different. They look internally, find postings that require experience they cannot get in their current role, apply to two, hear nothing from one and are declined by the other because their manager was not consulted and objected. They leave for a comparable role at another company. The organisation records a voluntary exit, replaces them externally at a premium, and the pattern repeats across a job family where the internal path has been effectively closed for years. Every move that did and did not happen is in the system, and the mobility structure — which roles feed which, how often, and where the dead ends are — has never been computed.

## Why It's Still Broken
Internal mobility is discussed as a culture and policy matter rather than as a measurable structure, and the HCM systems record transfers without anyone assembling them into a graph. The internal-applicant experience is handled by the recruiting system, which is optimised for external hiring. And there is a well-known organisational disincentive: managers lose good people when internal mobility works, so the process routinely depends on the consent of the person with the strongest reason to withhold it, which is a structural problem nobody has instrumented.

## What a Fix Looks Like
Compute the mobility graph and publish it. Every internal move over several years, as a graph of job families and levels, with volumes — which reveals immediately which roles are hubs, which are dead ends, and which paths exist in the career framework and never actually occur. Measure the internal fill rate by job family and by level, and the internal applicant funnel: applied, screened, interviewed, hired, with the drop-off points. Track manager blocking explicitly rather than informally, since it is the most cited obstacle and is currently invisible — an aggregate rate of internal applications that stall at manager approval is a fact about the organisation, not an accusation. And give the employee the graph: which roles people in their position have actually moved into, with volumes and typical tenure before the move, which is the single most useful career artefact a company can offer and is derivable from data it already holds.

## Who Feels the Pain
Employees who looked internally, found nothing, and left; managers who lose people to competitors rather than to colleagues; and talent leaders who believe in internal mobility and cannot say whether their organisation has any.

## Impact If Fixed
The mobility graph is a query over transfer history and it consistently surprises organisations — paths they believe exist turn out to be unused, and roles they consider entry-level turn out to be terminal. Publishing it to employees is the part with the most direct retention effect and costs nothing beyond the willingness to show people where they could actually go.
