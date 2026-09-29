# The Fight: Collective Computation Against Antitrust Law

**Origin:** [[origins/insurance-carriers/profile|Insurance Carriers]]
**Outcome:** The shared infrastructure survived; what it was allowed to publish did not.

## Why This Fight Looks Different From the Rest of the Vault

Every other origin in this vault stages its fight as one company against another — American Airlines against People Express, Epic against Cerner. Insurance carriers had that kind of fight too, at the margin, but the fight that actually shaped the industry's computing was structural: **an entire sector was permitted, by a specific 1945 act of Congress, to do something almost no other American industry may do — compute a shared number together and each price against it.**

## The Exemption

The **McCarran-Ferguson Act (1945)** exempted "the business of insurance" from most federal antitrust law, so long as the activity was state-regulated and did not amount to boycott, coercion or intimidation. Courts consistently read this to cover **joint ratemaking** — insurers pooling loss data and computing shared statistics together — because the underlying actuarial problem genuinely required it: an individual insurer, especially a smaller one, frequently did not have enough claims experience in a given class or territory to price it with any statistical confidence on its own. See [[origins/insurance-carriers/the-mechanism|the mechanism]] for why that is a real, not a manufactured, problem.

Regional and state rating bureaus doing this pooling consolidated into a single national body — the **Insurance Services Office (ISO)**, formed **1 April 1971** — which became the shared computing layer for the property-casualty industry: statistical collection, actuarial calculation, standardised policy language, all built once and used by hundreds of competing insurers.

## The Contested Decision, and Where It Broke

Pooling loss data among competitors and then jointly publishing the *price* that follows from it looks, from the outside, exactly like the price-fixing McCarran-Ferguson was never meant to shield — even though the courts had accepted it as "the business of insurance." Through the 1980s, that tension between a national advisory-rate-setting body and ordinary antitrust expectations drew sustained regulatory and public scrutiny.

ISO's response, in **1989**, was to change what it published. It stopped issuing **advisory rates** and began issuing **advisory loss costs** instead — the pooled, computed cost of claims only, with each insurer required to add its own expense and profit loading before the number became an actual price. Insurer control of the organisation was ceded to an independent board with a non-insurer majority in **1994**; ISO became an independent for-profit company in **1997**; **Verisk Analytics** acquired it in **October 2009**.

> ### The myth to kill
> **"ISO sets insurance rates" is wrong, and has been wrong since 1989.** ISO computes and publishes a shared *loss cost* — what claims are expected to cost, pooled across the industry. It has not published an advisory *rate* — what a policyholder actually pays — in over three decades. Every insurer's final price is its own competitive decision layered on top of a number it did not compute alone. Conflating the two erases exactly the antitrust distinction the 1989 change exists to preserve.

## The Second, Quieter Fight: Competing on Top of the Shared Number

Once the pooled loss cost became a shared floor rather than a shared price, the competitive fight moved to **what an individual insurer could compute that its rivals could not** — layered directly on top of ISO's number. The clearest instance is credit-based insurance scoring: **FICO introduced the first dedicated insurance score in 1993**, extending its consumer-credit methodology to predict claim likelihood rather than loan default. By the 2000s and 2010s, **roughly 95% of auto insurers and 85% of homeowners insurers** used credit-based scoring where state law permitted it — a rating factor computed privately, by each insurer's own contract with FICO, sitting on top of a loss-cost baseline every competitor shared.

**The honest shape of this fight is not insurer versus insurer over who computes fastest.** It is the industry, collectively, defending its right to compute the expensive, data-hungry part together — because the alternative was thin, unreliable pricing for anyone without a giant back book — while individual insurers fought each other over the comparatively cheap layer of differentiation bolted on top.

**Sources:** McCarran-Ferguson Act (1945); Wikipedia, *Insurance Services Office*; NAIC, *Credit-Based Insurance Scores* topic page; content.naic.org, CBIS model development trends resources; FICO, insurance-score history and adoption figures.