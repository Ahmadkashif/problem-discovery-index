# Millions of Administrations Are Scored and Never Analyzed

**Niche:** [[niches/behavioral-health-clinics/psychological-assessment-publishers/profile|Psychological Assessment Publishers]]
**Industry:** [[industries/behavioral-health-clinics|Behavioral Health Clinics]]
**Type:** Fix (Pain Point)
**One-liner:** Digital platforms score millions of administrations a year against norms collected a decade ago, and the publisher never compares the two — so norm obsolescence is discovered by outside researchers rather than by the people responsible for it.
**Tags:** #change-point-detection #time-series-forecasting #hypothesis-testing #confidence-intervals #probability-distributions #bayesian-inference #evaluation-metrics #descriptive-statistics #compliance #data-integration

## The Problem
Norms describe a population at a moment. Populations move — the documented generational drift in cognitive test scores is the best known case, and comparable shifts occur on symptom and behaviour scales as diagnostic thresholds, reporting norms, and referral patterns change. A publisher whose scoring platform processes administrations continuously is observing that movement in real time and is not looking. Restandardization is scheduled on a fixed cycle chosen by publication economics rather than triggered by evidence that the norms have decayed, so an instrument may spend years scoring against tables that have measurably drifted. When drift is eventually identified it is typically identified in the academic literature, which is the worst possible route for the publisher: the finding arrives as a criticism rather than as a product decision.

## Why It's Still Broken
Operational scoring and psychometric research sit in different parts of the organization with different systems and different governance. Scoring data is customer data under clinical confidentiality, and the terms under which it might be analyzed in aggregate are usually unaddressed rather than prohibited, which produces the safest possible default of not touching it. There is also a genuine methodological objection with force: administrations in the field are not a probability sample of any population, so a raw comparison of field scores to standardization norms confounds true drift with referral and setting composition. Because the naive analysis is invalid, and the valid one requires modelling composition, the question has stayed open.

## What a Fix Looks Like
A drift surveillance function built on aggregate, de-identified scoring data with composition explicitly modelled rather than ignored. The comparison is not field mean against norm mean; it is a modelled estimate of what the standardization population's score distribution would look like today, given observable composition covariates, checked against the anchor subsets where composition is most stable. That is enough to distinguish a shift in who is being tested from a shift in how the population scores, which is the whole difficulty. Surveillance runs continuously against every instrument, with alerting on sustained divergence rather than on noise, and feeds a restandardization prioritization that ranks instruments by measured decay instead of by publication schedule. The same infrastructure answers questions the publisher currently cannot: whether norms hold equivalently across settings and populations, and where subgroup differences in the field diverge from what the standardization sample predicted — which is the substance of most fairness criticism directed at these instruments.

## Who Feels the Pain
Clinicians making diagnostic and placement decisions against tables that may have aged; the psychometric staff accountable for norm currency with no instrument to measure it; the publisher's reputation when drift is announced by an outside researcher; and the patients and students on whom those decisions land.

## Impact If Fixed
Moves restandardization from a calendar decision to an evidence-based one, which redirects the largest recurring research expenditure in the business toward the instruments that actually need it. It also converts the field data from an unused by-product into the strongest ongoing validity evidence the publisher can hold — and validity evidence is the entire basis on which these products are defended, in clinics and in court.
