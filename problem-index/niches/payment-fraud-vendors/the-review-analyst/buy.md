# Decision Support From Clinical Practice

**Niche:** [[niches/payment-fraud-vendors/the-review-analyst/profile|The Review Analyst]]
**Industry:** [[industries/payment-fraud-vendors|Payment Fraud Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Clinical decision support learned how to present a model's opinion to a human expert without degrading their judgement, and fraud review presents a score.
**Tags:** #worker-facing #large-language-models #evaluation-metrics #confidence-intervals #workflow-orchestration #automation #hypothesis-testing #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to make forty seconds enough to decide correctly on exactly the cases the model could not — and whoever equips that decision changes the outcome of the transactions the product is worst at.

## The Problem
Clinical decision support has spent decades on the question of how a model should present its opinion to a human expert who remains responsible for the decision: when to show a recommendation, how to express uncertainty, how to avoid automation bias, how to surface the evidence rather than the conclusion, and how to measure whether the combination outperforms either alone. Fraud review shows a number between zero and one hundred and a queue.

## What Already Exists
Clinical decision support design principles; alert fatigue and automation bias research; evidence presentation and uncertainty communication practice; human-model team performance measurement; and override analysis.

## The Customization Gap
The adaptation is to a forty-second decision at enormous volume. It requires: (1) support that fits inside seconds rather than a consultation, which rules out most clinical presentation patterns and is the substantive constraint; (2) outcomes that are absent for declines, so the human-model team performance cannot be measured the way clinical studies do without the randomised sample; (3) an adversary, which medicine does not have and which means analysts must be able to recognise deliberate manipulation; (4) analysts who are not domain-credentialled experts and whose training is short, changing what the support must supply; and (5) volumes that make even small per-case improvements enormously valuable.

## Target Customer
Review operations leadership, analysts, outsourced review providers, and decision support vendors with no fraud presence.

## Impact If Solved
Clinical practice studied how to present a model to a responsible human and this category shows a score. Compressing those principles into forty seconds is the adaptation, and the volume makes small gains worth a great deal.
