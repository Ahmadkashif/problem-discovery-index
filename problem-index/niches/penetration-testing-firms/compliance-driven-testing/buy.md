# Buy: Compliance Automation Extended Into Testing

**Niche:** Compliance-Driven Testing
**Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Compliance automation platforms already sit between the buyer and the requirement, collecting every other piece of evidence, and hand off the testing requirement to a partner and a PDF.
**Tags:** #evaluation-metrics #compliance #data-integration #workflow-orchestration #automation #confidence-intervals
**Contested on:** Whether the engagement is scoped to find problems or to produce the artefact an auditor will accept, and whether anyone is willing to say which.

## The Problem

A company pursuing SOC 2 runs the whole programme inside a compliance automation platform. Controls are mapped, evidence is collected automatically from cloud accounts and identity providers and ticketing systems, policies are managed, gaps are tracked, and the auditor is given structured access.

Then the platform reaches the penetration testing requirement and stops. It displays a control, suggests a partner, and waits for the customer to upload a PDF. The most expensive single item in the programme, and the one whose adequacy is least verifiable, is the one the platform treats as an opaque attachment.

The buyer, who has been guided through every other control with specific evidence requirements, is left to procure a service they cannot evaluate, from firms whose deliverables they cannot compare, against a requirement nobody has defined for them.

## What Already Exists

Compliance automation: Vanta, Drata, Secureframe, Sprinto and Thoropass. Control mapping across SOC 2, ISO 27001, HIPAA, PCI and others, continuous evidence collection from integrated systems, policy management, gap tracking and auditor collaboration. Several have testing partner marketplaces and some resell testing directly.

Testing delivery: Cobalt, Synack and the managed testing platforms, several of which integrate with compliance platforms at the level of delivering a report into them.

Audit: the audit firms accepting the evidence, with largely undocumented internal criteria for what testing satisfies a requirement.

Adjacent: vendor risk platforms — Whistic, SecurityScorecard, Panorays — which collect the same artefact from the other direction as part of third-party assessment.

## The Customization Gap

**Testing is an attachment, not a control with evidence.** Everything else in these platforms is structured evidence with defined adequacy criteria. Testing is a file upload. Treating it like every other control — specific evidence requirements, a scope definition, a coverage statement — is the adaptation and it is mostly a data model and a specification.

**No adequacy guidance for the buyer.** The platforms guide customers precisely on every other control and go silent here. Publishing what depth of testing each framework and each auditor practice actually accepts would be enormously valuable to their users and is information these platforms are better placed than anyone to accumulate, since they see thousands of audits.

**Scope is not derived from the environment.** The platform already knows the customer's cloud accounts, services and data flows through its integrations. It could generate the testing scope, and instead asks the customer to describe their estate to a firm that asks the same question again.

**No structured findings ingestion.** Reports arrive as PDFs. The platform tracks remediation for every other control and cannot track penetration test findings, which are the highest-value findings the customer receives.

**No quality signal on the marketplace.** Partner directories list firms without any indication of depth, coverage or outcome. The platform is in the best position of anyone to collect and surface that and does not.

**The conflict is real.** A platform reselling testing has an interest in the transaction closing, which cuts against publishing candid adequacy guidance. Handling that honestly is the hard part and is also what would distinguish whichever platform does it.

## Target Customer

Vanta and Drata are the obvious adapters — the buyer is theirs, the moment is theirs, the environment data is theirs, and testing is the largest unmanaged item in a programme they otherwise manage end to end.

Testing firms benefit as the supply side of a better-specified market, particularly the ones whose work is deeper than the minimum and who currently have no way to show it at the point of purchase.

## Impact If Solved

The buyer gets guidance at the moment they need it, on the one control where they currently have none, from the platform already guiding them on everything else.

Deriving scope from the environment the platform already knows would eliminate the questionnaire that produces most of the scoping failure described in [[niches/penetration-testing-firms/engagement-scoping/profile|🟠 Engagement Scoping & Estimation]].

And structured findings ingestion would bring penetration test results into the same remediation tracking as every other control, which is where they should have been all along.
