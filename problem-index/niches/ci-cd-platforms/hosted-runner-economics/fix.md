# A Market Compared on List Price Alone

**Niche:** [[niches/ci-cd-platforms/hosted-runner-economics/profile|Hosted Runner Economics]]
**Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Hosted CI vendors are compared on price per minute, which is the one number that does not determine what a customer will actually pay or wait.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #cross-validation #quick-win #revenue-impact #automation
**Contested on:** Every serious competitor in hosted execution is fighting to deliver a started, warm, cache-local runner in seconds at the lowest cost per change — and whoever does that takes the account, because this market is compared on a spreadsheet and switching is a configuration change.

## The Problem
A platform team evaluates three vendors. They compare price per minute, machine specifications and concurrency allowances, and choose the cheapest. Six months later their bill is higher than the previous vendor's and their pipelines are slower, because the cheaper minutes are on slower machines, the queue is longer at peak, the cache is in another region, and the concurrency limit forces serialisation. Every one of those was discoverable during evaluation and none was published in comparable terms, so the decision was made on the only number available.

## Why It's Still Broken
List price is the one comparable number, so it becomes the basis of comparison by default. Vendors have no incentive to publish performance characteristics on which they might compare badly, and no independent benchmark exists with enough credibility to force it. Evaluations are short and run on a sample pipeline that does not reproduce the peak-time queueing or the cache behaviour at scale, which are the properties that actually differ. And the cost of a wrong choice shows up months later as a vague sense that pipelines are slow.

## What a Fix Looks Like
Make the comparison reflect what is paid and waited. Evaluate on cost per change delivered rather than price per minute, which incorporates machine speed, cache hit rate and redundant work, and is computable from a representative pipeline run repeatedly. Measure time to result including queue and startup, at peak as well as off-peak, since the peak is where the difference is and a quiet-afternoon trial will not show it. Test at realistic concurrency, because the serialisation imposed by a concurrency limit is frequently the largest practical difference between plans and is invisible on a single pipeline. Measure cache behaviour explicitly — hit rate and transfer time — since the proportion of a job spent moving data varies enormously between vendors and regions. Run the evaluation on the organisation's own worst pipeline rather than a sample one, because that is where the differences concentrate. And publish the methodology, since a credible shared comparison is the thing this market lacks and whichever vendor is genuinely best has an interest in it existing.

## Who Feels the Pain
Platform teams who chose on price and got a worse outcome; developers waiting at peak on a plan chosen for its minute rate; and vendors who are genuinely faster and cannot demonstrate it in a comparable way.

## Impact If Fixed
Cost per change and time to result including queue are both measurable in an evaluation and would change most vendor selections. Testing at realistic concurrency on the organisation's worst pipeline is what surfaces the differences that a sample trial hides.
