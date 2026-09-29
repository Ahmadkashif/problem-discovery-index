# Legacy: What Credit Bureaus Bequeathed

**Origin:** [[origins/credit-bureaus/profile|Credit Bureaus]]

## The Direct Inheritance

| Child | What it inherited |
|---|---|
| [[industries/lending-marketplaces|Lending Marketplaces]] | The score as the shared currency every lender and marketplace ranks against — and, per this vault's own note, the same missing-join problem this origin's mechanism describes: the marketplace sees the click and the funding notification, never the repayment outcome that would tell it whether its ranking was any good. |
| [[industries/bnpl-providers|BNPL Providers]] | A population the bureau system structurally cannot score well — thin-file, credit-invisible consumers — became this industry's core addressable market. BNPL's underwriting, per this vault's note, runs on device and behavioural signals precisely because bureau data "may not exist" for its typical applicant. |
| [[industries/collections-agencies|Collections Agencies]] | The direct downstream of every lending decision the bureau enabled, still leaning on bureau and adjacent data (LexisNexis, TLO) for skip tracing — fragmented across systems in exactly the way this vault's note for the industry describes. |
| [[industries/mortgage-brokers|Mortgage Brokers]] | The score as one input into a judgement that, per this vault's own note, still lives mostly in a loan officer's head — which lender's overlays a given profile will actually clear. The statistical number and the tacit knowledge of how underwriters actually behave coexist here, uneasily, exactly as this origin's contested-decision framing predicts. |
| [[industries/credit-unions|Credit Unions]] | The clearest surviving example of this origin's road not taken: this vault's own note describes credit unions still practising relationship-based, character-informed lending — the exact model the bureau system was built to make unnecessary — precisely because, as the note says, it "doesn't scale," which is the same reason the bureaus won the larger fight in the first place. |
| [[industries/independent-insurance-agents|Independent Insurance Agents]] | An indirect inheritance through this vault's `origins/insurance-carriers` origin: FICO extended statistical scoring into insurance underwriting in 1993, and agents placing commercial and personal lines now work against carrier appetite guides shaped, in part, by the same statistical-scoring logic this file describes. |

## The Second Inheritance: concentration risk, realised

Consolidating a nation's credit history into three companies solved the accountability problem FCRA was written for and created a different one: three points of catastrophic failure instead of two thousand. It was realised on a population scale in **2017**, when Equifax disclosed a breach of **approximately 147 million people** — names, Social Security numbers, dates of birth, addresses, driver's licence numbers, and around 209,000 credit card numbers, roughly 56% of American adults. The cause was mundane and avoidable: **a known Apache Struts vulnerability, unpatched despite a notification months earlier.** The resulting settlement, announced in **2019**, ran up to **$700 million** — $425M in consumer relief, $175M to states, $100M in CFPB civil penalties — the largest data-breach settlement on record at the time, on top of $1B+ in committed security spending.

**This is the fight's consolidation logic completing itself.** The same economics of scale that made three bureaus cheaper to run than two thousand also made a single unpatched server catastrophic in a way no individual local bureau's failure ever could have been.

## What an Episode Should Take From This

1. **Two founding dates, not one.** Statistical scoring (1956–58) and the standardised bureau score (1989) are separate events fifteen years apart; conflating them erases the period when scoring existed but wasn't yet the industry standard.
2. **The law caused the consolidation as much as the computer did.** FCRA's compliance burden, layered onto computerisation's existing economies of scale, is why 2,000 bureaus became three — a mechanism this vault's retail-banking origin arrives at independently for a different reason.
3. **Consolidation solves one failure mode and manufactures another.** Three national bureaus are more accountable than two thousand ungoverned local ones, and also a smaller, richer, more catastrophic target — both are true, and an episode should hold both rather than picking the tidier one.

**Sources:** See [[origins/credit-bureaus/the-fight|The Fight]] and [[origins/credit-bureaus/the-mechanism|The Mechanism]] for full citations; CFPB, *CFPB, FTC and States Announce Settlement with Equifax Over 2017 Data Breach* (2019); FTC, *Equifax to Pay $575 Million as Part of Settlement* (2019); this vault's `industries/lending-marketplaces.md`, `industries/bnpl-providers.md`, `industries/collections-agencies.md`, `industries/mortgage-brokers.md`, `industries/credit-unions.md`, `industries/independent-insurance-agents.md`.
