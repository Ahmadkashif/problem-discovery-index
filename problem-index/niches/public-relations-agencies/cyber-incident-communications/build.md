# One Fact Set Behind Every Disclosure

**Niche:** [[niches/public-relations-agencies/cyber-incident-communications/profile|Cyber Incident & Disclosure Communications]]
**Industry:** [[industries/public-relations-agencies|Public Relations Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** During a cyber incident six documents for six audiences are drafted by different people from facts that change every few hours, and nothing checks that they agree.
**Tags:** #large-language-models #transformers #evaluation-metrics #compliance #workflow-orchestration #automation
**Contested on:** Every serious competitor in this niche is fighting to keep the media statement, customer and regulator notices and any Form 8-K saying the same thing inside the four-business-day and state-notification clocks, under counsel's privilege, and whoever keeps disclosure consistent and on time wins the insurer- and law-firm-panel slot.

## The Problem
Forensics revises the number of affected records twice in a day. The 8-K draft is with securities counsel, the customer notice with privacy counsel, the media holding statement with the PR firm, the employee memo with HR. Each picks up the new number at a different time, and one document goes out with the old figure or a characterisation ("no evidence of misuse") that the others have dropped. Plaintiffs' lawyers and regulators compare them later.

## Why Nobody Has Built This
Each document belongs to a different professional, and the work is privileged, so firms are wary of shared systems. Disclosure tools serve finance; notification vendors serve mailing; PR firms serve the media.

## What to Build
A privileged incident workspace holding one structured fact set (scope, data types, timeline, containment, characterisations approved by counsel) with approval state, and every audience document linked to it. Any change to a fact flags every document that uses it; every outbound version is logged by audience and time; language from past incidents that cleared review is retrievable by situation.

## Target Customer
Breach coaches and the crisis communications firms on their panels; general counsel at listed companies.

## Impact If Built
Consistent disclosure across audiences inside the statutory clock, and a defensible record of who was told what and when.
