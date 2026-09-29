# Impact Evaluation Runs on Data the Assurance System Already Holds and Cannot Reach

**Niche:** [[niches/coffee-shops-independent/commodity-certification-standards-bodies/profile|Agricultural Certification Standards Bodies]]
**Industry:** [[industries/coffee-shops-independent|Independent Coffee Shops]]
**Type:** Fix (Pain Point)
**One-liner:** The organization commissions expensive external studies to find out whether certification works, while the audit system beneath it holds multi-year observations on hundreds of thousands of farms in a form nobody can analyze.
**Tags:** #causal-inference #survival-analysis #gradient-boosting #hypothesis-testing #confidence-intervals #evaluation-metrics #feature-engineering #dimensionality-reduction #data-integration #compliance

## The Problem
Two functions sit in the same organization and do not speak. Assurance generates, every year, structured observations on hundreds of thousands of certified units — practices observed, non-conformances found, corrective actions taken, and whether they recurred — accumulating into a multi-year longitudinal record of the exact conditions certification claims to improve. Monitoring and evaluation, meanwhile, commissions external impact studies with fresh household surveys on small samples, because the assurance data is held by dozens of certification bodies in inconsistent structures, keyed to audit events rather than to units over time, and was never designed for analysis. So the organization pays repeatedly for small-sample evidence about a question its own operational data could address at population scale.

## Why It's Still Broken
Assurance data is operational and its purpose is a certification decision, so it is structured for case management. The audits are performed by independent certification bodies whose systems the scheme oversees but does not control, which makes standardization a governance negotiation rather than an engineering task. And there is a methodological objection with real force: certified farms are not a random sample and there is no untreated comparison group inside the assurance data, so causal claims cannot be made from it naively — which has been allowed to mean nothing can be learned from it at all.

## What a Fix Looks Like
Assurance data restructured around the certified unit over time rather than around the audit event, with a common finding taxonomy that every certification body reports into as a condition of accreditation. That alone converts a pile of audit files into a longitudinal panel. The methodological limitation is then addressed directly rather than used as a reason to stop: within-scheme variation supports strong descriptive and predictive analysis — which practices persist, which corrective actions prevent recurrence, how long improvement lasts — and where causal claims are needed, the panel provides the treated arm at population scale for designs that bring in external comparison groups, which is a far stronger basis than the small bespoke samples currently used. Commissioned studies then become targeted supplements answering what the panel cannot, instead of the primary evidence base.

## Who Feels the Pain
The impact team commissioning expensive studies that answer narrow questions; assurance staff generating a valuable record that disappears into case files; buyers and regulators asking for evidence of effect and receiving small-sample studies; and the scheme's own credibility, which rests entirely on a claim about improvement it evidences less well than it could.

## Impact If Fixed
Replaces periodic small-sample evidence with continuous population-scale evidence about the organization's central claim. It also makes the assurance system self-improving, because knowing which corrective actions actually prevent recurrence is directly actionable in how audits are conducted — and that finding is currently unavailable to anyone in the industry.
