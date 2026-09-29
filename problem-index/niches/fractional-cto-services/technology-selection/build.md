# Build: Operational Outcomes at Decision Granularity

**Niche:** Technology Selection Advice
**Industry:** [[industries/fractional-cto-services|Fractional CTO Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A corpus of what actually happened after platform decisions — real migration cost, real failure modes at scale, real operational burden, real reversals — collected from the operators who lived it.
**Tags:** #gradient-boosting #bayesian-inference #confidence-intervals #evaluation-metrics #k-means-clustering #hypothesis-testing #data-integration
**Contested on:** Whether a platform recommendation rests on operational evidence from comparable deployments or on vendor documentation and the advisor's last three projects.

## The Problem

An advisor recommending a database for a client is answering a question with a real answer: for a workload of this shape at this scale with a team of this size, does this technology work, what does operating it actually cost in people and money, and what goes wrong.

Thousands of organisations have already run that experiment. Each one knows what the migration really cost against what was estimated, which failure modes appeared in production and at what load, how many engineer-hours a week the thing consumes, how the cost curve behaved as usage tripled, and whether they would choose it again. That is precisely the evidence a decision needs, and it exists only as scattered private experience, conference talks selected for having gone well, and blog posts written either in triumph or in anger.

So the advisor substitutes. Vendor documentation, which describes the intended behaviour. Analyst quadrants, which describe market position. Benchmarks published by interested parties. And their own three projects, which is a sample of three drawn by the accident of employment history. A recommendation that commits a company to a decade of operational consequence is made on that basis, routinely, by competent people, because nothing better is available.

## Why Nobody Has Built This

**Contribution is the problem, not collection.** The data is post-hoc, unstructured, and lives in the heads of people who have no reason to write it down. Every attempt to build this kind of corpus dies on the supply side, and the supply side is hard because contributing costs real time and returns nothing immediate.

**Candour requires anonymity, and anonymity destroys verifiability.** The useful contributions are the negative ones — we chose this and it cost us two years — and nobody attaches their employer's name to that. Anonymous contribution invites vendor astroturfing and competitor sabotage, and the mechanisms that make anonymous data trustworthy are the unsolved part.

**Vendors will fund the compromised version.** The revenue model that presents itself immediately is vendor sponsorship, which is exactly what destroyed analyst credibility, and the pressure toward it is enormous for anything that reaches scale.

**Comparability is genuinely hard.** "It didn't scale" means nothing without workload shape, access pattern, data volume, team size and operational maturity. Collecting enough context to make outcomes comparable makes contribution expensive; collecting less makes the corpus useless. Threading that is the actual product design problem and it has no obvious solution.

**The cold start has no bridge.** The corpus is worthless until it is dense in a given category, and contributors will not arrive before it is useful. Most attempts have tried to solve this with breadth and failed; the answer is almost certainly extreme narrowness at the start.

## What to Build

**Start with one category and go deep.** Not a technology decision platform — the operational record for one class of decision, chosen for high stakes, frequent occurrence and strong opinions: primary datastore selection, for instance. Density in one category is worth more than coverage of thirty, and it is the only cold start that works.

**Structure the contribution around what was decided and what followed.** The decision as made, with the alternatives considered. The context in enough detail to support comparison — workload shape, scale trajectory, team size, existing stack, deadline pressure. Then the outcomes: migration cost estimated versus actual, failure modes with the load at which they appeared, operational burden in engineer-hours, cost curve as usage grew, whether it was reversed and what the reversal cost. Structured enough to aggregate, short enough that a person will finish it.

**Buy the first wave.** Pay for structured interviews with operators who have run the decision, the way research firms pay for expert calls. It is expensive and it is the only reliable route past the cold start, and the resulting corpus is what attracts voluntary contribution.

**Make advisors the second wave.** A fractional CTO sees many decisions across many clients and is the highest-density source in the market. Give them a corpus they can cite in client reports in exchange for de-identified contribution — the exchange is favourable to them and it is the mechanism that turns a scattered profession into a collection network.

**Anonymity with verification.** Contributor identity verified and held, publication de-identified, provenance signalled — an operator at a company of this size in this sector — with weighting by verification strength. Vendor employees identified and excluded from the categories they sell into. This is the trust design, and it is the thing that has to be right from the first week because it cannot be retrofitted.

**Report distributions, not verdicts.** The output is never "choose this." It is: across forty-one deployments at this scale with this workload shape, migration ran a median of 2.3× the estimate, these failure modes appeared and at what load, operational burden was this many hours a week, and nine reversed the decision for these reasons. The advisor makes the recommendation; the corpus gives them a reference class instead of a sample of three.

**Refuse vendor money, visibly.** Subscription revenue from advisory practices and engineering organisations, and a published policy on vendor funding. The credibility is the asset and there is no version of this that survives selling it.

## Target Customer

Fractional CTOs, architecture consultants and technical advisory practices — the highest-intensity users, the best contributors, and the people whose professional exposure on a recommendation makes a citable reference class worth real money.

Second: engineering leadership at mid-market companies facing a specific decision, who will pay for one category's corpus at the moment they need it.

## Impact If Built

Platform recommendations acquire a reference class. The difference between "in my experience" and "across forty-one comparable deployments" is the difference between an opinion and an argument, and it is the first time the profession would have the latter.

The negative results become visible. The industry's technology discourse is a survivorship-biased record of successes written by people who succeeded; a corpus that records reversals as diligently as adoptions corrects the largest systematic distortion in how these decisions get made.

And the advisor's sample of three becomes a sample of forty, which is the whole point.
