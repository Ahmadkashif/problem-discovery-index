# Denial Appeals Written Without the Contract or the Chart

**Industry:** [[general-hospitals|General Hospitals]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** LLM appeal writers and denial worklists already exist, but a hospital's winning appeal depends on its payer contract language, the payer's own medical policy and the two-midnight rules for Medicare Advantage, none of which generic tools read.
**Tags:** #large-language-models #transformers #gradient-boosting #evaluation-metrics #workflow-orchestration #automation #revenue-impact

## The Problem
A 400-bed hospital receives thousands of denials a month. The expensive ones are clinical. The payer says the three-day stay should have been observation, downgrades a sepsis DRG to a urinary tract infection, or refuses the discharge to a skilled nursing facility. Premier's 2025 survey found ~15% of claims to private payers denied first time, ~70% overturned on appeal and $80.16 spent per Medicare Advantage appeal. That works out to ~$25.7B a year of administrative cost across providers. A denial nurse or physician advisor reads the denial letter, opens the chart, finds the evidence (lactate, organ dysfunction, the physician's documented expectation of a two-midnight stay) and writes an appeal against a deadline. Many of the levels have 60-day windows or shorter (recalled). Denials that miss the window are written off.

## What Already Exists
Denial management worklists in Epic Resolute and the clearinghouses (Waystar, Experian), outsourced revenue cycle companies (R1, Ensemble, Optum), and a wave of LLM appeal drafters from AKASA, Smarter Technologies, Commure and smaller startups. General-purpose LLMs will write a fluent appeal letter from a pasted chart summary. Clinical criteria come from MCG and InterQual.

## The Customisation Gap
A generic appeal argues medicine. A winning hospital appeal also argues the contract and the rules. It needs to know:

- whether this payer's contract requires it to honour the hospital's admission order, or bans retrospective DRG downgrades after a prior authorisation;
- which clinical criteria set the contract names;
- whether the Medicare Advantage plan is bound by traditional Medicare's two-midnight benchmark under CMS-4201-F (recalled);
- what this specific payer's medical policy says about the diagnosis (for sepsis, often Sepsis-3 rather than the SEP-1 definition the coders used).

It also needs the appeal level and its deadline, and the hospital's own record of which arguments won against which payer. That record sits in remittance files and appeal outcomes nobody has joined to the letter that produced them. The customisation is a contract-and-policy layer, plus outcome learning per payer, on top of an extraction and drafting engine that already exists.

## Impact If Solved
If appeals were drafted from the contract, the payer policy and the chart together, a denial nurse could move from ~4–6 appeals a day to ~15–20 (estimate). The hospital could appeal small-dollar clinical denials it now writes off, and the CFO would finally know which payer behaviours to take into the next contract negotiation.
