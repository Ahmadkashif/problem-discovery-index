# Testing the Hypothesis and Not the Script

**Niche:** [[niches/conversion-optimization-firms/variant-implementation/profile|Variant Implementation Quality]]
**Industry:** [[industries/conversion-optimization-firms|Conversion Optimization Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The measured difference includes the flicker, the broken layout and the tracking gap, and the report attributes all of it to the idea.
**Tags:** #automation #evaluation-metrics #workflow-orchestration #data-integration #confidence-intervals #descriptive-statistics #change-point-detection #compliance
**Contested on:** Every serious competitor in this niche is fighting to change a live page without introducing effects that have nothing to do with the hypothesis — and whoever implements variants cleanly takes the account.

## The Problem
Client-side testing modifies a page after it has loaded. The user sees the original briefly, then the variant — a flicker that is itself an experience difference. The script may fail on some browsers, leaving a broken layout for a subset of the variant group. Tracking may fire differently. All of these differences are between the groups and none is the hypothesis, and they are frequently larger than the effect being measured.

## Why Nobody Has Built This
Client-side injection is what makes testing possible without engineering involvement, which is the entire commercial premise of the tooling. Flicker is known and tolerated. Cross-browser verification is manual and expensive. And the artefacts are invisible in the result, which reports only a difference.

## What to Build
Measure the artefacts and move the tests that matter server-side. Measure flicker duration per variant and report it alongside the result, which is the core — an unmeasured artefact of the same magnitude as the effect makes the result uninterpretable. Verify variants across the browsers and devices the client's traffic actually uses, from analytics rather than from a standard list. Detect broken renders in the wild rather than only in pre-launch checks, since the failures happen on configurations nobody tested. Deliver server-side where the change is substantial, which eliminates flicker entirely and is the right answer for the tests that matter most. Verify tracking fires identically in both arms, which is a common and silent source of spurious difference. Compare technical performance between arms — load time, errors, rendering — and report it, since a slower variant loses for reasons unrelated to the idea. Exclude sessions where the variant failed to render rather than counting them, which is currently counted as a result. Fail the test rather than reporting it when the artefacts are comparable to the effect. Build variants as code with review where the change is non-trivial. And state the implementation method in every result, so the reader can weigh it.

## Target Customer
Conversion optimisation firms and in-house experimentation teams, testing platform vendors, engineering leadership, and front-end tooling providers.

## Impact If Built
The measured difference includes flicker, broken renders and tracking gaps, and the report attributes all of it to the idea. Measuring the artefacts and moving substantial tests server-side is what makes a result about the hypothesis.
