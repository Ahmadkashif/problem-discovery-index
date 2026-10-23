# Feasibility and Price Before the Van Leaves

**Niche:** [[niches/locksmiths/automotive-key-programming/profile|Automotive Key Replacement & Programming]]
**Industry:** [[industries/locksmiths|Locksmiths]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The locksmith quotes an all-keys-lost job on the phone without knowing whether any of their tools will program this exact vehicle, and finds out in the customer's driveway.
**Tags:** #gradient-boosting #survival-analysis #logistic-regression #feature-engineering #data-integration #worker-facing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to cut and program a working key on the first visit for any vehicle the dealer would quote days out, and whoever completes the most all-keys-lost jobs on site without a failed attempt takes the account.

## The Problem
Key programming success depends on details the call doesn't reveal: model year and build, immobilizer generation, mid-year security changes, and which tool and software version supports that combination. Coverage lists are coarse, and forum reports conflict. The locksmith quotes, drives out, tries one or two tools, and either completes in 30 minutes or spends two hours and leaves unpaid. Sometimes the attempt damages a module.

## Why Nobody Has Built This
The outcome data is scattered. Each tool vendor sees only its own tool's attempts. Locksmiths remember their own jobs but NASTF forbids storing the security data. Forums are anecdotes. No party has had a reason to pool outcomes, and tool vendors have reasons not to publish where they fail.

## What to Build
A feasibility service keyed to the VIN. It decodes the vehicle and maps it to an immobilizer family and key part. It then returns, for the locksmith's own tool set, the probability of success, the expected minutes, whether a bench read of the module is likely, and known failure modes with precautions. Outcomes come from participating locksmiths' job logs and, by agreement, from tool vendors' online telemetry: vehicle pattern, tool, version, procedure, result and time, never the codes. A pricing layer turns expected time and risk into a quote band. Hierarchical models pool sparse variants and update quickly when an automaker changes security mid-year.

## Target Customer
Automotive locksmiths and multi-truck firms doing all-keys-lost work; secondarily tool vendors, who would see their coverage gaps.

## Impact If Built
Jobs are accepted and priced on evidence, wasted trips and failed attempts fall, and newer technicians can take vehicles they would otherwise send to the dealer. For a busy automotive locksmith that is plausibly several recovered hours a week (estimate).
