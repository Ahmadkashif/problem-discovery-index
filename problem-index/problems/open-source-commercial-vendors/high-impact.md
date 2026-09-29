# Adoption That Cannot Be Seen

**Industry:** [[open-source-commercial-vendors|Open Source Commercial Vendors]]
**Type:** High Impact
**One-liner:** The companies deriving the most value from the software are often ones the vendor has never heard of, and every commercial decision is made from download counts that conflate a build cache with a production cluster.
**Tags:** #bert #word-embeddings #graph-neural-networks #gradient-boosting #k-means-clustering #confidence-intervals #feature-engineering #evaluation-metrics

## The Problem
An open-source vendor's software is used by organisations it cannot enumerate. Anyone can download, run and depend on it without any interaction, which is the point and is also the commercial problem.

The available signals are poor. Download counts are dominated by continuous integration systems pulling the same artefact thousands of times. Stars measure attention. Registry statistics cannot distinguish a developer experimenting from a company running a production fleet. Telemetry is contentious in open source, frequently disabled by default, and disabled again by exactly the security-conscious enterprises that matter most.

So every commercial decision runs on inference. Which industries actually use this. Which companies are running it at a scale where support would be worth buying. Which version is deployed in production, which determines whether a deprecation will hurt anyone. Whether the open-source strategy is producing commercial value at all, or whether the paid product would sell equally well without it.

Sales organisations at these companies work from inbound interest and conference conversations, which selects for the visible rather than the significant. The largest users are frequently the quietest.

## Why It's Unsolved
Telemetry is a genuine values conflict rather than a technical obstacle. Collecting usage data from open-source software without clear consent damages the trust the community relationship depends on, and several projects have caused lasting harm to themselves by getting it wrong. The correct posture is opt-in and clearly disclosed, which produces a biased sample of exactly the wrong kind.

Public signal reconstruction is the alternative and it is genuinely messy. Issues, discussions, public repositories, container image manifests, job postings, conference talks and blog posts contain enormous evidence about who uses what, and assembling it means entity resolution across sources with no shared identifier and highly variable reliability.

There is also a cultural discomfort. Analysing a community to find sales targets sits badly with maintainers who see the community as a community, and the tension between those two views is real inside every one of these companies.

And nobody has been willing to state the counterfactual honestly. Whether the open-source distribution is generating commercial value or merely giving the product away is the strategic question, and it is unanswerable without adoption data, so it is answered by conviction.

## What a Solution Looks Like
Adoption inferred from public signal, with the sources and the confidence stated. Job postings naming the technology, public repositories with configuration files, container manifests, conference talks, issue participants with corporate email domains, and discussion content that reveals deployment scale — each is weak individually and informative jointly.

Deployment scale estimation, since the commercially relevant distinction is not whether a company uses the software but whether they run it at a size where operating it is painful. Discussion content is surprisingly revealing about scale.

Version distribution inference for deprecation planning, which is the maintainer-facing use and the one the community would consider legitimate.

Telemetry designed for trust, if it is collected at all: opt-in, transparent about exactly what is sent, aggregated, and with the resulting insight returned to the community rather than only to sales.

And the strategic question addressed directly — where adoption converts and where it does not — because the licence changes that have swept this category were made under uncertainty that better measurement would have reduced.

## Impact If Solved
Every commercial decision at an open-source company is made without knowing who uses the software, which is why licence changes are made reactively and painfully. Reconstructing adoption from public signal respects the community relationship in a way telemetry does not, and it is the missing input to the strategic question the whole category is currently answering by conviction.
