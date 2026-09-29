# Integration Support Triage

**Parent Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Category:** Underserved Audience
**Contested on:** Every serious competitor that takes this seriously is fighting to answer whose fault a failed integration call was, in seconds rather than in an exchange of messages — and whoever does that takes the support organisation, because fault attribution is where every integration ticket begins and most of them end.

## Profile
**Market Size:** ~$240M US attributable to API and integration support operations
**Share of Parent Industry:** ~6% of category revenue
**Digital Adoption:** Low — attribution is established by argument and log comparison
**Target Buyer:** Provider support leadership; the beneficiary is the support engineer
**Automation Potential:** Very High — the request and response are both on record

## What Makes This a Distinct Niche
Integration support has a structure no other support function has: the failure involves two parties, both of whom believe it is the other's fault, and both are partly right often enough that the argument is genuine. The consumer says the API returned an error; the provider says the request was malformed; the truth is frequently that the request was valid under a reasonable reading of the documentation and the implementation is stricter, or that a field the consumer relied on was always optional. Establishing this takes an exchange of messages, log identifiers, timestamps and screenshots across an organisational boundary, and it happens on every ticket. The remarkable thing is that the provider has both the request and the response, in full, with the identifier the consumer is quoting — so the attribution question is determinable immediately and is instead negotiated.

## Current Tools & Gaps
Request logs with correlation identifiers, error responses with codes, developer portals with log access in some products, and support ticketing. The gaps: the consumer usually cannot see their own request as the provider received it, which is the single most useful thing the provider could show them; error responses are written for machines and name a code rather than the field and the reason; correlation identifiers exist and are not surfaced to the consumer at the moment of failure; repeated identical failures from one consumer are not detected, so nobody notices a broken integration until they complain; and the aggregate of consumer errors is never analysed, though it is a precise specification of where the documentation misleads.

## Problems
- [[niches/api-infrastructure-providers/integration-support-triage/build|🔨 Build: Establishing Whose Fault It Was]]
- [[niches/api-infrastructure-providers/integration-support-triage/buy|🛒 Buy: Correlation and Replay, Standard Everywhere Else]]
- [[niches/api-infrastructure-providers/integration-support-triage/fix|🔧 Fix: The Error Response That Names a Code]]
