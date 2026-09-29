# Resolution Rate Without a Quality Dimension

**Niche:** [[niches/ai-agent-platforms/vertical-outcome-agents/profile|Vertical Outcome Agents]]
**Industry:** [[industries/ai-agent-platforms|AI Agent Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Vertical agents report the share of tasks handled without a human, which counts a customer who gave up identically to a customer whose problem was solved.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #causal-inference #descriptive-statistics #revenue-impact #survival-analysis #gradient-boosting
**Contested on:** Every serious competitor in this sub-niche is fighting to resolve a higher share of one bounded domain's tasks without a human than an outsourcer would at the same cost — and whoever does that takes the account, because the buyer is comparing against a labour contract, not against a framework.

## The Problem
An agent reports a seventy percent resolution rate. Inside that number are tickets genuinely solved, tickets where the customer abandoned the conversation and did not come back, tickets where the customer got an answer that was wrong and will return next week as a new ticket, and tickets where the customer gave up and complained on a public channel instead. All four count as resolved. The buyer's actual outcome — whether the customer's problem went away — is not measured by anything the vendor reports, and the metric that determines the renewal is one the vendor controls the definition of.

## Why Nobody Has Built This
Deflection is easy to count and quality is not, and the category inherited deflection as a metric from the chatbot era where the same problem existed. Measuring genuine resolution requires following the customer beyond the interaction, which needs data from the buyer's systems and a definition both sides agree on. A quality-adjusted number is lower, and no vendor will publish one unilaterally. And buyers accept the metric offered because they have no alternative to propose.

## What to Build
Measure whether the problem went away. Define resolution as the absence of a recurrence within a window plus an absence of escalation, which is computable from the buyer's own systems, is far closer to the truth than deflection, and is the definitional change the whole sub-niche needs. Track repeat contact explicitly and subtract it, since a wrong answer that generates a new ticket is worse than an escalation. Detect abandonment as its own outcome rather than as a success. Measure against the human baseline on comparable tickets, which is the comparison the buyer is making implicitly and which frequently favours the agent in ways nobody has demonstrated — and sometimes does not, which the buyer deserves to know. Report cost per genuinely resolved task rather than per interaction, since that is what competes with an outsourcing rate. Report quality on the resolved set — accuracy, tone, policy compliance — from sampled human review, since a high resolution rate with poor quality is a liability rather than a saving. Segment by task type, because the aggregate conceals which categories the agent should not be handling. And agree the definition with the buyer at contract time, since the metric currently being optimised is one the vendor defines and grades.

## Target Customer
Business function owners buying outcomes, the finance functions comparing against outsourcing, and the vendors whose genuinely good agents are indistinguishable from ones that deflect well.

## Impact If Built
Deflection counts a customer who gave up as a success. Defining resolution as the absence of recurrence is computable from the buyer's own systems and is the definitional change that makes the headline number mean what everyone assumes it means.
