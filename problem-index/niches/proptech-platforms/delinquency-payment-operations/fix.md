# The Assistance Programme Nobody Told the Resident About

**Niche:** [[niches/proptech-platforms/delinquency-payment-operations/profile|Delinquency & Payment Operations]]
**Industry:** [[industries/proptech-platforms|Proptech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Emergency rental assistance programmes exist in most jurisdictions, pay landlords directly, and go unused because neither the household nor the site manager knows what is available or how to apply before the filing deadline passes.
**Tags:** #descriptive-statistics #evaluation-metrics #workflow-orchestration #compliance #automation #worker-facing #quick-win #confidence-intervals
**Contested on:** Every serious competitor in rental payment operations is fighting to identify a household moving into arrears early enough that a payment plan or an assistance referral still works — and whoever finds them earliest, without turning the capability into a screening tool, takes the account.

## The Problem
A household falls two months behind after a job loss. Their county operates an emergency rental assistance programme that would cover the arrears and pays the landlord directly. Neither the household nor the site manager knows it exists, or knows the eligibility rules, or knows that the application requires landlord participation and a W-9 the property has to supply. The case proceeds to a filing. The programme's funds go unspent that quarter, the household loses its home, and the operator absorbs an eviction cost and a vacancy — an outcome in which nobody's interest was served and which a fifteen-minute referral would have prevented.

## Why It's Still Broken
Assistance programmes are administered locally with no central registry, varying eligibility, varying application processes and varying funding cycles, so knowing what is available in a given county at a given moment is genuinely difficult. Site managers turn over frequently and the knowledge is not institutional. Some operators have historically been reluctant to participate in programmes because of documentation requirements or payment timelines. And the delinquency workflow in every platform is a notice calendar with no branch for assistance at all, so even a site manager who knows about a programme has nowhere in the system to record or track it.

## What a Fix Looks Like
Put the programme in the workflow. Maintain, per jurisdiction, what assistance exists, its eligibility criteria, its application process, its current funding status and what the landlord must supply — which is a content operation of the same kind as the other content problems in this industry and is entirely tractable. When a household enters arrears, surface the applicable programmes with a plain-language eligibility check and generate the landlord-side documents automatically, so participation costs the site manager minutes rather than an afternoon of research. Track the application as a state with its own clock against the legal sequence, so a pending application is visible to everyone rather than being a verbal assurance. And measure it: applications initiated, approved, amounts received, and arrears resolved — a figure that would let both operators and programme administrators see, for the first time, how much available assistance is going unclaimed.

## Who Feels the Pain
Households who lose homes while funds sit unspent; site managers who suspect help exists and have no way to find it; and operators absorbing eviction and vacancy costs that a programme would have covered.

## Impact If Fixed
This is the highest-consequence and lowest-technology fix in the industry: the money exists, the eligibility is usually met, and the failure is informational. Putting programme content and application generation into the delinquency workflow converts a research task nobody has time for into a default step, and the measurement would surface how much assistance goes unclaimed — a number that neither operators nor programme administrators currently have.
