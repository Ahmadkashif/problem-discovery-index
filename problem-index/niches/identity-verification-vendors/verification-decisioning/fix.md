# A Pass Rate Is Not an Accuracy

**Niche:** [[niches/identity-verification-vendors/verification-decisioning/profile|Verification Decisioning]]
**Industry:** [[industries/identity-verification-vendors|Identity Verification Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The dashboard reports the proportion of applicants who passed, which says nothing about whether the decisions were right.
**Tags:** #evaluation-metrics #descriptive-statistics #quick-win #confidence-intervals #compliance #hypothesis-testing #automation #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to confirm that a person is who they claim to be in seconds — and the contest splits cleanly enough that it is not terminal.

## The Problem
A vendor reports a ninety-four percent pass rate and a customer treats it as a quality measure. It is not: a vendor that passed everyone would report one hundred percent. The number conflates the applicant population, the threshold, the document mix and the actual accuracy into a single figure that cannot be compared between vendors or even between months. Customers procure on it, vendors compete on it, and it measures none of the things either party cares about.

## Why It's Still Broken
Pass rate is the metric that can be computed without outcome data, so it became the reported one — a number that is always available will displace a better number that is sometimes unavailable. It also flatters everyone, since a high pass rate looks like both accuracy and good conversion. Nobody agreed a better standard. And customers lack the data to construct one themselves.

## What a Fix Looks Like
Report the components instead of the composite. Break the pass rate into its parts — document read failure, liveness failure, face match failure, database resolution failure, manual review outcome — which is the fix and is available today in every vendor's logs. Report by document type, device and capture condition, since a pass rate over a mixed population is uninterpretable. Report retry and abandonment, because the applicant who failed twice and gave up is invisible in a pass rate and is the outcome that matters. Show the threshold and its effect, as the same system produces very different pass rates at different operating points and customers rarely know theirs. Report manual review agreement, which is a genuine quality signal obtainable without applicant outcomes. Publish the false accept rate at the operating point, since customers assume it and never see it. Distinguish a decline from an inability to complete, because they are different failures with different remedies. Standardise the definitions across the industry, as incomparable metrics are why procurement is uninformed. Show the customer their own population's distribution rather than a vendor average. And commit to measuring rejections, since decomposition is a start and outcomes are the answer.

## Who Feels the Pain
Customers procuring on an uninterpretable number; applicants failing for reasons nobody reports; policy teams unable to assess their own gate; and vendors competing on a metric that rewards leniency.

## Impact If Fixed
A number that is always available displaces a better number that is sometimes unavailable, and the pass rate flatters everyone. Decomposing it by failure stage, document type and device is available in the logs today and makes the metric mean something.
