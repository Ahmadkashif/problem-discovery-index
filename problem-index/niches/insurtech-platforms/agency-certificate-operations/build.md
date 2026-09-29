# Requested Wording Checked Against the Policy

**Niche:** [[niches/insurtech-platforms/agency-certificate-operations/profile|Agency Certificate Operations]]
**Industry:** [[industries/insurtech-platforms|Insurtech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A certificate request arrives specifying additional insured status, a waiver of subrogation and particular wording, and establishing whether the policy actually supports any of it requires a person to read the endorsements.
**Tags:** #bert #large-language-models #transformers #evaluation-metrics #confidence-intervals #compliance #automation #workflow-orchestration
**Contested on:** Every serious competitor in certificate operations is fighting to issue a certificate that provably matches what the policy supports without a person checking — and whoever removes the human verification step takes the agency.

## The Problem
A contract requires the insured to name the owner and the general contractor as additional insureds on a primary and non-contributory basis, with a waiver of subrogation, for ongoing and completed operations. A certificate request arrives quoting that language. An agency service representative opens the policy, checks whether the blanket additional insured endorsement covers parties required by written contract, whether it extends to completed operations, whether the primary and non-contributory wording is present, and whether the waiver endorsement applies. This takes fifteen minutes if the policy is familiar and considerably longer if it is not. Multiply across hundreds of requests a week. When it is not done properly, the agency issues a certificate describing coverage the policy does not provide, which is precisely the errors and omissions scenario the profession worries about most.

## Why Nobody Has Built This
The check requires reading policy endorsements and understanding what they do, which until recently was not automatable. The liability framing has also discouraged it: an agency relying on an automated verification that was wrong is in a worse position than one relying on an employee who was wrong, in the view of many agency principals — which is arguable and is the reason the product must be a check that supports the reviewer rather than one that replaces them. And the agency management system vendors have treated certificates as a document generation feature, which is the easy half.

## What to Build
A verification layer between the request and the issuance. The request's requirements are extracted — additional insured status and scope, primary and non-contributory, waiver of subrogation, limits, named parties, project references — and checked against the policy's actual endorsement stack, with each finding cited to the endorsement that supports or fails to support it. Supported requirements issue automatically. Unsupported ones are flagged before issuance with the specific gap named, which is the moment to go back to the carrier for an endorsement rather than after a claim. Uncertain ones route to a human with the relevant endorsement text assembled. The record of what was verified, against what policy language, at what time, is retained — which is the errors and omissions defence the agency currently does not have. The requirement extraction improves with the agency's own corpus, since the same contract language recurs constantly across an agency's book.

## Target Customer
Independent agencies of any size, agency management system vendors, and the larger brokers whose certificate operations are a staffed function.

## Impact If Built
Certificate operations is one of the largest and least valuable labour blocks in agency work, and the verification is the part that cannot currently be automated away. Beyond the hours, the flagging of unsupported requests before issuance addresses a genuine and widely acknowledged professional exposure — and creates a retained record of the verification, which is worth as much as the time saved.
