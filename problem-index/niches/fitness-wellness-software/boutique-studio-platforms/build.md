# Churn Prediction From Attendance Decay, With an Intervention Attached

**Niche:** [[niches/fitness-wellness-software/boutique-studio-platforms/profile|Boutique Studio Platforms]]
**Industry:** [[industries/fitness-wellness-software|Fitness & Wellness Software]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Attendance decay predicts cancellation weeks ahead with unusual reliability, every check-in is recorded, and the studio finds out when the member calls.
**Tags:** #survival-analysis #gradient-boosting #change-point-detection #confidence-intervals #evaluation-metrics #logistic-regression #revenue-impact #cross-validation
**Contested on:** Every serious competitor in studio software is fighting to identify a member who is going to cancel while they are still recoverable and put the studio in front of them — and whoever intervenes earliest and most effectively takes the account.

## The Problem
A member joined in January, came four times a week through February, three times in March, and has been twice in the last three weeks. In six weeks she will cancel, and by then the reason will have hardened into a decision. Right now she is recoverable by almost anything — a message from the instructor she likes, a class time that fits her changed schedule, a conversation about why she stopped coming to the 6am. The studio owner, managing two hundred members and teaching four classes a day, has no idea this is happening. The platform knows exactly.

## Why Nobody Has Built This
The platforms' revenue is payment processing on the membership, which means a lapsing member who keeps paying is not, in the short term, a revenue problem for the vendor — an uncomfortable observation and one that helps explain fifteen years of unbuilt retention capability. Beyond that, prediction without prescription is worse than useless to a studio owner with no time: a list of at-risk members is another task, and the products that have gestured at this have delivered exactly that list. And measuring whether an intervention worked requires running it as an experiment, which nobody has set up.

## What to Build
A member-level risk estimate with a prescribed action and a measured outcome. Risk comes from attendance trajectory relative to that member's own established pattern rather than to an absolute threshold — a member who always came twice a week and still does is not at risk, and a member who came five times and now comes twice is, which a simple rule gets backwards. Class preferences, instructor affinity, booking-to-attendance ratio, social connections within the studio and tenure all contribute. The prescription is specific and small: which member, what the likely cause appears to be, and one action — an instructor message, a class recommendation that fits their changed pattern, a schedule conversation. Interventions are assigned as a short daily list rather than a report, because that is what a studio owner will actually do. Effectiveness is measured against a holdout so the studio learns what works rather than assuming, which is also the only honest way to report the product's value.

## Target Customer
Studio platforms with large member bases, and directly the multi-location boutique operators for whom a point of monthly churn is a large annual number.

## Impact If Built
Retention is the entire economic model of boutique fitness, and the signal is among the cleanest available in any consumer business. Intervening weeks before a cancellation, when the member is still recoverable, is worth more than any acquisition improvement the studio could make — acquisition cost in this sector is high enough that a retained member is worth several prospects.
