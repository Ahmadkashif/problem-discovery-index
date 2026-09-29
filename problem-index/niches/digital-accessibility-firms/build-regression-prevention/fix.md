# The Component That Ships Broken Every Time

**Niche:** [[niches/digital-accessibility-firms/build-regression-prevention/profile|Build Regression Prevention]]
**Industry:** [[industries/digital-accessibility-firms|Digital Accessibility Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The same modal component fails the same way in every audit, gets fixed in three places, and ships broken again next quarter.
**Tags:** #quick-win #automation #workflow-orchestration #evaluation-metrics #compliance #descriptive-statistics #data-integration #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to stop new accessibility failures reaching production, because remediating them afterwards costs many times more — and whoever catches them in the build takes the account.

## The Problem
The same defects recur audit after audit. A modal that does not trap focus, a custom dropdown that does not announce its state, an icon button without a label. They are fixed where the audit found them and reappear wherever the pattern is used next, because the fix was applied to instances rather than to the component and nothing prevents the next instance. Organisations pay to find the same defect repeatedly.

## Why It's Still Broken
The fix goes to the instance rather than the source — a defect remediated where it was found leaves the component that produces it unchanged, so the next use recreates it. Audits report instances. Design systems are not audited separately. And nobody tracks recurrence across audits.

## What a Fix Looks Like
Fix the component and check it where it is defined. Audit the design system components separately and thoroughly, which is the fix and is a small, high-leverage piece of work. Fix the component rather than its instances, then migrate the instances, which is the sequence that actually ends the recurrence. Add accessibility tests to the component library so a regression fails there. Compare findings across audits to identify what recurs, which nobody does and which names the components to fix. Document the accessible pattern for each component so new uses start correctly. Discourage bespoke reimplementations of components the system already provides, since those are where the defects originate. Report recurrence rate as an audit metric, which shows whether remediation is working structurally. Check the component library before auditing the application, as that reorders the whole finding list. Prioritise the components used most, which is knowable from the codebase. And treat a recurring finding as a component defect rather than as a new instance.

## Who Feels the Pain
Organisations paying repeatedly for the same finding; developers fixing instances of a defect they did not create; disabled users encountering the same barrier in a new place; and the remediation budget, spent on recurrence.

## Impact If Fixed
A defect remediated where it was found leaves the component that produces it unchanged, so the next use recreates it. Auditing and fixing the design system components is a small piece of work that ends the recurrence.
