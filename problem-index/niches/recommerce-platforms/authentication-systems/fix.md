# The False Reject Nobody Counts

**Niche:** [[niches/recommerce-platforms/authentication-systems/profile|Authentication Systems]]
**Industry:** [[industries/recommerce-platforms|Recommerce Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A genuine item rejected as counterfeit leaves the building with its owner, generates no record anybody analyses, and so the error rate the platform reports is the rate in one direction only.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #descriptive-statistics #compliance #worker-facing #quick-win #probability-distributions
**Contested on:** Every serious competitor in this sub-niche is fighting to distinguish genuine from counterfeit against opponents who study exactly what is being checked — and whoever does that holds the category, because a single publicised false accept destroys the trust the whole platform rests on.

## The Problem
A seller sends in a genuine bag. It has an unusual production variation, or wear that obscures a check, or came from a factory run the reference data does not cover. It is rejected, returned, and the seller is told it did not pass authentication — an accusation, effectively, with no appeal that goes anywhere. They tell people. The platform records a rejection and moves on. Its published accuracy refers to items it accepted; the rejections are not verified by anybody, so the false reject rate is not merely unmeasured but unmeasurable in the current process, and the authenticator's incentive under an asymmetric penalty structure is to reject when unsure.

## Why It's Still Broken
A false accept produces a loud, expensive, traceable event and a false reject produces a quiet, unrecorded one, so the incentives and the measurement both point one way. Verifying a rejection requires effort on an item the platform has decided not to sell. Sellers who are wrongly rejected mostly do not pursue it, and those who do are handled individually. And an authenticator penalised only for accepts will rationally reject in doubt, which is the behaviour the structure produces rather than an individual failing.

## What a Fix Looks Like
Measure the direction nobody measures. Send a sample of rejected items for independent verification, which is the only way to estimate the false reject rate and which costs a small amount against a rate nobody currently knows — this is the fix and the number it produces is likely to surprise. Give sellers a real appeal route with a second, independent examination, since the current process offers an accusation with no recourse. Record the reason for every rejection in structured form, so patterns — a production variation the reference data lacks, a particular check causing rejections — become visible. Report both error rates with confidence intervals and manage the trade-off explicitly, since the platform is currently choosing a point on that trade-off without knowing where it is. Balance the authenticator's incentives, because penalising one direction only produces exactly the behaviour observed. Feed verified false rejects back into the reference data, since each one identifies a genuine variation the references did not cover. Treat the rejected seller as a customer rather than as a suspect in the communication, which costs nothing and is the difference between a disappointment and a public complaint. And publish the two-sided error rate, since a platform that can state both is making a stronger claim than one that states one.

## Who Feels the Pain
Sellers accused of offering counterfeits they did not; authenticators penalised in one direction and rejecting accordingly; and platforms whose stated accuracy describes half the errors.

## Impact If Fixed
The reported error rate covers one direction because rejected items leave unverified, and the incentive structure produces exactly the resulting bias. Independent verification of a rejection sample is the only way to estimate the other half, and every verified false reject is a reference-data gap identified.
