# Member Lapse Prediction and Intervention

**Industry:** [[fitness-wellness-software|Fitness & Wellness Software]]
**Type:** High Impact
**One-liner:** Attendance decay predicts cancellation weeks in advance with unusual reliability, and the platform holds every check-in — so the studio can intervene while the member is still recoverable rather than after they call.
**Tags:** #survival-analysis #gradient-boosting #logistic-regression #change-point-detection #feature-engineering #confidence-intervals #evaluation-metrics #causal-inference #revenue-impact

## The Problem
A fitness business lives on retention. Acquiring a member is expensive — paid advertising, introductory offers, staff time on tours and trials — and the payback period runs months. A member who cancels in month three has cost the business money. A member who stays two years is the entire profit model.

Cancellation is almost never sudden. It is preceded by weeks of declining attendance: from four visits a week to two, to one, to none, and then eventually a call or a cancelled card. By the time the member cancels they have not attended in a month and have already reorganised their week around not going. The decision was made much earlier, quietly, and the studio's opportunity to change it passed unnoticed.

The check-in record shows all of it. Every visit, timestamped, per member, alongside which class, which instructor, which time slot, and whether they came with anyone. It is one of the cleanest behavioural signals available in any consumer subscription business — an unambiguous record of whether the customer did the thing they are paying for.

Studios use it to print class rosters. Where retention analytics exist they are descriptive: a churn rate, a cohort chart, a list of members who have not attended in thirty days — which is a list of people who have already gone.

## Why It's Unsolved
The vendors' revenue model points elsewhere. Most of these platforms make their money on payment processing, so their product attention has gone to billing, marketplace demand and consumer app experience. Retention analytics do not obviously increase processing volume in the short term, and the connection between them is slow and hard to attribute.

Studio operators are also not analytical buyers. The person running an independent studio is usually a former instructor, working in the business, without the time or inclination to interpret a model output. Anything that requires interpretation will not be used, which means the product has to be an action rather than a score — and that is a harder thing to build and a riskier thing to ship.

The intervention side is genuinely uncertain, and this is the honest gap. Nobody knows what actually works. Does a text from the owner recover a lapsing member? A free session with a different instructor? A schedule suggestion? An offer? Studios try things inconsistently and measure nothing, so there is no evidence base — and building one requires deliberate experimentation that no single studio can run at meaningful scale.

## What a Solution Looks Like
A lapse risk score per member, updated continuously from attendance, framed as a hazard rather than a threshold — the useful statement is that this member's attendance pattern has changed in a way that historically precedes cancellation, not that they have missed thirty days.

The features that matter are behavioural and available: the trend in visit frequency, a break in a habitual slot, the departure of an instructor they consistently attended, a change in the mix of classes taken, whether they attend alone or with someone, and how their pattern compares to their own history rather than to an average.

It has to arrive as a task, not a dashboard. A short daily list of members worth contacting, with the reason — this member has attended the same Tuesday class for a year and has missed three weeks — because that specific fact is what lets a front desk person have a real conversation.

And the intervention should be measured. With hundreds of thousands of studios, the platform can run genuine experiments on what recovers a lapsing member, which no individual operator can do, and which is the only route to knowing whether any of this works.

## Impact If Solved
Retention is the whole business model in fitness, and the sector's churn rates are notoriously high. Moving intervention from after the cancellation call to weeks before it is the largest available improvement to studio economics, and the signal it rests on is already being collected at the door.
