# Buy: Disclosure Control From Statistical Agencies

**Niche:** Personal Data Classification
**Industry:** [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** National statistical agencies have quantified re-identification risk for fifty years, and privacy tooling asserts that data is anonymised because the name column was removed.
**Tags:** #entropy-cross-entropy-kl-divergence #probability-distributions #evaluation-metrics #confidence-intervals #dimensionality-reduction #compliance #hypothesis-testing
**Contested on:** Whether a system can determine that data is personal, whose it is and what category it falls into.

## The Problem

Deciding whether a dataset identifies individuals is a mature quantitative discipline. Statistical disclosure control has been practised by national statistical agencies since the mid-twentieth century, because publishing census and survey data requires knowing exactly how much information can be released before individuals become identifiable. The field has formal measures of uniqueness, established methods for suppression, generalisation and perturbation, and a substantial literature on re-identification attacks and their success rates.

Privacy tooling in the commercial world does almost none of this. Anonymisation is typically asserted after removing direct identifiers, which the disclosure control literature demonstrated decades ago is insufficient — the well-known re-identification results on supposedly anonymised medical and mobility datasets are exactly this failure.

So organisations classify a dataset as anonymised, exclude it from their privacy obligations, and share or retain it on a basis that would not survive contact with the discipline that has studied precisely this question for fifty years.

## What Already Exists

Statistical disclosure control: k-anonymity, l-diversity and t-closeness; uniqueness and disclosure risk measures; suppression, generalisation, swapping and perturbation methods; the practice manuals of national statistical offices, which are detailed and public.

Differential privacy: a formal framework with strong guarantees, implemented in production at several large technology companies and in census publication, with mature open-source libraries.

Re-identification research: a substantial literature quantifying how few attributes are needed to identify individuals in various populations, which is the empirical foundation the commercial world has not absorbed.

Synthetic data: a growing category generating datasets that preserve statistical properties without corresponding to real individuals, with its own disclosure risk questions.

Privacy tooling: pattern-based classification, and anonymisation features that typically mean removing named columns.

## The Customization Gap

**Risk is asserted, not measured.** The single largest gap. Applying uniqueness and disclosure risk measures to a commercial dataset is straightforward with existing methods and essentially never done outside research settings.

**The auxiliary information assumption is different.** Statistical agencies model an attacker with public data. A commercial organisation's risk depends on what it and its processors hold internally, which is a different and often larger auxiliary set — and one the flow and lineage picture could actually enumerate.

**Scale and continuity.** Disclosure control is applied to a dataset before publication, as a one-off exercise by a specialist. Commercial data changes continuously and there is no specialist, so the methods need to run automatically and repeatedly.

**Differential privacy has an adoption gap, not a technology gap.** The libraries exist and the guarantees are strong. Commercial adoption is thin because the utility cost is real and because nobody is required to use it, which means the missing piece is a product that makes the trade legible rather than a new method.

**The output must reach a legal audience.** A privacy lawyer deciding whether a dataset is anonymised for regulatory purposes needs an argument, not a k-anonymity parameter. Translating a quantitative risk measure into a defensible regulatory position is the adaptation that would make this usable.

**Synthetic data claims need the same scrutiny.** The category is growing and its disclosure risk is frequently asserted rather than measured, which is the same failure one layer up.

## Target Customer

Data governance and privacy engineering at organisations that share or retain large behavioural datasets on an anonymisation claim — which is where the exposure is largest and the current basis weakest.

The privacy platforms, for whom quantified disclosure risk would replace an assertion with a measurement in the part of their product with the most legal weight.

Synthetic data vendors, who need rigorous disclosure risk measurement to substantiate their own core claim.

## Impact If Solved

An anonymisation claim becomes a measurement rather than an assertion, which matters because the claim is what removes a dataset from the entire regulatory regime.

Fifty years of disclosure control practice is public, well documented and directly applicable, which makes this a transfer problem rather than a research one.

And modelling the organisation's own internal auxiliary data as the attacker's knowledge would give a more accurate and usually more alarming risk picture than the public-data assumption, which is the right basis for a commercial holder to reason from.
