# Build: Screening That Knows What It Cannot Claim

**Niche:** [[niches/recruiting-tech-vendors/screening-and-matching/profile|Screening & Matching]]
**Industry:** [[industries/recruiting-tech-vendors|Recruiting Tech Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Build screening on requirements that can be stated and checked, report what it does not know, and stop training rankers on recruiter agreement.
**Tags:** #causal-inference #hypothesis-testing #confidence-intervals #evaluation-metrics #large-language-models #compliance #transformers #descriptive-statistics
**Contested on:** Whether a screening product can be commercially viable while declining to claim it predicts performance.

## The Problem

Every matching feature in this category is trained on the only label available, which is what a recruiter did. A model that predicts recruiter agreement will reproduce whatever was in recruiter behaviour — including the parts nobody wants reproduced — and will do it at scale, consistently, with the appearance of objectivity.

The field has a canonical example. Amazon's abandoned resume-screening tool was a model trained on historical hiring that reproduced the pattern in that history, and the structural condition that produced it is present in every system in this category.

The honest position is that the sector cannot validate its matching claims and should say so. Instead the claims are made, the models ship, and the fairness reporting that exists measures whether the reproduction is balanced rather than whether it is right.

## Why Nobody Has Built This

Because the honest product is a weaker demo. "This finds candidates matching your stated requirements and makes no claim about who will perform" loses to "our AI identifies your best candidates" in a competitive evaluation.

The evidence to do better does not exist and generating it is expensive and slow. So the alternative to training on recruiter agreement is either a rules-based system that looks unsophisticated, or an honest statement of ignorance that no competitor will match.

And nobody in the buying process asks for validation evidence, because they would not know what to ask for and no vendor would have it.

## What to Build

Screening grounded in stated requirements, with the epistemic limits made explicit.

**Separate stated requirements from learned preference, completely.** Requirements are things the employer can articulate and defend as necessary — a licence, a language, a legal right to work, a demonstrable skill. Screening against them is checkable and defensible. Learned preference is a model of past behaviour and should never be presented as a requirement.

**Extract capability from the application rather than matching keywords.** What has this person actually done, described in their own words, mapped to the requirements. Generative extraction handles this far better than keyword matching and is where the genuine technical improvement is — it surfaces candidates whose relevant experience is real and not phrased the way the job description phrased it.

**Rank only where you can justify the ordering.** Requirements met, with the evidence for each, is a defensible ordering. A composite match percentage derived from recruiter agreement is not, and the product should not produce one.

**Report the limits in the product.** A stated line in the interface and the documentation: this system finds candidates matching stated requirements and does not predict job performance; no evidence exists that it does. That is true of every product in the category and saying it is a differentiator rather than a weakness.

**Instrument for the audit.** Retain the screen's reasons per candidate, the requirements version, and the rejection basis, so that a rejection audit is possible — which is the build in the first sub-niche and the only near-term source of evidence.

**Monitor the distributional effects continuously**, because a screen that reproduces past patterns will show it in pass rates by group, and finding that yourself is better than the alternative.

## Target Customer

Employers with legal exposure and a compliance function that has read the regulatory direction, for whom a defensible screening story is worth more than a match percentage. Also the ATS vendors, several of whom have already retreated from strong matching claims under scrutiny and need a product position to retreat to.

## Impact If Built

Screening rests on requirements the employer can state and defend rather than on a model of past recruiter behaviour. The capability extraction surfaces candidates that keyword matching discards. The product says what it does not know, which is both accurate and, as regulation arrives, the position that survives. And the audit becomes possible because the reasons were retained.
