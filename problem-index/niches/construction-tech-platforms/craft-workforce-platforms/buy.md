# Verifiable Credential Standards Applied to Trade Certifications

**Niche:** [[niches/construction-tech-platforms/craft-workforce-platforms/profile|Craft Workforce Platforms]]
**Industry:** [[industries/construction-tech-platforms|Construction Tech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Verifiable digital credential standards are mature, open and already deployed in education and professional licensing, and construction — an industry where a worker carries a wallet of physical cards — has adopted almost none of it.
**Tags:** #compliance #data-integration #evaluation-metrics #workflow-orchestration #automation #graph-theory #worker-facing #quick-win
**Contested on:** Every serious competitor in craft workforce software is fighting to give a worker a portable, verified record of their own hours, certifications, skills and safety history that follows them between employers — and whoever makes that record trusted by employers takes the market.

## The Problem
A worker arrives at a site with a wallet: an OSHA card, a welding qualification, a scissor lift card, an MSHA card, a site badge from a previous job. The gate checks them by looking at them. Verification of whether a card is genuine, current, or was ever issued requires phoning the issuer, which nobody does, so the industry's credential system is functionally a trust-the-plastic system. Cards are also lost, expire unnoticed, and are occasionally forged, and the contractor discovers the gap during an incident investigation.

## What Already Exists
The W3C Verifiable Credentials model and the Open Badges specification are mature, open standards with real deployment in higher education, professional licensure and digital identity programmes. Wallet applications, issuer tooling and verifier libraries are available as open source and as commercial products. Several credentialing bodies in other industries already issue verifiable credentials. Nothing in the required technology stack is unproven or expensive.

## The Customization Gap
The adaptation is about the issuers and the gate, not the cryptography. It requires: (1) an issuer onboarding path realistic for the bodies that actually issue trade credentials — training providers, union funds, equipment manufacturers, community colleges — many of which are small and have no engineering capacity, which means issuance has to be nearly free and nearly manual to start; (2) verification at a site gate in seconds, offline-capable, on whatever device the gate actually has, because a verification flow that needs connectivity will not survive a jobsite entrance; (3) expiry and revocation handled properly, since the most common real failure is not forgery but a credential that lapsed and nobody noticed; (4) a credential taxonomy specific to the trades so that a verifier can tell whether a credential actually covers the task at hand, which is a content problem requiring trade expertise rather than technical work; and (5) a migration path from the physical card, since the wallet will be mixed for years and a product that requires purity will not be adopted.

## Target Customer
Credentialing bodies, union training funds, safety training providers, large owners and contractors operating gated sites, and the workforce platform vendors who could issue and verify rather than store scans.

## Impact If Solved
Instant verification at the gate replaces a trust-the-plastic system with an actual one, which is a safety improvement as much as an administrative one. For the worker, credentials that cannot be lost and that prove themselves without a phone call are the first building block of the portable record, and the standards to do it have been sitting available and unused for years.
