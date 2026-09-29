# The Demand Partner Nobody Evaluates

**Niche:** [[niches/digital-native-publishers/advertising-stack-operations/profile|Advertising Stack Operations]]
**Industry:** [[industries/digital-native-publishers|Digital Native Publishers]]
**Type:** Fix (Pain Point)
**One-liner:** Fourteen demand partners are in the auction, three of them contribute almost nothing, and all fourteen add latency.
**Tags:** #quick-win #descriptive-statistics #evaluation-metrics #revenue-impact #automation #confidence-intervals #optimization-fundamentals #data-integration
**Contested on:** Every serious competitor in this niche is fighting to run a deep, leaky ad stack that funds the newsroom without destroying the page experience that retains readers — and whoever manages that trade with evidence rather than instinct keeps both revenue and audience.

## The Problem
Demand partners are added over years — each one promising incremental revenue, each one adding a call to the auction. Some win regularly and pay well. Some win occasionally at low prices. Some have not won a meaningful auction in a year and are still called on every page load. Nobody has ranked them by contribution net of the latency they add, because the report that would show it does not exist and removing a partner feels like removing revenue.

## Why It's Still Broken
Partners are added by a commercial conversation and removed by nobody, so the stack only grows — an addition has an owner and a removal does not. Contribution is reported per partner in isolation rather than as marginal value above the rest of the auction. Latency cost is unattributed. And the fear of losing revenue outweighs a cost nobody has measured.

## What a Fix Looks Like
Rank them and prune. Report each partner's win rate, revenue share and marginal contribution above the next bidder, which is the fix and is computable from auction logs. Measure the latency each partner adds, since that is the cost side and is directly observable. Identify partners whose marginal contribution is near zero, as they will be obvious once the report exists. Test removal on a traffic slice rather than debating it, which converts an argument into evidence and is easy. Review the partner list on a schedule with an owner, because a list nobody owns only accumulates. Check timeout behaviour, as partners that frequently time out add cost and contribute nothing. Look at duplicate demand, since the same buyer often reaches the publisher through several partners and the publisher pays fees twice. Report auction latency against page performance, which links the stack to the audience cost. Negotiate from the contribution data, as evidence changes the terms. And re-run the analysis quarterly, because partner performance shifts.

## Who Feels the Pain
Readers on slow pages; audience teams whose return visits decline for unexplained reasons; revenue teams carrying partners that contribute nothing; and publishers paying fees twice for the same demand.

## Impact If Fixed
An addition has an owner and a removal does not, so the partner list only grows. Ranking partners by marginal contribution against the latency they add is computable from auction logs and makes the prune obvious.
