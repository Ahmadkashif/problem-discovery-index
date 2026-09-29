# App Marketing Firms

## Profile
**Category:** Adtech & Martech
**Market Size:** ~$90B global mobile app install and re-engagement spend; the agency, consultancy and in-house UA function managing it accounts for several billion in fees and salaries
**Tech Maturity:** Highly quantitative and structurally blindfolded. User acquisition teams run some of the most sophisticated lifetime-value modelling in marketing, and since Apple's App Tracking Transparency and SKAdNetwork they do it on attribution that arrives aggregated, delayed, sometimes suppressed entirely, and encoded in a handful of bits the marketer has to design themselves.
**Workforce:** User acquisition managers and media buyers, mobile measurement and data analysts, creative producers and motion designers, app store optimisation specialists, monetisation and product analysts

## Key Pain Themes
The economics of the job are a payback question: pay to acquire a user today, recover it over months. That requires predicting a user's six-month value from their first few days, which was hard when user-level data existed and is much harder now. On iOS the signal returns as a SKAdNetwork postback with a coarse conversion value, a randomised delay, and a privacy threshold that nulls the campaign identifier entirely when volume is low — which is precisely where a new campaign starts.

The conversion value itself is a design problem handed to the marketer. A small number of bits must encode whatever the team most needs to know about an early user, and the choice — revenue bucket, event sequence, retention proxy — determines what every downstream model can ever learn. Most teams picked a schema at launch and have not revisited it.

Around this sits the creative treadmill. Playable and video ads fatigue in days, networks consume dozens of variants per week, and under aggregated attribution nobody can cleanly say which creative earned. And every network self-attributes, so the same install is claimed by several, while the MMP applies its own rules and finance reports something different again.

## Current Tech Landscape
AppsFlyer, Adjust, Singular, Branch and Kochava provide measurement and SKAN aggregation. Networks — AppLovin, Moloco, Unity, Liftoff, ironSource, Meta and Google — bid on their own models and disclose little. Apple's AdAttributionKit succeeds SKAdNetwork with a similar shape; Google's Privacy Sandbox on Android is still settling, and Android retains more user-level signal for now. App store optimisation runs on AppTweak, Sensor Tower, data.ai and SplitMetrics, with custom product pages and store experiments as the levers. Incrementality testing exists through geo splits and public service announcement campaigns and is used by a minority.

## Problems
- [[problems/app-marketing-firms/high-impact|🔴 High Impact: Bidding a Six-Month Payback on Three Days of a Coarse, Delayed Signal]]
- [[problems/app-marketing-firms/low-impact-1|🟡 Low Impact: Creative Production and Testing on the Treadmill]]
- [[problems/app-marketing-firms/low-impact-2|🟡 Low Impact: App Store Listing Optimisation]]
- [[problems/app-marketing-firms/worker-life-1|🟢 Worker Life: The UA Manager With Four Sets of Numbers]]
- [[problems/app-marketing-firms/worker-life-2|🟢 Worker Life: The Creative Producer Shipping Fifty Variants a Week]]
- [[problems/app-marketing-firms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/app-marketing-firms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
This is the one corner of marketing where the measurement constraint was imposed deliberately by a platform owner rather than emerging from neglect, and the response has been genuinely inventive — conversion value schemas, predictive lifetime value from the first hours, aggregated modelling. What has not happened is the corresponding rigour about what those inventions cost. Almost nobody measures how much error their conversion value schema imposes on their own predictions, how much of their reported ROAS survives an incrementality test, or whether the creative that won a network's internal allocation won on merit. The discipline optimises hard against numbers it has not validated, which is the same failure as everywhere else in this cluster, expressed by unusually numerate people under an unusually severe information constraint.
