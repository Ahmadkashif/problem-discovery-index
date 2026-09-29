# Tax Projection Tooling Pointed at the Withholding Form

**Niche:** [[niches/payroll-platforms/worker-facing-pay-tools/profile|Worker-Facing Pay Tools]]
**Industry:** [[industries/payroll-platforms|Payroll Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Tax preparation software projects a household's annual tax outcome accurately and cheaply, and the withholding election that determines whether that outcome is a refund or a bill is made once at hire on a form nobody understands.
**Tags:** #descriptive-statistics #time-series-forecasting #confidence-intervals #evaluation-metrics #compliance #automation #worker-facing #revenue-impact
**Contested on:** Every serious competitor building worker-facing pay software is fighting to let a person reconstruct and control their own pay — every line, every deduction, every withholding choice — and whoever makes a pay statement legible takes the deployment.

## The Problem
A worker completes a withholding form at hire, guessing at the questions, and never revisits it. If they over-withhold they give the government an interest-free loan all year and receive a refund they treat as a windfall. If they under-withhold they receive a bill they did not budget for. Life changes — a second job, a spouse's income change, a new child, a large bonus — all move the correct answer and none of them prompts a revision. The payroll system knows their year-to-date earnings and withholding precisely and could project the outcome at any moment.

## What Already Exists
Tax projection engines are mature and commodity, embedded in every consumer tax product and available as libraries and services. Withholding calculation is already implemented in every payroll system. Year-to-date data is precise and current. The tax rules for projection are the same rules already encoded for withholding. Everything needed exists and a substantial part of it is inside the payroll system itself.

## The Customization Gap
The adaptation is to a continuous projection rather than an annual filing. It requires: (1) projection from year-to-date actuals plus expected remaining earnings, updated every pay period, so the worker sees a live estimate of their annual outcome rather than a guess at hire; (2) household context handled carefully, since accurate projection needs a spouse's income and other jobs and the payroll system has neither — asking for it is reasonable, storing it is sensitive, and the design should make the data optional and the value clear; (3) event-driven prompts, since a bonus, a raise, a benefits change or a new dependent are all knowable to the system and all change the correct election, and a prompt at that moment is worth far more than a form at hire; (4) the recommendation expressed as an outcome rather than as a form field — this election means you will owe roughly this much or receive roughly this much — since the form's own vocabulary is the reason nobody completes it correctly; and (5) a firm boundary against tax advice, informing rather than advising, which is both the legal position and the honest one given the uncertainty in any projection.

## Target Customer
Payroll providers, employers whose workers experience tax surprises, and the consumer tax and financial wellness products that already project but have no access to live payroll data.

## Impact If Solved
Withholding is the largest deduction most workers have and is set by a form completed once under conditions of total incomprehension. A live projection expressed as an outcome, prompted at the moments the answer changes, converts an annual surprise into a managed choice — and the under-withholding case in particular is a household financial shock that is entirely preventable.
