# Knowing Who Is Actually in the Room

**Niche:** [[niches/ux-research-agencies/participant-verification/profile|Participant Verification]]
**Industry:** [[industries/ux-research-agencies|UX Research Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The study's entire validity rests on eight self-reports made by people paid to qualify.
**Tags:** #logistic-regression #evaluation-metrics #confidence-intervals #compliance #data-integration #descriptive-statistics #k-nearest-neighbors #automation
**Contested on:** Every serious competitor in this niche is fighting to establish that the eight people in a study were who they said they were, when screening is self-report against people whose income depends on passing — and whoever verifies them takes the account.

## The Problem
A study recruits people who match a profile, and the matching is done by asking them. Participants who make part of their living from research learn which answers qualify, and will give them. Some proportion of any study's participants are therefore not the population the study was about, and nothing detects it. Every finding is then generalised to a population that was partly absent from the room.

## Why Nobody Has Built This
Verification costs money and slows recruitment, both of which the schedule punishes. Panels have an interest in their participants qualifying. No cross-panel identity exists, so a participant can appear repeatedly under different profiles. And the failure is invisible — a wrongly qualified participant produces a session that looks like any other.

## What to Build
Verify the attributes the study actually depends on, and detect the professional. Verify the specific screening attribute the study's validity rests on — through behaviour, documentation or a task rather than a question — which is the core and is the only attribute worth the cost. Detect professional participants through response patterns, session behaviour and cross-study frequency, since they are the identifiable population and their presence is the main risk. Resolve identity across panels where possible, which is where repeat participation hides. Use behavioural qualification rather than stated qualification wherever the attribute allows, as showing beats claiming. Measure screener failure rates by asking verifiable questions among the unverifiable ones, which sizes the problem cheaply. Flag sessions where the participant's behaviour contradicts their stated profile, which is frequently obvious in the recording and never recorded. Track participation frequency per person across the agency's studies. Report the verification status of each participant in the findings, so the sample's quality is visible rather than assumed. Adjust or caveat findings where the sample is doubtful rather than reporting regardless. And share fraud signals across agencies, since the professional population is shared and nobody's individual detection is sufficient.

## Target Customer
UX research agencies and in-house teams, research operations, recruitment panels, and identity and fraud detection vendors.

## Impact If Built
A study's validity rests on self-reports made by people paid to qualify, and nothing detects the mismatch. Verifying the one attribute the study depends on, and detecting the professional population, is what makes the sample assertable.
