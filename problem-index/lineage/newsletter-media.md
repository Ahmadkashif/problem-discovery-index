# Lineage: Newsletter Media

**Industry:** [[industries/newsletter-media|Newsletter Media]]
**Wave:** [[series/eras/wave-10-creator-platform|10 — The Creator Platform]]
**The tool:** the Substack paid newsletter — a publication whose issues go by email to a list, with a subscribe button that charges readers a price the writer sets and a platform that keeps about 10% of subscription revenue, announced on 18 July 2017
**Builder:** Substack
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A writer with readers had no cheap way to charge them.

Email newsletters were old and free to send. What a lone writer lacked was the rest of a publisher: a checkout, recurring billing, a paywall that decided who received the paid issue, a web archive, and a list that kept paying subscribers and free ones apart. Assembling those from separate services was an engineering job, so most writers sold nothing and a few sold advertising.

The founders framed the stakes in their launch post. "As a result of a mass shift of advertising revenue to Google and Facebook, the news business is in crisis," they wrote, and the ad-funded alternative had produced "content farms, clickbait, listicles" and "a 'fake news' epidemic."

There was a proof that the other model worked. Ben Thompson's *Stratechery*, they noted, charged "$100 a year for his newsletter-first publication" and within two years was earning "upwards of $200,000 in annual revenue." But Thompson had built his own stack. The problem was making that repeatable for writers who could not.

## What Got Built

A publication in a box, with the business model fixed in advance.

The launch post, "A Better Future for News," by Chris Best and Hamish McKenzie, 18 July 2017, set the mission in one line: "Make it simple to start a publication that makes money from subscriptions." Substack bundled the sending, the payment processing, design templates and audience tools, and took "a small cut of subscription revenue." Wikipedia puts the cut at 10%.

The design choice that matters is that **the unit is the reader's subscription, not the advertiser's impression.** Revenue scales with how many people pay, not how many people see. Bill Bishop's *Sinocism*, an early publication on the platform, priced at $11 a month or $118 a year.

## Who Built It, And Why Them

Substack, founded in 2017 by Chris Best, Hamish McKenzie and Jairaj Sethi — and the combination is the answer.

Best had co-founded Kik Messenger and Sethi had led its platform: two people who knew how to build consumer software that handled messages at volume. McKenzie was a technology reporter, formerly of PandoDaily — someone who knew what writers needed and why the ad model was failing them.

A publisher could not have built this, because its business was the bundle; a product that let its best writers leave with their readers attacked its own model. An email service provider could have, but it sold sending by volume, not a share of a writer's income. **Substack aligned its revenue with the writer's by taking a percentage, not a fee** — which is why it could charge nothing up front, and why it went on to spend Andreessen Horowitz's $15.3 million Series A of 2019 partly on recruiting writers.

## What It Cost

The percentage is forever. A writer who reaches the scale Thompson did pays the platform a tenth of it indefinitely, for infrastructure whose cost does not grow with price.

The deeper cost is the one the model was meant to avoid. Substack sold writers freedom from the platforms, but email itself runs on mailbox providers the writer does not control. The subscription is paid; whether the issue lands in the inbox, Promotions or spam is decided elsewhere, and reported almost not at all.

## What You Still Touch

Every "Subscribe" button with a price attached to a newsletter follows the model announced in that July 2017 post — as do rivals built to compete with it.

- [[problems/newsletter-media/high-impact|🔴 Inbox Placement as an Unobservable Outcome]] — the delivery layer the subscription model did not own
- [[problems/newsletter-media/worker-life-1|🟢 The Writer on the Daily Deadline]]
- [[niches/newsletter-media/paid-subscription-retention/profile|Paid Subscription & Retention]]
- [[niches/newsletter-media/sender-reputation/profile|Sender Reputation Management]]

**Sources:** Chris Best and Hamish McKenzie, "A Better Future for News," Substack (on.substack.com), 18 July 2017 (mission line, crisis and clickbait quotes, Stratechery figures, "small cut"); Wikipedia, *Substack* (founders and prior roles, 2017 founding, 10% cut, Sinocism pricing, a16z $15.3 million Series A 2019); this vault's `history/newsletter-media.md` (vault material, not independent corroboration). ⚠️ **WebSearch was unavailable this session (session cap reached)**; research was by direct fetch only; Substack's fee support page returned 403. ⚠️ **Not established:** the exact percentage at launch (the 2017 post says only "a small cut"); Substack's payment processor and whether writers could export paying subscribers at launch — not confirmed, so not asserted; Sinocism's launch date on the platform; and whether Y Combinator backed the company. The argument that publishers and email services lacked the incentive to build this is interpretation, not a sourced finding.
