# Action Authorisation Policy

**Parent Industry:** [[industries/ai-agent-platforms|AI Agent Platforms]]
**Category:** Low Digitized
**Contested on:** Every serious competitor in this niche is fighting to place the human approval gate where the evidence says it belongs rather than where a nervous product manager guessed — and whoever does that takes the account, because gate placement determines whether a deployment saves anything.

## Profile
**Market Size:** ~$320M US
**Share of Parent Industry:** ~13% of category revenue
**Digital Adoption:** Very Low — gate placement is a guess
**Target Buyer:** Risk owners and the product leads who must choose
**Automation Potential:** High — the optimal placement is learnable from trajectories

## What Makes This a Distinct Niche
Every platform offers human-in-the-loop approval and permission scopes, and the question of where to put the gate is answered by intuition. Place it everywhere and the agent reviews every action, which saves nothing and trains reviewers to approve reflexively. Place it nowhere and one bad action destroys the deployment's credibility. The right placement depends on how often the agent is wrong on that action type, how costly and how reversible a wrong one is, and how reliably a human reviewer catches it — four quantities that are all measurable from data the platforms hold and none of which is used. This is the decision that determines whether an agent deployment is worth anything, and it is made by a product manager with a configuration screen.

## Current Tools & Gaps
Approval steps, permission scopes, tool allowlists, and spending or action limits. The gaps: no evidence-based placement recommendation; no measure of whether reviewers actually catch the errors they are there to catch; no accounting for reversibility, which should dominate the decision; no adaptation as the agent improves; and no measure of what each gate costs in throughput.

## Problems
- [[niches/ai-agent-platforms/action-authorisation-policy/build|🔨 Build: The Gate Placed by a Nervous Guess]]
- [[niches/ai-agent-platforms/action-authorisation-policy/buy|🛒 Buy: Authorisation Controls and Risk-Based Approval]]
- [[niches/ai-agent-platforms/action-authorisation-policy/fix|🔧 Fix: Reviewers Who Approve Everything]]
