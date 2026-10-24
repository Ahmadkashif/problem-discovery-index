# The Staff Comment Answered Twice and Missed Once

**Niche:** [[niches/land-developers/discretionary-rezoning-public-hearings/profile|Discretionary Rezoning & Public Hearings]]
**Industry:** [[industries/land-developers|Land Developers]]
**Type:** Fix (Pain Point)
**One-liner:** Staff comment letters list dozens of items across departments each round, and an item missed in round two becomes the reason for round four.
**Tags:** #large-language-models #bert #workflow-orchestration #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to carry rezoning and planned-development cases from filing to a council approval at the density the deal needs, and whoever gets the highest share of filed cases approved at the requested lot count takes the account.

## The Problem
Each resubmittal round returns a PDF of comments from planning, engineering, fire, parks and utilities. The entitlement manager and consultants answer them in a response letter. Items repeat with new wording, and a missed one costs another round and often a hearing date.

## Why It's Still Broken
Comments arrive as unstructured documents, responses are split among the engineer, the traffic consultant and the attorney, and nothing tracks an item across rounds.

## What a Fix Looks Like
Parse each comment letter into items by department, match items across rounds, assign each to its consultant, and generate the response matrix with status. Flag any item open from a prior round before resubmittal.

## Who Feels the Pain
Entitlement managers, civil engineers answering comments, and the land committee waiting on the hearing.

## Impact If Fixed
Closing every comment in the round it appears in avoids a resubmittal round, often four to eight weeks (estimate), per case.
