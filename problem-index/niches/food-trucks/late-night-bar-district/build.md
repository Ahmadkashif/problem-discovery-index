# Bar District Demand Surge Prediction

**Niche:** [[niches/food-trucks/late-night-bar-district/profile|Late-Night Bar District Trucks]]
**Industry:** [[industries/food-trucks|Food Trucks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product predicts the 1 AM rush intensity for late-night food trucks — operators prep blind for a crowd that could be 50 or 500 depending on which bars had events, whether Uber surge pricing is keeping people in the area, and whether it is raining.
**Tags:** #gradient-boosting #time-series-forecasting #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
Late-night demand is feast-or-famine: a Friday with a big concert at the nearby venue plus good weather generates a 500-person rush at 1 AM, while the same Friday with rain and no events produces 50 customers. Experienced late-night operators develop an intuition about which nights will be big — they track venue event calendars, watch weather forecasts, and know which holidays bring bar crowds — but this knowledge is unstructured and takes 1-2 years of late nights to develop. New operators either over-prep (wasting food they cannot store) or under-prep (missing the best revenue night of the month).

## Why Nobody Has Built This
Late-night food truck data is sparse: operators are the least digitized segment of the industry, cash transactions go unrecorded, and there are far fewer late-night trucks than daytime operators to form a training set. The demand signal (bar foot traffic at midnight) is not captured by standard foot traffic providers, which focus on business hours. Venue event data is fragmented across dozens of bar websites, Facebook events, and Eventbrite pages with no aggregated API.

## What to Build
A demand prediction engine for late-night operators that scrapes venue event calendars (bar events, concerts, sports watch parties), ingests weather forecasts and day-of-week patterns, and correlates with the truck's own POS history to predict tonight's rush intensity on a 1-5 scale. The operator gets a morning alert: "Tonight looks like a 4/5 — prep for 350+ customers" or "Slow night ahead — consider skipping or reducing prep by 40%."

## Target Customer
Late-night operators serving 4-6 nights/week who currently prep the same quantity regardless of expected demand, losing $4K-$10K annually to waste and missed revenue.

## Impact If Built
Right-sizing prep to demand intensity reduces waste 30-40% and ensures adequate stock on big nights, adding $6K-$12K in annual profit for a typical late-night operator.
