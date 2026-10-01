# The Estimate Nobody Updated After Guidance

**Niche:** [[niches/financial-data-vendors/broker-estimates-consensus/profile|Broker Estimates & Consensus]]
**Industry:** [[industries/financial-data-vendors|Financial Data Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** A broker's estimate untouched for six weeks after the company cut guidance still sits in consensus, and the surprise reported on results day is partly an artefact of it.
**Tags:** #change-point-detection #descriptive-statistics #evaluation-metrics #quick-win #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to hold the broadest set of contributed broker estimates at line-item detail and to clean them into a consensus clients trust — and whoever gets both the contributions and the hygiene right owns the number earnings surprises are measured against.

## The Problem
Fixed staleness windows (exclude after N days without revision) are blunt: too short in quiet periods, too long after an event. Specialists override by judgement where they notice.

## Why It's Still Broken
The rule is simple, defensible and auditable; an event-aware rule is better and harder to explain to a broker whose estimate was excluded.

## What a Fix Looks Like
Trigger a staleness review on events rather than on elapsed time; show the specialist each un-revised estimate with the event it predates; record the decision and reason; publish the policy so contributors know the rule.

## Who Feels the Pain
Clients trading on surprise, specialists cleaning under deadline, and brokers whose stale numbers are silently included.

## Impact If Fixed
A small policy and tooling change that removes a known, systematic distortion from the most quoted number in equity research.
