# Teaching a Two-Hundred-Page Policy

**Industry:** [[content-moderation-services|Content Moderation Services]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** New reviewers are trained on a long policy document that changes weekly, and consistency across thousands of people is expected to emerge from that.
**Tags:** #bert #transformers #large-language-models #k-nearest-neighbors #evaluation-metrics #confidence-intervals #compliance #worker-facing

## The Problem
Platform content policies are long, detailed, frequently updated and full of edge cases that were added because something happened. A reviewer must internalise enough of one to make hundreds of decisions a day, in a queue where cases arrive in random order across every category.

Training is classroom and shadowing, followed by a certification test, followed by production with quality monitoring. Policy updates arrive as bulletins, sometimes weekly, sometimes mid-shift, and are absorbed through announcements and team meetings. A reviewer who has been out for a fortnight returns to a policy that has changed in ways nobody enumerates.

Consistency across thousands of reviewers in dozens of markets is expected to emerge from this, and it does not. The same case will be decided differently by different reviewers, and by the same reviewer on a different day, and the industry manages that with audits rather than by addressing the cause.

The enforcement precedent is the missing artefact. Decisions made on similar past cases are the most useful guidance a reviewer could have and are not retrievable — there is no case law, only a policy document and an auditor.

## What Already Exists
Vendors run substantial training organisations with structured curricula, certification and refresher programmes. Platforms supply policy documentation and update channels. Quality audit provides feedback, after the fact. Knowledge base tools hold policy and guidance. Some operations maintain internal question channels where reviewers ask team leads about hard cases, which is where the real precedent lives and where it stays.

## The Customisation Gap
Retrieval of precedent is the obvious unbuilt capability. Given the case in front of a reviewer, surfacing the most similar previously-adjudicated cases with their outcomes and reasoning would provide exactly the guidance a policy document cannot — and the corpus exists, since every decision made is a case with an outcome.

Policy change communication is the second gap. What changed, which categories it affects, which past decisions would now be decided differently, and which specific reviewers need to know — all derivable from the diff and the reviewer's own case mix, and currently delivered as a bulletin everybody skims.

Personalised training is the third. A reviewer's audit history shows which policy areas they get wrong, and targeted refresher on those areas is considerably more useful than a generic annual retrain. The data exists in the quality system and is used for performance management rather than for teaching.

And the customisation is per client. Each platform's policy is different, so none of this transfers between accounts — which is precisely why a vendor serving several platforms needs it built as a system that takes a policy and a case corpus rather than as a bespoke build per client.

## Impact If Solved
Consistency is the product this industry sells and it is pursued through training and audit rather than through decision support. Precedent retrieval at the moment of decision addresses the cause directly, targeted policy-change communication closes the gap that opens every week, and personalised refresher turns audit data into teaching — which together would do more for consistency than any amount of additional auditing.
