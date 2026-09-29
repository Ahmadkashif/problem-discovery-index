# Multi-Jurisdiction Employment Compliance

**Industry:** [[hr-tech-platforms|HR Tech Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every HCM platform ships leave tracking, accrual rules and policy libraries, and the rules now differ by city — so a distributed employer configures them wrong and finds out through a claim.
**Tags:** #large-language-models #bert #transformers #word-embeddings #change-point-detection #transfer-learning #compliance

## The Problem
Employment rules have fragmented faster than any software category has kept up with. Paid sick leave accrual differs by state and by city, with different accrual rates, caps, carryover rules and permitted uses. Pay transparency requirements now mandate salary ranges in job postings in a growing list of jurisdictions with different thresholds. Predictive scheduling ordinances impose notice requirements and penalties in specific cities. Leave entitlements, final paycheque timing, expense reimbursement, meal and rest breaks, and worker classification all vary.

Remote work made every employer multi-jurisdictional. A company with sixty employees may now have people in twenty states and several cities, each with its own rules, and the HR generalist configuring the platform is not a lawyer.

So policies get configured to the strictest rule the company knows about, or to the headquarters rule, and the gaps surface as a claim, an audit or a demand letter.

## What Already Exists
HCM platforms ship configurable leave and accrual engines that are technically capable of representing almost any rule. Employment law publishers and compliance services (Littler, Jackson Lewis, XpertHR, Brightmine) track developments and publish summaries. PEOs absorb the burden for smaller employers. Some platforms offer state-level policy templates.

## The Customisation Gap
Templates exist at state level and the growth is at city level, which is where coverage collapses. Nobody maintains a machine-readable rule set at municipal granularity, because the long tail is unfundable by hiring.

Monitoring is the specific gap. Ordinances are adopted continuously and published in municipal code, and no vendor watches for them — employers discover a new requirement from a newsletter or a complaint. Continuously tracking municipal and state employment law changes, extracting the operative rule, and flagging every affected employer is a monitoring problem on public documents.

Applicability is the second half and is where employers actually get it wrong. Which rule applies depends on where the employee works, where the employer is located, headcount thresholds that vary by ordinance, and sometimes on hours worked in the jurisdiction. Determining the applicable rule set per employee from the platform's own records is straightforward once the rules are structured and is currently done by someone reading a summary.

Configuration verification is the third: whether the accrual actually configured matches the rule that applies is checkable automatically and is never checked until a dispute.

## Impact If Solved
Every distributed employer is out of compliance somewhere and does not know where, and the discovery mechanism is a claim. Automating rule monitoring, applicability and configuration verification protects employees from entitlements they are not receiving and employers from a class of liability they cannot currently see.
