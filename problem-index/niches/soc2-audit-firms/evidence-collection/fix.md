# Fix: That Is Not What We Asked For

**Niche:** Evidence Collection & Request Management
**Industry:** [[industries/soc2-audit-firms|SOC 2 & Attestation Audit Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The request is phrased in audit language, the client produces what they think it means, it is rejected, and the cycle costs a week per item.
**Tags:** #evaluation-metrics #compliance #workflow-orchestration #worker-facing #automation #confidence-intervals
**Contested on:** Whether evidence is pulled from connected systems or requested, chased and received as files.

## The Problem

The request says: provide evidence that logical access reviews were performed for in-scope systems during the period.

The client's compliance manager reads it. Which systems are in scope — they think they know. What counts as evidence of a review — a screenshot, an export, an email thread, a ticket. What period — the whole one, or a sample. Whether the reviewer must be named. They make reasonable choices and produce a set of screenshots.

The associate opens them a week later. They do not show the reviewer, and one is from outside the period. Rejected, with a clarification. The client produces something else. It arrives a week after that.

Two weeks for one item, three exchanges, and a compliance manager who has now spent hours on a request that could have been answered in ten minutes if they had been told what was needed.

The specific version takes the same length to write. Export the quarterly access review from the identity platform for the production environment, covering these four quarters, showing the reviewer name and the completion date for each. No interpretation required, no rejection, no second exchange.

## Why It's Still Broken

**Requests come from a generic programme.** Standard audit programmes express requests in control language because they must apply to every client, and nobody rewrites them per engagement.

**The auditor may not know the client's systems well enough.** Writing a specific request requires knowing which system holds what, which the auditor learns during the engagement.

**Nothing records what satisfied it last time.** The same request was answered correctly last period and the accepted artefact is in last year's workpapers, unavailable to the person writing this year's request.

**Rejection is cheap for the auditor.** The cost of an unclear request falls on the client's time and on the engagement calendar, not on the person who wrote it.

**Sufficiency is not stated because it varies.** What satisfies a request depends on the control and the reviewer, and nobody has written it down.

**The elapsed time is absorbed.** Weeks of exchange disappear into the engagement calendar and the client's frustration, and neither appears in any metric.

## What a Fix Looks Like

**Write requests that name the system and the artefact.** System, artefact, period, and the fields it must show. Same effort to write, no interpretation required, and it eliminates most rejections.

**Attach last period's accepted artefact.** For every recurring request, show what was accepted before. The client confirms or updates rather than guessing, which turns a two-week cycle into a same-day confirmation.

**State the sufficiency criteria.** What the evidence must demonstrate for the test to pass. This is known to the auditor and is almost never communicated.

**Build the request list from the client's system inventory.** Requests generated against the specific systems rather than against generic control language, which requires knowing the estate and is worth the scoping effort.

**Let the client ask before producing.** A quick clarification channel with a fast response is far cheaper than a rejection cycle, and most clients would use it.

**Measure the rejection rate.** Requests rejected and re-requested, per engagement. The number would be large, is not tracked anywhere, and is the evidence that would justify rewriting the request library.

**Fix the request library once.** The same ambiguous requests recur across every client. Rewriting them specifically, once, as a firm-level asset, removes the problem permanently rather than per engagement.

## Who Feels the Pain

The client's compliance manager, spending hours producing evidence that is rejected, then producing it again, for a request they could have answered immediately if told what was wanted.

The associate, chasing items and reviewing evidence that does not answer the test, several weeks into an engagement with a deadline.

The engagement calendar, which is determined far more by the exchange cycle than by the testing.

And the client's engineering colleagues, asked repeatedly for the same thing in slightly different forms.

## Impact If Fixed

Naming the system and the artefact takes the same time to write and eliminates most of the rejection cycle, which is the largest source of elapsed time in an engagement.

Attaching last period's accepted artefact turns a recurring request into a confirmation, and most requests recur.

And rewriting the firm's request library once, specifically, fixes the problem for every client and every future engagement rather than being solved individually and repeatedly by whoever is chasing.
