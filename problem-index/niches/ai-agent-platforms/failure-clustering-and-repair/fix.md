# The Prompt That Accretes Special Cases

**Niche:** [[niches/ai-agent-platforms/failure-clustering-and-repair/profile|Failure Clustering & Repair]]
**Industry:** [[industries/ai-agent-platforms|AI Agent Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Every failure adds a sentence to the prompt, the prompt reaches four thousand words of accumulated special cases, and nobody can remove anything because nobody knows what each instruction is holding up.
**Tags:** #large-language-models #evaluation-metrics #hypothesis-testing #confidence-intervals #descriptive-statistics #quick-win #automation #cross-validation
**Contested on:** Every serious competitor in this niche is fighting to turn a stream of individual agent failures into a small number of named, systematically fixable causes — and whoever does that takes the account, because the alternative is patching one case at a time forever.

## The Problem
The system prompt began as two paragraphs describing the agent's role. Two years and four hundred failures later it is four thousand words, most of them beginning "if the customer mentions" or "never". Some instructions contradict others. Several address cases that no longer occur. Nobody knows which are load-bearing, so nobody removes any, and the accumulated instructions now compete for the model's attention with the actual task — which means adding the next one makes something else slightly worse. The team is aware this is happening and has no safe way to stop it.

## Why It's Still Broken
Adding an instruction is the fastest available fix and demonstrably works for the reported case. Removing one requires knowing what it prevents, which nobody recorded. There is no regression suite, so a removal cannot be tested. Prompt growth is invisible as a metric. And each addition is individually reasonable, which is how every accretion problem works.

## What a Fix Looks Like
Attach evidence to every instruction and let it be removed. Record, for each instruction added, the failure case that motivated it and add that case to the regression suite, which is a two-line discipline at the moment of the fix and is what makes every later removal decision possible. Test removals against the suite, so an instruction can be deleted when its case is covered by a better mechanism or no longer occurs — this is the only safe route out and it exists as soon as the evidence is attached. Detect contradictions and redundancy across the prompt, which is mechanically checkable and reliably finds accumulated conflicts. Prefer structural fixes to instructional ones, since a case handled by routing, a tool change or a check is handled reliably, while an instruction is handled probabilistically and competes with every other instruction. Measure prompt length and instruction count as a health metric, so the accretion is visible. Group instructions and test whether whole groups can be replaced by a shorter statement, which is where the large reductions come from. Re-evaluate the full suite on every prompt change, so a fix that breaks two other cases is caught rather than shipped. And periodically rebuild the prompt from the regression suite rather than editing it, which is the equivalent of paying down the debt and is only possible once the suite exists.

## Who Feels the Pain
Reliability engineers afraid to remove anything; agents whose performance is degraded by instructions addressing cases that no longer arise; and the customers whose new failures are partly caused by the fixes for old ones.

## Impact If Fixed
Attaching the motivating failure case to every instruction is a two-line discipline that makes every future removal decision possible. Preferring structural fixes to instructional ones is what stops the accretion at its source, since a routing change is reliable where an instruction is probabilistic.
