# A Provenance Record That Travels With the Part

**Niche:** [[niches/field-service-software/third-party-maintenance/profile|Third-Party Maintenance — Parts Without the Manufacturer]]
**Industry:** [[industries/field-service-software|Field Service Software]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A third-party maintainer installs a part whose origin, test history and revision compatibility are known to one person in the warehouse, in a segment where a counterfeit or wrong-revision component is a regulatory event.
**Tags:** #graph-theory #evaluation-metrics #confidence-intervals #compliance #data-integration #workflow-orchestration #automation #revenue-impact
**Contested on:** Every serious competitor in third-party maintenance software is fighting to source, verify and certify a part for equipment its customer's manufacturer would rather it did not service — and whoever makes parts provenance reliable takes the account.

## The Problem
A board is pulled from stock and installed in a customer's imaging system. Where it came from — a broker, a decommissioned machine, a repair vendor — is in someone's memory or a line in a spreadsheet. Whether it was tested, by whom, against what, is similarly informal. Whether its revision is compatible with this machine's configuration is a judgement made by the technician. If the machine later fails in a way that harms a patient or a study, the maintainer is asked to produce a provenance record and cannot. The same gap makes the customer's own regulatory position uncertain, which is the argument OEMs use against third-party service and which the segment has never answered systematically.

## Why Nobody Has Built This
The segment is fragmented and margin-thin, and provenance record-keeping is overhead with no immediate revenue. The record also has to survive across parties — broker to maintainer to customer — which makes it a network problem rather than a product one, and network problems are not solved by a single vendor selling inventory software. And the incumbent field service platforms serve the OEM side of the market too, which makes building a capability whose purpose is to strengthen the third-party maintainer's position commercially awkward for them.

## What to Build
A part-level record that accumulates rather than resets: source and acquisition, any prior installed life, every test performed with its result and the technician who performed it, the revision and configuration compatibility determined, and every installation and removal. It travels with the part between organisations where parties participate, and stands alone inside a single maintainer where they do not. Compatibility is modelled as a graph — part revision to machine configuration to software version — rather than as a flat cross-reference, because the actual failures come from combinations rather than from single mismatches. Verification checks the part against known-counterfeit indicators and against the maintainer's own history with that source, and a source whose parts fail at an elevated rate becomes visible, which today is a feeling rather than a number.

## Target Customer
Independent service organisations in medical imaging, laboratory and industrial equipment, parts brokers who could differentiate on verifiable provenance, and the healthcare and research customers whose own regulatory position depends on it.

## Impact If Built
Provenance is the segment's structural vulnerability and the OEM's strongest argument against it, and a verifiable record answers it directly — which is worth more competitively than any operational efficiency. Internally, source-level failure rates convert a purchasing decision currently made on price and relationship into one made on evidence.
