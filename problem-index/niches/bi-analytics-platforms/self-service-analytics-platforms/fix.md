# Licences Bought and Never Opened

**Niche:** [[niches/bi-analytics-platforms/self-service-analytics-platforms/profile|Self-Service Analytics Platforms]]
**Industry:** [[industries/bi-analytics-platforms|BI & Analytics Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Organisations pay for hundreds of analytics licences whose holders have not opened the tool in six months, and the renewal is negotiated on the total rather than on the usage.
**Tags:** #descriptive-statistics #survival-analysis #k-means-clustering #evaluation-metrics #confidence-intervals #quick-win #revenue-impact #automation
**Contested on:** Every serious competitor here is fighting to let someone who is not an analyst get a correct answer without one — and that contest splits by delivery surface rather than by capability, which is why this niche is not terminal and is decomposed below.

## The Problem
A company holds eight hundred analytics licences. Roughly two hundred people open the tool in a given month and perhaps sixty do anything beyond viewing a dashboard someone sent them. The renewal comes round and is negotiated as a volume discount on eight hundred, because reducing the count requires naming the people to remove, which is a political act, and because nobody has assembled the usage picture that would make the case. The same conversation happens the following year with a slightly higher number.

## Why It's Still Broken
Usage reporting exists in every platform and is not oriented to this decision — it reports activity rather than entitlement against activity, and it certainly does not compute what could be reclaimed. Vendors have no reason to build the report that reduces their seat count. Internally, the person who would run the analysis is in the data team and the person who negotiates the renewal is in procurement, and neither has asked the other. And downgrading a colleague's licence is unpleasant enough that an unprioritised saving stays unrealised.

## What a Fix Looks Like
Produce the entitlement report and act on it. Usage per licensed user over twelve months, at a depth that distinguishes viewing from building, since those often carry different licence tiers and the mismatch between tier and behaviour is where most of the money is. Classify the population — builders, regular viewers, occasional viewers, dormant — and price each against the tier they hold. Automate the reclamation path with notice: a dormant licence flagged, the holder told, a window to object, then reclaimed into a pool, which removes the political act from the decision and is the mechanism that makes it happen at all. Report the reclaimable total before every renewal, which is the number the negotiation should start from. And watch the other direction too, because a viewer who repeatedly exports and rebuilds things in a spreadsheet is someone who needs a higher tier, and finding them is the part of this that improves the estate rather than only the bill.

## Who Feels the Pain
Data platform owners defending a budget they cannot justify in usage terms; finance signing renewals that grow independently of value; and the users on the wrong tier for what they actually do.

## Impact If Fixed
The data is complete in every platform and the report is a query, and the typical gap between licences held and licences used is large enough to be material at renewal. The notice-and-reclaim mechanism is what converts an analysis nobody acts on into a recurring saving.
