# The Alert Inventory Nobody Has

**Niche:** [[niches/observability-vendors/alert-quality-and-thresholds/profile|Alert Quality & Thresholds]]
**Industry:** [[industries/observability-vendors|Observability Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Classifying every alert into fired-and-actioned, fired-and-ignored, never-fired and missed-the-incident requires no modelling at all, would let most teams prune in an afternoon, and exists in no platform.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #k-means-clustering #quick-win #worker-facing #automation
**Contested on:** Every serious competitor here is fighting to replace thresholds somebody guessed with numbers backtested against the organisation's own incidents — and whoever does that takes the reliability account, because alert fatigue is the most cited operational complaint in the category.

## The Problem
A team has four hundred alert rules accumulated over five years. They know the alerting is bad. They cannot prune it, because they do not know which rules matter: some were created for incidents that no longer occur, some fire weekly and are auto-acknowledged, some duplicate each other, and some have never fired. Every firing, acknowledgement, escalation and resolution is recorded in the paging platform. The classification that would let them delete two hundred rules on a Friday afternoon is four queries and does not exist as a feature anywhere.

## Why It's Still Broken
Alert outcomes live in the paging platform and alert definitions live in the observability platform, which are two products and frequently two vendors, and nobody joined them. The classification requires deciding what counts as actioned, which is a small definitional decision nobody has made. And pruning alerts carries the same asymmetry as deleting dashboards and templates: removing one that mattered is visible and keeping a noisy one is not, so without evidence the rational choice is to keep everything.

## What a Fix Looks Like
Produce the inventory. Join alert definitions to firing history and to acknowledgement and resolution outcomes, and classify every rule into four classes: fired and led to action, fired and was acknowledged without action, never fired, and — the important one — incidents that occurred with no alert. Rank the fired-and-ignored class by volume, since a handful of rules usually produce most of the noise and deleting them is the fastest improvement available to on-call life. Identify duplicates and near-duplicates, which accumulate because creating a rule is easier than finding the existing one. Flag rules whose author has left and that have not fired in a year, which is a large and safely removable population. Report the missed-incident class separately and prominently, because it is the dangerous half and everyone's attention is on the noisy half. Make archival reversible so the decision is easy. And re-run it quarterly, because the estate regrows exactly as dashboard and template estates do.

## Who Feels the Pain
On-call engineers woken by rules nobody would defend; teams that know their alerting is bad and cannot safely prune it; and organisations whose real coverage gaps are hidden behind a wall of noise.

## Impact If Fixed
The classification needs no modelling and is a join between two systems every organisation already runs, and it is the fastest available improvement to on-call quality. The missed-incident class is the half nobody looks for and is where the actual risk sits.
