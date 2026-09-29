# The Calendar That Changes Every Week

**Niche:** [[niches/email-sms-marketing-platforms/the-lifecycle-marketer/profile|The Lifecycle Marketer]]
**Industry:** [[industries/email-sms-marketing-platforms|Email & SMS Marketing Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The campaign calendar is a spreadsheet that changes weekly and must be reconciled by hand against fifty automated flows nobody has mapped.
**Tags:** #workflow-orchestration #automation #descriptive-statistics #evaluation-metrics #quick-win #worker-facing #compliance #data-integration
**Contested on:** Every serious competitor in this niche is fighting to make fifty automated journeys comprehensible and monitored by one person — and whoever does that changes how much of a brand's lifecycle programme actually runs.

## The Problem
The campaign calendar lists this month's one-off sends: a promotion, a product announcement, a seasonal campaign, a re-engagement push. Merchandising changes the promotion date on Tuesday. The marketer now has to work out, by hand, which segments receive which campaign, whether anyone in those segments is also in an automated flow that will message them the same day, whether the combined frequency breaches anything, and whether the promotion contradicts an automated message going out that afternoon. They do this weekly, from a spreadsheet and a memory of fifty diagrams, and the customer occasionally receives the contradiction.

## Why It's Still Broken
Campaigns and flows are separate objects in every platform, planned in separate places, with no shared view of who receives what and when — the product's object model separates them and the customer experiences their sum. The calendar lives outside the platform because it involves people and dates the platform does not model. Frequency capping, where it exists, applies within a channel or a flow rather than across the whole programme. And the conflicts surface as customer complaints rather than as errors.

## What a Fix Looks Like
Unify the view of what a customer will receive. Show the projected message load per customer across campaigns and flows for the coming period, which is the fix, is computable from the schedules and segment definitions the platform already holds, and makes every conflict visible before it happens. Simulate a proposed campaign against the automated programme before it is scheduled, so a clash is caught at planning rather than at send. Enforce a global frequency policy across every channel, flow and campaign, which is the control that actually prevents the outcome and which no per-flow setting can provide. Detect content contradictions, such as a full-price announcement to someone in a discount flow, which is the most damaging conflict and is detectable from the message content and segment overlap. Bring the calendar into the platform so it is planned against the same objects it interacts with. Recalculate automatically when a date changes, since replanning by hand is the weekly task being removed. Show which customers are near a frequency limit before a campaign is sent, so a segment can be adjusted rather than a policy breached. Keep the whole picture as a standing view rather than a weekly reconstruction. Warn on the compounding case where several flows trigger from one customer action, which is the most common way someone receives four messages. And report actual message load per customer, because the intended frequency and the received frequency differ and only one of them is currently known.

## Who Feels the Pain
Marketers reconciling a calendar against fifty flows by hand every week; customers receiving contradictory messages on the same day; and brands whose unsubscribe rate is driven by frequency nobody is measuring.

## Impact If Fixed
The object model separates campaigns from flows and the customer experiences their sum, so the reconciliation falls on one person weekly. Projecting message load per customer from schedules and segments already held makes every conflict visible before it happens.
