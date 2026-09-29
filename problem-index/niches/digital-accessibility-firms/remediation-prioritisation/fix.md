# Four Thousand Findings, One Component

**Niche:** [[niches/digital-accessibility-firms/remediation-prioritisation/profile|Remediation Prioritisation]]
**Industry:** [[industries/digital-accessibility-firms|Digital Accessibility Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Three hundred of the findings are the same button component appearing on three hundred pages.
**Tags:** #quick-win #graph-theory #descriptive-statistics #evaluation-metrics #automation #workflow-orchestration #compliance #data-integration
**Contested on:** Every serious competitor in this niche is fighting to get four thousand findings into a backlog in an order somebody can work through, and whoever makes that list actionable takes the account.

## The Problem
Instance-level reporting makes a small number of defects look like an enormous programme. One shared component with an unlabelled control generates a finding on every page it appears on. The report lists all of them. The engineering team sees four thousand items and despairs; the actual work is perhaps forty component fixes. The report's structure is actively misleading about the size of the job, in the direction that makes it less likely to be started.

## Why It's Still Broken
The report enumerates instances — a finding recorded per occurrence multiplies one defect into hundreds, and nothing in the reporting format groups them. Auditors report what they find where they find it. The finding count has looked like thoroughness. And nobody has mapped instances to components.

## What a Fix Looks Like
Group before delivering, which is a step in the report rather than a product. Group identical findings by the component or template that produces them, which is the fix and usually collapses the list by an order of magnitude. Report the fix count alongside the instance count, since those are the two numbers and only one is currently shown. Identify the shared components explicitly, as fixing those is the highest-leverage work available. Show how many instances each fix resolves, which makes the sequencing obvious. Separate genuine one-off findings from instances of a pattern. Deliver the grouped list as the primary artefact and the instance list as the appendix. Ask the engineering team how the code is organised, since they can group it faster than an auditor can infer it. Verify a grouped fix once rather than re-verifying every instance. Report progress by fixes completed rather than by instances closed. And say clearly at the start of the report how many distinct defects were found, which is the number that determines whether anyone starts.

## Who Feels the Pain
Engineering teams who see an impossible programme; accessibility leads unable to get it prioritised; clients who paid for a report that discouraged action; and disabled users, for whom the forty fixes never happen.

## Impact If Fixed
A finding recorded per occurrence multiplies one defect into hundreds, and nothing in the format groups them. Grouping by component collapses the list by an order of magnitude and changes whether the work starts.
