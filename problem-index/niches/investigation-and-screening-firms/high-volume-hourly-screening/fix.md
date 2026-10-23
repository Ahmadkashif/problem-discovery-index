# The Disclosure Form That Invites a Class Action

**Niche:** [[niches/investigation-and-screening-firms/high-volume-hourly-screening/profile|High-Volume Hourly & Gig Screening]]
**Industry:** [[industries/investigation-and-screening-firms|Investigation & Background Screening Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The FCRA requires the background check disclosure to stand alone, and volume employers keep adding state notices, waivers and marketing text to it until a plaintiffs' firm notices.
**Tags:** #large-language-models #transformers #compliance #quick-win #automation #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to clear an hourly or gig applicant before that applicant accepts another offer, and whoever returns the largest share of complete, accurate reports within one business day takes the account.

## The Problem
FCRA §604(b)(2) requires a clear and conspicuous disclosure, in a document consisting solely of the disclosure, before an employer obtains a report. Volume hiring flows combine the disclosure with authorisation language, state-specific notices, liability releases and onboarding text across mobile screens. Extraneous content has driven a long line of statutory-damages class actions, and with hundreds of thousands of applicants a year the exposure multiplies.

## Why It's Still Broken
The disclosure is edited by the applicant tracking team, the screener's form builder and outside counsel at different times, and nobody owns the rendered version the applicant sees on a phone. State requirements (California, New York, Minnesota and others) add content that must go somewhere.

## What a Fix Looks Like
A lint check on the live, rendered flow: capture what the applicant actually sees, classify each block as federal disclosure, authorisation, state notice or extraneous, flag anything that breaks the stand-alone rule or omits a required state notice for the job's location, and log the approved version with a date.

## Who Feels the Pain
Employment counsel at volume employers; screening firms whose form builders are blamed; applicants who never read the wall of text.

## Impact If Fixed
A cheap, repeatable check removes one of the most litigated technical FCRA violations from flows that run hundreds of thousands of times a year.
