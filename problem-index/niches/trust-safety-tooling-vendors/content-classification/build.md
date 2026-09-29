# Build: Performance Where the Harm Is

**Niche:** Content Classification
**Industry:** [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Report and improve classifier performance per language, per community and per content type, and handle the context distinctions — quotation, reporting, counter-speech, reclaimed use — that aggregate accuracy conceals.
**Tags:** #bert #transfer-learning #large-language-models #contrastive-learning #evaluation-metrics #confidence-intervals #word-embeddings #compliance
**Contested on:** Whether a classifier works where the harm actually concentrates, or only in the aggregate.

## The Problem

A classifier reports ninety-four per cent accuracy. Inside that number is a distribution.

It performs very well on unambiguous content in high-resource languages. It performs less well on the same categories in languages with less training data. It performs poorly on code-switched and transliterated text, which is how much of the world actually writes online. It struggles with reclaimed speech, where a community's use of a term is not the harm the term normally indicates. And it frequently cannot distinguish harm from a report of harm, a quotation, a counter-speech response, satire or education.

Those failures are not evenly distributed across users. They fall on speakers of particular languages, on specific communities, and on the people most likely to be discussing harm rather than committing it — which includes journalists, researchers, activists and survivors.

The aggregate figure conceals all of it. A vendor with a weak Bengali classifier and a strong English one reports a number close to the English one, because the test set composition reflects the training data rather than the platform's user distribution.

The disaggregation is entirely computable. The vendor has the data. Reporting per-segment performance requires the breakdown to be published rather than aggregated.

## Why Nobody Has Built This

**The aggregate is more flattering.** Per-segment reporting shows the weak segments, which is a worse number in every marketing comparison.

**No buyer asks for it.** Platforms compare accuracy figures because that is what is published, and the question of which segments have been tested is not in a standard evaluation.

**Test sets reflect training data.** The evaluation set is built from the same distribution as the training data, so under-represented segments are under-represented in the test too — which means the aggregate is computed on a population that is not the platform's users.

**Context handling is genuinely hard.** Distinguishing a quotation from an endorsement, or reclaimed use from a slur, requires understanding that has been out of reach and is now becoming tractable with language models.

**Labelled data is scarce where performance is worst.** Improving lower-resource language performance requires labelled data in those languages, which is the constraint described in this industry's annotation problem.

**The failures affect people with the least leverage.** Over-removal of reclaimed speech and minority-language content affects communities least able to make the pattern visible to a vendor's product team.

## What to Build

**Report per-segment, always.** Performance by language, by content type, by community where identifiable, with sample sizes. This is the disclosure that would change what buyers can evaluate and it is computable now.

**Build test sets that reflect deployment, not training.** Evaluation weighted to the platform's actual user distribution rather than to the training corpus, which is a different set and frequently a very different picture.

**Handle context as a distinct problem.** Quotation, reporting, counter-speech, education, satire and reclaimed use are all cases where the surface content matches and the classification should not. Language models make this substantially more tractable than it was and it is where the largest improvement available sits.

**Invest in lower-resource languages deliberately.** Not as coverage claims but as measured performance, with the labelled data investment that requires — which is the actual constraint and is expensive.

**Consult the affected communities.** Reclaimed speech, community norms and context-dependent meaning cannot be determined from outside. The communities affected know and are not asked.

**Express uncertainty per segment.** A classifier should indicate where it is operating outside its competence — an unfamiliar language variant, an ambiguous context — so the platform can route to human review rather than acting.

**Publish the weaknesses.** A vendor stating plainly where its classifier is weak is making a credibility claim no competitor makes and is giving buyers what they actually need.

## Target Customer

Platforms operating in markets outside the high-resource languages, who are buying on an aggregate figure that does not describe their user base.

Vendors positioning on rigour rather than on headline accuracy, for whom per-segment reporting is the first defensible quality claim in a category of unverifiable ones.

Regulators, who increasingly require moderation accuracy reporting and will find that the figures available are aggregates computed on the vendor's own distribution.

## Impact If Built

Per-segment reporting makes visible the failures that cause most documented moderation harm, which are currently concealed inside a number that describes a different population.

Building evaluation sets that reflect deployment rather than training is a change in what is measured, not in the models, and would immediately reveal how much of the aggregate is a statement about English.

And handling context distinctions properly is where the largest available improvement sits, because the surface-level failures — quotation and reporting treated as the harm itself — affect exactly the users who are discussing harm rather than causing it.
