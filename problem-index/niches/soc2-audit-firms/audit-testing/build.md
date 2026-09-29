# Build: Test Everything, Then Say So

**Niche:** Audit Testing & Evidence
**Industry:** [[industries/soc2-audit-firms|SOC 2 & Attestation Audit Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Test full control populations from the continuous evidence clients already hold, and report the testing depth in a form the relying party can evaluate.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #bayesian-inference #compliance #automation #data-integration #descriptive-statistics
**Contested on:** Whether a control's operation is established from its full population or from twenty-five items because that is the convention.

## The Problem

An auditor tests whether quarterly access reviews were performed. The population is four organisational units over four quarters. They examine a sample and conclude the control operated effectively.

Another tests whether change management approvals were obtained. The population is four thousand changes over the period. They examine twenty-five and conclude the control operated effectively.

The second inference is much weaker than the first and the report expresses them identically. A control failing on ten per cent of changes has a good chance of passing a sample of twenty-five, and the resulting opinion is stated in the same words as one where every change was checked.

The reason for sampling was cost. Examining four thousand change tickets by hand was impossible within any engagement fee, so the profession developed a rigorous framework for inferring from samples — which was the correct answer to the constraint.

The constraint has gone for most of these populations. The client's compliance platform holds every change ticket with its approval status, every access review with its date and reviewer, every provisioning and deprovisioning event. The auditor could query all of it. A test that took a week of an associate's time becomes a query.

## Why Nobody Has Built This

**The report cannot express the difference.** A firm testing full populations issues the same opinion as one testing twenty-five, so the investment buys no commercial advantage.

**The buyer does not want rigour.** The company paying for the audit wants a clean report quickly. More thorough testing finds more exceptions, which is the opposite of what the purchaser is buying.

**Fee structures assume sampling.** Fixed fees are priced on the effort a sample-based audit requires, and a firm testing exhaustively initially spends more to build the capability.

**More testing finds more exceptions.** A firm that tests everything will qualify more reports, which is uncomfortable commercially even where it is correct professionally.

**Standards permit sampling and do not require more.** The methodology is defensible and compliant as it stands, so there is no professional obligation driving the change.

**Data access varies.** Not every client has a compliance platform with complete populations, so the capability applies unevenly and the engagement model must handle both.

## What to Build

**Query the population rather than sampling it.** Direct integration with the client's compliance platform, cloud accounts, ticketing and identity systems to extract the complete population for each control, tested exhaustively where the data supports it.

**Report the testing depth per control.** Population size, number tested, method. Even inside the existing report format, an appendix stating this would be a substantial improvement and would differentiate immediately.

**Escalate on exception rather than stopping.** An exception found in a sample currently triggers a defined expansion. With the full population available, an exception should trigger examination of everything, which produces the actual rate rather than a judgement about it.

**Report the exception rate, not the binary.** A control that operated correctly on ninety-six per cent of a four thousand item population is a far more informative statement than an unqualified pass, and it is available once the population is tested.

**Build the integration once and reuse it.** The same connectors serve every client using the same platforms, which is what makes full-population testing cheaper than sampling after the first few engagements.

**Handle the mixed case honestly.** Where a control's population is not available continuously, sample it and say so. A report distinguishing exhaustively-tested controls from sampled ones tells the reader exactly what they need.

**Publish the methodology.** A firm that publishes how it tests, and what depth it achieves, creates a comparison the rest of the market must answer — which is the only mechanism that would move the industry.

## Target Customer

Audit firms seeking differentiation in a market that has competed to price, for whom testing depth is the first available quality claim and becomes cheaper than sampling once the integrations exist.

Enterprise vendor risk teams — the parties actually relying on these reports — who would prefer an auditor who tested everything and currently cannot tell.

Standards bodies, who could permit or encourage the reporting of testing depth and thereby make the difference visible.

## Impact If Built

The methodological compromise that sampling exists to resolve has largely dissolved and the method has not followed, which makes this an unusually clean opportunity.

Reporting an exception rate rather than a binary pass is a far more informative statement about a control, and it becomes available the moment the full population is tested.

And publishing testing depth is what converts a quality improvement into a commercial one, which is the only way the rest of the market follows.
