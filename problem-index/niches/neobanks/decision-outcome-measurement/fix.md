# The Reinstatement That Is Not Recorded as an Error

**Niche:** [[niches/neobanks/decision-outcome-measurement/profile|Decision Outcome Measurement]]
**Industry:** [[industries/neobanks|Neobanks]]
**Type:** Fix (Pain Point)
**One-liner:** An account is frozen, reviewed, found legitimate and restored, and nothing in any system records that the model that froze it was wrong.
**Tags:** #evaluation-metrics #data-integration #confidence-intervals #compliance #quick-win #descriptive-statistics #automation #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to join several million decisions a year to the outcomes already sitting in the ledger — and whoever assembles that dataset has the only thing that makes every other decision in the institution improvable.

## The Problem
The reinstatement is the cleanest label the institution ever generates. A model decided this account was risky, a human examined the evidence and concluded it was not, and the account was restored. That is a confirmed false positive, adjudicated by the institution's own staff, with a full evidence trail. It is recorded in a case management system as a case closed with a resolution code, and it never reaches the model, the vendor or anyone measuring performance. Thousands of these are generated every month and every one of them is discarded.

## Why It's Still Broken
A reinstatement is processed as a customer service resolution rather than as a model error, so it is filed where resolutions are filed — the classification of the event determines where it goes, and nobody classified it as evidence. The model lives in a vendor system with no path back. Nobody has asked how many there are. And a false positive rate that has never been computed cannot become a target.

## What a Fix Looks Like
Treat the reinstatement as the label it is. Record every reinstatement against the decision that caused it, which is the fix, is a single reference field, and creates the institution's most valuable evidence stream out of something already being generated. Capture the analyst's reason in structured form, since why it was wrong is more useful than that it was wrong and the analyst already knows it. Report false positive rate by model, rule and segment, which is derivable the moment the join exists and which most institutions have never seen. Feed the confirmed cases back to the vendor as evaluation evidence, which is a contractual matter and is the only way the vendor's model improves on this population. Distinguish reinstated-and-fine from reinstated-and-later-fraudulent, since a small number of reinstatements are wrong in the other direction and that is important information about the review process. Use the cases as training data where the institution models internally. Count the cost per false positive including the support contacts, the churn and the complaint, which is what makes the number actionable at leadership level. Apply the same treatment to declined-then-approved applicants and to released holds, since the same discarded-label pattern runs through every decision type. Report the trend, since a rising false positive rate is the signal that a threshold or a population has moved. And set a target on it, because a rate that is measured and reported will be managed and one that is not will keep drifting upward.

## Who Feels the Pain
Customers frozen by models that never learn they were wrong; risk teams unable to demonstrate improvement; and institutions generating their best evidence and filing it as a closed ticket.

## Impact If Fixed
A reinstatement is classified as a customer service resolution rather than as evidence, and that classification decides where it goes. One reference field linking it to the decision creates the institution's most valuable evidence stream from something already being produced thousands of times a month.
