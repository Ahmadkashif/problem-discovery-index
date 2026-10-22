# IT Asset Discovery Extended to Analog Lines

**Niche:** [[niches/telecom-resellers/pots-line-replacement/profile|Legacy POTS Line Replacement]]
**Industry:** [[industries/telecom-resellers|Telecom Resellers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** IT asset management tools keep a live inventory of every networked device a company owns, and the copper lines behind its alarms and elevators fall outside them because they have no IP address.
**Tags:** #k-means-clustering #feature-engineering #descriptive-statistics #data-integration #compliance #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to inventory every copper line at a multi-site customer and replace each with a service that passes the attached device's own test (fire-alarm signalling, the elevator emergency phone, the fax), and whoever certifies each line working takes the portfolio.

## The Problem
A multi-site customer's IT team can list every laptop, switch and access point, but not the 2,000 analogue lines in its stores. The lines are paid by facilities from telco invoices, maintained by alarm and elevator contractors, and owned by nobody in IT.

## What Already Exists
IT asset management and network discovery platforms that scan networks, reconcile devices with purchase records and contracts, and keep a configuration database.

## The Customization Gap
An asset model for lines rather than devices: number, site, carrier, monthly cost, inferred purpose, attached device and its maintaining contractor, the local inspection regime, and replacement status. Data comes in from bills, CSRs and call records instead of network scans. The record must carry evidence that a replacement passed its device test (central-station signal received, elevator phone answered) and when the next inspection falls, and sites must be grouped into migration waves by telco retirement dates.

## Target Customer
Facilities and telecom managers at multi-site customers, and the resellers who want the inventory to be the start of their replacement project.

## Impact If Solved
Lines join the asset register the business already trusts, migrations are planned from data instead of site walks, and inspection evidence lives in one place.
