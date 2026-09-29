# The Corrections Nobody Learns From

**Niche:** [[niches/spend-management-platforms/gl-coding-and-erp/profile|GL Coding & ERP Integration]]
**Industry:** [[industries/spend-management-platforms|Spend Management Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The controller recodes the same merchant to the same account every month and the system never notices.
**Tags:** #quick-win #automation #evaluation-metrics #worker-facing #descriptive-statistics #data-integration #workflow-orchestration #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to code transactions correctly into a chart of accounts unique to every customer without rebuilding the model from scratch each time — and whoever transfers learning across customers makes implementation weeks instead of months.

## The Problem
Every month the controller opens the transaction list and recodes the same items: this vendor to the marketing account rather than software, this recurring charge to a different department, this project code on anything from that team. It is the same correction, made the same way, for the same reason, month after month. The system records the change and treats the next occurrence identically to the last. Nobody has counted how many corrections are repeats.

## Why It's Still Broken
Corrections are treated as editing, so the system records the new value and discards the fact that a correction occurred — the event is flattened into a state change. Rules exist but must be authored deliberately and controllers do not think of themselves as configuring software. Nobody reports correction volume. And the work is absorbed monthly by one person.

## What a Fix Looks Like
Notice the repeat and offer the rule. Detect a repeated correction and propose a rule, which is the fix and is a pattern match a system can do trivially. Report correction rate and the most-corrected merchants, since it is one query and will reveal that a handful of vendors account for most of the work. Apply the correction retrospectively to matching open items, because the controller is about to make the same change twenty more times in the same session. Let a correction be made once for a recurring vendor rather than per transaction, as recurring charges are the bulk of the repetition. Track corrections by user and by field, which shows whether the problem is merchant mapping, department or project coding. Ask the controller to confirm a proposed rule rather than creating it silently, since trust matters and a wrong automatic rule is worse than the correction. Surface the uncertain codings for review rather than presenting everything as equally confident, which focuses attention. Carry the rules through chart of accounts changes, because they currently break silently. Measure time spent recoding, since it is a large part of the month and is unmeasured. And feed the corrections into the shared model, as they are the training data the transfer problem needs.

## Who Feels the Pain
Controllers recoding the same items monthly; accounting teams whose close is lengthened by it; implementation teams whose rules never covered it; and platforms whose accuracy metric does not exist.

## Impact If Fixed
The system records the new value and discards the fact that a correction happened, flattening an event into a state change. Detecting repeats and proposing rules removes the recurring work and produces the labels the coding model needs.
