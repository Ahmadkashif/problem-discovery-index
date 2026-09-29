# A Vendor Deploys and Nobody Knows

**Niche:** [[niches/headless-commerce-vendors/composed-system-verification/profile|Composed System Verification]]
**Industry:** [[industries/headless-commerce-vendors|Headless Commerce Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Six vendors deploy to the retailer's production experience on their own schedules with no notice, so the retailer's system changes several times a week and nothing records when or by whom.
**Tags:** #change-point-detection #compliance #automation #evaluation-metrics #data-integration #descriptive-statistics #quick-win #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to verify continuously that a system assembled from six vendors produces correct prices, consistent inventory and acceptable performance — and whoever does that takes the category, because the architecture removed the guarantee and nobody replaced it.

## The Problem
Conversion drops four percent on a Wednesday. The retailer's own deployment log is empty; nothing changed on their side. In the same period the search vendor shipped a relevance update, the personalisation vendor changed a model, and the content platform released a version with a different caching behaviour. None of them told anybody, none were obliged to, and the retailer has no record that any of it happened. The investigation begins by asking six account managers whether anything changed, which takes days and produces partial answers.

## Why It's Still Broken
Vendors deploy continuously to their own service and consider the retailer's environment unaffected, which is true of the interface and false of the behaviour. Change notification is not in the contracts because nobody wrote it in. The retailer's own change management covers their own code. And the resulting investigations are attributed to the complexity of the architecture rather than to a missing feed.

## What a Fix Looks Like
Build the change timeline. Require every vendor in the stack to publish a change feed with timestamps and a behavioural description, as a contractual term, which is cheap for the vendor and transforms every investigation the retailer runs — this is the fix and it is a procurement decision more than an engineering one. Detect vendor changes independently where the feed is absent, by monitoring behavioural fingerprints on the services the retailer depends on, since the trustworthy version does not rely on the vendor's cooperation. Assemble one change timeline across all vendors and the retailer's own deployments, and annotate every metric chart with it, which turns a multi-day investigation into a glance. Require notice for behavioural changes, since a relevance model update is a behavioural change even though nothing in the interface moved. Run the verification suite automatically on any detected change, so a vendor's deploy is validated against the composition. Escalate on a correlated metric movement with a named change. Record the change history as evidence, since these conversations become commercial ones. And report how many incidents traced to an unannounced vendor change, because that number is the case for the contractual term.

## Who Feels the Pain
Retailers investigating changes they were not told about; on-call engineers asking account managers what happened; and vendors whose blameless deploy becomes a two-day dispute.

## Impact If Fixed
Six parties change the retailer's production experience weekly with no record, and every investigation starts by asking account managers. A contractual change feed is cheap for the vendor, and independent behavioural fingerprinting gives the retailer a version that does not depend on cooperation.
