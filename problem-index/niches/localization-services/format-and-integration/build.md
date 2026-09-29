# The Round Trip That Does Not Break

**Niche:** [[niches/localization-services/format-and-integration/profile|File Format & Integration Engineering]]
**Industry:** [[industries/localization-services|Localization Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Getting the text out and back again is engineering that is redone for every client and every format.
**Tags:** #automation #data-integration #workflow-orchestration #evaluation-metrics #compliance #sets-and-logic #descriptive-statistics #quick-win
**Contested on:** Every serious competitor in this niche is fighting to get content out of a client's systems and back again without an engineer handling every format by hand, and whoever automates that takes the account.

## The Problem
Every engagement begins with extraction: identify what is translatable, pull it out with enough context, preserve everything that must not change, and prove that reinsertion produces a working file. The formats vary by client and change with their tooling. Filters are configured by hand, tested informally, and a mistake produces a broken build or a corrupted document discovered late, in a language nobody at the client can read.

## Why Nobody Has Built This
Filters are configured per client because each client's content is idiosyncratic. Format handling is treated as engineering overhead rather than as a product. Validation of the round trip is manual. And a broken round trip is treated as an incident rather than as a predictable class.

## What to Build
Validate the round trip automatically and reuse what has been built. Round-trip every file before translation begins — extract, reinsert unchanged, verify identity — which is the core and catches the entire class of failure before any work is done. Validate again after translation with length, encoding and structural checks, since a valid round trip with source text does not guarantee one with translated text. Reuse filter configurations across clients with the same formats, which is most of them. Detect the content that will break on reinsertion — length constraints, embedded markup, placeholders, bidirectional text — before it reaches a linguist. Maintain connectors against client systems as they change, which is where silent breakage originates. Preserve and transmit context from the source format, as that is the difference between a translatable string and a guess. Handle the formats that are genuinely hard — design files, subtitles, help systems — properly rather than by manual export. Report which formats and clients generate the most engineering time, which directs the investment. Test connector integrations continuously rather than at setup. And make the validation part of intake rather than something an engineer remembers.

## Target Customer
Language service providers, enterprise localization teams, translation management platform vendors, and integration tooling providers.

## Impact If Built
A broken round trip is discovered late, in a language nobody at the client can read, and the whole class is preventable. Round-trip validation at intake catches it before any translation work begins.
