# Automated QC Templates Kept Current Per Platform

**Niche:** [[niches/postproduction-studios/deliverables-qc-and-mastering/profile|Deliverables QC & Mastering]]
**Industry:** [[industries/postproduction-studios|Postproduction Studios]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Automated QC tools ship platform templates, and the platforms revise their specs faster than anyone updates them.
**Tags:** #large-language-models #transformers #evaluation-metrics #compliance #automation #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to pass each platform's inspection on the first submission, and whoever delivers the lowest redelivery rate per programme hour takes the studio's mastering work.

## The Problem
Each platform publishes a delivery spec and revises it: new HDR metadata requirements, timed-text rules, audio layouts, IMF application profiles. QC templates are maintained by a facility engineer who reads the change notes when there is time. A package that passes the old template fails the new spec.

## What Already Exists
Interra BATON, Venera Pulsar and Quasar, and Telestream QC with template libraries; platform spec pages and error-code documentation such as Netflix's Backlot help site.

## The Customization Gap
The adaptation needs: platform spec documents monitored and diffed on each revision; changed requirements translated into proposed template changes for the facility's QC tool, for an engineer to approve; each template versioned against the spec version it implements; and the facility's own past rejections attached to the rule they tested, so the riskiest rules are tested hardest. The tools execute templates and leave keeping them current to the facility.

## Target Customer
Media engineers and QC leads at mastering facilities delivering to several platforms.

## Impact If Solved
Spec changes reach the templates within days instead of after the first rejection.
