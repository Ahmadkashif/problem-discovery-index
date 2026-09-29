# Separating the Video From the Algorithm

**Niche:** [[niches/creator-businesses/post-publication-attribution/profile|Post-Publication Attribution]]
**Industry:** [[industries/creator-businesses|Creator Businesses]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A video that underperformed may have been a bad video or may have been shown to the wrong first thousand people, and nothing in the data separates those.
**Tags:** #causal-inference #confidence-intervals #hypothesis-testing #evaluation-metrics #gradient-boosting #time-series-forecasting #monte-carlo-methods #k-nearest-neighbors
**Contested on:** Every serious competitor in this niche is fighting to separate what the creator did from what the recommendation system decided — and whoever can say what a video was actually responsible for replaces a decade of anecdote with evidence.

## The Problem
The result the creator sees is a product of two things: what they made and how the platform distributed it. The platform shows a new upload to a test audience, measures the response, and expands or withdraws distribution accordingly — so a weak start compounds into a weak result regardless of whether the content was good. The available analytics report the compounded outcome. A decade of professional expertise consists of people learning to read through this, tacitly, without ever being able to check.

## Why Nobody Has Built This
The mechanism is deliberately opaque, so separating its effect looked impossible rather than merely hard — and an inference problem widely believed to be unsolvable attracts no serious attempts. The platform has no incentive to expose the allocation. Creators lack the statistical apparatus and the tooling vendors lack the ambition. And the advice industry is profitable without it.

## What to Build
Model the distribution and subtract it. Model the early impression allocation from the traffic source and timing data the platform does expose, which is the core — the first hours' behaviour is the most informative signal available about what the algorithm decided. Construct a matched baseline from the creator's own comparable uploads, so the question becomes how this video did relative to what the channel would normally expect. Estimate the content effect as the residual, with honest uncertainty, since the residual is what the creator controls and it is what they are trying to learn about. Use the traffic source breakdown, because browse, suggested, search and external behave differently and separating them separates much of the confound. Detect the video that started weakly and never recovered versus the one that was distributed well and rejected, as those are opposite lessons and currently look identical. Pool across creators to estimate the platform's general behaviour, which no single channel can observe. Express variance explicitly so a single result is not over-read. Track the creator's own hypotheses and test them, which turns intuition into evidence. Identify which factors the creator actually controls, since effort spent on the rest is wasted. And publish the method, because the credibility of this claim rests entirely on being checkable.

## Target Customer
Creators and channel managers, management companies, creator analytics vendors, and the education industry built on anecdote.

## Impact If Built
An inference problem widely believed to be unsolvable attracts no serious attempts, so nobody tried. Modelling the early allocation and comparing against a matched baseline from the creator's own catalogue separates the two effects well enough to learn from.
