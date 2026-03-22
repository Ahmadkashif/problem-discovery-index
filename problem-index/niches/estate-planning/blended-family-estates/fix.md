# Non-Probate Transfer Coordination

**Niche:** [[niches/estate-planning/blended-family-estates/profile|Blended Family Estates]]
**Industry:** [[industries/estate-planning|Estate Planning]]
**Type:** Fix (Pain Point)
**One-liner:** Attorneys stop discovering after a client's death that joint accounts, TOD registrations, and beneficiary designations sent half the estate to the wrong people — because no tool shows the actual distribution outcome across probate and non-probate assets.
**Tags:** #decision-trees #feature-engineering #evaluation-metrics #compliance #data-integration

## The Problem
In a typical American estate, 60-80% of assets pass outside the will or trust: retirement accounts pass by beneficiary designation, life insurance passes by beneficiary designation, joint accounts pass by right of survivorship, TOD (transfer-on-death) brokerage accounts pass by registration, and real estate held in joint tenancy passes by survivorship. The will or trust only controls assets titled in the individual's name alone (or funded into the trust). For blended families, this creates a dangerous gap: the attorney drafts a perfect QTIP trust plan, but the majority of assets bypass it entirely through non-probate transfers. The actual distribution at death looks nothing like the plan on paper.

## Why It's Still Broken
Estate planning attorneys draft documents. They don't control account titling, beneficiary designations, or real estate deeds — those are actions the client must take with each financial institution and county recorder. There is no unified view of how an estate would actually distribute at death, accounting for both probate assets (controlled by the will/trust) and non-probate assets (controlled by designations and titling). The attorney sees their documents; the financial advisor sees the accounts; the insurance agent sees the policies. Nobody sees the complete picture. For blended families, where competing interests make every dollar allocation adversarial, this fragmentation is the primary cause of post-death disputes.

## What a Fix Looks Like
A distribution simulation tool that takes: (1) the estate plan documents (will, trust, POAs), (2) a complete asset inventory with titling and ownership structure, (3) beneficiary designations for all designation-controlled accounts, and (4) family structure (current spouse, children from each marriage, stepchildren). The system simulates death and shows: "Here is exactly how every asset would distribute today." It produces a side-by-side comparison: "Intended distribution per estate plan" vs. "Actual distribution per current titling and designations." Discrepancies are flagged with specific action items: "Retitle the Schwab brokerage account from joint tenancy with spouse to the revocable trust" or "Change IRA beneficiary from spouse outright to QTIP Trust." For blended families, the system calculates each family branch's share (new spouse, children from first marriage, children from second marriage) under both scenarios.

## Who Feels the Pain
Estate planning attorneys who draft plans for blended families and know that the plan is only as good as the client's follow-through on retitling and designation changes. Clients who believe their estate plan protects their children but whose actual asset distribution tells a different story. Family members who discover after death that the estate plan was undermined by non-probate transfers.

## Impact If Fixed
Prevents the most common cause of blended family estate litigation — non-probate transfers that override the estate plan. Each prevented dispute saves $20K-$100K+ in legal fees and years of family conflict. Provides attorneys with a documented recommendation trail for asset retitling and designation changes, reducing malpractice exposure.
