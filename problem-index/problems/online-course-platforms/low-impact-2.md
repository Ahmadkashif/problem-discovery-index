# Course Maintenance and Content Decay

**Industry:** [[online-course-platforms|Online Course Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** A technical course is materially wrong eighteen months after recording, ranking signals lag by years, and the only mechanism for noticing is a learner complaining in the Q&A.
**Tags:** #bert #transformers #large-language-models #change-point-detection #gradient-boosting #evaluation-metrics #automation #workflow-orchestration

## The Problem
Recorded courses decay. A course on a web framework, a cloud console, a design tool or a tax rule is accurate on the day it was made and degrades from then on: interfaces are redesigned, APIs deprecate, defaults change, a menu item moves. The learner following along finds the screen does not match, loses confidence in the whole course, and either struggles through or leaves.

Nothing detects this. The platform ranks by rating and enrolment, which are accumulated over the course's life and therefore reward age. Instructors update when they have time, and updating means re-recording video, which is expensive enough that many never do. Marketplace incentives make it worse: an established course with four years of ratings outranks a current one, so the rational strategy is to keep selling the old recording.

The signal is sitting in plain sight. Q&A threads fill with learners saying the interface has changed; completion rates at a specific lesson drop; refund reasons cluster. All of it is in the platform's data and none of it is aggregated into a statement that a course has decayed.

## What Already Exists
Platforms show a last-updated date, which instructors can advance with a trivial change. Udemy and others surface recency in ranking to a limited degree. Q&A and review systems collect learner complaints. Some creator platforms provide analytics showing drop-off by lesson. Version-specific courses exist for major software releases where the vendor's release cadence forces it. Corporate learning systems have content review workflows that consumer platforms lack entirely.

## The Customisation Gap
Decay detection is an unbuilt inference over data the platform already has: drop-off concentrated at a specific timestamp in a specific lesson, Q&A content clustering around confusion at that point, review sentiment mentioning outdated material, and — the external half — the referenced tool's own release notes and documentation changing. Combining internal behaviour with the subject's external change history would identify decayed segments precisely rather than course-wide.

Precision matters because the remedy is expensive. Telling an instructor that their course is outdated is not actionable; telling them that lesson fourteen between four and seven minutes shows a fourfold drop-off spike since the tool's April release, with twelve Q&A threads about the changed menu, is a thirty-minute fix.

The customisation is per subject domain. A tax course decays on a legislative calendar, a framework course on a release cycle, a design course when a tool's interface is redesigned, and a management course barely at all. The external change signal is different in each case and the monitoring has to be domain-specific, which is why no generic feature has appeared.

And the ranking needs to reflect it. A freshness-adjusted ranking, where decay is measured rather than self-declared, would change the marketplace incentive from keeping the old recording alive to maintaining it.

## Impact If Solved
Content decay is a persistent and invisible tax on this category: learners pay for instruction that no longer matches reality, blame themselves or the instructor, and trust the platform less. Segment-level detection makes maintenance affordable, domain-aware external monitoring catches decay before learners do, and a decay-adjusted ranking is the one change that would align a marketplace's incentives with its learners' interests.
