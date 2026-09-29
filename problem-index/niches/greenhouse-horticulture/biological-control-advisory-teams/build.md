# A Private Pest Surveillance Network Used to Write One Greenhouse at a Time

**Niche:** [[niches/greenhouse-horticulture/biological-control-advisory-teams/profile|Biological Control Field Advisory Teams]]
**Industry:** [[industries/greenhouse-horticulture|Greenhouse Horticulture]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Advisors observe pest pressure in thousands of greenhouses every week across every producing region, and the observations are used to write individual release programmes and nothing else.
**Tags:** #time-series-forecasting #gradient-boosting #change-point-detection #evaluation-metrics #causal-inference

## The Problem
A field advisor walks a customer's greenhouse, counts thrips on sticky cards, checks whether the predatory mites established, and adjusts the release programme for the coming weeks. Across a major supplier that happens in thousands of houses, weekly, in every greenhouse region on the continent.

The result is a real-time, geographically dense, species-resolved picture of pest pressure — a surveillance network no government agency operates and no competitor can replicate, run incidentally by a company that sells insects.

It is consumed one greenhouse at a time. The advisor uses this week's counts to adjust this grower's programme. Nothing aggregates the counts into a regional pressure signal, nothing forecasts where pressure is heading, and nothing warns a grower two counties away that the same pest is building.

That is a large miss, because pest population dynamics are the most forecastable thing in the business. Thrips and whitefly populations grow on temperature-driven schedules; a count today implies a population in ten days with real precision. Biological control has a structural weakness against chemistry — it works if deployed early and fails if deployed late — so the value of a forecast is unusually high, and the party best placed to produce one is producing none.

The second miss is outcome measurement. A release programme is a prescription: this species, this rate, this interval. Whether it worked is observed at the next visit and recorded as the basis for the next adjustment, never as a scored result. Nobody can say which programmes establish reliably, in which crops, at which pressure levels — which is the entire scientific question the company exists to answer.

## Why Nobody Has Built This
Revenue is in the insects. The advisory workforce is a cost of selling them, so investment goes to production capacity and species range, not to analytics whose output would be given away with the advice.

The observations are also captured as they are used — a note in a visit record — which makes them fine for the next conversation and useless for aggregation. That is the same barrier the industry has everywhere: the data is a by-product of a workflow that had no reason to standardise it.

And there is a competitive hesitation about regional signals. A supplier publishing a regional pressure warning is telling customers something that also helps non-customers, and possibly telling a chemical competitor where the pressure is.

## What to Build
The surveillance network as a forecasting product, and the release programme as a measured prescription.

**Standardise the count.** Species, life stage, count per card, card position, crop and growth stage, on a scale that means the same thing in every region. Nothing else is possible until this exists.

**Forecast population trajectory per house.** Degree-day driven growth against observed counts is a well-understood dynamic, and the advisor's real question — will this be an outbreak in ten days — becomes answerable rather than intuitive.

**Aggregate to regional pressure.** Pressure by species, crop and week across a region is a genuine product for growers, and an early-warning service is a defensible reason to buy from the supplier who has the network.

**Score establishment.** Did the released beneficial establish, at what rate, under what conditions. This is the company's own scientific claim and it is currently supported by trials rather than by the thousands of commercial releases it performs weekly.

**Model programme failure.** Biological programmes fail for identifiable reasons — released late, pesticide residue, temperature, humidity, wrong species for the pest stage. Those causes are observable in the visit record and are diagnosed case by case.

## Target Customer
Technical Director or Head of Crop Advisory at a beneficial-insect supplier. The commercial argument is direct: the insects are close to interchangeable and the advice is the moat, so the advice needs to be demonstrably better than a competitor's.

## Impact If Built
Biological control's competitive weakness against chemistry is timing — it must be deployed before pressure builds. The company holding the only continent-scale pest surveillance network is the one that could turn timing from a judgment into a forecast, and it currently uses the network to fill in a visit report.
