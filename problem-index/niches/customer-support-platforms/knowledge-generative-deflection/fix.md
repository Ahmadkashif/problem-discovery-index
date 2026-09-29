# Nobody Measures the Wrong Answer Rate

**Niche:** [[niches/customer-support-platforms/knowledge-generative-deflection/profile|Knowledge & Generative Deflection]]
**Industry:** [[industries/customer-support-platforms|Customer Support Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Deflection is reported as the share of conversations that did not reach an agent, which counts a customer who was told something false and believed it as a success.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #compliance #quick-win #automation #revenue-impact
**Contested on:** Every serious competitor in support deflection is fighting to detect which knowledge has quietly become wrong before it is used to answer a thousand customers — and whoever keeps the corpus true takes the account.

## The Problem
A support organisation reports a deflection rate that has improved substantially since generative answering was deployed, and a cost per contact that has fallen accordingly. Inside that number are customers who received an incorrect answer and did not return — because they gave up, because they believed it, or because they took the wrong action and will return later with a larger problem that is recorded as a separate contact. The metric cannot distinguish any of those from a genuine resolution, and it is the metric the investment was justified on and is reported to the executive who approved it.

## Why It's Still Broken
Non-escalation is the only signal available without additional measurement, and it is cheap, immediate and flattering. Measuring correctness requires sampling and expert review, which is a cost against a metric that currently looks good. And the vendors have no incentive to propose a measure that would reduce their reported performance — particularly where the contract prices resolutions, in which case an incorrect answer that was accepted is revenue.

## What a Fix Looks Like
Sample and review, and report the composition rather than the rate. A random sample of deflected conversations is reviewed by someone qualified to judge whether the answer was correct, complete and appropriate — which is ordinary quality assurance practice applied to the automated channel exactly as it is applied to the human one, and which is conspicuously absent. Classify outcomes: correctly resolved, incorrectly answered, abandoned without resolution, and deflected-but-returned, where the customer came back within a window with a related issue. That last category is computable without any review and is the cheapest immediate improvement, since a deflection followed by a contact about the same thing is not a deflection. Report the wrong-answer rate with severity weighting. Publish it alongside the deflection rate, so the two are read together. And where a contract prices resolutions, settle it on verified resolutions, which is the arrangement both parties should want and only one currently benefits from.

## Who Feels the Pain
Customers who acted on incorrect information; support leaders reporting a cost saving whose composition they cannot state; and the agents who handle the returning contacts that the deflection metric already counted as resolved.

## Impact If Fixed
The deflected-but-returned measure costs a query and immediately corrects the most flattering part of the metric. Sampled correctness review applies the same quality standard to the automated channel that the industry has always applied to the human one, and reporting both together is what makes an outcome-priced contract mean something.
