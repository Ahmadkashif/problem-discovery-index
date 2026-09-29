# Knowing What Actually Leaves

**Industry:** [[privacy-tech-vendors|Privacy Tech Vendors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** The processor register lists the vendors somebody remembered to register, and the tags on the website send data to companies nobody has heard of.
**Tags:** #graph-neural-networks #change-point-detection #gradient-boosting #dbscan #bert #evaluation-metrics #compliance #data-integration

## The Problem
An organisation is responsible for the third parties that process personal data on its behalf, and for the transfers it makes to them. The register of those parties is maintained by asking teams which vendors they use and collecting contractual assurances from each.

The register is incomplete for structural reasons. Teams procure tools directly, marketing adds tags to the website, a vendor subcontracts to a processor nobody was told about, and an integration created for a trial persists for years. The website is the clearest case: a typical commercial site loads scripts that transmit user data to a long list of parties, many added by different teams over time, and the privacy team's register rarely matches what a browser actually observes.

Verification is contractual rather than empirical. An organisation obtains a data processing agreement and a certification from a vendor and treats the obligation as met. Whether that vendor does what the agreement says, subcontracts further, or transfers data to a jurisdiction that was not disclosed is not checked by anyone.

And the consequence has teeth. Enforcement in several jurisdictions has focused specifically on undisclosed data transfers and on the presence of third-party tags collecting data before consent, with findings against organisations who did not know what their own site was doing.

## What Already Exists
Vendor risk modules in the major platforms maintain registers with questionnaire and certification evidence. Website scanning tools detect tags and cookies and are offered by the consent vendors. Tag management systems provide a control point that is only as good as its governance. Browser-based privacy tooling and academic measurement projects have repeatedly documented the gap between declared and actual data flows. Cloud egress monitoring exists on the infrastructure side and is rarely connected to the privacy register.

## The Customisation Gap
Observation should replace declaration. What a website actually loads, in what sequence, before and after consent, to which destinations, carrying what — is directly measurable by rendering the site as a user and watching, and reconciling that against the register and the consent configuration is the specific check that enforcement actions have turned on. Scanning products do part of this and rarely close the loop against the register or the consent state.

Consent-conditioned behaviour is the part that matters most and is measured least. Whether a tag fires before consent, whether rejecting actually stops it, and whether the consent signal propagates to the vendor are all testable by automated interaction, and the failures are common — a rejected category that still transmits is a frequent finding and is almost never detected by the organisation itself.

Server-side flows are the harder half. Data leaving through backend integrations, pipelines and cloud egress is invisible to a browser-based scan, and inferring it requires the same flow analysis the data map needs — which makes these two the same project.

And subcontracting chains are unmapped. A vendor's own processors are disclosed contractually and never verified, and detecting onward transfer from observed behaviour is the only mechanism that would.

## Impact If Solved
Organisations are accountable for data flows they cannot see and maintain a register of the ones they were told about. Observing what actually leaves — from the browser and from the infrastructure — and reconciling it against the register and the consent state addresses precisely the failures enforcement has focused on, and gives a privacy team the one thing it currently lacks about its own organisation, which is a fact rather than a declaration.
