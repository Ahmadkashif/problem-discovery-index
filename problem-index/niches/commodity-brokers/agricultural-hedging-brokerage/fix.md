# Hedge Status Declared Once and Never Verified

**Niche:** [[niches/commodity-brokers/agricultural-hedging-brokerage/profile|Agricultural Hedging Brokerage]]
**Industry:** [[industries/commodity-brokers|Commodity Brokers]]
**Type:** Fix (Pain Point)
**One-liner:** An account is coded "hedge" at opening, and nobody checks again whether its positions still match anything physical.
**Tags:** #logistic-regression #feature-engineering #evaluation-metrics #compliance #quick-win
**Contested on:** *Not terminal as stated.* The honest partial sentence is "every competitor is fighting to keep an agricultural hedger hedged through a price spike". But for a farmer the contest is advice and a margin plan that the farmer and the farmer's lender trust, won by brokers with farm relationships. For elevators, feed mills and processors it is clearing a large hedge book against cash-contract positions and financing its margin calls at scale, won by FCMs with balance sheets and grain-system integration. Decomposed into contested sub-niches below.

## The Problem
Hedge designation matters. It affects exchange margin rates, position-limit exemptions and, informally, how patiently the FCM treats a margin call. But a hedge account can drift into speculation, through positions larger than the crop, trading in unrelated contracts, or holding past the marketing window, without anyone noticing until a deficit.

## Why It's Still Broken
Designation is a form at account opening, and the physical data that would verify it sits outside the FCM.

## What a Fix Looks Like
A periodic check that compares each hedge account's positions with the exposure the client declared (acres, head, storage capacity, contract volume), flags drift, and prompts the broker to refresh the declaration or reclassify the account.

## Who Feels the Pain
FCM risk and compliance staff, brokers whose patience with a "hedger" proves misplaced, and the genuine hedgers whose terms tighten after someone else's blow-up.

## Impact If Fixed
Margin patience goes to real hedgers, position-limit exemptions are defensible, and speculative drift is caught before it ends in a deficit.
