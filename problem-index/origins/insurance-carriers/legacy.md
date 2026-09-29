# Legacy: What Insurance Carriers Bequeathed

**Origin:** [[origins/insurance-carriers/profile|Insurance Carriers]]

## The Direct Inheritance

| Child | What it inherited |
|---|---|
| [[industries/independent-insurance-agents|Independent Insurance Agents]] | A distribution layer built entirely on top of carrier-computed pricing it does not control and cannot audit — the agent sells the number, the carrier and ISO's pooled data produced it. |
| [[industries/insurtech-platforms|Insurtech Platforms]] | The credibility-weighting shape itself, wearing new clothes. Every insurtech pitch about "better risk segmentation from alternative data" is proposing a new input into a formula Mowbray and Whitney specified in 1914–18 — the industry's real innovation surface has always been *what feeds Z and the class average*, not the blending logic. |
| [[industries/insurance-tpa|Insurance Third-Party Administrators]] | The claims-adjudication layer downstream of a pricing decision it did not make, working from the same class and policy data structures the pooled system produced. |
| [[industries/public-adjusters|Public Adjusters]] | The asymmetry built into claims: the carrier holds the pooled statistical model of what a class of claims should cost; the individual policyholder holds one claim and no model at all. Public adjusters exist specifically to correct that imbalance on the policyholder's side. |
| [[industries/insurance-restoration|Insurance Restoration]] | A billing and scoping structure built to reconcile against carrier-side claims data — vendors that fit the carrier's model of what a covered repair costs get paid faster than vendors who do not. |

## The Deeper Inheritance: Shared Infrastructure, Private Edge

The pattern this origin bequeathed most consistently is not a technology. It is a **market structure**: a heavily regulated, antitrust-exempted shared statistical layer that every competitor draws on, with individual competitive advantage confined to whatever proprietary data or scoring an insurer can add on top of that shared floor.

That structure explains something about the vault's insurance-adjacent industries that would otherwise look like an oddity: **so much of the "innovation" documented in insurtech niches is about acquiring a new data source to feed into an old formula, rather than about building a new formula.** Telematics, wearables, satellite imagery of a roof — each is a new candidate variable for the credibility-weighted estimate described in [[origins/insurance-carriers/the-mechanism|the mechanism]]. None of them changes the shape of the underlying calculation.

## What an Episode Should Take From This

1. **"Insurers were slow" is the wrong story, and it is worth actively correcting when it comes up.** They were 1930s–50s computing pioneers, and the record for that is unusually clean and citable.
2. **A shared, regulator-tolerated statistical commons can outcompete every individual company's private data — right up until it can't.** ISO's pooled loss costs remain the baseline for pricing across the property-casualty industry more than fifty years after its founding, precisely because no single insurtech entrant has assembled a large enough proprietary claims history to replace it outright.
3. **The genuinely defensible layer was never the shared infrastructure. It was always the proprietary input layered on top of it** — first actuaries' judgment, then credit-based scoring in 1993, now whatever alternative data an insurtech can source that a rival cannot. An FDE evaluating an insurtech pitch should ask exactly this: is the new thing a better formula, or a new variable for the same fifty-year-old formula?

**Sources:** See [[origins/insurance-carriers/the-mechanism|The Mechanism]] and [[origins/insurance-carriers/the-fight|The Fight]] for full citations; this vault's `industries/insurtech-platforms.md`, `industries/insurance-tpa.md`, `industries/public-adjusters.md` and `industries/insurance-restoration.md`.