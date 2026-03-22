# Tax Law Change Impact Analysis

**Niche:** [[niches/estate-planning/high-net-worth-trusts/profile|High-Net-Worth Trusts]]
**Industry:** [[industries/estate-planning|Estate Planning]]
**Type:** Fix (Pain Point)
**One-liner:** When estate tax exemptions change — as they will in 2026 — attorneys stop manually reviewing every HNW client's plan to determine who needs restructuring and how urgently.
**Tags:** #large-language-models #logistic-regression #feature-engineering #evaluation-metrics #compliance #automation

## The Problem
The federal estate tax exemption is scheduled to drop from ~$13M to ~$7M per person in 2026. Every HNW estate planning firm must review hundreds of existing client plans to determine: which clients are now exposed to estate tax they weren't before, which existing trust structures become suboptimal under the new exemption, and which clients need immediate action (gifting before the sunset) vs. those who can wait. Attorneys are doing this review manually — pulling each client file, recalculating exposure under the new exemption, and prioritizing outreach. A 200-client HNW practice faces 400-600 hours of review work. This same problem recurs with every legislative change affecting estate tax, gift tax, or trust taxation.

## Why It's Still Broken
Estate planning software stores documents, not structured planning data. When an attorney drafted a client's plan 5 years ago, the key parameters (asset values at time of planning, trust structure chosen, exemption amount used, gift tax exclusions utilized) were captured in the documents and the attorney's notes, not in a queryable database. To assess the impact of a law change, the attorney must re-read the plan documents to extract the relevant parameters before they can even begin the recalculation. No estate planning tool maintains a structured, queryable representation of each client's planning parameters that could be batch-analyzed against new tax rules.

## What a Fix Looks Like
A client plan parameter database that extracts and maintains structured data from estate planning documents: trust types, funding amounts, exemption amounts used, beneficiary structures, asset values (with growth projections), and state of domicile. When a tax law change occurs (or is proposed), the system batch-analyzes all clients against the new rules and produces a prioritized outreach list: "47 clients now have estate tax exposure they didn't have before. The 12 with the largest exposure gaps are listed first, with recommended actions." An LLM-assisted extraction layer reads existing plan documents and populates the structured database retroactively, so the system works even for clients planned years ago.

## Who Feels the Pain
Senior estate planning attorneys who maintain ongoing relationships with 100-300 HNW clients and face periodic legislative changes that require bulk plan reviews. Their paralegals and associates who do the manual file-by-file review work.

## Impact If Fixed
Reduces law-change review cycles from 400-600 hours to 20-40 hours for a 200-client practice. Enables proactive client outreach within days of legislative changes rather than months. Prevents missed deadlines for time-sensitive strategies like pre-sunset gifting, which could save clients millions in estate tax.
