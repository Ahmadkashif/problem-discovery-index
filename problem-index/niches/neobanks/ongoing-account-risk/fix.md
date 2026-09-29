# The Freeze That Is All or Nothing

**Niche:** [[niches/neobanks/ongoing-account-risk/profile|Ongoing Account Risk]]
**Industry:** [[industries/neobanks|Neobanks]]
**Type:** Fix (Pain Point)
**One-liner:** The only available response to a risk signal is a full freeze, so a customer whose pattern looked slightly unusual loses access to their rent money while somebody reviews it.
**Tags:** #compliance #evaluation-metrics #workflow-orchestration #confidence-intervals #quick-win #automation #revenue-impact #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to tell a fraudster from a customer having a bad month, using the institution's own ledger — and whoever does that stops freezing the wages of people who did nothing wrong.

## The Problem
A signal fires at moderate confidence. The action available is a full account restriction: card declined, transfers blocked, balance inaccessible. The customer, who may well be entirely legitimate, cannot pay rent, buy food or move money to cover a bill, and receives a form letter citing the deposit agreement. A review happens within some number of days. Meanwhile the response was calibrated for a certainty the signal did not have, because the system offers one action and the analyst has to choose between doing nothing and doing everything.

## Why It's Still Broken
The action set is binary because the systems were built to stop loss and stopping loss completely is the simplest implementation — the absence of a middle is an engineering default that became a policy. A partial restriction requires product work in the card and transfer paths that nobody has funded. Compliance guidance is read conservatively, which favours the maximal action. And the customer harmed has no mechanism that reaches the people configuring this.

## What a Fix Looks Like
Build the middle of the action set. Introduce graded responses — transaction limits, holds on new payees only, step-up verification, a monitored period, a partial balance hold — which is the fix and matches the response to the confidence rather than to the worst case. Preserve access to funds wherever the specific risk does not require otherwise, since the rent money is the harm and much of the time it is not what the signal was about. Ask the customer for the resolving evidence immediately, because most false positives clear with one document and there is frequently no route to supply it. Set an explicit review clock with a commitment, so the customer knows when rather than being told nothing. Explain what happened to the extent permitted, connecting to the support agent niche, since an unexplained restriction is the complaint even more than the restriction itself. Tie the severity to the model's confidence explicitly, so the action is proportionate by construction. Reverse quickly and cleanly when the review clears, including restoring anything cancelled. Measure the duration and severity distribution of restrictions, which nobody reports and which describes the customer harm precisely. Distinguish compliance-mandated holds from discretionary ones in the customer's own communication, since one is explicable and the other should be justified. And report false freeze rate and time-to-resolution as operating metrics, because a firm that measures these will manage them and one that does not will keep freezing wages by default.

## Who Feels the Pain
Customers who cannot pay rent because a signal fired at moderate confidence; analysts choosing between nothing and everything; and institutions whose churn and complaint volume is driven by their own action set.

## Impact If Fixed
The absence of a middle is an engineering default that became a policy, so a moderate-confidence signal produces a maximal action. Graded responses matched to confidence, with an immediate route to supply resolving evidence, address the harm without changing the risk appetite.
