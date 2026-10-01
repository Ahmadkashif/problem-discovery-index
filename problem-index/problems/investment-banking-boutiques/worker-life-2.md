# The Associate Ticking and Tying at Midnight

**Industry:** [[investment-banking-boutiques|Investment Banking Boutiques]]
**Type:** Worker Life Changing
**One-liner:** The associate is personally accountable for every number in a board book matching the model, the CIM and the last version, and checks them by hand with a printout and a pen.
**Tags:** #large-language-models #transformers #object-detection #evaluation-metrics #worker-facing #compliance #quick-win

## The Problem
Before a board presentation, a fairness-opinion committee, or the release of a CIM, every number in the document must tie: the revenue figure on page 12 must match the model, the model must match the audited financials and the quality-of-earnings report, the EBITDA on page 30 must equal the EBITDA on page 12 after the adjustments footnoted on page 31, and the percentages must add. This is "ticking and tying", and in most boutiques it is done by the associate and analyst with a printed copy, a pen and the model open on a second screen, often in the last hours before the document goes out.

The documents change constantly. A late adjustment to the model moves forty numbers across three documents. Some update through linked cells; many were pasted as values weeks ago. The associate cannot know which without checking every one.

## Why It Matters to the Worker
The stakes are disproportionate to the task. A wrong number in a board book or fairness presentation is the kind of error that ends up in a deposition, and the person who missed it is the associate. The work is tedious, cannot be delegated upward, and happens at exactly the point in the deal when everyone is most tired. It produces a distinctive anxiety — the fear of the one number not checked — that bankers describe as worse than the hours.

It also wastes the associate's actual role, which is to manage the analyst, shape the analysis and own the client relationship day to day. An associate who spends the final two nights before a board meeting ticking numbers is not reviewing the argument the numbers are supposed to support.

## What a Solution Looks Like
Automated tie-out. Extract every number from the deck, the CIM and the model; resolve each to what it claims to represent (FY24 adjusted EBITDA, LTM revenue, net debt at close); link it to its source cell; and flag every mismatch, every stale paste and every internal inconsistency — totals that do not add, percentages that disagree with their inputs, the same metric shown at two values. Output is a marked-up document the associate reviews, not a pass/fail.

Version comparison that understands numbers: show what moved between this draft and the last one, and whether the movement was expected from the model change.

## Impact If Solved
Tie-out is a few hours on a small document and a few days on a CIM or board book, repeated on every revision. Automating detection, so that humans review flagged discrepancies rather than every figure, removes the most anxious work in the associate's week and materially reduces the risk of an error reaching a board or a court.
