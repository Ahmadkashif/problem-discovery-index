# Reject Inference From Credit Scoring

**Niche:** [[niches/mobile-game-publishers/survivorship-correction/profile|Survivorship Correction]]
**Industry:** [[industries/mobile-game-publishers|Mobile Game Publishers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Lenders have a named discipline and regulatory pressure for learning about the applications they declined, and publishers have nothing for the concepts they killed.
**Tags:** #causal-inference #random-variables #expectation-maximization #hypothesis-testing #confidence-intervals #evaluation-metrics #compliance #bayesian-inference
**Contested on:** Every serious competitor in this niche is fighting to find out what the killed concepts would have done, because every threshold in the industry is validated against the population that passed it — and whoever assembles that evidence takes the account.

## The Problem
Credit scoring confronted this exact problem decades ago and gave it a name. A lender only observes repayment for applicants it approved, so every scorecard is trained on the accepted population and systematically misjudges the rejected one. The discipline that grew up around it — reject inference, randomised approval holdouts through the cutoff, bureau outcome data on declined applicants, and statistical correction for the selection — is mature, documented and partly mandated. Mobile publishing has the identical censoring and none of the practice.

## What Already Exists
Reject inference methodology; randomised approvals through the cutoff to generate unbiased samples; external outcome data on declined applicants; selection-corrected model estimation; and swap-set analysis comparing decisions under two rules.

## The Customization Gap
The adaptation is from an applicant with an external outcome record to a concept with no life after the kill. It requires: (1) no external bureau — a declined loan applicant borrows elsewhere and the outcome is purchasable, whereas a killed prototype usually ceases to exist, which is the substantive difference and forces the holdout to do more work; (2) a unit of analysis that is a game rather than a person, so sample sizes are in the hundreds not the millions; (3) an outcome measured in revenue over months rather than in default over a fixed term; (4) no regulatory forcing function, so the spend must be justified commercially; and (5) a killed-then-shipped-elsewhere population that is the nearest thing to bureau data and must be assembled manually.

## Target Customer
Mobile publishers, publishing groups, games research consortia, and credit risk methodology vendors seeking adjacent markets.

## Impact If Solved
Lending named this problem, mandated part of the fix and built the methods. The absence of anything like a bureau for killed prototypes is what makes the randomised holdout carry the entire burden here.
