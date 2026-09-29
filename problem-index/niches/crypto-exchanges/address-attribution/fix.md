# Taint That Never Decays

**Niche:** [[niches/crypto-exchanges/address-attribution/profile|Address Attribution & Taint Propagation]]
**Industry:** [[industries/crypto-exchanges|Crypto Exchanges]]
**Type:** Fix (Pain Point)
**One-liner:** Funds seven hops and three years removed from an incident are treated exactly like funds that came straight from it.
**Tags:** #graph-theory #confidence-intervals #evaluation-metrics #quick-win #compliance #descriptive-statistics #hypothesis-testing #automation
**Contested on:** Every serious competitor in this niche is fighting to say who actually controls an address and how far illicit taint legitimately travels through a public ledger — and whoever attributes most accurately, with a confidence they can defend, owns the input every downstream decision consumes.

## The Problem
An exchange was hacked years ago. The funds moved, were traded, passed through services, changed hands many times. A customer receives coins from a mainstream platform and their deposit is flagged because a tracing path connects them, at some remove, to that incident. The propagation rules that produced the connection — which accounting method, how many hops, what proportion, whether time matters — are not visible to the exchange applying them and not consistent between vendors. The result is a flag with no sense of proportion.

## Why It's Still Broken
Propagation rules were product decisions made by vendors, so the exchange consuming the flag never had to think about them — the input arrived as a fact and was treated as one. Conservative propagation is safe for everyone except the customer. There is no agreed standard for how taint should decay. And nobody measures how many flags come from distant, high-hop, low-proportion paths.

## What a Fix Looks Like
Make the path visible and weight it. Show the hop count, proportion and elapsed time on every flag, which is the fix and is data the tracing already computed but does not surface. Weight the risk by those factors rather than treating any path as equivalent, since a direct transfer and a seven-hop fractional trace are obviously different and are currently the same. Report the distribution of flags by hop distance, which is a single query and will show immediately how much of the queue is distant tracing. Set separate thresholds by path proximity, because one threshold across all distances guarantees the wrong answer at both ends. Let taint decay with time and intermediate services, as a decade-old incident propagating undiminished is a modelling choice nobody made deliberately. Compare vendors' propagation on the same case, since disagreement is the clearest evidence that these are choices rather than facts. Document the exchange's own propagation policy, which is required to defend a freeze and currently does not exist. Exclude paths through large mixing services where proportion becomes meaningless, because attributing a fraction of a pool to a specific customer is not an inference the data supports. Prioritise analyst time by path strength, so the strong cases are not queued behind the weak. And measure how many distant-path flags ever resolve as genuine, which will settle the question empirically.

## Who Feels the Pain
Customers flagged for receiving ordinary funds; analysts tracing seven-hop paths that will not resolve; exchanges applying rules they cannot explain; and the credibility of tracing evidence generally.

## Impact If Fixed
Propagation rules were vendor product decisions and arrived as facts, so nobody applying them chose them. Surfacing hop distance, proportion and age — all already computed — turns an undifferentiated flag into a proportionate one.
