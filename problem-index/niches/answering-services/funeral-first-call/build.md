# A Removal-Ready Check Before the Director Is Called

**Niche:** [[niches/answering-services/funeral-first-call/profile|Funeral Home First-Call Answering]]
**Industry:** [[industries/answering-services|Telephone Answering Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The operator who takes a death call cannot tell whether the information is enough for the removal team to go, so the director is woken to find out.
**Tags:** #large-language-models #logistic-regression #evaluation-metrics #workflow-orchestration #worker-facing #automation
**Contested on:** Every serious competitor in this niche is fighting to take a death call at 3 a.m. with a complete first-call record (place of death, release status, medical examiner involvement, next of kin and their authority, weight and access for the removal), and whoever hands the on-call director a removal-ready first call without a callback takes the account.

## The Problem
Whether a removal can proceed depends on facts the caller may not know or may state loosely: "the nurse said it's fine" is not a release, a death at home without hospice may involve the medical examiner, and some facilities need a specific form signed. Directors call back to check, or arrive to find the body cannot be released.

## Why Nobody Has Built This
Funeral answering is a small segment, scripts are generic, and the rules vary by state (medical examiner jurisdiction) and by facility (hospital and nursing-home release procedures). Nobody has collected which first calls led to a wasted trip or a callback.

## What to Build
A first-call record with a readiness check. Each field is captured as structured data, and the rules for the place of death and jurisdiction (home with hospice, home without hospice, hospital, nursing home, ME case) determine which fields are required. A readiness status (ready, needs release, ME pending) goes with the page. The director confirms the outcome the next day, so the rules learn which combinations caused trouble.

## Target Customer
Funeral-specialist answering services; regional funeral groups running their own night lines.

## Impact If Built
Directors are woken with a decision ready rather than a question, removal teams stop making wasted trips, and families are not called back at night for details.
