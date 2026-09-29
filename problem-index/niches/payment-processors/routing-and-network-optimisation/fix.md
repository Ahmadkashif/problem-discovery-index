# The Optional Fields Nobody Sends

**Niche:** [[niches/payment-processors/routing-and-network-optimisation/profile|Routing & Network Optimisation]]
**Industry:** [[industries/payment-processors|Payment Processors]]
**Type:** Fix (Pain Point)
**One-liner:** The authorisation message has optional fields that issuers' risk models use, the integration omits most of them, and transactions are declined for missing information nobody knew to send.
**Tags:** #data-integration #evaluation-metrics #descriptive-statistics #quick-win #revenue-impact #compliance #automation #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to present the transaction in the way most likely to be approved — route, network, token, authentication, data — and whoever does that prevents the declines everybody else is busy retrying.

## The Problem
The authorisation message supports optional data: address details, the cardholder's name, an email, a phone number, an order identifier, a merchant category detail, a recurring indicator. Issuers' risk models use several of these, and a transaction arriving without them is evaluated on less evidence and declined more often. Most merchant integrations send the required fields and whatever the sample code included. The merchant does not know these fields matter, the processor's documentation lists them as optional, and a measurable share of declines is caused by information the merchant has and did not send.

## Why It's Still Broken
The fields are documented as optional, which reads as unimportant, and nobody quantified what omitting them costs — the word optional is doing the damage and a measured uplift figure would change every integration. Issuers do not publish which fields their models use. The merchant's engineer integrated once and moved on. And the loss is a slightly lower approval rate with no visible cause.

## What a Fix Looks Like
Measure the fields and require what matters. Quantify the approval uplift per field from the processor's own data, which is the fix, is a straightforward comparison across transactions that did and did not include each field, and converts a documentation footnote into a business case. Rename the documentation from optional to recommended with the measured uplift stated, which is a one-line change that would move more approval rate than most engineering projects. Validate at integration and warn when high-value fields are missing, so the gap is caught when the merchant is building rather than discovered never. Populate what the processor can from its own records, since some fields are knowable to the processor even when the merchant omits them. Vary by issuer, because the fields that matter differ and the processor can see which. Audit existing merchants for omissions, which is a list of straightforward revenue improvements the processor can take to each of them. Make the recurring and instalment indicators mandatory where applicable, since these materially change issuer treatment and are widely omitted. Report per-merchant field completeness alongside their approval rate, which makes the connection visible. Feed it into the merchant's integration health score, so it is surfaced continuously rather than at onboarding. And measure the aggregate approval uplift from a field completeness programme, because it is one of the cheapest improvements available in this category.

## Who Feels the Pain
Merchants declined for evidence they had and did not send; processors whose approval rate is limited by other people's integrations; and issuers making decisions on less information than exists.

## Impact If Fixed
The word optional in the documentation is doing the damage, and nobody has quantified what omitting each field costs. A measured per-field uplift turns a footnote into a business case and an integration warning into more approved revenue than most engineering projects deliver.
