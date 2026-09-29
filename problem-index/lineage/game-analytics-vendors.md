# Lineage: Game Analytics Vendors

**Industry:** [[industries/game-analytics-vendors|Game Analytics Vendors]]
**Wave:** [[series/eras/wave-07-big-data|7 — Big Data]]
**The tool:** the GameAnalytics SDK and its fixed event types — business, resource, progression, error and ad events with pre-built dashboards, plus free-form "design" events named by a colon-separated hierarchy of up to five segments
**Builder:** GameAnalytics
**Builder in vault:** [[industries/game-analytics-vendors|Game Analytics Vendors]]
**Verification:** partial — see Sources

## The Problem That Came First

Mobile analytics arrived before game analytics, and it was built for apps.

Flurry, founded in 2005, became — in Wikipedia's account — a universal analytics platform for mobile apps that took off "with the advent of the iPhone," and after merging with Pinch Media held almost 80% of mobile analytics. The unit was the session and the custom event: how many users opened the app, how long they stayed, how often they tapped a named button.

A game needs a different vocabulary. A designer does not ask how long a session was. She asks **which level players quit on, what they spent soft currency on before they paid, and where on the map they died.** A generic tool can record all of that as custom events, but then every studio invents its own names, and nothing in the tool knows that "level_3_fail" and "L3:death" mean the same thing — or how to build a funnel from them.

## What Got Built

GameAnalytics, a Copenhagen start-up whose 2010 holding page promised "a comprehensive middleware solution for game- and userdata tracking, analysis, and reporting," for everyone "from the hobbyist to the VC funded social game developer," launching in Q1 2011.

By mid-2013 the product was a free SDK for Unity3D, Corona, Flash and iOS, a **Cohort tool** for retention, a **Funnels tool** for "where players are dropping off," and — inside the Unity editor — **3D heatmaps rendered over the level geometry in the Scene View**, so a designer saw deaths on the map she built.

The durable artefact is the event schema. Today's SDK sorts everything a game sends into typed buckets — business, resource, progression, error, ad — each with pre-populated KPI dashboards. What does not fit goes into **design events**, identified by "a colon-separated string of up to 5 segments that define the event hierarchy." The typing is what makes the product game-specific: progression is a first-class concept, not a string a studio happened to choose.

## Who Built It, And Why Them

A team that combined game development with academic data mining.

The 2012 site lists three founders — Morten Wulff (CEO), Matthias Flügge (CPO) and Dr Christian Thurau (CTO) — with Anders Drachen as lead game analyst and two data-mining and pattern-recognition academics, Kristian Kersting and Christian Bauckhage, as advisers. By 2013 Alessandro Canossa had joined as adviser on "advanced game metrics & spatial analysis." Michael Arrington invested via CrunchFund.

**The business case was the long tail.** Large publishers could afford an in-house telemetry team, as Microsoft's Halo testing lab showed. The thousands of small studios shipping on Unity and mobile could not, and a generic app analytics tool gave them sessions rather than levels. A free, game-typed SDK, pre-wired into the engine they already used, was a way to collect data across the long tail that no single studio held. The company describes itself as having launched in 2011 as "the first gaming-specific analytics platform," raised $2.5M in 2012, was acquired by Mobvista in 2016 and now claims over 100,000 games.

## What It Cost

**The fixed types answer the questions every game shares, and only those.** The events that would explain *why* retention fell in one particular game — a new boss, a changed tutorial — are exactly the ones that go into free-form design events. The documentation warns against "excessive unique nodes" there, and those events get no pre-built dashboard.

And the SDK records what the studio chose to send. The schema is written once, early, and nobody at the vendor owns it.

## What You Still Touch

A retention dashboard showing a Day-7 drop with no reason attached is the fixed taxonomy doing its job and reaching its limit.

- [[problems/game-analytics-vendors/high-impact|🔴 The Dashboard Shows the Drop and Cannot Say Why]]
- [[problems/game-analytics-vendors/low-impact-1|🟡 Instrumentation Nobody Owns]] — the schema the SDK cannot write for you
- [[niches/game-analytics-vendors/event-taxonomy-ownership/profile|Event Taxonomy Ownership]]
- [[niches/game-analytics-vendors/metric-movement-explanation/profile|Metric Movement Explanation]]

**Sources:** WebSearch was unavailable this session (session cap reached); research was by direct fetch. gameanalytics.com via the Wayback Machine: holding page Jan 2011 (© 2010; "launching our product in Q1 2011"), home page Sept 2012 (founders and team), About Us, Features and Unity Integration pages, July 2013 (Copenhagen; advisers; Cohort and Funnels tools; SDK platforms; Scene View 3D heatmaps); gameanalytics.com/about, current (2011 launch, "first gaming-specific analytics platform" — a company claim, not verified; $2.5M 2012; Mobvista 2016; 100,000+ games); docs.gameanalytics.com, *Design Events* (five-segment hierarchy, cardinality warning, event types, manual dashboards); Wikipedia, *Flurry (company)* (2005, iPhone take-off, Pinch Media, ~80% share). The reference to Microsoft's lab draws on this sweep's `lineage/player-research-firms.md`, vault material. ⚠️ **Not established:** when the current fixed event types and the five-segment design-event scheme were introduced — the 2013 pages mention custom events and an event structure but not these types, so they are described as today's SDK, not the 2011 one. Flurry's pivot date and the Pinch Media merger date were not given in the source read. The spelling Flügge (2012) versus "Matthias F. Hansen" (2013) for the same CPO is as the pages show it; I did not resolve it.
