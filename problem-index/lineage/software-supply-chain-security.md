# Lineage: Software Supply Chain Security

**Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** SPDX — the Software Package Data Exchange, a machine-readable document listing a package's files, components and licences, begun in 2010 as "Package Facts," version 1.0 August 2011, now ISO/IEC 5962:2021
**Builder:** Linux Foundation
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

The first people who needed to know what was inside a piece of software were lawyers, not security engineers.

By the late 2000s almost every commercial product — phones, routers, televisions, enterprise software — shipped open-source code inside it, and each open-source component carried a licence with obligations: attribution, notices, sometimes source disclosure. A device maker assembling software from dozens of suppliers had to know every component and every licence in the finished build, and so did every customer downstream of it.

The information existed only as prose. Each supplier answered in its own spreadsheet or questionnaire, and each recipient re-did the audit. **The cost was the re-discovery**: the same package scanned and described again at every hop of the chain, because nothing let one party hand its findings to the next in a form a machine could read.

## What Got Built

A document format, not a scanner.

SPDX specifies how to describe a software package: its files with checksums, the components it contains, the licence of each, the copyright text, and who produced the description. The licence part came with its own artefact — the **SPDX License List**, short identifiers such as `MIT` or `Apache-2.0` that give every licence one unambiguous name.

The timeline, per the project's own history: drafting began in **February 2010** in a working group of FOSSBazaar under the Linux Foundation, under the working name "Package Facts"; the SPDX name was adopted that August, when it became a pillar of the Foundation's Open Compliance Program. **SPDX 1.0 shipped in August 2011** and handled single packages. Version 2.0 (May 2015) added multiple packages and the relationships between them. SPDX 2.2 (2020) added "SPDX-lite" to meet the NTIA's minimum elements for a software bill of materials, and the Linux Foundation fast-tracked 2.2.1 through ISO as **ISO/IEC 5962:2021**, available August 2021.

## Who Built It, And Why Them

The Linux Foundation — and the reason is neutrality, not engineering.

A licence-disclosure format only has value if suppliers and customers who are commercial rivals all adopt the same one. No single vendor could publish that format without its competitors suspecting it; a scanning-tool company had a direct interest in keeping findings inside its own product. The Linux Foundation already sat between the companies that ship Linux and was building a compliance programme for exactly those members. It could convene them, host the licence list, and eventually carry the specification to ISO — a route open to a standards-minded foundation and not to a vendor.

That origin also fixed the format's shape. SPDX was built to answer **"what licence obligations am I inheriting?"** — a question about identity and provenance, asked once per release.

## What It Cost

**The question changed; the document didn't.** When US federal policy in 2021 made SBOMs a procurement expectation, SPDX was the ready-made candidate precisely because it already enumerated components. But a licence document is a snapshot per release. A vulnerability question arrives continuously, about components that must be matched across thousands of documents from different vendors — and SPDX was never designed around a shared, reliable identifier for doing that join.

So the format solved generation and left consumption without a product. SBOMs pile up as filed compliance evidence, which is what licence-compliance documents always were.

## What You Still Touch

Every `SPDX-License-Identifier:` comment at the top of a source file, and every SBOM a vendor attaches to a federal contract, descends from this licence-compliance format.

- [[problems/software-supply-chain-security/low-impact-2|🟡 Bills of Materials Nothing Consumes]] — the licence snapshot, asked a security question
- [[problems/software-supply-chain-security/high-impact|🔴 Findings Nobody Can Act On]]
- [[niches/software-supply-chain-security/sbom-consumption/profile|SBOM Consumption]]
- [[niches/software-supply-chain-security/artefact-provenance-integrity/profile|Artefact Provenance & Integrity]]

**Sources:** spdx.dev, "About — Overview / History" (February 2010 FOSSBazaar work-group, "Package Facts," August 2010 naming and Open Compliance Program, SPDX 1.0 August 2011, SPDX-lite in 2.2, 2021 ISO fast-track and ISO/IEC 5962 availability August 2021); Wikipedia, *Software Package Data Exchange* (version dates 2.0 May 2015, 2.1 November 2016, 2.2.1 October 2020, 3.0 April 2024; NTIA minimum elements); NIST, "Software Security in Supply Chains: Software Bill of Materials" (EO 14028 §10(j) SBOM definition; SPDX, CycloneDX and SWID as accepted formats). ⚠️ **Not established:** the individuals and member companies who convened the 2010 work-group — not named in the sources fetched, so no founder is credited; the exact date of Executive Order 14028 and of the NTIA minimum-elements report (both 2021 per NIST, day not checked). **Search budget:** the session's WebSearch cap was reached during this note; the claims above rest on direct page fetches only.
