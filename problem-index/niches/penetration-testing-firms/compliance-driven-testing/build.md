# Build: The Honest Compliance Package

**Niche:** Compliance-Driven Testing
**Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A productised compliance testing offering that automates everything automatable, states exactly what depth it provides, and prices the upgrade to real assessment explicitly.
**Tags:** #evaluation-metrics #confidence-intervals #gradient-boosting #compliance #automation #workflow-orchestration #revenue-impact
**Contested on:** Whether the engagement is scoped to find problems or to produce the artefact an auditor will accept, and whether anyone is willing to say which.

## The Problem

Compliance-driven testing is sold as penetration testing and is frequently something considerably shallower — automated scanning with a validation pass and a report. This is not necessarily fraudulent; it may be entirely adequate for what the framework requires. The problem is that nobody says so.

The buyer purchases a penetration test and receives a document titled penetration test report. They pass it to their auditor, attach it to customer questionnaires, and cite it to their insurer. Every downstream reader treats it as equivalent to a deep manual assessment, because nothing in the artefact distinguishes them. The security team, who would have preferred a real assessment, has one line in the budget and it is now spent.

Meanwhile the firms doing thorough work are bidding against this in the same procurement, on price, with no way to demonstrate the difference. The rational competitive response is to move down-market, which is why the whole category's pricing is under pressure.

There is an honest version of this product and nobody is selling it: automate what is automatable, do it well and cheaply, state plainly what it covers and what it does not, and offer the deeper assessment as a clearly differentiated upgrade.

## Why Nobody Has Built This

**Ambiguity is profitable.** A firm selling a scan-plus-validation engagement as a penetration test earns more than one selling the same work honestly labelled. The incentive to keep the label vague is direct and operates on the supply side of the whole market.

**The buyer often prefers the ambiguity too.** A compliance buyer who needs an artefact is not harmed by a document that reads as more than it is — it satisfies the auditor, the questionnaire and the insurer. Honest labelling makes their artefact weaker, which is a genuine disincentive on the demand side.

**No framework defines the depth.** SOC 2, PCI and the rest reference penetration testing without specifying what would satisfy it. With no definition, there is no standard against which an honest product could claim compliance, and a firm stating its limits risks a client's auditor rejecting it.

**Productising invites price comparison.** A clearly specified fixed-scope package is easy to compare on price, which compresses margin faster than a bespoke engagement whose scope is fuzzy.

**Firms fear cannibalising the deep work.** An explicit cheap tier looks like an invitation for existing clients to trade down, though in practice the buyers currently buying thin engagements are mostly not buying deep ones either.

## What to Build

**Automate the automatable and be good at it.** External and internal scanning, configuration review, dependency and patch analysis, certificate and exposure checks, credential hygiene — run properly, validated by a human to remove false positives, delivered fast and priced low. This is a real product with real value and it should not pretend to be more.

**Label it precisely.** Not "penetration test" but a named, defined service level with a plain statement of what it comprises: automated coverage across these classes, manual validation, no business logic testing, no authorisation matrix testing, no chained exploitation. The label is the product's whole integrity and its main commercial risk.

**Map to the framework requirement explicitly.** Which control this satisfies, with the specific evidence, formatted for the auditor. The buyer's actual job is satisfying a requirement, and doing that cleanly is genuinely valuable work that is currently done badly.

**Report automated versus manual coverage.** What proportion of the engagement was tooling and what was human, stated in the report. This is the single number that would let a downstream reader distinguish this from a deep assessment, and it is the field the industry most avoids.

**Price the upgrade in the same proposal.** Alongside the compliance package, the assessment the client would need to actually understand their risk, with what it adds. A meaningful share of compliance buyers would buy more if anyone showed them the difference, and today nobody does because the ambiguity is more profitable.

**Sell through the compliance platforms.** The buyer is already in Vanta or Drata managing their SOC 2 evidence. Meeting them there, with the artefact landing straight into their evidence collection, is a far better distribution path than competing in a procurement process on day rate.

**Publish what the framework actually requires.** A firm that documents, per framework and per auditor practice, what depth is genuinely necessary would be doing the industry a service and would establish itself as the honest broker in a market with none.

## Target Customer

Compliance and audit functions at growing technology companies, who buy annually, need the artefact, and are currently overpaying for ambiguity or underbuying without knowing it.

Compliance automation platforms as the distribution channel, since their users are exactly this buyer at exactly the moment of need.

Testing firms themselves as a productised revenue line that stops distracting their senior testers from the deep work they should be doing.

## Impact If Built

The market separates. Compliance buyers get a cheaper, faster, honestly labelled product that does what they need, and risk buyers get assessment — which is better for both and ends the competition between them.

Reporting automated-versus-manual coverage is the single field that would let every downstream reader — auditor, customer, insurer — understand what they are looking at, which is currently impossible.

And the deep testing market stops being dragged toward the price of the thinnest acceptable deliverable, which is the structural pressure making genuinely expert work harder to sell every year.
