# Automated Migration From Dependency Tooling

**Niche:** [[niches/internal-developer-platforms/golden-path-drift/profile|Golden Path Drift]]
**Industry:** [[industries/internal-developer-platforms|Internal Developer Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Dependency update tools open reviewed pull requests across hundreds of repositories automatically, and platform template updates are applied by asking teams to do it themselves.
**Tags:** #graph-theory #bert #descriptive-statistics #evaluation-metrics #confidence-intervals #automation #workflow-orchestration #compliance
**Contested on:** Every serious competitor here is fighting to make a platform improvement reach the services that already exist — and whoever does that takes the platform, because a golden path that only applies at creation improves nothing after the first month.

## The Problem
Dependency update tooling solved the fan-out problem: detect that an update is available, apply it across every repository that depends on it, open a reviewed change in each, run the tests, and track which have merged. It is deployed at scale and is unremarkable. Template updates are the same fan-out with a different payload and are applied by a platform team sending a message asking teams to update.

## What Already Exists
Automated dependency update tools with cross-repository fan-out, grouping and rollout tracking; codemod and automated refactoring tooling that applies structural changes across codebases; large-scale change tooling used inside large engineering organisations; and pull request automation frameworks.

## The Customization Gap
The adaptation is to templated files the team has since edited. It requires: (1) three-way merge against the template's own history rather than a replacement, which is the mechanism that handles a team's local edits and is what distinguishes this from an overwrite; (2) provenance to know which regions are template-derived, since without it the merge has no basis and this is the enabling record described in the build note; (3) conflict presentation in terms the receiving team understands, because the team did not write the template and a raw conflict in generated configuration is unresolvable for them — the change must explain what the platform wanted and why; (4) change classification, since a mechanical update can be merged automatically with tests passing and a semantic one needs a decision, and treating them identically produces either risk or unnecessary review; and (5) rollout tracking with a coverage metric, since the platform team's question is what proportion of the estate has the fix and the dependency tooling's per-repository view does not answer it.

## Target Customer
Platform engineering teams, scaffolding and template vendors, and the dependency update tooling projects for whom this is an adjacent payload.

## Impact If Solved
The fan-out pattern is proven and deployed at scale for dependencies, and the template payload has not been connected to it. Three-way merge against template history is the mechanism, and provenance is what makes it possible.
