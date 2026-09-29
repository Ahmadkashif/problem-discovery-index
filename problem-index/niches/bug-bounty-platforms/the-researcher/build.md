# Build: Expected Value Before the Week

**Niche:** The Researcher
**Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Targeting information that lets a researcher estimate what a week on a given programme is worth — contest level, recent coverage, typical payouts, duplicate risk — before committing the week.
**Tags:** #gradient-boosting #bayesian-inference #evaluation-metrics #confidence-intervals #probability-distributions #survival-analysis #worker-facing #revenue-impact
**Contested on:** Whether a week of skilled work has a knowable expected value, or a payoff decided by who submitted first and how someone rated it afterwards.

## The Problem

A researcher deciding where to spend the coming week has almost no information. They can see a programme's scope, its payout table and its public statistics on resolved submissions. They cannot see how many other researchers are currently working that scope, when the programme was last comprehensively covered, which asset classes have already been exhausted, how often this programme downgrades severity, or what the realistic probability is that anything they find will already have been submitted.

So the allocation decision — the most consequential one they make, repeatedly — is a guess. Experienced researchers develop heuristics: avoid programmes that just launched publicly because everyone is there, prefer recently expanded scope, avoid programmes with reputations for downgrading. These heuristics are folklore, traded privately, and approximate.

The platform could compute all of it. Current participation per programme, submission density by asset class, time since the last wave of coverage, payout distributions by finding class, severity divergence, duplicate rates. Every number is in the database. None is exposed to the person whose entire economic decision depends on it.

## Why Nobody Has Built This

**It would redistribute researcher attention away from some programmes.** Publishing that a programme is heavily contested or rates poorly would reduce its submissions. The programmes are the paying customers, and the platform is the party who would be doing the publishing.

**Duplicate risk is the most useful number and the most sensitive.** Telling a researcher there is a high probability their finding is already submitted means telling them not to bother, which reduces submissions — the metric programmes are shown and platforms report.

**Some of it leaks programme information.** Submission density by asset class tells a researcher where others are looking, which is useful targeting information and also a rough map of where the programme is weak.

**The heuristics work well enough for the top researchers.** The people best placed to demand this have already built private versions from experience, which removes the loudest constituency for building it.

**Supply is assumed abundant.** Platforms have historically treated researcher participation as inexhaustible, so investing in supply-side economics has never been urgent.

## What to Build

**A contest indicator per programme.** How many researchers have submitted recently, trending, by asset class. Not identities — density. This single number would let a researcher avoid the crowded programme, which is the largest driver of duplicate loss.

**Coverage recency.** When each asset class was last the subject of significant submission activity. A scope that has been quiet for a year is a very different prospect from one that had a wave last month, and researchers currently infer this badly.

**Payout distributions by class, per programme.** What this programme has actually paid for this kind of finding, historically, with the distribution rather than the table's stated range. The stated range is aspirational; the history is the truth.

**Programme behaviour statistics.** Severity divergence from the market reference, downgrade frequency, time to triage and to payment, dispute outcomes. This is the accountability half and it belongs here as well as in [[niches/bug-bounty-platforms/severity-and-scope/profile|🟠 Severity & Scope Adjudication]], because the researcher needs it at the moment of choosing.

**An expected-value estimate.** Combining the above with the researcher's own history in comparable technology areas: a rough expected return for a week here. Stated with wide uncertainty, because it deserves wide uncertainty, and still enormously better than nothing.

**Capability-aware matching.** Match researchers to programmes by demonstrated strength in the relevant technology area rather than by overall reputation rank. This is better for everyone — the researcher works where they are strong, the programme gets a specialist — and platforms currently rank by a single aggregate score.

**Portable, verifiable reputation.** A researcher's record as something they can carry between platforms, cryptographically attested. This is against any individual platform's interest and is exactly why it should exist, and an independent body or an open standard is the plausible home.

## Target Customer

Researchers directly, though they are not the paying side — which means the realistic route is a platform treating supply as a competitive constraint rather than a free input.

A platform competing for researcher supply is the natural builder. The smaller platforms have the strongest incentive, since attracting researchers from the incumbents is their main growth path and supply-side transparency is a differentiator the incumbents would find awkward to match.

An independent third party building portable reputation and cross-platform statistics is the more credible long-term home and the harder business.

## Impact If Built

Researchers can allocate the scarcest resource in this market rationally, which is the basic condition of a functioning labour market and is currently absent entirely.

A contest indicator alone would substantially reduce duplicate loss, because most duplication is many people independently working the same newly public scope with no way to see each other.

And capability-aware matching would improve outcomes on both sides simultaneously — a rarity — by putting researchers where their specific strengths apply rather than where their aggregate rank places them.
