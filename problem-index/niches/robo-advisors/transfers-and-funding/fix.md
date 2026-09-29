# Six Weeks and No Status

**Niche:** [[niches/robo-advisors/transfers-and-funding/profile|Transfers & Funding]]
**Industry:** [[industries/robo-advisors|Robo-Advisors]]
**Type:** Fix (Pain Point)
**One-liner:** The client initiated a transfer from their old custodian a month ago and has no idea whether anything is happening.
**Tags:** #workflow-orchestration #quick-win #automation #evaluation-metrics #data-integration #descriptive-statistics #worker-facing #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to keep money arriving — through an account transfer that stalls and a contribution that quietly stops — and whoever detects and recovers both without a human takes the growth the funnel currently leaks.

## The Problem
The client decided to move their account, signed the transfer form, and waited. Somewhere in the process the delivering firm rejected the request because a name field did not match, or the account type was misidentified, or a residual position could not transfer. Nobody told the client. They check the app, see nothing, assume it is in progress, and after five weeks either call support or give up. This is the first experience a new client has of the platform.

## Why It's Still Broken
Transfers run on legacy inter-custodian infrastructure and were implemented as an operations queue, so status lives in a back-office system and no one connected it to the client view. Rejection reasons are cryptic codes. Operations is measured on transfers completed rather than on elapsed time. And abandoned transfers are not counted at all.

## What a Fix Looks Like
Show the status and prevent the rejection. Surface transfer state to the client in plain language, which is the fix and requires connecting an existing operational status to the app. Set expectations at initiation with a realistic timeframe, since silence is tolerable when it was predicted and intolerable when it was not. Validate the information before submission against the known rejection causes, because the same handful of mismatches cause most rejections and are checkable up front. Translate rejection codes into an action the client can take, as the codes are currently passed to support and stop there. Detect a stalled transfer and act rather than waiting for the client to ask, since elapsed time is visible and nobody watches it. Report abandonment, which is the number that measures the real cost and does not currently exist. Handle partial transfers explicitly, because residual positions are common and leave the client believing the move failed. Prompt the delivering firm on a schedule, as follow-up is currently ad hoc. Notify on completion with what arrived, since clients frequently do not notice. And measure median and tail transfer time, because the tail is where every abandoned client sits.

## Who Feels the Pain
New clients waiting weeks with no information; support teams fielding status calls they cannot answer; operations chasing rejections after the fact; and platforms losing clients at the moment of highest intent.

## Impact If Fixed
Transfers were implemented as a back-office queue and nobody connected status to the client view. Surfacing state and pre-validating against the common rejection causes removes most of the delay and all of the silence.
