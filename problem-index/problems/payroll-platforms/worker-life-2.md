# Support During a Missed Deposit

**Industry:** [[payroll-platforms|Payroll Platforms]]
**Type:** Worker Life Changing
**One-liner:** Support representatives stop taking calls from people whose rent is due and whose pay did not arrive, because failed disbursements are detected and worked before the employee opens their banking app.
**Tags:** #change-point-detection #gradient-boosting #time-series-forecasting #evaluation-metrics #confidence-intervals #automation #workflow-orchestration #worker-facing

## The Problem
A direct deposit fails. The account was closed, the routing number was mistyped, the bank rejected it, the file was late, the employer's funding did not clear. The employee finds out on payday, when the money is not there.

They call. Sometimes they call their employer, who calls the provider. Sometimes they call the provider directly. Either way the conversation reaches a support representative, and the person on the other end has bills timed to that deposit.

The representative's job is to establish what happened and get the money moving — a reversal and reissue, a wire, a same-day ACH, a paper cheque — while the caller is distressed and the options all take time the caller does not have. Payroll support runs at volume on paydays for exactly this reason, and paydays cluster on Fridays and at month end.

The representative usually resolves it. They do so in a conversation where the stakes are immediate and personal, several times a day, on days when the queue is already at its peak.

## Why It Matters to the Worker
This is among the most emotionally demanding support queues in software, and the reason is that the product failure lands on a household budget. A caller whose rent is due is not upset about a feature; they are frightened, and the representative absorbs that directly.

The frustration is that a large share was preventable and visible earlier. A rejected account was rejected by the bank when it was added, days before payday, and nothing acted on the rejection. A late file was late while there was still time to expedite. A funding shortfall was predictable from the employer's balance history.

Representatives can see this in the account history when the call comes in, which makes each conversation an exercise in explaining a failure the system knew about and did not surface.

The queue also clusters. Payday volume is entirely predictable and staffing rarely reflects it, so the hardest calls arrive when the wait times are longest, which makes every caller angrier before the conversation starts.

## What a Solution Looks Like
Pre-validate accounts when they are entered rather than when they are paid. Account verification services exist and catch most invalid accounts days ahead, when a correction is trivial.

Detect funding risk before the deadline. An employer whose account will not cover the run is predictable from balance and history, and the difference between finding out at funding and finding out a day earlier is the difference between an expedite and a failure.

Monitor disbursement outcomes actively. Returns and rejections arrive as messages, and the employee should be told and remediated before they discover it themselves — an outbound message saying the deposit failed, why, and what is happening now is a fundamentally different experience from an empty account.

Staff to the payday curve, which is known months in advance and is not a forecasting problem at all.

And when a call does come, the representative should open with the cause identified and the remediation options priced by arrival time, rather than beginning an investigation.

## Impact If Solved
A missed deposit is the most consequential failure in payroll and it is currently discovered by the person it harms. Detecting and remediating before payday removes the harm and, with it, the hardest recurring conversation in the provider's support organisation.
