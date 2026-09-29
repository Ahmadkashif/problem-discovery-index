# Policy Checking & Renewal Audit

**Parent Industry:** [[industries/insurtech-platforms|Insurtech Platforms]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in policy checking is fighting to detect every material difference between an expiring policy, what was requested, and what the carrier actually issued — and whoever catches the most differences without a person reading both documents takes the account.

## Profile
**Market Size:** ~$430M US spend attributable to policy checking within agency and carrier operations
**Share of Parent Industry:** ~3% of insurtech revenue, against a substantial block of skilled labour
**Digital Adoption:** Low — the task is reading two documents side by side
**Target Buyer:** Agency and brokerage operations leaders; carrier quality assurance functions
**Automation Potential:** Very High — this is structured document comparison and is performed entirely by reading

## What Makes This a Distinct Niche
Policy checking is the practice of comparing what the carrier issued against what was requested and against what expired, to catch the differences. It exists because the differences are common and consequential: a limit that came back lower than quoted, an endorsement that was dropped at renewal, a location that fell off a schedule, an exclusion that was added, a named insured that was not carried forward. Every one of those is a coverage gap the client believes they do not have, and the agency that failed to catch it carries the errors and omissions exposure. The work is performed by experienced service staff reading a new policy against an expiring one and a quote, page by page, and it is the single most tedious skilled task in agency operations. Many agencies check only their largest accounts, because there is not enough capacity to check them all — which means the exposure is knowingly accepted across most of the book.

## Current Tools & Gaps
Agency management systems hold policy data at a summary level and store the documents. Some outsourced policy checking services exist, performed offshore by people. A few products have attempted automated comparison with limited adoption. The gaps: comparison operates on document text rather than on a structured coverage representation, so it produces noise; endorsement stacks are not resolved, so the comparison is between base forms rather than between operative terms; the quote or request — the third document in the comparison and frequently the most important — is rarely in structured form at all; and nobody measures the outcome, so an agency does not know its own check catch rate, how many accounts go unchecked, or what the differences it finds are worth.

## Problems
- [[niches/insurtech-platforms/policy-checking-renewal-audit/build|🔨 Build: Three-Way Comparison of Expiring, Requested and Issued]]
- [[niches/insurtech-platforms/policy-checking-renewal-audit/buy|🛒 Buy: Document Comparison Tooling With a Coverage Model]]
- [[niches/insurtech-platforms/policy-checking-renewal-audit/fix|🔧 Fix: Most of the Book Is Never Checked at All]]
