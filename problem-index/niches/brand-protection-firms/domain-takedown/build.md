# Build: Blocked in Minutes, Removed in Hours

**Niche:** Domain & Phishing Takedown
**Industry:** [[industries/brand-protection-firms|Brand Protection Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Optimise for protecting users in minutes through blocklists and email defences, with registrar takedown as the slower parallel track rather than as the primary action.
**Tags:** #change-point-detection #gradient-boosting #graph-theory #evaluation-metrics #confidence-intervals #survival-analysis #automation #data-integration
**Contested on:** Whether a malicious domain is removed fast enough to matter.

## The Problem

A phishing domain is registered at nine in the morning, obtains a certificate, is weaponised by eleven, and sends its campaign at noon. Most victims interact within the first few hours.

The takedown process starts when detection surfaces the domain, which may be at one in the afternoon. A request goes to the registrar, who has an abuse process with its own queue and its own response time. The domain comes down at some point between six hours and three days later.

By then the campaign has finished. The takedown removes an asset the operator had already used and was going to abandon. It is counted as a takedown, and the users who were going to be harmed were harmed.

The action that would have protected them is faster and is frequently treated as secondary. Blocklist submission propagates to browsers, email gateways and security products within minutes. Email security vendors can block the sending pattern immediately. The brand's own customers can be warned. Each of these protects users while the takedown is still in a registrar's queue.

The industry counts takedowns, so takedown is the primary action, and the fast protective measures are treated as supplementary.

## Why Nobody Has Built This

**Takedown is the countable action.** A blocklist submission is not a takedown and does not appear in the metric the contract is priced on.

**Blocklist propagation is invisible to the brand.** The firm cannot easily demonstrate that users were protected by a blocklist entry, whereas a removed domain is a concrete deliverable.

**Detection latency is where much of the delay sits.** Being fast at submission does not help if detection took four hours, and detection speed varies enormously between signal sources.

**Registrar response times are unpublished.** Nobody can route to the fastest path or hold a slow registrar accountable, because the data is not collected or shared.

**Pre-weaponisation intervention is contested.** A registered but unused lookalike domain has not done anything yet, and acting against it raises legitimacy questions — though it is the cheapest moment to act.

**Different buyers, different metrics.** Security teams care about user protection and brand teams care about takedowns, and the same contract often serves both with the brand metric.

## What to Build

**Make blocklist submission the first action, automatically.** On detection, submit immediately to browser blocklists, email security vendors and threat intelligence feeds, before the takedown request. Minutes rather than hours, and it protects users while the removal is pending.

**Measure and report time to user protection.** From first observation to blocklist propagation, alongside time to removal. This is the metric that corresponds to harm and it is currently not reported.

**Detect at certificate issuance and at registration.** Certificate transparency surfaces a domain at the moment it prepares to serve traffic, frequently before weaponisation. Registration feeds surface it earlier still. Both are established sources and coverage is inconsistent.

**Predict which registrations will be weaponised.** Lookalike registrations are numerous and most are never used. Ranking by the characteristics that precede weaponisation — registrar, nameserver, certificate timing, hosting choice — focuses attention on the ones that will matter.

**Publish registrar and host response times.** Median time to action per registrar, measured and shared. This would let firms route to the fastest path and would create accountability for the slowest, and the data is a by-product of work already done.

**Attribute infrastructure clusters.** Many phishing domains share hosting, nameservers or registration patterns. Acting at the cluster level removes many domains at once and is the same operator-level logic as everywhere else in this industry.

**Warn the brand's own customers.** Where a campaign targets a brand's customers, the brand can warn them directly and frequently does not, because the response is owned by the enforcement vendor rather than by customer communications.

## Target Customer

Security and fraud teams, who buy this lane, are measured on fraud losses, and would immediately prefer a time-to-protection metric over a takedown count.

Brand protection firms with a security-oriented client base, for whom protection speed is a genuine differentiator that the takedown metric currently hides.

Email security and blocklist providers, who are the fastest protective channel and are underused as an enforcement partner.

## Impact If Built

Users are protected within minutes rather than after the campaign has run, which is the difference between an enforcement action and a prevented harm.

Measuring time to user protection rather than time to takedown aligns the metric with the harm, and it is measurable today by any firm willing to report it.

And publishing registrar response times would create accountability for the slowest abuse processes, which are the single largest source of delay in a lane where hours determine the outcome.
