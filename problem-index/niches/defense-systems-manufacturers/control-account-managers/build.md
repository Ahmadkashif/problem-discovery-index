# A Reasoning Record Behind Every Estimate at Completion

**Niche:** [[niches/defense-systems-manufacturers/control-account-managers/profile|The Control Account Manager]]
**Industry:** [[industries/defense-systems-manufacturers|Defense Systems Manufacturers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** CAMs re-sign estimates every month without ever learning whether their past estimates held, and the reasons behind each change are lost.
**Tags:** #tacit-knowledge-ml #gradient-boosting #survival-analysis #large-language-models #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to give the control account manager an estimate at completion that holds, and whoever's estimates move least between the month they are signed and contract completion takes the account.

## The Problem
An experienced CAM "knows" an account is in trouble before the indices show it: a supplier's tone has changed, a test is going to need a second article, the team is burning overtime to hold the schedule. That judgement shapes the estimate, but the system records only the number. When the CAM moves on, the reasons go with them, and nobody grades how good the estimates were.

## Why Nobody Has Built This
Earned value software was built to compute and report, not to capture reasoning, and DoD reporting doesn't require the CAM's rationale beyond the variance narrative. Grading estimates needs years of closed accounts, which programme control rarely assembles.

## What to Build
At each monthly sign-off, a short structured record drafted from the month's data (drivers, assumptions, risks counted and not counted) for the CAM to confirm in a minute. On closed accounts, grade each signed estimate against the final cost; learn which patterns of indices, staffing and narrative preceded large estimate moves; and show each CAM, for each account, the closest historical analogues and how their estimates ended.

## Target Customer
Programme control directors at primes and large tier-1s with hundreds of CAMs on cost and incentive contracts.

## Impact If Built
Estimates that move less late in a programme mean fewer reach-forward surprises; even a small reduction in late EAC growth on a multi-billion-dollar backlog is worth more than the whole tool (estimate).
