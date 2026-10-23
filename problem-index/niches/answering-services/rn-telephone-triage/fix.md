# The Caller Who Tells the Story Twice

**Niche:** [[niches/answering-services/rn-telephone-triage/profile|RN Telephone Triage Lines]]
**Industry:** [[industries/answering-services|Telephone Answering Services]]
**Type:** Fix (Pain Point)
**One-liner:** The operator takes the parent's details and symptoms, transfers to the triage nurse, and the nurse starts again from "what's going on?", adding minutes to calls that already average about a quarter of an hour.
**Tags:** #large-language-models #transformers #data-integration #workflow-orchestration #quick-win #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to put a nurse licensed in the caller's state on the line within minutes at 3 a.m. and reach a protocol-correct disposition that keeps safe callers out of the emergency department, and whoever covers every state a practice's patients call from with the shortest wait for a nurse takes the account.

## The Problem
Many services front triage with an unlicensed operator who collects demographics and the reason for calling, then warm-transfers or queues the call for a nurse. A triage provider cites an industry average of 14.3 minutes for clinician-handled calls plus two minutes for the unlicensed front end. The operator's notes often do not reach the nurse's software, so the caller repeats everything, sometimes while frightened and holding a sick child.

## Why It's Still Broken
The answering platform and the triage software are different products from different vendors, often at different companies, and the hand-off was built as a phone transfer.

## What a Fix Looks Like
A structured pre-triage record (patient, age, callback number, chief complaint, red-flag answers, the caller's own words) passed with the call into the nurse's encounter. A draft protocol suggestion from the stated complaint is shown for the nurse to accept or change, and the transcript is available if the nurse wants to hear the original.

## Who Feels the Pain
Callers repeating themselves; nurses losing minutes per call during peaks; practices paying per minute for duplication.

## Impact If Fixed
A minute or two saved per triage call across peak hours shortens the wait for the next caller, which is the contest the niche is fought on.
