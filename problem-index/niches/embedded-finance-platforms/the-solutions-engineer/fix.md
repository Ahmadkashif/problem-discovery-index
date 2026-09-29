# The Same Question, The Fortieth Time

**Niche:** [[niches/embedded-finance-platforms/the-solutions-engineer/profile|The Solutions Engineer]]
**Industry:** [[industries/embedded-finance-platforms|Embedded Finance Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Every implementation channel asks the same forty questions and each is answered from scratch by someone typing into Slack.
**Tags:** #worker-facing #large-language-models #automation #quick-win #workflow-orchestration #evaluation-metrics #tacit-knowledge-ml #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to get the regulated-product knowledge a solutions engineer carries in their head into a form a first-time developer team can use without them — and whoever extracts it turns the category's scarcest people into leverage instead of a bottleneck.

## The Problem
The solutions engineer has twelve active implementation channels. In each of them, a developer asks how holds are released, what happens to a pending authorisation when a card is frozen, whether fees can be assessed before settlement, how to handle a partial capture, what the bank requires in the disclosure flow. The answers are the same every time and are typed out again every time, in a channel that will be archived when the programme launches, taking the answer with it.

## Why It's Still Broken
Answering in the channel is faster than writing documentation, so the marginal decision is always to answer — and the aggregate cost is never faced. The answers are scattered across dozens of private channels. Nobody reads those channels as a corpus. And solutions engineering headcount is the shock absorber, so the pressure lands on people rather than on the process.

## What a Fix Looks Like
Mine the channels and answer once. Extract the recurring questions and their answers from the implementation channels, which is the fix and is a mechanical reading of material already written. Rank by frequency, since a handful of questions account for most of the volume and addressing them clears most of the load. Put the answers where the question arises rather than in a documentation site, because a developer asks in the channel precisely when the docs did not reach them. Suggest an answer in-channel with the engineer reviewing it, so the quality bar holds and the typing stops. Capture new answers into the corpus automatically, which keeps it alive without a maintenance project. Mark the bank-specific answers as such, since a general answer applied to the wrong sponsor is worse than no answer. Track question volume per implementation, which reveals both the hardest parts of the product and the teams in trouble. Feed the frequent questions back into the API design, because a question asked forty times is usually a design report. Preserve the channels rather than archiving them, since the corpus is being deleted at exactly the moment it is complete. And measure engineer hours per implementation, which is the number that shows the leverage arriving.

## Who Feels the Pain
Solutions engineers typing the same answers daily; developers waiting for a reply that exists in another channel; and platforms whose implementation capacity is capped by a handful of people.

## Impact If Fixed
Answering is always faster than documenting, so the aggregate cost is never faced. The implementation channels already contain the answers and they are being archived at the moment they are most complete.
