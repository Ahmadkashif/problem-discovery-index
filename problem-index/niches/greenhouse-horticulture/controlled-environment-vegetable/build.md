# Crop Steering Decision Support from Plant Morphology Data

**Niche:** [[niches/greenhouse-horticulture/controlled-environment-vegetable/profile|Controlled-Environment Vegetable Production]]
**Industry:** [[industries/greenhouse-horticulture|Greenhouse Horticulture]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product captures plant morphology data (internode length, stem thickness, leaf area, truss load) and translates it into crop steering recommendations — the decision of whether to push the plant toward vegetative or generative growth is made entirely by the head grower's visual assessment.
**Tags:** #cnn #regression #computer-vision #tacit-knowledge-ml #revenue-impact

## The Problem
In greenhouse tomato production, the head grower's most critical daily decision is crop steering: should the plant invest energy in vegetative growth (more leaves, thicker stems, stronger root system) or generative growth (more flowers, larger fruit, faster ripening)? The answer depends on reading the plant's current balance — measured informally by internode length (longer = too vegetative), stem thickness below the growing point (thicker = vegetative, thinner = generative), leaf size and color (darker green = more nitrogen available = likely to go vegetative), and truss set success (poor set = plant is too generative). The grower adjusts this balance by manipulating the difference between day and night temperature (DIF strategy), irrigation frequency and EC (electrical conductivity), and pruning aggressiveness. Getting this wrong costs 10-20% of potential yield — $5-$10/sq meter annually on a 20-acre facility worth $15-$20M/year in revenue.

## Why Nobody Has Built This
Quantifying plant morphology at scale requires measuring characteristics (stem diameter, internode length, leaf area index) that are currently assessed visually by walking rows. Camera-based measurement is feasible but requires high-resolution imaging at plant level with standardized positioning — challenging in a dense canopy environment. The training data requires pairing morphology measurements with the grower's steering decisions and subsequent yield outcomes over multiple crop cycles. No dataset of this type exists; it must be created through instrumented growing trials. The crop steering decision itself is context-dependent — the right action varies by cultivar, season, crop age, and market timing.

## What to Build
A row-mounted camera system that captures weekly images of plant growing points, stems, and trusses from standardized positions. A CNN-based measurement model extracts internode length, stem diameter, leaf area, and fruit count from images. A gradient-boosted decision model trained on 2-3 seasons of data from 5+ facilities recommends steering adjustments: "Plant balance is trending vegetative — increase night temperature by 1°C and widen irrigation intervals to steer generative." The system learns facility-specific plant response patterns over time.

## Target Customer
Head growers and crop managers at CEA vegetable operations with 5+ acres of greenhouse or vertical farm production. Approximately 500-1,000 US facilities at this scale, with high per-facility value ($5K-$20K/year). Secondary: Dutch-style greenhouse consulting companies (e.g., Hortimax Advies, Delphy) as a value-added service.

## Impact If Built
Yield improvement of 5-10% through more precise crop steering, worth $750K-$2M annually on a 20-acre tomato greenhouse. Head grower's time on row walks reduced by 40-50%, redeployed to higher-value problem solving. Knowledge retention when the head grower leaves — the model captures the steering patterns that previously existed only in one person's experience.
