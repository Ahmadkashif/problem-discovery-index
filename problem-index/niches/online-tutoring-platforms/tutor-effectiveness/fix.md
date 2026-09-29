# Fix: Rebooking Is Standing In for Learning

**Niche:** [[niches/online-tutoring-platforms/tutor-effectiveness/profile|Tutor Effectiveness & Learning Measurement]]
**Industry:** [[industries/online-tutoring-platforms|Online Tutoring Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Every ranking, tier and match on the platform runs on rebooking rate, and nobody has checked whether rebooking has anything to do with learning.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #causal-inference #compliance #quick-win #worker-facing
**Contested on:** Whether the platform will test its own central proxy against any outcome at all.

## The Problem

Rebooking rate is the platform's quality metric. It determines ranking, tier assignment, whether a tutor is surfaced, and in aggregate what they earn. It is treated, throughout the organisation, as meaning that the tutoring was good.

Nobody has established that. The correlation between rebooking and learning has not been measured at any platform in this industry, on any sample, that anyone has published. It is plausible that it is positive and weak; it is entirely possible that beyond a threshold it is flat or negative, since the tutor who makes a student work hard is less pleasant to book again than the one who makes the homework go away.

The platform is therefore running its entire quality apparatus on an untested proxy, and has been for years.

## Why It's Still Broken

Rebooking is available, immediate, unambiguous and aligned with revenue. Any alternative is delayed, partial, contested and might reduce revenue. That asymmetry has been sufficient.

Testing the proxy also has an obvious risk: if the test shows rebooking is a poor proxy for learning, the platform then knows — in writing — that its rankings do not measure what it implies they measure, while it continues to charge families for a service on that basis. Not testing is the safer position for anyone whose job is attached to the metric.

And there is a smaller structural reason: the outcome data needed for even a modest test lives outside the platform, and nobody owns the relationship that would obtain it.

## What a Fix Looks Like

Test the proxy on whatever sample you can get. This is a study, not a platform.

Find the outcome data that already exists. District-contracted tutoring usually has assessment data under contract. Some families will share report cards or test scores in exchange for something modest. Platform-administered diagnostics, where they exist, give pre-and-post on the platform's own instrument. A sample of a few thousand student-tutor pairs with any outcome measure is enough to answer the question directionally.

Then run the comparison. Does a tutor's rebooking rate predict their students' measured gains, controlling for starting level, subject and session count. Report the correlation with an interval. That single number — currently unknown to the entire industry — reframes everything the platform does with the metric.

Look at the shape, not just the coefficient. The interesting possibility is non-monotonicity: rebooking may predict learning at the low end (bad tutors do not get rebooked) and stop predicting or reverse at the high end. If so, the ranker's behaviour at the top of the distribution is exactly wrong, and that is actionable immediately.

Test the cheaper in-session proxies against the same outcomes. Student talk ratio and question-before-explanation are computable from recordings, and if either predicts gains better than rebooking does — which the teaching literature suggests is likely — the platform has a better signal available at low cost today.

And publish what you find, at least internally, with the intervals. The finding may be uncomfortable and it converts an assumption the whole business rests on into a measured quantity.

## Who Feels the Pain

Effective tutors, whose income depends on a metric that may not reward them, and who know from experience that being demanding costs them ratings. Families, who choose from a ranking that promises quality and measures satisfaction. Students, who get the tutor the proxy selected. And the platform, whose entire quality apparatus rests on an untested assumption it has never had reason to examine.

## Impact If Fixed

The industry's central metric gets tested for the first time. If it holds up, everything is better-founded than it was. If it does not — which is the more likely outcome above the low end — the platform learns that its rankings are pointed at the wrong target while there is still a cheap in-session alternative available, and can change course before someone else measures it for them.
