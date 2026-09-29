# Build: Attribution With Its Basis Attached

**Niche:** Attribution & Expert Testimony
**Industry:** [[industries/digital-forensics-firms|Digital Forensics Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Attribution expressed as structured inferences with defined confidence, separating the activity cluster from the named group, so the parties making consequential decisions can weigh it.
**Tags:** #bayesian-inference #graph-theory #evaluation-metrics #confidence-intervals #hypothesis-testing #probability-distributions #compliance #tacit-knowledge-ml
**Contested on:** Whether an attribution claim carries a confidence anyone has calibrated.

## The Problem

An attribution appears in a report as a sentence. The intrusion is assessed with high confidence to be the work of a particular group.

That sentence then travels to people who cannot evaluate it. An insurer deciding whether a state-actor exclusion applies. Counsel assessing whether a ransom payment would breach sanctions. A board approving a public statement. A regulator forming a view of the incident. Each reads a confidence term whose meaning is a firm's internal convention and a conclusion whose reasoning is prose.

Underneath, the attribution rests on distinct inferences with very different strengths. Infrastructure overlapping with previously attributed activity — strong or weak depending on whether the infrastructure is shared. Tooling resembling a known family — potentially weak, since tools are sold, shared and stolen. Targeting consistent with the group's pattern — usually weak, since patterns overlap. Tradecraft similarities — variable. And the separate question of whether the technical cluster corresponds to the named group, which is frequently a weaker claim than the clustering itself and is collapsed into it.

None of that structure reaches the reader. They receive a name and a confidence word.

## Why Nobody Has Built This

**Certainty is what the client wants.** Counsel and insurers want a conclusion they can act on. A structured breakdown of inference strengths is more honest and harder to use.

**Confidence conventions are internal and undefined.** Firms have their own scales with no published probability mapping, and defining one invites comparison and challenge.

**Attribution is contested by nature.** Even with strong evidence, the boundaries between named groups, and the relationship between clusters and groups, are genuinely disputed within the field.

**Calibration data barely exists.** Attributions are rarely conclusively resolved, so nobody knows how often a high-confidence assessment has been wrong.

**The consequences discourage precision.** Where an attribution affects an insurance exclusion, both a stronger and a weaker claim have parties who prefer them, which makes careful expression politically fraught.

**The naming is inherited and messy.** Group names come from vendor taxonomies that overlap inconsistently, so a firm using a name adopts another organisation's clustering decisions along with it.

## What to Build

**Define the confidence scale in probability terms and publish it.** High confidence means this probability range. Without a defined mapping the term is uninterpretable by exactly the people making decisions on it.

**Structure the inferences separately.** Each supporting observation as its own claim with its own strength — infrastructure, tooling, targeting, tradecraft, timing — so a reader can see which carry the weight and which are corroborative.

**Separate the cluster from the name, always.** Two distinct claims: this activity forms a coherent cluster, and this cluster is the group known as X. The second is frequently weaker and is routinely presented as part of the first, which is the single largest source of overstatement in attribution.

**Answer the questions that actually matter downstream.** Insurers need to know about state association; counsel needs to know about sanctions exposure. These are specific questions with specific evidential requirements, and answering them directly — with their own confidence — is more useful than a group name from which the reader must infer them.

**State the competing hypotheses.** What else would produce this evidence, and why it is considered less likely. This is standard analytic practice, it is cheap, and its absence is what makes an attribution unfalsifiable in the reader's hands.

**Record and score what resolves.** Where later evidence settles an attribution, score the earlier assessment. Sparse data over years is the only route to calibration and nobody is collecting it.

**Write for the downstream reader.** The sentence that reaches the insurer and the regulator should carry its own qualification, because the qualification will not survive extraction otherwise.

## Target Customer

Firms with expert witness practices, where overstatement carries direct professional risk and admissibility standards already demand a defensible basis.

Cyber insurers, whose exclusion decisions depend on attribution and who currently receive a name and a confidence word — and who have the leverage to require structured expression across a panel.

Breach coach law firms, who must assess sanctions exposure from an attribution and need the specific question answered rather than a group name.

## Impact If Built

The most consequential non-technical claim in an incident report becomes something its readers can actually weigh.

Separating the cluster from the name would resolve a large share of attribution overstatement, because the two claims have genuinely different evidential strength and are presented as one.

And answering the downstream questions directly — state association, sanctions exposure — rather than through a group name would give insurers and counsel what they need instead of requiring them to infer it from a taxonomy they do not understand.
