# Solutions Architect in a Replatform

**Industry:** [[headless-commerce-vendors|Headless Commerce Vendors]]
**Type:** Worker Life Changing
**One-liner:** Solutions architects live inside multi-year replatforming programmes, designing compositions whose failure modes only appear in production, held responsible for outcomes that depend on a dozen parties.
**Tags:** #graph-theory #large-language-models #evaluation-metrics #hypothesis-testing #confidence-intervals #workflow-orchestration #transfer-learning #worker-facing

## The Problem
A large retailer decides to replatform. The programme runs for a year or more, involves the platform vendor, several component vendors, a systems integrator and the retailer's own teams, and the solutions architect designs how it fits together.

The design decisions are consequential and made with incomplete information. Which service owns pricing. How inventory is reconciled between the commerce engine and the warehouse system. Where personalisation sits relative to caching. How search stays current. Each choice has failure modes that appear under production load with real data, which is at the end of a year-long programme.

The architect is accountable for an outcome depending on components they do not control, vendors they cannot direct and a retailer's legacy systems nobody fully documents. Replatforming programmes have a poor completion record, and when one goes badly the architecture is the first thing examined.

Meanwhile the same architect is designing for several clients, and each composition is bespoke enough that experience transfers imperfectly.

## Why It Matters to the Worker
The feedback loop is a year long. An architect learns whether a decision was right when it reaches production, by which time they have made the same decision several times elsewhere.

Accountability exceeds authority substantially. The architect designs and does not control implementation quality, vendor behaviour or the retailer's willingness to change processes, and owns the result.

These programmes are high-pressure and highly visible — a replatform is a board-level commitment with a deadline tied to a peak season — and the architect is at the centre of every escalation.

And the knowledge does not compound. Each composition is documented as a client deliverable, the failure modes discovered are discussed informally, and there is no accumulating body of evidence about which patterns work. An architect with ten implementations behind them has real judgement and no artefact.

## What a Solution Looks Like
A pattern library grounded in outcomes. The vendor has delivered many implementations and knows which compositions produced problems, and turning that into documented patterns with their known failure modes is the most valuable thing they could give their architects.

Design-time validation. Checking a proposed composition against known problematic patterns — a service holding pricing that cannot see promotion state, a caching layer positioned where personalisation must bypass it — is a rules-and-retrieval problem over accumulated experience.

Reference implementations that are actually reference implementations, maintained and tested against realistic load, so that architects compose from validated building blocks rather than from documentation.

Load and failure characterisation earlier. Much of what appears at production launch is discoverable with realistic data and traffic at design time, and testing environments in these programmes are typically nothing like production.

Post-implementation review captured systematically, so that what went wrong in each programme becomes evidence rather than corridor conversation.

## Impact If Solved
Replatforming outcomes are decided by architectural choices made with a year-long feedback loop by architects whose accumulated judgement never becomes an asset. A pattern library grounded in the vendor's own delivery history is the difference between each implementation starting from documentation and each one starting from evidence.
