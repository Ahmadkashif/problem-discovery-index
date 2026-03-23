# Rate Transparency Tool for Infrequent Shippers

**Niche:** [[niches/freight-brokerage/small-shipper-spot-market/profile|Small Shipper Spot Market Participants]]
**Industry:** [[industries/freight-brokerage|Freight Brokerage]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** DAT and FreightWaves publish market rate data, but it's designed for brokers and carriers — small shippers can't interpret spot rate averages, don't know what a fair all-in rate includes, and have no benchmark to evaluate the quotes they receive from their broker.
**Tags:** #gradient-boosting #large-language-models #revenue-impact #quick-win

## The Problem
When a small shipper receives a freight quote of $2,800 for a Chicago-to-Atlanta dry van load, they have no way to know if that's fair. DAT's spot rate data shows a range of $1.80-$2.40/mile, but the shipper doesn't know how to convert that to an all-in rate (factoring in fuel surcharge, linehaul, accessorials), doesn't know what equipment type they need, and doesn't understand that the rate varies by day of week and lead time. The information asymmetry between broker and small shipper is the primary source of margin extraction from this segment.

## What Already Exists
DAT RateView and Greenscreens.ai provide rate benchmarking, but the interface assumes freight industry knowledge. Google-searchable freight rate calculators provide rough estimates but lack accuracy for specific lanes and dates. No tool translates market rate data into a simple "is this quote fair?" answer for a non-expert shipper.

## The Customization Gap
A small-shipper rate transparency tool needs: (1) a simplified input (origin, destination, what you're shipping, when) without requiring freight class or equipment type knowledge; (2) automatic equipment and freight class determination from the product description; (3) a "fair rate range" output in plain language ($2,400-$2,900 for this shipment, based on current market conditions); (4) comparison scoring for quotes received ("this quote is 12% above market average — here's why that might be justified or not"). The translation from industry data to shipper-friendly intelligence is the gap.

## Target Customer
Small business owners and shipping clerks who don't have freight industry expertise but need to evaluate whether their broker's quotes are reasonable.

## Impact If Solved
Small shippers armed with rate transparency save 5-15% on freight spend by identifying and negotiating overpriced quotes. On a $100K annual freight budget, that's $5K-$15K in savings — meaningful for a small business.
