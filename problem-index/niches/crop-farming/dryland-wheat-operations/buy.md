# Dryland-Adapted Yield Prediction from Soil Moisture and Weather

**Niche:** [[niches/crop-farming/dryland-wheat-operations/profile|Dryland Wheat & Small Grain Operations]]
**Industry:** [[industries/crop-farming|Crop Farming]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** In-season yield prediction models (Climate FieldView, Gro Intelligence) use NDVI and weather data calibrated for irrigated row crops — they significantly overestimate dryland wheat yields because they do not account for the stored-moisture-dependent yield ceiling that dominates dryland production.
**Tags:** #gradient-boosting #time-series-forecasting #data-integration

## The Problem
Dryland wheat yield is primarily determined by stored soil moisture at planting plus growing-season precipitation — a fundamentally different yield model than irrigated crops where yield is primarily determined by heat units, nutrient availability, and pest management. Existing yield prediction platforms use satellite NDVI as a primary predictor, which works well for irrigated corn (canopy greenness correlates with yield when water is not limiting) but poorly for dryland wheat (a green canopy in April may still fail if June precipitation does not materialize). Dryland farmers need yield predictions that weight soil moisture and precipitation probability appropriately rather than relying on vegetation indices calibrated for irrigated conditions.

## What Already Exists
Climate FieldView, Gro Intelligence, and USDA/NASS provide yield forecasts at county and field level. These models are trained primarily on Corn Belt data and perform poorly in the Great Plains dryland environment. University extension (Kansas State, Montana State, North Dakota State) publishes dryland yield estimation guidelines but not real-time prediction tools.

## The Customization Gap
A dryland yield prediction model must incorporate: stored soil moisture at planting (the primary yield determinant — accounts for 40-60% of yield variation in dryland wheat), growing-season precipitation accumulation versus historical distribution, crop water use calculated from temperature and humidity (evapotranspiration), soil water-holding capacity (which determines how much stored moisture translates to available water), and variety-specific water use efficiency. The model must provide uncertainty estimates that reflect the high variance inherent in dryland production — a point prediction of "40 bushels" is less useful than "25-55 bushels with 50th percentile at 40."

## Target Customer
Dryland wheat farmers and their crop insurance agents (yield predictions inform insurance decisions). Approximately 50,000-80,000 US dryland operations.

## Impact If Solved
Grain marketing decisions improve — farmers forward-contract based on realistic yield expectations rather than hoping for above-average yields. Crop insurance purchasing becomes more informed — farmers can evaluate whether yield protection levels are appropriate given soil moisture at enrollment. Input investment decisions improve — if predicted yield is below break-even, the farmer can reduce late-season inputs rather than investing in a crop that will not be profitable.
