# Product Analytics From SaaS

**Niche:** [[niches/indie-game-studios/playtest-and-demo-instrumentation/profile|Playtest & Demo Instrumentation]]
**Industry:** [[industries/indie-game-studios|Indie Game Studios]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** SaaS product analytics made funnels, cohorts and drop-off standard practice, and indie studios ship demos with no instrumentation at all.
**Tags:** #data-integration #automation #evaluation-metrics #descriptive-statistics #k-means-clustering #survival-analysis #confidence-intervals #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to turn a playtest or a demo into a machine-readable account of where players stopped enjoying the game — and whoever does it best takes the account.

## The Problem
Product analytics solved the equivalent problem for software: instrument events, build a funnel, find the step where people leave, cohort by version, and know whether a change helped. It became standard practice because the tooling made it cheap. A game demo is a product experience with a funnel and a drop-off point, and the studios shipping them have none of this — not because it does not apply but because nobody packaged it for a game build.

## What Already Exists
Event instrumentation SDKs; funnel and drop-off analysis; cohort comparison across versions; session replay concepts; and retention curves.

## The Customization Gap
The adaptation is to a real-time interactive build rather than a web session, and to a pre-revenue outcome. It requires: (1) engine-level integration for Unity, Unreal and Godot rather than a web or mobile SDK — the integration surface is the practical barrier and is what has kept generic tools out; (2) a session model built on game state, area and progression rather than page and click; (3) offline-capable buffering, since a game session is not a connected web session; (4) wishlist conversion as the outcome rather than a purchase or a subscription, which is the metric the studio actually needs; and (5) reporting in design vocabulary — pacing, difficulty, area — rather than in analytics vocabulary, which determines whether a designer uses it.

## Target Customer
Indie studios, publishers, user research services, and product analytics vendors seeking a vertical.

## Impact If Solved
Product analytics made funnels standard because the tooling made them cheap. Engine-level integration and a game-state session model are the adaptation; wishlist conversion as the outcome is what makes it worth buying.
