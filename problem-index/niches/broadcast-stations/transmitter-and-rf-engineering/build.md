# Alarm Triage That Knows Each Site's History

**Niche:** [[niches/broadcast-stations/transmitter-and-rf-engineering/profile|Transmitter, Tower & RF Engineering]]
**Industry:** [[industries/broadcast-stations|Broadcast TV & Radio Stations]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The remote control pages the engineer on thresholds, and only the engineer knows whether this rise in reflected power at this site means ice on the antenna, a failing line or nothing.
**Tags:** #tacit-knowledge-ml #autoencoders #change-point-detection #time-series-forecasting #large-language-models #worker-facing #automation
**Contested on:** Every serious competitor in this niche (contract engineering firms, remote-control and transmitter-monitoring vendors, and the groups' own engineering departments) is fighting to keep each licensed transmitter on the air and within its FCC parameters with fewer engineer hours per site, and whoever keeps the most sites legal and on air per engineer takes the account.

## The Problem
Threshold alarms fire on symptoms. An engineer covering several sites decides from a phone, often at night, whether to drive out. That decision rests on years of watching one transmitter, and the readings that preceded past failures are rarely written down.

## Why Nobody Has Built This
Remote-control and transmitter vendors each see their own equipment, and few groups centralise telemetry. Labelled failures are rare per site. Engineers are sceptical of tools that have not seen their plant.

## What to Build
A cross-vendor monitoring layer that learns each site's normal multivariate behaviour across seasons and loads, ranks alarms by how unusual they are for that site, and matches the pattern to the site's past incidents. Each incident ends with a one-line diagnosis from the engineer, which becomes the site's history and the model's labels. A backup engineer sees the same history.

## Target Customer
Group directors of engineering, contract engineering firms and public broadcasters with one or two engineers.

## Impact If Built
Fewer wasted site visits, earlier fixes for failures that would take a station off the air, and site knowledge that survives a retirement. Each engineer can then cover more sites safely.
