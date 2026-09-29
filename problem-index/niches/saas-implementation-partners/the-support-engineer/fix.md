# Why Is This Field Required

**Niche:** [[niches/saas-implementation-partners/the-support-engineer/profile|The Post-Go-Live Support Engineer]]
**Industry:** [[industries/saas-implementation-partners|SaaS Implementation Partners]]
**Type:** Fix (Pain Point)
**One-liner:** The client wants a field made optional, and nobody knows whether making it optional breaks a downstream process.
**Tags:** #worker-facing #quick-win #graph-theory #data-integration #evaluation-metrics #workflow-orchestration #descriptive-statistics #compliance
**Contested on:** Every serious competitor in this niche is fighting to let someone support a configuration built by people who have left, documented in a slide deck, with no record of why any of it is the way it is — and whoever supplies that context takes the account.

## The Problem
The most ordinary change request is the hardest one. A field is mandatory; the client wants it optional. It might be required by a validation rule, an integration, a report, a compliance requirement, or somebody's preference in a workshop three years ago. Establishing which takes hours of tracing, the answer is frequently not conclusive, and the engineer either refuses a reasonable request or makes the change and hopes.

## Why It's Still Broken
The dependencies are not mapped — a configuration element's consumers are discoverable only by searching the whole tenant, which nobody has time to do for a routine request. Intent was never recorded. The people who know have left. And the change is small enough that a full investigation feels disproportionate.

## What a Fix Looks Like
Map the dependencies once and record the reasons going forward. Build a reference map of what consumes each configuration element, which is the fix and is extractable from platform metadata on most of these platforms. Record a reason against every configuration element as changes are made from now on, which costs a line and compounds. Recover the original reasons from requirements documents and tickets where they exist, for the elements that matter most. Check usage data to see whether the element is actually used, which frequently answers the question outright. Flag elements referenced by integrations specifically, as those are the dependencies that break most expensively. Note compliance-driven configuration explicitly, since those must never be changed casually and are indistinguishable from preferences today. Test the change in a realistic sandbox rather than reasoning about it. Keep a change log with the reason for each modification, which is the version history the platform does not provide. Escalate to the original delivery team while they are still reachable. And answer the client with the dependency list rather than with a judgement, which is more persuasive either way.

## Who Feels the Pain
Support engineers tracing dependencies for a routine request; clients waiting days for a small change or refused without explanation; managed services margins consumed by investigation; and the next incident, caused by a change made hopefully.

## Impact If Fixed
A configuration element's consumers are discoverable only by searching the whole tenant, which nobody has time to do for a routine request. A reference map extracted from metadata makes the ordinary change answerable.
