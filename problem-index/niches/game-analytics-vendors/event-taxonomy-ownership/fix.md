# Four Events That Mean the Same Thing

**Niche:** [[niches/game-analytics-vendors/event-taxonomy-ownership/profile|Event Taxonomy Ownership]]
**Industry:** [[industries/game-analytics-vendors|Game Analytics Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Level completion is recorded by four differently named events added by four people across three years.
**Tags:** #quick-win #data-integration #descriptive-statistics #evaluation-metrics #automation #sets-and-logic #workflow-orchestration #compliance
**Contested on:** Every serious competitor in this niche is fighting to keep an event schema coherent as a game changes for years, when the schema was designed early by whoever was available and nobody owns it — and whoever takes ownership takes the account.

## The Problem
The same action gets instrumented repeatedly. Someone adds an event, a year later someone else needs the same thing and cannot find it, so they add another with a different name and slightly different parameters. Now an analysis must know that all four exist, and any analyst who knows about three of them produces a number that is quietly wrong. This accumulates for the life of the game.

## Why It's Still Broken
There is nowhere to look — an engineer who cannot discover whether an event already exists will create a new one, every time, and the duplication is invisible until an analysis disagrees with another. No review catches it. Names are chosen locally. And nobody audits the event list.

## What a Fix Looks Like
Audit the events you have and make them discoverable. Produce an inventory of every event actually firing, with volume and last-seen date, which is the fix and usually surprises everyone involved. Cluster events by name, parameters and firing context to surface likely duplicates, since the pattern is obvious once anyone looks. Document what each event means in one line, which is the cheapest thing that prevents the next duplicate. Make the inventory searchable by the engineers who instrument, as discoverability is the actual cause. Mark canonical events where duplicates exist so analyses agree with each other. Retire events nobody consumes, which is a large share of any mature schema. Check for an existing event as a step in the instrumentation process. Flag events that stopped firing, which frequently indicates a break nobody noticed. Publish the inventory rather than keeping it in a data team's folder. And run the audit annually rather than once.

## Who Feels the Pain
Analysts producing numbers that disagree; engineers instrumenting what already exists; studios acting on a metric that counted three of four events; and the data team defending numbers they cannot fully explain.

## Impact If Fixed
An engineer who cannot discover whether an event already exists will create a new one, every time, and the duplication is invisible until two analyses disagree. A searchable inventory with one-line definitions stops the next one.
