# Buy: Vulnerability Management Turned Back Toward the Tester

**Niche:** Remediation Verification
**Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Vulnerability management platforms already track findings to closure inside the client and have no channel back to the firm that raised them.
**Tags:** #evaluation-metrics #survival-analysis #confidence-intervals #gradient-boosting #data-integration #workflow-orchestration #compliance
**Contested on:** Whether a firm can demonstrate that its findings get fixed, that the fixes hold, and that the same weakness class stops recurring.

## The Problem

The client side of this problem is well served. Vulnerability management platforms ingest findings from scanners, penetration tests and bug bounties, deduplicate them, route them to owners, track them to closure, and report mean time to remediation. They are mature, widely deployed, and they hold exactly the data a testing firm needs.

The data never flows back. A penetration test report is imported as a set of items, worked through the client's process, and closed. The firm that produced the findings receives nothing — not a closure notification, not a remediation rate, not a signal that a finding was disputed or accepted as risk. The relationship is a one-way import.

So the client has remediation analytics for their own estate, the firm has none across its portfolio, and the party best placed to say whether a given class of weakness is fixable in practice — the firm that has watched thousands of organisations try — is the only one with no data.

## What Already Exists

Vulnerability management and risk-based prioritisation: Kenna, Nucleus Security, Vulcan Cyber, Brinqa, Seemplicity, and the vulnerability modules inside the large platforms. These handle ingestion from many sources, deduplication, ownership routing, SLA tracking and closure reporting.

Application security posture management: the newer category consolidating findings across the software lifecycle, with strong repository and pipeline integration — which is where the join between a finding and the commit that fixed it would actually be made.

Penetration testing delivery platforms: Cobalt, Synack, HackerOne's assessment products and the platforms firms use internally, which structure findings and in some cases offer client-side tracking — the closest existing bridge and still oriented to delivery rather than to outcome.

Ticketing and repositories: Jira, ServiceNow, GitHub and GitLab, which hold the actual remediation record and are already integrated into all of the above.

## The Customization Gap

**Tenancy is inverted.** These platforms are client-tenanted, one instance per organisation. A testing firm needs a firm-tenanted view across many clients, each isolated, with de-identified aggregate analysis across the portfolio. That inversion is the core adaptation and nothing in the category supports it.

**No outbound channel to the finding's author.** Findings flow in and nothing flows out. A simple, permissioned outbound feed — this finding closed, disputed, accepted as risk, reopened — would give firms most of what they need and is a small feature nobody has built because no vendor's buyer has asked for it.

**Closure is not verification.** These platforms record that a ticket closed, which is a statement about a workflow rather than about the weakness. Verifying that the fix actually closed the vulnerability requires a re-probe, which sits with the testing firm and is not connected to the closure event.

**Class recurrence is not modelled.** Platforms deduplicate to avoid double-counting the same finding. What matters here is the opposite: recognising that a new finding in a new location is the same class as one fixed last year. That is a taxonomy and trend capability the category deliberately does not have.

**Regression detection is absent.** A closed finding that reappears is typically ingested as a new item. Distinguishing a regression from a fresh finding is essential to the durability question and is nowhere in the data model.

**Cross-client benchmarking is the valuable output and is contractually delicate.** Which finding classes are remediated fastest across organisations of a given shape is what the portfolio view produces, and it requires de-identification rigorous enough to satisfy every client whose data contributed.

## Target Customer

The penetration testing delivery platforms are the most natural adapters — Cobalt, Synack and the internal platform vendors already serve testing firms, already structure findings, and a remediation outcome loop is the obvious extension of their existing client-side tracking.

The vulnerability management vendors have the better data position and the wrong buyer; an outbound findings-status feed would be a small feature for them and would enable the whole category.

Buyers are testing firm leadership, with client security leadership as a willing participant because the class recurrence analytics are genuinely more useful to them than what they currently have.

## Impact If Solved

The data that already exists reaches the party that needs it. This is a plumbing problem rather than a research one, which makes it unusually tractable for the change it produces.

An outbound status feed alone would give firms remediation rates by finding type across their whole portfolio, which is the single most useful thing they could learn about their own work.

And class recurrence tracking would give both sides the diagnostic that matters: whether the client's engineering process is learning, which is a more important question than whether any particular instance was patched.
