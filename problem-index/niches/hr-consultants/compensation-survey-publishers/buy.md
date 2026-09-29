# Survey Data Quality Against a Contributor You Cannot Annoy

**Niche:** [[niches/hr-consultants/compensation-survey-publishers/profile|Compensation Survey Publishers]]
**Industry:** [[industries/hr-consultants|HR Consultants]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Bad submissions must be caught, and the person who sent them is a voluntary contributor whose participation is the whole business.
**Tags:** #anomaly-detection #data-integration #workflow-orchestration #evaluation-metrics #automation

## The Problem
Thousands of employers submit pay data each cycle, in their own formats, from their own systems, under their own definitions. Base salary that includes allowances. Bonus reported as target where the benchmark wants actual. Full-time equivalents counted differently. Currency and pay frequency confusions. A department's data submitted twice.

Every one of these distorts a percentile that customers will set salary ranges against, and increasingly post publicly under transparency law. Survey operations staff catch what they can inside a compressed submission window, using range checks and experience.

The complication is that the submitter is a volunteer. Participation is reciprocal — contribute data, receive the survey — and the network is the moat. Chasing a contributor with queries about their submission is a cost to the relationship, so operations is systematically reluctant to query, which means questionable data gets accepted more often than anyone would like.

## What Already Exists
Data quality platforms — Great Expectations, Monte Carlo, Soda, and the enterprise suites — do schema validation, distributional checks, anomaly detection, and stewardship queues competently, and are widely deployed.

## The Customization Gap
Every generic platform assumes a source you control. This one assumes a source you must not irritate.

**Query budget as a first-class constraint.** The system should decide not just what is anomalous but whether it is worth asking about, weighing the submission's influence on published results against the relationship cost. A contributor supplying ten incumbents in a thick benchmark can be left alone; the same anomaly in a thin cut cannot. No off-the-shelf tool models the cost of asking.

**Validate against the contributor's own history.** The strongest signal is not a population range but this employer's own prior submissions. A company whose engineering pay jumps 22% year over year either restructured or made a definitional error, and only their own series reveals which.

**Cross-participant coherence.** Because many employers submit for the same benchmarks in the same markets, an individual submission can be checked against the cohort — while respecting the aggregation and disclosure rules that govern what may be compared. That constraint is part of the specification, not a filter applied afterwards.

**Definitional error detection, not just outliers.** The common failures are not extreme values; they are correct-looking numbers under the wrong definition. Bonus reported as target rather than actual sits comfortably inside every range and is detectable by its relationship to base and to the contributor's history.

**Influence-weighted triage.** Fixing one record in a benchmark with four hundred incumbents changes nothing. In one with nine, it changes the published number. Prioritization should follow effect on output, which is a computation about the published result rather than about the record.

## Target Customer
Head of survey operations at a compensation data business, running a fixed team against a submission window that does not move and a contributor base that grows every year.

## Impact If Solved
Published percentiles get more accurate exactly where they are thinnest and most consequential. Operations spends its limited contributor goodwill on the queries that actually change the output. And under pay transparency, where an employer will post and defend a range built on these numbers, the accuracy of thin cuts stops being an internal quality matter and becomes the product's core claim.
