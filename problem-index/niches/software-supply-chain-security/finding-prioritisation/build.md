# A Severity Score From Somebody Who Has Never Seen the Application

**Niche:** [[niches/software-supply-chain-security/finding-prioritisation/profile|Finding Prioritisation]]
**Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A scan returns thousands of findings, a handful matter, and the tools report a severity score computed by someone who has never seen the application — which is why the output is filed rather than fixed.
**Tags:** #gradient-boosting #logistic-regression #graph-theory #bayesian-inference #confidence-intervals #evaluation-metrics #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to turn thousands of findings into the handful that matter for this application — and whoever does that takes the account, because the ratio between what the category reports and what is worth acting on is its central unresolved problem.

## The Problem
A scan of a service returns one thousand four hundred findings, of which two hundred and ten are rated high or critical. The security engineer works through them. Most concern code paths the application never executes; several are in a library used only by a development tool; one is in a parser the application calls on user input and is genuinely urgent. The engineer finds it on the second day. The severity ratings that put two hundred and ten items ahead of it were assigned by a published scoring process that knew nothing about this application, its code, its configuration or its exposure, and the tool presented them in that order.

## Why Nobody Has Built This
The published severity rating is free, standardised and universally available, so it became the field's currency despite being a property of the vulnerability rather than of the situation. Contextual prioritisation requires reachability analysis, configuration understanding and exposure assessment, which are harder and which the vendors have implemented with varying rigour and sold as a premium tier. The organisation's own dismissal history is a strong prior and is thrown away every night when the scan regenerates. And the raw count is the metric reported to leadership, which rewards detection rather than prioritisation.

## What to Build
Compute priority from the situation rather than reporting severity from the vulnerability. Combine the factors that actually determine whether a finding matters: reachability from the application's own code, exploitability in its configuration, exposure of the affected component to untrusted input, evidence of exploitation in the wild, the asset's own criticality, and the compensating controls in place — each of which is obtainable and none of which is in a published severity score. Use the organisation's own history as a prior: a finding of a class they have dismissed forty times before is unlikely to be the one that matters, and that record exists and is discarded. Report a small ranked list with the reasoning, since the output's purpose is to be acted on and a list of two hundred is not. State the dismissals persistently, so a finding assessed as not applicable never returns — which is the security engineer niche's central complaint. Report the residual honestly, since prioritisation means deferring things and an honest statement of what is deferred and why is a stronger position than a queue nobody reads. And validate against outcomes, since the only real test is whether the findings ranked highest are the ones that turn out to matter, and that is checkable against incidents and published exploitation.

## Target Customer
Application security leadership, the security engineers carrying the queue, and the composition analysis vendors for whom prioritisation is now the only differentiation left.

## Impact If Built
The category's output is ignored because it is unprioritised, and the factors that would prioritise it are obtainable and mostly unused. Persisting dismissals alone removes a large share of a queue that is currently regenerated nightly.
