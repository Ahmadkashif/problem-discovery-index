# IPM Scouting Automation

**Parent Industry:** [[industries/greenhouse-horticulture|Greenhouse Horticulture]]
**Category:** Highly Automatable

## Profile
**Market Size:** $1-2B (embedded — IPM labor and biological control costs)
**Share of Parent Industry:** ~8% of operating costs
**Digital Adoption:** Low — scouting is done visually with paper or basic tablet forms; no commercial greenhouse uses automated pest/disease detection despite the task being fundamentally a pattern recognition problem
**Target Buyer:** IPM Manager / Head Grower responsible for pest and disease management
**Automation Potential:** High — pest and disease detection from visual cues is a classic computer vision task, with the training data challenge being the primary barrier to deployment

## What Makes This a Distinct Niche
IPM (Integrated Pest Management) scouting is the most labor-intensive and skill-dependent task in greenhouse crop protection. IPM scouts walk greenhouse ranges for 4-6 hours daily, inspecting plants at random sampling points for thrips, whitefly, spider mites, fungus gnats, aphids, and 10-15 disease organisms (botrytis, powdery mildew, downy mildew, pythium, fusarium). Detection of early-stage infestations — a single thrips on the underside of a leaf, the first powdery mildew spore circle on a petal — requires the same kind of tacit visual pattern recognition that takes 2-3 years to develop and degrades with fatigue. A missed detection delays treatment by 3-7 days, during which an exponentially reproducing pest population can spread from one bench to an entire zone. The current scouting paradigm is fundamentally a human-powered image classification system: the scout is a biological CNN scanning for anomalies across thousands of plants.

## Current Tools & Gaps
Scouting is recorded on paper maps or basic tablet apps (Bioline's ScoutPro, SciScout). Sticky trap monitoring provides population-level data for flying insects but does not identify location-specific infestations or immobile life stages. No commercial product performs automated pest or disease detection from plant images in greenhouse environments. Research prototypes exist (PlantDoc, iNaturalist-derived classifiers) but none are trained on the greenhouse-specific pest complex at the cultivar-level resolution needed for commercial deployment.

## Problems
- [[niches/greenhouse-horticulture/ipm-scouting-automation/build|🔨 Build: Computer Vision-Based Pest and Disease Detection for Greenhouses]]
- [[niches/greenhouse-horticulture/ipm-scouting-automation/buy|🛒 Buy: Scouting App with Structured Data Collection and Trend Analytics]]
- [[niches/greenhouse-horticulture/ipm-scouting-automation/fix|🔧 Fix: Sticky Trap Counting and Threshold Alert Automation]]
