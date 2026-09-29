# Fix: Nothing Ever Leaves the Feed

**Niche:** Indicator Lifecycle & Decay
**Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Adding an indicator requires a collection event and removing one requires a decision, so feeds only grow and the growth is presented as coverage.
**Tags:** #evaluation-metrics #confidence-intervals #descriptive-statistics #automation #worker-facing #revenue-impact
**Contested on:** Whether an indicator is retired when it stops describing reality, or accumulates indefinitely.

## The Problem

Indicators enter a feed automatically, from collection. They leave when somebody decides to remove them.

That asymmetry determines everything. Collection runs continuously and requires no human judgement. Retirement requires someone to look at a specific indicator, conclude it is no longer valid, and take an action they could be wrong about. So content flows in and does not flow out, and a feed's size grows monotonically regardless of how much of it still describes anything.

The growth is then presented as a virtue. Indicator counts appear in marketing material and procurement comparisons, where a larger number reads as better coverage rather than as a longer historical archive.

The customer receives the archive as though it were current. Their matching engine treats a four-year-old address the same as one added this morning. Their analysts investigate matches on both. And the proportion of the feed that is historical grows every year, which means the false positive rate attributable to staleness grows with it.

Nobody is acting badly. Retention is the default, removal is effortful and risky, and the only visible metric rewards the accumulation.

## Why It's Still Broken

**The default is retention and defaults govern.** No positive action is required to keep an indicator, so keeping is what happens.

**Removal carries attributable risk.** An indicator retired and later implicated is a specific error with a name attached. Stale content produces diffuse false positives that nobody attributes to anyone.

**The count is the metric.** Indicator volume is published, compared and optimised. Nothing measures currency, so nothing rewards it.

**Age is recorded and not acted on.** Most feed formats carry a first-seen date. The information is present and no default behaviour uses it.

**Customers can filter and do not.** Age filtering exists downstream, needs configuration, and is rarely applied — so the problem sits with the party least able to judge what an appropriate age threshold is per indicator type.

**The historical archive has genuine value.** Old indicators are useful for retrospective hunting and research, which is a real argument for retaining them — and not for shipping them in the same stream as current content.

## What a Fix Looks Like

**Separate the current feed from the historical archive.** Two products: indicators believed to describe live infrastructure, and the full historical corpus for retrospective hunting. This resolves the tension directly — the archive keeps its value and stops contaminating the operational stream.

**Make retirement the default with a renewal.** An indicator expires unless something re-confirms it. Inverting the default is the structural fix, and re-confirmation can be automatic where the indicator continues matching or the infrastructure is still observed serving malicious content.

**Publish the age distribution.** A customer should see the age profile of what they receive. Vendors with current content benefit from the comparison, which is what would make currency a competitive attribute rather than an invisible one.

**Apply age filtering by default downstream.** Customers ingesting feeds should apply type-appropriate age thresholds as a default configuration rather than as an option nobody enables. This is available to every organisation today.

**Report retirement rate as a quality metric.** How much content a vendor retired this quarter, and why. A feed that never retires anything is telling you something, and no vendor currently reports it either way.

**Handle hashes separately.** Hashes do not decay like network indicators, and applying one lifecycle policy across types produces the wrong answer for at least one of them.

**Ask for currency in procurement.** A buyer asking what proportion of a feed was observed in the last ninety days changes the conversation from volume to currency, and is a question any buyer can ask tomorrow.

## Who Feels the Pain

The SOC analyst, investigating matches on infrastructure that stopped being malicious years ago.

The organisation that blocked a legitimate service because a reallocated address was still in a feed.

The customer, paying for a subscription whose headline number is substantially a historical archive.

And vendors who do retire diligently, whose smaller indicator counts look worse in a comparison that has no currency column.

## Impact If Fixed

Separating the current feed from the historical archive resolves the tension between operational currency and research value, and it is a packaging decision rather than a technical one.

Inverting the default so indicators expire unless re-confirmed is the structural fix, and re-confirmation is largely automatable for any vendor observing their own indicators.

And publishing the age distribution would make currency visible in procurement, which is the mechanism by which it would start being rewarded rather than quietly ignored.
