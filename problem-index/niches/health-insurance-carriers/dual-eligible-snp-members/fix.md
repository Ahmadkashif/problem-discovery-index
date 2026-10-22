# Two Plans' Worth of Letters for One Member

**Niche:** [[niches/health-insurance-carriers/dual-eligible-snp-members/profile|Dual-Eligible & Special Needs Plan Members]]
**Industry:** [[industries/health-insurance-carriers|Health Insurance Carriers]]
**Type:** Fix (Pain Point)
**One-liner:** A dual-eligible member enrolled with the same company for Medicare and Medicaid still gets separate cards, notices and denial letters from systems that do not talk.
**Tags:** #data-integration #workflow-orchestration #large-language-models #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to reach each new special needs plan member for a health risk assessment and care plan inside CMS's 90-day window, and whoever completes the most assessments with hard-to-reach dual-eligible members, and keeps them enrolled, takes the account.

## The Problem
Medicare and Medicaid sides of a member's coverage are often administered on separate platforms, even inside one parent company. The member gets two sets of letters, sometimes contradictory, and a denial on one side may be covered on the other. Integrated plans are expected to unify notices and appeals (recalled), but their systems were not built that way.

## Why It's Still Broken
Medicaid business runs on state-specific configurations and contracts, Medicare business on CMS's. Integration requirements arrived faster than platform consolidation.

## What a Fix Looks Like
A single member record and notice layer across both coverages. It checks every coverage decision against both benefit sets before a denial goes out, generates one integrated notice with the right appeal path, and gives care managers and member services one view.

## Who Feels the Pain
Dual-eligible members confused by contradictory letters; care managers explaining them; plans facing complaints and disenrolment.

## Impact If Fixed
Fewer denials for services the other coverage would pay, fewer confused members, and better retention in integrated plans.
