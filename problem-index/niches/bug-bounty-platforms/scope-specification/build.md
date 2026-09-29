# Build: Scope as a Queryable Contract

**Niche:** Scope Specification
**Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A structured, queryable scope definition with a binding pre-work answer for researchers and an automatic check at submission, including an explicit policy for assets the programme did not know it had.
**Tags:** #graph-theory #evaluation-metrics #confidence-intervals #compliance #automation #data-integration #worker-facing
**Contested on:** Whether what counts as in-bounds is machine-checkable before a researcher starts, or a paragraph of prose interpreted after they finish.

## The Problem

Scope is the most consequential parameter of the bounty relationship and it is expressed as prose on a web page.

For the researcher this means the decision to invest a week is made on an interpretation. The policy lists a domain; the target is on a subdomain operated by a third party. The policy prohibits denial of service; the finding demonstrates resource exhaustion. The policy lists production assets; the target is a staging host that was publicly reachable. Each of these is a real situation, none is addressed by the page, and all are resolved after the submission by the party who pays.

For the programme it means triage capacity is consumed by submissions that were never eligible. A large share of what a triager reads is out of scope, and determining that requires a human because the scope exists only as text.

The tension that has prevented a fix is real. A rigidly enumerated scope would exclude the asset nobody knew about, which is frequently the most valuable thing a programme learns. So programmes keep scope loose deliberately, and the looseness costs both sides.

## Why Nobody Has Built This

**The enumeration objection is legitimate.** If scope is a list, findings outside the list are excluded, and those are often the findings that matter most. Any design that does not solve this will be rejected by programmes for good reasons.

**Loose scope preserves discretion.** A programme that can interpret after the fact has an option worth money. This is the same incentive that runs through the parent niche and it operates here too.

**Asset reality changes faster than policy.** Infrastructure is added and removed continuously; a policy page is edited occasionally. Any static specification is stale within weeks, which means the specification has to be generated from live asset data rather than maintained by hand.

**Ownership attribution is genuinely hard.** Whether a given host belongs to the organisation, a subsidiary, a vendor or an unrelated party sharing infrastructure is a real problem, and getting it wrong in either direction is costly.

**A binding pre-work answer transfers risk to the programme.** Committing in advance that a target is in scope means paying for whatever is found there, which is exactly the commitment programmes currently avoid making.

## What to Build

**A structured scope schema, published and open.** Assets and patterns, asset classes, techniques, conditions, time bounds, and — the essential part — an explicit `unknown` outcome with a stated policy. An open schema is worth far more than a proprietary one, because its value comes from every platform and every programme using the same shape.

**Make the unknown case the headline feature.** For assets not in the specification, the programme states in advance what happens: eligible at a defined band, eligible subject to confirmation of ownership, or ineligible. This preserves the discovery value that makes loose scope attractive while removing the ambiguity, and it is the design decision that makes the whole thing acceptable to programmes.

**A pre-work query with a binding window.** A researcher submits a target and receives a verdict — in, out, or unknown-with-policy — binding for a stated period. Programmes will accept this far more readily than they expect, because the alternative is paying triagers to answer the same question after the work.

**Generate the specification from live asset data.** Connected to the programme's own attack surface management or cloud inventory, so scope reflects what actually exists rather than what someone wrote in March. Staleness is the practical failure mode of every scope page and it is solved by generation rather than by discipline.

**Check at submission, before a human.** Automatic scope evaluation on every submission, with clear out-of-scope cases rejected with a citation of the specific rule. This is the feature that pays for the build, because out-of-scope triage is the programme's largest wasted expense.

**Define chaining explicitly.** Whether an out-of-scope component contributing to an in-scope impact is eligible, stated as a rule rather than argued case by case. This is the most common hard case and no programme has a written position on it.

**Version the specification and timestamp submissions.** A submission is evaluated against the scope in force when the researcher began, not when a triager reads it. Scope changing mid-investigation is a recurring grievance and versioning resolves it completely.

## Target Customer

The platforms, where submission-time checking reduces triage cost directly and measurably, which is the argument that funds it.

Programme managers running public programmes, who carry the out-of-scope triage burden and would adopt this for the cost saving alone.

The open schema should sit with a neutral body or an open-source effort, because its value is entirely in adoption across platforms rather than in exclusivity.

## Impact If Built

Researchers can decide where to spend a week knowing whether the work can be paid, which is the most basic condition of a functioning labour market and is currently absent.

Submission-time scope checking removes a large fraction of the triage burden mechanically, which is the clearest operational saving available to any programme.

And an explicit unknown-asset policy would preserve the single most valuable property of bounty programmes — finding what the organisation did not know it had — while removing the ambiguity that currently makes those findings the most likely to go unpaid.
