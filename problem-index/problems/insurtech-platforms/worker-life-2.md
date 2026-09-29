# Underwriting Assistant Transcription

**Industry:** [[insurtech-platforms|Insurtech Platforms]]
**Type:** Worker Life Changing
**One-liner:** Underwriting assistants stop keying loss runs and vehicle schedules out of PDFs and start doing the analytical preparation that would actually help an underwriter decide.
**Tags:** #large-language-models #bert #transformers #word-embeddings #evaluation-metrics #transfer-learning #automation #worker-facing

## The Problem
The underwriting assistant is the role that turns an email into a submission. Open the attachments, read the ACORD application, key the named insured and the exposures, transcribe the vehicle schedule from a spreadsheet, work through the loss run — which arrives as a PDF from the expiring carrier in that carrier's own format — and enter each claim year with paid and reserved amounts. Then order the reports, check the clearance, and put it in front of an underwriter.

It is hours per submission on the larger accounts, and the volume is set by how many submissions the carrier receives rather than by how many it wants. A large share of what gets keyed is declined shortly afterwards.

Loss runs are the worst of it. They are the most important document in the submission, they are produced in hundreds of incompatible formats, they frequently span multiple carriers across the experience period, and they must be read carefully because an underwriting decision rests on them. Keying them is slow, tedious and consequential.

## Why It Matters to the Worker
The assistant role is where underwriters are developed. People enter it to learn the business and progress into underwriting, and what they are supposed to be learning is how risk is assessed. Spending the majority of the day on transcription teaches data entry.

It is also a role under quiet pressure from both directions: volume rises with submission flow the carrier cannot control, and headcount is a cost line under constant scrutiny. Assistants absorb the gap through hours.

The frustration is knowing which parts mattered. An assistant who has keyed two thousand loss runs has developed genuine intuition about what a bad one looks like — a pattern of small frequent claims, a large reserve that has been developing, a gap in the experience period — and nothing in the role uses it. That intuition is exactly what the carrier needs and it never surfaces.

## What a Solution Looks Like
Extraction rather than entry. The ACORD form, the schedules and the loss runs should arrive as populated fields with confidence scores, and the assistant should review and correct rather than type. Loss run parsing across the hundreds of formats in circulation is the highest-value single piece and is a well-shaped problem given the volume of examples every carrier holds.

Review should be prioritised by consequence. A misread claim amount matters more than a misread street address, and the interface should reflect that rather than presenting every field identically.

What the assistant does with the time is the point. Preparing a submission properly — normalising loss experience, identifying the development pattern, flagging the exposures that do not match the application narrative, comparing to similar risks the carrier has written — is analytical work that helps an underwriter and develops the assistant toward becoming one.

## Impact If Solved
Submission intake capacity determines how much business a carrier can consider, and it is currently spent largely on transcription for accounts that will be declined. Automating the keying raises throughput without hiring and turns the industry's main underwriting apprenticeship back into an apprenticeship.
