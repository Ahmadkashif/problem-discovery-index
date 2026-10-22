# Availability Claim Validator Against Plant and Speed Tests

**Niche:** [[niches/wired-broadband-providers/bdc-availability-filings/profile|Broadband Data Collection & Availability Filings]]
**Industry:** [[industries/wired-broadband-providers|Wired Broadband Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Providers certify location-level availability claims without systematically checking each against their plant, drop lengths, subscriber speeds and crowdsourced tests, and learn which claims were weak only when a challenge arrives.
**Tags:** #gradient-boosting #k-nearest-neighbors #feature-engineering #evaluation-metrics #compliance #data-integration
**Contested on:** Every serious competitor in this niche is fighting to produce a semiannual availability filing reconciled to the current Fabric that survives the challenge process, and whoever delivers it with the fewest engineer-hours and the fewest sustained challenges takes the account.

## The Problem
A filing claims tens of thousands of locations. Some are passed by plant but need a 1,500-foot drop or make-ready that would take months; some are served by a technology that can't deliver the advertised speed at that distance; some are duplicates of a neighbouring Fabric point. Each is a challenge waiting to happen.

## Why Nobody Has Built This
Filing tools focus on producing the file format. The evidence needed to validate claims sits in other systems: plant records, install history, speed tiers, crowdsourced speed tests licensed separately.

## What to Build
A validator that scores each claimed location for challenge risk using distance from plant and drop length, install history nearby, the speed tier actually delivered to neighbouring subscribers, licensed speed-test data and Fabric unit counts, trained on past challenge outcomes. It ranks claims for engineer review before certification and assembles evidence for the ones kept.

## Target Customer
Regulatory managers and consulting engineers at mid-sized operators and filing consultancies.

## Impact If Built
Fewer sustained challenges, faster certification, and a defensible record when a state or competitor contests coverage.
