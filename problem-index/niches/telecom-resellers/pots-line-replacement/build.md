# Line-to-Device Discovery Across a Site Portfolio

**Niche:** [[niches/telecom-resellers/pots-line-replacement/profile|Legacy POTS Line Replacement]]
**Industry:** [[industries/telecom-resellers|Telecom Resellers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A retailer with 400 stores pays for 2,000 copper lines and can't say which one serves the fire panel in store 212, so every replacement project starts with a truck roll to find out.
**Tags:** #gradient-boosting #k-means-clustering #feature-engineering #large-language-models #automation #compliance
**Contested on:** Every serious competitor in this niche is fighting to inventory every copper line at a multi-site customer and replace each with a service that passes the attached device's own test (fire-alarm signalling, the elevator emergency phone, the fax), and whoever certifies each line working takes the portfolio.

## The Problem
Multi-site businesses accumulated copper lines over decades. Bills list numbers and addresses, not purposes. Some lines are dead and still billed, some serve devices nobody remembers, and a few carry life-safety signals. Replacing a line without knowing what it serves risks a silent alarm or a failed elevator inspection. Leaving it risks a sudden disconnect when the telco retires the wire center.

## Why Nobody Has Built This
Analog lines have no IP address to scan. The evidence of what a line does is indirect: who it calls, when, and for how long. That evidence sits in the losing carrier's call records, which resellers rarely request. The market grew fast and sells devices, so nobody built the discovery step.

## What to Build
A classifier that infers each line's purpose from its call pattern before any site visit. Alarm communicators call a central station's receiver numbers at regular test intervals with very short calls. Elevator phones rarely call out, and when they do it is to a monitoring centre. Fax lines show fax-length calls to varied numbers. Dial-up payment terminals show bursts at business hours. Unused lines show nothing. The classifier combines CSRs, call detail and bill data, ranks lines by risk, and generates a site-by-site survey list so the technician confirms rather than discovers.

## Target Customer
POTS-replacement resellers selling to multi-site retail, banking, property and education customers, and those customers' facilities and telecom managers.

## Impact If Built
Fewer site visits, dead lines cancelled immediately, and life-safety lines identified and protected before cut-over instead of found afterwards.
