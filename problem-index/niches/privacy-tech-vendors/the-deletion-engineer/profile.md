# The Engineer Who Must Delete It

**Parent Industry:** [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
**Category:** Underserved Audience
**Contested on:** Whether deletion is a capability the systems were built with, or a script an engineer writes each time against infrastructure that resists it.

## Profile

**Market Size:** ~$490M
**Share of Parent Industry:** ~7%
**Digital Adoption:** Low — a ticket and a script
**Target Buyer:** Data and platform engineering leadership
**Automation Potential:** High — deletion is a system design problem with known solutions

## What Makes This a Distinct Niche

The workflow platform routes a deletion request to an engineer. Their warehouse has no row-level deletion path without rewriting partitions. Their backups are immutable by design, because that is what makes them trustworthy against ransomware. Their application logs contain user identifiers and were never meant to be queried by person. Their streaming platform has a retention window and no concept of removing one participant's events. Their feature store holds derived values computed from the data. Their model was trained on it.

None of this is an oversight. Every one of those properties was chosen for a good reason by someone who was not thinking about deletion, because deletion was not a requirement when the system was designed.

So the engineer writes a script. They write a similar script next month. Each one is bespoke, unverified, run against production under a deadline, and the confirmation it produces is their word that it worked.

This is an underserved audience because the entire privacy tooling category stops at the ticket. The person who actually performs the deletion has no tooling, no pattern library, no verification support and no way to say that a system cannot do what is being asked.

## Current Tools & Gaps

Deletion connectors in privacy platforms for common SaaS systems. Ticketing into the engineering tracker. Database delete statements. Retention policies in warehouses and object stores. Some tooling for GDPR-style deletion in specific data platforms.

The gaps are large. There is no pattern library for deletion across common architectures, so every organisation solves the warehouse and log problems from scratch. Backups have no accepted technical answer, only a policy statement. Derived data — aggregates, feature stores, indexes, models — is ignored almost universally. Verification is absent, so the engineer cannot demonstrate the deletion worked. Nothing lets them formally record that a system cannot delete. And deletion is not a design requirement in any system architecture practice, so new systems continue to be built without it.

## Problems

- [[niches/privacy-tech-vendors/the-deletion-engineer/build|🔨 Build: Deletion as a Platform Capability]]
- [[niches/privacy-tech-vendors/the-deletion-engineer/buy|🛒 Buy: Retention and Deletion From the Data Platforms]]
- [[niches/privacy-tech-vendors/the-deletion-engineer/fix|🔧 Fix: The System Cannot Do It and There Is Nowhere to Say So]]
