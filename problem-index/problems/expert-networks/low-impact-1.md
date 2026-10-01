# MNPI Screening by Attestation and Sample

**Industry:** [[expert-networks|Expert Networks]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every network and every fund runs the same compliance checks on every expert call, built from conflict-check and surveillance tools designed for other industries, and still relies on a signed form and a chaperone listening to a fraction of calls.
**Tags:** #large-language-models #bert #transformers #evaluation-metrics #compliance #workflow-orchestration #automation

## The Problem
Before an expert is cleared for a call, the network checks that they are not a current employee of the subject company, collects an attestation that they will not disclose confidential information or breach an obligation to a current or former employer, screens for government officials and employees of restricted entities, and applies the client's own rules — many funds bar current employees of any public company, require cooling-off periods after departure, or ban certain topics outright. During the call, some clients require a compliance chaperone, and some networks record and review calls. After the call, transcripts destined for a library are reviewed before publication.

The rules differ by client. A multi-strategy fund, a long-only manager, a private equity firm and a consultancy each impose a different policy on the same network, and the network's compliance analysts apply them by reading a policy document and a profile.

## What Already Exists
Conflict-check and intake tools from legal practice management; employee communications surveillance from banking compliance (lexicon-based and increasingly model-based); identity and sanctions screening; the networks' own attestation workflows; and post-call transcript review by human compliance staff. The largest networks have built internal tooling around all of it.

## The Customisation Gap
Surveillance tools look for misconduct in an employee's own messages; expert-call review is looking for one specific category of statement — a non-public fact about a named company's current or upcoming performance, contract, product or deal — inside an otherwise legitimate conversation about an industry. That needs a classifier trained on the distinction between "the market is softening" and "we lost the Walmart contract last week", which is a domain-specific labelling exercise no generic lexicon covers.

Client policies need to be machine-readable: extracted once from the client's compliance manual into rules (tenure since departure, employer type, banned topics) and applied automatically at profile forwarding rather than discovered by the client's compliance team after the call is scheduled. And employment-status checks need to be continuous, because the risk sits in experts whose current-employer field in the database is two years stale.

## Impact If Solved
Compliance review is the step that makes the whole product purchasable by regulated funds and is a cost every network carries per call. Real-time and post-call MNPI detection, applied consistently across every call rather than a chaperoned sample, turns a sampling defence into full-population evidence that a fund's chief compliance officer can actually show an examiner.
