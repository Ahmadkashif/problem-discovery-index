# Signing on Current Reach When the Question Is Who Is Still Working in Five Years

**Industry:** [[creator-talent-agencies|Creator Talent Agencies]]
**Type:** High Impact
**One-liner:** Agencies commit years of representation on the basis of a follower count, to careers whose main risk is a distribution algorithm that can halve a creator's reach in a month.
**Tags:** #survival-analysis #time-series-forecasting #gradient-boosting #confidence-intervals #causal-inference #change-point-detection #evaluation-metrics #revenue-impact

## The Problem
An agency's economics depend on signing creators whose earning capacity grows and lasts. The signing decision is made on current audience size, recent growth, a manager's sense of the person, and whether a competitor is also interested. It is a bet on a career and it is made with a snapshot.

Creator careers behave unlike traditional talent careers in ways the inherited model does not accommodate. The audience is not owned; it is granted by a platform's distribution and can be withdrawn. A format ages — a creator who built on one style of video finds it stops being served, and the decline looks like a personal failure when it is a systemic change. Income concentrates in a small number of brand categories that move together in a downturn. And the whole roster is exposed to the same handful of platforms, so an agency that believes it has diversified across forty creators has in fact taken one large position on three distribution algorithms.

Nothing in the industry forecasts this. Managers observe decline once it is unmistakable and respond by trying to diversify the creator into products, live events or other platforms — usually at the point when leverage is already gone, which is the worst moment to start.

The other half of the problem is that the agency cannot say what its own roster is worth. A creator's expected earnings over the next three years, and the uncertainty around it, is the number that should drive signing, investment, advance decisions and the agency's own planning, and it is not computed anywhere.

## Why It's Unsolved
The industry is young and built on relationships, and the people who are good at it are good at judging individuals rather than at modelling populations. There is a genuine and reasonable scepticism that a career is forecastable at all, and a strong cultural preference for the manager's instinct — which is real and valuable and also demonstrably prone to the same recency bias as everyone else's.

The data is fragmented by design. Platform analytics are per-creator and per-platform, accessible only through the creator's own account, and increasingly restricted. Earnings data sits in agency finance systems in a form that is per-deal rather than per-career. Nobody has assembled the longitudinal picture of many creators' trajectories over many years, which is what any trajectory model requires.

Survivorship bias contaminates every intuition in the business. The visible examples are the creators who lasted; the ones who plateaued at a million followers and quietly stopped earning are not in anyone's reference set, and an industry that learns from its successes will systematically misunderstand what predicts durability.

And the incentives cut against long horizons. A manager is compensated on current deals, and the work that would protect a five-year career — building owned audience, developing product, diversifying platforms — costs current earning time. That trade is made implicitly, constantly, in favour of the present.

## What a Solution Looks Like
Forecast the career as a distribution, not a line. Expected earnings over three years with an interval, decomposed into platform-dependent and platform-independent income, is the number that should drive every decision an agency makes about a creator. It will be wide, and the width is informative: a creator whose income is entirely dependent on one platform's recommendation surface has a genuinely wider distribution than one with an email list and a product, and that is the case for diversification made numerically rather than rhetorically.

Model the platform risk explicitly, because it is the dominant factor and it is correlated across the roster. Reach changes attributable to algorithm and format shifts are separable from those attributable to a creator's own output, using the behaviour of comparable creators as a control — which is exactly the cross-roster comparison an agency can make and an individual creator cannot. Knowing that a decline is systemic rather than personal changes the advice and changes the creator's morale.

Detect the turn early. A format losing distribution shows up in reach-per-post and in audience composition before it shows up in income, and the gap between those two is the window in which diversification is still cheap. Missing that window is the single most expensive recurring error in creator management.

Select on durability signals rather than reach. Owned audience, format breadth, audience age and retention, income concentration by brand category, and the creator's own working patterns are candidate predictors of a career that lasts, and an agency with years of roster history can find out which of them actually predict.

## Impact If Solved
An agency is a portfolio of concentrated, correlated, undiversified bets on short careers, selected on a lagging popularity metric. Trajectory forecasting changes signing, advance and investment decisions; separating systemic from personal decline changes the advice given at the moment it matters most; and early detection of format decay opens the window where diversification is still affordable. For the creators, it is the difference between a representation business that manages a career and one that monetises a moment.
