# A Correction Model That Knows One Reporter's Writing

**Niche:** [[niches/court-reporting-firms/steno-scoping-proofreading/profile|Steno Scoping & Proofreading Networks]]
**Industry:** [[industries/court-reporting-firms|Court Reporting Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every edit a scopist makes to a reporter's raw file is a labelled example of that reporter's writing, and it is thrown away when the transcript is certified.
**Tags:** #tacit-knowledge-ml #transformers #lstms-and-grus #seq2seq #evaluation-metrics #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to edit a reporter's raw CAT file into a certifiable transcript overnight in that reporter's own dictionary and style, and whoever needs the fewest audio checks per page in that reporter's writing takes the account.

## The Problem
A scopist who has edited one reporter for five years knows that a particular stroke usually means "cardiologist" when a medical expert is testifying, and that this reporter drops a word when counsel speeds up. A new scopist learns it all again, job by job. Generic suggestion tools know language, not this reporter.

## Why Nobody Has Built This
The edit history lives in each reporter's CAT files, which CAT vendors do not collect. Reporters and scopists have no tools to train models, and per-reporter data seemed too small before modern sequence models.

## What to Build
A per-reporter correction model, trained with the reporter's consent on pairs of raw stroke sequences and their certified translations from her past jobs, on top of a pooled base model. It proposes corrections ranked by confidence, explains them ("you wrote this stroke as 'arterial' in 14 of 16 medical depositions") and suggests dictionary entries. It runs inside the CAT software, and the reporter owns the model.

## Target Customer
High-volume freelance reporters and the scopists they retain; scoping networks; CAT vendors as a licensed feature.

## Impact If Built
Fewer audio checks per page, faster onboarding of a new scopist, and a reporter's writing knowledge kept in a form that survives a scopist's retirement.
