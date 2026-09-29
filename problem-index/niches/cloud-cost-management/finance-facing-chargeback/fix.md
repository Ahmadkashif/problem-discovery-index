# The Number That Does Not Match the Invoice

**Niche:** [[niches/cloud-cost-management/finance-facing-chargeback/profile|Finance-Facing Allocation & Chargeback]]
**Industry:** [[industries/cloud-cost-management|Cloud Cost Management]]
**Type:** Fix (Pain Point)
**One-liner:** The cost tool says one number, the provider's invoice says another, and reconciling them takes a finance analyst two days a month because commitment amortisation and credits are applied differently.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #compliance #quick-win #revenue-impact #data-integration
**Contested on:** Every serious competitor here is fighting to produce a cloud allocation that reconciles to the invoice, survives audit and forecasts accurately enough to plan against — and whoever does that takes the finance account, because a number that does not add up is worse than no number.

## The Problem
The platform reports the month's cloud cost. The invoice from the provider is different. The difference comes from commitment amortisation treated one way in the tool and another on the invoice, credits applied at a different level, a support charge included in one and not the other, and currency conversion timing. A finance analyst spends two days establishing that the numbers are consistent, every month. The exercise produces nothing except confidence, and it must be repeated because nothing was fixed.

## Why It's Still Broken
Amortisation, credits and discounts are genuinely complicated and the providers document them incompletely, so vendors implement an interpretation and differences accumulate quietly. The tool's headline number is chosen for the engineering view — usually amortised and net of discounts — while the invoice is a cash figure, and both are correct for their purpose and are compared as though they should match. Nobody produces a reconciliation statement, because the vendor's product is reporting rather than accounting.

## What a Fix Looks Like
Produce the reconciliation as an output rather than an exercise. A bridge from the invoice total to the reported total, line by line — amortisation timing, credits, support, taxes, currency, refunds — which is arithmetic and turns a two-day investigation into a page. Report both bases explicitly and label them, since the cash figure and the amortised figure are both needed by different consumers and the confusion comes from a single unlabelled number. Show credits and discounts as separate reconciling items rather than netting them silently, which is where the largest unexplained differences usually originate. Flag definitional differences rather than absorbing them, because a silent absorption is what makes the totals diverge in the first place. Keep the reconciliation for audit, since in most organisations someone will eventually ask for the evidence. And alert when a new reconciling item appears, since a provider changing how something is billed is otherwise discovered by an analyst three months later.

## Who Feels the Pain
Finance analysts reconciling by hand every month; controllers who cannot use the tool's number without checking it; and organisations whose cost reporting carries an asterisk that undermines everything built on it.

## Impact If Fixed
The bridge is arithmetic over data both sides already hold and converts a recurring two-day exercise into a report. Labelling the basis explicitly removes the most common source of confusion outright.
