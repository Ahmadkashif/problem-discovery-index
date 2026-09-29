# Verifiable Credentials for Supplier Onboarding

**Niche:** [[niches/procurement-spend-platforms/supplier-side-tools/profile|Supplier-Side Tools]]
**Industry:** [[industries/procurement-spend-platforms|Procurement & Spend Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Verifiable digital credential standards are mature and let an issuer attest something once in a form any relying party can check, and supplier onboarding collects the same certificate as a PDF from every supplier for every buyer.
**Tags:** #compliance #data-integration #graph-theory #evaluation-metrics #confidence-intervals #workflow-orchestration #automation #quick-win
**Contested on:** Every serious competitor building for suppliers is fighting to let a small supplier transact with a large buyer without absorbing the buyer's process cost — and whoever reduces the supplier's cost of being a supplier takes the network.

## The Problem
A buyer requires proof of insurance. The supplier emails a PDF certificate from their broker. The buyer's onboarding team reads it, records the expiry, and chases a renewal in eleven months. Eighteen buyers do the same thing with the same certificate. The insurer knows the policy is in force and could say so directly to anyone the supplier authorises; instead a document is passed around and manually verified, which is both more work and less reliable, since a PDF certificate is trivially alterable and is rarely checked with the issuer.

## What Already Exists
The W3C Verifiable Credentials model and its ecosystem are mature, with wallets, issuer tooling and verifier libraries available as open source and commercially, and real deployments in education and professional licensing — as the construction craft workforce niche elsewhere in this vault describes. Insurance certificate verification services exist. Business registry data is available. Tax identity verification is a standard service. Every component required is present.

## The Customization Gap
The adaptation is to procurement's specific attestations and to an issuer population that includes small brokers and certifying bodies. It requires: (1) issuer onboarding that is nearly free, since the issuers are insurance brokers, small certifying bodies and state agencies with no engineering capacity, and a scheme that requires integration work from them will not start; (2) the specific credential types procurement actually collects — insurance with coverage limits and named insureds, tax identity, diversity and small business certification, quality and security certifications, financial standing — each with a defined schema; (3) revocation and expiry handled properly, since the most common real failure is not forgery but a lapsed policy nobody noticed, and a credential that proves current status is strictly better than a certificate dated last March; (4) buyer-side verification that is trivially fast and produces the audit record the buyer's own compliance requires; and (5) a migration path that accepts documents alongside credentials, because the transition will take years and a scheme requiring purity will not be adopted.

## Target Customer
Large buyers and public agencies with heavy onboarding requirements, procurement platform vendors, insurance brokers and certifying bodies as issuers, and the supplier diversity certifying organisations for whom this is a natural fit.

## Impact If Solved
Insurance certificates alone account for a large share of supplier onboarding and renewal friction, and a verifiable credential that proves current coverage is both less work for everyone and more reliable than the document it replaces. The diversity certification case is the one with the most consequence, since verification is exactly what that programme's credibility depends on and is currently a PDF.
