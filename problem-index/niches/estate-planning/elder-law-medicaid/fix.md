# Look-Back Period Transfer Tracking

**Niche:** [[niches/estate-planning/elder-law-medicaid/profile|Elder Law & Medicaid Planning]]
**Industry:** [[industries/estate-planning|Estate Planning]]
**Type:** Fix (Pain Point)
**One-liner:** Elder law attorneys stop discovering undisclosed transfers during the Medicaid application process — when it's too late to fix them — and instead track all client transfers from the start of the attorney-client relationship.
**Tags:** #logistic-regression #feature-engineering #evaluation-metrics #compliance #data-integration #automation

## The Problem
Medicaid imposes a 5-year look-back period: any transfers made for less than fair market value during the 60 months before a Medicaid application create a penalty period during which the applicant is ineligible for Medicaid benefits. Families frequently make transfers they don't realize are problematic — gifting $15K to a grandchild, adding a child to a bank account, paying a child's mortgage, transferring a car. These transfers surface during the Medicaid application process when the state agency reviews 5 years of financial records, often creating unexpected penalty periods of 3-12 months during which the family must pay $8,000-$15,000/month for nursing home care out of pocket. Attorneys discover these transfers retroactively, after the damage is done.

## Why It's Still Broken
There is no tool that helps elder law attorneys proactively track a client's financial transfers during the look-back period. Bank statements are reviewed manually — the attorney or paralegal pages through 60 months of statements (often from multiple financial institutions) looking for transfers that might trigger penalties. Clients forget transfers, minimize them, or don't understand what counts as a "transfer for less than fair market value." The information asymmetry between what the client discloses and what the state Medicaid agency will discover in financial records is the primary source of application denials and penalty periods.

## What a Fix Looks Like
A transfer tracking tool that connects to client financial accounts (via Plaid or bank statement upload/OCR) and flags transactions that could constitute Medicaid-penalizable transfers: gifts, payments to family members, account ownership changes, property transfers, and below-market-value sales. The system maintains a running penalty calculation: "Based on transfers identified so far, your client would face a 4.3-month penalty period. The look-back window closes on [date]." Attorneys see a dashboard for each client showing: total identified transfers, estimated penalty exposure, and the date the look-back period expires. The system also flags transactions that need attorney review to determine if they qualify for an exception (transfers to a spouse, transfers to a disabled child, transfers of a home to a caretaker child).

## Who Feels the Pain
Elder law attorneys who handle Medicaid applications and regularly encounter undisclosed transfers that derail applications. Paralegals who spend 4-8 hours per case reviewing 60 months of bank statements from multiple institutions. Families who face unexpected penalty periods and must find $50K-$150K for private-pay nursing home care while waiting out the penalty.

## Impact If Fixed
Reduces bank statement review time from 4-8 hours to 30-60 minutes per case. Prevents surprise penalty periods by identifying problematic transfers early enough to develop mitigation strategies (cure transfers, undue hardship exceptions, caregiver agreement documentation). Saves families an average of $30K-$100K per avoided penalty period.
