# Accuracy Evidence on the User's Own Content

**Niche:** [[niches/court-reporting-firms/cart-realtime-captioning/profile|CART & Realtime Captioning]]
**Industry:** [[industries/court-reporting-firms|Court Reporting Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Disability offices choose between human CART and automatic captions on price, because nobody measures either on the lectures and meetings the user actually attends.
**Tags:** #transformers #evaluation-metrics #hypothesis-testing #confidence-intervals #worker-facing #compliance
**Contested on:** Every serious competitor in this niche is fighting to give a deaf or hard-of-hearing user live text accurate enough on technical and multi-speaker content to count as effective communication under the ADA, and whoever proves that accuracy on the user's own courses and meetings, against cheaper automatic captions, takes the account.

## The Problem
Captioning vendors quote accuracy figures measured on clean test audio. Automatic caption vendors do the same. A deaf engineering student's experience depends on how both perform on her thermodynamics lecturer, with his accent, his formulas and the questions from the back of the room. The disability office has no way to know, so the cheaper option wins until the student complains.

## Why Nobody Has Built This
Scoring live captions needs a verified reference transcript, which costs more than the captioning itself. Agencies fear measurement could cut against them on easy content, and automatic-caption vendors gain nothing from it.

## What to Build
A sampled evaluation service. Record a few minutes per session with consent, produce a verified reference by careful human correction, and score the live CART output and a parallel automatic caption on word accuracy, technical-term accuracy, speaker attribution and lag, with confidence intervals per course. Term-level results feed the captioner's preparation for the next session.

## Target Customer
University disability and accessibility services directors; captioning agencies defending contracts; public bodies required to caption meetings.

## Impact If Built
Captioning decisions made on evidence. Human CART goes where it changes outcomes and automatic captions where they suffice, and captioners get a factual basis for their rates.
