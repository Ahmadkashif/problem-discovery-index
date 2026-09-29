# The Expert Doing Setup for Three Days

**Niche:** [[niches/ai-red-teaming-firms/manual-expert-assessment/profile|Manual Expert Assessment]]
**Industry:** [[industries/ai-red-teaming-firms|AI Red Teaming Firms]]
**Type:** Fix (Pain Point)
**One-liner:** A four-week engagement gives its scarcest input — a researcher who is genuinely good at this — three days of environment setup, access negotiation and tooling before any research begins.
**Tags:** #worker-facing #automation #workflow-orchestration #evaluation-metrics #data-integration #quick-win #descriptive-statistics #compliance
**Contested on:** Every serious competitor in this sub-niche is fighting to produce the finding the client's own team and every automated suite would have missed — and whoever does that takes the engagement, because a client with an internal red team is paying for exactly one thing.

## The Problem
Day one of an engagement: request access, wait. Day two: receive credentials, discover the test environment differs from production, negotiate. Day three: wire up tooling to the client's API shape, write a harness, work out how to capture results. Day four: begin the work the client is paying for. Twenty percent of the scarcest resource in the business went to setup that is nearly identical at every engagement, and the researcher — whose value is in the last week when they have built enough context to see something non-obvious — has one week less to get there.

## Why It's Still Broken
Setup looks bespoke because every client's environment differs, which hides how repetitive the process is. Engagement teams are small and the person who could build the reusable harness is the person running the engagement. Access negotiation involves the client's security function and is treated as unavoidable friction. And the cost is inside a fixed-price engagement, so nobody outside sees it.

## What a Fix Looks Like
Move the setup off the researcher and before the engagement. Standardise the harness so that connecting to a new client's system is configuration rather than code, which covers most of the variation and is the largest single saving available. Run access negotiation as a pre-engagement workstream owned by the delivery organisation, completed before day one, which is a scheduling change rather than a technical one and removes the worst of the delay. Provide a pre-built environment with logging, result capture and the technique catalogue ready to run, so day one is exploration. Automate the catalogue sweep before the researcher arrives, so they start from what is already known to fail rather than rediscovering it — which both saves time and raises the floor the novel work starts from. Template the client-specific context gathering, since researchers ask the same questions every time. Measure the setup-to-research ratio per engagement, because it is currently unmeasured and is a large fraction of the firm's cost of goods. Reuse per-client configuration across repeat engagements, which currently starts from nothing each time. And protect the final week, since context accumulates through an engagement and the most valuable findings come late, which makes time lost at the start disproportionately expensive.

## Who Feels the Pain
Researchers spending a fifth of an engagement on plumbing; clients receiving three weeks of research for four weeks of fees; and the firms whose scarcest input is being spent on setup.

## Impact If Fixed
Twenty percent of the business's scarcest resource goes to a nearly-identical setup, and the time is taken from the end of the engagement where the best findings come from. A configurable harness plus a pre-engagement catalogue sweep raises the floor the novel work starts from.
