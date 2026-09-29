# Build: Candidates Worth a Human's Time

**Niche:** Detection & Candidate Review
**Industry:** [[industries/brand-protection-firms|Brand Protection Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A detection and review pipeline that ranks candidates by expected harm rather than by match strength, and gives the reviewer the context that determines legitimacy before they decide.
**Tags:** #cnns #contrastive-learning #gradient-boosting #graph-theory #evaluation-metrics #confidence-intervals #automation #worker-facing
**Contested on:** Whether the candidates reaching a reviewer are the listings that matter, and whether the reviewer has what they need to decide.

## The Problem

The queue is ordered by match strength. A listing whose image is a near-exact copy of a brand photograph ranks highly. A listing from an operator running four hundred accounts, using original photography and a misspelled brand name in the description, ranks low or does not appear.

So the review capacity — which is the constraint — is spent on the listings that are easiest to detect rather than the ones that do the most damage. A single seller offering one counterfeit item and an operation shipping thousands a week arrive in the same queue, undifferentiated, and the second is frequently harder to detect than the first.

The review itself is worse served. The analyst sees a photograph, a title, a price and a seller name, and must decide whether this is infringement. What would actually determine it — whether this seller is an authorised distributor, whether the goods are genuine units sold through a parallel channel, whether the listing is a repair service or a compatible part, what was decided about this seller last month — is not on the screen.

So the decision is made on the visual and the price, which is exactly the basis on which legitimate resellers, repairers and parallel importers get actioned.

## Why Nobody Has Built This

**Volume is the product.** A pipeline that surfaces fewer, better candidates produces fewer notices, and notices are what the contract is priced on. The commercial incentive points at match volume.

**Harm ranking requires operator attribution.** Ordering by expected harm means knowing that these four hundred listings are one operation, which is the capability described in [[niches/brand-protection-firms/operator-attribution/profile|🟠 Operator Attribution]] and is not built.

**Legitimacy context lives with the brand, not the firm.** Authorised distributor lists, serial and batch data, and channel records sit with the client and are frequently not shared, incomplete or out of date.

**False positives cost the firm nothing directly.** A wrongly-actioned seller is harmed, the platform absorbs the appeal, and the firm's count goes up. The absence of a cost signal is why precision has not been prioritised.

**Better detection worsens the review problem.** A matcher that surfaces more borderline cases increases the number of hard legal judgements made in three seconds, which nobody has resourced.

**Reviewer accuracy is unmeasured.** Without an error rate in either direction, there is no evidence that the review is a problem and no basis for investing in it.

## What to Build

**Rank by expected harm, not match strength.** Estimated volume, price point, product category risk, operator scale and distribution reach. A high-volume operation ranks above an isolated listing regardless of how cleanly the image matched.

**Put the legitimacy context in front of the reviewer.** Authorised distributor status, prior determinations on this seller, seller tenure and rating history, whether the listing describes repair or compatibility, whether the price is consistent with genuine parallel supply. The reviewer currently infers all of this from a photograph.

**Classify the legal category before the queue.** Apparent counterfeit, apparent authorised resale, apparent parallel import, apparent repair or compatible part, apparent parody or commentary, unrelated use of a similar mark. These require different handling and currently arrive identically — and routing them separately is the single most effective protection against wrongful action.

**Require and record a rationale.** The reviewer states the basis for the determination in a structured form. This takes seconds, makes the decision reviewable, and is the only thing that makes an appeal evaluable against what was actually decided.

**Measure accuracy in both directions.** Sample determinations and re-review them blind. The rate at which legitimate listings are actioned is the error that matters most and is unknown at every firm.

**Feed appeal outcomes back.** A reversed determination is the strongest available signal about the detection and review pipeline, and it currently reaches nobody.

**Ingest the brand's own channel data properly.** Authorised seller lists, serialisation and distribution records, maintained rather than collected once. Most wrongful actions against legitimate sellers would be prevented by a current authorised-seller list alone.

## Target Customer

Brand protection firms with a quality position to defend, particularly those serving brands that have been publicly embarrassed by wrongful enforcement against a legitimate seller.

Brands themselves, who bear the reputational cost of a wrongly-suspended reseller and currently receive a count that does not distinguish.

Platforms, who absorb the appeals and are increasingly under regulatory pressure on notice accuracy — and who could require rationale and accuracy data from notice senders.

## Impact If Built

Review capacity moves to the listings that cause the harm, rather than to the ones that matched most cleanly, which is a straight reallocation of the industry's binding constraint.

Classifying the legal category before review is the most effective available protection against actioning legitimate sellers, and it is a routing change rather than a new judgement.

And measuring the wrongful-action rate would produce the number this industry does not have — the one that would let a brand choose a firm on accuracy rather than on volume.
