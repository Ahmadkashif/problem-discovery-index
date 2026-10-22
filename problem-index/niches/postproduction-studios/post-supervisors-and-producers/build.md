# One Cost-to-Complete View Across Every Vendor

**Niche:** [[niches/postproduction-studios/post-supervisors-and-producers/profile|Post Supervisors & Post Producers]]
**Industry:** [[industries/postproduction-studios|Postproduction Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A post supervisor learns that the VFX budget is 15% over when the vendor's invoice arrives, because nothing joins six vendors' status into one forecast.
**Tags:** #time-series-forecasting #bayesian-inference #large-language-models #evaluation-metrics #data-integration #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to give the post supervisor one live view of every vendor's status, cost-to-complete and delivery risk across a show, without making each vendor re-key its data, and whoever does it takes the production.

## The Problem
A series' post budget is spread across editorial, finishing, three VFX vendors, sound, music and deliverables. Each vendor reports in its own format, weekly at best. The post supervisor maintains a cost report by hand for the studio's production finance team, and overruns appear late, when change orders and overages arrive together near delivery.

## Why Nobody Has Built This
Vendors guard their internal data and won't adopt a client's system for every show. The post supervisor is often a freelancer, so nobody buys software for a role that changes employer every season.

## What to Build
A supervisor-side workspace that ingests what vendors already send (status reports, bid and change-order PDFs, shot counts, invoices, review notes) and turns them into a single cost-to-complete and schedule forecast per vendor. Extraction is done by language models, and the forecast learns from how similar shows burned their budget over time. Studios can mandate it for their productions; the supervisor keeps their history from show to show.

## Target Customer
Post supervisors and post producers on scripted series and features; production finance at studios and streamers who receive their cost reports.

## Impact If Built
Overruns become visible weeks earlier, while there is still room to cut shots or renegotiate, and the weekly hand-built cost report goes away.
