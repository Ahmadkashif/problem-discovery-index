# Millions of Administrations Never Test the Norms They Are Scored Against

**Niche:** [[niches/corporate-training/talent-assessment-publishers/profile|Talent Assessment Publishers]]
**Industry:** [[industries/corporate-training|Corporate Training]]
**Type:** Fix (Pain Point)
**One-liner:** Candidates are scored against norm groups collected years ago from populations that may no longer resemble who is applying, and the platform processing millions of administrations never checks.
**Tags:** #change-point-detection #hypothesis-testing #confidence-intervals #probability-distributions #bayesian-inference #evaluation-metrics #descriptive-statistics #causal-inference #compliance #data-integration

## The Problem
A score means something only relative to a norm group — this candidate is at the seventieth percentile of a defined comparison population. Those norms were collected at a point in time from a population assembled under assumptions about who applies for these roles. Applicant populations shift: geographies open, remote hiring changes who applies, sourcing channels change the mix, and the underlying distribution of a construct can itself move. The publisher's platform processes millions of administrations continuously and is therefore observing all of it, and does not compare what it sees to the norms it is scoring against. A norm group that has drifted produces systematically distorted percentiles, and in a selection context that means candidates being rejected or advanced on a comparison that no longer holds.

## Why It's Still Broken
Operational scoring and psychometric research sit in different parts of the organization with different systems and governance. Live administration data is client data under commercial agreements, and whether it may be analyzed in aggregate is usually unaddressed rather than prohibited — producing the safest possible default. There is also a real methodological objection: applicants are a self-selected population, not a probability sample, so a raw comparison of applicant scores to norm groups confounds true drift with changes in who is applying. Because the naive analysis is invalid and the valid one requires modelling composition, the question has stayed open.

## What a Fix Looks Like
Standing norm surveillance on aggregate, de-identified administration data with composition modelled rather than ignored. The comparison is not applicant mean against norm mean; it is a modelled estimate of what the norm population's distribution would look like given today's observable composition, checked against the subsets where composition is most stable. That separates a shift in who is applying from a shift in how the population scores, which is the entire difficulty. Surveillance runs continuously across instruments and norm groups, alerting on sustained divergence, and feeds a re-norming prioritization ranked by measured decay rather than by publication schedule. The same infrastructure answers the questions regulators and litigants increasingly ask: whether norms hold equivalently across subgroups and geographies, and where observed subgroup differences diverge from what the norming sample predicted.

## Who Feels the Pain
Candidates evaluated against comparisons that may no longer hold; client organizations making selection decisions on percentiles of uncertain meaning; the psychometric staff accountable for norm currency with no instrument to measure it; and the publisher, whose defence in an employment challenge rests on norms it has not verified.

## Impact If Fixed
Moves re-norming from a calendar decision to an evidence-based one, redirecting the largest recurring research expenditure toward the instruments that need it. More importantly, in a domain where assessments are challenged in litigation and increasingly scrutinized by regulators, continuous validity and fairness monitoring drawn from the operating base is a far stronger defence than a norming study from the last decade.
