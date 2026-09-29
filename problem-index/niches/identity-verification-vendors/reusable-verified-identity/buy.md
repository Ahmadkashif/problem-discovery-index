# Verifiable Credentials and Federated Identity

**Niche:** [[niches/identity-verification-vendors/reusable-verified-identity/profile|Reusable Verified Identity]]
**Industry:** [[industries/identity-verification-vendors|Identity Verification Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Federated identity solved authentication reuse years ago and identity proofing reuse never followed, because proving who someone is carries liability that logging them in does not.
**Tags:** #compliance #data-integration #workflow-orchestration #automation #evaluation-metrics #graph-theory #confidence-intervals #sets-and-logic
**Contested on:** Every serious competitor in this niche is fighting to let a person verify once and prove it everywhere without the verifier becoming a tracker — and whoever makes that acceptable to relying parties and to the person removes the repetition the whole category is built on.

## The Problem
Federated authentication is ubiquitous: sign in with an established provider and the relying party accepts it. The protocols, the trust frameworks and the user expectations are all established. Identity proofing — establishing who someone actually is, not merely that they hold an account — has never federated in the same way, because the relying party is accepting a legal and regulatory responsibility rather than a convenience.

## What Already Exists
Federated authentication protocols; verifiable credential and decentralised identifier standards; identity assurance level frameworks; trust framework governance models; and national digital identity schemes in several jurisdictions.

## The Customization Gap
The adaptation is to a claim that carries regulatory liability. It requires: (1) liability allocation between issuer and relying party, which authentication federation never needed and which is the substantive obstacle — the technology has been ready for years and this has not been settled; (2) assurance levels mapped to specific regulatory obligations, so a relying party can determine sufficiency rather than guess; (3) freshness and revocation semantics for a proofing claim, which differ from a session credential entirely; (4) a privacy architecture where the issuer does not observe presentations, since a proofing federation is far more sensitive than a login one; and (5) commercial incentives that currently oppose reuse, requiring a model where the issuer is paid for the credential rather than per check.

## Target Customer
Network and product leadership, relying parties, standards bodies and trust framework operators, and national digital identity programmes.

## Impact If Solved
The standards have been ready for years and the liability question has not been settled. Answering it — and paying the issuer for the credential rather than per check — is what would let proofing federate the way authentication already has.
