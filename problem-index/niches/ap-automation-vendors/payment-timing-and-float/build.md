# When to Pay and How

**Niche:** [[niches/ap-automation-vendors/payment-timing-and-float/profile|Payment Timing & Float]]
**Industry:** [[industries/ap-automation-vendors|AP Automation Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every invoice has an optimal payment date and method, and most are paid on whatever day the run happens to fall.
**Tags:** #optimization-fundamentals #evaluation-metrics #revenue-impact #confidence-intervals #time-series-forecasting #automation #gradient-boosting #compliance
**Contested on:** Every serious competitor in this niche is fighting to decide when each invoice should be paid by which method, balancing discount capture, working capital and supplier relationship — and whoever optimises it honestly, while float pays for the product, holds the category's central conflict.

## The Problem
An invoice offers two percent for payment within ten days, which is a very high annualised return, and is paid on day thirty because that is when the run executes. Another is paid early for no reason, tying up cash that had a better use. A third goes by a method costing more than necessary. These are decisions with clear economics and they are made by a schedule. Meanwhile the platform increasingly earns from float and payment method, which means the optimiser and the beneficiary are the same party and the conflict is undisclosed.

## Why Nobody Has Built This
Payment runs were built as a batch operation, so timing became an operational convenience rather than an economic decision — a schedule is simpler than an optimisation and nobody costed the difference. Discount terms are recorded as text in the vendor record and never evaluated. Float revenue rewards later payment and slower methods. And nobody reports discounts missed.

## What to Build
Optimise the decision and be honest about the conflict. Model each invoice's payment timing against discount terms, cost of capital, cash position and supplier relationship, which is the core and is a well-posed optimisation with clear inputs. Capture early payment discounts automatically where the return beats the cost of capital, since that comparison is arithmetic and the returns are frequently extraordinary. Choose payment method on cost and speed rather than on default, as method economics differ materially and are currently invisible to the buyer. Forecast cash requirements from the payables pipeline, which the platform can do better than any treasury system because it sees the invoices earliest. Weight supplier relationship explicitly, since paying a critical small supplier late to hold cash is a decision that should be made rather than defaulted into. Disclose the platform's own economics on timing and method, because an optimiser with an undisclosed interest will eventually be discovered and the disclosure is a competitive asset. Report discounts available, captured and missed, which is the number that makes the case and is not produced. Handle the constraint that cash is finite, as the optimisation is a scheduling problem rather than a per-invoice one. Offer supplier-side early payment where both sides benefit, which is real value rather than extracted float. And measure the working capital and discount outcome as the product's contribution, since it is larger than the software fee.

## Target Customer
Payment operations and treasury leadership, CFOs, suppliers waiting for payment, and working capital and dynamic discounting vendors.

## Impact If Built
Payment runs were built as a batch operation, so timing became an operational convenience and nobody costed the difference. Discount capture alone frequently exceeds the software fee, and the optimisation's inputs are already in the system.
