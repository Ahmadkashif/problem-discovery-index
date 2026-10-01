# Seven Thousand Marks a Quarter, Each Built From a Blank Comp Set

**Niche:** [[niches/private-equity-firms/portfolio-valuation-advisory/profile|Portfolio Valuation Advisory]]
**Industry:** [[industries/private-equity-firms|Private Equity Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A valuation practice re-marks thousands of private companies every quarter by having analysts refresh comparable sets, multiples and memos one company at a time, while sitting on the panel that would let most of it be computed and the analyst's time go to the exceptions.
**Tags:** #gradient-boosting #k-nearest-neighbors #large-language-models #regularization #confidence-intervals #evaluation-metrics #automation #tacit-knowledge-ml
**Contested on:** Every serious competitor in this niche is fighting to produce a quarterly fair value mark the sponsor, its auditor and its LPs all accept — defensible against observable market evidence, consistent across hundreds of companies and delivered before the reporting deadline — and whoever does that most credibly at volume takes the valuation mandate.

## The Problem
Every quarter a valuation team receives updated financials for each company it covers, refreshes the public comparable set and their trading multiples, updates precedent transactions, reruns the DCF, decides how much weight each method gets, writes the valuation memo and defends it to the sponsor and the auditor — within a few weeks after quarter-end. The work is extremely repetitive in shape: most companies' marks move with their own earnings and with sector multiples, and the analyst's judgement matters most in the minority where something changed — a covenant issue, a lost customer, a failed sale process, a sector re-rating.

The senior valuer's skill is knowing which comparables actually behave like this private company, how much of a public multiple's move should pass through, and when a company's own trajectory has broken from its sector. That judgement is tacit, and it is re-exercised from scratch on every company every quarter.

## Why Nobody Has Built This
The practice is priced per mark and staffed with analysts, so automation looks like revenue loss until fee pressure forces it. Comparable selection is treated as professional judgement that cannot be delegated. Auditors scrutinise methodology, so any model must be explainable. And the panel of past marks — the training data — has never been organised as data rather than as a stack of memos.

## What to Build
**Organise the panel.** Every company-quarter: financials, capital structure, comparable set chosen, multiples applied, method weights, concluded value and the memo text. This is the corpus, and it already exists in files.

**Learn the valuer's comp selection.** A retrieval model that proposes a comparable set and weights for each company from its business description, financial profile and the sets senior valuers chose historically for similar companies — with agreement against senior valuers measured, and their own quarter-to-quarter consistency used as the ceiling.

**Pre-compute the routine mark.** A model of the quarter's expected value move from the company's own financial change and its comparables' movement, with an interval; marks inside the interval go to quick review, marks outside or companies with flagged events go to full analyst work.

**Draft the memo.** LLM-drafted memo sections from the structured inputs, in the house style, with every figure linked.

**Flag the exceptions.** Covenant pressure, customer loss mentions in management commentary, divergence between the company's trajectory and its sector — the cases where judgement earns its fee.

## Target Customer
Heads of portfolio valuation at independent valuation firms; sponsors' internal valuation committees as a secondary market.

## Impact If Built
A large share of quarterly valuation labour is routine refresh. Pre-computing the routine marks with honest intervals and drafting the memos turns valuation teams toward the companies where the mark genuinely needs judgement, raises consistency across thousands of marks, and preserves senior valuers' comparable-selection judgement as an asset of the firm rather than of the individual.
