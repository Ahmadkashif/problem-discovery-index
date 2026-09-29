# Job Matching Is the Product and Is Done by Hand

**Niche:** [[niches/hr-consultants/compensation-survey-publishers/profile|Compensation Survey Publishers]]
**Industry:** [[industries/hr-consultants|HR Consultants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every pay benchmark in the economy rests on someone deciding that this employer's job title means the same thing as that one's, and that decision is made by a person reading a description.
**Tags:** #text-classification #word-embeddings #large-language-models #k-means-clustering #evaluation-metrics

## The Problem
A compensation survey works by mapping thousands of employers' internal jobs onto a common benchmark architecture, so that pay for "Senior Software Engineer II" at one company is comparable to "Software Development Engineer" at another. Every percentile the industry quotes depends on that mapping being right.

It is done by analysts reading job descriptions and titles and assigning a benchmark code, supported by matching guides and participant self-reporting. It is slow, it is the largest labour item in survey production, and it is the single largest source of error in the output — a mismatched job pulls the market rate for an entire benchmark in a direction nobody can trace afterwards.

Participants make it harder. They self-match to save effort and they self-match optimistically, because a job matched to a higher benchmark makes their pay look competitive. Analysts catch some of this and cannot possibly catch all of it across thousands of submissions on an annual cycle.

## Why Nobody Has Built This
The job architecture is the firm's crown jewel and its maintenance is a craft. Matching has always been done by people who know the architecture intimately, and the professional view is that judgment about job content cannot be automated — a view formed when the alternative was keyword matching against titles, which genuinely does not work.

The economics also hid the problem. Matching labour scaled with survey participation, participation grew slowly, and the cost was absorbed. Pay transparency legislation changed that: employers now need ranges they can post publicly and defend, demand for granular local benchmarks rose sharply, and the same analyst pool has to cover far more cuts.

And accuracy was never measured. A mismatch produces a slightly wrong percentile that nobody can detect, so the process has run for decades without anyone knowing its error rate.

## What to Build
A semantic matching engine that proposes and scores matches, with analysts adjudicating rather than performing them.

**Match on content, not title.** A job description, its reporting line, its required experience, and its scope carry the signal; the title carries noise and marketing. Embedding descriptions against the benchmark architecture's own definitions is the core operation, and the firm has decades of analyst-confirmed matches to fit and validate against — the training set already exists, in the archive.

**Return a distribution over benchmarks with confidence.** Many jobs sit genuinely between two benchmarks, and forcing a single code discards information the survey could use. Where confidence is low, the analyst gets a ranked shortlist with the reasoning, which is a very different task from reading from scratch.

**Flag self-match optimism.** A participant's self-matched job whose description sits closer to a lower benchmark is exactly the case an analyst should see, and the model identifies it directly. This is the largest single quality improvement available and it is currently unaddressed.

**Detect architecture drift.** Jobs that consistently match poorly to everything are the signal that the architecture has a gap — a role the market has created that the taxonomy has not caught up with. Today that is noticed anecdotally, years late.

## Target Customer
Global head of surveys or Chief Data Officer at a compensation data business. Two forces make it timely: pay transparency has multiplied the number of cuts customers demand, and matching labour is the constraint on producing them.

## Impact If Built
Survey production cost is dominated by matching, and matching accuracy is the accuracy of the entire product. Doing it semantically lets the same team cover more jobs, more geographies, and faster cycles — and it makes the quality of the match measurable for the first time in an industry that has never known its own error rate.
