# Four Hundred Recordings and No Idea What to Test

**Niche:** [[niches/conversion-optimization-firms/hypothesis-generation/profile|Hypothesis Generation]]
**Industry:** [[industries/conversion-optimization-firms|Conversion Optimization Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The strategist has watched thirty session recordings and has thirty observations and no hypothesis.
**Tags:** #quick-win #descriptive-statistics #k-means-clustering #evaluation-metrics #confidence-intervals #change-point-detection #automation #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to tell which of an endless supply of observations describes a mechanism worth testing — and whoever makes that selection takes the account.

## The Problem
Watching session recordings is absorbing and unproductive. Each session shows a person doing something slightly odd, and the oddness is usually idiosyncratic. Thirty sessions produce thirty observations and no pattern, because the pattern would only be visible across thousands and the strategist is sampling by hand. The time is spent, the tool is being used, and the output is a list of things somebody noticed.

## Why It's Still Broken
Recordings are watched individually — a pattern that exists across thousands of sessions cannot be seen by watching thirty, and the tool's interface invites exactly that. Quantitative and qualitative tools are separate. Nobody aggregates. And watching feels like research.

## What a Fix Looks Like
Find the pattern quantitatively and use the recordings to understand it. Start from the funnel data to locate where users are lost, which is the fix and points the qualitative work at somewhere specific. Watch recordings of the specific failure rather than a random sample, which turns thirty sessions from a survey into an investigation. Quantify how many sessions show the behaviour before treating it as a finding, since that is the difference between an anecdote and a pattern. Use the platform's own segment filters to isolate the failing sessions rather than sampling everything. Count error occurrences, repeated actions and backtracking, which are countable and are usually where the mechanism is. Write the observation as a mechanism with a prediction before it enters the backlog. Estimate how many users the pattern affects, which determines whether a test could detect it. Record which observations became tests and which of those produced effects, so the selection improves. Timebox the recording watching, since it expands to fill whatever is available. And treat recordings as the explanation of a quantified pattern rather than as a source of patterns.

## Who Feels the Pain
Strategists spending days on unproductive watching; clients paying for observation rather than hypothesis; the backlog, filled with noticed oddities; and the test capacity, spent on idiosyncrasies.

## Impact If Fixed
A pattern that exists across thousands of sessions cannot be seen by watching thirty, and the interface invites exactly that. Locating the failure quantitatively first turns recording-watching into an investigation.
