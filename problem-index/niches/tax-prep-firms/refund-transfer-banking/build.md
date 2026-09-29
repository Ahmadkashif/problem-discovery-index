# The Only Record of When the IRS Actually Pays, Used Only to Size an Advance

**Niche:** [[niches/tax-prep-firms/refund-transfer-banking/profile|Refund Transfer & Advance Banking]]
**Industry:** [[industries/tax-prep-firms|Tax Preparation Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** These banks hold millions of filed returns joined to whether the refund arrived, when, at what amount, and whether it was cut — an empirical model of tax authority behaviour that the tax authority does not publish and every taxpayer wants.
**Tags:** #gradient-boosting #survival-analysis #time-series-forecasting #causal-inference #evaluation-metrics

## The Problem
A refund transfer lets a taxpayer pay the preparation fee out of the refund instead of up front, and a refund advance lends cash against a refund not yet issued. Between them they carry a large share of independent and franchise preparation volume, because the customer base is one that often cannot pay a few hundred dollars in January. A small number of banks fund these products, and each runs a real analytical operation to do it: underwrite the advance, set the limit, screen for fraud, and monitor risk at the level of the individual preparer office.

To underwrite an advance you must predict one thing — will this refund arrive, and when. Doing that for two decades produces a dataset with no counterpart anywhere.

The return as filed, every line of it. Then what the IRS actually did: paid in full, paid short, held for review, offset for child support or student loans or state debt, or never paid at all. Joined at the return level, across millions of filings a year, across many filing seasons, across every state.

The IRS publishes aggregate statistics and a generic "most refunds in 21 days." It does not publish which returns get held, for how long, or why. Its own tracking tool tells a taxpayer almost nothing until the money is already moving. Practitioner knowledge about which credits attract review is folklore passed between preparers.

The bank has the answer as a measured distribution. And it uses it to decide how much to lend.

The unbuilt work is that this dataset is the only empirical model of how the tax administration behaves toward ordinary filers, and its most valuable outputs are not credit decisions at all.

## Why Nobody Has Built This
The invoice is a fee on a financial product. Analysis is a cost of underwriting it, funded exactly to the point where losses are acceptable and stopped there. A model that predicts a delay six weeks out is worth building only if the advance is repriced on it; a model that explains *why* the delay happened has no line item.

The season shape reinforces this. Essentially the entire year's volume arrives in a ten-week window. There is no time to investigate anything mid-season, and by the time the data is clean enough to study, the analytical staff are already building next season's rules. The organisation is structured to survive the season, not to learn from it.

There is also a real reluctance to be seen modelling the tax authority. A bank that published which credits draw scrutiny would be handing a map to exactly the population the authority is scrutinising, and it operates under consumer-protection attention it has no appetite to increase.

So the richest observational dataset on American tax administration exists, is refreshed annually, and produces a lending limit.

## What to Build
Treat the refund as an event with an arrival time to be predicted, not a binary to be underwritten.

**Model time-to-refund as survival.** Every return is a subject, the refund is the event, and the season end censors the ones still outstanding. Return characteristics, credit claims, filing method, filing date, prior-year history and state all condition the hazard. This is the natural form for the problem and it is not how it is currently modelled — the current question is "will it clear before my exposure window," a much cruder one.

**Separate the reasons a refund is short.** An offset, a math error notice, a disallowed credit and an identity hold produce similar outcomes in the ledger and completely different outcomes for the taxpayer. The bank can distinguish them from the funding record and largely does not bother, because for repayment purposes they are the same.

**Estimate the effect of return characteristics on review, honestly.** The bank has the closest thing to a natural experiment: near-identical returns, some held and some not, across millions of cases. That is a causal question with a real answer, and the answer is currently guessed at by every preparer in the country.

**Forecast the season, not the return.** Processing speed shifts year to year with law changes, staffing, government shutdowns and system changes. The bank sees that shift in near real time — days before anyone else, because it is watching funding arrive. A within-season nowcast of processing throughput is genuinely valuable to the preparation chains it serves and does not exist.

**Give the taxpayer the prediction.** The single most common question in a preparation office is when the money will come. The bank can answer it with a calibrated interval and instead relays a generic 21-day estimate. A dated, honest estimate — with the reasons a return might be slower — is a better product than the one being sold, and it is built from data already held.

## Target Customer
Chief Risk Officer or VP of Tax Products at a refund-product bank or the programme bank behind a large preparation franchise. The argument is not better loss rates, which are already tolerable. It is that the underwriting dataset supports a product the preparation channel would pay for on its own — a defensible refund timing forecast — and that the channel is the thing actually being competed for.

## Impact If Built
Tens of millions of American households receive a refund that is the largest single payment they see all year, and plan around a date nobody will give them. The only party that can predict that date from evidence uses the prediction to size a loan and throws the rest away.
