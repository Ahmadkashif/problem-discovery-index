# Event Triage Trained on the Operators' Own Verdicts

**Niche:** [[niches/security-alarm-integrators/video-verified-remote-guarding/profile|Video-Verified Monitoring & Remote Guarding]]
**Industry:** [[industries/security-alarm-integrators|Security Alarm Integrators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every remote-guarding operator labels thousands of camera events a shift as real or nuisance, and that verdict never goes back into the filter that raised the event.
**Tags:** #object-detection #cnns #transfer-learning #contrastive-learning #evaluation-metrics #worker-facing #automation
**Contested on:** Every serious competitor in this niche is fighting to clear each camera event (real intruder or not) within seconds at a monthly cost per camera below what a guard costs, and whoever delivers the most police-priority verified dispatches per operator hour takes the account.

## The Problem
Camera analytics detect people and vehicles, but at a car lot at 2 a.m. a person may be a thief, a security patrol, a lot attendant or someone cutting through. Operators make that call from context: time, path, behaviour, the site's normal traffic. They log a disposition. The analytics never see it, so the same attendant raises the same event every night.

## Why Nobody Has Built This
Detection models come from camera and analytics vendors, while dispositions live in the monitoring software. Video belongs to the subscriber under contract, which makes pooling across clients sensitive. Each provider is also too small to build its own model, and too protective of its operator know-how to share.

## What to Build
A per-site and per-provider event classifier fine-tuned on the provider's own operator dispositions, under its own client contracts. It learns site-specific normal activity (authorised people, regular vehicles, schedules), ranks the queue by probability of a real threat and auto-closes recurring nuisance events with an audit trail. Precision on "auto-close" is held to a strict bar on sites with recent incidents.

## Target Customer
Remote-guarding providers and central stations running 10,000+ cameras, and the monitoring-software vendors who could ship it as a feature.

## Impact If Built
Operators handle more cameras each without missing real events, which is the cost per camera the niche is contested on, and their judgement becomes an asset of the provider rather than of each individual.
