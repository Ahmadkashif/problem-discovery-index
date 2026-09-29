# The Category's Central Object, Unmodelled

**Niche:** [[niches/qa-test-automation-vendors/change-to-test-impact/profile|Change-to-Test Impact]]
**Industry:** [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The relationship between a change and the tests it breaks is the central object of the category and is modelled nowhere, which is why selection, repair and classification are all built on weaker proxies.
**Tags:** #graph-theory #gradient-boosting #bert #k-nearest-neighbors #evaluation-metrics #confidence-intervals #automation #cross-validation
**Contested on:** Every serious competitor here is fighting to model the relationship between an application change and the tests it affects — and whoever does that takes the category, because that relationship is its central object and is modelled nowhere.

## The Problem
A change renames a component and adjusts a layout. Forty tests fail. The selection mechanism did not know which tests to run because it uses file proximity; the repair mechanism does not know whether the change was cosmetic because it compares selectors; the flakiness detection cannot tell a maintenance break from a genuine failure because it looks at re-run behaviour; and the developer cannot be told whether their change is verified because nothing relates the change to the tests. All four failures are the same missing model, and both sides of it are in the repository and the execution history.

## Why Nobody Has Built This
Each capability was built separately by a different product team using whatever signal was locally available, which produced four proxies rather than one model. The historical relationship — this kind of change has broken these tests before — is free, requires no instrumentation and has not been used, apparently because nobody framed the problem as one relationship. Interface changes, which cause most end-to-end breakage, are outside code coverage entirely, so the one principled approach that exists does not cover the dominant case. And the vendors hold this data across thousands of applications and use it to display results.

## What to Build
Construct the relationship and build everything on it. Learn from history first, since every organisation has thousands of examples of a change followed by a set of test outcomes and the association is directly learnable with no instrumentation — which makes it available to every stack rather than to the ones that support coverage. Add structural evidence where it exists: coverage where obtainable, dependency graphs from build systems, and interface-element mapping for end-to-end tests, which addresses the case code coverage cannot see. Classify the change itself into behavioural and presentational, which is the distinction everything downstream needs and is derivable from the diff's structure — a renamed identifier, a moved element, a changed style are one class and a removed branch or an altered condition are another. Then serve all four consumers from the one model: selection, repair classification, failure attribution and change verification. Report confidence, since the model will be uncertain and the correct response differs by consumer — selection can tolerate uncertainty by running more, and repair cannot. And improve continuously, since every change and outcome is another labelled example.

## Target Customer
Test automation vendors, whose four separate features are all approximations of this; platform engineering teams; and the build system vendors whose dependency graphs are the strongest structural input.

## Impact If Built
Four separate capabilities in the category are approximations of one unmodelled relationship, and the data to construct it is free and universal. Learning from history removes the instrumentation requirement that caps adoption of the only principled alternative.
