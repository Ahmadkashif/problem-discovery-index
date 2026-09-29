# The Same Flakiness Rediscovered Everywhere

**Niche:** [[niches/qa-test-automation-vendors/test-corpus-intelligence/profile|Test Corpus Intelligence]]
**Industry:** [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** A framework's known race condition produces the same flaky failure in thousands of customers' suites, each of whom diagnoses it independently over several weeks.
**Tags:** #k-means-clustering #dbscan #bert #descriptive-statistics #evaluation-metrics #confidence-intervals #quick-win #automation
**Contested on:** Every serious competitor that gets here is fighting to use a fleet-wide record of tests, failures, repairs and the changes that caused them — and whoever does that can distinguish a cosmetic change from a regression, which is the capability the whole category is missing.

## The Problem
A widely used component library has a timing behaviour that causes tests to fail intermittently when an element is asserted on immediately after a transition. The failure looks like an ordinary flaky test. Thousands of teams encounter it, each spends between an afternoon and several weeks establishing the cause, each arrives at the same workaround, and a few of them write a blog post. The vendor whose platform ran all of those tests sees the identical failure signature across their entire customer base and reports it to each customer as a flaky test.

## Why It's Still Broken
Failures are analysed per customer because the product is scoped per customer, and nothing aggregates signatures across the fleet. The signature is highly recognisable — the same framework, the same element type, the same timing pattern — which makes this an easy clustering problem nobody has run. There is a mild concern about attributing a problem to a third-party framework publicly, which is a communication question rather than a reason. And the support organisation encounters it repeatedly and handles each instance as a ticket.

## What a Fix Looks Like
Cluster failures across the fleet and publish what the clusters mean. Group failure signatures across customers by their structural characteristics — framework, version, element and interaction type, timing pattern — which is straightforward clustering and immediately surfaces the patterns affecting many customers. Attribute each cluster to a cause where it can be established, which for framework behaviours is usually a known issue and for others is worth the vendor's investigation once rather than every customer's investigation separately. Tell customers when their flaky test matches a known fleet-wide pattern, with the cause and the remedy, which converts weeks of diagnosis into a notification. Publish the catalogue, since it is a public good, is a strong credibility position for the vendor, and reaches the customers of every other vendor too. Report the cluster's prevalence, which helps the framework maintainers prioritise and is information only the vendor has. And feed it upstream to the framework projects, since the fix belongs there and the evidence exists nowhere else.

## Who Feels the Pain
Teams spending weeks diagnosing a known framework behaviour; support organisations handling the same issue repeatedly as individual tickets; and framework maintainers who do not know how widely a behaviour is causing trouble.

## Impact If Fixed
Fleet-wide signature clustering is straightforward and immediately identifies the patterns affecting many customers. Notifying a customer that their flaky test is a known pattern turns weeks of independent diagnosis into a message, and feeding it upstream is where the actual fix belongs.
