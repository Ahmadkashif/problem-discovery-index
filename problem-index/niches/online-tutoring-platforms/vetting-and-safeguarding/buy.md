# Buy: Screening and Safety Tooling Adapted to Unsupervised Contact With Minors

**Niche:** [[niches/online-tutoring-platforms/vetting-and-safeguarding/profile|Tutor Onboarding, Vetting & Safeguarding]]
**Industry:** [[industries/online-tutoring-platforms|Online Tutoring Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Background screening and trust-and-safety products are mature; neither category is built for repeated unsupervised one-to-one contact between an adult contractor and a child.
**Tags:** #compliance #evaluation-metrics #confidence-intervals #large-language-models #data-integration #workflow-orchestration #automation #descriptive-statistics
**Contested on:** Whether general-purpose screening and safety tooling meets the standard this specific exposure requires.

## The Problem

Both halves of this problem have vendors. Background screening — identity, criminal records, sex offender registries, continuous monitoring — is available from established providers and is used widely, including by the platforms in this industry. Trust and safety tooling for messaging and content moderation is mature.

Neither was built for this exposure. Screening products are built for employment decisions, where the risk being managed is to an employer. Content moderation tooling is built for public platforms where the harm is in what is posted. Here the risk is to a child in a private, unsupervised, recurring one-to-one relationship, and the relevant signals are relational and structural rather than content-based.

## What Already Exists

Checkr, Sterling, HireRight and the screening category with continuous monitoring options. Sex offender registry checks and, in some jurisdictions, child-specific clearances. Trust and safety platforms with messaging moderation. Identity verification. Session recording infrastructure. Reporting and case management tooling.

## The Customization Gap

**The standard should be child-contact screening, not employment screening.** Jurisdictions and school systems have specific requirements for people working with children — enhanced checks, registry searches, sometimes fingerprinting, often mandatory re-checking intervals. Screening vendors offer these as options rather than defaults, and platforms frequently buy the employment package. Knowing which standard applies, per jurisdiction, and applying it consistently is the platform's work.

**Continuous monitoring is available and under-bought.** Vendors offer record-update subscriptions and many platforms purchase a one-time check because it is cheaper. For this exposure the recurring product is the appropriate one, and the decision is procurement rather than technology.

**The signals are relational, not content-based.** Moderation tooling classifies messages for policy violations. The pattern here is structural — contact frequency outside sessions, attempts to move off-platform, scheduling anomalies, a single relationship diverging from a tutor's other relationships. That is graph and metadata analysis, which no moderation product offers.

**False positives end a person's livelihood and stain them permanently.** An accusation in this domain is uniquely damaging even when unfounded. The review process — trained reviewers, evidence standards, escalation, documentation, the ability to be cleared — carries far more weight than the detection, and no vendor product includes it.

**The recorded party is a child and the recordings are sensitive.** Retention, access control, who may view a session and under what circumstances, and how a family can request deletion are all compliance questions the platform must answer specifically. Trust and safety tooling assumes public content, not private video of minors.

## Target Customer

Platform trust and safety teams selecting screening and safety vendors, who need to know which package and which standard actually applies. Also the screening vendors, for whom child-contact platforms are a distinct segment with requirements their employment-oriented default does not meet.

## Impact If Solved

The screening, monitoring subscription, identity and case management infrastructure gets bought at the right specification, and the relational signals, the review process and the minors' recording posture get built. The practical result is a platform that can state its standard, apply it consistently, and refresh it — rather than one that checked everyone once.
