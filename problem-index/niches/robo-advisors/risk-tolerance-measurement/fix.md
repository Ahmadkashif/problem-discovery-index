# Six Questions, No Validation

**Niche:** [[niches/robo-advisors/risk-tolerance-measurement/profile|Risk Tolerance Measurement]]
**Industry:** [[industries/robo-advisors|Robo-Advisors]]
**Type:** Fix (Pain Point)
**One-liner:** Nobody at the platform can say whether the questionnaire predicts anything, and it sets every client's allocation.
**Tags:** #hypothesis-testing #descriptive-statistics #evaluation-metrics #quick-win #confidence-intervals #compliance #cross-validation #automation
**Contested on:** Every serious competitor in this niche is fighting to predict how a client will actually behave in the next drawdown from the behaviour the platform already observes — and whoever predicts it best replaces the questionnaire as the input that sets the allocation.

## The Problem
The six questions were written by a product team years ago, reviewed by compliance, and shipped. They ask how a client would feel about a hypothetical decline, how long until they need the money, and how they would describe their investing experience. Nobody has ever checked whether the answers relate to what clients subsequently did. The output of those six items is the primary determinant of every client's asset allocation.

## Why It's Still Broken
The instrument satisfied its compliance purpose on the day it shipped, so no validation was required and none was scheduled — and a question nobody is obliged to ask tends not to get asked. Validation requires joining onboarding records to behavioural data across teams. A weak result would be uncomfortable to hold. And changing the questions means re-papering suitability.

## What a Fix Looks Like
Run the analysis and report it. Join the stated tolerance to observed drawdown behaviour and measure the association, which is the fix and is a day's work on data the platform already holds. Report it item by item, since some questions almost certainly carry the signal and others almost certainly carry none. Drop or replace the items that predict nothing, because a shorter instrument that works is better in every respect. Check for differential behaviour across client segments, as an item that works for one population and not another is a real problem. Test retest stability where clients have answered more than once, which reveals whether the construct is stable at all. Compare against a behavioural benchmark, since the question is not whether the instrument is perfect but whether it beats what the platform could infer for free. Document the validation, which is a supervision strength rather than an exposure. Re-run after each market event, because each one supplies new criterion data. Publish the summary, as being the first platform to validate its instrument is a credible position. And set a review cycle, so the instrument stops being a decade-old artefact.

## Who Feels the Pain
Clients allocated by an unvalidated instrument; investment teams defending allocations built on it; supervisors accepting it as suitability evidence; and platforms that cannot answer the most basic question about their own input.

## Impact If Fixed
No validation was required on the day it shipped, so none was ever scheduled. Joining stated tolerance to observed behaviour is a day's analysis and either confirms the instrument or ends a decade of allocating on noise.
