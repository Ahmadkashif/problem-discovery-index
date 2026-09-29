# Content Analysts Know Which Lender Guidelines Lie

**Niche:** [[niches/mortgage-brokers/product-pricing-engines/profile|Product & Pricing Engines]]
**Industry:** [[industries/mortgage-brokers|Mortgage Brokers]]
**Type:** Fix (Pain Point)
**One-liner:** The people maintaining the rules know which lenders' published guidelines do not match what they actually do, and there is no field for it.
**Tags:** #tacit-knowledge-ml #anomaly-detection #text-classification #worker-facing #data-integration

## The Problem
A content analyst who has maintained a lender's rules for three years knows things the guidelines do not say. That this lender's published overlay is applied inconsistently and the account executive will waive it on request. That another lender's stated turn times are aspirational in the last week of a month. That a documentation requirement is enforced strictly by one operations centre and loosely by another. That a particular programme is technically live and effectively closed to new business.

That knowledge decides whether the engine's output is useful. A price from a lender who will not actually honour it wastes a broker's week.

The rules configuration holds what the guidelines say. There is nowhere to record what the analyst knows about how the lender behaves, so it lives in the analyst, gets shared informally with support and account teams, and disappears when they leave — in a role with ordinary turnover.

## Why It's Still Broken
The engine's positioning is that it reflects lender guidelines accurately. Recording that a lender's published guidelines are unreliable sits awkwardly with a business whose partners are those lenders, so the observation stays verbal.

The data model also has one representation per rule: what the guideline says. A second layer — how it is applied in practice, with confidence and evidence — is a schema change nobody has proposed.

And the feedback that would confirm it arrives somewhere else. Brokers who get a price a lender then declines contact support, and support closes the ticket without connecting it to the content.

## What a Fix Looks Like
Give practice knowledge a structured, internal home and test it against outcomes.

**Typed practice notes on lender rules.** Applied inconsistently, waivable, stated turn time unreliable, programme effectively closed — with evidence, a date, and a confidence level. Seconds to record.

**Join to the outcome data the engine already has.** Where a lender's searches convert to locks at a much lower rate than comparable pricing implies, or where locks renegotiate unusually often, that is evidence for or against a practice note. Within a quarter the company would know which analyst observations are reliable.

**Route support escalations back to content.** A broker reporting that a lender would not honour a price is the most direct possible evidence about the rules, and it currently terminates in a ticket queue.

**Surface at the point of maintenance.** An analyst picking up a lender should see the accumulated practice knowledge about it rather than starting from the guidelines and their own memory.

**Keep it internal and unattributed externally.** This is the engine understanding its own accuracy, not a public rating of lenders — which resolves the partner-relationship concern squarely rather than by silence.

## Who Feels the Pain
Content analysts, holding knowledge that decides product quality with nowhere to put it. Support teams, handling escalations that content could have prevented. Brokers, who lose a week on a price that was never real. And the borrower at the end of it.

## Impact If Fixed
The engine's value is that its answers are actionable, and the difference between a guideline and a lender's actual behaviour is precisely where that breaks. Capturing practice knowledge and validating it against the conversion data already in the system turns a known-but-unwritten problem into a measurable one, and it is the input the execution modelling in this niche depends on.
