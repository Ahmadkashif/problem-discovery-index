# Estimates Sold as Facts With No Published Error

**Niche:** [[niches/marketing-agencies-smb/search-competitive-intelligence-data/profile|Search & Competitive Intelligence Data]]
**Industry:** [[industries/marketing-agencies-smb|SMB Marketing Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every number in the product is a modelled estimate, and every number is displayed as though it were measured.
**Tags:** #tabular-ml #gradient-boosting #evaluation-metrics #anomaly-detection #causal-inference

## The Problem
Search volume, traffic, and competitor revenue figures in these products are not observations. They are estimates — from clickstream panels projected to a population, from clickstream-to-search-volume models, from sampled rank tracking, from partial crawl coverage. Some are close. Some, particularly for smaller sites, long-tail keywords, and non-US markets, are far off.

They are presented as flat integers. A traffic estimate of 41,200 looks like a measurement. Agencies build client strategies on it, pitch new business with it, and set expectations that they will later be judged against.

The organization knows the estimates vary in quality. It knows panel coverage is thin in some markets, that keyword volume estimates for low-volume terms are unstable, and that traffic estimates for sites below a size threshold are close to noise. None of that reaches the customer, and internally it is understood as a known limitation rather than measured as a distribution.

## Why Nobody Has Built This
Confidence intervals look like weakness in a competitive market. When a rival ships a number and you ship a number with an interval, the sales conversation is harder — even though the interval is the honest product. Nobody wants to move first.

The accuracy question is also awkward because it is answerable. Site owners have their own analytics, and every comparison of an estimate to actual traffic is a potential embarrassment. There is a quiet institutional preference not to run that comparison systematically.

And there is no ground truth pipeline. Building one requires site owners to share verified analytics, which is a partnership programme nobody has bothered to construct even though the incentive to participate — better estimates for your own site — is obvious.

## What to Build
Measure the estimates and report their uncertainty.

**Assemble ground truth through a verification programme.** Site owners connect verified analytics in exchange for corrected estimates and a report on how the model performs for sites like theirs. That is a fair trade and it produces the labelled dataset the whole product needs.

**Model estimation error as a function of what the model knows.** Site size, category, geography, traffic composition, panel coverage in that market. The output is an interval per estimate, computed rather than asserted.

**Show the interval where the number is weak.** Not everywhere — a high-confidence estimate for a large US site can stay a number. The value is in flagging the cases where the figure should not be relied on, which is exactly where agencies are currently misled and later blamed.

**Fix the systematic biases the ground truth reveals.** Panel projection almost certainly mis-estimates specific categories and geographies in consistent directions, and those corrections are learnable.

**Publish accuracy by segment.** No competitor does, and being the first to publish is a positioning move as much as a product one — an agency choosing a data vendor for a client pitch has no current basis to choose except brand.

## Target Customer
Chief Data Officer or VP of Data Products. The strategic argument is that these products increasingly compete on breadth of features against each other, and accuracy is the one axis where a serious data operation can differentiate and no one is claiming ground.

## Impact If Built
Agencies plan client work, set expectations, and win business on these numbers, and the numbers are estimates presented as measurements. Publishing honest uncertainty makes the tool usable for the decisions it is actually used for — and the verification programme that produces it makes the underlying estimates better for everyone.
