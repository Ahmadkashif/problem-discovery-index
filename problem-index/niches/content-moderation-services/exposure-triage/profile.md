# Exposure Triage

**Parent Industry:** [[industries/content-moderation-services|Content Moderation Services]]
**Category:** Contested Sub-Niche
**Contested on:** Whether each item routed to a human reviewer actually required a human, and whether anyone can demonstrate how much of the queue did not.

## Profile

**Market Size:** ~$1.4B
**Share of Parent Industry:** ~12%
**Digital Adoption:** Low — the queue arrives composed
**Target Buyer:** Vendor operations leadership, platform trust and safety
**Automation Potential:** Very high — it is a routing and classification problem

## What Makes This a Distinct Niche

This is the volume half of exposure management: reducing the *number* of times a person is shown distressing material, by establishing which items genuinely need human judgement and which reached a human because the routing had no better option.

It is separable from its sibling in every way that matters. [[niches/content-moderation-services/presentation-controls/profile|🎯 Presentation & Dosimetry]] takes the item as given and changes what it does to the viewer; triage decides whether the viewer sees it at all. Triage is a classification and routing problem, measurable within weeks against a straightforward target — severe items routed to humans, and the error rate that reduction costs. Dosimetry is an interface and occupational health problem whose evidence is clinical and arrives over months. A vendor can build triage and never build dosimetry, and most would, because triage also reduces cost.

The contest is over a question nobody currently asks: of the items a reviewer saw today, how many could have been resolved without them. The honest answer in most operations is a large fraction — duplicate and near-duplicate material that has been adjudicated thousands of times, items the classifier was highly confident about but routed anyway because the policy requires human confirmation, items where the decision turned on a text field the reviewer had to open a video to reach. Nobody measures it, because measuring it requires classifier visibility the vendor is rarely given and would produce a number that embarrasses the party who composed the queue.

## Current Tools & Gaps

Platform-side classifiers do the primary filtering and are genuinely capable at the high-confidence extremes. Hash-matching against known-violating material is mature, well deployed for the worst categories, and is the single most effective exposure reduction ever built in this industry — it prevents re-review of material already adjudicated. Some platforms operate confidence thresholds that auto-action the clear cases.

The gaps are on the vendor's side of the line. Near-duplicate detection beyond exact hashing is patchy, so visually similar variants of adjudicated material are reviewed again and again. Nothing routes on the basis of what the decision actually turns on, so a reviewer opens a video when the determining evidence was in the caption. Escalation paths are one-directional — a reviewer who realises an item needed no human has no way to send that signal back into routing. And the vendor is usually blind to classifier confidence on its own queue, which makes measuring avoidable review impossible and arguing about it futile.

## Problems

- [[niches/content-moderation-services/exposure-triage/build|🔨 Build: The Avoidable Review]]
- [[niches/content-moderation-services/exposure-triage/buy|🛒 Buy: Near-Duplicate Detection From Content Integrity]]
- [[niches/content-moderation-services/exposure-triage/fix|🔧 Fix: The Queue Arrives Composed]]
