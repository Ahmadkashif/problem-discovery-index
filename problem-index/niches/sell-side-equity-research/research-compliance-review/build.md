# A Reader for Rule 2241

**Niche:** [[niches/sell-side-equity-research/research-compliance-review/profile|Research Compliance Review]]
**Industry:** [[industries/sell-side-equity-research|Sell-Side Equity Research]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Disclosure blocks are generated automatically, but whether the report body meets the rules is still checked by a supervisory analyst reading it line by line.
**Tags:** #large-language-models #bert #evaluation-metrics #compliance #workflow-orchestration #automation
**Contested on:** Every serious competitor in this niche is fighting to clear every research report for release inside the earnings-morning window with zero disclosure or quiet-period errors — and whoever does that best lets the department publish first without a FINRA finding.

## The Problem
The checks that matter are in the text: a price target with no stated valuation basis or risks; a rating change without the required language; a peer company discussed in the body that carries its own disclosure obligations; promotional language on a company where the firm is pitching for a mandate.

## Why Nobody Has Built This
Authoring vendors stopped at structured disclosures; surveillance vendors focus on communications after the fact; and the review sits behind the information barrier, which makes vendors cautious about handling pre-publication research.

## What to Build
A pre-review pass that extracts every issuer mentioned, reconciles them against the disclosure database and control-room lists, classifies passages against a Rule 2241 and house-procedure checklist, and returns flags with the rule cited. Trained on the firm's own history of supervisory edits, deployed inside the barrier.

## Target Customer
Heads of research compliance and supervisory analyst teams at broker-dealers.

## Impact If Built
Faster release on report mornings and an auditable record of every check performed.
