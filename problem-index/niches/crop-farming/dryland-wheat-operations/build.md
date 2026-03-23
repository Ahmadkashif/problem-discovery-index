# Soil Moisture Profile-Based Planting Decision Model

**Niche:** [[niches/crop-farming/dryland-wheat-operations/profile|Dryland Wheat & Small Grain Operations]]
**Industry:** [[industries/crop-farming|Crop Farming]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product translates soil moisture probe data and weather forecasts into a field-specific plant/fallow recommendation with yield probability and economic analysis — dryland farmers make this $85-185/acre decision based on feel and experience developed over decades of probing soil with a shovel.
**Tags:** #gradient-boosting #gaussian-processes #tacit-knowledge-ml #revenue-impact

## The Problem
The single most consequential agronomic decision in dryland wheat farming is whether to plant or fallow each field in a given year. The decision depends on stored soil moisture (measured by depth of wet soil in the profile — experienced farmers probe 4-6 feet deep and assess moisture at each foot), precipitation forecast for the growing season (inherently uncertain), and the economic break-even point (minimum yield to cover input costs at current wheat prices). An experienced dryland farmer has decades of calibration: "In my experience, when I have 3 feet of wet profile and we get average spring rain, I yield 35-40 bushels — that's above break-even at current prices, so I plant." A beginning dryland farmer lacks this calibration and may plant into insufficient moisture (losing $100-200/acre in input costs on a failed crop) or fallow unnecessarily (forgoing $100-150/acre in revenue from a crop that would have succeeded).

## Why Nobody Has Built This
Dryland yield prediction from soil moisture requires region-specific models that correlate soil moisture profile (measured or estimated from rainfall/evapotranspiration calculations), soil type (water-holding capacity varies 2x between sandy and clay soils), and growing season weather with actual yield outcomes. This data exists scattered across USDA NRCS soil surveys, university extension trial data, and individual farmer records — but has never been assembled into a training dataset. Precision ag companies focus on irrigated corn/soybeans (higher revenue per acre, larger market) and have not invested in dryland-specific models.

## What to Build
A planting decision model that accepts: soil moisture probe readings (or estimates from rainfall/evapotranspiration calculations using USDA's Crop Water Stress model), soil type (from NRCS Web Soil Survey, auto-populated by field location), seasonal weather outlook (NOAA Climate Prediction Center, probabilistic forecast), and current wheat price/input costs. Outputs: expected yield probability distribution (25th/50th/75th percentile), economic analysis (probability of exceeding break-even), and a plant/fallow recommendation with confidence interval. Trained on university dryland research trial data and cooperating farmer records from the Great Plains.

## Target Customer
Dryland wheat farmers managing 1,000+ acres in the Great Plains (western Kansas, eastern Colorado, Oklahoma panhandle, Montana, Dakotas). Approximately 50,000-80,000 US dryland wheat operations. Average contract value: $2-5/acre/season.

## Impact If Built
Planting decisions improve by reducing both types of error: planting into insufficient moisture (input cost loss) and unnecessary fallowing (revenue forgone). At 3,000 acres, even a 5% improvement in plant/fallow decision accuracy represents $15,000-45,000 in annual economic impact. New dryland farmers achieve experienced-farmer-level decision quality within 2-3 seasons instead of 15-20 years.
