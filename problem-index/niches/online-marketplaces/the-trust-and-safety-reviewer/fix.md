# No Way to Say the Policy Is Wrong

**Niche:** [[niches/online-marketplaces/the-trust-and-safety-reviewer/profile|The Trust & Safety Reviewer]]
**Industry:** [[industries/online-marketplaces|Online Marketplaces]]
**Type:** Fix (Pain Point)
**One-liner:** Reviewers encounter the same policy gap hundreds of times, decide each instance against a rule that does not fit, and have no channel to report that the rule is the problem.
**Tags:** #worker-facing #compliance #descriptive-statistics #k-means-clustering #evaluation-metrics #automation #quick-win #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to support a reviewer whose every case is genuinely ambiguous — and whoever does that takes the quality, because these are the decisions automation could not make and they are being timed like data entry.

## The Problem
A category of listing keeps arriving that the policy does not address — a product that is legal in some jurisdictions, a service that resembles a prohibited one, a description whose meaning depends on a subculture the policy writers do not know. Reviewers decide each one, differently, because the rule does not fit. They mention it to each other. Some write it in a free-text field that goes into a database nobody reads. The policy is updated eventually, months later, when a journalist or a regulator raises it — and the two hundred reviewers who could have raised it in week one had no way to.

## Why It's Still Broken
The review tool was built for deciding cases, not for reporting on the rules, so there is no field for it. Reviewers are frequently contracted staff outside the policy function's organisational reach. Free-text notes exist and are unqueryable at volume. And the policy team's inputs are escalations, legal advice and press coverage, none of which surface the everyday gap that two hundred people are working around.

## What a Fix Looks Like
Give the gap a channel and read it. Add a structured policy-gap flag with a reason taxonomy to the review tool, taking a reviewer seconds, which is the fix — the information already exists in their heads and nothing collects it. Cluster the flags, since one reviewer's note is an anecdote and two hundred flags on the same pattern is a finding that a policy team can act on. Report flag volume by policy area as a standing metric, so a rule generating constant friction is visible before it becomes an incident. Detect the gap without the flag too, by measuring reviewer disagreement and decision inconsistency by case type, since a category where reviewers reliably disagree is a policy gap whether or not anybody reported it. Close the loop: tell the reviewers what happened to their flags, because a channel that swallows input is used once. Route urgent gaps directly, since some of these are time-sensitive and a monthly review cycle is too slow. Include the outsourced reviewers, who see the most cases and have the least access. And treat the reviewers as the policy function's primary sensor, since they are the only people who see every hard case and are currently the only group not consulted.

## Who Feels the Pain
Reviewers applying a rule they can see does not fit, hundreds of times; sellers on the wrong side of an inconsistent decision; and policy teams learning about their own gaps from outside the company.

## Impact If Fixed
Two hundred people see the gap in week one and have no way to say so. A structured flag plus clustering turns anecdote into a finding, and measuring reviewer disagreement by case type detects the gap even when nobody reports it.
