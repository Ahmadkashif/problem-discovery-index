# A Break With No Source

**Niche:** [[niches/embedded-finance-platforms/ledger-integrity/profile|Ledger Integrity]]
**Industry:** [[industries/embedded-finance-platforms|Embedded Finance Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The reconciliation is off by four hundred dollars, nobody can say which transactions caused it, and the investigation is a person reading ledger entries.
**Tags:** #graph-theory #change-point-detection #automation #quick-win #evaluation-metrics #data-integration #descriptive-statistics #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to prove continuously that the sub-ledger's record of who owns what matches the money actually held at the bank — and whoever can prove it at any moment rather than at month end wins the accounts where a break means customers lose access to their money.

## The Problem
The daily reconciliation reports a variance. It is small, and it is unexplained. Finding it means someone pulling the day's ledger entries, the bank file, the network settlement report and the authorisation log, and looking for the combination that accounts for four hundred dollars across two hundred thousand transactions. It usually turns out to be a timing difference or a duplicate reversal, and finding that out takes most of a day. The same shapes recur constantly and nothing learns them.

## Why It's Still Broken
Break investigation was always manual, so the tooling stopped at reporting the variance — the process was designed to surface the number, not to explain it, and explaining it was assumed to be judgement. Ledger entries do not carry enough lineage to trace a balance back to its causes. Most breaks are small enough to be tolerated rather than fixed, which removes the pressure. And the recurring shapes are known to the people investigating them and recorded nowhere.

## What a Fix Looks Like
Attribute the break automatically. Search for transaction combinations that account for the variance, which is a mechanical matching problem and resolves most breaks without a person. Classify against the known shapes — timing, duplicate, unmatched reversal, fee posting, rounding, network adjustment — since the same handful recur and classification alone routes the work. Record every resolved break with its cause, because that corpus is what makes classification improve and it is currently discarded. Show the variance decomposed by programme, which narrows the search immediately and is a straightforward grouping nobody displays. Compare against yesterday's break profile, so an ordinary timing variance is distinguished from something new. Age and escalate breaks explicitly, since small tolerated breaks accumulate silently. Flag the break that is not one of the known shapes, because that is the one worth a person's day. Give investigators the four sources in one view rather than four exports, which is most of the manual time. Track investigation time per break type, so the automation targets itself. And alert on the trend, since a growing tolerance threshold is a signal about the system rather than about the day.

## Who Feels the Pain
Finance operations staff spending days on four-hundred-dollar variances; engineers pulled into investigations; and platforms whose small tolerated breaks are accumulating unexamined.

## Impact If Fixed
The process was built to surface the variance and assumed the explanation was judgement. Combinatorial attribution plus classification against the recurring shapes resolves most breaks without an investigator and isolates the one that matters.
