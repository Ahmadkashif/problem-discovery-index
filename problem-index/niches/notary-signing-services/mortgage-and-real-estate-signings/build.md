# A Signing Outcome Ledger Across Every Agent

**Niche:** [[niches/notary-signing-services/mortgage-and-real-estate-signings/profile|Mortgage & Real Estate Signings]]
**Industry:** [[industries/notary-signing-services|Notary & Signing Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Title companies choose signing agents on certification badges and fee, because nobody records how each agent's signings actually turned out.
**Tags:** #gradient-boosting #survival-analysis #confidence-intervals #evaluation-metrics #data-integration #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor is fighting for title and escrow order flow, but borrower loan signings are won by returning a clean, fully executed package before the funding cutoff, while seller and deed signings are won by proving the signer is the owner of record before the deed records — two contests with different winners. Decomposed into contested sub-niches below.

## The Problem
A title company may use hundreds of signing agents a year, directly or through several signing services. The outcomes that matter — a redraw, a late scanback, a missed courier, a borrower complaint, and rarely an impostor who got through — are recorded, if at all, in an escalation email or a claim file. Marketplace ratings measure responsiveness and volume. When a closing manager chooses between two certified agents, they have no evidence of which one causes fewer redraws or has ever refused a suspicious seller.

## Why Nobody Has Built This
Each party holds a slice: the marketplace sees acceptance and completion, the signing service sees its own redraws, the title company sees funding delays, and the underwriter sees claims years later. None has an incentive to share, and agents fear being scored on errors they did not cause, such as late documents or lender mistakes.

## What to Build
An outcome ledger keyed to the agent's commission number and the order: package returned clean or not, which pages failed and why, scanback and courier timing, document arrival time (so lender-caused failures are separated), borrower feedback, and identity incidents with their later resolution. Score agents with confidence intervals that reflect how few orders a new agent has, and separate borrower-signing performance from seller-signing performance, since they measure different skills.

## Target Customer
Title agency operations directors and underwriters' agency-management teams; large signing services competing on quality.

## Impact If Built
Order flow moves to agents with evidence of clean work, redraw rates fall, and the market finally pays for quality rather than for availability at the lowest fee.
