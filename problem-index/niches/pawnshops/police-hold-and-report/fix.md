# The Hold Tag on the Shelf

**Niche:** [[niches/pawnshops/police-hold-and-report/profile|Police Hold-and-Report Compliance]]
**Industry:** [[industries/pawnshops|Pawnshops]]
**Type:** Fix (Pain Point)
**One-liner:** A police hold arrives as a phone call or letter, becomes a paper tag on an item in the back, and is either released late or forgotten until the item is sold by mistake.
**Tags:** #large-language-models #compliance #workflow-orchestration #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to get every transaction reported in each jurisdiction's required form by its deadline, and every hold released on its exact date, straight from the pawn ticket, and whoever makes that automatic across every location's rules takes the account.

## The Problem
When a detective matches a pawned item to a burglary report, the store must keep it — unsold, unredeemed, unaltered — until the hold is released or the item seized. Holds are rare (Oregon reports a police pickup rate of 0.094%), so stores handle them by habit: a tag, a note in a drawer. Items are sold while on hold, or held for months after the case closed because nobody asked for the release.

## Why It's Still Broken
The POS treats a police hold as an inventory status at best, with no officer, case number, expiry or release document attached, and no prompt to follow up.

## What a Fix Looks Like
Record each hold as an object on the item: requesting agency and officer, case number, date, the statutory or agreed duration, follow-up reminders, and the release or seizure document scanned to it. Block sale, redemption and listing while it is open.

## Who Feels the Pain
Store managers fielding detectives' calls; owners whose money is tied up in held items; clerks who sell a held item and face the consequences.

## Impact If Fixed
No held item is sold by mistake, held stock is released promptly when cases close, and the store can answer a detective's question in seconds.
