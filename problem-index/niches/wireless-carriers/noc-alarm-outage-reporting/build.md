# Topology-Aware Alarm-to-Incident Correlation

**Niche:** [[niches/wireless-carriers/noc-alarm-outage-reporting/profile|NOC Alarm Correlation & Outage Reporting]]
**Industry:** [[industries/wireless-carriers|Wireless Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** When a fibre ring or a power feed fails, the NOC sees thousands of alarms across radio, transport and power, and finding the one root event still depends on which operator is on shift.
**Tags:** #graph-neural-networks #transformers #hidden-markov-models #evaluation-metrics #automation #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to turn a flood of network alarms into the handful of incidents that need action, with a cause attached, fast enough to restore service and file the FCC outage report on time, and whoever gives the shortest time from first alarm to correct incident takes the network-operations contract.

## The Problem
Correlation rules group alarms by site and time window and by hard-coded parent-child relations. Real topology (which sites hang off which transport ring, which share a power feed, which microwave hop depends on which) changes constantly and lives in inventory systems that are rarely current. Experienced operators recognise the patterns; rules don't.

## Why Nobody Has Built This
Each vendor correlates within its own domain. Cross-domain correlation needs an accurate topology graph, which nobody owns, and historical incidents with confirmed root causes, which are recorded loosely in tickets.

## What to Build
A model that learns alarm sequences over the inferred network graph, recovering topology from co-occurring alarms where inventory is wrong. It groups alarms into incidents, ranks probable root causes, estimates affected users and sites, and learns from operators' confirmations. Output goes straight into the ticketing system as one incident with a cause and a scope.

## Target Customer
Heads of network operations at national and regional carriers.

## Impact If Built
Minutes saved per major incident, fewer duplicate dispatches, accurate outage scope, and a NOC that performs the same on every shift.
