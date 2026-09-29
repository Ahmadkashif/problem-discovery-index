# Everything Is Signed and Nothing Is Verified

**Niche:** [[niches/software-supply-chain-security/artefact-provenance-integrity/profile|Artefact Provenance & Integrity]]
**Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Organisations adopt artefact signing enthusiastically and verification barely at all, which produces a cryptographic record nobody checks and a security property nobody has.
**Tags:** #graph-theory #descriptive-statistics #evaluation-metrics #confidence-intervals #compliance #automation #workflow-orchestration #data-integration
**Contested on:** Every serious competitor here is fighting to prove that what is running was built from what was reviewed, by an authorised process, from known inputs — and whoever does that takes the platform and compliance account, because regulation is now asking and nobody can answer.

## The Problem
A platform team adopts signing. Every build produces a signed artefact with a provenance attestation. The work is done, the initiative is closed, and the deployment path does not verify any of it — because verification requires a trust policy stating which signers and which build processes are acceptable, and failing a verification blocks a deployment, and nobody wanted to own either. The organisation has the cryptographic material to prove provenance and no mechanism that checks it, which provides the appearance of the property and none of its substance.

## Why Nobody Has Built This
Signing is easy to adopt because it adds a step to a build and breaks nothing. Verification is hard to adopt because it can break a deployment, which means somebody must own the policy, the exceptions and the failure path — and the initiative that delivered signing typically did not extend that far. Trust policy is genuinely difficult: an organisation with several build systems, vendored artefacts, third-party images and emergency paths cannot express a simple rule, and the tooling offers little help. And the failure mode of not verifying is silent, so the incomplete adoption looks complete.

## What to Build
Make verification operable. Build the trust policy as a maintained artefact with tooling, since this is where adoption actually fails — expressing which signers, which build processes, which source repositories and which conditions are acceptable, with the ability to evolve it as the estate changes. Verify at deployment and at admission, which is where it provides the property, with the policy evaluated and the decision recorded. Provide a graduated rollout: report-only first, so an organisation can see what would have failed before it does fail, which is the mechanism that makes adoption possible and is absent from most implementations. Give verification failure an operational playbook — who is notified, what the exception path is, how an emergency deployment proceeds — because the first genuine failure at two in the morning determines whether verification survives. Cover the whole chain rather than the final artefact, since the interesting question is whether the source was reviewed and the dependencies were the resolved ones, and a signature on the output alone answers little. Report coverage: what proportion of production artefacts are verified, by policy, which is the honest measure of the property the organisation actually has. And map the technical artefacts to the regulatory questions, since the demand arrives in outcome language and the answer is a set of attestations somebody must translate.

## Target Customer
Platform engineering and compliance functions under regulatory or customer pressure, and the supply chain security vendors whose customers have adopted signing and stopped.

## Impact If Built
Signing without verification is the common state and provides none of the security, and verification fails to be adopted because the policy and the failure path are unowned. Report-only rollout and an operational playbook for failure are what make verification something an organisation can actually turn on.
