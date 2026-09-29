# Lineage: GRC & Compliance Platforms

**Industry:** [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** the Unified Compliance Framework (UCF) — a licensed database that splits every mandate into citation records and maps each citation to a shared set of "common controls," first published 2005 with 60 authority documents
**Builder:** Network Frontiers
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

One firewall rule, five auditors.

By 2004 a large company's IT department was answering to Sarbanes-Oxley, which was new, HIPAA's security rule, which was coming, PCI, ISO 27002, state privacy laws and whatever its customers wrote into contracts. Each mandate arrived as its own document in its own vocabulary, and each got its own project, its own spreadsheet and its own evidence request. The same password policy was proved again for every audit because nobody could say, with authority, that "strong authentication" in one text and "unique user IDs" in another were the same obligation.

The cost was not the controls. It was the **translation** — and it scaled with every new mandate rather than with the size of the estate.

## What Got Built

A database, not an application.

The Unified Compliance Framework takes each **authority document** — a statute, a regulation, a standard, a contract — and breaks it into individual **citations**. Each citation is then mapped to a **common control**: one harmonised statement of what must be true, written general or specific as the source demands. Pick the authority documents that apply to you and the framework returns the de-duplicated list of controls that satisfies all of them at once.

It shipped in 2005 with 60 authority documents. By 2015 Network World reported more than 800 documents, roughly 90,000 citation records and about 9,000 common controls. It reaches most users indirectly: GRC vendors license the mapped content and embed it, and Unified Compliance later sold direct access through a portal, the Common Controls Hub, including a free tier limited to five authority documents.

## Who Built It, And Why Them

Network Frontiers, the firm of Dorian Cougias, working with the technology lawyer Marcelo Halpern.

The company's own account dates the idea to spring 2004, in a Miami conference room where blue-chip CIOs described the same complaint: duplicated mandates, siloed projects, rising cost and error. Cougias and Halpern then examined the existing frameworks and found they mixed general and specific controls in a way that made requirements hard to trace and harder to maintain when a new mandate landed.

**Why them and not a software vendor** is visible in the pairing. The hard part was never storage or workflow — it was a defensible legal reading of what each citation requires, plus a repeatable rule for when two citations are the same control. That needed a lawyer's interpretation and a publisher's discipline; the company reports developing 270 mapping rules and testing them for six months. A GRC tool vendor had every reason to buy that mapping rather than build it, because it has to be re-done every time any regulator anywhere revises a sentence.

## What It Cost

**Equivalence is asserted, not measured.** A common control says two citations are satisfied by the same thing; it says nothing about whether that thing reduces risk. The framework is a map of obligations, and — as its own coverage noted — it identifies required controls without verifying they work.

The second trade is dependency. The mapping is proprietary and licensed, so the crosswalk at the heart of many platforms is a third party's interpretation, updated on that party's schedule.

## What You Still Touch

Every "test once, comply many" claim in a modern platform — one control shown satisfying SOC 2, ISO 27001 and HIPAA in adjacent columns — is this data structure. So is the dashboard of green controls that nobody has linked to a single prevented incident.

- [[problems/grc-compliance-platforms/low-impact-1|🟡 Mapping Between Frameworks That Overlap]] — the problem the UCF was built for, still unsolved at the edges
- [[problems/grc-compliance-platforms/high-impact|🔴 Every Control Green and Nobody Has Measured What That Buys]] — the question a map of obligations cannot answer
- [[niches/grc-compliance-platforms/framework-mapping/profile|Framework Mapping & Crosswalks]]
- [[niches/grc-compliance-platforms/control-state-normalisation/profile|Control State Normalisation]]

**Sources:** Unified Compliance, "The First Meeting and Founding Ideas Behind the UCF" (company blog — spring 2004 Miami meeting, 2005 release with 60 authority documents, 270 rules, six-month test; self-reported, not independently corroborated); Network World, "The Unified Compliance Framework simplifies how companies manage compliance," 9 April 2015 (800+ documents, ~90,000 citations, ~9,000 controls, free five-document tier, limitation on verification); ResearchGate, "Das Unified Compliance Framework (UCF)" (first published 2005 by Network Frontiers LLC); Crunchbase / LinkedIn company profiles (Network Frontiers dba Unified Compliance). ⚠️ **Not established:** Halpern's firm at the time — the company blog places him at Latham & Watkins, other profiles at Perkins Coie, so no firm is named in the body; Network Frontiers' founding year (profiles give 1992, unconfirmed) and location; whether the UCF was the first cross-mapped control framework — COBIT and vendor crosswalks predate it and I did not establish priority.
