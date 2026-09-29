# Nobody Measures What Verification Costs in Completion

**Niche:** [[niches/esignature-document-workflow/risk-based-identity-assurance/profile|Risk-Based Identity Assurance]]
**Industry:** [[industries/esignature-document-workflow|E-Signature & Document Workflow]]
**Type:** Fix (Pain Point)
**One-liner:** Every company believes stronger verification reduces completion and none of them knows by how much, on which transactions, or for which signers it fails outright.
**Tags:** #hypothesis-testing #confidence-intervals #descriptive-statistics #evaluation-metrics #logistic-regression #cross-validation #quick-win #compliance
**Contested on:** Every serious competitor in signing assurance is fighting to set the verification level per transaction from its actual risk rather than per account from a default — and whoever does that gives customers both lower fraud and less friction, which are currently traded against each other.

## The Problem
The argument happens in every implementation. Legal wants government identity verification; sales says it will kill completion; somebody splits the difference with knowledge-based authentication; the setting stands for four years. Nobody measures the completion difference, and every platform has the data to measure it — envelopes sent, verification method applied, completion outcome, abandonment point, and the stage at which the signer stopped. The decision is made on assertion in a category that holds the evidence.

## Why It's Still Broken
Analytics in these products report on envelope status rather than on the effect of configuration choices, so the question is not one the dashboard can express. The comparison also needs care, because assurance level correlates with document type and value, and a naive comparison of completion by method will conclude that strong verification destroys completion when it is partly measuring that strong verification is applied to harder transactions. Nobody has framed it as a measurement problem. And the fraud side of the trade-off has no data at all, so even a good completion measurement only illuminates one half.

## What a Fix Looks Like
Measure the completion cost properly and report it. Completion rate by verification method, controlled for document type, value and counterparty relationship — which is a regression rather than a cross-tab and is the difference between a useful number and a misleading one. Abandonment stage within the verification flow, which identifies where specifically people give up and is frequently a fixable interface problem rather than an inherent cost of the method. Verification failure rate for legitimate signers, broken down by available characteristics, since knowledge-based authentication is known to fail systematically for thin-file signers, recent immigrants and young adults, and a company applying it universally is excluding people without knowing it. Time-to-complete by method, which matters as much as completion for transactional flows. And a controlled comparison where volume permits, which is the only way to get a clean answer and which is entirely feasible for high-volume senders. The result is a number to put against the risk in an argument currently conducted with neither.

## Who Feels the Pain
Legal and sales functions arguing annually without evidence; signers excluded by a verification method that cannot identify them; and companies carrying either unnecessary friction or unpriced risk, without knowing which.

## Impact If Fixed
Every platform holds the data and none reports it, so the category's most consequential configuration decision is made on assertion. The legitimate-signer failure rate is the finding most likely to change behaviour, because exclusion is an access problem rather than a conversion one.
