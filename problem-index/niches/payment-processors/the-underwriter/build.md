# Reading a Website Against a Clock

**Niche:** [[niches/payment-processors/the-underwriter/profile|The Underwriter]]
**Industry:** [[industries/payment-processors|Payment Processors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Underwriters decide a business's fate by reading its website and its processing history under an approval-time target, and never learn which of their decisions was right.
**Tags:** #worker-facing #large-language-models #evaluation-metrics #confidence-intervals #compliance #workflow-orchestration #gradient-boosting #automation
**Contested on:** Every serious competitor in this niche is fighting to give the underwriter evidence and feedback rather than a website and a clock — and whoever does that turns an unmeasured judgement into a skill that can improve.

## The Problem
The application arrives. The underwriter opens the applicant's website to work out what they actually sell, checks a registry, looks at whatever processing history exists, considers the category's chargeback norms, and decides — approve, decline, or approve with a reserve — within a target time set because merchants leave if onboarding is slow. They do this dozens of times a day. The loss exposure they are managing is real and arrives months later, recorded against a merchant rather than against their decision. Whatever judgement they develop is developed without feedback and is lost when they leave.

## Why Nobody Has Built This
The underwriter was placed where automation could not reach and given the automation's leftovers — a queue, a score and a target — which is how a judgement role ends up with capacity tooling. Speed is measurable and competitive while accuracy is invisible for months. The outcome belongs to a different team. And the business model assessment requires reading a website, which was genuinely manual until recently.

## What to Build
Give the underwriter a case and a record. Classify the business model from the website, the catalogue and the application automatically, which is reliable now and is the single most time-consuming part of the review. Assemble the external evidence — registry, ownership, sanctions, web presence, prior processing, related entities — so the underwriter starts with the file rather than a browser. Show comparable past cases and what happened to them, which is how consistency and judgement both develop and is the thing they most lack. Present the loss exposure explicitly, since the decision is a credit judgement and the underwriter is currently reasoning about risk without a quantity. Recommend terms rather than a binary, because reserve and limit structures let a marginal merchant be approved safely and are currently applied from a table. Flag the specific concerns with evidence, so the underwriter's attention goes to the question rather than to the search. Route by complexity so the straightforward applications clear automatically and the difficult ones get time. Record the reasoning in structured form, which supports the outcome join, consistency analysis and appeal at once. Give them their own outcome record, connecting to the fix note. And balance the speed target against measured accuracy, because measuring one and not the other produces exactly the behaviour it rewards.

## Target Customer
Acquirer risk operations leadership, the underwriters themselves, and the onboarding platform vendors serving this function.

## Impact If Built
The underwriter was placed where automation could not reach and given the automation's leftovers, which is how a credit judgement role ends up with a queue and a target. Classifying the business model automatically and showing comparable outcomes is what turns browsing into reviewing.
