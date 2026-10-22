# Redline Pickup That Reads the Clouds

**Niche:** [[niches/architecture-firms/cd-production-sheet-coordination/profile|Construction Document Production & Sheet Coordination]]
**Industry:** [[industries/architecture-firms|Architecture Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A principal's QA/QC review produces hundreds of clouds, and a junior staff member picks them up one by one, guessing at the handwriting.
**Tags:** #cnns #object-detection #large-language-models #transformers #worker-facing #automation #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to cut the hours between a design-development model and an issued, internally consistent construction set, and whoever eliminates schedule, tag and cross-reference errors without adding a new authoring tool takes the account.

## The Problem
After review, the marked-up set returns to the production team. Each cloud must be read, understood, located in the model, fixed and checked off. Some are drafting fixes, some coordination questions for consultants, some design decisions for the project architect. Misread or missed redlines reappear in the issued set.

## Why Nobody Has Built This
Markups are free-form — handwriting on scanned paper, Bluebeam clouds with shorthand — and linking a cloud on a PDF sheet back to the model element it concerns requires reading both drawings and text, which only recent vision-language models do well.

## What to Build
A pickup assistant that reads every markup in a reviewed set, transcribes and classifies it (drafting fix, coordination, design question, code), links it to the model element or sheet object, proposes the edit for routine drafting fixes, routes the rest to the right person, and produces a pickup log showing every cloud resolved — which also becomes labelled data on what reviewers flag.

## Target Customer
BIM managers and technical directors at firms of 20+ staff with formal QA/QC reviews.

## Impact If Built
Pickup time cut by more than half, missed redlines eliminated, and the review history captured for the firm's QA/QC programme.
