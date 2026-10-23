# The Greeting Gets Scored and the Escalation Does Not

**Niche:** [[niches/answering-services/call-quality-scoring/profile|Call Quality & Escalation Compliance Scoring]]
**Industry:** [[industries/answering-services|Telephone Answering Services]]
**Type:** Fix (Pain Point)
**One-liner:** QA scorecards reward greeting in the client's name and polite closing, while the item that decides lawsuits and cancellations, whether the urgent call was escalated in time, is rarely on the form.
**Tags:** #evaluation-metrics #descriptive-statistics #compliance #workflow-orchestration #quick-win
**Contested on:** Every serious competitor in this niche is fighting to prove, call by call, that each client's script was followed and every escalation was made inside its time limit, and whoever can put that evidence for every call in front of the client at renewal takes the account.

## The Problem
Supervisors score sampled calls on a standard form: greeting, tone, spelling, closing. Escalation correctness requires knowing the account's rules and checking the paging log, which takes longer, so it is skipped unless a complaint triggers it.

## Why It's Still Broken
The scorecard came from general customer-service practice and from the courtesy criteria external awards also judge. Scoring escalation needs data from two systems (recording and paging log) that the reviewer must open separately.

## What a Fix Looks Like
Rebuild the scorecard around escalation, with courtesy secondary. Put the call's paging and acknowledgement timeline beside the recording in the review screen, and oversample calls that involved a page, a hold on a medical account or a patch.

## Who Feels the Pain
Clients exposed by missed escalations; operators coached on the wrong things; owners who discover the problem through a lawsuit.

## Impact If Fixed
At no extra review time, QA attention moves to the calls that carry the service's liability and its renewals.
