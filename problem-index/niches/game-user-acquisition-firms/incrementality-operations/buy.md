# Experimentation Platforms From Product Engineering

**Niche:** [[niches/game-user-acquisition-firms/incrementality-operations/profile|Incrementality Operations]]
**Industry:** [[industries/game-user-acquisition-firms|Game User Acquisition Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Product engineering made running an experiment a routine self-service action, and marketing incrementality is a quarterly project.
**Tags:** #hypothesis-testing #causal-inference #confidence-intervals #evaluation-metrics #automation #workflow-orchestration #monte-carlo-methods #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to run incrementality tests often enough to know what their spend is actually buying, when each one is currently a project — and whoever makes them routine takes the account.

## The Problem
Product organisations made experimentation routine by building platforms: self-service test creation, automatic randomisation and assignment, power calculations before launch, guardrail metrics, automated readouts with correct statistics, and an accumulating archive of results. Teams run hundreds of experiments a year without a statistician involved in each. Marketing incrementality testing is methodologically similar and is run as a bespoke project.

## What Already Exists
Self-service experiment creation; automatic randomisation and assignment; pre-launch power calculation; automated statistical readout; and searchable experiment archives.

## The Customization Gap
The adaptation is to a treatment that is advertising exposure, which cannot be assigned directly. It requires: (1) randomisation over geographies or audiences rather than over users, since the platform controls who sees an ad and the advertiser does not — this is the substantive difference and forces designs with far less power; (2) a treatment delivered by a third party whose own optimisation interferes with the assignment; (3) outcomes accruing over months rather than within a session; (4) a holdout that costs real money in forgone spend rather than nothing; and (5) unit counts in the dozens of geographies rather than the millions of users.

## Target Customer
UA teams and agencies, mobile publishers, measurement vendors, and experimentation platform providers.

## Impact If Solved
Product engineering made experiments routine and self-service, and teams run hundreds a year. Randomising over geographies because the platform controls exposure, with a holdout that costs real money, is what the marketing version must handle.
