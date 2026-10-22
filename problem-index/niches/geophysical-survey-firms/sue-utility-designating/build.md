# A Test-Hole Scorecard for Every Designating Crew

**Niche:** [[niches/geophysical-survey-firms/sue-utility-designating/profile|Subsurface Utility Designating (QL-B)]]
**Industry:** [[industries/geophysical-survey-firms|Geophysical Survey Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every QL-A test hole is a free audit of a QL-B designation, and no SUE provider keeps a running record of how far its geophysical lines were from where the pipes actually were.
**Tags:** #gradient-boosting #gaussian-processes #confidence-intervals #evaluation-metrics #feature-engineering #tacit-knowledge-ml #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to deliver QL-B utility designations that hold up when the QL-A test holes are dug, on the DOT's design schedule, and whoever's lines survive excavation most often keeps the on-call contract.

## The Problem
On a designated corridor, the designer orders QL-A test holes where conflicts matter. Each hole exposes a utility and records its measured position and depth. That measurement is compared with the QL-B line only informally — a note that the line was "two feet off" — and filed in the project. Across hundreds of projects, a firm cannot say how accurate its designating is by method, utility type, soil, depth, congestion or crew.

## Why Nobody Has Built This
Test-hole sheets arrive as PDFs or field forms from a vacuum-excavation crew, sometimes a different subcontractor; matching each hole to the designated line it tests is spatial work no one budgets; and an honest accuracy record is uncomfortable for a firm whose liability insurer would like to see it.

## What to Build
Ingest test-hole records, match each to the designated utility it exposes, and store horizontal and vertical offsets with the conditions — method used, utility material and diameter, depth, soil, congestion, crew and interpreter. Fit models of expected offset by condition and publish confidence bands for future designations, so the plans can show a realistic tolerance rather than a single line. Use the same record to train interpreters on their own misses.

## Target Customer
SUE practice leaders at engineering firms and geophysical subcontractors bidding DOT on-call contracts.

## Impact If Built
A provider that can show a DOT its verified accuracy by condition wins on evidence, prices congested corridors honestly, and fixes the crews and methods that drive redesigns and strikes.
