# A Graph With a Published Coverage Figure

**Niche:** [[niches/crm-platforms/activity-graph-capture/profile|Activity Graph Capture]]
**Industry:** [[industries/crm-platforms|CRM Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every behavioural forecast, multi-threading metric and coverage analysis rests on the engagement graph, and no vendor states what proportion of real interactions their graph actually contains.
**Tags:** #graph-theory #bert #k-nearest-neighbors #evaluation-metrics #confidence-intervals #hypothesis-testing #data-integration #automation
**Contested on:** Every serious competitor in activity capture is fighting to reconstruct a complete, correctly attributed engagement graph from email and calendar without asking a representative to do anything — and whoever holds coverage and attribution accuracy highest takes the account.

## The Problem
A dashboard reports that a deal has three contacts engaged on the buying side and that engagement has declined. In fact there are seven, four of whom correspond with the representative from addresses the system never matched to the account, and engagement has risen. Every conclusion drawn from the graph — the forecast, the risk flag, the coverage gap, the multi-threading score — inherits the error, and nothing in any interface indicates that the graph is incomplete. The organisation makes decisions on a measurement whose accuracy is not merely unpublished but uncomputed.

## Why Nobody Has Built This
Coverage is measurable — a sampled audit of actual mailbox contents against the captured graph gives an honest figure — and publishing it means publishing a number below 100%, which no vendor wants to do first in a market where competitors claim completeness by implication. Internally the resolution failures are invisible: an unmatched email is silently dropped rather than queued, so the product's own telemetry shows successful processing. And customers have not asked, because the idea that the graph might be substantially incomplete does not occur to someone looking at a populated dashboard.

## What to Build
A resolution layer that reports its own quality. Contact resolution uses the full available signal — email domain, name matching, signature parsing, calendar co-attendance, corporate hierarchy data and prior confirmed matches — and returns a confidence rather than a binary match. Unmatched and low-confidence interactions go to a queue rather than to nothing, and a single representative confirmation resolves a contact permanently, which is the cheapest possible labelling loop and is currently absent. Deal attribution is modelled rather than assumed, using timing, participants and content relative to the account's open opportunities, with the ambiguous cases marked as such rather than assigned. And the headline output is a coverage and accuracy figure per account and per period, computed against periodic sampled audits, shown in the product. A vendor that publishes coverage takes a short-term hit and gains the only defensible claim in a category where everyone's dashboards look equally full.

## Target Customer
Activity capture and revenue intelligence vendors, CRM incumbents whose native capture is the default, and the revenue operations teams building forecasts on a graph of unknown completeness.

## Impact If Built
Every downstream capability in this industry — behavioural forecasting above all — is limited by the graph beneath it, and the graph's quality is currently unknown to everyone including its builders. Publishing coverage changes what customers can compare on, and the confirmation queue converts silent failures into a resolvable backlog at the cost of seconds of representative attention.
