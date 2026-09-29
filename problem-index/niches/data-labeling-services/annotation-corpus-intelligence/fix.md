# Nobody Knows Whether the Third Annotator Was Worth It

**Niche:** [[niches/data-labeling-services/annotation-corpus-intelligence/profile|Annotation Corpus Intelligence]]
**Industry:** [[industries/data-labeling-services|Data Labeling Services]]
**Type:** Fix (Pain Point)
**One-liner:** Projects specify three annotators per item because three is the convention, and the data to establish whether the third one changed any outcome is in every project's database.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #monte-carlo-methods #quick-win #revenue-impact #bayesian-inference
**Contested on:** Every serious competitor that gets here is fighting to turn millions of annotation events with their outcomes into answers about who is reliable, what agreement is achievable and whether the data helped — and whoever does that holds the empirical basis for questions the whole field guesses at.

## The Problem
A contract specifies three annotators per item, which increases the cost by roughly two hundred percent over a single pass and is agreed without discussion because three is what everybody does. In practice the third annotator changes the aggregated outcome on a small minority of items — the ones where the first two disagreed — and on the rest is pure cost. Whether three is right, whether two with targeted escalation would be equivalent, and whether five is needed on the hardest items are all answerable from the data every completed project already contains, by simply recomputing the outcome with fewer annotators and comparing.

## Why It's Still Broken
The convention predates the current task mix and has never been revisited. The analysis is a retrospective simulation over completed projects — drop the third annotator's judgement and see what changes — which is straightforward and has not occurred to anybody as a thing to do. The vendor bills for the third annotator, which removes the incentive to establish they are unnecessary. And the customer specifying three has no basis for a different number either.

## What a Fix Looks Like
Simulate the alternative over completed projects. Recompute the aggregated outcome using one, two and three annotators over historical data and report how often the answer changes, which is a direct retrospective simulation requiring no new work and immediately establishes the marginal value of each additional pass. Do it per task type, since the answer differs enormously between a straightforward categorisation and an ambiguous expert judgement, and the single convention is certainly wrong for one of them. Model the adaptive alternative: two annotators with a third only where they disagree, which is the obvious policy and is cheaper than three everywhere while producing the same outcome on the items where the first two agreed — the saving is substantial and the equivalence is checkable. Extend to the hard tail, since some items may warrant five and the current uniform policy under-serves exactly the items that matter. Present the cost-quality frontier to the customer, so the number of passes becomes a decision with evidence rather than a convention. And report the marginal contribution honestly, including where it shows that the vendor has been billing for passes that changed nothing.

## Who Feels the Pain
Customers paying for redundancy that changes nothing on most items; the hardest items receiving the same treatment as the easiest; and an industry whose central cost parameter is set by convention.

## Impact If Fixed
The retrospective simulation requires no new work and directly establishes the marginal value of each annotation pass, per task type. The adaptive two-plus-escalation policy is both cheaper and demonstrably equivalent on the items where the first two agree, which is most of them.
