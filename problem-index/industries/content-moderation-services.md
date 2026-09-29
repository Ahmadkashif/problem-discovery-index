# Content Moderation Services

## Profile
**Category:** Trust, Safety & Security
**Market Size:** ~$12B globally in outsourced content moderation and trust and safety operations; Accenture, Teleperformance, Majorel, TaskUs, Concentrix and a tier of specialist providers supply most of the human review the internet runs on
**Tech Maturity:** Workforce operations at enormous scale with borrowed tooling. These vendors staff, train and manage tens of thousands of reviewers across dozens of languages, on client-supplied review interfaces they usually do not control, measured by quality audits designed by the client. The technology that would most reduce the harm this work does to the people performing it sits with the platform rather than with the employer who carries the liability.
**Workforce:** Content reviewers and moderators, team leads and quality auditors, policy trainers, workforce planners and schedulers, wellness and clinical staff where provided, account managers

## Key Pain Themes
The commercial model is volume and agreement. Contracts price per decision or per hour against a throughput expectation, and quality is measured by whether a reviewer's decision matches an auditor's on a sampled subset. That metric rewards literal policy application, because that is what an auditor applying a policy document will mark correct — and it teaches reviewers to stop exercising the contextual judgement that the hardest cases require.

The second theme is that the vendor carries the occupational liability and does not control the exposure. Litigation and reporting across several jurisdictions have documented the psychological cost of sustained exposure to the worst material online, and the settlements and claims have landed substantially on the outsourcing tier. Meanwhile the decisions that determine how much distressing material a reviewer actually sees — pre-classification, presentation fidelity, segment isolation, queue composition — are made in the platform's tooling.

The third is that the outcome never returns. A vendor makes hundreds of millions of decisions a year and learns which matched an auditor's sample. Whether the decisions made the platform safer, whether they were upheld on appeal, whether the enforcement was proportionate — none of that comes back, so a business built entirely on decision quality has no measure of decision quality beyond internal agreement.

## Current Tech Landscape
Review tooling is predominantly client-supplied, with each platform's own queueing, presentation and decision interface. Classifiers upstream determine what reaches humans and are operated by the platform. Vendor-side workforce management runs on standard contact-centre tooling adapted for review. Quality audit is a sampled manual process. Wellness provision is contractually specified with delivery that reporting has repeatedly found inconsistent. Specialist providers exist for the highest-severity categories including child safety, with more established clinical protocols.

## Problems
- [[problems/content-moderation-services/high-impact|🔴 High Impact: Priced on Volume, Measured on Agreement, Blind to Outcome]]
- [[problems/content-moderation-services/low-impact-1|🟡 Low Impact: Teaching a Two-Hundred-Page Policy]]
- [[problems/content-moderation-services/low-impact-2|🟡 Low Impact: Coverage in Languages Nobody Built For]]
- [[problems/content-moderation-services/worker-life-1|🟢 Worker Life: The Reviewer]]
- [[problems/content-moderation-services/worker-life-2|🟢 Worker Life: The Auditor Enforcing a Metric They Know Is Wrong]]
- [[problems/content-moderation-services/ml-opportunity|🧠 ML Opportunities]]
- [[problems/content-moderation-services/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
This industry is the one where the split between who holds the capability and who holds the liability is starkest. The platform runs the classifiers, designs the queue and sets the policy; the vendor employs the people, absorbs the psychological cost and faces the claims. Every intervention that would reduce occupational harm — deciding what genuinely needs human eyes, presenting it at reduced fidelity, isolating the segment at issue, capping cumulative severe exposure — is technically available and sits on the wrong side of a contract. The same split explains the quality problem: the vendor is measured on agreement with a sample because the client will not share the outcome data that would allow anything better. A vendor that built exposure reduction and outcome-linked quality measurement into its own operation would be competing on something other than price for the first time.
