# District Reimbursement Packages

**Industry:** [[land-developers|Land Developers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Developers in Texas MUDs and Florida CDDs fund roads, water, sewer and drainage up front and are repaid from district bonds, but proving which dollars are eligible is a manual paper chase through pay applications, invoices and engineer certifications.
**Tags:** #large-language-models #bert #feature-engineering #evaluation-metrics #compliance #data-integration #automation

## The Problem
Outside city limits in Texas, and across much of Florida's new suburbs, the public infrastructure under a subdivision is financed by a special district. The developer advances the money: it builds the water lines, sewer, drainage, detention and often roads, and the district later sells bonds and reimburses it. In Texas the district's engineer prepares a bond application with an engineering report, TCEQ approves what may be issued and the Attorney General reviews the issue (search summary). In Florida a CDD issues special-assessment bonds, and FMSbonds alone had financed 478 Florida CDD issues totalling $4.96B since 2020 by the time the University of Florida counted them in 2025. Forestar's 10-K states plainly that it relies on governmental districts to issue bonds to reimburse it for qualified expenses.

The reimbursement depends on documentation. Every eligible dollar has to trace from a contractor's pay application and invoice, through lien waivers and proof of payment, to a line in the engineer's cost summary that the rules allow. Costs have to be split between eligible public facilities and ineligible private ones (amenity centres, landscaping above standard, lot grading), and between districts when a project straddles more than one. Texas rules also require a developer contribution on some facilities (often cited as 30% of certain water, sewer and drainage costs; recalled). The developer's accountant, the district engineer, the district's auditor and bond counsel each review the package. A missing waiver or a mis-coded invoice is a dollar that waits for the next bond series, years later.

## What Already Exists
Construction accounting systems (Sage 300 CRE, Sage Intacct, Yardi, Viewpoint) record job costs and pay applications. Procore and similar platforms hold contracts and change orders. Document management (SharePoint, Box) stores invoices and waivers. District engineers and accountants run reimbursement audits in Excel, and district managers run the budgets and assessment rolls.

## The Customisation Gap
The generic systems track what was spent. Reimbursement needs what was eligible, and that depends on district rules: facility categories by statute and by the district's creation documents; TCEQ or local eligibility and the developer-contribution requirement; splits by district, phase and bond series; cost-sharing with the city or a utility; and an audit trail from each pay-application line to its waiver, payment and engineer certification. The package also has to match the bond schedule. Eligible costs are capped by what assessed value supports, so the developer needs to know which costs to put in the next series and which can wait. A tool built for this would read invoices and pay applications, classify each line against the district's rules, flag missing support, and assemble the reimbursement exhibit the engineer and auditor expect.

## Impact If Solved
Every eligible dollar documented at the time it is paid is a dollar reimbursed in the first bond series rather than a later one. For a developer carrying ~$30M of district-eligible infrastructure (estimate), moving 10% of it into the first series instead of one ~2 years later pulls ~$3M forward, worth ~$0.6M at a ~10% annual cost of capital, and cuts ~2–4 weeks of accountant and engineer time from each bond application (all estimates).
