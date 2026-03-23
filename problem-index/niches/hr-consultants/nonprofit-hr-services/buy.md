# Nonprofit Compensation Benchmarking from 990 Data

**Niche:** [[niches/hr-consultants/nonprofit-hr-services/profile|Nonprofit HR Services]]
**Industry:** [[industries/hr-consultants|HR Consultants]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Compensation benchmarking tools (PayScale, Salary.com) serve the for-profit market — nonprofit consultants need benchmarking against IRS Form 990 compensation data from comparable organizations, because that's what the IRS uses to evaluate "reasonable compensation."
**Tags:** #data-integration #regression #tabular-ml #compliance #revenue-impact

## The Problem
Nonprofits must demonstrate that executive compensation is "reasonable" under IRS intermediate sanctions (IRC Section 4958) — meaning comparable to what similar organizations pay for similar roles. The IRS uses Form 990 data as its primary benchmark. HR consultants performing compensation reviews for nonprofit clients must: search GuideStar/Candid for 990s of comparable organizations (similar mission, budget size, geography, and staff size), extract compensation data from Schedule J, normalize for total compensation (salary + benefits + deferred compensation), and build a comparability analysis. This research takes 6-10 hours per executive compensation review because 990 data is semi-structured, comparable organizations must be identified manually, and total compensation components are reported inconsistently across organizations.

## What Already Exists
GuideStar (now Candid) provides searchable 990 data and a compensation benchmarking tool, but it's designed for researchers and funders, not HR consultants. The data is available but not structured for easy comparability analysis. PayScale and Salary.com provide for-profit compensation data that is irrelevant for nonprofit IRS comparability determinations. ERI (Economic Research Institute) offers nonprofit compensation surveys but at $5,000+/year.

## The Customization Gap
HR consultants need a tool that: (1) filters 990 compensation data by mission area (NTEE code), budget range, geography, and organization size, (2) extracts and normalizes total compensation (base + benefits + deferred + other) from Schedule J for all key employees, (3) generates a comparability analysis report that satisfies IRS standards (documenting the methodology, comparable organizations selected, and percentile placement of the client's compensation), and (4) updates annually as new 990 data is filed. The tool should produce a board-ready report that documents the reasonableness determination, protecting both the nonprofit and its board members from intermediate sanctions.

## Target Customer
HR consultants conducting annual executive compensation reviews for nonprofit clients, and nonprofit board compensation committees that need IRS-defensible reasonableness documentation.

## Impact If Solved
Reduces compensation benchmarking from 6-10 hours to 1-2 hours per review. Provides IRS-defensible documentation that protects nonprofit executives and board members from intermediate sanctions (25% excise tax on excess compensation, plus potential 200% additional tax on the organization). For a consultant performing 15 compensation reviews per year, this saves 60-120 hours annually.
