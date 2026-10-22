# The Post-Closer Chasing Trailing Documents

**Industry:** [[mortgage-lenders|Mortgage Lenders]]
**Type:** Worker Life Changing
**One-liner:** Long after a loan is sold, a post-closer is still emailing title agents and county recorders for the recorded mortgage, the final title policy and the MI certificate, across hundreds of loans at once, with investor deadlines and fees attached to every one.
**Tags:** #large-language-models #transformers #bert #feature-engineering #worker-facing #automation #workflow-orchestration

## The Problem
Selling a loan does not finish it. The investor buys on the closing package, but several documents only exist weeks or months later: the recorded mortgage or deed of trust from the county, the final title policy from the title agent, the mortgage insurance certificate, the recorded assignment where required, and corrected documents if anything was wrong. Investors require each by a deadline, commonly in the 90–120 day range (estimate), and charge fees or demand repurchase when they are late. A post-closer at a lender closing 1,000 loans a month carries several thousand open trailing documents at any time (estimate).

The work is a chase. The post-closer checks recorder websites county by county, emails title agents who have their own backlogs, matches each arriving PDF to the right loan, checks it against the closing package (names, legal description, recording stamp, policy amount), uploads it to the investor's portal and marks it received. Rejected documents start the cycle again. Counties with slow recording and title agents who close a deal and move on generate most of the backlog.

## Why It Matters to the Worker
The task never ends and is never visible until it fails. Each document is trivial; the volume is not. A post-closer works a list that grows by hundreds every month and shrinks only by persistence, and the only time anyone senior looks at it is when an investor sends an aging report with fees, or a repurchase demand over a final policy that was never obtained. The worker is judged on the backlog without control over the agents and counties who cause it.

It is also the first job cut in a downturn and the last hired back in a boom, so the backlog from the busy months lands on whoever is left. The work is checking the same fields on the same documents for years, and the knowledge of which title agent responds to which kind of email is held only in the post-closer's head.

## What a Solution Looks Like
An agent that knows every open trailing document by loan, investor and deadline; checks county recorder sites and title agent portals automatically; reads each arriving document, matches it to the loan, and checks names, legal description, amounts and recording information against the closing package; uploads it to the investor; and escalates only mismatches and documents about to breach a deadline. Follow-ups to title agents are drafted and sent on a schedule that reflects each agent's real response pattern. The post-closer works the exceptions and the relationships, not the inbox.

## Impact If Solved
If document matching, checking and upload take ten minutes per document by hand (estimate), automating them at a lender handling ~3,000 trailing documents a month returns about 500 hours a month (derived). Aging fees and repurchase exposure on missing final policies fall, and the post-closer's job becomes resolving the handful of genuinely broken documents rather than checking thousands of good ones.
