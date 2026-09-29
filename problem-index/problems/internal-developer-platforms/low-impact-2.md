# Golden Path Drift After Generation

**Industry:** [[internal-developer-platforms|Internal Developer Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Scaffolding tools generate a service from a template in seconds, and from that moment the service and the template diverge forever, so a platform improvement never reaches anything that already exists.
**Tags:** #bert #word-embeddings #gradient-boosting #dbscan #graph-theory #evaluation-metrics #automation

## The Problem
A golden path is a template: generate a new service with the standard structure, pipeline, observability, security configuration and dependencies already correct. Generation works well and is one of the platform's clearest wins.

Then the service lives. It is modified for its own needs, the template improves, and the two drift apart permanently. Six months later the template has better defaults, a security fix and a new logging convention, and the two hundred services generated before that update have none of them.

The platform team's options are all poor. Ask every team to adopt the change, which is a persuasion campaign per improvement. Write a migration script, which is bespoke per change and breaks on divergent services. Or accept that improvements apply only to new services, which means the platform's benefit accrues to the smallest and least important part of the estate.

This is the single largest limit on what a platform can achieve. Every improvement reaches a shrinking fraction of the services that exist.

## What Already Exists
Cookiecutter-style scaffolding is standard in every platform. Backstage software templates and their commercial equivalents handle generation well. Renovate and Dependabot solve exactly this problem for dependency versions and solve it well. Infrastructure-as-code modules propagate through version bumps where teams update them. Some platforms offer template versioning without a propagation mechanism.

## The Customisation Gap
Dependency updating is solved and the same idea has never been generalised to templates. Renovate opens a pull request when a dependency version changes; nothing opens a pull request when a template changes, though the problem shape is nearly identical.

The difficulty is drift. A dependency bump is a version string; a template change must be applied to a file that has been modified locally, which is a three-way merge with the possibility of conflict. That is well-understood technology and is exactly what nobody has packaged for this use.

Drift measurement is the prerequisite and is independently useful. How far each service has diverged from its template, in which respects, and whether the divergence is deliberate customisation or neglect — a distinction that is inferable from whether the local change was intentional and coherent.

Convergence prioritisation follows: which drift actually matters. A missing security configuration matters, an old logging format usually does not, and a platform team with a ranked list can spend its persuasion budget where it counts.

## Impact If Solved
Golden paths deliver their value once, at generation, and every subsequent improvement reaches only new services — which caps what a platform can ever achieve on an existing estate. Automated template propagation with drift-aware merging is the generalisation of a pattern that already works for dependencies, and it is what would let a platform improve the software that already exists.
