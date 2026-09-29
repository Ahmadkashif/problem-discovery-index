# Disengagement Prediction on the Only Attendance Corpus That Exists

**Niche:** [[niches/gyms-independent/fitness-benefit-network-analytics/profile|Fitness Benefit Network Analytics]]
**Industry:** [[industries/gyms-independent|Independent Gyms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The network holds check-in histories for millions of members across thousands of facilities and reports them as monthly utilization rates.
**Tags:** #survival-analysis #logistic-regression #gradient-boosting #ml-time-series #evaluation-metrics #revenue-impact

## The Problem
The economics of a fitness benefit are entirely about who keeps going. A member who visits eight times a month justifies the fee the plan pays; one who visits twice in January and never returns does not, and the plan sees the same per-member cost either way. When the health plan reviews the programme, the question is always the same — is anyone actually using this — and the answer arrives as an aggregate participation percentage.

The network can see far more than that. It knows every check-in, at which facility, at what time of day, in what sequence. It knows the shape of the four weeks before someone stops: the visit interval lengthening, the routine shifting from mornings to sporadic evenings, one facility replaced by none. Pass 1 says independent gym owners discover attrition only when a card declines or someone simply stops showing up. The network has the same blindness at a thousand times the scale, and unlike the gym owner it has the data to fix it.

Nothing predicts. Reporting is monthly, backward-looking, and aggregated to the plan level, which is the one resolution at which an individual's disengagement is invisible.

## Why Nobody Has Built This
The reporting was built to answer the contract, and the contract asks for utilization rates. The analytics team's calendar is dominated by plan reporting cycles and renewal presentations, and every one of those is a descriptive question. Nobody has ever been asked for a prediction, so nobody built one.

There is also a structural distance from the intervention. The network does not own the member relationship — the plan does, and the gym does — so a prediction has historically had nowhere to go. That has changed: these networks now run their own member apps and communication channels, and the reason for not predicting has quietly expired without anyone noticing.

## What to Build
A member-level disengagement model on the check-in corpus, with the intervention path attached.

**Time-to-lapse as the target.** This is survival analysis, not a churn flag: the useful output is a hazard that rises weeks before the last visit, not a binary at the end. Visit interval, interval trend, time-of-day consistency, facility switching, class versus open-gym mix, and the first-90-day pattern are the features, and every one of them is already in the record.

**Early-tenure segmentation.** The first six weeks determine most of it. A member who establishes a twice-weekly rhythm in weeks two through four behaves differently from one whose visits are sporadic from the start, and separating those two populations early is worth more than any model refinement later.

**Facility effects, isolated.** Because the same member population is spread across thousands of facilities, the network can estimate what a facility contributes to retention independent of who walks in the door — something no individual gym can compute about itself, and no benchmark publisher can either. That is both an operational tool for network management and, credibly, a product.

**Intervention as an experiment.** Every outreach the network sends is a chance to learn what actually restarts attendance, and randomizing it costs nothing. Absent that, the model predicts and no one ever learns whether acting on it helps.

## Target Customer
VP of Analytics or Chief Data Officer at a fitness benefit network. The commercial logic is direct: the renewal conversation with a health plan turns on demonstrated engagement, and a network that can show it identified disengaging members and measurably brought some of them back is arguing from a different position than one presenting a participation percentage.

## Impact If Built
The plan gets the outcome it is paying for. The network gets a defensible renewal argument and a facility-quality signal it can act on. And the independent gyms in the network — which cannot afford this analysis and, per Pass 1, mostly do not attempt it — get the one thing that fixes 30-50% first-year attrition: a warning before the member is gone.
