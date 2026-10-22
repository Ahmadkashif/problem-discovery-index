# Drill Targets Ranked Against Holes Already Drilled

**Niche:** [[niches/geophysical-survey-firms/junior-mining-exploration-geophysics/profile|Junior Mining Exploration Geophysics]]
**Industry:** [[industries/geophysical-survey-firms|Geophysical Survey Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Geophysical firms have picked thousands of drill targets for juniors and almost never learn which ones hit, even though the results are disclosed publicly in drill-result press releases.
**Tags:** #tacit-knowledge-ml #gradient-boosting #bayesian-inference #feature-engineering #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn a ground or airborne survey into a ranked drill-target list that a junior explorer's board will fund and its qualified person will sign, and whoever's targets hit mineralisation most often keeps the claim-holder's next season.

## The Problem
An interpreter ranks a dozen anomalies — a chargeability high flanking a resistivity low, a magnetic break along a fault — and the junior drills the top three. The holes report assays months later. The interpreter's firm hears about it, if at all, from the news. Over a career, an experienced exploration geophysicist develops a sense of which anomaly styles carry mineralisation in which deposit models; that sense is never scored.

## Why Nobody Has Built This
The drill results belong to the junior; joining a disclosed hole to the specific anomaly it tested requires reading press releases and technical reports and matching coordinates; and survey firms move on to the next client.

## What to Build
A targeting record that stores each ranked anomaly with its geophysical character, the deposit model, and the interpreter's confidence, then harvests drill-hole outcomes from public disclosures and technical reports where coordinates allow, and from clients by agreement. Models learn which anomaly characteristics predicted mineralised intercepts by deposit type and terrain, and future target lists carry a calibrated hit probability alongside the interpreter's rank.

## Target Customer
Exploration geophysics consultancies and survey firms serving juniors, and juniors choosing between interpretation proposals.

## Impact If Built
A junior with one season's money gets targets with a track record behind them, and the firm that shows its hit rate wins the next claim-holder.
