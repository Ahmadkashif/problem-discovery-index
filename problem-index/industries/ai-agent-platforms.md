# AI Agent Platforms

## Profile
**Category:** Data & AI Economy
**Market Size:** ~$2.5B US agent platforms and agentic application vendors, growing very fast from a small base
**Tech Maturity:** Impressive demos, unpredictable production — LangGraph, CrewAI, AutoGen and the orchestration frameworks provide the plumbing; Sierra, Decagon, Cognition, Lindy and the vertical agent companies sell outcomes. Nobody can tell a customer, before deployment, what fraction of tasks their agent will complete correctly.
**Workforce:** Forward-deployed engineers, agent reliability and evaluation engineers, integration engineers, solutions architects, support and escalation staff, prompt and workflow designers

## Key Pain Themes
Reliability is the category's binding constraint and nobody has a way to predict or guarantee it. An agent that succeeds nine times out of ten sounds impressive and is unusable for a task where a failure means a wrong refund, a deleted record or a customer told something untrue. The failures are not random either — they cluster in ways that only emerge in production, on inputs nobody anticipated, and each fix is a patch on a specific case rather than a systematic improvement. Below that sit two burdens the category carries permanently: tool and connector coverage, where every customer's stack requires integrations that are individually shallow and collectively endless; and action authorisation, where deciding what an agent may do without a human is a policy question that arrives as a configuration screen. The forward-deployed engineers who make deployments work spend their lives at customer sites tuning, and support staff handle the consequences when an agent does something wrong on a customer's behalf.

## Current Tech Landscape
Orchestration frameworks have converged on graph-based control flow with explicit state, which is a meaningful improvement on early autonomous loops. Tool calling is now a first-class model capability and the reliability of tool selection has improved substantially. The Model Context Protocol has emerged as a connector standard with real adoption. Evaluation for agents remains immature — trajectory-level assessment is much harder than single-turn output grading, and most teams rely on a handful of end-to-end test cases plus production monitoring. Vertical agent companies have found traction in customer support and coding, where the task is bounded and the failure is recoverable. Human-in-the-loop approval is the standard safety mechanism and its placement is chosen by intuition.

## Problems
- [[problems/ai-agent-platforms/high-impact|🔴 High Impact: Predicting Whether a Task Will Succeed]]
- [[problems/ai-agent-platforms/low-impact-1|🟡 Low Impact: Tool and Connector Coverage]]
- [[problems/ai-agent-platforms/low-impact-2|🟡 Low Impact: Action Authorisation Scoping]]
- [[problems/ai-agent-platforms/worker-life-1|🟢 Worker Life: Forward-Deployed Engineer On Site]]
- [[problems/ai-agent-platforms/worker-life-2|🟢 Worker Life: Support Staff After a Bad Action]]
- [[problems/ai-agent-platforms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/ai-agent-platforms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
The platforms accumulate something the field badly needs: millions of complete task trajectories with the tools called, the state at each step, the outcome and — in the vertical products — whether the customer was satisfied. That corpus supports the questions the category currently answers with intuition, including where human approval actually needs to sit, which failures are recoverable, and what predicts a task going wrong before it does. It is currently used to debug individual incidents.
