# Control Efficacy Measurement

**Parent Industry:** [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
**Category:** High Market Share
**Contested on:** Whether the relationship between implementing a framework's controls and actually suffering fewer incidents has ever been measured, by anyone.

## Profile

**Market Size:** ~$1.71B
**Share of Parent Industry:** ~19%
**Digital Adoption:** Very low — the question has not been asked
**Target Buyer:** Platform leadership, cyber insurers, regulators, enterprise security buyers
**Automation Potential:** High for normalisation, low for the causal work

## What Makes This a Distinct Niche

The category sells control implementation and the market buys assurance. A SOC 2 report or an ISO certificate is treated by enterprise buyers, insurers and partners as evidence that an organisation is secure. The frameworks behind those certificates are consensus documents — written by committee, revised slowly, and never validated against what actually happens to organisations.

Whether a company with every control green is meaningfully safer than one without is an empirical question, and nobody has answered it. Not the frameworks, which have no outcome data. Not the auditors, who assess conformance. And not the platforms, who hold continuous control state across tens of thousands of organisations and have the only dataset in existence that could.

This is the largest unexamined assumption in enterprise security procurement. Billions of dollars of software, audit fees and engineering time are allocated on the premise that these specific controls reduce risk, in these proportions, and the premise has never been tested. A platform that tested it could say which controls actually matter — the most valuable statement anyone could make about security compliance, and a commercially uncomfortable one for a business that certifies against all of them equally.

### Contested sub-niches

- [[niches/grc-compliance-platforms/control-state-normalisation/profile|🎯 Control State Normalisation]]
- [[niches/grc-compliance-platforms/outcome-linkage/profile|🎯 Outcome Linkage]]

## Current Tools & Gaps

Platforms report control pass rates, framework readiness percentages and time to certification. Some offer benchmarking against anonymised peers, which compares implementation against implementation and says nothing about outcome. Risk quantification approaches such as FAIR model loss exposure from expert estimates rather than from observed control-outcome relationships. Insurers collect security questionnaires at underwriting and hold claims data that is never joined to control state.

The gaps are total. No control is weighted by evidence of effect, so a framework's hundred controls are treated as equally important because nobody knows otherwise. Nothing distinguishes a control that is genuinely load-bearing from one that persists because it was in an early revision. No platform has attempted to relate its own corpus to incidents. Insurers hold the outcome data and the platforms hold the control data and the two have never been joined. And the research literature on security control effectiveness is thin precisely because the observational data sat inside vendors who had no reason to look.

## Problems

- [[niches/grc-compliance-platforms/control-efficacy/build|🔨 Build: Which Controls Actually Matter]]
- [[niches/grc-compliance-platforms/control-efficacy/buy|🛒 Buy: Evidence-Based Practice From Medicine and Insurance]]
- [[niches/grc-compliance-platforms/control-efficacy/fix|🔧 Fix: All Hundred Controls Are Equally Important]]
