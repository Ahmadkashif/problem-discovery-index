# A Per-State Notice Rule Engine

**Niche:** [[niches/parking-operators/parking-notice-processing/profile|Parking Notice Processing & Disputes]]
**Industry:** [[industries/parking-operators|Parking Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Whether a parking notice may be sent, and what it must say, now depends on the state, and nothing checks each notice before it is mailed.
**Tags:** #large-language-models #bert #transformers #evaluation-metrics #compliance #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to recover unpaid sessions by lawful notice, and whoever collects the largest share of notice value after voids, refunds and upheld disputes takes the account.

## The Problem
Processors use one template per client with state tweaks added by hand. Maine now requires specific fields and a 10-business-day window, and bars plate recognition at public lots subject to its statute's exceptions. Other states are drafting their own rules, and DPPA suits test the lookups themselves.

## Why Nobody Has Built This
The rules are new and scattered across consumer-protection, motor-vehicle and privacy statutes. Processors are small, and their counsel works case by case.

## What to Build
A rule engine that encodes, per state and lot, whether plate recognition and a registered-owner lookup are permitted for this purpose, and checks signage and fee posting from lot photos. It verifies required notice fields and payment windows, applies any fee caps and credit-reporting bans, and enforces image retention limits. Every notice is checked before mailing; failures are blocked with the reason. A language model classifies incoming disputes (paid but misread, plate mismatch, signage, emergency, other) and drafts replies citing the governing rule, and dispute outcomes flow back to the misread model.

## Target Customer
Notice processors, operators running gateless lots in several states, and their general counsel.

## Impact If Built
Blocking non-compliant notices avoids exposure that runs to treble the fee in Maine and $2,500 per DPPA violation (search summary). Cutting upheld disputes by a third (estimate) raises net collection on every notice mailed.
