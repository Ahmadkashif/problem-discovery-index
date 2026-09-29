# Condition Models That Never Learn From the Claim That Followed

**Niche:** [[niches/home-inspection/property-condition-risk-data-providers/profile|Property Condition & Risk Data Providers]]
**Industry:** [[industries/home-inspection|Home Inspection]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The firm scores a roof from imagery, the insurer pays a claim on it three years later, and the two facts never meet.
**Tags:** #computer-vision #gradient-boosting #survival-analysis #evaluation-metrics #causal-inference #revenue-impact

## The Problem
These firms score the condition of tens of millions of properties — roof age and material, apparent wear, tree overhang, pool presence, envelope condition — from aerial imagery, permit records, and assembled attributes. An insurer uses the score to decide whether to write the policy and at what price.

Then something happens. The roof holds for fifteen years, or fails in a hailstorm four years later, or the property has a water loss unrelated to anything visible from the air. That outcome is recorded, by the carrier, in a claim.

The two records almost never meet. Condition scoring and claims experience are separate businesses inside the same industry, often inside the same company, and the feedback loop that would tell anyone whether a condition score predicts anything is not closed. Models are validated against labelled imagery — does the model agree with a human annotator about what the roof looks like — which measures perception, not prediction. Whether "fair" roofs actually generate more claims than "good" ones, and by how much, is asserted far more often than it is measured.

## Why Nobody Has Built This
The commercial structure separates them. Condition data is sold as a feed; claims data belongs to carriers and is fiercely protected. A vendor sells the same scores to twenty carriers and receives outcomes from none of them, so the natural place to close the loop is the one place with no incentive to.

Inside the larger firms that own both — property data and claims analytics under one roof — the separation persists for a different reason: the businesses were acquired, run on different platforms, serve different clients, and report to different leaders. Joining them is an organizational problem wearing a technical costume.

And validating against annotation is comfortable. It produces a clean accuracy number, it is fast, and nobody has to wait three years or negotiate for outcome data.

## What to Build
An outcome-linked validation and modelling layer for condition scoring.

**Assemble the linkage** — for whatever subset of the portfolio outcomes can be obtained. Carrier consortium arrangements, reinsurer relationships, and the firm's own claims businesses each provide a partial view; none needs to be complete for the model to improve enormously over annotation-only validation.

**Reframe the target as time to loss.** The commercially useful quantity is not what the roof looks like but the hazard of a claim of a given type within the policy period, and its distribution. That is survival modelling with censoring, weather exposure as a time-varying covariate, and condition observations as the features — and it is a fundamentally different model from the classifier currently in production.

**Separate condition from exposure.** A property in a hail corridor and a property in a mild climate with identical roofs have very different claim probabilities, and a score that blends condition with geography is useless for the underwriting question, which is what this particular roof adds beyond where it sits.

**Report calibrated probabilities.** A carrier pricing risk needs a number that means what it says. Ordinal condition grades — good, fair, poor — force every user to invent their own mapping to loss cost, which means twenty carriers are each guessing at the translation the vendor is best placed to provide.

## Target Customer
Chief Data Officer or SVP of Product at a property data and analytics provider. The argument is competitive and short: every vendor in this market claims accurate condition assessment, and the first one that can publish observed loss ratios by score band has ended the comparison.

## Impact If Built
Property insurance availability is a live crisis in several states, and it is driven substantially by carriers who cannot distinguish good risks from bad ones and therefore withdraw from whole markets. A condition score demonstrably tied to loss experience lets a carrier write business it currently declines. For the vendor, it converts a data feed — which competes on coverage and price — into a validated risk model, which does not.
