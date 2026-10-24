# The PRN Given Before Anyone Tried Step One

**Niche:** [[niches/idd-group-homes/behavior-support-data/profile|Behaviour Support Plans & Restrictive Intervention Data]]
**Industry:** [[industries/idd-group-homes|IDD Group Homes]]
**Type:** Fix (Pain Point)
**One-liner:** A PRN sedative for behaviour is signed on the MAR with no record of the de-escalation steps the plan required first.
**Tags:** #logistic-regression #compliance #worker-facing #quick-win #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to turn DSPs' observations of behaviour into data a clinician uses to revise the plan, and whoever cuts restrictive interventions per resident furthest takes the account.

## The Problem
Plans list steps (redirect, offer a preferred activity, quiet space) before a PRN psychotropic may be given. The MAR records the dose; the behaviour record, if any, is separate. Reviewers cannot tell whether the steps were followed, and frequent PRN use goes unnoticed.

## Why It's Still Broken
MAR and behaviour data live in different modules or on paper, and nothing requires one before the other.

## What a Fix Looks Like
When a behaviour PRN is selected on the eMAR, require the plan's de-escalation steps to be checked off with times, and send the clinician a weekly count of PRN doses per resident.

## Who Feels the Pain
Residents given sedatives that might have been avoided; DSPs blamed in reviews for undocumented steps; human rights committees reviewing incomplete records.

## Impact If Fixed
PRN psychotropic use becomes reviewable and could fall by ~20–30% once it is visible (estimate), at the cost of a few required fields.
