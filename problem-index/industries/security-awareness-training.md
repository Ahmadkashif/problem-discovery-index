# Security Awareness Training

## Profile
**Category:** Trust, Safety & Security
**Market Size:** ~$3B US in security awareness training and phishing simulation, dominated by KnowBe4 with Proofpoint, Hoxhunt, Living Security, Ninjio and a long tail of content vendors
**Tech Maturity:** Effective delivery infrastructure attached to a metric the vendor controls. These platforms send simulated phishing at scale, track who clicks, assign training and report a click rate that improves over time. The difficulty of the simulations is set by the vendor and the customer, which means the headline metric is partly a statement about the test rather than about the workforce.
**Workforce:** Security awareness managers and programme owners, content and curriculum designers, platform engineers, customer success staff, the employees on the receiving end of the programme

## Key Pain Themes
The industry's metric is click rate on its own tests. A programme reports that clicks fell from a high starting point to a low one over a year, and that trend is consistent with a workforce that learned something and equally consistent with simulations that got easier, more recognisable, or more heavily pre-announced. Nobody outside the vendor and the customer sets the difficulty, and no published benchmark relates simulated click rate to actual compromise.

The second theme is that the programme has documented capacity to harm. Simulations imitating bonus announcements, redundancy notices or benefit changes have repeatedly generated public controversy and real distress; punitive use of results — naming, disciplinary action, public lists — is common enough that it shapes how employees regard the security function. The behaviour that actually helps an organisation is reporting a suspicious message, and a programme that punishes clicking teaches people to say nothing.

The third is that the valuable output lands somewhere else. Employee reports of real suspicious messages are a genuinely useful detection source, and they arrive as an unstructured queue at a security team already at capacity, where most are legitimate mail.

## Current Tech Landscape
Simulation platforms integrate with mail systems to deliver and track campaigns, with template libraries covering common lures. Training is delivered as short modules with completion tracking, and content quality varies widely. Reporting buttons integrated into mail clients feed either the platform or the security team. Email security gateways handle the automated defence layer and their effectiveness determines what reaches employees in the first place. Some vendors have moved toward personalised difficulty and continuous micro-training, which is a genuine improvement on annual modules.

## Problems
- [[problems/security-awareness-training/high-impact|🔴 High Impact: Measuring Click Rate on a Test You Set the Difficulty Of]]
- [[problems/security-awareness-training/low-impact-1|🟡 Low Impact: Training Content and Targeting]]
- [[problems/security-awareness-training/low-impact-2|🟡 Low Impact: The Reporting Pipeline Nobody Resourced]]
- [[problems/security-awareness-training/worker-life-1|🟢 Worker Life: The Awareness Manager Everyone Resents]]
- [[problems/security-awareness-training/worker-life-2|🟢 Worker Life: The Employee on the Remedial List]]
- [[problems/security-awareness-training/ml-opportunity|🧠 ML Opportunities]]
- [[problems/security-awareness-training/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
This category has the cleanest available path to an outcome measure and does not take it. Every customer runs an email security gateway that records real phishing attempts, an incident record of actual compromises, and a reporting stream from employees — so the relationship between simulated performance and real-world resistance is estimable inside any large customer, and across customers by a vendor. The reason it is not measured is that the current metric improves reliably and the real one might not. The second, more serious issue is that the intervention itself carries known harms, and a category that measured outcomes would be able to say which programme designs deliver resistance without the trust damage that punitive simulation reliably produces.
