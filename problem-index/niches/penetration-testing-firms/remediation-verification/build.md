# Build: The Finding Followed Home

**Niche:** Remediation Verification
**Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A follow-up loop that joins each finding to what happened to it — fixed, ignored, regressed, recurred — and turns a firm's archive of engagements into evidence that its work changes outcomes.
**Tags:** #survival-analysis #evaluation-metrics #confidence-intervals #gradient-boosting #hypothesis-testing #causal-inference #data-integration #revenue-impact
**Contested on:** Whether a firm can demonstrate that its findings get fixed, that the fixes hold, and that the same weakness class stops recurring.

## The Problem

A testing firm's entire value proposition is that its findings matter. It has no evidence for this.

The engagement ends at the report. Whether the client fixed anything, whether the fix worked, whether the same weakness reappeared in the next release — all of it happens on the other side of a boundary that closes at handover. The firm learns nothing, and neither does the client in any structured way.

The consequences run in every direction. A firm cannot tell which of its finding types get remediated and which are filed and ignored year after year, so it keeps writing the ignored ones the same way. It cannot compare remediation advice — whether the fix it recommends for a given weakness holds, or regresses two releases later — so its guidance is habit rather than evidence. It cannot show a prospect that its clients end up more secure, so it competes on day rate. And the client, who does the same test annually, receives the same findings repeatedly without anyone naming that as the actual problem.

The data exists, and unusually it is not all behind the wall. The client's ticketing system, repository history and release record hold the answer, and most clients would grant access to it if anyone asked — because the analysis is useful to them too. Nobody asks, because follow-up is unbilled and nobody's job.

## Why Nobody Has Built This

**The engagement model ends at delivery.** Fees attach to the test. A ninety-day and twelve-month check-in is unbilled work against a relationship that has gone quiet, and in a utilisation-driven business unbilled work does not happen.

**Asking is uncomfortable.** "Did you fix what we found?" implies the client may not have, and invites an answer the firm cannot act on and the client would rather not give. The social friction is enough to prevent it on its own.

**The answer might be bad for the firm.** A firm that measures remediation may learn that a large share of its findings are never acted on, which raises an awkward question about what the engagement achieved. That is the most valuable finding available and the least welcome.

**Attribution is genuinely messy.** Clients fix things for many reasons, partially, with modified scope, while the codebase changes underneath. Linking a finding to the change that resolved it requires joining across ticketing, repositories and releases with inconsistent references.

**Recurrence requires a class model, not a finding match.** The same weakness in a new endpoint is a recurrence; matching on the original finding's location misses it entirely. Detecting class-level recurrence needs a taxonomy applied consistently across years of reports written by different people.

**No standing corpus.** Even a firm that follows up has nowhere to put the answer, so it becomes an account manager's recollection rather than an asset.

## What to Build

**Put the follow-up in the engagement letter.** Scheduled checks at ninety days and twelve months, written in at signing as part of the deliverable at no extra fee. This removes every obstacle at once — not a favour, not an awkward reopening, not discretionary unbilled time — and clients agree readily at the moment they are most positively disposed.

**Make the check-in useful to the client.** Frame it as a remediation review rather than a survey: what was fixed, what was not and why, what is now blocking. Clients accept this eagerly because it helps them, and it reliably surfaces follow-on work, which is the commercial argument that gets it funded internally.

**Join findings to the client's own systems where permitted.** Ticket status, the commit or release that addressed the finding, and a re-probe of the specific weakness. Read-only, scoped, and offered as a benefit — many clients will grant it because the resulting remediation analytics are better than what their own vulnerability management gives them.

**Classify every finding into a durable taxonomy at authoring time.** CWE or an internal equivalent, applied consistently. Without this, recurrence detection is impossible and the corpus is a pile of prose. Doing it at authoring costs a tester seconds and is the enabling step for everything downstream.

**Detect regression and class recurrence separately.** Regression is the same weakness returning at the same place — a fix that did not hold. Recurrence is the same class appearing somewhere new — a process that has not learned. They have different causes and different remedies, and conflating them is why annual reports read identically year after year.

**Score the remediation advice.** Where the firm recommended approach A and the client applied approach B, compare durability. Across thousands of engagements this produces evidence about which fixes hold, which no firm in this industry currently possesses and every one of them could.

**Report the outcome measures to prospects.** Remediation rate by finding type, regression rate, class recurrence trend. A firm that can state these has an argument no competitor can answer, and the asymmetry is durable because it takes years to build.

## Target Customer

Testing firm leadership, sold on differentiation rather than efficiency — the argument is that the market prices on day rate precisely because nobody can demonstrate outcome, and this is the only way out of that.

Client security leadership are a genuine second buyer, because class recurrence is the metric that tells them whether their engineering organisation is learning, and almost none of them have it.

Cyber insurers are the most interesting third party: they would price a client with a falling recurrence trend differently from one with a flat one, and today they cannot see either.

## Impact If Built

The firm can finally answer whether its work matters. That claim is the foundation of the entire industry and is currently supported by nothing but the plausibility of the activity.

Remediation advice becomes evidence-based. Which fixes hold is an empirical question that every firm has the data to answer and none has asked.

And class recurrence gives clients the diagnostic they actually need. Fixing the same category of weakness every year is an engineering process problem, not a testing problem, and naming it is worth more to the client than another list of instances.
