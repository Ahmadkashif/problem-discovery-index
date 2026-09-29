# A Report With No Stated Validity

**Niche:** [[niches/ai-red-teaming-firms/assessment-revalidation/profile|Assessment Revalidation]]
**Industry:** [[industries/ai-red-teaming-firms|AI Red Teaming Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Assessment reports carry a date and no statement of what they apply to or what would invalidate them, so they are cited indefinitely about systems that have since changed in every respect.
**Tags:** #compliance #evaluation-metrics #descriptive-statistics #confidence-intervals #quick-win #automation #hypothesis-testing #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to re-establish an assessment's conclusions after the system changes, at a fraction of the original cost — and whoever does that takes the account, because the alternative is a report that expires on the client's next model upgrade.

## The Problem
A report is cited in a regulatory filing eighteen months after it was written. In the interim the client changed model version twice, added three tools, restructured their prompt and changed retrieval. The report says none of that would matter, because it says nothing about it. It names a date and a system by its product name. Everybody in the chain treats it as current because nothing in it says otherwise, and the firm that wrote it would be horrified to see what it is being used to support.

## Why It's Still Broken
Stating validity conditions shortens a report's useful life, which is commercially unwelcome and is precisely the point. No convention exists, so a firm that adds a validity statement looks like it is hedging. Clients want a durable artefact for their compliance file and a bounded one is worth less to them in the short term. And the misuse happens downstream where the firm never sees it.

## What a Fix Looks Like
State what the report applies to and what ends it. Include a configuration statement naming the exact model version, application version, prompt version, tool set and retrieval configuration assessed, which is a paragraph and is the minimum honest content — a report that does not say what it assessed cannot be misapplied honestly or otherwise. List the changes that invalidate the assessment explicitly, so a client knows when to come back and a downstream reader knows when to stop relying on it. State an expiry date reflecting how fast the field moves, since even an unchanged system faces a changing technique landscape and a two-year-old clean report is not evidence of present robustness. Mark each finding as version-specific or structural, so a reader can tell which conclusions would survive a change. Offer a revalidation path in the report itself, which converts the expiry from a limitation into a service. Provide a short current-status attestation that can be re-issued cheaply, which is what the compliance file actually needs and is a better product than a stale long report. Push for a convention across firms, since unilateral honesty is penalised and a norm removes that. And track where reports are cited, because a firm whose work is supporting claims it does not make has a reputational exposure it cannot currently see.

## Who Feels the Pain
Regulators and boards relying on reports about systems that no longer exist; firms whose work is cited to support conclusions they did not reach; and clients who did not know their upgrade ended their assurance.

## Impact If Fixed
A configuration statement and an invalidating-change list are a paragraph each and are the minimum honest content of a report. A cheaply re-issued current-status attestation is a better compliance artefact than a stale long report and turns the expiry into a service.
