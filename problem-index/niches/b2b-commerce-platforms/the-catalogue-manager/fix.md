# The Manufacturer Changed the Spec

**Niche:** [[niches/b2b-commerce-platforms/the-catalogue-manager/profile|The Catalogue Manager]]
**Industry:** [[industries/b2b-commerce-platforms|B2B Commerce Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Manufacturers revise specifications, supersede parts and change packaging without telling anyone, and the distributor finds out when a customer receives the wrong thing.
**Tags:** #change-point-detection #compliance #evaluation-metrics #workflow-orchestration #automation #quick-win #data-integration #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to tell the catalogue manager which gaps are costing sales — and whoever ranks the work by revenue at risk turns an endless backlog into a finite prioritised queue.

## The Problem
A manufacturer revises a datasheet. The dimension changes by two millimetres, or the part is superseded, or the case quantity goes from twelve to ten. Nobody is notified. The distributor's catalogue continues to state the old value for months or years. A customer orders on that specification, receives something that does not fit or a quantity they did not expect, and the return, the credit and the lost confidence all land on the distributor, who published data they received in good faith and had no mechanism to keep current.

## Why It's Still Broken
There is no notification standard — manufacturers publish PDFs and portals and expect distributors to check. The distributor carries thousands of suppliers and cannot poll them all. Detecting a change means diffing documents nobody stores. And the cost appears as returns and credits attributed to shipping or picking rather than to catalogue drift, so the root cause is never counted.

## What a Fix Looks Like
Detect the change rather than wait to be told. Store every source document with its retrieval date and diff on each refresh, which is mechanical, requires no cooperation from the manufacturer, and is the whole of the fix — the reason it does not exist is that nobody keeps the documents. Monitor manufacturer sources on a schedule weighted by revenue and volatility, since polling everything equally is neither necessary nor possible. Flag changed attributes for review rather than auto-applying them, because a diff is not always a correction. Track supersession explicitly as a first-class relationship, which is the most consequential change type and the one most often missed. Alert on packaging and unit-of-measure changes with priority, since those produce the most expensive errors and the least ambiguous diffs. Notify customers who bought on a specification that has since changed, which no distributor does and which is the difference between a returned order and a prevented one. Score suppliers on change frequency and notification quality, giving merchandising a lever. And attribute returns and credits to catalogue accuracy where the data supports it, which is how the problem finally becomes visible to the people who fund the fix.

## Who Feels the Pain
Catalogue managers publishing data they cannot verify; customers receiving parts that do not match the specification; and distributors absorbing returns caused by someone else's revision.

## Impact If Fixed
Diffing stored source documents needs no cooperation from the manufacturer and is the entire fix — it is absent only because nobody keeps the documents. Attributing returns to catalogue drift makes a cost currently booked to shipping visible to the people who would fund the work.
