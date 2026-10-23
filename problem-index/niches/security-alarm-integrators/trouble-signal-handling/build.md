# Outage Clusters and Self-Restoring Troubles Recognised Automatically

**Niche:** [[niches/security-alarm-integrators/trouble-signal-handling/profile|Central-Station Trouble & Supervisory Signal Handling]]
**Industry:** [[industries/security-alarm-integrators|Security Alarm Integrators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** When a feeder trips or a wire centre loses copper, thousands of panels report the same trouble, and the station works them one phone call at a time.
**Tags:** #change-point-detection #dbscan #random-forests #time-series-forecasting #feature-engineering #automation #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to clear the supervisory and trouble signals that make up most of a station's traffic without an operator touching them, while missing no fire or life-safety trouble, and whoever handles the most signals per operator hour within UL 827 rules takes the account.

## The Problem
AC-loss and communication-failure troubles arrive in bursts that share a cause: a utility outage, a carrier fault, a cellular tower down, a copper retirement. Most restore on their own. Operators can't see the cluster from inside the queue and can't tell which individual trouble is real, such as a fire panel's communicator that has actually failed.

## Why Nobody Has Built This
Automation platforms process signals per account, and their rules are static delays. Geography and external outage data aren't in the platform. Stations tune rules by experience, and the people who know which troubles self-restore are the senior operators.

## What to Build
Spatio-temporal clustering of trouble bursts with change-point detection on regional signal rates, joined to utility outage feeds, carrier notices and weather. Each cluster is held as one event and auto-restored. A per-signal classifier predicts self-restoration within a window from device type, history and cluster membership. Life-safety accounts are excluded from suppression and escalated if the restore doesn't come.

## Target Customer
Monitoring-operations leaders at wholesale and proprietary stations with 100,000+ accounts, and the automation-platform vendors.

## Impact If Built
Storm nights become manageable, operator hours shift to alarms and real troubles, and the station's cost per account falls, which is the basis on which wholesale stations compete.
