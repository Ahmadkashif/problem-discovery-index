# Every Finding Is Dispositioned and No Disposition Comes Back

**Niche:** [[niches/software-dev-agencies/oss-risk-license-compliance-data/profile|Open Source Risk & License Compliance Data]]
**Industry:** [[industries/software-dev-agencies|Software Development Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** Developers mark millions of findings as false positive, not exploitable, or accepted risk every week, and the vendor treats it as workflow state instead of as the largest labelled dataset it will ever have.
**Tags:** #evaluation-metrics #tacit-knowledge-ml #automation #workflow-orchestration #worker-facing

## The Problem
Every scan produces findings, and every finding gets dispositioned. A developer fixes it, upgrades past it, marks it a false positive, marks it not exploitable in this context, or accepts the risk with a reason. This happens continuously, across every customer, at enormous volume.

Each disposition is an expert judgment about the vendor's own output. "Not exploitable here" is a security engineer saying the finding was technically correct and practically irrelevant, and explaining why. "False positive" is a claim the curation was wrong. "Accepted risk" is a statement about how this organisation weighs this class of issue.

The vendor's systems record these as workflow state. The finding moves to a status, the dashboard updates, and the reason — where a reason was even captured — sits in a free-text field nobody reads.

What is lost is precisely what the product most needs. False positive rates by advisory, ecosystem and package are computable and are not computed. Recurring not-exploitable patterns — a class of finding that every customer with a given architecture dismisses — would be a rule, and instead each customer rediscovers it. And the vendor cannot answer the question every prospect asks in every evaluation: what proportion of your findings do teams actually act on.

The same silence surrounds remediation. When a vulnerability is fixed by upgrading, the vendor could observe how long the upgrade took, whether it broke anything, and which upgrade paths customers avoid — the empirical basis for advice better than "upgrade to the latest version".

## Why It's Still Broken
The scanner was built as a detector, and detectors are evaluated on what they find. Nothing in the original design contemplated the finding's fate as data, so the schema treats disposition as status.

There is also a live commercial disincentive. Systematically measuring false positive rates produces a number a competitor would quote in a sales cycle, and no vendor wants to be first to have one.

And dispositions live inside customer environments, sometimes in the customer's own issue tracker rather than the vendor's console, which makes the data genuinely harder to reach than it looks — and makes it a contractual question as much as a technical one.

## What a Fix Looks Like
**Make the disposition structured.** A short required reason code — not exploitable, unreachable, mitigated by configuration, curation incorrect, accepted risk — with optional detail. Seconds per finding, and it converts the largest data exhaust in the product into supervision.

**Compute and act on false positive rates by advisory.** An advisory that a hundred customers all mark incorrect is a curation defect, and it should route back to the research team automatically. That loop does not exist today and would improve the underlying data continuously.

**Mine not-exploitable patterns into rules.** When the same finding is dismissed for the same architectural reason across many customers, that is a suppression rule the product should offer rather than a discovery each customer makes independently.

**Report action rate as a product metric.** What proportion of findings, by priority band, teams actually acted on. This is the honest measure of whether prioritisation works, it is what every buyer is trying to assess, and publishing it is a stronger claim than any noise-reduction promise.

**Observe remediation, not just detection.** Upgrade paths taken, time to remediate, and upgrades reverted. Advice grounded in what actually worked for comparable codebases is a distinct product, and the data arrives free.

**Handle it contractually and privately.** Aggregated, de-identified disposition telemetry is a reasonable thing to negotiate for and a normal thing to offer value in exchange for. Treating it as unreachable is a choice.

## Who Feels the Pain
Development teams re-triaging the same false positives across every project; security engineers whose contextual expertise is written into a text box and discarded; the vendor's research team, curating without ever learning which of its entries customers found wrong; and the buyer, evaluating prioritisation claims that no vendor has ever quantified.

## Impact If Fixed
The single largest source of labelled feedback in this business is currently a status field. Capturing it makes curation quality measurable and self-correcting, turns repeated expert triage into product rules, and produces the only credible answer to the alert fatigue complaint that has defined the category since it began — a measured action rate rather than another promise of less noise.
