# The Discount Nobody Took

**Niche:** [[niches/ap-automation-vendors/payment-timing-and-float/profile|Payment Timing & Float]]
**Industry:** [[industries/ap-automation-vendors|AP Automation Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The terms say two percent for ten days, the invoice was paid on day twenty-eight, and nobody noticed either fact.
**Tags:** #quick-win #descriptive-statistics #evaluation-metrics #automation #revenue-impact #workflow-orchestration #confidence-intervals #data-integration
**Contested on:** Every serious competitor in this niche is fighting to decide when each invoice should be paid by which method, balancing discount capture, working capital and supplier relationship — and whoever optimises it honestly, while float pays for the product, holds the category's central conflict.

## The Problem
Early payment discount terms are printed on invoices and recorded in vendor records as free text. The payment run does not read them. An invoice offering a discount worth a very high annualised return is paid on the standard cycle, and the opportunity passes without appearing in any report. Over a year, across a mid-sized payables book, the unclaimed total is frequently larger than what the company pays for the AP software.

## Why It's Still Broken
Discount terms were captured as descriptive text because that is how they appear on the invoice, so no system ever evaluated them — an unstructured field is invisible to a scheduler. The payment run is a batch with a fixed date. The approval delay often makes the discount window unreachable before anyone could act. And nobody reports discounts missed, so the loss has never been visible.

## What a Fix Looks Like
Read the terms and count the loss. Extract discount terms into structured fields at capture, which is the fix and is the step that makes everything after it automatic. Report discounts available, captured and missed with their annualised value, since that report will be the most persuasive document the finance team sees this year. Flag invoices with a reachable discount window for priority approval, because the approval delay is usually what makes the discount unreachable. Compute the annualised return and compare it to the cost of capital, as the comparison is trivial and the answer is nearly always to take the discount. Schedule payment to the discount date rather than to the run date, which is a scheduling change rather than a rebuild. Alert when a discount is about to lapse, since a day's notice recovers it. Show the terms to whoever is approving, because they currently have no idea a delay is costing money. Negotiate terms where a supplier would offer them and has not been asked, as many would. Track capture rate as an ongoing metric, which keeps the gain from decaying. And disclose whether the platform's own float economics conflict with taking the discount, because the customer is entitled to know.

## Who Feels the Pain
Finance teams leaving free money unclaimed; suppliers who offered a discount nobody took; approvers unaware their delay has a price; and CFOs who have never seen the number.

## Impact If Fixed
Discount terms are captured as free text because that is how they appear, and an unstructured field is invisible to a scheduler. Extracting them and reporting the annualised value of what was missed frequently exceeds the cost of the software.
