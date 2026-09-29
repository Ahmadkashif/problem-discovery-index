# A Guarantee That Covers a Minority of Features

**Niche:** [[niches/mlops-platforms/feature-coverage-and-lineage/profile|Feature Coverage & Lineage]]
**Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Feature stores exist specifically to guarantee that training and serving see the same values, and they deliver that guarantee only for features defined inside them — which is a minority of the features any real model uses.
**Tags:** #data-integration #graph-theory #evaluation-metrics #automation #descriptive-statistics #workflow-orchestration #hypothesis-testing #compliance
**Contested on:** Every serious competitor in this niche is fighting to extend the consistency guarantee to the features that were never registered — and whoever does that takes the account, because the unregistered features are the majority and are where the failures are.

## The Problem
A team adopts a feature store, registers forty features, and believes the consistency problem is handled. The model in production takes a hundred and thirty inputs. Ninety of them come from a warehouse join in the training script and an inline computation in the serving handler, written separately, agreeing by coincidence. Nobody has computed the ratio, so the team's confidence is calibrated to a guarantee that covers less than a third of their exposure. The next skew failure lands in the ninety, the investigation starts with the assumption that the feature store rules it out, and two days are spent before someone checks the coverage.

## Why Nobody Has Built This
Registering a feature is friction that a researcher under deadline routes around, and the route around is always available. Vendors measure adoption by features registered, which is a number that grows, rather than by coverage, which is a number that would embarrass. Discovering unregistered features requires inspecting the serving path, which belongs to a different team and frequently a different vendor. And nobody has framed coverage as a metric, so it is not reported, not targeted, and not improved.

## What to Build
Measure coverage and close it automatically. Report the registered share of every production model's input vector as a standing metric, which requires only the model signature and the registry and immediately reframes the team's confidence — this is the smallest useful build in the niche and the one that changes behaviour fastest. Discover unregistered features by instrumenting the serving path and tracing each input back to its origin, which turns a manual audit into a continuous inventory. Offer promotion in one step, so that an unregistered feature discovered today can be brought under governance without a project, because friction is the whole reason it was not registered in the first place. Extend the lineage graph from the upstream source through the feature to every model consuming it, in both directions, since the reverse query — what breaks if this column changes — is the one the data engineering team needs and cannot answer. Attach ownership to every feature, registered or not, because an unowned broken feature is an incident with no assignee. Detect duplicate and near-duplicate definitions across teams, which are endemic and silently disagree. And report coverage-weighted risk rather than a raw count, since an unregistered feature the model barely uses is not the same exposure as an unregistered one it depends on.

## Target Customer
Data and ML platform teams, feature store vendors whose guarantee is being over-trusted, and the data engineering functions who own the upstream sources.

## Impact If Built
The guarantee is real and partial, and nobody measures the part. Reporting registered coverage per model is a small build that recalibrates an entire organisation's confidence, and reverse lineage answers the question the data team currently cannot.
