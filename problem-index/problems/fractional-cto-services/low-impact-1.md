# Technical Due Diligence Under Deal Timelines

**Industry:** [[fractional-cto-services|Fractional CTO Services]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Two weeks, restricted code access, a management team with an interest in the answer, and a report that will inform an eight-figure decision.
**Tags:** #graph-neural-networks #gradient-boosting #bert #change-point-detection #evaluation-metrics #confidence-intervals #compliance #survival-analysis

## The Problem
Technical due diligence assesses a target company's technology for an acquirer or investor. The questions are consistent: is the architecture sound enough to support the growth case, what technical debt is material, what is the key-person risk, are there licensing or security exposures, is the team what the plan requires, and what will the first two years of engineering investment actually cost.

The constraints are severe. The timeline is the deal's, usually two to four weeks. Code access is limited and sometimes supervised, since the target is disclosing to a possible acquirer who might walk away. Management are the primary source and have an interest in the outcome. And the practitioner is frequently unfamiliar with the domain.

So the assessment leans on interviews, a document request list, a partial code review and experience. The reports that result are professional and are substantially a set of judgements with limited underlying measurement, and their accuracy is unknown because nobody ever checks them against what happened post-close.

The recurring failure is the same in most post-mortems: the thing that turned out to matter was not the architecture that got the attention but the key-person dependency, the undocumented integration, or the engineering capacity assumption that was optimistic by a factor of two.

## What Already Exists
Diligence practices have standard question sets and maturity frameworks. Static analysis, dependency and licence scanning, and security scanning can run quickly where access permits, and open-source licence compliance tooling is mature. CodeScene provides behavioural code analysis from repository history and is the closest available instrument. Some private equity operating groups have built internal diligence toolkits. Data room platforms handle document exchange.

## The Customisation Gap
What is missing is fast, access-constrained measurement. Repository history alone — without a full code review — yields change concentration, coupling, ownership concentration, bus-factor exposure, contributor continuity and the rate at which components are rewritten, all of which speak directly to the diligence questions and can be produced in a day if the history is available even in read-only form.

Key-person risk is the clearest case and the most consistently underweighted. Ownership concentration by component, contributor tenure and the proportion of critical code with a single knowledgeable author are computable and are almost never quantified in a diligence report, despite being the finding most likely to matter after close.

The engineering cost projection is the second gap. The plan's assumptions about delivery capacity can be tested against the target's own historical throughput, cycle time and rework rate rather than accepted from management, and the divergence between the two is frequently the most important number in the report.

And the calibration is what a firm can build across deals: retaining diligence findings against post-close outcomes across many transactions would produce base rates for which findings actually predicted problems — a corpus private equity operating groups are uniquely placed to build and none have.

## Impact If Solved
Diligence findings inform decisions with very large consequences and rest on limited measurement under severe time pressure. History-derived analysis that works under restricted access produces the key-person, concentration and capacity findings that post-close post-mortems repeatedly identify as the ones that mattered, and a retained corpus against outcomes would give the practice something no individual's experience can supply.
