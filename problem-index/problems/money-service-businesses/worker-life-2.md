# The Analyst Chasing One Sender Across Forty Agents

**Industry:** [[money-service-businesses|Money Service Businesses]]
**Type:** Worker Life Changing
**One-liner:** A BSA analyst at a transmitter spends most of each alert proving that "Mohammad Iqbal", "Muhammed Ikbal" and "M. Iqbal" at three stores are one person splitting transfers, before writing a SAR narrative against a 30-day clock — the part that needs judgement gets the last hour of the day.
**Tags:** #large-language-models #seq2seq #k-nearest-neighbors #word-embeddings #evaluation-metrics #worker-facing #compliance #workflow-orchestration

## The Problem
Structuring — breaking a transfer into pieces to stay under recordkeeping, ID or reporting thresholds — is the most common pattern a transmitter's monitoring system flags. Detecting it depends on knowing who the sender is. At an agent network, the same person can send from many locations, under spellings that vary with the clerk's keyboard and the transliteration of a name from Urdu, Arabic, Amharic or Spanish, with an ID number mistyped once in every few transfers and a phone number that changes. Receivers vary the same way on the other side.

So the analyst's day is entity resolution by hand. Open the alert; search the transaction database for name variants, ID fragments, phone numbers and addresses; build a spreadsheet of the transfers that belong to this person; check whether the receivers are shared with other senders; decide whether the pattern is structuring, a family pooling remittances, or an agent splitting one customer's transfer to avoid an ID check. Then write a SAR narrative that explains all of this to FinCEN in prose. A transmitter files many such reports (estimate: thousands a year at the large firms), and each one has a filing clock. During the months when FinCEN's Southwest Border Geographic Targeting Order applied, analysts in affected regions also processed CTRs at a $200 threshold.

## Why It Matters to the Worker
The job attracts people who want to catch financial crime, and most of their hours go to deduplicating names. The judgement they are good at — this is a family, this is a crew, this agent is in on it — gets compressed into the last minutes before a deadline. Errors are personal: a missed linkage found later by an examiner or a monitor becomes the analyst's finding. Turnover is high and backlogs are visible to management every week.

It is also isolating work. SAR confidentiality means the analyst cannot discuss specific cases outside the team, and rarely learns whether a report led anywhere.

## What a Solution Looks Like
Sender and receiver resolution done before the alert reaches the analyst: a probabilistic identity graph that groups transfers across agents, spellings and scripts, shows the evidence behind each link and lets the analyst split or merge with one click. The alert opens on a timeline of the resolved person's transfers, receivers and agents, with comparable past cases and how they were decided. A first-draft SAR narrative is generated from the resolved timeline and the analyst's decision, in FinCEN's expected structure, for the analyst to edit rather than write.

## Impact If Solved
Hours per alert become minutes, backlogs shrink without adding headcount, and analysts spend their time on the decision they were hired for. Better resolution also reduces both kinds of error the analyst fears most: the structuring ring missed because its members were spelled five ways, and the innocent family flagged because five relatives sent to the same aunt.
