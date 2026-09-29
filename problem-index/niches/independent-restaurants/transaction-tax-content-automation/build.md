# Product Classification Is the Whole Product and Is Done by Hand

**Niche:** [[niches/independent-restaurants/transaction-tax-content-automation/profile|Transaction Tax Content & Determination]]
**Industry:** [[industries/independent-restaurants|Independent Restaurants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Whether a bagel is taxable depends on whether it was sliced, and every product a customer sells has to be put in a category by a person.
**Tags:** #text-classification #large-language-models #word-embeddings #graph-ml #evaluation-metrics

## The Problem
Tax determination has two halves. The first is knowing the rules — this jurisdiction taxes prepared food at this rate with these exceptions — and the company maintains that corpus superbly. The second is deciding which rule applies to the thing being sold, and that is the half that breaks.

A customer onboards with tens of thousands of SKUs described in their own words: "BFST SNDWCH EGG CHZ", "PARTY TRAY LG", "SODA 20OZ FTN". Each has to be mapped to a taxability category, and prepared food is the worst category in the system — taxability can turn on temperature, on whether utensils were provided, on seating, on slicing, on whether the item is sold by weight, and the distinction differs by state and sometimes by city.

Mapping is done by implementation consultants and customer staff working through spreadsheets. It is the slowest part of every onboarding, it is where the errors are, and an error is a wrong tax collected on every transaction until someone notices — usually at audit, years later.

## Why Nobody Has Built This
The company's identity is the rules corpus. Decades of investment, organizational structure, and competitive positioning are built around having the most accurate and current tax content, and classification is treated as an implementation service rather than as a product surface. It shows up in professional services revenue, not in the content roadmap.

The customer is also nominally responsible. Contracts place classification accuracy with the taxpayer, which is legally sound and operationally useless — the customer is a restaurant group that knows less about prepared food taxability than anyone in the building.

And the outcomes are invisible. A misclassification produces a wrong tax that nobody detects until an audit, and audit results come back to the customer, not to the vendor. So the classification error rate is unmeasured and unmeasurable in the current arrangement.

## What to Build
Treat classification as a first-class prediction problem over the corpus the company already owns.

**Learn from the mapping history.** Millions of product descriptions have already been mapped to taxability categories across the customer base. That is a labelled dataset of exactly the right shape, and it is sitting in customer configurations.

**Classify from the description, with confidence.** Short, abbreviated retail product strings are a well-understood text problem, and the taxonomy is fixed and known. Output a category with a calibrated confidence so that high-confidence mappings auto-apply and the rest route to review — which turns weeks of onboarding into hours plus a short exception list.

**Ask the discriminating question, not all of them.** Prepared food taxability often hinges on one attribute — heated or not, utensils or not, sold by weight or by unit. When classification is uncertain, the system should ask the one question that resolves it rather than presenting the customer with a taxonomy.

**Detect drift in live configurations.** New products get added by customers continuously and mapped by whoever is fastest. Items whose classification looks inconsistent with similar items across the customer base are checkable, and flagging them is the only mechanism that would ever surface an error before an audit.

**Close the loop where audits are visible.** Where the company supports a customer through an audit, the findings are ground truth about its own classification quality — currently handled as a service engagement and never fed back.

## Target Customer
VP of Tax Content or Chief Product Officer. The commercial argument is onboarding: implementation time is the largest friction in the sales cycle and the largest professional services cost, and classification is most of it.

## Impact If Built
Restaurants and retailers collect the tax this system computes, on every transaction, in real time. Misclassification means over-collecting from consumers or under-collecting and carrying a liability that compounds until audit. Making the mapping accurate and measurable improves the correctness of a very large volume of everyday commerce, and it removes the single biggest obstacle to getting a new customer live.
