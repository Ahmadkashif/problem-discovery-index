# Computer Vision-Based Pest and Disease Detection for Greenhouses

**Niche:** [[niches/greenhouse-horticulture/ipm-scouting-automation/profile|IPM Scouting Automation]]
**Industry:** [[industries/greenhouse-horticulture|Greenhouse Horticulture]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No commercial product performs automated pest and disease identification from plant images in greenhouse environments — despite the task being fundamentally a visual classification problem that experienced scouts perform with their eyes at 60-80% accuracy for early-stage infestations.
**Tags:** #cnn #object-detection #computer-vision #tacit-knowledge-ml #revenue-impact

## The Problem
An experienced IPM scout identifies thrips damage by the silvery stippling pattern on leaf surfaces visible only at certain angles, distinguishes botrytis from mechanical damage by the fuzzy gray sporulation at wound margins, and spots a single whitefly adult on the underside of a leaf among thousands of plants. These identifications at the early stage — when intervention is most effective and least costly — require visual pattern recognition that takes 2-3 years of daily practice to develop. The scout simultaneously classifies the organism, assesses severity, maps the spatial distribution, and estimates population trend — a multi-task visual assessment. Greenhouse operations spending $100K-$300K/year on biological control agents need accurate early detection to deploy beneficial insects effectively; late detection means chemical intervention at 3-5x the cost with market-access consequences (retailers increasingly require "biological only" pest management).

## Why Nobody Has Built This
Three challenges: (1) the target organisms are small (thrips are 1-2mm, mites are 0.5mm) and require close-up imaging that fixed overhead cameras cannot provide — scouting-level detection requires scout-level proximity, (2) no large labeled dataset exists for greenhouse-specific pests at the cultivar level; PlantVillage covers field crops and iNaturalist covers macro-scale organisms, but neither has the greenhouse pest complex at diagnostic resolution, (3) the economic model is challenging — the scout is being paid $15-$20/hour to do the scouting already, so the CV system must either be dramatically cheaper (automated cameras) or dramatically better (catching what the scout misses).

## What to Build
A two-tier detection system: (1) zone-level monitoring using overhead cameras that detect canopy-level anomalies (color changes, growth suppression, visible damage patterns) and direct the scout's attention to priority areas, and (2) a smartphone-based leaf-level classifier that the scout uses during targeted scouting — photograph the suspect area, receive a classification with confidence score and severity assessment. The smartphone app generates training data with every use (scout confirms or corrects the classification), creating a growing dataset. Initial model covers the 10 most common greenhouse pests and 5 most common diseases, trained on 30,000-50,000 labeled images collected from 10+ partner greenhouses.

## Target Customer
IPM managers and head growers at commercial greenhouses spending $50K+/year on scouting labor and biological control. Approximately 3,000-5,000 US greenhouses at this scale. Price model: $200-$500/month per zone for camera monitoring, free smartphone app subsidized by biological control supplier partnerships.

## Impact If Built
Scouting efficiency improves 30-50% through zone-level priority direction — the scout spends time where problems are, not randomly sampling clean areas. Early detection rate for the top 5 pests improves from 60-70% (experienced scout alone) to 85-90% (scout + CV system), reducing the window for exponential pest population growth. Biological control efficacy improves 20-30% through more timely and spatially targeted deployment. Combined annual value of $30K-$100K per greenhouse in reduced pest damage and optimized biocontrol spending.
