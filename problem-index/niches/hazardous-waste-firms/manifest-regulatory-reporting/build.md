# A Biennial Report Compiled From e-Manifest and Reconciled Before Filing

**Niche:** [[niches/hazardous-waste-firms/manifest-regulatory-reporting/profile|e-Manifest & Generator Regulatory Reporting]]
**Industry:** [[industries/hazardous-waste-firms|Hazardous Waste Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every shipment a large generator reports in its Biennial Report is already in e-Manifest, and the report is still typed from spreadsheets that disagree with it.
**Tags:** #large-language-models #descriptive-statistics #data-integration #compliance #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to produce a generator's regulatory filings straight from its manifest record, and whoever files Biennial and exception reports that match e-Manifest with the fewest state corrections takes the account.

## The Problem
The Biennial Report describes each waste stream generated and shipped, with source, form and management-method codes and quantities. States compare it with what receiving facilities report. Mismatches mean correction requests and, for repeat errors, attention.

## Why Nobody Has Built This
Until the third rule, many generators had no e-Manifest account and received paper copies; the report modules in EHS platforms were built for keyed data; and the code fields come from receiving facilities' records that generators rarely see.

## What to Build
A compiler that pulls the generator's manifests from e-Manifest, groups lines into streams by profile, fills source, form and management-method codes from the receiving facility's data, adds on-site management the generator records, flags quantities that disagree with the generator's own logs, and outputs the state's filing format.

## Target Customer
EHS reporting managers at generators with several large-generator sites, and consultants who file for clients.

## Impact If Built
Cutting report preparation by ~60% on ~40–80 hours per large-generator site (estimate) saves ~1,000 hours a cycle for a 30-site generator, and cuts state correction requests on the 2028 cycle.
