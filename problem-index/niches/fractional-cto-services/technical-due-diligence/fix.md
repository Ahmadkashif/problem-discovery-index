# Fix: Twenty Risks, No Ordering

**Niche:** Technical Due Diligence
**Industry:** [[industries/fractional-cto-services|Fractional CTO Services]]
**Type:** Fix (Pain Point)
**One-liner:** Diligence reports flag every risk and rank none, because flagging is free and being wrong about severity is not, and nobody ever checks which flags materialised.
**Tags:** #confidence-intervals #evaluation-metrics #hypothesis-testing #bayesian-inference #logistic-regression #compliance #revenue-impact
**Contested on:** Whether a technical opinion formed in two weeks under restricted code access can be made defensible enough to price an eight-figure decision.

## The Problem

A technical diligence report arrives at the investment committee with twenty findings. Technical debt in the billing subsystem. Single-person knowledge concentration on the data pipeline. An unsupported framework version. Scaling headroom uncertain beyond a certain load. Two GPL-adjacent dependencies. Incomplete disaster recovery testing. Each is described, each is real, and each carries a severity label — high, medium, low — assigned by a practitioner's judgement with nothing behind it.

The committee's question is the one the report does not answer: which of these will actually cost us money, how much, and when. The practitioner knows that three of the twenty matter and the rest are the ordinary condition of any company of that age. The report does not say so, because saying so means being specifically wrong if one of the seventeen bites, and the incentive structure is entirely asymmetric — an unflagged risk that materialises is a professional catastrophe, while seventeen over-flagged risks cost nothing at all.

So reports hedge, committees discount the hedging uniformly, and the technical workstream contributes less to the decision than its cost implies. Everybody involved knows this and the equilibrium is stable, because no individual practitioner can afford to move first.

## Why It's Still Broken

**The asymmetry is structural.** A missed risk is attributable to a named person and ends a career. An over-flagged risk is invisible and costs nothing. No practitioner acting rationally will rank confidently, and no firm will instruct them to.

**No ground truth exists.** The category has never tracked which flagged risks subsequently materialised. Nobody knows the base rate for "single-person knowledge concentration on a core subsystem" causing a real problem within three years, because nobody has ever collected it — so severity judgements are not merely uncalibrated, they are uncalibratable with current practice.

**The outcome is on the other side of the close.** After the deal, the portfolio company is owned by the buyer and the diligence firm is gone. The one party who could close the loop — the investor, who holds the company for five years — treats the diligence report as a pre-close artefact and files it.

**The report format encourages enumeration.** Checklist-driven templates with a section per risk area mean every area produces findings whether or not the area is interesting, and a report with three findings looks like insufficient work regardless of whether three is the honest number.

**Ranking requires quantification nobody will attempt.** Saying a risk is severe means estimating remediation cost and probability, which is a forecast, which can be checked, which returns to the first problem.

## What a Fix Looks Like

**Investors must close the loop, because only they can.** A private equity firm holds its portfolio companies for years and has every diligence report it ever commissioned. Reviewing each at eighteen and thirty-six months against what actually happened — which flagged risks materialised, what they cost, and which of the problems that emerged were never flagged at all — is entirely within one organisation's control. No cooperation from anyone is required. A firm doing thirty deals a year has a meaningful base rate within four years, and nobody has one today.

**Express severity in money and time.** Estimated remediation cost with a range, and the window in which it is likely to bite. A committee can act on "roughly $400k of engineering across eighteen months, most likely in year two" and cannot act on "medium". The range is where the honesty lives — a wide range is a legitimate answer and is more useful than a colour.

**Separate the three findings that matter.** A mandatory short section: the small number of findings that should affect price, structure or the hundred-day plan, stated with the practitioner's actual confidence. Everything else moves to an appendix explicitly framed as the ordinary condition of a company at this stage. Making this a required report structure removes the individual practitioner's exposure, because the format compels the ranking rather than the person choosing to offer it.

**Score the practitioners.** Once the investor has outcomes, diligence providers can be evaluated on whether their high-severity flags materialised and whether the problems that emerged were in their report at all. That single measurement changes the incentive from flag-everything to be-right, which is the only force that will move the equilibrium.

**Base rates in the report.** With a corpus, the report can say: of companies of this shape with this pattern, this share hit a material problem within three years. That is a fundamentally different claim from a practitioner's colour code, and it is available to any investor willing to look at their own history.

## Who Feels the Pain

The investment committee, receiving a document engineered to be unfalsifiable and having to price a deal from it anyway.

The practitioner, who knows which three findings matter, cannot say so without personal exposure, and watches their genuine insight get flattened into a colour.

The portfolio company, which inherits a hundred-day plan built on an unranked list and spends the first year remediating findings in the order they appeared in a report rather than in the order of what would actually hurt.

And the diligence firm, competing on reputation in a market where quality is unobservable, which is exactly the market structure that prevents anyone from being rewarded for being better.

## Impact If Fixed

The technical workstream starts affecting prices. A finding expressed as a cost range in a window is negotiable — it becomes a price adjustment, an escrow, a condition — while a colour code is not.

The investor with the base rates has a genuine edge in a market where everyone else is guessing, and the edge is built entirely from data they already own and have never looked at.

And the incentive inverts. When flagging everything stops being free because the flags are scored, the category's reports become shorter, sharper and worth what they cost.
