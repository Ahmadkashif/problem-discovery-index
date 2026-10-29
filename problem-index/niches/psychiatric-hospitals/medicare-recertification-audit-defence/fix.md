# Recertifications Signed After the Day They Were Due

**Niche:** [[niches/psychiatric-hospitals/medicare-recertification-audit-defence/profile|Medicare Recertification, Active-Treatment Records & Audit Defence]]
**Industry:** [[industries/psychiatric-hospitals|Psychiatric Hospitals]]
**Type:** Fix (Pain Point)
**One-liner:** The day-12 recertification of a Medicare psychiatric stay is a paper or EHR form that nobody reminds the psychiatrist about, so many are signed late or at discharge, and a late signature can make the days after it unpayable.
**Tags:** #workflow-orchestration #compliance #worker-facing #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to make each Medicare and Medicaid psychiatric day defensible when an auditor reads the record later, and whoever has the lowest share of audited paid days recouped takes the account.

## The Problem
The rule is simple: recertify as of day 12, then at least every 30 days (42 CFR 424.14). The practice is a stack of forms found by the health information team after discharge.

## Why It's Still Broken
EHRs store the form but rarely track the stay day, and psychiatrists rotate across units and weekends. Medicare does not review the stay as it happens, so nobody notices until an audit.

## What a Fix Looks Like
A stay-day tracker that puts the recertification in the attending's queue on day 11 with a draft built from the current treatment plan and notes, and escalates to the medical director if it is unsigned on day 12.

## Who Feels the Pain
Health information managers, attending psychiatrists and compliance officers.

## Impact If Fixed
If ~5% of Medicare stays have a late recertification (estimate) and each puts ~10 paid days at risk, a hospital with 1,000 Medicare stays a year protects ~500 days, ~$500,000 at ~$1,000 a day.
