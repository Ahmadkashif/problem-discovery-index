# Audit Testing & Evidence

**Parent Industry:** [[industries/soc2-audit-firms|SOC 2 & Attestation Audit Firms]]
**Category:** High Market Share
**Contested on:** Whether a control's operation is established from its full population, now that the population is available, or from twenty-five items because that is the convention.

## Profile

**Market Size:** ~$900M
**Share of Parent Industry:** ~30%
**Digital Adoption:** Low — sampling by convention, evidence by request
**Target Buyer:** Audit firm leadership, standards bodies, relying parties
**Automation Potential:** Very high for testing, low for the standards change

## What Makes This a Distinct Niche

Testing is where an opinion acquires whatever weight it has. An attestation tests a sample of each control's population — a number of access reviews, a number of change tickets, a number of onboarding records — and states an opinion about the whole period.

Sampling exists because examining everything used to be impossible. For most clients it no longer is. Compliance platforms hold continuous, complete records of exactly the populations auditors sample: every access review with its date and reviewer, every change ticket with its approval, every provisioning event. The compromise the methodology was built around has largely dissolved and the methodology has not moved.

The gap this leaves is specific. A control can operate badly for most of a period and pass a sample. A sample of twenty-five from a population of four thousand supports a much weaker inference than most readers assume. And the reader's understanding of what was examined and the auditor's are very different — the report says the controls operated effectively, and the basis is a sample the reader cannot see.

The second half of the problem is that even a firm testing exhaustively cannot say so usefully, because the report format does not express it.

### Contested sub-niches

- [[niches/soc2-audit-firms/full-population-testing/profile|🎯 Full-Population Testing]]
- [[niches/soc2-audit-firms/rigour-expression/profile|🎯 Rigour Expression]]

## Current Tools & Gaps

Audit methodology with defined sampling requirements and guidance on sample sizes. Workpaper platforms recording tests performed and evidence obtained. Evidence request lists sent to clients. Compliance platform integrations at some firms, used to collect evidence more easily rather than to change the testing.

The gaps are that the available evidence has not changed the method. Sample sizes are conventional rather than derived from the population and the assurance required. Continuous evidence is used to make sampling easier rather than to replace it. Exceptions found in a sample do not trigger population-wide examination in most engagements. Nothing in the report distinguishes a control tested exhaustively from one tested at twenty-five. And no firm publishes its testing depth, so rigour is invisible to everyone outside the engagement.

## Problems

- [[niches/soc2-audit-firms/audit-testing/build|🔨 Build: Test Everything, Then Say So]]
- [[niches/soc2-audit-firms/audit-testing/buy|🛒 Buy: Continuous Auditing From Internal Audit]]
- [[niches/soc2-audit-firms/audit-testing/fix|🔧 Fix: Twenty-Five of Four Thousand]]
