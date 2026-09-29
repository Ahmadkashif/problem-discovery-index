# Inventory Forecasting and Yield Under Dynamic Insertion

**Industry:** [[audio-adtech-networks|Audio Adtech Networks]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Dynamic insertion turned a fixed slot into a perishable, back-catalogue-heavy inventory, and most publishers forecast it with a spreadsheet trend on last month's downloads.
**Tags:** #time-series-forecasting #exponential-smoothing #gradient-boosting #convex-optimization #confidence-intervals #evaluation-metrics #revenue-impact #recurrent-forecasting

## The Problem
Dynamic ad insertion decoupled the advertisement from the episode. A slot in an episode published two years ago can be filled today, which means a publisher's sellable inventory is the sum of expected future downloads across their entire back catalogue, at several positions per episode, segmented by geography and any targeting sold.

Forecasting that is harder than it looks. New episodes decay on a curve that varies by show and format; back catalogue produces a long persistent tail that occasionally spikes when a guest becomes newsworthy or an episode is recommended; seasonality is strong and show-specific; and a single successful episode can change a show's baseline permanently. On top sits the allocation problem: a sold campaign with a targeting requirement competes for the same impressions as a broad one, and overselling a targeted segment means under-delivery discovered at the end of the flight.

Most publishers run this in a spreadsheet with a growth assumption. The consequences are make-goods, unsold inventory that expires unnoticed, and campaigns that deliver against the wrong audience because the targeted supply was not there.

## What Already Exists
Megaphone, Art19, AdsWizz, Acast and Triton all provide inventory forecasting and delivery management inside their serving platforms, with varying sophistication. Programmatic marketplaces apply their own pacing. Larger networks have in-house yield teams with bespoke models. General-purpose ad server forecasting from the display world exists and transfers poorly, because the back-catalogue structure and the download decay curve have no display equivalent.

## The Customisation Gap
The platform forecasts are generic across a diverse publisher base, and the structure that matters is show-specific. A daily news podcast, a weekly interview show and an evergreen narrative series have entirely different decay curves, back-catalogue behaviour and seasonality, and a single model fitted across all of them is wrong for each in a different direction.

Forecast uncertainty is the missing output. A yield decision — whether to sell this inventory forward at a fixed rate or hold it for the spot market — is a decision under uncertainty, and a point forecast makes it impossible to reason about. Publishers routinely oversell because the forecast said a number and nothing said how confident it was.

The allocation layer needs the same treatment. Fulfilling a set of campaigns with overlapping targeting requirements from a stochastic supply is a constrained optimisation with a well-understood shape, and it is done by hand at most publishers. The specific failure — selling a scarce targeted segment to a low-value broad campaign that would have been happy with anything — happens continuously and silently.

And the host-read inventory needs modelling separately, because it is a different product: fixed to an episode, not dynamically replaceable, and worth more.

## Impact If Solved
Forecast error in this channel manifests as make-goods, expired unsold inventory and mis-delivered campaigns, all of which come straight out of publisher margin on a business with thin margins. Show-specific forecasts with honest intervals plus a proper allocation layer address a large recurring revenue leak, and the yield decision — sell forward or hold — is one a publisher currently makes with no quantitative basis at all.
