# Indicator Lifecycle & Decay

**Parent Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Category:** Highly Automatable
**Contested on:** Whether an indicator is retired when it stops describing reality, or accumulates in the feed indefinitely because removal requires someone to decide.

## Profile

**Market Size:** ~$300M
**Share of Parent Industry:** ~6%
**Digital Adoption:** Low — age is recorded, decay is not modelled
**Target Buyer:** Vendor platform engineering, threat intelligence platform vendors
**Automation Potential:** Very high — decay is observable and modellable

## What Makes This a Distinct Niche

An indicator describes infrastructure at a point in time. Infrastructure moves. An address that hosted a command server last month is reallocated to a hosting customer this month. A domain is seized, sinkholed or expires and is re-registered by someone unrelated. A certificate is revoked. A hash remains valid indefinitely, which makes hashes different from everything else and is rarely reflected in how feeds treat them.

So an indicator's accuracy decays, at different rates for different types, and the decay is the single largest driver of false positives in this industry. An address matching legitimate traffic six months after it was flagged is not a vendor error in collection — it is a vendor failure to retire.

Feeds accumulate because removal requires a positive decision and retention requires none. The result is that a large indicator feed is substantially a historical record presented as a current one, and the customer's analysts absorb the difference.

This is the most automatable niche in the industry. Decay is observable — an indicator that stops matching, or starts matching high-volume ordinary traffic, is telling you something — and modelling it is a well-posed problem on data vendors already hold.

## Current Tools & Gaps

First-seen and last-seen timestamps in most feed formats, inconsistently populated. Expiry fields in some standards, rarely used. Manual retirement when an analyst notices. Sinkhole lists maintained by some vendors. Customer-side age filtering, configured by the customer if they think of it.

The gaps are conspicuous. Decay is not modelled, so there is no per-type or per-context estimate of how long an indicator remains valid. Reallocation is not detected, though address reassignment and domain re-registration are both observable from public data. Sinkholing is detected inconsistently, though sinkholes are well known and largely enumerable. Retirement is manual, so it happens rarely. And no feed publishes its own age distribution, so a customer cannot see that most of what they receive is old.

## Problems

- [[niches/threat-intelligence-vendors/indicator-lifecycle/build|🔨 Build: Modelled Decay and Automatic Retirement]]
- [[niches/threat-intelligence-vendors/indicator-lifecycle/buy|🛒 Buy: Infrastructure Change Data, Already Public]]
- [[niches/threat-intelligence-vendors/indicator-lifecycle/fix|🔧 Fix: Nothing Ever Leaves the Feed]]
