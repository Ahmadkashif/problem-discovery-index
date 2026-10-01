# The Buyer List Built From Memory

**Industry:** [[investment-banking-boutiques|Investment Banking Boutiques]]
**Type:** High Impact
**One-liner:** Every sell-side process records exactly which buyers engaged and which bid, and the next buyer list is still built from a managing director's memory and a database screen.
**Tags:** #gradient-boosting #survival-analysis #graph-theory #k-nearest-neighbors #evaluation-metrics #feature-engineering #tacit-knowledge-ml #revenue-impact

## The Problem
A mandate is won to sell a $150M-revenue specialty distribution business. The first real work product is the buyer universe: the strategic acquirers and financial sponsors who will receive the teaser. An associate screens Capital IQ and PitchBook for companies in adjacent SIC codes and sponsors with a stated interest in distribution, producing three hundred names. The managing director then does the thing the client is actually paying for — strikes two hundred of them, adds twenty nobody's screen found, and ranks the rest into tiers.

That judgment is tacit. The MD knows that one mid-market sponsor takes every management meeting and has not submitted a final bid in four years; that a strategic acquirer's corporate development team is enthusiastic in first round and is routinely overruled by its board; that a family office nobody's database tags as active has bought three distributors quietly; that a particular platform company is two years into a hold and hungry for an add-on. None of this is written down. It is the accumulated residue of hundreds of processes, absorbed as an individual and walked out of the door when the MD leaves.

Meanwhile the evidence exists. Every past process at the firm logged each buyer's path through the funnel — teaser sent, NDA signed, CIM opened, data room activity, indication of interest and its range, management meeting, letter of intent, final bid, and the winning price. That is a labelled record of buyer behaviour across sectors, sizes and market conditions. It lives in per-deal Excel trackers and DealCloud fields filled inconsistently, and it is never joined across deals.

The consequence is a buyer list that over-contacts (extending the process, leaking confidentiality, and burning the client's management time on tourists) and under-contacts (missing the one buyer who would have paid a full turn more). The client never learns which happened.

## Why It's Unsolved
The data problem is assembly. Buyer names are recorded differently in every tracker — a sponsor, its fund, its portfolio company and the individual partner are all "the buyer" depending on who typed the row — so entity resolution across a decade of spreadsheets is the first and least glamorous task. Outcome fields are missing whenever a process died or an associate stopped updating the tracker in the final weeks.

The labelling problem is that the expert's own judgment is inconsistent. An MD asked to tier the same buyer list twice, a month apart, will not produce the same tiers, and two MDs at the same firm will disagree on a third of the names. The model must learn from realised behaviour — who actually bid — rather than from expert tiers, and realised behaviour is confounded by the expert's choices: a buyer that was never contacted never bid, which says nothing about whether it would have. Selection bias is built into every label.

The deployment problem is speed and trust. A buyer list is drafted in an afternoon by someone who has done it many times; a tool that takes longer, or produces a ranking the MD cannot interrogate, will be ignored. It must show its reasoning in the MD's own terms — "bid on two comparable distributors in 2023, platform in year three of hold, took meetings but never bid on deals above $200M" — and it must be faster than the MD's memory. There is also an organisational barrier: senior bankers' buyer knowledge is their personal franchise, and making it institutional is not obviously in their interest.

## What a Solution Looks Like
Assemble the process ledger first: every buyer, every mandate, every stage reached, every indication and bid, resolved to canonical entities with sponsor–fund–portfolio-company relationships as a graph. That table, once built, is the firm's most defensible asset and needs no model to be useful — simply showing an MD every past interaction with each name on a draft list changes the conversation.

On top of it, a buyer-propensity ranking: for a new mandate described by sector, size, margin profile, geography and ownership, estimate each candidate's probability of reaching each funnel stage, using its historical behaviour, its similarity to past buyers of comparable assets, and live signals such as fund vintage, dry powder, hold period of existing platforms and recent acquisitions. Present it as a ranked list with evidence beside every name, and let the MD override — capturing the override as a label.

## Impact If Solved
The buyer list is the largest single determinant of a sell-side outcome that is in the bank's control. A firm that contacts fewer tourists and finds the missing bidder shortens processes, protects confidentiality and can plausibly add a fraction of a turn of EBITDA to outcomes — while converting individual bankers' memory into an asset that survives their departure and that a competitor structurally cannot buy.
