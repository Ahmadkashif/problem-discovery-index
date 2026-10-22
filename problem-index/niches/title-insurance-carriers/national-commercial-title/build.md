# Exception and Endorsement Risk for Large Commercial Deals

**Niche:** [[niches/title-insurance-carriers/national-commercial-title/profile|National Commercial & High-Liability Title]]
**Industry:** [[industries/title-insurance-carriers|Title Insurance Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Commercial underwriters decide under deal pressure which exceptions to delete and which endorsements to give on a nine-figure policy, with no evidence of which concessions have ever produced claims.
**Tags:** #gradient-boosting #survival-analysis #large-language-models #transformers #bayesian-inference #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to commit large single-risk title capacity on a multi-state commercial deal, directly or through co-insurance and facultative reinsurance, on pro forma terms lender's counsel accepts before signing, and whoever commits the most capacity soonest while keeping the exceptions it needs takes the account.

## The Problem
On a large commercial deal, lender's counsel push to delete survey exceptions, add zoning, contiguity, access and same-as-survey endorsements, and insure over encroachments the survey shows. Each concession widens coverage. The commercial underwriter decides on the strength of the survey, the zoning report and experience, against a signing date and a competing underwriter ready to say yes. Commercial claims are rare, large and slow. No underwriter has a model linking the concessions it made to the claims that followed.

## Why Nobody Has Built This
Commercial claims are too few for any single underwriter to model naively. Pro formas are negotiated as redlined documents rather than structured data. And the underwriters see the work as relationship business that analytics cannot help.

## What to Build
Parse every issued commercial policy and pro forma into structured exceptions deleted, endorsements given and affirmative coverages, joined to survey findings, property type, jurisdiction, liability and later claims. Fit hierarchical Bayesian claim-emergence models that borrow strength across property types and states. At decision time, show the underwriter the expected loss contribution of each requested concession and the capacity the deal can carry before co-insurance.

## Target Customer
Presidents and chief underwriters of national commercial divisions at the four families, and regional underwriters competing for the mid-market.

## Impact If Built
The underwriter commits capacity faster on the concessions that do not drive losses and holds firm, with evidence, on the ones that do. In a contest won on speed and terms, that is the margin.
