# Buy: SaaS Discovery, Read as a Processor Inventory

**Niche:** Third-Party & Processor Register
**Industry:** [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** SaaS management and security posture tools already enumerate every third-party application with access to company data, and sell it to IT and security as a spend and risk problem.
**Tags:** #graph-theory #evaluation-metrics #gradient-boosting #compliance #data-integration #automation #change-point-detection
**Contested on:** Whether the list of parties receiving personal data is derived from what actually leaves the organisation, or from what somebody remembered to register.

## The Problem

An organisation's third-party data recipients are already enumerated, by two categories of product, for two other purposes.

SaaS management platforms discover every application in use — through expense data, single sign-on logs, browser extensions and network traffic — to control spend and licence sprawl. SaaS security posture products enumerate OAuth grants and their scopes to find risky integrations with excessive access.

Both produce, as a by-product, precisely the list the processor register is trying to assemble by asking people. An application holding an OAuth grant with read access to the customer relationship system is a processor with access to personal data, whether or not anyone registered it.

The lists exist in IT and security tooling. The register is maintained in a privacy platform by a person sending intake forms. The two are never compared, and the privacy team is frequently unaware the enumeration exists.

## What Already Exists

SaaS management: Zylo, Productiv, Torii, BetterCloud and the SaaS management features in identity providers — discovery through expense, single sign-on, browser and network signals, with application inventories and usage data.

SaaS security posture: Obsidian, AppOmni, Valence, Nudge Security and similar, enumerating OAuth grants, their scopes, the data they can reach and the risk they present.

Identity providers: Okta, Entra and Google Workspace, which authorise the grants and hold the authoritative record of what each application can access.

Cookie and tag scanners: the browser-side half, covered by the consent platforms and dedicated scanners.

Privacy platforms: processor registers populated by intake forms and procurement integration.

## The Customization Gap

**Scope is read for risk, not for personal data.** Security posture tools flag an OAuth grant as excessive. Privacy needs to know that the scope reaches personal data, which categories, and therefore that the application is a processor requiring an agreement. That is a mapping from scope to data category nobody maintains.

**No contractual join.** These tools enumerate applications. Privacy needs each matched against the data processing agreement repository, so the output is a list of processors with and without contractual cover. The join is simple and unbuilt.

**Browser-side and SaaS-side are separate worlds.** Cookie scanners cover tags; SaaS tools cover authorised applications; server-side integrations are covered by neither. The register needs all three and no product spans them.

**Subprocessors are out of scope entirely.** These tools see the direct relationship. The processor register requires the chain beneath it, which comes from the vendor's published disclosures rather than from any telemetry.

**Jurisdiction is not determined.** Security tooling does not care where an application processes. Privacy cares enormously, and the information sits in the vendor's own transfer statements.

**The buyer is in a different function.** IT and security buy these tools and privacy does not know they exist. The most valuable immediate action in most organisations is a conversation between two teams rather than any new software.

## Target Customer

SaaS security posture vendors — Obsidian, AppOmni, Nudge Security — are the most natural adapters, holding the authoritative grant inventory and needing only the data-category mapping and the contractual join to produce a processor register.

The privacy platforms should be integrating with these tools rather than maintaining intake forms, which is a partnership rather than a build.

Privacy counsel as the buyer for the reconciled output, and IT as the party who already holds the input.

## Impact If Solved

The processor register's weakest input — who somebody remembered to register — is replaced by an enumeration that already exists in the building for other reasons.

Mapping OAuth scopes to data categories would identify which applications are processors and which are not, which is a determination currently made by whether someone filled in a form.

And joining the enumeration to the contract repository produces the compliance finding that matters: applications with access to personal data and no data processing agreement, which in most organisations is a substantial list nobody has ever seen.
