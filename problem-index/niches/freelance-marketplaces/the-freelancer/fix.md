# Fix: Nobody Knows Their Effective Hourly Rate

**Niche:** [[niches/freelance-marketplaces/the-freelancer/profile|The Freelancer]]
**Industry:** [[industries/freelance-marketplaces|Freelance Marketplaces]]
**Type:** Fix (Pain Point)
**One-liner:** A freelancer quotes $75 an hour, and after proposal writing, revisions, scope creep and admin, earns something closer to $40 — and has never computed which.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #feature-engineering #data-integration #worker-facing #workflow-orchestration #quick-win
**Contested on:** Whether the unpaid hours can be attributed to the contracts that caused them.

## The Problem

A freelancer's rate is the number they quote. Their actual earnings per hour worked is that number divided by a multiplier nobody computes, made up of the proposals that produced nothing, the revision rounds beyond what was priced, the scope that expanded without a change order, the client communication, the invoicing, and the platform fee.

The consequences of not knowing are specific and expensive. Freelancers cannot tell which clients are profitable and which are quietly subsidised — and the subsidised ones are typically the pleasant, demanding, repeat clients they most want to keep. They cannot tell whether a fixed-price contract was a good deal. They price the next job from the last job's quoted rate rather than its realised one, so the error propagates. And when they consider raising rates, they have no evidence about what they are currently earning, so they do not.

## Why It's Still Broken

Time tracking exists and freelancers largely do not use it for unpaid work. Tracking billable hours has an obvious purpose — it produces an invoice. Tracking the two hours spent on proposals that went nowhere produces only a depressing number, and the discipline required to log it consistently is exactly the discipline that fails when someone is busy.

Attribution is genuinely awkward too. Proposal time is spent before there is a contract to attribute it to, and most of it never becomes one. Attributing failed-proposal time across won contracts is the correct treatment and is not obvious to anyone without a cost accounting background, which is essentially the entire population.

And the platforms have no interest. A freelancer who computed their true effective rate might raise it, price fixed work higher, or take less of it.

## What a Fix Looks Like

Compute it from what already gets captured, and only ask for logging where nothing else will do.

Most of the inputs are already recorded somewhere. Proposal submissions are timestamped in the platform export. Message volume and timing on a contract is a good proxy for communication load. Milestone and revision cycles are in the contract record. Platform fees are explicit. Calendar entries carry client names. A tool assembling these gets a defensible estimate of total hours per contract without the freelancer logging anything, and an estimate that exists beats a precise number that does not.

Attribute the unpaid overhead properly. Proposal time in a period, including proposals that failed, spread across contracts won in that period — that is the correct cost accounting and it is the step that converts a per-contract number into a realised rate. Show the win-rate sensitivity explicitly, because a freelancer whose proposal win rate is 10% is carrying nine failed proposals on every contract and that arithmetic, seen once, changes behaviour.

Then report the thing that matters: realised rate per contract, per client and per contract type, ranked. The output people react to is the client list sorted by realised rate, because it almost always contains a surprise — the demanding repeat client who looked like the best account and is near the bottom, the one-off that looked small and was the most profitable hour of the quarter.

Add the comparison to quoted rate, per contract, with the gap decomposed: fees, unpriced revisions, scope expansion, communication, proposals. Naming which component dominates tells the freelancer what to change — a large revision component is a contracting problem, a large proposal component is a targeting problem, and these call for completely different responses.

Keep manual logging minimal and optional, for the genuinely uncaptured. The tool should be useful on day one from exported history alone, with logging as refinement rather than precondition — because a tool requiring a month of diligent logging before it says anything is a tool nobody finishes setting up.

## Who Feels the Pain

Every freelancer, most acutely those on fixed-price work where scope expansion has no meter running, and those early in their career who set rates by copying what others charge without knowing what anyone realises. Also anyone deciding whether freelancing is viable at all, who is making that decision against a number that overstates their income by a large and unknown factor.

## Impact If Fixed

A freelancer finds out what they actually earn per hour worked, which is the foundational number for every pricing, client and capacity decision they make and the one they have never seen. The client profitability ranking alone typically reprices or ends one relationship immediately. And rates across this market are set by people working from the quoted number — correcting that, individually, is the most direct thing anyone can do about the downward pressure that defines the industry.
