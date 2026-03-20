# State-Aware Compliance Script Generation

**Industry:** [[collections-agencies|Collections Agencies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic script builders exist but none dynamically adjust collection scripts for the 50+ state-level FDCPA variations, Reg F requirements, and client-specific restrictions in real time.
**Tags:** #large-language-models #transformers #attention-mechanisms #word-embeddings #transfer-learning #evaluation-metrics #compliance

## The Problem
Collection agents must follow different disclosure requirements, call frequency limits, and communication restrictions depending on the debtor's state of residence, the debt type (medical, credit card, student loan), and the creditor's specific compliance mandates. A collector working accounts across 15 states in a single shift must mentally track dozens of rule variations — New York's required mini-Miranda language differs from California's, Texas has unique time-barred debt disclosures, and medical debt in several states now requires additional notices. Compliance officers manually maintain script libraries that run to hundreds of pages, and agents routinely get written up for using the wrong state's disclosure.

## What Already Exists
Compliance management platforms (ComplianceEase, Provana) offer call monitoring and post-hoc script adherence scoring. Collection platforms include static script trees that branch on debt type. General-purpose script generators can produce call guides but have no awareness of FDCPA/Reg F/state-level nuance or the real-time context of which account the agent is currently working.

## The Customisation Gap
The system must ingest a continuously updated regulatory knowledge base (state statutes, CFPB guidance, consent decrees) and generate contextual scripts that adapt in real time as the agent navigates a call — surfacing the correct mini-Miranda, time-barred debt disclosure, cease-and-desist acknowledgment, or payment plan terms based on the specific account's jurisdiction, debt type, and creditor rules. It needs to handle mid-call state changes (debtor says they moved to a different state) and flag when an agent deviates from required language before the call ends, not after.

## Impact If Solved
Compliance violation rates drop by 60-80% on monitored calls. New agent ramp-up time decreases from 4-6 weeks to 1-2 weeks as the script engine handles regulatory complexity. Agencies reduce legal exposure from consent decree violations, which can carry penalties of $1,000+ per call.
