# The Route Built From Habit

**Niche:** [[niches/crm-platforms/field-sales-distributor-crm/profile|Field Sales & Distributor CRM]]
**Industry:** [[industries/crm-platforms|CRM Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A field representative's week is a route they have run for years, visiting accounts on a cadence set by convention rather than by which accounts would repay a visit — and nobody has ever tested whether the cadence is right.
**Tags:** #descriptive-statistics #gradient-boosting #optimization-fundamentals #evaluation-metrics #confidence-intervals #hypothesis-testing #revenue-impact #automation
**Contested on:** Every serious competitor in field sales software is fighting to capture what happened on a call from a vehicle in under a minute without typing — and whoever the representatives actually use takes the account.

## The Problem
A representative visits their A accounts weekly, B accounts fortnightly and C accounts monthly, because that is the classification the organisation adopted at some point and the route was built around it. Whether a weekly visit to a particular A account produces anything, whether a C account would grow if visited more, and whether the drive time between two towns is worth what is at the end of it are all unexamined. The classification is based on current revenue, which means the route is optimised to serve the accounts that already buy and systematically under-serves the ones that could.

## Why It's Still Broken
Call cadence is treated as a management standard rather than as a variable, and it is set by a classification that is easy to compute and weakly related to the question. Testing it would mean deliberately varying visit frequency across comparable accounts, which is straightforward and has never been part of how these organisations operate. And the representative's own knowledge of which accounts repay a visit — which is considerable — has no mechanism to reach the routing decision.

## What a Fix Looks Like
Measure the return on a visit and let the cadence follow. The organisation's own history contains what it needs: visits, orders and the relationship between them, across hundreds of accounts and years. Estimating the effect of visit frequency requires care because frequency is assigned by classification rather than at random — the accounts visited most are the ones already buying most — so the honest version involves either a deliberate variation in cadence across matched accounts, which is inexpensive and settles the question, or a design that uses the natural variation in route disruptions, absences and territory changes. Then rank accounts by expected return per visit including drive time, which is the number that should set cadence and currently does not exist. Present it as a proposed schedule the representative edits, because their knowledge of an account's situation is frequently decisive and a system that overrides it will be ignored. Report coverage honestly too: which accounts have not been visited in a quarter, which is a list most field organisations would find uncomfortable and useful.

## Who Feels the Pain
Representatives driving routes set by a classification nobody has tested; accounts that would grow with attention and sit in the C tier; and sales leadership allocating the organisation's most expensive resource — field time — by convention.

## Impact If Fixed
Field time is the largest cost in a distributor's sales organisation and is allocated by a revenue-based classification that is almost certainly wrong at the margins. A deliberate cadence variation across matched accounts is a cheap experiment that would settle a question every field organisation has and none has answered, and the expected-return ranking turns the route from a habit into a decision.
