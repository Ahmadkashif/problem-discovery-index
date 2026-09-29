# Commercial Submission Ingestion and Triage

**Industry:** [[insurtech-platforms|Insurtech Platforms]]
**Type:** High Impact
**One-liner:** Turn the email attachments a carrier receives all day into structured submissions, and rank them by the probability they will be quoted and bound — so underwriters spend their time on the business they will actually write.
**Tags:** #large-language-models #bert #transformers #gradient-boosting #word-embeddings #feature-engineering #evaluation-metrics #transfer-learning #revenue-impact

## The Problem
A commercial insurance submission arrives as an email. Attached are some combination of an ACORD application, a loss run from the expiring carrier, a schedule of vehicles or locations in a spreadsheet nobody standardised, a supplemental questionnaire, financial statements, and a broker's covering note explaining what they are actually looking for.

Before an underwriter can assess it, all of it has to become structured data in the policy system. That work is done by underwriting assistants, and it is transcription: named insured, FEIN, addresses, class codes, payroll or sales by class, vehicle schedules, prior loss history by year with paid and reserved amounts, coverage requested, limits, deductibles.

The volume is the crushing part. A carrier receives many multiples of the submissions it will ever quote, and a large share are declined — wrong appetite, wrong geography, wrong size, an unacceptable loss history. The decline usually happens after the transcription, because you cannot assess appetite without reading the submission, and reading it at volume is what the assistants are for.

So a carrier spends its intake capacity keying data about business it will never write, while the submissions it wants sit in the same queue waiting their turn. Brokers experience this as slow quote turnaround, and quote turnaround is the single strongest driver of which carrier a broker sends the next submission to.

## Why It's Unsolved
The documents resist standardisation in a way that has defeated thirty years of effort. ACORD forms exist and are the interchange standard, and they arrive as scanned PDFs, as partially completed forms, as forms superseded by an email that contradicts them. Loss runs are produced by the expiring carrier in whatever format that carrier uses, and there are hundreds of formats. Schedules arrive as spreadsheets with columns invented by the broker's assistant.

The industry's structural answer — get everyone to submit in a standard format — has been attempted repeatedly and fails because the broker holds the power in the relationship. A carrier that makes submission harder receives fewer submissions, which is precisely the wrong outcome.

Triage has its own difficulty. Predicting whether a submission will bind requires knowing what the carrier's appetite actually is, which is not what the appetite guide says. Underwriters apply judgement that has never been written down, and the declines are recorded with a reason code chosen from a short list that rarely captures the real reason.

## What a Solution Looks Like
Extraction from the documents as they actually arrive, with confidence per field and a review queue for the uncertain — not a portal that asks brokers to change their behaviour. Loss run parsing is the highest-value single component, because it is the most laborious, the most error-prone, and the most determinative of the underwriting decision.

Triage sits on top: a predicted probability that this submission will be quoted and bound, from the extracted attributes plus the carrier's own history of what it has written and declined. Submissions likely to bind go to an underwriter immediately; submissions clearly outside appetite get a fast, honest decline, which brokers value more than a slow one.

The decline reason matters and should be captured properly. A carrier that knows why it declines is a carrier that can tell its brokers what to send, which is the cheapest distribution improvement available to it.

## Impact If Solved
Quote turnaround determines where brokers send business, and it is currently gated by transcription capacity spent largely on submissions that will be declined. Removing the keying and ranking the queue increases the volume of desirable business a carrier can actually consider, without hiring — and the ranking rests on the carrier's own bind history, which no vendor can replicate.
