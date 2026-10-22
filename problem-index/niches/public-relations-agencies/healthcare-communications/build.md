# Predicting MLR Rejections Before Submission

**Niche:** [[niches/public-relations-agencies/healthcare-communications/profile|Healthcare & Life Sciences Communications]]
**Industry:** [[industries/public-relations-agencies|Public Relations Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Agencies send drafts into medical-legal-regulatory review blind, when years of reviewer comments already show which claims, phrasings and omissions each sponsor's committee rejects.
**Tags:** #bert #large-language-models #transformers #logistic-regression #evaluation-metrics #compliance #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to get trial readouts, disease-awareness campaigns and product news through medical-legal-regulatory review and into coverage without the material becoming unfiled or non-compliant promotion, and whoever gets compliant stories out fastest takes the account.

## The Problem
A press release about a phase 3 readout goes to the sponsor's MLR committee. It comes back with comments: a superlative removed, a safety statement moved up, a secondary endpoint described too confidently, a reference that does not support the sentence it is attached to. The agency revises and resubmits. Each round takes days, and the news window (a medical congress, a data embargo lifting) does not move.

## Why Nobody Has Built This
MLR comments live in the sponsor's review system, not the agency's, and agencies keep them only as marked-up PDFs. Review platforms are built for the sponsor's workflow and routing, not for predicting a committee's behaviour from the drafter's side.

## What to Build
A pre-submission checker trained on the agency's archive of drafts and MLR comments per sponsor: it flags sentences likely to draw comment (comparative claims, efficacy language without context, missing fair balance, references that do not support the claim), suggests the phrasing that passed last time, and links each claim to the approved labelling and the reference pack. It reports, per sponsor, the comment categories that recur.

## Target Customer
Healthcare practice leads at agencies with several pharmaceutical or device sponsors; sponsor communications teams who want fewer rounds.

## Impact If Built
One or two fewer MLR rounds per release would put stories out inside news windows that are now missed, with a documented claim trail if FDA asks.
