# The Voluntary Election That Arrived as an Email

**Niche:** [[niches/trust-companies/institutional-custody-asset-servicing/profile|Institutional Custody & Asset Servicing]]
**Industry:** [[industries/trust-companies|Trust Companies]]
**Type:** Fix (Pain Point)
**One-liner:** Clients still send tender, exchange and rights elections as free-text messages and emails, and a missed or misread election becomes a claim against the custodian.
**Tags:** #large-language-models #bert #compliance #workflow-orchestration #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to deliver each client's positions, cash and corporate-action entitlements without breaks before the client's own NAV and settlement cutoffs, and whoever has the fewest unresolved breaks at the cutoff takes the account.

## The Problem
For voluntary events the custodian must collect each client's decision before its own deadline, which falls ahead of the market deadline. Instructions arrive as structured messages from some clients and as free-format messages, emails or portal comments from others, sometimes with conditions. Analysts re-key them under deadline pressure.

## Why It's Still Broken
Client systems vary, small clients will not adopt structured messaging, and the volume of elective events is too uneven to staff for evenly. Responsibility splits between client service, which receives the email, and operations, which processes it.

## What a Fix Looks Like
Language-model parsing of every incoming instruction into a structured election — account, event, option, quantity, conditions — matched to the event record and the client's position, with anything ambiguous returned to the client immediately and a deadline tracker that escalates unanswered events before the custodian's cutoff.

## Who Feels the Pain
Corporate actions analysts at peak periods; client service officers fielding the claim; and clients whose elections were applied wrongly.

## Impact If Fixed
Fewer re-keyed instructions and earlier escalation remove a recurring source of costly claims, with every election traceable from the client's words to the processed option.
