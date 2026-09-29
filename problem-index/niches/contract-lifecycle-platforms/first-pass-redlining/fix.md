# The Tool Never Learns From the Correction

**Niche:** [[niches/contract-lifecycle-platforms/first-pass-redlining/profile|First-Pass Redlining]]
**Industry:** [[industries/contract-lifecycle-platforms|Contract Lifecycle Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A lawyer overrides the same suggestion for the eleventh time and the system makes it again on the twelfth contract, because corrections are discarded.
**Tags:** #descriptive-statistics #k-means-clustering #bert #evaluation-metrics #confidence-intervals #hypothesis-testing #quick-win #automation
**Contested on:** Every serious competitor in automated redlining is fighting to make the routine edits correctly without counsel and to know reliably when a provision is not routine — and whoever holds that boundary takes the legal function, because being wrong once on the wrong clause ends the deployment.

## The Problem
The review tool suggests striking a mutual non-solicitation clause, because the playbook says so. Counsel reinstates it every time, because the playbook was written before the company entered a market where mutual non-solicitation is standard and expected. The tool has now been overridden on this point forty times across four lawyers. It will suggest it again tomorrow. Nobody has noticed the pattern, because rejected suggestions are not counted, and the playbook has not been updated, because nobody owns noticing.

## Why It's Still Broken
Acceptance and rejection are treated as interface events rather than as data, so they are logged for telemetry at best and never analysed. Updating the playbook from observed behaviour requires someone to own the playbook as a living artefact rather than as a document produced once. And there is a reasonable caution about a system that changes its legal positions automatically — which argues for surfacing the pattern to a human rather than for discarding the signal entirely, which is what happens now.

## What a Fix Looks Like
Treat every override as evidence. Record acceptance, rejection and modification per suggestion with the provision, the contract type and the counterparty, which is logging and produces the dataset immediately. Report the consistently rejected suggestions, ranked by frequency, which is a short list and is a direct instruction about what in the playbook is wrong. Report the consistently modified ones too, since a suggestion that is always edited the same way is a playbook position stated slightly wrong. Distinguish a rejection specific to one lawyer from one shared across the team, since the first is a disagreement to resolve and the second is a policy error. Propose the playbook update explicitly, for a human to approve, rather than either changing silently or doing nothing. And show the suggestion's historical acceptance rate alongside it, so a lawyer seeing a suggestion that has been rejected forty times knows that before spending time on it.

## Who Feels the Pain
Lawyers correcting the same thing repeatedly; legal operations maintaining a playbook that has drifted from practice without evidence of how; and vendors whose products appear less accurate than they are because a stale playbook is attributed to the tool.

## Impact If Fixed
Logging acceptance and rejection is trivial and produces a ranked list of playbook errors immediately. The historical acceptance rate shown inline is a small change that saves the lawyer's attention on suggestions the team has already collectively rejected.
