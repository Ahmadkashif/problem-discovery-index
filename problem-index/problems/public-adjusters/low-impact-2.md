# Client Intake and Case Pipeline Management

**Industry:** [[public-adjusters|Public Adjusters]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** CRM tools can track leads and clients, but they can't manage the public adjuster's unique pipeline — where every case is a contingency bet with different expected value, settlement timeline, and carrier negotiation complexity — or help the firm decide which claims to take and which to refer out.
**Tags:** #gradient-boosting #regression #tabular-ml #workflow-orchestration

## The Problem
Public adjusters operate on contingency — they invest inspection time, documentation effort, and negotiation hours before receiving any payment. Not all claims are worth taking: a $15,000 residential water damage claim might generate $1,500-$2,250 in fees after 3-4 months of work, while a $500,000 commercial fire claim generates $50,000-$75,000. But the commercial claim requires more expertise and takes longer. The intake decision — which claims to accept, which to refer to other adjusters, and how to prioritize the active caseload — is currently made by gut feel. Public adjusters often take too many small claims to fill their pipeline, then can't service their large claims properly, reducing recovery rates on the most valuable cases. During catastrophic events, the intake problem reverses: hundreds of potential clients call simultaneously, and the firm must triage which ones to prioritize with no system for estimating case value or complexity.

## What Already Exists
Generic CRMs (HubSpot, Salesforce) track client interactions. ClaimWizard provides basic public adjuster CRM. Project management tools (Monday.com, Asana) can track case stages. None model the financial characteristics of public adjusting cases — expected settlement value, estimated time investment, probability of successful recovery, or opportunity cost of accepting one case over another.

## The Customisation Gap
A public adjuster pipeline system needs to: (1) score incoming leads by estimated claim value (based on loss type, property type, policy limits if known, and preliminary damage description), (2) estimate time-to-settlement based on loss type, carrier reputation, and complexity indicators, (3) calculate expected ROI per case (estimated fee vs. estimated time investment), (4) manage caseload capacity — alerting when the firm is taking on more cases than it can service at quality, (5) prioritize active cases by settlement proximity, documentation completeness, and carrier response deadlines, and (6) during catastrophic events, provide mass intake processing with automatic lead scoring and prioritization.

## Impact If Solved
Increases firm revenue per adjuster by 20-30% through better case selection — focusing on high-value claims rather than filling the pipeline with low-value work. Reduces average case cycle time by 15-20% through proactive prioritization and deadline management. Enables catastrophic event response at 3-5x normal capacity by automating intake triage. Provides financial visibility — the firm owner knows the expected value and timeline of the entire pipeline, enabling better cash flow management.
