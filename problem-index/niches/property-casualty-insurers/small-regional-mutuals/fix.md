# Exposure Data Too Thin for the Cat Model

**Niche:** [[niches/property-casualty-insurers/small-regional-mutuals/profile|Small & Regional Mutual Insurers]]
**Industry:** [[industries/property-casualty-insurers|Property & Casualty Insurers]]
**Type:** Fix (Pain Point)
**One-liner:** Missing roof ages and construction types make the reinsurance broker's cat model assume the worst, and the mutual pays for its data gaps at every renewal.
**Tags:** #cnns #k-nearest-neighbors #data-integration #feature-engineering #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to give a mutual with no data-science staff a pricing and catastrophe view its regulator and reinsurer will accept, and whoever turns bureau loss costs, cat models and the mutual's own thin experience into a filed rate change before the reinsurance renewal takes the account.

## The Problem
Catastrophe models price unknown attributes conservatively. A mutual whose policy records lack year built, roof age, roof material or construction class gets modelled losses, and reinsurance quotes, above what its real book deserves.

## Why It's Still Broken
The data was never captured at application, inspections are expensive, and nobody at the mutual owns exposure data quality between renewals.

## What a Fix Looks Like
Fill and verify missing attributes from property records and aerial imagery. Flag policies where the record contradicts the evidence, and produce a cleaned exposure file with confidence levels before the broker's renewal submission deadline.

## Who Feels the Pain
CFOs negotiating reinsurance, underwriters rating on wrong data, and policyholders paying for both.

## Impact If Fixed
Lower modelled loss and reinsurance cost from better data alone, and rating that matches the property.
