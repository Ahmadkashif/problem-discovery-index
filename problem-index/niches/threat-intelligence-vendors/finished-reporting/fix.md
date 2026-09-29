# Fix: Published to the Portal and Nobody Knows

**Niche:** Finished Intelligence Reporting
**Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** An analyst spends a week on a careful assessment, it appears in a portal, and no mechanism exists by which they would ever learn whether it mattered.
**Tags:** #evaluation-metrics #confidence-intervals #worker-facing #workflow-orchestration #revenue-impact
**Contested on:** Whether a finished assessment reaches the person who can act on it in a form they can act on.

## The Problem

The report is finished. It goes to the portal, an email notification goes out, and the analyst moves to the next piece of work.

What happens next is invisible to them. Some subscribers may have read it. Some may have acted. Somewhere, possibly, a detection engineer implemented the described behaviours and caught something months later. Or the report was never opened by anyone with the context to use it.

The analyst will not learn which. There is no channel. The vendor may track page views, which measures whether a link was clicked. Customer success may hear anecdotally that a particular report was appreciated, and that anecdote reaches the analyst if someone remembers to pass it on.

So a profession of skilled people produces careful analytical work into a void. The consequences compound: analysts cannot tell which of their work is valuable, so they cannot improve. The vendor cannot tell which reporting to invest in, so production is driven by what analysts find interesting. And the quality difference between a genuinely useful assessment and a competent but irrelevant one is invisible to everyone, which means it is not rewarded.

## Why It's Still Broken

**Publishing is the completion event.** The production process ends at publication. Nothing in the workflow contemplates what happens afterwards.

**Customers have no reason to report back.** Telling a vendor that a report was useful, or that you acted on it, costs time and returns nothing. Most customers would do it if asked simply and would not initiate it.

**Page views are available and meaningless.** A metric exists, it is easy, and it measures link-clicking. Its availability reduces pressure to measure anything real.

**Acting on intelligence happens later and elsewhere.** A detection deployed from a report catches something three months later, in a different system, with no link back. Even a willing customer would struggle to attribute it.

**Asking invites an unwelcome answer.** A vendor that asks whether reporting is used may learn that most of it is not, which is the most important thing they could learn and the least comfortable.

**Analysts do not ask for it.** The absence of feedback is so complete that it is treated as a property of the job rather than as a fixable gap.

## What a Fix Looks Like

**Ask, simply, at the point of reading.** One question at the end of a report: was this relevant, did you act, what would have made it more useful. Low friction, in context, answered by a minority — and that minority is infinitely more than zero.

**Track operational consumption, not page views.** Whether detections were extracted, whether hunt queries were run, whether indicators were promoted to blocking. Where the vendor supplies structured artefacts, this is directly measurable.

**Give analysts a quarterly feedback digest.** What their reporting produced, in whatever form is available — read rates among relevant customers, the feedback received, anything a customer volunteered. Even partial feedback is a substantial change from none.

**Close the loop on the hunt.** Where a vendor supplies hunt queries with a report, ask whether they found anything. This is the most direct evidence a report mattered, and it is a single question to customers who ran the hunt.

**Distinguish reach from relevance.** A report read by many irrelevant subscribers and one read by the three customers it applied to are different outcomes, and undifferentiated read counts make the second look like failure.

**Make customer intelligence requirements explicit.** A customer who has stated what they need to know can be asked whether a report answered it, which is a far better feedback question than whether they liked it.

**Reward relevance, not volume.** If analysts are assessed on reports published, production optimises for volume. Assessing on whether reporting reached and helped the customers it concerned would change what gets written.

## Who Feels the Pain

The analyst, doing careful work for years with no signal about whether any of it was useful — which is a recognised driver of attrition in intelligence work generally.

The vendor, unable to direct production toward what customers need because they have no idea what customers used.

The customer, receiving a stream of reporting shaped by what analysts found interesting rather than by what would help them.

And the reporting that would have mattered, published to a portal nobody with the right context happened to open.

## Impact If Fixed

A single in-context question at the end of a report is close to free and would give an industry its first feedback on its analytical product.

Tracking operational consumption — detections extracted, hunts run — measures the thing that matters and is directly available wherever a vendor supplies structured artefacts.

And giving analysts a quarterly digest of what their work produced would change the experience of the job substantially, in a profession where the complete absence of feedback is currently treated as normal.
