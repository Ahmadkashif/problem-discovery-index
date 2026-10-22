# Production Tracking Extended to Bid Reconciliation

**Niche:** [[niches/postproduction-studios/feature-episodic-vfx/profile|Feature & Episodic VFX]]
**Industry:** [[industries/postproduction-studios|Postproduction Studios]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Every VFX vendor already logs artist time per shot in Flow Production Tracking or ftrack; neither tool was built to grade the bid that priced the shot.
**Tags:** #gradient-boosting #feature-engineering #evaluation-metrics #descriptive-statistics #data-integration #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is "every serious competitor is fighting to price shot packages on fixed bids accurately enough to win the award and still make money," but the winners differ: tentpole feature packages are won by whoever can commit hundreds of artists under a trusted supervisor in the richest incentive jurisdiction, while episodic and invisible-effects work is won by whoever turns around high shot counts at a known cost per shot inside a weekly schedule. Decomposed into contested sub-niches below.

## The Problem
Vendors hold years of shot-level actuals: hours by department, version counts, note dates. Bid reviews still rely on producers' memories, because the bid sits in a spreadsheet and the actuals sit in a tracker with its own fields and naming.

## What Already Exists
Autodesk Flow Production Tracking (formerly ShotGrid) and ftrack hold shots, tasks, versions, time logs and bid-day fields; both have APIs and reporting. Finance systems hold invoices.

## The Customization Gap
The adaptation needs: bid lines imported with their category, department split and assumptions, not just a total; actuals split into work before first client approval and work after scope-changing notes; normalisation for artist seniority and site rate; bid accuracy reported by shot type, client, supervisor and show phase; and a view a producer can use mid-bid ("our last five creature shots for this studio ran 40% over"). The trackers' generic dashboards report utilisation, not bid error.

## Target Customer
VFX producers and finance leads at vendors already running Flow Production Tracking or ftrack, who want bid analytics without replacing the tracker.

## Impact If Solved
Producers stop repeating the same underbid on the same shot types. A vendor that cuts overruns on its worst shot category by a quarter recovers most of a typical episodic package's margin (estimate).
