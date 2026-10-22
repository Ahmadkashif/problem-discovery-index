# The Line Decrease Triggered by a Bureau Blip

**Niche:** [[niches/credit-card-issuers/credit-line-management/profile|Credit Line Management]]
**Industry:** [[industries/credit-card-issuers|Credit Card Issuers]]
**Type:** Fix (Pain Point)
**One-liner:** A single bureau trigger — a new inquiry, a utilisation spike elsewhere — fires a line decrease on a good customer, who gets an adverse action notice and closes the account.
**Tags:** #change-point-detection #gradient-boosting #evaluation-metrics #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to prove, on randomised holdout cells, that each line increase or decrease earns more incremental revolving balance and interchange than it adds in loss, and whoever measures that counterfactual best takes the account.

## The Problem
Decrease rules react to point-in-time attributes, some of which reverse within a month. The decrease itself raises the cardholder's utilisation and can lower their score.

## Why It's Still Broken
Decreases were tuned in downturns to cut exposure quickly, and their false-positive cost — attrition and complaints — is booked elsewhere.

## What a Fix Looks Like
Require persistence or corroboration before acting on volatile triggers, test decreases against holdouts measuring attrition and complaints as well as loss, and review reasons for accuracy.

## Who Feels the Pain
Good cardholders cut without cause, retention teams, and complaint handlers.

## Impact If Fixed
Exposure cut where risk is real, not where a data point flickered.
