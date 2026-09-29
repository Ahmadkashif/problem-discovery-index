# The Implementation Engineer Launching Someone Else's Bank

**Industry:** [[embedded-finance-platforms|Embedded Finance Platforms]]
**Type:** Worker Life Changing
**One-liner:** Solutions engineers walk developer teams through building a regulated financial product for the first time, answering the same questions in a different order for every programme, and carry the bank-specific knowledge in their heads.
**Tags:** #large-language-models #bert #k-nearest-neighbors #word-embeddings #evaluation-metrics #workflow-orchestration #worker-facing #automation

## The Problem
The programme's engineering team is good at software and new to banking. They do not know what an ACH return code means, why a card authorisation can be held and never captured, what a provisional credit obligation is, or why the bank partner will not permit the merchant category they planned to support.

The implementation engineer teaches them, while configuring the programme, while translating between the programme's product intentions and the bank partner's constraints, while running the integration through sandbox and into production.

Every launch covers the same ground. Ledger semantics, the difference between authorisation and settlement, webhook idempotency, KYC step-up flows, dispute timelines, what happens on an account closure. The explanations are written again each time, adapted to a team with a different starting point.

Bank constraints are the part with no documentation. What a given sponsor bank will accept — which categories, which onboarding evidence, which marketing language, which product structures — lives in the accumulated experience of the people who have worked with that bank. A new implementation engineer learns it by getting told no.

Then the programme goes live and the same engineer becomes its support contact, because they are the person who knows how it was built.

## Why It Matters to the Worker
The role is a permanent context switch. Several concurrent launches, each at a different stage, each with a different bank partner's constraints and a different team's level of understanding, plus the support load of everything launched previously. The context cost of that is the dominant feature of the day.

The teaching is uncompensated and invisible. A large fraction of the work is financial education for other companies' engineers, and it does not appear in any metric, while time-to-launch does.

The knowledge accumulates in the wrong place. What the engineer knows about bank partner behaviour, programme archetypes and the ways launches go wrong is commercially valuable, entirely tacit, and lost when they move on.

And the support tail means there is no clean end. A launch completes and becomes a permanent obligation, so the load monotonically increases until something is handed off badly.

## What a Solution Looks Like
Precedent as the starting point. A new programme described in its own words should surface the closest programmes the platform has already launched, with their configurations, the issues that arose, and the decisions that were made. Most launches are variations, and the platform has the corpus.

Bank constraint knowledge made explicit. Every no from a bank partner, with its reason, recorded as structured knowledge and surfaced during configuration rather than during review, converts the most tacit and most commercially significant knowledge in the role into an asset.

Explanations generated against the programme's own stack and context, so the fifth explanation of authorisation-versus-settlement semantics this quarter is drafted rather than written, in the programme's language, referencing their actual integration.

Configuration validated before testing. Conflicts with bank constraints, combinations that caused incidents previously, and missing required settings are statically checkable and are currently found in the sandbox at best.

Launch risk predicted from configuration. The platform knows which launches were clean and which generated a month of incidents, and the configuration differences are recorded. Telling an engineer at week two that this launch resembles the difficult ones is actionable while there is still time.

## Impact If Solved
Implementation capacity is the binding constraint on how many programmes a platform can carry, and it is limited by how many concurrent contexts one experienced person can hold. Surfacing precedent, making bank constraints explicit and generating the repeated explanations removes the portion of the work that is genuinely repeated, and keeps the hard-won bank knowledge inside the platform.
