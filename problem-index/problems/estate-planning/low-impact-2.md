# Asset Inventory Aggregation for Trust Funding Verification

**Industry:** [[estate-planning|Estate Planning Law Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Financial account aggregation tools exist for wealth management but aren't purpose-built for the estate planning use case — where the goal is confirming that revocable trust funding is complete and that all non-probate beneficiary designations align with the client's overall plan.
**Tags:** #feature-engineering #decision-trees #data-integration #automation #compliance

## The Problem
A revocable living trust is only effective if assets are actually titled in the trust's name — a fact that many clients and some attorneys don't rigorously follow up on after the documents are signed. Clients sign their trust documents, leave the attorney's office, and then don't retitle their financial accounts, real property, or brokerage accounts to the trust. When the client dies, the probate-avoidance purpose of the trust is defeated because the assets are still in the individual's name. Additionally, retirement accounts, life insurance policies, and some investment accounts pass outside the trust via beneficiary designation — and these designations must be coordinated with the trust plan to avoid tax inefficiencies and unintended distributions (e.g., an IRA beneficiary designation naming children outright rather than in trust, defeating creditor protection and stretch provisions).

## What Already Exists
Financial data aggregation platforms (Plaid, Yodlee, Orion) allow wealth managers to connect client financial accounts for portfolio monitoring. Estate planning software (Wealth Counsel) has no financial data integration. Tax software (TurboTax, professional preparers) has income data but not asset titling information. There is no tool that specifically addresses the trust funding gap — confirming that every client asset is either in the trust, passes by beneficiary designation aligned with the plan, or has a specific reason for being titled differently.

## The Customisation Gap
Trust funding verification requires estate-planning-specific logic that generic aggregation tools don't provide: understanding which asset types are typically held in trust vs. held outside by design (retirement accounts shouldn't be in a revocable trust; IRAs need specific beneficiary designation treatment), flagging assets that appear to be in the individual's name that should be in the trust, and checking beneficiary designations on non-probate assets for alignment with the overall plan. This requires mapping the financial data not just to account values but to the specific provisions of the client's trust documents.

## Impact If Solved
Reduces unfunded trust problems that defeat the estate planning purpose. For the attorney, it creates a systematic trust maintenance service offering — annual trust review engagements that confirm funding is complete and designations are current. For clients, it ensures the plan they paid to have drafted actually works as intended.
