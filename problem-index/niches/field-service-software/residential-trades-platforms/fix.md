# The Callback Nobody Attributes

**Niche:** [[niches/field-service-software/residential-trades-platforms/profile|Residential Trades Platforms]]
**Industry:** [[industries/field-service-software|Field Service Software]]
**Type:** Fix (Pain Point)
**One-liner:** First-time fix rate is the number the entire residential service industry runs on, and most contractors cannot compute it, because a return visit is booked as a new job and nothing links it to the one that failed.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #k-nearest-neighbors #automation #quick-win #revenue-impact
**Contested on:** Every serious competitor in residential trades software is fighting to predict what the job actually is before the truck leaves, and to match the technician and the parts to it — and whoever moves first-time fix rate most takes the account.

## The Problem
A technician visits, replaces a part, and leaves. Eight days later the customer calls again about the same unit. The call is booked as a new job, possibly by a different call taker, possibly under a different job type, and the system treats it as fresh demand. Unless someone notices, the contractor's records show two jobs and one satisfied customer. First-time fix rate, warranty cost, technician performance and the effectiveness of every operational change all depend on knowing that the second visit was a consequence of the first, and the link is made by human recollection or not at all.

## Why It's Still Broken
Linking requires a definition — what counts as a callback, over what window, for which equipment — and definitions are contentious because callback rate is used to evaluate technicians. So the field exists in most systems, is optional, and is filled in inconsistently by the people whose numbers it affects. Vendors have not imposed a definition because their customers have not agreed on one, and the result is that the industry's most important operating metric is self-reported by the party being measured.

## What a Fix Looks Like
Detect the link rather than asking for it. A second visit to the same property, on the same equipment, within a window, for a related symptom, is identifiable from data the system already holds, and the match can be made with a confidence rather than a judgement. Publish the definition explicitly and let the contractor set the window, so the number means something specific and is comparable over time. Separate the categories that behave differently: a genuine misdiagnosis, a part that failed, a job the customer declined to complete, and a different problem on the same unit are four different things with four different responses, and lumping them is why callback conversations go badly. Report by technician with volume-appropriate uncertainty, because a technician with fourteen jobs this month does not have a meaningful callback rate and treating a small sample as a performance signal is both statistically wrong and corrosive.

## Who Feels the Pain
Owners managing to a number they cannot compute; technicians blamed or credited on the basis of whoever remembered to tick a box; and customers whose second call is treated as a new inquiry.

## Impact If Fixed
Automatic callback detection gives the industry's central metric an actual measurement, which makes every subsequent improvement evaluable — including the diagnosis prediction that the build note describes, which cannot be assessed without it. Separating callback causes typically shows that a large share are not misdiagnosis at all, which changes both the operational response and the conversation with technicians.
