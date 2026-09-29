# Verify Once, Prove Anywhere

**Niche:** [[niches/identity-verification-vendors/reusable-verified-identity/profile|Reusable Verified Identity]]
**Industry:** [[industries/identity-verification-vendors|Identity Verification Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A person who has verified successfully nine times still has no way to prove it the tenth.
**Tags:** #compliance #data-integration #workflow-orchestration #evaluation-metrics #automation #graph-theory #confidence-intervals #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to let a person verify once and prove it everywhere without the verifier becoming a tracker — and whoever makes that acceptable to relying parties and to the person removes the repetition the whole category is built on.

## The Problem
Verification is performed independently by every relying party. Each one bears the cost, each one runs the same risk of wrongly rejecting, and the person repeats the same process with the same document indefinitely. The result is a category whose revenue depends on the repetition and a population repeatedly exposed to the same failure. Verifiable credential standards exist and are maturing, and the obstacles are that relying parties will not accept someone else's verification without a liability answer, and that a central reusable identity is a surveillance concern.

## Why Nobody Has Built This
The business model is per-verification, so reuse reduces revenue — an incumbent has a direct commercial reason not to build it and the incumbents are the ones with the verifications. Liability for relying on another party's check is unallocated and nobody wants to hold it. Regulated use cases have their own requirements that a generic credential may not satisfy. And the privacy design is genuinely hard to get right.

## What to Build
Make reuse acceptable rather than merely possible. Issue a credential describing what was verified, how, when and to what assurance level, which is the core and is what a relying party needs in order to decide whether to accept it. Allocate liability explicitly through the credential's terms, because that is the actual obstacle and it is contractual rather than technical. Design so the issuer does not learn where the credential is presented, since a reusable identity that reports back is a surveillance system and will be rejected on that basis. Support selective disclosure, as most relying parties need far less than a full identity and asking for everything is what makes people refuse. Handle freshness and revocation, because a verification from three years ago is not the same claim as one from this morning. Let the person hold and control their own credential, which is both the privacy answer and the reason they will adopt it. Map assurance levels to regulated requirements, so a bank can determine whether a credential satisfies its obligation. Start where repetition is highest and regulation lightest, since that is where adoption is achievable. Keep a fallback to full verification, as no credential will cover everyone. And measure repeat verification rates, which is the size of the problem and is currently the business model.

## Target Customer
Network and product leadership, relying parties paying repeatedly, people verifying repeatedly, and standards bodies and credential issuers.

## Impact If Built
The business model is per-verification, so the parties holding the verifications have a direct reason not to enable reuse. The obstacle is liability allocation and a privacy design, both of which are contractual and architectural rather than technical.
