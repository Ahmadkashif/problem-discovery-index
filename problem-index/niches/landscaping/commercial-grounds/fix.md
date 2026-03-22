# Contract Renewal Risk Prediction

**Niche:** [[niches/landscaping/commercial-grounds/profile|Commercial Grounds]]
**Industry:** [[industries/landscaping|Landscaping]]
**Type:** Fix (Pain Point)
**One-liner:** Commercial landscapers discover a contract is at risk only when the property manager announces they're rebidding — by which point the relationship is usually unrecoverable, and a $200K-500K annual contract walks out the door with 60 days' notice.
**Tags:** #gradient-boosting #revenue-impact #data-integration #logistic-regression

## The Problem
Commercial grounds contracts are the high-value anchors of landscaping companies — a single HOA community or office park portfolio can represent $200K-500K in annual revenue. These contracts renew on 2-3 year cycles, and the landscaper typically learns whether they've been retained or replaced 60-90 days before the contract expires. By the time a property manager initiates a rebid, the decision to explore alternatives has already been made — usually 6-12 months earlier when dissatisfaction crossed a threshold. The signals of dissatisfaction are visible in hindsight but not tracked in real time: increasing complaint frequency, shorter property manager response times to invoices (indicating less engagement), requests for scope reductions, delayed approvals on enhancement proposals, and the subtle shift from "our landscaper" to "the landscaper" in communications. Experienced account managers pick up on these signals intuitively but the pattern recognition takes years to develop and doesn't transfer across accounts or personnel.

## Why It's Still Broken
No commercial landscaping platform treats contract health as a measurable, predictable metric. Aspire, BOSS LM, and LMN track financial performance per contract (revenue, cost, margin) but not relationship health indicators. Communication with property managers happens across email, phone, text, and in-person meetings with no centralized sentiment tracking. Complaint data exists in email threads but is never aggregated or trended. The account manager's subjective sense of "this account feels shaky" is the only early warning system, and it fails when account managers are overloaded (managing 15-30 properties each) or when the company experiences account manager turnover.

## What a Fix Looks Like
A contract health dashboard that aggregates signals from existing data sources: complaint frequency and resolution time from email/helpdesk (parsed via NLP), service visit compliance scores, enhancement proposal acceptance rates, invoice payment timing trends, and property manager communication frequency and tone. A gradient-boosted binary classifier trained on historical contract renewal outcomes (renewed vs. lost) predicts renewal probability per contract updated monthly. Contracts dropping below 70% predicted renewal probability trigger an automated alert to the account manager and operations director with a specific action plan: "Schedule in-person walk-through with property manager," "Propose 5% price reduction with scope enhancement," or "Document three recent above-and-beyond service instances for renewal presentation." The model improves as it accumulates more renewal/loss outcomes, requiring 30-50 contract cycles to reach reliable predictions.

## Who Feels the Pain
Company owners who lose $200K-500K contracts with insufficient warning to replace the revenue, account managers who feel blindsided when a property manager they thought was satisfied announces a rebid, and field crews who face sudden schedule disruption when a major contract is lost mid-season.

## Impact If Fixed
Provides 6-9 months of early warning on at-risk contracts instead of 60-90 days, enabling proactive relationship repair that converts 25-40% of would-be losses into retained accounts — worth $300K-1M in preserved annual revenue for a company with 20-40 commercial contracts.
