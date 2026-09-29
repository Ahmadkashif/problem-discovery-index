# Breed Analysts Know Which Herds to Distrust and Fix It by Hand

**Niche:** [[niches/livestock-operations/livestock-genetic-evaluation/profile|Livestock Genetic Evaluation Programmes]]
**Industry:** [[industries/livestock-operations|Livestock Operations]]
**Type:** Fix (Pain Point)
**One-liner:** The staff who run the evaluation know exactly which member herds submit unreliable data, and that knowledge exists in three people.
**Tags:** #tacit-knowledge-ml #anomaly-detection #data-integration #worker-facing #automation

## The Problem
An analyst who has run breed evaluations for fifteen years knows things no edit rule captures. That this herd's weaning weights have been implausible since a change of management. That this operation splits contemporary groups strategically before every bull sale. That this herd's calving ease scores are recorded by someone who scores everything a point high. That a particular consultant advises members to report selectively, and his clients' data looks a certain way.

They handle it — adjusting contemporary group assignments, excluding records, flagging herds for follow-up. The evaluation improves. The reasoning is recorded nowhere.

So the same herds are re-diagnosed every cycle, new analysts rebuild the picture over years, and when the person who has run the evaluation for two decades retires, the association loses its most effective quality control with no replacement mechanism.

## Why It's Still Broken
The evaluation system stores records and results. There is no object representing a judgment about a herd, so an analyst's assessment can only be applied as an edit, and the edit carries no reason.

Member relations make it delicate. Breed associations are member-owned, and a written record saying a member's data is unreliable is uncomfortable in a way that keeps the assessment verbal — which also makes it unaccumulable and unauditable.

And it works, for now. Three experienced people can hold the picture for a breed, so the problem is invisible until they leave.

## What a Fix Looks Like
Make herd-level assessment a first-class, internal, dated record.

**Herd quality profiles.** Structured, versioned assessments of each herd's reporting reliability by trait, with evidence and dates. Held internally as evaluation quality material, which is what it is.

**Typed adjustment reasons.** Every contemporary group change and record exclusion carries a coded reason and a note. Over a cycle this becomes the dataset of what actually goes wrong with member submissions.

**Automate what the analysts do by pattern.** Group splitting, scorer drift, and post-management-change discontinuities are all detectable statistically once someone has described what to look for — and the analysts can describe it precisely if asked.

**Test the assessments.** With adjustments recorded, the association can check whether herds flagged as unreliable actually produced records that later looked wrong. Some judgments will hold and become rules; others will not, which is equally worth knowing.

**Surface at review.** An analyst reviewing a submission should see what the association already knows about that herd. That is the payoff and what makes recording worth the seconds.

## Who Feels the Pain
Evaluation analysts, re-diagnosing the same herds every cycle. New analysts, learning a breed's membership over years. The association, whose evaluation quality is a small number of tenures. And every producer buying genetics on a prediction whose reliability depends on who happened to review the submissions.

## Impact If Fixed
The evaluation is the only rigorous quantitative product this industry transacts on, and its quality control is undocumented expertise in a handful of people approaching retirement. Capturing it makes the control transmissible, converts pattern recognition into rules the system can apply at scale, and protects a data asset built over a century that no competitor could rebuild.
