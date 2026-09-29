# A Score That Is the Same for Every Brand

**Niche:** [[niches/influencer-marketing-platforms/creator-risk-and-suitability/profile|Creator Risk & Brand Suitability]]
**Industry:** [[industries/influencer-marketing-platforms|Influencer Marketing Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every platform has a searchable creator database and an authenticity score, and none of them can tell a brand whether this specific creator is a risk for this specific brand.
**Tags:** #large-language-models #transformers #compliance #evaluation-metrics #confidence-intervals #automation #bert #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to tell a brand whether this specific creator is a risk for this specific brand — and whoever answers that replaces a generic authenticity score with a judgement somebody can act on.

## The Problem
A brand is about to sign forty creators. The platform shows a brand safety score for each — a single number derived from a generic scan of recent posts. It tells a financial services brand nothing about regulatory claims in a creator's back catalogue, tells a children's brand nothing about content adjacency, and tells a brand with public commitments nothing about whether this creator has said things that contradict them. So a coordinator scrolls through feeds for as long as they can stand, on the newest content only, and the brand signs on that basis. The exposure is real, the tooling answers a different question, and everyone knows it.

## Why Nobody Has Built This
A universal score is buildable once and sellable to everyone, which is why it exists, and a brand-specific judgement requires understanding what each brand cares about. Historical content across video, audio, comments and deleted-but-archived material is expensive to process and was impractical until recently. Nobody wants to be the party that declares a creator risky. And when something goes wrong the brand absorbs it publicly, not the platform.

## What to Build
Make the assessment brand-specific. Take the brand's own risk posture as input — categories, values, regulatory exposure, public commitments, competitor conflicts — which is the whole difference from a universal score and can be expressed once and applied to every assessment. Assess the creator's full public history rather than recent posts, since the material that causes incidents is almost always old and the current tooling looks at the wrong window. Cover video, audio and comments, not just captions, which is where most of the content actually is and where the generic scanners do not look. Produce a reasoned assessment with the specific evidence rather than a score, because a manager must make a judgement and a number gives them nothing to weigh. Distinguish severity and recency properly, as a decade-old remark and a current pattern are different risks and a flat scan conflates them. Monitor after signing, since risk does not stop at selection and mid-campaign incidents are the most damaging. Assess adjacency — who the creator associates with and what appears alongside their content — which is a common source of brand exposure and is entirely unexamined. Keep a record of what was assessed and when, which is what protects the brand and the manager when something surfaces later. Support an escalation path for ambiguous cases, since many are genuinely judgement calls and pretending otherwise is worse. And measure the assessment against actual incidents, because a risk product that has never checked its own hit rate is selling comfort.

## Target Customer
Brand safety, legal and partnership teams, influencer platforms differentiating beyond workflow, and the agencies signing creators at volume.

## Impact If Built
A universal score is buildable once and sellable to everyone, which is why it exists and why it answers nobody's question. Taking the brand's own risk posture as input, and assessing the full history across video and comments, is where the exposure actually lives.
