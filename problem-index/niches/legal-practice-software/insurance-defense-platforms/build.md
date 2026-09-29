# Reduction Prediction at the Point of Time Entry

**Niche:** [[niches/legal-practice-software/insurance-defense-platforms/profile|Insurance Defense & Panel Counsel Platforms]]
**Industry:** [[industries/legal-practice-software|Legal Practice Software]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Carriers reduce defense invoices with a deterministic rules engine and return the reductions as structured data, and no practice management vendor has ever trained on that feedback to warn a timekeeper before the entry is submitted.
**Tags:** #logistic-regression #gradient-boosting #bert #large-language-models #evaluation-metrics #confidence-intervals #revenue-impact #worker-facing
**Contested on:** Every serious competitor in insurance defense software is fighting to get a firm's invoice through the carrier's bill review engine unreduced on the first pass — and whoever predicts the reduction before submission takes the account.

## The Problem
An associate writes "Review file; prepare for deposition; correspond with client — 3.2". Six weeks later the carrier reduces it: block billing, and the correspondence element is a guideline exclusion. The associate is told in a firm meeting to write better narratives, which is advice rather than information. Meanwhile the firm holds three years of its own submitted entries paired with the carrier's line-item adjudication — thousands of labelled examples of exactly which narratives, task codes, timekeeper levels and durations get reduced by which carrier — and uses it to produce a monthly realisation figure.

## Why Nobody Has Built This
The feedback data lives in the carrier's remittance and appeal files, which arrive in a format the firm's system stores and does not parse back to the originating time entry. Making the join is unglamorous plumbing across an accounting boundary, and no vendor has been asked for it because firms do not know it is possible. There is also a political reluctance: a product that visibly coaches a firm to bill in ways that pass review invites a conversation about whether it is coaching compliance or coaching evasion — a real question, and one the product design has to answer explicitly rather than avoid.

## What to Build
A model over the firm's own entry-to-adjudication history that scores each time entry as it is written, per carrier, and says what will be reduced and why — with the guideline provision cited and the firm's own reduction history for that pattern attached. The design commitment that makes it legitimate is that it never suggests changing what was done or inflating what is described; it identifies entries whose *description* fails to establish work that was genuinely performed, which is the actual cause of most reductions, and it flags entries that will be reduced for substantive reasons as unbillable so the firm stops writing them off silently. Guideline text is parsed per carrier into checkable provisions, and the model reconciles what the guidelines say with what the engine actually does, which are not the same and where the difference is the most valuable thing in the product.

## Target Customer
Insurance defense and panel counsel firms of 10-200 lawyers, and the practice management vendors serving them who currently ship LEDES export and stop.

## Impact If Built
Realisation improvements of three to eight points are the realistic range from narrative and coding correction alone, and in a business with defense-firm margins that is the difference between a good year and a bad one. The by-product is more valuable still: a firm that can characterise a carrier's actual reduction behaviour has, for the first time, evidence to bring to a panel rate negotiation.
