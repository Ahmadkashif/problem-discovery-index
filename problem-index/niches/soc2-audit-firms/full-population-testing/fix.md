# Fix: The Integration Fetches Evidence for a Sample

**Niche:** Full-Population Testing
**Industry:** [[industries/soc2-audit-firms|SOC 2 & Attestation Audit Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The firm connected to the client's compliance platform, which holds every item, and uses it to retrieve the twenty-five it was going to sample anyway.
**Tags:** #evaluation-metrics #compliance #data-integration #automation #workflow-orchestration #confidence-intervals
**Contested on:** Whether an auditor examines every item in a control's population, now that the population is sitting in a platform the client already runs.

## The Problem

The firm has built an integration with the client's compliance platform. It was sold as a modernisation and it genuinely helps — evidence arrives without the client having to produce it, the request list is shorter, and fieldwork moves faster.

What the integration does is retrieve the evidence for the sample. The auditor selects twenty-five change tickets, the integration fetches those twenty-five, and the test proceeds as before.

The platform holds all four thousand. The query that returns twenty-five and the query that returns four thousand differ by a limit clause.

So a firm has built the hard part — the connection, the authentication, the data mapping — and uses it to make the existing method more convenient rather than to change the method. The sampling that existed because examining everything was impossible continues inside a system where examining everything is a query.

Nobody made a decision about this. The integration was scoped as an evidence collection improvement, because that is how the inefficiency was framed, and the methodology was not part of the project.

## Why It's Still Broken

**The integration was scoped as evidence collection.** The problem it was built to solve was the slowness of evidence requests, not the weakness of sampling.

**Methodology change requires a different approval.** Connecting to a platform is an operations decision. Changing how controls are tested is a methodology decision requiring technical standards sign-off.

**More items tested means more exceptions found.** The method change has a consequence the firm has to be willing to accept, and the integration alone does not.

**The report does not reward it.** Testing four thousand items produces the same opinion as testing twenty-five, so there is no visible return.

**Nobody costed the alternative.** The marginal cost of testing the full population through an existing integration is close to zero, and nobody has computed it because nobody framed the question.

**The sample selection tooling is already built.** Workpaper systems support sampling well, which makes the existing path the path of least resistance.

## What a Fix Looks Like

**Extract the population, not the sample.** Change the query. For controls where the integration already reaches the data, this is close to a one-line change with a large methodological consequence.

**Express the control test as a rule.** Once the population is available, the test is a rule evaluated over it rather than a human checking items. Writing the rules is the actual work and it is reusable across every client.

**Record the population size in the workpaper.** Even before the method changes, recording what the population was makes the sample's weakness visible internally and is the first step to changing it.

**Make the methodology decision explicitly.** Someone with technical standards authority should decide whether the firm tests full populations where the data allows. Currently the answer is no by default because nobody asked.

**Accept the exceptions.** A firm testing everything will find more, and the professional answer is that those exceptions were always there. The commercial conversation with clients about this needs preparing in advance rather than discovering mid-engagement.

**Report the difference internally first.** Track which controls were tested exhaustively versus sampled, per engagement. Even without external reporting, a firm knowing its own testing depth is in a better position than one that does not.

**Reuse across clients.** The rules and the connectors are the same for every client on the same platform, which is what turns a per-engagement cost into a firm-level asset.

## Who Feels the Pain

The reader of the report, who receives an opinion based on twenty-five items when four thousand were available to the auditor through an existing connection.

The associate, who selects a sample and checks it by hand against a system that could have evaluated the rule over everything in seconds.

The firm, which has paid for the hard part of the capability and uses it to make an obsolete method faster.

And the client with genuinely well-operated controls, whose quality is indistinguishable in a report that tested twenty-five of them.

## Impact If Fixed

Changing the query from a sample to a population is close to trivial where the integration already exists, and it converts a weak inference into a strong one.

Expressing control tests as reusable rules is the work that makes this scale, and it is written once and applied to every client on the same platform.

And recording the population size in the workpaper, even before anything else changes, would make the weakness of the current sample visible inside the firm — which is where the decision to change it has to be made.
