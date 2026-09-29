# Waiting Four Days for an Answer

**Niche:** [[niches/game-porting-studios/the-engineer-in-a-strangers-codebase/profile|The Engineer in a Stranger's Codebase]]
**Industry:** [[industries/game-porting-studios|Game Porting Studios]]
**Type:** Fix (Pain Point)
**One-liner:** The engineer asked the client why a system works this way, and will hear back some time next week.
**Tags:** #worker-facing #quick-win #workflow-orchestration #automation #evaluation-metrics #data-integration #descriptive-statistics #large-language-models
**Contested on:** Every serious competitor in this niche is fighting to make a large unfamiliar codebase comprehensible to an engineer with no access to its authors and no documentation of why anything is the way it is — and whoever does that takes the account.

## The Problem
Questions to the client go into an email thread or a shared channel and come back days later, if at all — the original team is busy shipping their own patches and the person who wrote the system may have left. Meanwhile the engineer either blocks, or guesses and moves on. Guessing is what usually happens, and the wrong guess surfaces weeks later as a defect nobody can explain.

## Why It's Still Broken
There is no channel designed for it — questions sent into a general email thread compete with everything else in the recipient's day and lose, and nobody on either side owns the response time. The client has no obligation in the contract. Questions are not tracked, so nobody knows how many are outstanding. And the cost of a guess appears much later and is attributed to the engineer.

## What a Fix Looks Like
Give the questions a channel, an owner and a clock. Track technical questions in a shared queue with an owner and a target response time, which is the fix and is a board rather than a product. Put a response expectation in the contract, since a client who has agreed to it responds and one who has not does not. Name a technical contact on the client side rather than sending questions to a team address. Batch questions rather than sending them individually, which suits how the client's engineers work. Record every answer in a project knowledge base, because the same question recurs across engineers. Mark where an engineer proceeded on an assumption, so those can be revisited rather than forgotten. Report the outstanding question count and age to both parties weekly, which is what makes the cost visible. Escalate a blocked question after a defined period rather than leaving the engineer stuck. Ask the highest-value questions first while the client's attention is available, since it decays through the project. And capture the answers at project close as part of the studio's own record.

## Who Feels the Pain
Engineers blocked or guessing; studios absorbing defects caused by a wrong assumption; producers whose schedule contains a dependency nobody scheduled; and clients who would have answered if asked properly.

## Impact If Fixed
Questions sent into a general email thread compete with everything else in the recipient's day and lose, and nobody owns the response time. A tracked queue with a contractual expectation is a board that removes the guessing.
