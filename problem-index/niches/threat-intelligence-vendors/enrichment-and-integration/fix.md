# Fix: Everyone Runs the Same Lookup Separately

**Niche:** Enrichment & Integration
**Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Thousands of organisations perform the same passive DNS and ownership lookups about the same addresses, separately, because the vendor shipped a value and a type.
**Tags:** #evaluation-metrics #data-integration #automation #workflow-orchestration #revenue-impact
**Contested on:** Whether context arrives attached to the indicator or is assembled by whoever needs it, every time.

## The Problem

An indicator arrives as a value and a type. To act on it, somebody needs to know what it is — who owns the address, what else resolves there, whether it is shared hosting, what the domain's registration history looks like.

So every organisation receiving that indicator performs the same lookups. Against the same commercial passive DNS provider. Against the same registration data. At their own cost, through their own integration, with their own rate limits and their own inconsistencies in how the results are interpreted.

The vendor could have done it once. They already hold much of it — they discovered the indicator through infrastructure analysis and know what it resolved to and what it was serving. Enriching at the source costs one lookup for all customers instead of one per customer.

The duplication is substantial in aggregate. A widely-distributed indicator is enriched independently by every organisation that receives it, which across an industry is the same query run thousands of times about the same address within the same week.

It also produces inconsistency. Two organisations enriching the same indicator from different sources reach different conclusions about what it is, which shows up as different triage outcomes for the same activity.

## Why It's Still Broken

**Enrichment is treated as the customer's layer.** The vendor ships intelligence; the customer's platform enriches. The division is conventional and nobody has questioned whether it is efficient.

**Enrichment data has licensing constraints.** Some commercial enrichment cannot be redistributed, so a vendor enriching and shipping the result may be redistributing licensed data. This is a real constraint and it does not cover the enrichment a vendor derives from its own collection.

**Feed formats encourage minimalism.** The widely-used simple formats are lists. Richer formats exist and are used partially, so the common denominator is a value and a type.

**Downstream systems accept little.** Matching engines take value lists, which makes richer delivery appear pointless even where the alerting layer could use it.

**Customers pay for enrichment separately.** Enrichment providers sell directly to end users, so there is an established commercial arrangement in which the customer does this work.

**Nobody has measured the duplication.** The aggregate cost is invisible because it is spread across thousands of separate budgets.

## What a Fix Looks Like

**Ship what the vendor already knows.** Infrastructure type, hosting context, what the indicator was observed serving, related infrastructure, the campaign it belongs to. This is the vendor's own collection data, involves no third-party licensing, and is the majority of what a customer looks up.

**Use the richer formats properly.** STIX carries relationships, context and confidence. Most pipelines reduce it to values. Both vendors and consuming platforms could use the format's existing capability rather than defaulting to the lowest common denominator.

**Enrich once at the customer's ingestion layer, not per alert.** Where the vendor cannot ship enrichment, the customer should enrich at ingestion rather than at alert time. This deduplicates within the organisation at minimum and is a straightforward pipeline change.

**Cache and share within the organisation.** Many organisations enrich the same indicator repeatedly across different alerts because the results are not cached.

**Separate what can be redistributed from what cannot.** Vendors should ship their own derived context freely and reference licensed enrichment rather than embedding it, which addresses the licensing constraint without abandoning the principle.

**Ask for enrichment in procurement.** A buyer requiring that indicators arrive with infrastructure context and campaign association changes what vendors ship, and is a question they can ask at the next renewal.

## Who Feels the Pain

The SOC analyst, waiting for lookups to return before they can assess an alert that could have arrived assessed.

The organisation, paying for enrichment subscriptions to derive context the intelligence vendor already had.

Smaller organisations most, since enrichment subscriptions have a fixed cost and they receive the same indicators as everyone else with less budget to interpret them.

And the industry in aggregate, running the same query about the same address thousands of times a week.

## Impact If Fixed

Vendors shipping their own collection context costs them one enrichment for all customers instead of one per customer, and it is data they already hold with no licensing obstacle.

Using the richer formats' existing capability requires no new standard — the fields exist and both ends default to ignoring them.

And enriching at ingestion rather than per alert is a pipeline change available to every organisation today that would eliminate the repeated lookup within their own operation immediately.
