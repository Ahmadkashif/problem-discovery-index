# Skill Taxonomy for Requisitions Nobody Writes Consistently

**Niche:** [[niches/it-staffing-firms/contingent-workforce-msp-vms/profile|Contingent Workforce MSP & VMS Programmes]]
**Industry:** [[industries/it-staffing-firms|IT Staffing Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Every rate benchmark and supplier comparison depends on two requisitions being the same job, and requisitions are written by hiring managers in their own words.
**Tags:** #text-classification #word-embeddings #large-language-models #k-means-clustering #data-integration

## The Problem
A programme's analytics rest on grouping like with like. A rate benchmark for "Senior Java Developer" is only meaningful if the requisitions in it are actually comparable, and requisitions arrive as free text written by hiring managers who describe the same role as a backend engineer, a Java developer, a full-stack developer, or a software engineer III, with skill lists that mix languages, frameworks, tools, domains, and wishful thinking.

Programmes handle it with a category taxonomy applied at intake, usually by a coordinator picking from a dropdown under time pressure. The category is coarse, the mapping is inconsistent, and everything downstream — rate cards, supplier scorecards, savings reporting — inherits the inconsistency.

## What Already Exists
Text classification and semantic similarity are commodity capabilities. Commercial skills taxonomies exist and are actively maintained. Job title normalization is offered by several labour market data vendors.

## The Customization Gap
The available taxonomies were built for a different question.

**Rate comparability, not skill description.** Public taxonomies group roles by what the work is. A rate benchmark needs groups that behave the same way in the market — and two roles with nearly identical skill descriptions can price very differently because of clearance requirements, on-site expectations, or client-specific tooling. The right grouping is defined by observed price behaviour, which the programme can measure and a taxonomy vendor cannot.

**Seniority is the dominant variable and is written arbitrarily.** Level titles are not comparable across clients or even across departments, and the actual seniority signal sits in the years of experience, scope language, and rate expectation in the requisition body.

**Client-specific vocabulary must map to a shared spine.** Each enterprise has internal role names and internal levels. The programme needs both — client-specific for the client's own reporting, and normalized for cross-client benchmarking — and generic classification produces one.

**The requisition, not the title.** Most of the signal is in the body: the must-haves, the location and on-site requirement, the clearance, the duration, and the manager's own rate expectation. Title-only normalization discards it.

**Drift detection.** New skills and new role shapes appear continuously, and a taxonomy that does not notice quietly misclassifies the fastest-growing part of the market — which is also the part where rate error is most expensive.

## Target Customer
Head of Data Science or VP of Analytics at an MSP or VMS provider, where requisition categorization quality silently determines the credibility of every number the programme reports.

## Impact If Solved
Every benchmark, scorecard, and savings claim the programme makes rests on this grouping, and it is currently produced by a coordinator with a dropdown. Grouping requisitions by observed market behaviour rather than by title makes rate cards meaningfully comparable for the first time — and it is the precondition for the fill-probability modelling that is the real prize here.
