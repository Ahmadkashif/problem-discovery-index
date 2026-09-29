# Enterprise Assistant Governance

**Parent Industry:** [[industries/developer-tools-vendors|Developer Tools Vendors]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor here is fighting to make an assistant approvable by a security and legal function — provenance, licence exposure, data boundaries and audit — and whoever does that takes the enterprise, because a blocked tool has no adoption to win.

## Profile
**Market Size:** ~$1.9B US enterprise assistant deployment and governance
**Share of Parent Industry:** ~15% of category revenue
**Digital Adoption:** Medium — deployment is widespread and governance is asserted
**Target Buyer:** Chief information security officers, legal, platform engineering
**Automation Potential:** High — provenance and policy checking are tractable and mostly unattempted

## What Makes This a Distinct Niche
The enterprise purchase of an assistant is not decided by developers. It is decided by whether a security function will permit source code to leave the perimeter, whether legal is satisfied that generated code does not import a licence obligation, whether the vendor can demonstrate rather than assert what happens to the data, and whether the organisation can produce an audit trail when a regulator or a customer asks how a piece of code came to exist. These are the questions that stall deployments for quarters at a time in regulated industries, and they are answered today with contractual language and a trust-me. The competitors are different — this is contested against security tooling vendors and the enterprise procurement process rather than against other editors — and the winning property is demonstrable control rather than suggestion quality.

## Current Tools & Gaps
Enterprise tiers with contractual data commitments, self-hosted and dedicated deployment options, filtering for public code matches, and policy controls of varying depth. The gaps: provenance is asserted through a filter rather than established, so a licence question cannot be answered retrospectively; there is no record of which code was generated, by which model, from which prompt, so the audit question has no answer; policy enforcement is coarse — on or off per repository — where the real requirement is conditional on the code's sensitivity; and nothing measures leakage of secrets or proprietary context into prompts, which is the concrete risk security actually worries about.

## Problems
- [[niches/developer-tools-vendors/enterprise-assistant-governance/build|🔨 Build: Where Did This Code Come From]]
- [[niches/developer-tools-vendors/enterprise-assistant-governance/buy|🛒 Buy: Supply Chain Provenance Applied to Generated Code]]
- [[niches/developer-tools-vendors/enterprise-assistant-governance/fix|🔧 Fix: Secrets and Proprietary Context Leaving in Prompts]]
