# Legacy: What Retail Banking Bequeathed

**Origin:** [[origins/retail-banking/profile|Retail Banking]]

## The Direct Inheritance

| Child | What it inherited |
|---|---|
| [[industries/payment-processors\|Payment Processors]] | The batch settlement clock, and the resulting split between the authorisation decision and its recorded outcome. The vault's high-impact note for this industry is a direct consequence. |
| [[industries/credit-unions\|Credit Unions]] | The core-banking vendor relationship — strategy constrained by a platform chosen decades ago. |
| [[industries/neobanks\|Neobanks]] | The interface, without the charter. Built entirely on rails they did not lay and cannot change. |
| [[industries/bnpl-providers\|BNPL Providers]] | The point-of-sale credit decision, taken from the incumbent by being present at the moment of purchase. |
| [[industries/lending-marketplaces\|Lending Marketplaces]] | Origination, decoupled from balance sheet. |
| [[industries/collections-agencies\|Collections Agencies]] | The downstream of every lending decision, working from records the lender's batch systems produced. |

## The Rails Argument

Almost every fintech company in this vault is, structurally, **a better interface on top of 1970s infrastructure.**

That is not a criticism, and an episode should resist making it one. It is a genuinely important observation about where value gets created: the rails were laid once, by institutions that no longer capture most of the value they enable, and the profitable position turned out to be adjacent to them rather than beneath them.

But it also sets the limit. A neobank cannot make money move faster than ACH allows. A BNPL provider cannot settle outside the windows. A payment processor cannot get the settlement file earlier than the batch produces it. **Every one of these companies is fast at the parts they built and bounded by the parts they inherited**, and the vault's problem notes for these industries are substantially a catalogue of that boundary.

## The Deeper Inheritance: the missing join, manufactured

The single most repeated finding in this entire vault is some version of: *the organisation observes the outcome of its own decision and never joins the two, because the data sits in two systems on two clocks.*

**That pattern is not a modern failure of engineering discipline. It was built into commercial computing in its first decade**, for entirely sound reasons, and then inherited by everything downstream.

`industries/payment-processors.md` is the exemplar. A processor decides whether to retry a declined authorisation — a prediction — and the result of that prediction lands in a settlement file two days later in a different system. Nobody joins them. The industry consequently treats a prediction problem as a configuration problem, and the vault's own analysis says exactly that.

The cause is in this file.

## What an Episode Should Take From This

1. **The wall was arithmetic, not ambition.** BofA automated because it was going to run out of clerks. The most consequential technology projects are often responses to a business that literally cannot be delivered, not to a vision.
2. **The standard was the unlock — again.** E-13B in 1956, like the UPC in 1973. Two of the spine's first two waves turn on competitors agreeing on a format.
3. **The architecture outlived its reason by sixty-five years and nobody can remove it.** This is the best available answer to a fresh graduate asking why enterprise software is the way it is.

**Sources:** See [[origins/retail-banking/the-mechanism|The Mechanism]] and [[origins/retail-banking/origin-story|Origin Story]]; this vault's `industries/payment-processors.md` (Analysis section).
