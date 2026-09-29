# Regression Suites and Certification Surveillance

**Niche:** [[niches/ai-red-teaming-firms/assessment-revalidation/profile|Assessment Revalidation]]
**Industry:** [[industries/ai-red-teaming-firms|AI Red Teaming Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Certification bodies solved keeping an assessment valid as a product changes, with surveillance audits and change notification obligations, and this industry issues a dated document.
**Tags:** #compliance #automation #evaluation-metrics #workflow-orchestration #descriptive-statistics #confidence-intervals #change-point-detection #quick-win
**Contested on:** Every serious competitor in this niche is fighting to re-establish an assessment's conclusions after the system changes, at a fraction of the original cost — and whoever does that takes the account, because the alternative is a report that expires on the client's next model upgrade.

## The Problem
Keeping a certification valid while the certified thing changes is a solved institutional problem. Certification schemes require the holder to notify significant changes, conduct periodic surveillance at a fraction of the initial assessment's depth, and re-certify on a cycle. Software engineering solved the technical half with regression suites that re-run on every change. AI assessment has neither the obligation nor the suite, and the report's validity is simply not addressed.

## What Already Exists
Certification schemes with change notification obligations and surveillance audits; regression test suites re-run automatically on change; continuous compliance monitoring platforms; configuration change detection; and the distinction between initial assessment depth and surveillance depth.

## The Customization Gap
The adaptation is to a system that changes because a third party updated it. It requires: (1) change detection rather than change notification, since the change originates with a model provider who has no obligation to anybody in this relationship and the client frequently does not know either — a behavioural probe substitutes for the notification the certification model assumes; (2) surveillance defined as re-running the recorded probes with a statistical comparison, which is cheap and is a genuine surveillance activity rather than a token one; (3) a validity statement on every report specifying the configuration it applies to, which the fix note develops and which certification schemes have always had; (4) a defined trigger list — model version, prompt changes, tool additions, retrieval changes — since the client needs to know what invalidates their assessment and is currently told nothing; and (5) tiering, so a minor change triggers a probe re-run and a major one triggers a partial re-assessment, which is exactly how surveillance schemes are structured.

## Target Customer
Assessment firms, their clients, and the certification and conformity assessment bodies whose scheme design applies directly.

## Impact If Solved
Certification schemes solved validity-under-change with surveillance and notification obligations. Behavioural change detection substitutes for the notification nobody here is obliged to give, and probe re-runs make surveillance genuine rather than token.
