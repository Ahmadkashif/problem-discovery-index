# Game User Acquisition Firms

## Profile
**Category:** Gaming & Interactive
**Market Size:** ~$40B US in mobile and PC game user acquisition spend; the specialist agency and in-house UA function directing it is a multi-billion-dollar layer of salaries and fees
**Tech Maturity:** The most quantitative marketing discipline in existence, predicting a quantity dominated by people who have not spent yet. Games UA teams run lifetime value models, incrementality tests and creative pipelines at a level most consumer marketing never approaches, and the number they are predicting has most of its mass in a tail that early behaviour identifies poorly.
**Workforce:** User acquisition managers and media buyers, UA data scientists and analysts, creative producers and playable ad engineers, portfolio and cross-promotion managers, monetisation partners on the game side

## Key Pain Themes
Games revenue is extraordinarily concentrated. A small fraction of players generate most in-app purchase revenue, and within that fraction the distribution is concentrated again — which means predicted lifetime value is a prediction about a heavy tail, made from a few days of behaviour, for cohorts where the decisive players have not spent anything yet. A model with good average error and a poor tail will systematically misprice exactly the cohorts worth buying.

The second theme is that lifetime value is not a property of the player. It depends on what the game ships afterward — content cadence, event quality, monetisation changes, balance — so a cohort's realised value is determined largely by a team the UA function does not control, while UA is held to the payback number.

The third is creative, where the industry has a documented practice problem. Misleading ads depicting gameplay that does not exist in the game have been widespread, have drawn platform policy responses and consumer protection attention, and persist because they acquire installs cheaply. Whether they acquire anything valuable, after the churn they cause, is a measurable question the industry has largely avoided asking.

## Current Tech Landscape
Acquisition runs through Meta, Google, AppLovin, Unity, ironSource, Moloco, TikTok and the programmatic layer, with attribution through AppsFlyer, Adjust and Singular under SKAdNetwork and its successors. Predicted lifetime value modelling is in-house at any serious operator. Creative production spans video, playable and static formats with network-specific specifications. Cross-promotion within a portfolio is a substantial and underexploited channel. Incrementality testing through geo splits and public service announcement campaigns exists and is used by a minority.

## Problems
- [[problems/game-user-acquisition-firms/high-impact|🔴 High Impact: Predicting a Number Whose Mass Is in People Who Have Not Spent Yet]]
- [[problems/game-user-acquisition-firms/low-impact-1|🟡 Low Impact: Creative That Shows a Game That Does Not Exist]]
- [[problems/game-user-acquisition-firms/low-impact-2|🟡 Low Impact: Portfolio Cross-Promotion Allocation]]
- [[problems/game-user-acquisition-firms/worker-life-1|🟢 Worker Life: Held to a Payback Somebody Else Determines]]
- [[problems/game-user-acquisition-firms/worker-life-2|🟢 Worker Life: The Playable Engineer Building an Ad for a Mechanic That Is Not in the Game]]
- [[problems/game-user-acquisition-firms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/game-user-acquisition-firms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
Games user acquisition optimises harder against a predicted number than almost any other marketing discipline, and that number is a heavy-tail expectation estimated from a few days of a cohort's life, for a quantity that will be determined mostly by what the game ships over the following six months. The discipline's sophistication is real and is pointed at the wrong decomposition: it treats lifetime value as a property of the acquired player rather than as a joint outcome of the player and the content they will encounter. Separating those two — which is possible, because the same cohorts are observed across many content cadences — would change both how UA is evaluated and how content investment is justified, and neither function currently has the evidence to argue with the other.
