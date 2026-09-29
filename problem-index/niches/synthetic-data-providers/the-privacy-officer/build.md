# Asked to Sign Off on an Epsilon

**Niche:** [[niches/synthetic-data-providers/the-privacy-officer/profile|The Privacy Officer]]
**Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A privacy officer is asked to approve a data release on the basis of a mathematical parameter and a set of attack results, neither of which their profession has a framework for evaluating.
**Tags:** #hypothesis-testing #confidence-intervals #monte-carlo-methods #evaluation-metrics #compliance #worker-facing #bayesian-inference #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to give the person who signs the release something they can defend afterwards — and whoever does that takes the account, because that signature is the last gate every deal passes through.

## The Problem
A privacy officer receives a vendor report. It states a differential privacy parameter, reports that a membership inference attack achieved an accuracy near chance, and asserts that the data is safe to release. They do not know what the parameter permits, whether that attack was the strongest available or the weakest, what auxiliary information the attacker was assumed to hold, or what happens to the unusual individuals in the dataset whose exposure the aggregate result conceals. They are being asked to accept accountability for a judgement they have no basis to make, by a party with an interest in the answer. Most of them say the only defensible thing, which is not yet.

## Why Nobody Has Built This
The vendors build for the technical buyer who selected them, not for the gatekeeper who blocks them, which is a common and expensive misreading of the sale. The artefact the officer needs is a risk statement, and the field has not agreed on how to construct one — so producing it means taking a position that could be wrong in public. Privacy professionals have frameworks for processing personal data and no framework for synthetic derivation, which sits awkwardly between anonymisation and processing in most regimes. And building for this buyer means producing documents that constrain what the sales team can claim.

## What to Build
Build the approval artefact. Produce a residual risk statement in the officer's own vocabulary — what an attacker with stated auxiliary information could plausibly learn, about whom, with what likelihood — rather than a parameter, since that is the form their framework already accepts and the translation is the entire product. State the threat model explicitly: who the adversary is, what they know, what they hold, what they are trying to do, which is standard practice in security assessment and absent here. Report the exposure of the most-at-risk individuals rather than the average, because the officer's obligation runs to individuals and an aggregate attack success rate is the wrong statistic for that duty. Provide a comparison basis, so the officer can see how this release compares to other releases their organisation has approved and to published practice, which is how professional judgement is actually exercised. Map to the specific regulatory questions their regime asks about anonymisation and re-identification, since that is the test they will be held to. Support an independent review step, because deferring to a third party is the standard mechanism for a decision the decision-maker cannot verify. And generate the record the approval will be audited against, which the fix note develops.

## Target Customer
Privacy, data protection and compliance functions; the generation vendors blocked at this gate; and the assurance firms for whom synthetic release review is an unclaimed service line.

## Impact If Built
The gatekeeper blocking every deal is the constituency nobody builds for. Translating a mathematical parameter into a residual risk statement under a stated threat model is what their framework can accept, and reporting the most-at-risk individuals rather than the average matches the duty they actually hold.
