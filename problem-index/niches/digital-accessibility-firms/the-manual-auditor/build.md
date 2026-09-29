# Everything Around the Judgement

**Niche:** [[niches/digital-accessibility-firms/the-manual-auditor/profile|The Manual Auditor]]
**Industry:** [[industries/digital-accessibility-firms|Digital Accessibility Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The judgement takes seconds and the documentation takes minutes, several thousand times.
**Tags:** #worker-facing #automation #workflow-orchestration #evaluation-metrics #large-language-models #data-integration #compliance #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to support an auditor working a site keyboard-only and then twice with screen readers for weeks, documenting each failure against a criterion — and whoever supports that work takes the account.

## The Problem
Manual accessibility auditing is skilled observation wrapped in clerical work. The auditor notices that a control does not announce its state — that judgement takes a moment. Then they identify the element, find its location in the page, decide which criterion it violates, rate it, write the description, capture a screenshot, and record it in a spreadsheet. The clerical portion takes several times longer than the judgement and happens thousands of times per audit.

## Why Nobody Has Built This
Tooling investment went to automated checking, which is a different problem. The auditor is not the buyer. The clerical work is billable. And the workflow has been a spreadsheet for long enough to seem inherent.

## What to Build
Capture the observation and generate the paperwork. Let the auditor mark a finding in one action while working and generate the documentation around it, which is the core and removes the multiple that makes an audit take weeks. Capture the element, its location and the surrounding context automatically at the moment of marking, since reconstructing that afterwards is a large share of the time. Suggest the criterion and severity for the auditor to confirm rather than requiring them to classify each one manually. Record what the screen reader announced, which is the evidence and is currently transcribed by hand. Reuse judgements on components that have not changed since the last audit, as re-auditing unchanged components is most of a repeat engagement. Generate the report from the findings rather than as a separate writing task. Support the keyboard-only pass and the screen reader passes as distinct modes with their own capture. Let the auditor annotate by voice while working, since their hands and attention are on the technology. Track time per finding so the improvement is measurable. And make the tooling itself accessible, because a meaningful proportion of auditors use assistive technology and frequently cannot use their own firm's tools.

## Target Customer
Accessibility firms and consultancies, in-house accessibility teams, audit tooling vendors, and assistive technology vendors.

## Impact If Built
The judgement takes a moment and the documentation around it takes several times longer, thousands of times per audit. One-action capture with generated documentation is where the weeks actually go.
