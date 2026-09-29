# The Job That Restarts From Zero

**Niche:** [[niches/ai-inference-providers/batch-and-throughput-inference/profile|Batch & Throughput Inference]]
**Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Type:** Fix (Pain Point)
**One-liner:** A twelve-hour batch job interrupted at hour nine starts again from the beginning, which is why nobody runs these jobs on the cheap interruptible capacity that suits them perfectly.
**Tags:** #automation #workflow-orchestration #evaluation-metrics #data-integration #descriptive-statistics #revenue-impact #quick-win #time-series-forecasting
**Contested on:** Every serious competitor in this sub-niche is fighting to deliver the lowest cost per million tokens by exploiting capacity nobody else can use — and whoever does that takes the account, because the buyer has no latency requirement and therefore no other criterion.

## The Problem
A job processing forty million documents is nine hours in when the underlying instance is reclaimed. There is no record of which documents completed, no durable store of the results produced so far, and no way to resume — so the job restarts, the nine hours are wasted, and the team concludes that interruptible capacity is unusable for this. They move to reserved hardware at three times the price. The work is item-level and independent, which makes it about the most naturally resumable workload that exists, and nothing in the product treats it that way.

## Why It's Still Broken
Batch was bolted onto an interactive serving path where requests are short and resumption is meaningless, so the machinery was never needed. Durable intermediate storage is an operational cost providers would rather not carry for a discounted product. Customers work around it by sharding jobs themselves, which works and hides the problem from the provider. And the cheap capacity that would make this valuable is not offered, so the resumption gap never becomes acute.

## What a Fix Looks Like
Make the job resumable by construction. Track completion at item granularity in durable storage and write results incrementally, which is straightforward for independent items and turns an interruption into a pause — this single change is what makes interruptible capacity viable for the workload. Resume automatically on a new instance, including a different accelerator type, since the job's state is a completion set rather than a process image. Pre-emptively checkpoint on an interruption warning where the platform provides one, which costs seconds. Report progress and projected completion continuously, so a team can see whether Friday is still achievable and act if it is not. Make partial results retrievable at any time, since a job at ninety percent is frequently useful and currently yields nothing until it finishes. Handle poison items — a document that reliably fails — by isolating and reporting them rather than failing the job, which is the most common cause of a large job dying near the end. Deduplicate on resume so items are not processed twice, which matters when the customer is billed per token. And price interruptible capacity to reflect that resumption is now cheap, because the whole point of the fix is to make the cheap tier usable.

## Who Feels the Pain
Data teams paying reserved prices for work that could run on spot; providers whose troughs stay empty because the product cannot survive an interruption; and engineers hand-rolling sharding and checkpointing that should be in the platform.

## Impact If Fixed
Item-level completion tracking turns an interruption into a pause for a workload that is naturally resumable, and it is the precondition for the entire cost advantage this sub-niche rests on. Retrievable partial results make a ninety-percent job useful where today it yields nothing.
