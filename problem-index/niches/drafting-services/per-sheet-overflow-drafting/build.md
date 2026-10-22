# Markup Intake That Asks Before the Shift

**Niche:** [[niches/drafting-services/per-sheet-overflow-drafting/profile|Per-Sheet Overflow Drafting]]
**Industry:** [[industries/drafting-services|Drafting Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A one-off client's markups are read for the first time by the drafter who has to draw them, overnight, when the client is asleep and cannot answer.
**Tags:** #transformers #large-language-models #object-detection #seq2seq #workflow-orchestration #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to turn a one-off marked-up set into correct, standards-conforming sheets by the client's deadline at a fixed per-sheet price, and whoever needs the fewest clarification rounds takes the overflow work.

## The Problem
On overflow work the bureau has no history with the client and no time to build one. The markups arrive in the afternoon, the set is due in two days, and every ambiguous cloud costs a day of email or a guess. Most rework on per-sheet jobs comes from markups read wrongly, not from drafting errors.

## Why Nobody Has Built This
Markup tools are built for the person marking, not the person executing. Bureaus are too small to build intake software, and marketplaces see only the transaction, not the drawings.

## What to Build
An intake step that reads the markup set the moment it arrives: detects and transcribes every cloud and note, links each to its sheet, lists implied changes on unmarked sheets, and sends the client a short question list within the hour while they are still working. The drafter receives a task list with answers attached, and the returned set is checked against the list before delivery.

## Target Customer
Small US bureaus, freelancers and offshore firms doing one-off architectural and engineering sets; marketplaces that want fewer disputes.

## Impact If Built
Fewer guessed markups and fewer second rounds on fixed-price work, which is where per-sheet margin is lost.
