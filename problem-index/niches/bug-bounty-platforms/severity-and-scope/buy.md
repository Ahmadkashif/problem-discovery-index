# Buy: Adjudication Practice From Marketplaces That Solved It

**Niche:** Severity & Scope Adjudication
**Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Every two-sided marketplace with disputes eventually built rules, precedent and neutral adjudication, and bounty platforms still resolve each argument privately from scratch.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #bayesian-inference #compliance #workflow-orchestration #revenue-impact
**Contested on:** Whether the rules a researcher works under are knowable before the work, or decided afterwards by the party who pays.

## The Problem

Marketplaces where one side does work and the other decides whether it was acceptable all face this problem, and the mature ones have solved it in recognisably similar ways: published rules specific enough to be applied consistently, a record of how prior cases were decided, an adjudication process with some independence from the paying side, and transparency about outcome rates so participants can choose where to work.

Bounty platforms have none of these fully. Rules are prose. Prior decisions are private. Adjudication is mediation by the platform, whose customer is the programme. Outcome rates by programme are not published, so a researcher cannot see that this programme closes forty per cent of valid submissions as informative.

The consequence is the standard one for a marketplace without adjudication: the supply side discounts its participation, the best participants leave for platforms or programmes with better reputations, and the market's quality degrades in a way the platform sees only as a slow decline in researcher engagement.

## What Already Exists

Labour marketplaces: Upwork, Fiverr and the freelance platforms, with dispute resolution processes, escrow, milestone acceptance criteria and published client rating and hire history — the last of which lets a freelancer avoid clients with bad records, which is precisely the missing capability here.

Content and gig platforms: appeals processes with published policy, escalation tiers and increasingly transparency reporting on outcome rates.

Insurance and warranty claims: loss adjustment practice, with defined severity schedules, independent adjusters and an appeals path — the severity schedule idea in particular transfers well.

Sports and competition: rule books, published precedent, and neutral officiating separated from the parties, which is the structural template for independent adjudication.

Vulnerability scoring: CVSS, EPSS and SSVC, providing a vocabulary for severity that bounty programmes use loosely and inconsistently.

## The Customization Gap

**CVSS is used as a label rather than a method.** Programmes cite CVSS and then assign the band they intend. Applying the scoring method rigorously, showing the vector, and reporting when a programme's assigned band diverges from the computed one is a small change with a large effect on disputability.

**No client-side reputation.** Every mature labour marketplace publishes how the paying side behaves — acceptance rates, payment speed, dispute outcomes. Bounty platforms publish researcher reputation and nothing about programme behaviour, which is a one-sided transparency that no other marketplace of this maturity retains.

**Adjudication is not independent.** Mediation by the platform, whose revenue comes from the programme, is structurally compromised however fairly individual cases are handled. Marketplaces that have faced this introduced separation — an ombuds function, an external panel, or at minimum a published process with outcome statistics.

**No precedent record.** Disputes resolve privately, so nothing accumulates. Publishing anonymised resolutions would let both sides predict outcomes and would reduce the volume of disputes substantially, which is the observed effect in every venue that has done it.

**Acceptance criteria are not agreed up front.** Freelance platforms learned to define deliverable acceptance before work starts. Bounty scope is the equivalent and is left as prose, which is the same mistake those platforms made and corrected.

**The first-to-file rule has no analogue and needs one.** Duplicate handling is where the lottery dynamic bites hardest, and no adjacent marketplace has this exact structure — the nearest is patent priority, which has formal filing timestamps and a public record precisely because the stakes require it.

## Target Customer

The platforms themselves, and the argument is researcher supply rather than programme satisfaction: every marketplace that neglected supply-side fairness eventually lost its best suppliers, and the strongest researchers are already selective about which programmes they work.

Programmes with a genuine interest in attracting good researchers would adopt published outcome statistics voluntarily, because a programme that rates fairly benefits from the comparison.

## Impact If Solved

Programme-side transparency is the single most transferable idea. Publishing acceptance rates, payment speed and dispute outcomes by programme would let researchers allocate effort rationally and would reward the programmes that behave well — which no current mechanism does.

Applying a severity method rigorously, rather than citing one, would convert most severity disputes from assertion against assertion into a disagreement about a specific vector component.

And a precedent record would stop the same argument recurring indefinitely, which is the cheapest available reduction in dispute volume for both sides.
