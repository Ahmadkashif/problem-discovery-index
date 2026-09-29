# Air-Gapped Means Out of Date

**Niche:** [[niches/ci-cd-platforms/self-managed-enterprise-ci/profile|Self-Managed & Enterprise CI]]
**Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Environments that are disconnected for security reasons run software that is years old for the same reasons, which makes the security posture worse rather than better.
**Tags:** #graph-theory #descriptive-statistics #evaluation-metrics #confidence-intervals #change-point-detection #compliance #quick-win #automation
**Contested on:** Every serious competitor here is fighting to give an organisation hosted-grade pipelines inside its own boundary — with the evidence, the hardware and the control it requires — and whoever does that takes the enterprise, because the alternative is that they keep operating it themselves.

## The Problem
A secure environment has no route to the internet, by design. Every tool, base image, dependency and platform component must be brought in through a controlled process that involves a request, a review, a transfer and a manual installation. The process is slow enough that it is used rarely, so the environment's toolchain is two years behind, its base images carry known vulnerabilities, and the pipeline's own platform is several versions old. The isolation that was supposed to improve security has produced an estate that would fail any dependency scan, and everyone involved knows it.

## Why It's Still Broken
The import process was designed around the exceptional case — bringing in something new — and is used for the routine case of keeping things current, for which it is far too heavy. Nobody owns currency in these environments: security owns the boundary, platform owns the tools, and neither owns the fact that the tools are old. The vulnerability exposure is invisible because the scanners that would report it also need updating and frequently cannot reach their feeds. And there is a widespread and incorrect belief that isolation substitutes for patching.

## What a Fix Looks Like
Make currency routine rather than exceptional. Establish a regular, batched, pre-approved import channel for the known toolchain — a scheduled bundle with its provenance and scan results attached, reviewed as a batch rather than per artefact — which turns dozens of individual requests into one recurring process and is the change that makes currency achievable at all. Mirror internally, so that the isolated environment has a local registry populated by the import rather than requiring an import per need. Scan inside the boundary with offline vulnerability data included in the bundle, so exposure is visible even though the feed cannot be reached live. Report currency explicitly — how far behind each component is and what known vulnerabilities that implies — which is the number that makes the risk legible to the people who own the boundary. Verify the bundle's integrity on arrival with signatures, which is what allows the batch review to be trusted. And measure the import process itself, since its latency is what determines how far behind the environment runs.

## Who Feels the Pain
Engineers working in secure environments with outdated tooling; security functions whose isolation has produced an unpatched estate; and organisations whose most sensitive environments are their least current.

## Impact If Fixed
A scheduled pre-approved bundle converts currency from an exceptional request into a routine process, which is the whole reason these environments fall behind. Offline scanning with imported vulnerability data makes the exposure visible to the people who own the isolation decision.
