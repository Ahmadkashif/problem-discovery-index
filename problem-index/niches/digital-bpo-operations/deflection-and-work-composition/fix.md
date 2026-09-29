# Fix: The Customer Repeats Everything to the Agent

**Niche:** [[niches/digital-bpo-operations/deflection-and-work-composition/profile|Contact Deflection & Work Composition]]
**Industry:** [[industries/digital-bpo-operations|Digital BPO Operations]]
**Type:** Fix (Pain Point)
**One-liner:** The customer spent six minutes with the bot, escalated, and the agent's first question is what the problem is.
**Tags:** #data-integration #workflow-orchestration #large-language-models #evaluation-metrics #descriptive-statistics #worker-facing #quick-win #automation
**Contested on:** Whether the bot's conversation will be handed to the agent in a form they can use in five seconds.

## The Problem

A customer tries self-service. They explain their problem, answer questions, try a suggested fix, and it does not work. They escalate.

The agent picks up and asks what the problem is. The customer, already frustrated by six minutes that produced nothing, explains it again — often less patiently the second time, which is where a meaningful share of difficult contacts originate.

The bot conversation exists. It is frequently passed to the agent as a link or a raw transcript that nobody opens under a handle time target, or as nothing at all. So the most common escalated-contact experience in the industry begins by discarding everything that was already established.

## Why It's Still Broken

The deflection platform and the contact centre platform are different systems, often from different vendors, integrated for routing rather than for context. Passing a transcript technically satisfies the integration requirement.

A raw transcript is also unusable in practice. Six minutes of bot dialogue is more reading than an agent can do while a customer waits, so even where it is passed, it is not read — which then reads as evidence that agents do not want it.

And nobody owns the seam. The client owns the bot, the BPO owns the agents, and the handoff between them is a technical integration that was signed off as working.

## What a Fix Looks Like

Pass a summary, not a transcript, and put it where the agent's eyes already are.

Generate a three-line summary at the moment of escalation: what the customer is trying to do, what has already been established or verified, and what was attempted and failed. This is a summarisation task over a short conversation, it takes under a second, and it is the entire fix.

Put it at the top of the agent's screen, unmissable, before the contact connects. Not behind a tab, not as a link. The agent should have read it before they say hello.

Carry the verified facts forward as data, not prose. Identity verified, account located, order number confirmed, troubleshooting step completed. These should populate the agent's workspace so nothing verified is re-verified, which is both the time saving and the thing that most annoys customers.

Open with acknowledgement. An agent who begins with "I can see you have been trying to reset your password and the code did not arrive" has changed the contact entirely, and it costs nothing.

Measure it. Repeat-explanation rate — detectable from the transcript as the customer restating what they already told the bot — by escalation path. This tells you which handoffs are broken and it is computable today.

And feed the failed escalations back to the deflection team. Every escalation is a bot failure with a reason, and the reasons cluster. That is the highest-quality improvement signal the deflection programme could receive, and it currently flows nowhere.

## Who Feels the Pain

Customers, explaining themselves twice after an experience that already wasted their time — which is the single most common complaint about automated support. Agents, starting from zero on a contact that arrives pre-frustrated and being measured on handle time for the rework. And the client, whose deflection programme is generating hostility it never sees, because the hostility lands on the vendor's agents.

## Impact If Fixed

The escalated contact starts where the bot conversation ended, which removes the repetition that causes most of the frustration. Verified facts stop being re-verified. And the escalation reasons flow back to the deflection team, which is the feedback that makes the bot better rather than merely busier.
