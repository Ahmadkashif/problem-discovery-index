# Build: A Platform for the Whole Job

**Niche:** The Sole Trust & Safety Engineer
**Industry:** [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** One product covering every harm type a growing platform faces, with the legal obligations surfaced, the vendor accuracy verifiable, and a prioritisation across categories that a generalist can actually operate.
**Tags:** #evaluation-metrics #confidence-intervals #gradient-boosting #compliance #workflow-orchestration #worker-facing #automation #data-integration
**Contested on:** Whether one person can own every harm type at a growing platform using tools whose accuracy they cannot verify.

## The Problem

The tooling market assumes a trust and safety organisation. Products are specialised — a classification vendor, a fraud vendor, a child safety solution, a case management system, an appeals workflow — each with its own integration, its own dashboard and its own configuration.

A platform with one trust and safety engineer buys two or three of them, integrates them imperfectly, and operates a set of products designed for a team.

What they actually need is different in kind. Coverage across every harm type rather than depth in one. The legal obligations surfaced — child safety reporting requirements in particular have specific legal force and specific timelines, and a generalist may not know they exist. A prioritisation across categories, because harassment volume and child safety incidents differ by orders of magnitude in frequency and severity and both land in one queue. A way to check whether the vendor's accuracy claim holds in their environment. And support for the regulatory reporting that is now required and is a specialist task.

Nobody builds for this. The specialised products serve the organisations, and the growing platform assembles a partial version and hopes.

## Why Nobody Has Built This

**The market looks small per customer.** A platform with one trust and safety engineer has a small budget, and the vendors are built around larger deals.

**Breadth conflicts with product depth.** A product covering every harm type is worse at each than a specialist, which is a real trade and is not obviously the wrong one for this buyer.

**Child safety has specific legal and operational requirements.** Handling it properly requires specific arrangements and lawful handling obligations, which is a barrier to a general product and is also exactly where the generalist most needs support.

**Regulatory reporting is jurisdiction-specific and changing.** Supporting it means maintaining obligation knowledge across jurisdictions, which is ongoing specialist work.

**The buyer does not know what they need.** A first trust and safety hire learning the domain cannot specify a product for a job they are still discovering.

**Vendors sell into the growth stage after this one.** The commercial attention is on platforms large enough to have a team, so the stage before it is served by whatever those products can be made to do.

## What to Build

**Cover the harm types a growing platform actually faces, in one product.** Spam, fraud, harassment, adult content, self-harm and child safety, with the depth appropriate to a platform at this stage rather than the depth a large platform needs.

**Surface the legal obligations by jurisdiction.** What this platform is required to do, by when, given where its users are — particularly child safety reporting, where the obligations are specific, legally binding and frequently unknown to a first hire.

**Make vendor accuracy checkable.** A built-in evaluation workflow letting the engineer label a sample of their own content and measure the classifier on it. This is the verification they currently cannot do and it is straightforward to provide.

**Prioritise across categories.** Given the volumes and the severities, where should this person's limited attention go. A queue that mixes a thousand spam reports and one child safety escalation needs the prioritisation built in.

**Handle the regulatory reporting.** The transparency reports and statutory submissions now required, generated from the platform's own data rather than assembled by hand by someone learning the requirements.

**Provide the operational defaults.** Thresholds, escalation paths, appeal processes and retention policies as sensible defaults rather than as configuration decisions a generalist must make alone.

**Connect them to a peer network.** People in exactly this role at other platforms are the most useful resource available and there is no directory of them.

## Target Customer

Growing platforms past their first stage — marketplaces, social products, communities, gaming platforms — at the point where trust and safety becomes a named role held by one person.

Engineering leadership at those platforms, who hired the role and cannot evaluate whether it is adequately supported.

Vendors willing to serve the stage before their current market, for whom this is both a defensible product and the acquisition path into customers who will later have teams.

## Impact If Built

A role that exists at every growing platform and is served by nobody gets a product built for the job as it actually is rather than for the job at a larger organisation.

Surfacing the legal obligations, particularly the child safety reporting requirements, addresses the highest-consequence gap — a generalist may not know an obligation exists, and the consequences of that are severe.

And making vendor accuracy checkable in their own environment gives this person the one thing they most lack: a way to know whether the tools they are relying on actually work where they have deployed them.
