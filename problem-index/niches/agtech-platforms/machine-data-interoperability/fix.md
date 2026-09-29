# Field Boundaries That Disagree Between Systems

**Niche:** [[niches/agtech-platforms/machine-data-interoperability/profile|Machine Data Interoperability]]
**Industry:** [[industries/agtech-platforms|Agtech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The same field is 78 acres in one system, 81 in another and 79.4 on the lease, and every per-acre figure the farm computes — yield, cost, rent, programme payment — depends on which number was used.
**Tags:** #descriptive-statistics #numerical-methods #evaluation-metrics #confidence-intervals #compliance #data-integration #automation #quick-win
**Contested on:** Every serious competitor in mixed-fleet farm software is fighting to assemble one coherent field record from equipment of different brands — and whoever makes a mixed fleet's data reconcile without manual repair takes the account.

## The Problem
A field's boundary exists in the equipment manufacturer's platform, in the farm management system, in the crop insurance record, in the government programme record, in the landlord's lease and in the agronomist's system, and no two agree exactly. Some differences are trivial and some are not — a three-acre discrepancy on an eighty-acre field changes yield per acre by several percent, changes the cost per acre, changes what is owed on a per-acre lease and potentially changes a programme payment. Every analysis the farm performs rests on a denominator that is quietly inconsistent across the systems it came from.

## Why It's Still Broken
Boundaries were captured at different times by different methods — a GPS pass around the perimeter, a digitised aerial photograph, a surveyed legal description — and each is defensible. Nobody designated an authoritative source, so each system maintains its own, and when they disagree the person looking at a particular number does not know which lineage it came from. The differences are individually small enough to seem like rounding and collectively large enough to matter, which is the pattern of problems that persist indefinitely.

## What a Fix Looks Like
Designate one boundary and reconcile everything to it. The farm maintains a canonical boundary per field, chosen deliberately — typically the surveyed or programme boundary for legal and payment purposes, with the planted area recorded separately, since the planted acres and the field acres are genuinely different numbers and conflating them is a common error. Every other system's boundary is matched to it with the difference reported, so a discrepancy is a known quantity rather than an invisible one. Per-acre computations state which denominator they used. Boundary changes over time are versioned, since fields are split, combined and re-shaped and a historical yield figure should use the boundary in force that year. And the reconciliation report — which fields disagree, by how much, across which systems — is the standing artefact that lets the farm close the differences rather than rediscover them.

## Who Feels the Pain
Farm records managers reconciling acreage across systems every winter; growers comparing yields across years computed on different denominators; and landlords and tenants whose per-acre settlement depends on a number neither party has examined.

## Impact If Fixed
A canonical boundary is the foundational join for every other reconciliation in this niche and for every per-acre figure the farm produces. It costs a decision and a comparison, and the separation of planted acres from field acres alone corrects a recurring error in yield reporting that most operations do not know they have.
