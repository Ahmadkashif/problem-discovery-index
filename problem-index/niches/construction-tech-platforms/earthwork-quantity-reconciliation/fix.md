# The Differing Site Condition Proven Six Months Late

**Niche:** [[niches/construction-tech-platforms/earthwork-quantity-reconciliation/profile|Earthwork & Sitework — Quantity Reconciliation]]
**Industry:** [[industries/construction-tech-platforms|Construction Tech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** When the ground is not what the geotechnical report showed, the contractor's entitlement depends on contemporaneous notice and evidence, and the evidence is assembled months later from four systems by an engineer working from memory.
**Tags:** #descriptive-statistics #evaluation-metrics #change-point-detection #confidence-intervals #compliance #workflow-orchestration #automation #revenue-impact
**Contested on:** Every serious competitor in earthwork software is fighting to reconcile the material actually moved against the material paid for, across design surfaces, machine control, survey and truck counts — and whoever makes those four numbers agree takes the account.

## The Problem
Crews hit rock where the borings showed soil, or unsuitable material where the plans showed fill. The superintendent mentions it, work continues because stopping is worse, and a notice is filed late or not at all. Six months later the contractor has a cost overrun and tries to assemble a differing-site-condition claim: which areas, on which dates, what material, how much extra, and what the contract documents said. The answer exists — in machine data, haul logs, daily reports and photos — and reconstructing it takes weeks of an engineer's time, produces a partial record, and frequently arrives after the contractual notice window has closed, which defeats the claim regardless of its merits.

## Why It's Still Broken
Notice requirements are short and the field is busy, and the person who first sees the condition is an operator in a machine. Nobody has built the path from "this is not what the plans showed" to a filed notice, so the observation travels by conversation. The evidence is fragmented by vendor, as the rest of this sub-niche describes. And there is a practical disincentive at the moment it matters: filing notice reads as adversarial early in a job when the relationship still feels good, so contractors routinely wait until the relationship is already damaged, which is after the window.

## What a Fix Looks Like
Detect the divergence automatically and make notice a one-step action. Machine control data compared against the design surface and the geotechnical model will show, without any human observation, where material is being handled that the design did not anticipate — different volumes, different machine effort, different production rates in a specific area. Flag it the week it happens, with the area, dates, quantities and the relevant contract documents assembled. Give the superintendent a one-tap confirmation and a photo, and generate the notice from the evidence rather than from a memory. Track the notice against the contractual window so nobody discovers the deadline afterwards. The same package, updated continuously, becomes the claim if it is needed and disappears quietly if it is not.

## Who Feels the Pain
Superintendents who reported a condition verbally and are asked about it months later; project engineers reconstructing six months of work from four systems; and contractors absorbing costs they were contractually entitled to recover.

## Impact If Fixed
Contemporaneous, evidenced notice within the contractual window is the single determinant of whether a differing-site-condition cost is recoverable, and generating it automatically converts a category of absorbed loss into a routine administrative event. The detection itself requires no new data collection — only a comparison the contractor already has every input for.
