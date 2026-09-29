# Change Management From Software Release Engineering

**Niche:** [[niches/game-liveops-services/remote-configuration-safety/profile|Remote Configuration Safety]]
**Industry:** [[industries/game-liveops-services|Game LiveOps Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Software learned to stage, review, monitor and roll back every change to production, and game configuration skips all of it.
**Tags:** #workflow-orchestration #automation #data-integration #compliance #evaluation-metrics #change-point-detection #graph-theory #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to tell someone what a configuration value actually reaches before they change it in a live game — and whoever maps the blast radius takes the account.

## The Problem
Software release engineering built a complete answer to the problem of changing a running system: version control, review proportional to risk, automated validation, progressive delivery by percentage, automatic monitoring with rollback triggers, and a change record joined to incidents. Remote configuration in live games has identical power to change production behaviour and almost none of these controls, because it was classified as data rather than as a deployment.

## What Already Exists
Progressive delivery and percentage rollouts; automated pre-deployment validation; review policies scaled to risk; automatic rollback on metric regression; and change records linked to incidents.

## The Customization Gap
The adaptation is to a change made by a designer rather than an engineer, against a game economy rather than a service. It requires: (1) an operator who is a designer working at speed, so the controls must not feel like a deployment pipeline — the tooling has to be as fast as the console it replaces, which is the substantive difference; (2) impact measured in game economy and player experience rather than in error rates and latency, which needs an entirely different monitoring set; (3) a dependency graph from configuration keys into game code, which has no direct analogue in service deployment; (4) changes that are frequently intentional economy interventions rather than fixes, so the rollback criteria are ambiguous; and (5) a player base that notices and discusses every change publicly, adding a reputational dimension deployment tooling has never had to handle.

## Target Customer
Live game operators, live ops platform vendors, platform engineering teams, and progressive delivery vendors.

## Impact If Solved
Release engineering solved changing a running system and configuration was exempted by classification. Being fast enough for a designer, and monitoring economy rather than latency, is what the borrowed pipeline does not provide.
