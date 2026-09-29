# Technology Selection Advice

**Parent Industry:** [[industries/fractional-cto-services|Fractional CTO Services]]
**Category:** Low Digitized
**Contested on:** Whether a platform recommendation rests on operational evidence from comparable deployments or on vendor documentation, analyst reports and the advisor's own last three projects.

## Profile

**Market Size:** ~$450M
**Share of Parent Industry:** ~15%
**Digital Adoption:** Very low — vendor material and personal recollection
**Target Buyer:** Advisory practitioners, architecture consultants, client engineering leadership
**Automation Potential:** Moderate — the evidence exists but is nobody's to aggregate

## What Makes This a Distinct Niche

A large share of what a fractional CTO is paid for is a decision between named options. This database or that one. This cloud, this framework, this message broker, this vendor, or building it. Each decision commits the client to years of operational consequence and is frequently irreversible in practice.

The evidence available to make it is startlingly thin. Vendor documentation describes the happy path. Analyst reports describe market position, which correlates weakly with whether a technology will work for this workload. Benchmarks are published by parties with an interest. Conference talks describe successes. What the advisor actually uses, underneath the research, is their own experience of the last three projects — a sample of three, selected by where they happened to work, in contexts that may not resemble the client's at all.

This is a distinct niche because the buyer, the failure and the missing evidence are all different from the assessment niches. The buyer is often the client's own engineering leadership rather than an investor. The failure is slow — a wrong platform choice does not fail on delivery, it fails eighteen months later in operational cost and constraint. And the missing evidence is not inside the client's boundary at all; it is distributed across everyone who has already made the same choice and never wrote down what happened.

## Current Tools & Gaps

Analyst firms — Gartner, Forrester, IDC — sell market positioning and are structurally compromised by vendor relationships. Review platforms like G2 and TrustRadius collect user sentiment at a granularity far coarser than an architecture decision requires, heavily gamed, and weighted toward buyers rather than operators. Public benchmarks exist per category and are almost always authored by a vendor or an enthusiast. Technology radars published by consultancies are genuinely useful and are one firm's opinion, updated twice a year.

The gap is operational outcome data at decision granularity. Nobody aggregates what actually happened after the choice: what the migration really cost, what the failure modes were in production at a given scale, what the operational burden turned out to be, how the cost curve behaved as usage grew, how often the choice was reversed and why. Every organisation that has made the decision knows the answer for their case. None of them are asked, and the one profession that sees many such cases — advisory — has no mechanism for retaining them, which is the same corpus problem as [[niches/fractional-cto-services/assessment-calibration/profile|🎯 Assessment Calibration]] seen from a different angle.

## Problems

- [[niches/fractional-cto-services/technology-selection/build|🔨 Build: Operational Outcomes at Decision Granularity]]
- [[niches/fractional-cto-services/technology-selection/buy|🛒 Buy: Review Platforms Pointed at Operators]]
- [[niches/fractional-cto-services/technology-selection/fix|🔧 Fix: The Sample of Three]]
