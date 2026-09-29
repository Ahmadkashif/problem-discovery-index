# Build: What the Marginal Dollar Buys

**Niche:** Programme Effectiveness Measurement
**Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A measurement layer that compares each bounty finding against what the organisation's own tooling and testing had already found, and estimates what additional spend would buy.
**Tags:** #causal-inference #gradient-boosting #evaluation-metrics #confidence-intervals #survival-analysis #bayesian-inference #data-integration #revenue-impact
**Contested on:** Whether a programme can show that its spend bought security, or only that it bought submissions.

## The Problem

A programme spends several hundred thousand dollars a year and reports that it received four thousand submissions, of which three hundred were valid, of which twelve were high severity, at an average payout and a median triage time.

The security leader presenting that to a budget committee is describing a process, not an outcome. The obvious question — would we have found these anyway — has no answer, and the less obvious but more important one — what would another hundred thousand buy — has no answer either.

The join that would answer the first question is straightforward and nobody performs it. The organisation runs scanners, static analysis, dependency checks and often contracted testing. For any bounty finding, the question of whether the same issue already existed in an internal finding queue, or was reported by a scanner and deprioritised, or was caught in a pull request review, is a database lookup. Do it across a year of findings and the programme's genuine novelty rate falls out.

The second question is harder and is the one that determines budget. Bounty returns diminish — the same researchers work the same surface, the easy findings go first, and at some point the marginal dollar buys a duplicate. Nobody has ever estimated where that point is for any programme.

## Why Nobody Has Built This

**The answer might argue against the programme.** A novelty rate showing that a large share of bounty findings were already in an internal queue is an uncomfortable number for the programme owner who champions the spend, and for the platform whose revenue it is.

**The join requires internal data the platform does not have.** Scanner output, internal finding queues and code review history live inside the customer. The platform sees only its own submissions, which means the measurement has to be built by the customer or by a third party sitting across both.

**Nobody owns the comparison.** The platform reports its own activity. The vulnerability management vendor reports the internal queue. Neither joins to the other, and the programme owner has no tooling to do it by hand at any useful scale.

**Deduplication across sources is genuinely hard.** A scanner finding and a researcher's narrative describing the same weakness look nothing alike. Matching them requires normalisation into a common representation, which is real work.

**Marginal return needs variation to estimate.** Estimating the shape of the curve requires observing programmes at different spend levels, or the same programme changing spend — which means the platform, holding many programmes, is the only party who could do it.

**Incident reduction is unmeasurable at the individual programme level.** Incidents are rare, multi-causal and confounded by everything else the security team does. Any honest measurement has to acknowledge that the top-line claim is not directly testable and work with intermediate outcomes instead.

## What to Build

**Start with the novelty join.** Normalise bounty findings and internal findings — scanner output, static analysis, contracted test findings, internal reports — into a common finding representation, and match. The output is a novelty rate: the share of bounty spend that bought a finding nothing else had. This is computable today by any programme with the will to do it, and it is the number that reframes the entire budget conversation.

**Decompose the non-novel share.** A finding that duplicates an internal one is not necessarily wasted spend — it may have been sitting in a backlog, deprioritised, unactioned for a year. Distinguishing "we already knew and had fixed it" from "we already knew and had ignored it" matters enormously, and the second is a finding about the organisation rather than about the programme.

**Estimate the marginal return curve.** Across the platform's programmes, model valid novel findings per dollar as a function of spend, programme age, scope size and researcher participation. Report to each programme where it sits on the curve and what an increment would be expected to buy, with honest uncertainty. Only the platform can do this and it would be the most valuable thing it could offer a budget holder.

**Compare channels on the same estate.** Where an organisation runs both bounties and contracted testing, compare cost per novel finding and the finding classes each channel produces. They are complementary rather than competing and nobody has ever evidenced how.

**Track time-to-discovery as the intermediate outcome.** How long a weakness existed in production before anyone reported it, and whether that interval is shortening. This is measurable, it moves, and it is a far better proxy for programme effect than incident counts.

**Report what the programme found that nothing else could.** The finding classes that only ever arrive through bounties — chained logic abuse, business logic flaws, creative attack paths — quantified. This is the honest case for the channel and no programme currently makes it with evidence.

## Target Customer

Programme owners and security leadership defending a budget, who currently present activity and know it is activity.

The platforms, for the marginal return curve specifically, which requires their cross-programme corpus and would make them genuinely advisory rather than transactional.

Cyber insurers and boards as the eventual demand side, both of whom currently treat the existence of a programme as a binary signal.

## Impact If Built

The budget conversation changes from volume to value. A programme that can state its novelty rate and its position on the marginal return curve is arguing from evidence, which no programme currently does.

The non-novel decomposition would surface a problem larger than the bounty programme: findings already known and unactioned, which is an organisational failure that bounty spend is quietly compensating for.

And quantifying what only bounties find is the honest defence of the channel — it is almost certainly real, it is almost certainly a smaller share than the headline numbers suggest, and nobody has ever measured it.
