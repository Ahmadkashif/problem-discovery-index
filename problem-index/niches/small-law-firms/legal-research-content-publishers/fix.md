# The Citator Says a Case Is Questioned and Nobody Measures Whether It Should Have

**Niche:** [[niches/small-law-firms/legal-research-content-publishers/profile|Legal Research & Practice Content Publishers]]
**Industry:** [[industries/small-law-firms|Small Law Firms]]
**Type:** Fix (Pain Point)
**One-liner:** A flag on a case tells an attorney whether they may rely on it, the flag is a human judgment call, and no two analysts are ever compared.
**Tags:** #evaluation-metrics #hypothesis-testing #tacit-knowledge-ml #compliance #worker-facing

## The Problem
The citator is the most consequential product in legal publishing. An attorney checks whether an authority is still good before relying on it, and a flag saying a case has been questioned, criticised or overruled determines whether it goes into a brief. Failing to check, or checking and getting a wrong answer, is malpractice territory.

Behind each flag is a person. An analyst reads a citing reference and decides how it treated the cited case: followed, distinguished, criticised, limited, overruled in part. Many of these are clear. A large number are not — courts disagree with cases obliquely, distinguish them in ways that functionally gut them, or criticise a proposition without addressing the holding. The judgment is genuinely difficult and it is made by one analyst.

That judgment is recorded as a code. What the analyst saw in the opinion, why they read a passage as criticism rather than distinction, what they considered and rejected — none of it is captured. The flag is the whole artefact.

Three consequences follow. Consistency is unmeasured: two analysts handling comparable treatments may flag differently, and nothing surfaces it because there is no record of the basis. Defensibility is weak: when a customer disputes a flag, the answer must be reconstructed by re-reading. And there is no training data — the corpus of reasoning that would let any of this be automated or checked does not exist, only its conclusions.

The same gap runs through headnoting and classification, where an editor decides which propositions in an opinion are worth stating and where each belongs in the taxonomy.

## Why It's Still Broken
Production is measured in throughput. The queue of citing references is enormous and never empties, and time spent recording reasoning is time not spent clearing it.

The schema has no place for it. Downstream systems consume a flag; nothing in the pipeline needs an explanation, so nothing collects one.

And there is caution about creating a record of internal deliberation in a product whose accuracy attracts professional liability. A file showing analysts debating whether a case was overruled is a document nobody wanted to create. That instinct also prevents the publisher demonstrating that its process is rigorous and consistent, which is its own exposure.

## What a Fix Looks Like
**Capture the basis at the moment of the call.** The passage relied on, the treatment assigned, the alternative considered, and a one-line reason. Attached to the existing workflow, this costs a minute on the hard cases and nothing on the easy ones.

**Measure inter-analyst agreement, deliberately.** Route a sample of citing references to several analysts and compare. It is uncomfortable, it is the only way to know whether the house standard is a standard, and it produces the calibration set any automated treatment classifier will need.

**Make prior decisions retrievable by pattern.** Analysts reason by analogy to treatments they have seen before. A retrieval layer over past decisions keyed by treatment pattern rather than by case name is useful from day one, which is what determines whether people use it.

**Feed it upward.** The reasoning record is the supervision for automated treatment classification — the highest-value automation available in this business and the one nobody can attempt without labelled examples of how ambiguous treatments are resolved.

**Publish the process, not the deliberation.** Settle with counsel what is retained and in what form, then use the consistency measurement externally as a quality claim. A publisher that can state its inter-analyst agreement rate has an argument no competitor can answer, at a moment when generative alternatives are competing on exactly this ground.

## Who Feels the Pain
Attorneys at small firms relying on a flag whose basis they cannot see and whose consistency nobody has measured; the analysts, whose expertise is recorded as a single code; and the publisher, whose most defensible asset against generative competition is a body of judgment it has never demonstrated the reliability of.

## Impact If Fixed
The citator's authority is the publisher's deepest moat, and it currently rests on reputation rather than on measurement. Recording the reasoning makes consistency provable, makes disputes answerable, and creates the labelled corpus without which the editorial layer cannot be extended, automated, or defended.
