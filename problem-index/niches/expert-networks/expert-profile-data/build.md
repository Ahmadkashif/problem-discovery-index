# Detecting the Job Change Before the Call

**Niche:** [[niches/expert-networks/expert-profile-data/profile|Expert Profile & Restriction Data]]
**Industry:** [[industries/expert-networks|Expert Networks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An expert's record says "former" until they next take a call, while their public profile changed months ago.
**Tags:** #change-point-detection #logistic-regression #large-language-models #evaluation-metrics #compliance #data-integration
**Contested on:** Every serious competitor in this niche is fighting to know an expert's current employer and restriction status before the call rather than after it — and whoever keeps a large database current without re-asking every expert wins both compliance and speed.

## The Problem
Networks learn of job changes when the expert updates their profile or attests before a call. Between calls the database is wrong for a share of experts that grows with time.

## Why Nobody Has Built This
Re-verifying inactive experts has no immediate revenue, and the risk is borne only when a stale record is used.

## What to Build
Monitor permitted public signals for employment changes, score each record's staleness risk, prioritise re-verification for experts likely to be sourced soon, and block forwarding when a likely change is unconfirmed.

## Target Customer
Compliance and operations heads at networks.

## Impact If Built
Keeps the compliance-critical field current where it matters, and speeds sourcing by surfacing experts whose new roles make them newly relevant.
