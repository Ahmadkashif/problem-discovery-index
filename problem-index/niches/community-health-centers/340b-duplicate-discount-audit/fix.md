# Carve-In Elections That Contract Pharmacies Don't Follow

**Niche:** [[niches/community-health-centers/340b-duplicate-discount-audit/profile|Medicaid Duplicate-Discount Prevention & HRSA 340B Audit]]
**Industry:** [[industries/community-health-centers|Community Health Centers]]
**Type:** Fix (Pain Point)
**One-liner:** A health center tells HRSA it carves Medicaid out at its contract pharmacies, but a pharmacy keeps routing Medicaid managed care claims through 340B, and the duplicate discounts surface only at audit.
**Tags:** #change-point-detection #feature-engineering #data-integration #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to keep every 340B purchase defensible against diversion and Medicaid duplicate-discount findings, and whoever has the fewest adverse findings per HRSA 340B audit takes the account.

## The Problem
Carve elections differ for fee-for-service and managed care Medicaid, by state, and sometimes by plan. A plan change or a pharmacy software update can break the logic without anyone noticing.

## Why It's Still Broken
The election is recorded in HRSA's system and a spreadsheet. The pharmacy's billing logic is configured by the administrator, and nobody compares the two.

## What a Fix Looks Like
A monthly check of every contract pharmacy's Medicaid claims against the center's elections, with change-point alerts when a pharmacy's Medicaid 340B share jumps.

## Who Feels the Pain
340B managers and compliance officers, and CFOs facing repayment.

## Impact If Fixed
One pharmacy misrouting ~50 Medicaid claims a month for a year means ~600 duplicate discounts. Catching it in the first month avoids most of the repayment (~$150,000 at ~$250 each, estimate).
