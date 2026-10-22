# Look Consistency Scored Across Sets and Seasons

**Niche:** [[niches/commercial-photographers/on-model-lifestyle-ecommerce/profile|On-Model & Lifestyle Ecommerce Content]]
**Industry:** [[industries/commercial-photographers|Commercial Photographers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A brand's creative director rejects images that "don't feel like us" by scrolling contact sheets, and no system can say which set, photographer or retoucher drifted.
**Tags:** #tacit-knowledge-ml #contrastive-learning #cnns #transfer-learning #evaluation-metrics #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to keep a brand's look identical across thousands of SKUs, models, sets and seasons while every model's usage terms stay inside their contracts, and whoever holds the look without overrunning talent usage takes the account.

## The Problem
Look consistency is the brand's most valuable visual asset and its least measured. Crop heights drift between sets, one photographer's light is a touch harder, a retoucher smooths skin more than the guide allows, a new model's poses don't match the vocabulary. The creative director catches it by eye, late, and the rejected looks are reshot with the samples already back in the warehouse.

## Why Nobody Has Built This
Consistency is partly measurable (crop, framing, colour, contrast) and partly the creative director's taste, and that taste has never been labelled. Brands treat their style as proprietary and don't share it. Studio software measures throughput, not look.

## What to Build
An embedding model fine-tuned on the brand's approved and rejected images, learning the creative director's judgement of "on brand" from their past decisions, combined with measurable checks (crop line, head position, colour statistics, retouch intensity). It scores every new image against the brand's look as it's captured, attributes drift to set, photographer or retoucher, and shows the nearest approved references.

## Target Customer
Heads of creative production at apparel, footwear and beauty brands that run multi-set seasons, and the studios competing for their business.

## Impact If Built
Drift is caught on set rather than in review, reshoots for "off-brand" fall, and the creative director's eye scales to every set at once and stays with the brand after they leave.
