# Income-Qualified Incentive Eligibility Checker

**Niche:** [[niches/solar-installers/low-income-affordable/profile|Low-Income & Affordable Solar]]
**Industry:** [[industries/solar-installers|Solar Installers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A comprehensive eligibility screening tool that takes a household's address, income, household size, and utility account information and instantly identifies every federal, state, local, and utility incentive program they qualify for — including income-qualified programs, disadvantaged community programs, and program stacking rules — replacing the 3-5 hours of manual research installers currently spend per low-income customer.
**Tags:** #gradient-boosting #automation #data-integration #compliance #quick-win #logistic-regression

## The Problem
Low-income solar incentive programs are fragmented across government levels: federal (IRA Section 48(e) low-income bonus credits), state (22+ states with dedicated programs), utility (dozens of utility-specific low-income solar programs), and local (municipal incentives, foundation grants, community development block grants). Each program has unique eligibility criteria — some use area median income (AMI) thresholds, some use federal poverty level (FPL), some use census tract disadvantaged community status, some use utility discount program enrollment as a proxy for income qualification. An installer serving this market must research which programs exist in the customer's jurisdiction, determine eligibility for each, calculate the combined benefit, understand stacking rules (some programs are mutually exclusive), and communicate the financial package to the customer. This research takes 3-5 hours per customer and is error-prone — missing one program can cost the customer $2,000-10,000 in unclaimed incentives.

## Why Nobody Has Built This
The data is fragmented across dozens of sources: DSIRE for state and federal programs, utility websites for utility programs, municipal ordinances for local incentives, and IRS guidance for tax credits. Program rules change frequently — new funding rounds, revised income thresholds, new census tract designations. Maintaining a comprehensive, current database across all jurisdictions requires continuous monitoring of regulatory updates. The market has been small (low-income solar is 3-5% of installations) and the customer base has limited ability to pay for software tools. The IRA's low-income bonus credits (enacted 2022, effective 2023) dramatically increased the incentive value and market size, making this problem newly worth solving.

## What to Build
An eligibility screening platform that: (1) maintains a comprehensive database of all income-qualified solar incentive programs across federal, state, utility, and local levels, with eligibility criteria, benefit calculations, application processes, and stacking rules; (2) takes household inputs — address, income, household size, utility account, homeowner/renter status — and screens against all programs in the database, producing a ranked list of eligible programs with estimated dollar value; (3) calculates the optimal program combination considering stacking rules — some programs reduce the cost basis for tax credits, so the order of application affects total benefit; (4) generates a customer-facing incentive summary showing the total system cost, combined incentive value, and net customer cost; and (5) provides a program update feed when regulations change, alerting installers to new programs or modified eligibility criteria in their service territory.

## Target Customer
Solar installers serving low-income customers (GRID Alternatives affiliates, installers participating in state programs). Community solar developers with low-income subscription carve-outs. Nonprofits and community organizations that help low-income residents access solar.

## Impact If Built
Reduces per-customer incentive research from 3-5 hours to 10-15 minutes through automated eligibility screening. Increases average incentive capture by 15-30% by identifying programs the installer wasn't aware of. Enables mainstream solar installers to serve the low-income market by removing the specialized knowledge barrier. Accelerates low-income solar adoption by making the financial package clearer and faster to assemble.
