# Apologising for a Decision You Cannot See

**Niche:** [[niches/neobanks/the-support-agent/profile|The Support Agent]]
**Industry:** [[industries/neobanks|Neobanks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The person a frozen member reaches can see that the account is restricted and not why, and spends the call apologising for a decision they are not permitted to explain or reverse.
**Tags:** #worker-facing #compliance #workflow-orchestration #large-language-models #evaluation-metrics #automation #confidence-intervals #quick-win
**Contested on:** Every serious competitor in this niche is fighting to let the person a frozen member reaches explain what happened and do something about it — and whoever does that turns the category's worst interaction into a resolvable one.

## The Problem
A member's rent is due and their account is frozen. They reach an agent. The agent's console shows a restriction flag and a code they cannot interpret. Policy prevents disclosing risk logic. The escalation queue to the risk team returns an answer in days. So the agent says they understand the frustration, that the account is under review, that they cannot say why or when, and that they are sorry. The member, who has done nothing wrong in most cases, becomes distressed and then angry. The agent has this conversation repeatedly, all day, and can do nothing about any of it.

## Why Nobody Has Built This
The non-disclosure policy was inherited from fraud practice, where telling a subject what triggered a detection helps them evade it, and applied wholesale to a population that is mostly not adversarial — the principle is sound in its original context and indefensible when applied to everyone. Risk systems were built for risk teams and the support console was built separately. Nobody owns the interface between them. And the agent's distress is absorbed as a characteristic of the job.

## What to Build
Give the agent something to say and something to do. Separate what can be disclosed from what cannot, deliberately, rather than defaulting everything to secret — most restrictions rest on ordinary facts whose disclosure enables nothing, and this classification is the single change that transforms the interaction. Give the agent the case detail even where the member receives a summary, since the agent's total blindness is what makes the conversation degrading for both. State an expected duration with a real distribution from the institution's own history, because not knowing when is worse than the restriction itself. Tell the member what would resolve it, since a large share clear on one document and there is frequently no route to say so. Let the agent collect that evidence and attach it to the case immediately, which turns the call into progress rather than a message. Give the agent a real escalation path with a commitment, so that the option exists rather than appearing to. Route the urgent hardship cases, since a member who cannot pay rent today is a different situation from one who noticed a restriction and the system treats them identically. Prepare the agent with the likely questions and honest answers, which is the difference between a script and support. Record what the agent was told and what they said, which protects everyone and feeds the outcome record. And measure this interaction specifically — resolution rate, repeat contacts, agent attrition on this queue — because it is the worst experience the category produces and nobody manages it as such.

## Target Customer
Member support leadership at digital banks, the agents on the restricted-account queue, and the risk organisations whose decisions arrive at that queue unexplained.

## Impact If Built
A non-disclosure principle sound in its original fraud context is applied wholesale to a mostly non-adversarial population. Classifying what can be disclosed, and letting the agent collect the resolving document on the call, converts an apology into progress.
