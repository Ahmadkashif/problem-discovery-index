# Making Deletion Safe Enough to Do

**Niche:** [[niches/data-platform-integrators/retirement-and-rationalisation/profile|Retirement & Rationalisation]]
**Industry:** [[industries/data-platform-integrators|Data Platform Integrators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Everyone knows which assets are unused and nothing gets deleted, because deleting requires certainty nobody has.
**Tags:** #graph-theory #data-integration #compliance #workflow-orchestration #evaluation-metrics #automation #confidence-intervals #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to actually remove an unused asset, which requires proving nothing depends on it and finding someone willing to say so — and whoever makes deletion safe takes the account.

## The Problem
Models accumulate because deleting one requires knowing that nothing depends on it, and lineage covers only what the platform can see. Something outside — a spreadsheet, a reverse ETL job, a partner's extract, an analyst's saved query — may depend on it, and the person who would know has left. So nothing is deleted, the estate grows, and change becomes progressively riskier for everything that remains.

## Why Nobody Has Built This
Lineage stops at the platform boundary and the risk lives beyond it. Nobody owns most assets, so nobody can approve removal. The downside of a wrong deletion is visible and the upside of a right one is diffuse. And no deprecation process exists.

## What to Build
Extend the lineage, then make removal a staged process rather than a decision. Extend lineage beyond the platform to downstream consumers — reporting tools, reverse ETL, extracts, notebooks — which is the core and is where the residual risk actually lives. Deprecate rather than delete: mark, warn consumers, monitor for access, then remove, which converts an irreversible decision into a reversible sequence. Monitor access during the deprecation window so a hidden consumer surfaces before removal rather than after. Assign an owner to every asset, since the absence of one is why nothing can be approved. Make removal reversible for a period, which lowers the stakes decisively. Provide a standard deprecation notice to consumers with a timeline. Batch retirements rather than deciding asset by asset, as the process cost is what makes individual removal uneconomic. Report what was removed and what it saved, which sustains the practice. Track the estate's net growth as a managed metric, since rationalisation without a growth constraint is pushing water. And make creation require an owner and a stated purpose, which is the upstream fix.

## Target Customer
Data platform teams and leadership, integrators and analytics consultancies, catalogue and lineage vendors, and governance providers.

## Impact If Built
Deleting requires certainty nobody has because lineage stops at the platform boundary and nobody owns the asset. Extended lineage plus a staged deprecation converts an irreversible decision into a reversible sequence.
