# A Decade of Swapping the Product Image

**Niche:** [[niches/programmatic-ad-platforms/creative-decisioning/profile|Creative Decisioning]]
**Industry:** [[industries/programmatic-ad-platforms|Programmatic Ad Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Dynamic creative optimisation has existed for a decade and still mostly swaps a product image and a headline, because the systems that assemble the ad know nothing about why a creative works.
**Tags:** #transformers #diffusion-models #large-language-models #contrastive-learning #causal-inference #evaluation-metrics #revenue-impact #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to build a system that knows why a creative works rather than which variant won — and whoever does that turns the largest untouched lever in the category into an optimisable one.

## The Problem
The optimisation system knows that variant seven outperformed variant three. It does not know that variant seven showed a person using the product while variant three showed the product alone, that its headline made a concrete claim rather than an abstract one, or that its dominant colour contrasted with the pages it ran on. So when the next campaign starts, nothing transfers — the system begins from scratch, permutes slots again, and rediscovers by brute force what it could have known. Creative is generally accepted as the largest single driver of effectiveness, and it is the only major component the industry treats as an opaque blob with an identifier.

## Why Nobody Has Built This
Creative is owned by agencies and brand teams and treated as a craft that resists measurement, which keeps it outside the optimisation stack by convention rather than by necessity. Representing a creative's content required multimodal understanding that was not practical until recently. Variant testing produced acceptable incremental gains and absorbed the available effort. And brand teams resist a system that appears to tell them what to make.

## What to Build
Represent the creative, then reason about it. Extract structured attributes from every asset — objects, people, setting, composition, colour, motion, pacing, message type, claim structure, call to action, brand presence and timing — which is the foundation and is now straightforward with multimodal models; everything else in this niche depends on it. Model performance as a function of those attributes rather than of a variant identifier, which is what makes learning transfer across campaigns, advertisers and categories and is the entire difference from the current approach. Account for the confound properly, since creative, audience, placement and timing move together and naive attribute attribution produces confident nonsense — this is where the work actually is. Match creative to context, because the fit between a specific advertisement and a specific page is the real decision and the stack currently makes it as two independent ones. Generate variants against attribute hypotheses rather than permuting slots, which is now practical and turns testing into something that learns. Detect fatigue at the attribute level, which is the fix note's subject. Respect brand constraints as hard rules, since a system that produces off-brand output will be switched off after one incident regardless of its performance. Tell the creative team what is working in terms they use — this message type, this composition, this framing — because an insight expressed as a variant number is unusable to the people who make the work. Pool learning across advertisers with appropriate abstraction, which is the platform's unique asset here. And evaluate against a variant-testing baseline on transfer to new campaigns, since that is the claim being made.

## Target Customer
Demand-side platforms, creative optimisation vendors, agency creative and strategy teams, and advertisers whose creative decisions are made without evidence.

## Impact If Built
The system knows variant seven won and not that it showed a person using the product, so nothing transfers and every campaign restarts from brute force. Modelling performance against extracted attributes is what makes learning transfer, and handling the confound is what separates it from confident nonsense.
