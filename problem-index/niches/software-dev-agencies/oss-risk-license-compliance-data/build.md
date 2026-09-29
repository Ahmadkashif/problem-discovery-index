# Severity Scores Nobody Validates Against Exploitation

**Niche:** [[niches/software-dev-agencies/oss-risk-license-compliance-data/profile|Open Source Risk & License Compliance Data]]
**Industry:** [[industries/software-dev-agencies|Software Development Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Scanners emit thousands of critical findings per codebase, a small fraction of published vulnerabilities are ever exploited, and the vendor has never measured which of its criticals mattered.
**Tags:** #gradient-boosting #survival-analysis #evaluation-metrics #graph-neural-networks #causal-inference

## The Problem
A dependency scan on a real application returns hundreds to thousands of findings. Each carries a severity, mostly inherited from a public scoring standard that rates a vulnerability's theoretical impact in isolation — not its impact in this application, with this configuration, behind this network boundary, on a code path that may never execute.

The consequence is the defining complaint of the category. Development teams cannot remediate thousands of findings, so they triage by severity, and severity is a poor guide: a large majority of published vulnerabilities are never exploited in the wild, while a small number are exploited within days of disclosure. Teams learn that criticals are usually not urgent, which is a rational adaptation and a dangerous habit.

The vendors know this. Several have added reachability analysis — does the vulnerable function actually get called — which is a genuine improvement and still a static property rather than a prediction. What none of them does is model exploitation itself: given a vulnerability's characteristics, its ecosystem, its dependency position, the artefacts published about it, and how it was disclosed, what is the probability it is exploited, and when.

That is a supervised problem with real labels. Exploitation is observed and catalogued. Proof-of-concept publication is observed. Inclusion in exploit kits and in botnet activity is observed. The vendor's own telemetry records which findings customers actually fixed and how fast. Nobody joins these.

## Why Nobody Has Built This
Severity arrived as an inherited standard, and inheriting it is defensible in a way that departing from it is not. A vendor that downgrades a critical and is wrong once has a serious problem; one that reports every critical as critical has an industry-standard problem.

Coverage was also the competitive axis for a decade. Vendors competed on ecosystems supported and advisories curated, because that is what procurement compared, and precision was nobody's scorecard.

And the alert-fatigue complaint has been absorbed as a product problem rather than a data problem — answered with filters, policies and workflow rather than with a model of what actually gets exploited.

## What to Build
Exploitation prediction, with the dependency graph as a feature and the vendor's own remediation telemetry as a second label.

**Model time to exploitation as survival.** Most vulnerabilities are never exploited, and those that are are exploited at wildly varying speed. That is time-to-event data with heavy censoring — the correct frame, and one no vendor uses.

**Use the ecosystem graph.** A vulnerability's real significance depends on how central the package is, how many things depend on it transitively, and how quickly maintainers patch. The vendor holds the entire dependency graph for the major ecosystems and can compute all of this.

**Predict at the application level, not the advisory level.** The customer's question is what to fix in this codebase this week. Combining exploitation likelihood with reachability, deployment context and exposure produces a ranked list, which is the actual deliverable, and it can be scored.

**Model licence risk as obligation, not as a label.** Licence findings are reported as an identifier. What the customer needs is the obligation triggered by their specific use — linking, distribution, network service — and whether it conflicts with another dependency's terms. That determination is made by lawyers today and is the most consistently repeated legal judgment in software.

**Publish the calibration.** How the previous quarter's high-priority findings performed against subsequent exploitation. In a market where every vendor claims to cut noise, being the one with a measured hit rate is a position no competitor can assert their way past.

## Target Customer
Chief Research Officer or VP of Security Research at a software composition analysis vendor. The commercial argument is that advisory coverage has converged across vendors and prioritisation is now the only differentiator anyone is buying on — and it is currently sold as a heuristic.

## Impact If Built
Development teams across the industry ration attention against severity scores that are known to be weakly related to real risk, and a large amount of remediation effort goes to vulnerabilities that will never be exploited while the ones that will get the same queue position. A calibrated exploitation model over the dependency graph reallocates that effort — and it is buildable from data these vendors already hold.
