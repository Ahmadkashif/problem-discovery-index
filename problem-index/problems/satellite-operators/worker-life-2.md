# The Imagery Operations Analyst Screening Every Scene

**Industry:** [[satellite-operators|Satellite Operators]]
**Type:** Worker Life Changing
**One-liner:** At an earth-observation operator, analysts open scene after scene to check cloud cover, haze, geolocation and artefacts before imagery ships within the hours the customer was promised, and get back the shift when only the doubtful scenes reach them.
**Tags:** #semantic-segmentation #cnns #transfer-learning #evaluation-metrics #worker-facing #automation #quick-win

## The Problem
An earth-observation operator promises customers imagery of a site within hours of collection: a defence agency watching an airfield, an insurer checking flood extent, a commodity analyst counting oil tanks, a utility checking vegetation along a line. Every collected scene goes through processing — radiometric correction, orthorectification, pan-sharpening or, for radar, focusing — and then through a human check. The imagery operations analyst opens the scene and asks: is the target actually visible, or under cloud, haze or smoke? Did the orthorectification put the image where it belongs, or is it offset by tens of metres over mountainous terrain? Are there stripes, saturation or compression artefacts? For radar, are there ambiguities or interference streaks? If the scene fails, the analyst decides whether to re-task the satellite, deliver with a caveat, or substitute an archive image.

The checks are repetitive and time-boxed. Analysts on a shift review hundreds of scenes (estimate), most of which are fine. Cloud masks from the processing chain are useful but miss thin cirrus and confuse snow, salt flats and bright roofs for cloud. Customers judge the operator on how often a delivered image is unusable and how often an order was missed for a cloud the analyst should have caught before the satellite's next pass.

## Why It Matters to the Worker
The analyst is paid to judge imagery but spends most of the shift confirming that clean scenes are clean. The hard calls — partial cloud over the exact target, a subtle geolocation error, an artefact that might be an object — get the same few seconds as the easy ones. Errors are visible and personal: a customer complaint about an unusable image traces back to whoever passed it. Shifts follow the satellites' passes and the customers' time zones, so the work runs nights and weekends.

## What a Solution Looks Like
A quality model that segments every scene for cloud, haze, shadow, snow and artefacts at target level rather than scene level, checks geolocation against reference imagery and terrain, scores each delivery against the customer's own acceptance criteria, and passes clearly good and clearly bad scenes automatically. The analyst sees only the doubtful scenes, with the model's reasons highlighted, and their decisions become training data. Re-tasking recommendations are generated for failed collections with the next feasible pass and its forecast cloud cover.

## Impact If Solved
Taking the clearly good and clearly bad scenes off the analyst's screen cuts the review load by most of its volume (estimate), moves attention to the scenes where judgement matters, shortens delivery times, and reduces the unusable-image complaints that land on the analyst's name.
