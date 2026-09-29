# Every Control Green and Nobody Has Measured What That Buys

**Industry:** [[grc-compliance-platforms|GRC & Compliance Platforms]]
**Type:** High Impact
**One-liner:** The platform measures control implementation and the market treats it as evidence of security, and the relationship between the two has never been tested against incident data by anyone.
**Tags:** #causal-inference #survival-analysis #bayesian-inference #confidence-intervals #gradient-boosting #hypothesis-testing #evaluation-metrics #compliance

## The Problem
A compliance platform tracks whether an organisation has implemented the controls a framework specifies: access reviews performed, encryption enabled, vulnerability scanning running, background checks completed, policies acknowledged, changes approved. When enough are green, an auditor attests and the organisation receives a report that enterprise buyers, insurers and partners treat as an assurance signal.

The signal's meaning is assumed. The frameworks are consensus documents produced by committees of practitioners — reasonable, widely accepted, and not derived from data about which controls prevent incidents. Nobody has tested whether organisations with a given control implemented suffer fewer or less severe incidents than comparable organisations without it, controlling for the obvious confounders.

Practitioners are candid about this in private. The gap between compliance and security is the oldest joke in the field, and the substance of it is that a control can be technically implemented in a way that satisfies an auditor and does nothing — an access review performed as a bulk approval, a policy acknowledged without being read, a scanner running against a fraction of the estate.

The consequences are real. Organisations allocate security budget toward what the framework requires because that is what gets certified, which is a reasonable response to procurement pressure and may not be the allocation that reduces the most risk. Insurers price partly on certification. Enterprise buyers gate purchases on it. A large economic apparatus rests on a correlation nobody has estimated.

The platform is the only party positioned to estimate it. It holds continuous control state across tens of thousands of organisations, with configuration detail, over years — and it uses that to render dashboards.

## Why It's Unsolved
Incident data is the missing half and it is scarce, sensitive and non-random. Organisations do not disclose most incidents, disclosure requirements capture only some categories, and the ones that become public are the largest and the most embarrassing. Any analysis built on public breach data is analysing a biased sample.

The commercial position is uncomfortable in the way that recurs across every assurance business here. A platform selling certification against a framework has no obvious interest in publishing that a third of the controls do not predict anything. The finding would be valuable to customers and corrosive to the product's framing.

The confounding is severe. Organisations that implement controls well differ systematically — better funded, more mature, more attentive — and separating the control's effect from the organisation's character requires careful design rather than a correlation. This is genuinely hard and is not a reason not to attempt it.

And the frameworks have no mechanism to respond. They are revised on multi-year cycles by committee, so even a clear empirical finding would take years to change what is certified, which reduces the perceived value of producing it.

## What a Solution Looks Like
Start with the correlations and be honest about what they are. Relating control state to the incidents that are observable — disclosed breaches, insurance claims where an insurer partner will share, customer-reported incidents — across a large population gives a first empirical picture, with the sample bias stated rather than hidden. Even a crude result is more than the field currently has.

Use control quality, not control presence. The platform sees configuration detail: whether an access review was a genuine review or a bulk approval, whether scanning covers the estate or a subset, whether multi-factor authentication is enforced or merely available. Distinguishing implemented from implemented well is the most informative variable available and is thrown away by the binary framing certification requires.

Partner for the outcome data. Insurers hold claims data and have a direct interest in knowing which controls predict losses; several have begun building this internally. A platform holding control state and an insurer holding claims is the natural pairing, and the analysis is achievable where neither party can do it alone.

Report the uncomfortable finding. If some controls predict nothing, saying so is the most valuable contribution this category could make — and a platform that publishes it becomes the one making evidence-based recommendations while competitors sell checklists.

## Impact If Solved
A large apparatus of procurement, insurance and budget allocation rests on an assumption about controls that nobody has tested, and the only organisations able to test it sell the certification. Relating control quality to observable incident outcomes, with the sample limitations stated, would be the first empirical evidence in a field that has operated on consensus for thirty years — and would let organisations spend on what works rather than on what gets certified.
