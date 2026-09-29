# Investigation Outcomes as the Missing Label Set

**Niche:** [[niches/credit-unions/financial-crime-consortium-analytics/profile|Financial Crime Consortium Analytics]]
**Industry:** [[industries/credit-unions|Credit Unions]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Analysts at hundreds of institutions investigate and dispose of millions of alerts a year, each disposition is a label on the model that raised it, and the labels stay inside the institution.
**Tags:** #gradient-boosting #logistic-regression #evaluation-metrics #cross-validation #graph-neural-networks #feature-engineering #confidence-intervals #causal-inference #compliance #data-integration

## The Problem
Detection models raise alerts; investigators at member institutions work them and record a disposition — cleared, escalated, reported. That disposition is precisely the supervised label the model needs, generated at enormous volume by trained people, and it largely stays in each institution's own case management system. The vendor sees alert volume and, in a consortium model, some case outcomes, but not consistently and not in a structure that supports learning. So models are tuned on retrospective known-fraud sets and on rule refinement, while the industry's largest continuously generated label stream — millions of expert dispositions a year — is fragmented across hundreds of institutions. False positive rates above ninety percent persist partly because the feedback that would reduce them is not collected in a usable form.

## Why Nobody Has Built This
Case dispositions live in institution-owned systems and touch reporting that is confidential by statute, which has made the whole area feel legally closed rather than merely unaddressed. The label is also noisier than it looks — a cleared alert may reflect a genuine false positive, an investigator's time pressure, or an activity that was suspicious and unprovable — so naive training on dispositions teaches the model to predict investigator behaviour rather than criminality. And consortium governance means any change to what members contribute is a negotiation rather than a product decision.

## What to Build
A structured disposition capture layer designed around both constraints. Members contribute dispositions in a common taxonomy that separates the outcome from the reason — cleared as benign, cleared for insufficient evidence, escalated, reported — with the confidentiality-protected content never leaving the institution and only the classification and its features contributing to the shared model. Investigator context is captured lightly, because knowing that a disposition was made under queue pressure is itself a signal about label quality. On that base the vendor gains what it has never had: precision and recall measured against expert judgment at consortium scale, model performance decomposed by typology, institution size, and alert type, and — the highest-value output — the ability to distinguish alerts that are false positives from alerts that were suspicious and simply could not be proven, which is a distinction no current system makes and which points directly at where investigative capacity is being wasted.

## Target Customer
VPs of financial crime research and chief data scientists at consortium analytics vendors running 100-500 analysts, and the financial crime officers at member institutions whose investigators absorb the false positive burden.

## Impact If Built
Attacks the industry's defining cost — a false positive rate above ninety percent, borne as analyst hours at every member institution — with the only signal capable of reducing it. The disposition corpus is also strictly non-replicable: only a consortium operator sees expert judgment at this volume across institutions, and a competitor cannot assemble it without the same membership.
