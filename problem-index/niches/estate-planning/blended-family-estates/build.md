# Blended Family Estate Conflict Detector

**Niche:** [[niches/estate-planning/blended-family-estates/profile|Blended Family Estates]]
**Industry:** [[industries/estate-planning|Estate Planning]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Attorneys see every conflict between a blended-family client's estate plan documents and their actual asset titling/beneficiary designations — before the client dies and the children from the first marriage discover they've been unintentionally disinherited.
**Tags:** #large-language-models #bert #decision-trees #feature-engineering #evaluation-metrics #tacit-knowledge-ml #compliance

## The Problem
A remarried client comes to an estate planning attorney wanting to "take care of my new spouse during their lifetime, then pass everything to my children from my first marriage." The attorney drafts a QTIP trust that accomplishes this. But the client's $800K IRA still names the ex-spouse as beneficiary. The $500K life insurance policy names the current spouse outright (not the QTIP trust). The joint checking account with the new spouse passes by survivorship, bypassing the trust entirely. The result: at death, the estate plan documents say one thing, but the actual asset distribution — driven by beneficiary designations and account titling that operate outside the will/trust — produces a completely different outcome. Experienced estate planning attorneys develop an instinct for asking about these conflicts, but the information lives across multiple financial institutions and the client often doesn't know their own designations.

## Why Nobody Has Built This
The data needed to detect conflicts lives in multiple places: the estate plan documents (drafted by the attorney), retirement account beneficiary designations (held by Fidelity, Schwab, Vanguard), life insurance beneficiary designations (held by insurance companies), bank account titling (held by banks), and real estate deeds (held by county recorders). No single system has visibility into all of these. The attorney sees the estate plan documents but must rely on client self-reporting for beneficiary designations, which clients frequently get wrong ("I think I changed it when we got married"). Building a conflict detector requires either aggregating data from multiple financial institutions (technically possible via Plaid for some account types) or creating a structured intake process that systematically captures beneficiary designation and titling information that attorneys currently gather haphazardly.

## What to Build
A conflict detection platform with two components: (1) a structured intake module that systematically captures every asset, its titling/ownership structure, and its beneficiary designation (for retirement accounts, life insurance, TOD accounts), and (2) a conflict analysis engine that compares the actual distribution that would occur at death (based on titling and designations) against the intended distribution expressed in the estate plan documents. The system flags misalignments: "IRA at Fidelity ($800K) names Jane Smith (ex-spouse) as primary beneficiary — this overrides the QTIP trust provision in Section 4.2 of the trust agreement." An LLM-assisted extraction layer reads estate plan documents to identify intended distributions, while the structured intake captures actual designations. The tacit knowledge component: experienced blended-family attorneys know which asset types and designation patterns are most likely to create conflicts, and the system learns these patterns to prioritize its review.

## Target Customer
Estate planning attorneys who handle 5-15 blended family cases per month and currently rely on client self-reporting for beneficiary designation information, knowing that clients frequently have outdated or incorrect information.

## Impact If Built
Prevents the #1 cause of estate plan failure in blended families: beneficiary designation misalignment. Each prevented failure avoids $50K-$500K+ in unintended asset transfers and potential family litigation. Reduces malpractice exposure for attorneys who fail to identify designation conflicts.
