# Buy: Review Infrastructure Adapted to a Score That Sets Income

**Niche:** [[niches/freelance-marketplaces/reputation-and-ratings/profile|Reputation & Ratings]]
**Industry:** [[industries/freelance-marketplaces|Freelance Marketplaces]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Review platforms are built for product ratings where the rated object is inanimate and a wrong average costs nobody their rent.
**Tags:** #bayesian-inference #descriptive-statistics #confidence-intervals #evaluation-metrics #large-language-models #hypothesis-testing #worker-facing #compliance
**Contested on:** Whether commodity review infrastructure can carry the statistical and procedural weight of a score that determines a person's income.

## The Problem

Review and ratings infrastructure is abundant. Collection widgets, moderation pipelines, sentiment analysis, response management and display components are all available as services, and a marketplace can have a functioning rating system in weeks.

Every one of these products was designed for reviewing things. A product's average rating has no due process requirements, no appeal, no income consequence, and the product does not have to keep working with the reviewer afterwards. On a labour marketplace all four of those are false, and the infrastructure has no representation for any of them.

## What Already Exists

Trustpilot, Bazaarvoice, Yotpo and the commerce review stack. Open-source rating components. Sentiment and text classification services that handle review text well. Moderation tooling for abusive content. Verified-purchase mechanisms. The collection, storage and display layer is genuinely solved and nobody should be rebuilding it.

## The Customization Gap

**Rater calibration is not in any of these products.** Every one of them computes an arithmetic mean, sometimes with recency weighting or Bayesian shrinkage toward the global average. None models the individual rater, because for product reviews with thousands of ratings it does not matter. Here it is the dominant error term, and adding it means the score computation has to move out of the review product entirely into a model the platform owns.

**The counterparty relationship changes what can be collected.** A freelancer knows exactly who rated them and often has to work with that client again or wants the referral. Review infrastructure assumes a rater with no ongoing exposure. The adaptations — double-blind simultaneous release, private feedback separated from public score, rating windows that close before either party can retaliate — are workflow mechanics that no review product implements and that materially change what the ratings mean.

**Due process has to exist.** A rating that costs someone their tier needs a defined challenge path: what evidence is admissible, who decides, how long it takes, what happens to the score in the interim. Review platforms offer a takedown request for policy violations, which is a different thing entirely and answers "is this abusive" rather than "is this accurate".

**Text carries information the star does not.** Clients frequently write reviews whose content contradicts their star rating — detailed praise attached to three stars, terse neutral text attached to five. That text is a second, partially independent measurement of the same engagement, and extracting a rating-consistent signal from it is a substantial addition to the score's information content. Commodity sentiment scoring is not calibrated for this and tends to reproduce the star rating rather than complement it.

**Regulatory obligations are arriving.** Algorithmic transparency rules for platform work in the EU, and comparable pressure elsewhere, increasingly reach scores used in work allocation — including a right to an explanation and to contest. Review products have no concept of an obligation like that and the compliance layer has to be built around them.

## Target Customer

Marketplace product teams running a bought or homegrown review stack and hitting one of three walls: low-count freelancers with meaningless scores, a retaliation dynamic that suppresses honest rating, or a regulator asking how a score that allocates work is computed and contested.

## Impact If Solved

The commodity layer keeps handling collection, moderation and display, and the four adaptations make the number defensible. In practice that means a freelancer's score stops being an artefact of who hired them first, and the platform can answer the question of how it was computed — to the freelancer, and to whoever else asks.
