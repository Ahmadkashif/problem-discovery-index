# SNAP Retailer Authorization & Integrity (USDA FNS)

**Parent Industry:** [[industries/grocery-stores|Grocery Stores]]
**Category:** Insight Layer
**Value-Chain Position:** Regulatory & enforcement bodies

## What They Do
USDA's Food and Nutrition Service authorises stores to accept SNAP, monitors their EBT transactions for trafficking, and investigates and sanctions them. Supermarkets and super stores together redeemed over 79% of about $125B of benefits in FY2021 while being 15% of authorized firms. FNS's super store class includes supercenters, which belong to the queued general merchandise retailers industry; supermarkets alone redeemed 27.0% ($33.9B) (USDA FNS). That year FNS ran 11,273 investigations and issued 1,595 permanent and 1,155 time-limited disqualifications (USDA FNS). It also processes the state SNAP restriction waivers that now change what each store may sell under SNAP.

## Insight Function
**Size:** ~20-60 data and integrity analysts running transaction monitoring and trafficking-case selection (estimate). The hundreds of investigators working one case at a time and authorisation specialists processing one store at a time are production and are not counted.
**Output:** Authorisations and reauthorisations, trafficking alerts from transaction analysis, investigations, sanctions, annual retailer reports
**Proprietary data:** Every EBT transaction at every authorized store, plus store applications, visit reports and investigation outcomes
**Clock:** The agency's own reauthorisation and investigation cycles
**Buyer:** Director of retailer operations at FNS

## Scorecard
| Criterion | Weight | Score |
|---|---|---|
| Q1 Insight is the invoice | ×3 | 1 |
| Q2 Labor mass + repeatable | ×2 | 3 |
| Q3 Proprietary data moat | ×3 | 5 |
| Q4 External clock | ×2 | 2 |
| Q5 Buyer + market | ×2 | 1 |
| **Weighted total** | | **30/60** |

**Kill switches:** **statutory confidentiality**, live. 7 U.S.C. 2018(c) requires regulations that "limit the use or disclosure" of information obtained from retail food stores to administering and enforcing the program, with criminal penalties for unauthorised disclosure. In *Food Marketing Institute v. Argus Leader Media* (US Supreme Court, No. 18-481, 24 June 2019, 6–3) the Court held store-level SNAP redemption data confidential under FOIA Exemption 4. Government procurement on its own would not be a switch.
**Verdict:** Logged — kill switch. The analytics team plausibly passes the gate at 10 or more, but this is one agency with no invoice, and the richest store-level dataset in grocery is fenced by statute. Q2 is 3 because transaction monitoring is largely automated and the analyst team does not grow with redemption volume.
