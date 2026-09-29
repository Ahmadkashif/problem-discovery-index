# Build: A True Effective Rate and a Portable Record

**Niche:** [[niches/crowdsourcing-platforms/the-crowdworker/profile|The Crowdworker]]
**Industry:** [[industries/crowdsourcing-platforms|Crowdsourcing Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Measure a crowdworker's real hourly earnings across platforms including every unpaid minute, and give them a portable record of the work they have done.
**Tags:** #descriptive-statistics #confidence-intervals #evaluation-metrics #data-integration #time-series-forecasting #compliance #worker-facing #quick-win
**Contested on:** Whether unpaid time can be captured accurately enough to compute a real rate.

## The Problem

A crowdworker earning across two or three platforms cannot say what they make per hour. The platforms report earnings; none reports the time spent searching for tasks, reading instructions, taking qualification tests, or working on batches that broke and paid nothing.

Academic studies of this market have repeatedly found effective hourly earnings substantially below relevant minimum wages, and those studies are conducted by researchers with instrumentation the workers themselves do not have. The people earning the wage cannot measure it.

The consequences are practical. Without a real rate a worker cannot tell which platform, which requester or which task type is worth their evening, so the allocation of their time is guesswork. And without a portable record, years of work produce nothing they can carry.

## Why Nobody Has Built This

The platforms have no reason. A true effective rate is a smaller number than the headline and would direct workers toward whichever platform treats them best, which is not an outcome any individual platform is optimising for.

Third parties have built parts — earnings trackers and time extensions exist — and stopped short of the whole, mainly because capturing unpaid time requires continuous browser-level instrumentation with all the fragility and terms-of-service risk that implies.

And the workforce is diffuse, low-income and globally distributed, which makes it look like a poor market. That underestimates it: this workforce already builds and maintains tooling collectively, and adoption of something genuinely useful would be fast.

## What to Build

A cross-platform measurement tool and a portable record.

**Capture the whole session, not just the paid part.** Browser-level timing of search, listing browsing, instruction reading, qualification tests, task work and abandoned attempts, attributed to platform and requester. This is the instrumentation that makes the rate real and it is the hard engineering — it must be light, private, and resilient to markup changes.

**Compute the effective rate honestly.** Earnings divided by total time including everything unpaid, per platform, per requester, per task type, with the paid-only rate shown alongside so the gap is visible. The gap is the finding.

**Rank by what actually pays.** Which task types and which requesters produce the best real rate for this worker. Most workers' intuitions here are partly wrong and the correction is worth real money to them immediately.

**Track rejections with evidence.** Automatically retain the submission, the instructions and the timing for every task, so a worker facing a rejection has the record. This is the single most requested thing among experienced workers and it is straightforward local storage.

**Build the portable record.** Task types, volumes, tenure, approval history, qualifications held and platforms worked — owned by the worker, exportable, with no requester-confidential content. In a market where every platform holds a worker's history hostage, a portable record is the only credential this workforce can have.

**Aggregate with consent.** Pooled, anonymised data on realised rates by requester, platform and task type is the market intelligence no individual can produce and the evidence base that researchers, ethics boards and worker organisations currently reconstruct laboriously. Built on explicit, revocable consent, it is also the thing that would most change platform behaviour.

## Target Customer

Crowdworkers directly, especially the substantial group for whom this is meaningful income and who already install extensions. Worker organisations and researchers, for whom the consented aggregate is the dataset the field lacks. And the academic-focused platforms, which compete on treatment and would benefit from a comparison they win.

## Impact If Built

A worker can see what they actually earn per hour worked, which is the number governing every decision they make and which only outside researchers have ever computed. Time gets allocated to what actually pays. Rejections meet a worker with evidence. And the consented aggregate gives this workforce, for the first time, a shared factual basis for what the market pays.
