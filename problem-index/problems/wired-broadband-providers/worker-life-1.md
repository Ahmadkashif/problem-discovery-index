# The Co-op CSR When the Network Goes Down

**Industry:** [[wired-broadband-providers|Wired Broadband Providers]]
**Type:** Worker Life Changing
**One-liner:** At a small telco or co-op, the same four people who take payments and sell service also answer every call when a fibre is cut, and they find out about the outage from the angry customers calling in.
**Tags:** #change-point-detection #time-series-forecasting #large-language-models #worker-facing #automation #workflow-orchestration

## The Problem
A rural telco, electric co-op fibre subsidiary or small fibre ISP serving ~3,000–30,000 subscribers (estimate) typically has a handful of customer service representatives. They take bill payments, sign up new customers, schedule installs, and handle tier 1 technical support, often for electric and broadband accounts at once. When a backhoe cuts a feeder, a cabinet loses power or an upstream provider has a problem, hundreds of customers lose service at once and the phones light up.

The representative usually has no outage map and no message from the network team yet. The first caller is the alert. They reboot the first customer's router over the phone before realising it is the third call from the same road. They cannot say how many people are affected, what caused it or when it will be back, because the one network engineer is in a truck heading to the cut. Callers are frustrated and sometimes abusive; the queue grows; every call ends with "we're working on it". Afterwards someone works out bill credits by hand.

## Why It Matters to the Worker
The representative absorbs the anger for a failure they had nothing to do with and can do nothing about, without the information that would let them help. In a small community the callers are often neighbours, and "I don't know" lands personally. The same people are judged on call handling time and on sales and payment work that piles up during the outage. Small operators also struggle to keep these staff, and every departure takes the person who knew which customers have medical equipment or run a business from home.

## What a Solution Looks Like
Outages detected automatically from the network itself: when many ONTs or modems behind the same splitter, cabinet or node drop within minutes, the system marks the affected area on a map, posts a status page, updates the phone greeting and texts affected customers before they call. The representative's screen shows, for the caller's address, whether they are inside a known outage, its likely cause and the latest estimate from the field. A language model drafts the customer updates from the engineer's terse field notes. When service returns, the affected accounts and their outage minutes are listed for credits.

## Impact If Solved
Proactive notification can cut outage call volume sharply, and every remaining call is shorter because the representative can answer it. For a team of four, that is the difference between a lost day of sales and payment work and a manageable afternoon, and it removes the worst part of the job: being yelled at with nothing to say.
