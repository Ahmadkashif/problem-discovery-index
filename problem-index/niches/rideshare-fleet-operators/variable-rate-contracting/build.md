# Build: Earnings-Linked Rental with Verification and Reconciliation

**Niche:** [[niches/rideshare-fleet-operators/variable-rate-contracting/profile|Variable-Rate Contracting]]
**Industry:** [[industries/rideshare-fleet-operators|Rideshare Fleet Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Write the rental as a floor plus a share of verified weekly earnings, with driver-authorised earnings verification and automatic reconciliation.
**Tags:** #compliance #data-integration #confidence-intervals #descriptive-statistics #evaluation-metrics #monte-carlo-methods #revenue-impact #workflow-orchestration
**Contested on:** Whether gig earnings can be verified across platforms with driver consent, reliably enough to bill against.

## The Problem

The fixed weekly rate is the structural defect of this industry. It works when demand is good and fails for everybody at once when it is not, and both parties know this and neither can act on it alone.

A driver would take a revenue share in a heartbeat — it removes the worst weeks, which are the ones that end the arrangement. An operator would consider it if the accounting worked and their lender allowed it. What prevents it is not appetite but infrastructure: there is no way for an operator to know what a driver actually earned that week, no system to administer a variable bill with floors and caps, and no financing structure that treats a revenue-share receivable as bankable collateral.

## Why Nobody Has Built This

Verification is the binding constraint. Lending has payroll and bank verification infrastructure that is mature and widely used; gig earnings verification is comparatively thin and platform-specific, and an operator cannot build it alone. Platform-affiliated rental programmes solve it by being inside the platform, which is precisely why the independent fleet cannot copy them.

Risk transfer is the second constraint and it is real rather than an excuse. The operator's own costs — vehicle finance, insurance, depreciation, facilities — are fixed. Taking demand variance onto a cost base that cannot flex is how a fleet becomes insolvent in a soft quarter, and doing it responsibly requires either capital reserves, a floor in the contract, or a financing partner who shares the exposure. None of these are free.

And there is a characterisation risk. A rental priced as a share of the driver's earnings, with the operator monitoring those earnings, starts to look less like a vehicle lease and more like a participation in the driver's business, with tax, licensing and possibly employment-adjacent implications that vary by state and that nobody wants to be the first to test.

## What to Build

The infrastructure layer, with the contract structure designed around what the verification can actually support.

**Driver-authorised earnings verification.** Consent-based connection to the driver's platform accounts, returning weekly gross earnings and hours — the gig-work analogue of payroll verification, which exists in fragments and not as a standard. This is the keystone: it unlocks not just variable rentals but underwriting, insurance pricing and driver-side financial products generally, which makes it a bigger business than the rental use case alone.

**A contract structure that bounds the operator's exposure.** Not a pure revenue share — a floor covering the operator's fixed cost on that vehicle, plus a share of earnings above it, with a cap. The floor is what makes the position financeable; the share is what makes bad weeks survivable for the driver; the cap is what makes good weeks worth working. Model the structure against the fleet's own history before offering it, because the parameters determine whether the operator has bought insurance or sold it.

**Automatic reconciliation and billing.** Weekly: verified earnings in, contract terms applied, invoice generated, payment collected, with a full audit trail and a clear statement to the driver of how the number was computed. The computation must be explicable in two sentences, because a driver who cannot check their bill will not trust the arrangement regardless of how favourable it is.

**A capital structure that accommodates it.** The operator's exposure to market variance has to go somewhere: reserves sized from the simulation, a lender who prices the structure, or a risk-sharing arrangement. Modelling the fleet's cash flow under market-wide earnings declines — the same Monte Carlo the pricing work needs — is what makes this conversation possible with a financing partner.

**Handle the characterisation deliberately.** Get the structure reviewed in the states of operation, document the arrangement as a vehicle lease with variable consideration rather than as a partnership, and keep the operator out of directing the driver's work. This is legal work rather than engineering and it is the step most likely to stop the project, so it goes first.

## Target Customer

Independent fleet operators competing against platform-affiliated rental programmes, for whom a variable rate is the strongest available differentiator with drivers. More fundamentally, the verification layer has a broader market: gig-earnings verification serves lenders, insurers and fintechs who are all currently unable to underwrite this population, and the fleet use case is one application of it.

## Impact If Built

The structural mismatch at the centre of the industry gets closed: the payment responds to the conditions that determine whether it can be paid. Drivers stop working longer hours to reach zero in bad weeks. Operators trade some upside for a book that does not fail all at once. And gig earnings verification — the missing infrastructure behind a dozen adjacent products — gets built because someone finally needed it enough.
