# A Last and Fit Feedback Loop From Wear Tests

**Niche:** [[niches/specialty-design-studios/footwear-and-leather-goods-design/profile|Footwear & Leather Goods Design]]
**Industry:** [[industries/specialty-design-studios|Specialty Design Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An experienced footwear developer can handle a last and predict where a shoe will rub or slip, and that judgement is never paired with the wear-test and returns data that would show whether they were right.
**Tags:** #tacit-knowledge-ml #gradient-boosting #k-nearest-neighbors #feature-engineering #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to get a shoe or bag from sketch to a confirmed last, pattern and wearable sample in the fewest factory rounds, and whoever controls the last and the fit across the size run takes the account.

## The Problem
Fit failures in footwear — heel slip, toe-box pressure, instep tightness — are usually found in wear tests or, worse, in returns. The developer who chose or modified the last had a view about these risks, but it was expressed in a conversation with the factory, not recorded against the last's measurements, and the wear-test notes live in a separate file.

## Why Nobody Has Built This
Last data is physical and held by factories and last-makers; wear-test panels are small and informal at independent studios; returns data sits with brands and retailers.

## What to Build
A record linking each style's last (scanned or measured: ball girth, instep, heel width, toe spring), its pattern, the developer's predicted fit risks, wear-test comments by foot measurement, and post-launch fit returns. Nearest-neighbour retrieval surfaces past lasts with similar measurements and their outcomes; a model predicts fit-complaint risk by region before the first sample is made.

## Target Customer
Heads of footwear development at brands and independent footwear studios developing 50+ styles a year.

## Impact If Built
Fewer fit rounds and fit returns, and a last library whose performance is known rather than remembered.
