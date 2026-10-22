# Recorded-Line Supervision Built for Securities

**Industry:** [[commodity-brokers|Commodity Brokers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** FCMs and larger IBs must record the calls and chats that lead to futures trades, and the surveillance tools that review them were built for securities lexicons, so supervisors either read too much or miss what futures misconduct sounds like.
**Tags:** #transformers #bert #large-language-models #evaluation-metrics #compliance #automation #workflow-orchestration

## The Problem
Under the CFTC's 2012 recordkeeping rule, every FCM, and every IB with more than $5M of gross revenue over the prior three years, records oral communications that lead to a futures or options transaction and keeps them for a year. Written communications such as email, chat and text are kept for five years. NFA's supervision rule then expects the firm to review those records reasonably. In practice a compliance officer samples calls, runs keyword searches across chat, and reviews alerts from the archive vendor.

Futures misconduct has its own vocabulary and patterns. A broker promising a farmer that a hedge "can't lose", or calling an options strategy "insurance" without discussing the premium, is a sales-practice issue under NFA's communications rules. Discussing working orders in a way that suggests spoofing, sharing a hedger's order before entering it, trading a customer account without written discretion, or coaching a client through the bona fide hedging rules for position limits are others. Most of it happens in ag and energy jargon over a recorded line, in calls that are mostly about weather and basis.

## What Already Exists
Archiving and surveillance platforms such as Smarsh, Global Relay and NICE capture voice, chat and email, transcribe calls, and score them against lexicons and conduct models. Their models were developed mainly for securities broker-dealers under FINRA rules and for trading-floor market abuse at banks.

## The Customisation Gap
A futures broker needs its own risk taxonomy, mapped to CFTC and NFA rules rather than FINRA's: guarantees against loss, misleading hedging claims, unauthorised discretionary trading, order front-running, spoofing intent, and position-limit evasion. It needs transcription tuned to commodity speech, so contract months, "Z5 corn", basis, crush, cattle on feed, HTA and LRP are recognised rather than garbled. It needs links from each call to the order and fill it led to, so a reviewer sees the conversation next to the trade. And it needs sampling that weights brokers and accounts by risk (new brokers, discretionary accounts, retail speculators, sharp losses) rather than reviewing calls in arrival order.

## Impact If Solved
A compliance officer at a mid-size FCM or IB reviewing a few hundred calls a month (estimate) could cover the risky calls instead of a random sample. Examinations would find a documented, risk-based review. And the firm would catch the sales-practice and order-handling problems that most often turn into NFA disciplinary actions before a customer complaint finds them.
