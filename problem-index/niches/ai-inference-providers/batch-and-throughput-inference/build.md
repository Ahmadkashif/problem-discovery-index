# A Deadline in Days, Priced Like a Deadline in Milliseconds

**Niche:** [[niches/ai-inference-providers/batch-and-throughput-inference/profile|Batch & Throughput Inference]]
**Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Offline inference jobs have deadlines measured in days and are served on infrastructure built to deliver a first token in milliseconds, which prices them for a guarantee they do not want.
**Tags:** #dynamic-programming #convex-optimization #markov-decision-processes #time-series-forecasting #revenue-impact #evaluation-metrics #automation #workflow-orchestration
**Contested on:** Every serious competitor in this sub-niche is fighting to deliver the lowest cost per million tokens by exploiting capacity nobody else can use — and whoever does that takes the account, because the buyer has no latency requirement and therefore no other criterion.

## The Problem
A data team needs eighty million support tickets classified by Friday. They submit them through the same endpoint a chat product uses, at the same per-token price with a modest batch discount, served on the same reserved hardware that is sitting idle at three in the morning and contended at two in the afternoon. The job has enormous flexibility — it can run overnight, it can be interrupted, it can take until Friday — and none of that flexibility is expressible or rewarded. The provider, meanwhile, has troughs it cannot fill and spot capacity it cannot use for interactive work.

## Why Nobody Has Built This
Batch looks like the same product at higher volume, which hides that its economics are inverted. Building for interruptible capacity requires checkpointing and rescheduling machinery that the interactive path does not need. Deadline-aware scheduling requires the scheduler to model time horizons it currently has no concept of. And pricing batch much lower invites the question of why interactive costs what it does, which is a conversation providers prefer not to start.

## What to Build
Make flexibility the product. Accept a deadline with every job and schedule against it, so a job due Friday runs in the troughs and a job due in an hour does not — which is the central mechanism and turns a cost problem into a scheduling one. Run on interruptible and spot capacity as the default, with checkpointing so an interruption costs minutes, which the fix note develops and which is where the cost advantage actually comes from. Offer a price-versus-deadline menu at submission: this costs a third if you can wait until tomorrow, which is a choice the customer would take gladly and is offered by nobody. Fill the provider's own troughs first, since batch work is the natural complement to interactive demand and scheduling it into the gaps improves fleet utilisation and batch cost simultaneously — this is the alignment that makes the whole niche work. Report progress and projected completion against the deadline, because that is what a data team needs and a job that silently might not finish by Friday is the failure they fear. Support prioritisation within a job, so partial results are usable if the deadline slips. Batch aggressively without latency concern, using the very large batch sizes the interactive path cannot. And expose cost per million tokens as the headline metric, since that is the only number this buyer is comparing.

## Target Customer
Data engineering and analytics teams running offline inference, and the providers whose idle troughs are the natural supply for it.

## Impact If Built
The flexibility these jobs have is total and entirely unexpressible today. Scheduling batch into the provider's own troughs improves utilisation and cuts the customer's bill at the same time, which is the rare alignment that makes the whole sub-niche work.
