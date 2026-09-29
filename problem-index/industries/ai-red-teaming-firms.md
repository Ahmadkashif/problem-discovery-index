# AI Red Teaming Firms

## Profile
**Category:** Data & AI Economy
**Market Size:** ~$600M US AI security testing and model assurance services, expanding rapidly with regulatory pressure
**Tech Maturity:** Genuine expertise, no coverage metric — Lakera, Robust Intelligence, Gray Swan, HackerOne's AI programmes and the specialist consultancies employ skilled people who find real vulnerabilities. None of them can tell a client how much of the risk surface was examined, which is the question that determines whether a clean report means anything.
**Workforce:** Red team researchers, harm taxonomy specialists, domain experts for sector-specific testing, report writers, automation engineers, client engagement leads

## Key Pain Themes
Coverage is unmeasurable and everything follows from that. A penetration test of a network can be scoped against an asset inventory; a model has an unbounded input space and no equivalent. So a report saying no critical findings might mean the system is robust or might mean the team tested the wrong things, and neither the firm nor the client can distinguish these. Below that sit two operational problems: building harm taxonomies for specific domains, where generic categories do not capture what actually goes wrong in a clinical or financial deployment; and regression testing after model updates, where a client changes model version and the entire assessment becomes stale with no cheap way to revalidate. The people doing the work face something the software security industry took decades to acknowledge — sustained exposure to harmful content as a job requirement — and the report writers translating findings for engineering teams spend their time on documentation rather than research.

## Current Tech Landscape
Automated probing tools and open jailbreak datasets provide breadth cheaply and go stale as models are updated against known attacks. Guardrail products from Lakera, Protect AI and others sit in front of deployed models. The research literature on adversarial prompting is large, public and moves quickly, which means both defenders and the firms are working from substantially shared knowledge. Regulatory pressure is the main commercial driver: the EU AI Act, NIST's AI Risk Management Framework and sector regulators are converging on requirements for documented testing, which creates demand for assurance regardless of whether coverage can be measured. Bug bounty models have been extended to AI systems with mixed results, since severity assessment is far more contested than in traditional security.

## Problems
- [[problems/ai-red-teaming-firms/high-impact|🔴 High Impact: Coverage Is Unmeasurable]]
- [[problems/ai-red-teaming-firms/low-impact-1|🟡 Low Impact: Domain-Specific Harm Taxonomies]]
- [[problems/ai-red-teaming-firms/low-impact-2|🟡 Low Impact: Regression Testing After Model Updates]]
- [[problems/ai-red-teaming-firms/worker-life-1|🟢 Worker Life: Researcher Exposure to Harmful Content]]
- [[problems/ai-red-teaming-firms/worker-life-2|🟢 Worker Life: Report Writer Translating Findings]]
- [[problems/ai-red-teaming-firms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/ai-red-teaming-firms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
These firms accumulate the only cross-model, cross-deployment record of what actually fails: thousands of assessments with the probe, the model, the configuration, the defence in place and the outcome. That corpus answers questions the field currently cannot — which defensive measures actually work across deployments, which failure classes generalise, and how much of a model's robustness is specific to it. The commercial obstacle is that publishing comparative defensive efficacy would make some clients' vendors look bad and some findings would be uncomfortable, and the firms are paid by the parties who would be embarrassed.
