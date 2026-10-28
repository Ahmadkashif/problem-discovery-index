# A Care Summary That Follows the Season

**Niche:** [[niches/community-health-centers/agricultural-worker-health-programs/profile|Agricultural Worker Health Programmes]]
**Industry:** [[industries/community-health-centers|Community Health Centers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A farmworker with diabetes or hypertension arrives at a new state's health center each season with no record, and the clinic repeats labs, guesses at doses and loses the referral that was pending two states ago.
**Tags:** #large-language-models #transformers #data-integration #workflow-orchestration #worker-facing #quick-win
**Contested on:** Every serious competitor in this niche is fighting to keep a mobile agricultural worker's chronic care continuous as the worker moves between seasons, farms and states, and whoever keeps the largest share of returning workers with hypertension or diabetes still controlled at their first visit of the season takes the account.

## The Problem
Records stay where they were made. Exchange networks require the receiving clinic to know where to look, and the worker may not know the name of last season's clinic.

## Why Nobody Has Built This
The population is small for national vendors, it moves across state HIE boundaries, and it is wary of anything that looks like tracking. Consent and language barriers make a generic patient portal useless.

## What to Build
A worker-held summary sent by text in the worker's language, holding problems, medications, last readings and open referrals, with a code the next clinic can scan to pull the full record through national exchange. An LLM drafts the summary from the chart at the last visit of the season. The worker controls who sees it.

## Target Customer
330(g) awardees and the networks of migrant health centers along the main migration streams.

## Impact If Built
If 40% of returning chronic patients arrived with a summary (estimate), a clinic seeing 2,000 such patients a season would avoid ~800 repeat intakes and duplicate lab panels, roughly ~$80,000 of avoidable cost, and start those patients' first visit with last season's readings and doses, which is where control is kept or lost (estimate).
