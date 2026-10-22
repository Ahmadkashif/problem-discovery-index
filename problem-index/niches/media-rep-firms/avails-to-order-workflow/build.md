# A Revision Translator for Pairs Without a Pipe

**Niche:** [[niches/media-rep-firms/avails-to-order-workflow/profile|Avails, Proposals & Order Exchange]]
**Industry:** [[industries/media-rep-firms|Media Representative Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Order exchange platforms carry structured orders between integrated systems; revisions that arrive as emails, and pairs that aren't integrated, still get typed by hand.
**Tags:** #large-language-models #transformers #seq2seq #evaluation-metrics #automation #workflow-orchestration #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to move an avail request, proposal, order and every revision between the agency's buying system and each station's traffic system without anyone re-keying it, and whoever closes the re-keying gap for the most agency–station pairs becomes the default pipe for spot.

## The Problem
A buyer emails: "drop week of 11/4 in all markets, move 30% of early news to late news, add :15s". The rep's assistant translates that into line changes for each station's order and types them into each traffic system, then confirms. Integration platforms help only when the revision comes through the buying system and the station is connected.

## Why Nobody Has Built This
Exchange vendors compete on integrations, not on understanding free text. Free-form revisions were unreadable by software until recently.

## What to Build
A translator that reads revision emails and revised buying-system exports, and produces an exact line-level change list per station. It applies the list through any available integration, or emits a paste-ready change set where none exists, and tracks confirmation. It learns each agency office's phrasing from historical email–order pairs. Every applied change carries a confidence, and low-confidence lines go to a human.

## Target Customer
Heads of sales operations at rep firms and station groups.

## Impact If Built
The gap the integration platforms leave closes without waiting for every agency and station to connect, which is the coverage contest this niche turns on.
