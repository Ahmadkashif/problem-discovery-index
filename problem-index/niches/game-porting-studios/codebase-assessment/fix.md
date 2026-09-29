# The Engine That Was Not Standard After All

**Niche:** [[niches/game-porting-studios/codebase-assessment/profile|Codebase Assessment]]
**Industry:** [[industries/game-porting-studios|Game Porting Studios]]
**Type:** Fix (Pain Point)
**One-liner:** The quote assumed a standard engine version and the client had rewritten the renderer two years ago.
**Tags:** #quick-win #descriptive-statistics #evaluation-metrics #automation #data-integration #confidence-intervals #workflow-orchestration #graph-theory
**Contested on:** Every serious competitor in this niche is fighting to measure the properties of an unfamiliar game codebase that determine how hard it will be to port — and whoever builds that scanner takes the account.

## The Problem
The most expensive surprise in porting is discovering that an engine described as standard has been heavily modified. A custom renderer, a replaced asset pipeline, engine source changes that will not survive an upgrade, middleware swapped for something bespoke. The quote assumed the engine's normal platform support would apply. It does not, and the work multiplies. The client usually did not mention it because to them it is simply how their game works.

## Why It's Still Broken
Nobody asks the question precisely enough — a client asked whether they use a standard engine will answer yes in good faith, because the modifications are invisible to them as modifications. Diffing against the stock engine requires source access. The assumption is buried in the quote rather than stated. And the discovery happens after signature.

## What a Fix Looks Like
Ask the measurable question and state the assumption out loud. Diff the client's engine against the stock version at the stated release, which is the fix and takes hours where it is possible at all. Ask specifically about renderer, asset pipeline and engine source modification rather than about the engine generally, since the general question reliably returns the wrong answer. State the engine assumption explicitly in the quote as a condition, which converts a surprise into a variation. Request the project and build files even where full source is unavailable, as they reveal a great deal. Check middleware versions against target platform support, which is a lookup and frequently decides the project. Ask whether the engine can be upgraded, because an unupgradeable fork changes everything downstream. Keep a checklist of the specific divergences that have cost money before, which is the cheapest institutional memory available. Price a paid assessment phase where access is refused, which is the honest response to an information asymmetry. Record what was found against what was quoted, so the checklist improves. And walk away from projects where the assumption cannot be checked at all, which is a commercial discipline rather than a technical one.

## Who Feels the Pain
Studios absorbing a multiplied scope; engineers handed a codebase nobody assessed; producers defending a date built on a false premise; and clients who answered honestly and are now in a dispute.

## Impact If Fixed
A client asked whether they use a standard engine will answer yes in good faith, because the modifications are invisible to them as modifications. Diffing against the stock engine and stating the assumption in the quote turns the surprise into a variation.
