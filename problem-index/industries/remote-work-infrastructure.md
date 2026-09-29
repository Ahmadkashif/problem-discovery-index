# Remote Work Infrastructure

## Profile
**Category:** Platform Labour & Digital Work
**Market Size:** ~$8B US in employer-of-record, global payroll, contractor management and workforce monitoring services; Deel, Remote, Oyster, Velocity Global, Papaya and G-P hold the employment layer, with a separate monitoring tier from Hubstaff, Time Doctor, ActivTrak and Teramind
**Tech Maturity:** Strong payments and onboarding infrastructure sitting on compliance determinations that are largely manual and entirely opaque. A platform asserts that a worker in a particular country can be engaged in a particular way, and the customer has no means of evaluating that assertion until an authority disagrees.
**Workforce:** Employees engaged through employers of record, international contractors, compliance and payroll specialists at the platforms, legal and tax advisors, and the people subject to workforce monitoring

## Key Pain Themes
The employer-of-record model works by a local entity employing the worker and invoicing the client. The client's exposure depends on determinations the platform makes: whether this engagement is employment or contracting in this jurisdiction, whether the arrangement creates a permanent establishment for tax purposes, whether the benefits and termination terms satisfy local law. Those determinations are made by people using internal knowledge bases, expressed as a green tick in a product, and are not auditable by the customer who carries the residual risk.

Misclassification is the sharpest instance. Whether a worker is genuinely a contractor is a legal test that differs by country and is applied to the facts of the engagement — what the person actually does, how they are controlled, whether they work exclusively. A platform can process a contractor payment correctly and cannot make the underlying relationship compliant, and the distinction is frequently blurred in how these services are sold.

The monitoring tier raises a different problem. Activity tracking — keystroke counts, screenshots, application usage, idle detection — measures presence and motion rather than output, and its deployment has grown with remote work. The evidence that it improves performance is thin; the evidence that it damages trust and correlates with attrition is better established.

## Current Tech Landscape
Employer-of-record platforms operate owned or partnered entities across many countries with payroll, benefits, onboarding and termination handled locally. Global payroll aggregation connects to in-country providers. Contractor management handles invoicing, tax forms and payments across jurisdictions. Compliance content is maintained internally and surfaced as guidance rather than as advice, with the liability boundary carefully drawn. Monitoring tools integrate at the endpoint and produce activity reports. Equipment provisioning and device management for distributed teams is an adjacent and growing category.

## Problems
- [[problems/remote-work-infrastructure/high-impact|🔴 High Impact: The Platform Certifies Compliance in Sixty Countries and Nobody Can Audit the Determination]]
- [[problems/remote-work-infrastructure/low-impact-1|🟡 Low Impact: Payroll and Benefits Localisation]]
- [[problems/remote-work-infrastructure/low-impact-2|🟡 Low Impact: Activity Monitoring That Measures Motion]]
- [[problems/remote-work-infrastructure/worker-life-1|🟢 Worker Life: The Employee Whose Employer Is a Company They Have Never Heard Of]]
- [[problems/remote-work-infrastructure/worker-life-2|🟢 Worker Life: The Compliance Specialist Tracking Sixty Jurisdictions]]
- [[problems/remote-work-infrastructure/ml-opportunity|🧠 ML Opportunities]]
- [[problems/remote-work-infrastructure/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
This industry sells compliance as a product and delivers it as an assertion. The determinations that matter — classification, permanent establishment, benefit adequacy, termination validity — are legal judgements applied to facts, made by specialists reading internal guidance that is updated manually across dozens of jurisdictions, and presented to the customer as a settled status. When one is wrong, the consequence arrives years later from a tax or labour authority and lands substantially on the client. The platforms hold the information that would make this auditable: the facts of each engagement, the rule that was applied, the date the rule was last verified, and the outcomes of the disputes they have handled. Surfacing that would convert a green tick into evidence, and it is resisted for the same reason it is valuable — an auditable determination is a contestable one.
