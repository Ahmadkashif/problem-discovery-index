# Matching a Person to a Court Record Across Three Thousand Counties

**Niche:** [[niches/property-management/tenant-screening-data/profile|Tenant Screening Data & Scoring]]
**Industry:** [[industries/property-management|Property Management]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** A common name matched to the wrong eviction record costs somebody a home, and the matching is rules and researchers.
**Tags:** #transformers #word-embeddings #graph-neural-networks #evaluation-metrics #compliance

## The Problem
Eviction and criminal records live in county courts. There are thousands of them, they publish in incompatible formats, many carry only a name and a partial address, and few carry an identifier that reliably distinguishes one person from another. Some are online; some require a physical visit; some are scanned paper.

Screening requires deciding whether a record about a name belongs to this applicant. The consequence of getting it wrong runs both ways and neither is symmetric: a false match denies housing to someone who did nothing, and a missed match hands an owner a risk they were paying to avoid. False matches are the ones that produce FCRA litigation, regulatory action, and the reputational damage the category is known for.

The matching is done by rules — name, date of birth where available, address history overlap — supplemented by human researchers reviewing borderline cases, and by physical court runners in jurisdictions with no electronic access. Rules are tuned conservatively, which pushes volume to human review, which is the cost centre. Turnaround expectations are measured in minutes, against a rental market where a unit leases in days.

## What Already Exists
Entity resolution is mature. Modern embedding models handle name variation, transliteration and nicknames far better than edit distance. Identity resolution vendors serve marketing and fraud at enormous scale, and commercial court record aggregators exist.

None is built for this decision. Marketing identity resolution optimises for coverage and tolerates false positives, because the cost of a wrong match is a mistargeted advert. Here a false positive is a denied housing application and a legal claim. Fraud-oriented systems are tuned in the opposite direction from what FCRA's accuracy standard requires, and none of them produces the reviewable, disputable, per-record decision trail the statute demands.

## The Customization Gap
**The loss function is legally asymmetric and must be explicit.** False match and missed match have very different costs, the difference is set by regulation and litigation exposure rather than by business preference, and it varies by record type. Generic matching products expose a similarity threshold, not a cost-calibrated decision.

**Every decision must be explainable and disputable.** A consumer can dispute a record, and the bureau must reinvestigate and explain. A model that returns a probability with no reviewable basis cannot be deployed. Retrieval of the matching evidence — which fields agreed, which did not, what tipped it — has to be a first-class output.

**Address and residence history is the discriminating signal.** Distinguishing two people with the same name in the same county turns on where each lived when. That is a temporal graph over addresses, and it is the domain structure generic products do not model.

**Jurisdiction rules are part of the match.** What may be reported, for how long, and whether a record type is usable at all now varies by state and municipality and is changing fast. The system must apply jurisdiction rules as versioned, dated logic, and prove which rule applied to a given report.

**Court formats change without warning.** Each county's publication changes when its case management system does, silently. Drift detection on ingestion is an operational necessity, not a refinement.

**Human review is part of the design, not a fallback.** The realistic goal is routing: confident matches automated, genuinely ambiguous ones to researchers with the evidence assembled. Optimising which cases reach a human is where most of the cost reduction is.

## Target Customer
VP of Data Operations or Chief Compliance Officer at a tenant screening bureau — the pairing is unusual and it is exactly why this sits unowned.

## Impact If Solved
Record matching is simultaneously the largest labour cost in screening and its largest legal exposure. Better matching reduces both at once, and it is the one improvement in this business where the consumer interest and the bureau's commercial interest point the same way.
