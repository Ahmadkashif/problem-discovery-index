# The Mechanism: A $300M Cable, Obsolete in Two Years

**Origin:** [[origins/exchanges-market-makers/profile|Exchanges & Market Makers]]
**Tags:** #optimization-fundamentals #probability-distributions #time-series-forecasting #evaluation-metrics #revenue-impact #automation

> Every other mechanism file in this vault's origins describes an algorithm — a rule for turning data into a decision. This one describes something rarer: a case where the entire competitive advantage was a **physical medium**, not a model, and where the model that mattered was simple enough to fit in a sentence. Read it for what it says about infrastructure investment generally, not for trading strategy.

## The Question Reg NMS Created

Once [[origins/exchanges-market-makers/the-fight|Rule 611]] required every trading venue to avoid executing at a price worse than a protected quote displayed anywhere else in a linked national market, a new, very literal question became commercially decisive: **exactly how many microseconds does it take for a price change on exchange A to become visible and actionable on exchange B?**

Whoever could answer "sooner than everyone else" could trade against a stale quote before the rest of the market updated it — not by predicting the future, but by **seeing the present slightly earlier than a competitor could.** This is latency arbitrage, and its "model" is barely a model at all: if you know a price has already moved and the venue in front of you does not know that yet, trade against its old price before it catches up.

## The Physical Answer: Fibre

**Spread Networks** built a private fibre-optic route between Chicago and northern New Jersey — the two poles of US futures and equities trading — that ran as straight as engineering and rights-of-way would permit, rather than following existing rail or road corridors as prior cables did. The project cost roughly **$300M**, ran 827 miles, and went live in **August 2010**, cutting round-trip latency to **13.3 milliseconds** — about 3 milliseconds faster than the best previous route. In a market where microseconds were now tradeable, 3 milliseconds was an enormous, durable-looking edge.

## The Physical Answer That Beat It

It was not durable. **Light travels faster through air than through the glass of a fibre-optic cable**, and a straight-line microwave link needs no trench, no right-of-way negotiation along a fixed route, and no physical cable at all. **McKay Brothers launched a commercial microwave link in 2012**, pushing one-way latency toward roughly **4.1 milliseconds versus fibre's 6.6 milliseconds** on the same corridor — faster, cheaper to build, and trivially easier to extend or duplicate.

**Spread Networks' $300M asset, engineered to be the fastest physical link money could build in 2010, was competitively obsolete within about two years — beaten not by a smarter algorithm but by a cheaper physical medium exploiting a property of light that had been true since long before either company existed.** (Documented in detail, alongside the broader HFT infrastructure race, in Michael Lewis's *Flash Boys*, 2014.)

## Why This Is the Purest Case in the Vault

Every other origin in this series builds a case that data, or an algorithm, or a regulatory position was the moat. Here, for once, **the moat was a physical fact about the universe — the refractive index of glass versus air — and it was a moat with a two-year lease.** Nobody out-modelled Spread Networks. Somebody built a cheaper pipe.

## The Transferable Pattern

> **When the entire product is speed, the model is often trivial and the infrastructure is everything — which means the infrastructure is exactly as durable as the next cheaper way to move the same signal, and no faster.**

An FDE pricing a "fastest data pipeline" or "lowest-latency inference" product should treat any infrastructure-based speed advantage as rented, not owned, until proven otherwise — because in this industry's own history, the fastest physical asset money could buy lasted about twenty-four months before physics itself was exploited more cheaply by someone else.

**Sources:** Reporting on Spread Networks' Chicago–NJ fibre route (announced 2010, live August 2010, ~$300M, 827 miles, 13.3ms round trip); reporting on McKay Brothers' commercial microwave network (2012, ~4.1ms one-way vs 6.6ms fibre); Michael Lewis, *Flash Boys* (2014).