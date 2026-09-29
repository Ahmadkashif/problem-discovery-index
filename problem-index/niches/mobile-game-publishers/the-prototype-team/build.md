# Feedback Instead of a Verdict

**Niche:** [[niches/mobile-game-publishers/the-prototype-team/profile|The Prototype Team]]
**Industry:** [[industries/mobile-game-publishers|Mobile Game Publishers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A team is told no thirty times a year and never told why in terms it can act on.
**Tags:** #worker-facing #evaluation-metrics #descriptive-statistics #confidence-intervals #causal-inference #survival-analysis #automation #tacit-knowledge-ml
**Contested on:** Every serious competitor in this niche is fighting to give a team that is killed dozens of times a year some way to know whether any of the work was good — and whoever provides it takes the account.

## The Problem
The prototype funnel gives its builders one bit of information per attempt. A designer who has run thirty concepts has thirty bits and no model of what worked. They cannot tell whether a concept failed because the idea was wrong, the first ninety seconds were confusing, the test audience was mismatched, or the number was simply noisy at that sample size. Under those conditions nobody can improve, and the people who are best at this leave.

## Why Nobody Has Built This
The funnel is designed for portfolio throughput, not for individual development. The data to diagnose a failure exists but is only ever reduced to the pass metric. Nobody owns the team's craft development. And the industry treats attrition in these roles as normal.

## What to Build
Return a diagnosis with every kill. Produce a structured failure diagnosis from the test telemetry — where players left, what they did not reach, which of the concept's intended mechanics were engaged — which is the core and turns one bit into something a designer can act on. Separate concept from execution where the data permits, since a good idea with a bad first session is a completely different lesson from a weak loop. Report the statistical confidence of the kill, because a number that close to the threshold on that sample size does not mean what the verdict implies and designers know it. Compare the concept against the team's own prior attempts rather than against a universal threshold, which is where a sense of improvement can come from. Keep a designer-level record of contributions and outcomes across attempts, as none exists and careers are built on assertion. Identify which of a designer's concepts were near-misses, since those are the strongest evidence of craft. Aggregate patterns across the team's history so recurring mistakes become visible. Deliver the diagnosis quickly, while the work is still in mind. Write it in design language rather than in analytics language. And distinguish clearly between the concept being rejected and the person being judged, which is the thing the current process does worst.

## Target Customer
Mobile publishers, hypercasual and hybridcasual studios, game design teams, and games talent and development vendors.

## Impact If Built
Thirty attempts yielding thirty bits of information is not a learning environment, and the people best at this leave it. A structured failure diagnosis from telemetry the publisher already holds turns a verdict into craft development.
