# The Approved List That Became a Bottleneck

**Niche:** [[niches/open-source-commercial-vendors/enterprise-procurement-compliance/profile|Enterprise Procurement & Compliance]]
**Industry:** [[industries/open-source-commercial-vendors|Open Source Commercial Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** An enterprise maintains a list of approved open-source components, the approval process takes weeks, and engineers respond by using whatever is on the list or by not asking.
**Tags:** #descriptive-statistics #survival-analysis #hypothesis-testing #confidence-intervals #evaluation-metrics #compliance #quick-win #workflow-orchestration
**Contested on:** Every serious competitor here is fighting to get open-source software through an enterprise's legal, security and procurement review without a three-month project — and whoever does that takes the enterprise adoption, because the review is where it currently stops.

## The Problem
The approved component list has four hundred entries, most approved years ago at versions long superseded. Adding a component takes six to eleven weeks. Engineers respond rationally: they use an approved component that is a poor fit, they use an unapproved one and do not mention it, or they build something themselves that is worse than either. The list's purpose was to manage risk and its effect is to push adoption underground, which produces more risk than it prevents and is invisible to the function that maintains it.

## Why It's Still Broken
The list was designed as a gate and gates create queues, and the queue length is not measured by anyone. Approvals are per component rather than per policy, so every request is a bespoke review. Versions are not tracked, so the list approves things that no longer exist. Nobody measures circumvention, which means the policy's actual effect is unknown. And the review function is staffed for the volume it receives rather than the volume that exists, which is a different and larger number.

## What a Fix Looks Like
Make the common path fast and reserve review for what warrants it. Pre-approve by policy rather than by component: a permissive licence, an established project meeting stated sustainability criteria, and a non-distributed internal use can be approved automatically against a published rule, which removes most of the queue immediately and is a policy decision rather than a technology one. Reserve individual review for the cases the policy flags — copyleft licences in distributed products, projects failing the sustainability criteria, unusual usage contexts. Track versions rather than components, and re-evaluate automatically on a new release rather than treating the original approval as permanent. Measure the queue: requests, time to decision, and the proportion of requests that are eventually approved, which will show that most are and that the review is a delay rather than a filter. Measure circumvention by comparing the components actually present in the codebase against the approved list, which is a composition analysis run and regularly finds hundreds of unapproved components — the honest measure of the policy's effect. And publish the criteria, so an engineer can tell before asking whether something will be approved.

## Who Feels the Pain
Engineers waiting weeks or routing around the process; review functions processing requests that are nearly all approved; and enterprises whose actual open-source risk is in the components nobody declared.

## Impact If Fixed
Policy-based pre-approval removes most of the queue and is a decision rather than a system. Measuring circumvention against the codebase is a single composition analysis run and produces the honest assessment of what the policy is actually achieving.
