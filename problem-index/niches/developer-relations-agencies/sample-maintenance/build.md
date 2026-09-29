# Samples That Still Run

**Niche:** [[niches/developer-relations-agencies/sample-maintenance/profile|Sample & Tutorial Maintenance]]
**Industry:** [[industries/developer-relations-agencies|Developer Relations Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The most consequential content the programme produces is the least maintained.
**Tags:** #automation #workflow-orchestration #evaluation-metrics #compliance #data-integration #descriptive-statistics #change-point-detection #quick-win
**Contested on:** Every serious competitor in this niche is fighting to keep dozens of sample applications and tutorials working, because a developer's first experience of the product is running one — and whoever maintains them takes the account.

## The Problem
A developer evaluating a product clones the sample, runs it, and it fails. The sample was written eighteen months ago for a conference talk, its dependencies have moved, and the product's own interface changed twice since. The advocate who wrote it has moved on to the next talk. The programme has dozens of these, each representing a first impression, and nobody knows which of them still work.

## Why Nobody Has Built This
Samples are produced as artefacts of events rather than as maintained assets. Nobody owns them after the talk. Testing them requires infrastructure the programme does not have. And the failure is experienced by someone evaluating the product who simply leaves.

## What to Build
Test them continuously and retire what cannot be maintained. Build and run every sample in continuous integration against current dependencies and the current product, which is the core and turns a decaying collection into a maintained one. Test against the product versions the sample claims to support, so a passing test means something specific. Assign an owner per sample, since the absence of one is why they rot. Archive or clearly mark samples that will not be maintained, which is better than leaving them to fail silently on somebody's evaluation. Track which samples developers actually clone and run, so the maintenance effort goes where it matters. Fail loudly and visibly when a sample breaks, rather than discovering it from an issue. Pin dependencies so a sample does not break for reasons unrelated to the product. Update samples as part of the product's own release process where they demonstrate a changed interface. Report the proportion of samples currently passing, which is a number nobody has and which is usually sobering. And treat a broken sample as a first-impression defect rather than as stale content.

## Target Customer
Developer relations agencies and in-house functions, engineering and developer experience leadership, developer platform vendors, and testing tooling providers.

## Impact If Built
A developer's first experience of the product is running a sample that broke eighteen months ago and nobody noticed. Continuous testing with a named owner turns a decaying collection into an asset.
