# Generated Once, Divergent Forever

**Niche:** [[niches/internal-developer-platforms/golden-path-drift/profile|Golden Path Drift]]
**Industry:** [[industries/internal-developer-platforms|Internal Developer Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Scaffolding tools generate a service from a template in seconds, and from that moment the service and the template diverge forever, so a platform improvement never reaches anything that already exists.
**Tags:** #graph-theory #bert #k-means-clustering #descriptive-statistics #evaluation-metrics #confidence-intervals #automation #compliance
**Contested on:** Every serious competitor here is fighting to make a platform improvement reach the services that already exist — and whoever does that takes the platform, because a golden path that only applies at creation improves nothing after the first month.

## The Problem
A platform team improves the service template: better observability defaults, an updated base image, a corrected health check, a security header. It applies to services created from that moment. The four hundred existing services keep what they had. Six months later the team runs a campaign to update the estate, which means opening four hundred pull requests by hand or asking four hundred teams to do it, and the campaign covers perhaps half before other work intervenes. A year later the estate has services carrying five different eras of template, and the newest improvement is in twelve of them.

## Why Nobody Has Built This
Scaffolding is a one-way operation by design — it generates and forgets — because tracking the relationship afterwards requires knowing which parts of a service came from the template and which the team wrote, and nothing records that. The generated code is then edited, which makes a naive re-application destructive. Migration campaigns are run manually because there is no mechanism, and they stall because they are somebody's project rather than a process. And scorecards were adopted as the response, which measures the divergence without addressing it.

## What to Build
Maintain the relationship and update mechanically. Record provenance at generation: which files and sections came from which template at which version, so the relationship survives and a later update knows what it may touch — this is the enabling change and is cheap at generation and impossible to reconstruct afterwards. Compute divergence continuously, so the platform team sees the estate's distribution across template versions and the specific services carrying each deficiency, which is the visibility that turns a vague campaign into a targeted one. Apply updates as proposed changes rather than as overwrites, opening a reviewed change per service with the template's diff applied and conflicts surfaced where the team has edited that region — which is exactly how dependency update tooling works and is directly transferable. Batch by change rather than by service, since one template improvement across four hundred services is one decision and four hundred mechanical applications. Distinguish the mechanical from the semantic, since a base image bump applies cleanly and a restructured configuration does not, and only the second needs a person. Report coverage per improvement, so the platform team knows what proportion of the estate a change has actually reached. And retrofit provenance for the existing estate by matching services against template history, which is imperfect and is far better than nothing.

## Target Customer
Platform engineering teams, scaffolding and template tooling vendors, and the security functions who need a template fix to actually reach the estate.

## Impact If Built
A platform's leverage is limited to new services, which is a small fraction of the estate, and the mechanism to change that is provenance at generation plus proposed updates. The dependency update pattern transfers directly and is the proven form of this exact interaction.
