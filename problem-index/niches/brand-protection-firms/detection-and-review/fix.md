# Fix: Three Seconds and a Photograph

**Niche:** Detection & Candidate Review
**Industry:** [[industries/brand-protection-firms|Brand Protection Firms]]
**Type:** Fix (Pain Point)
**One-liner:** A legal determination that can end a small business's income is made from a product photo, a price and a seller name, by a reviewer with a throughput target.
**Tags:** #evaluation-metrics #confidence-intervals #worker-facing #compliance #hypothesis-testing #workflow-orchestration
**Contested on:** Whether the candidates reaching a reviewer are the listings that matter, and whether the reviewer has what they need to decide.

## The Problem

A reviewer opens a candidate. A photograph of a handbag. A price of sixty pounds. A seller name. A title. They have seconds, because the queue has thousands in it.

The question they are answering is whether this listing infringes. That is a legal question, and the answer depends on things not on the screen. Is the item genuine and lawfully resold, which is permitted? Is it a parallel import, which is permitted in some jurisdictions and not others? Is the seller an authorised distributor whose listing looks unofficial? Is this a repair service using the brand name to describe what it repairs, which is permitted? Is it a compatible part, correctly labelled? Is it commentary?

The reviewer sees a photograph and a price. A low price suggests counterfeit and is also what a clearance sale, a used item or a parallel import looks like. So the decision is made on a visual impression and a price signal, and the categories that are lawful look, from a photograph, exactly like the category that is not.

When they get it wrong in the direction of over-enforcement, a legitimate seller loses their listing, sometimes their account and their income, and appeals through a process built for a party with counsel.

## Why It's Still Broken

**The cost of a false positive falls outside the system.** The harmed party is a seller with no relationship to the firm. The platform absorbs the appeal. The firm's count increases. Nothing in the firm's own metrics registers the error.

**Throughput is the metric.** Reviewers are measured on candidates processed, which is the standard structure that produces quick decisions on hard cases.

**The context is not available.** Authorised seller lists are stale or absent. Purchase and distribution records sit with the brand. The reviewer could not make a better decision with more time because the information is not there.

**Notice processes favour the complainant.** Platform processes generally action on notice and place the burden on the seller to contest, which means an error costs the filer nothing and the seller a great deal.

**Accuracy is unmeasured.** No firm publishes a wrongful-action rate, and most do not compute one, so there is no evidence of a problem and no pressure.

**Appeal outcomes do not return.** The reversal, which is the clearest evidence of an error, goes to the platform and stops there.

## What a Fix Looks Like

**Maintain the authorised seller list properly.** Current, complete, integrated into review. A large share of wrongful actions against legitimate sellers would be prevented by this one thing, and it is a data maintenance problem shared with the brand.

**Route the lawful categories away from the counterfeit queue.** Apparent resale, repair, compatible parts and commentary handled through a separate path with a higher evidence bar and legal review. They require different judgement and currently receive the same three seconds.

**Require a structured rationale.** The reviewer states the basis. Seconds to record, and it makes the determination reviewable and the appeal evaluable — currently an appeal contests a decision whose reasoning nobody recorded.

**Measure the wrongful-action rate.** Sample actioned listings and re-review with full context. This is the number the industry lacks and it would very likely be large enough to change behaviour.

**Get appeal outcomes back from platforms.** A reversal is the strongest signal available and it currently reaches nobody at the firm. Requesting it is straightforward and no firm does.

**Remove the throughput target from contested categories.** A reviewer deciding a repair-service listing should not be under the same speed expectation as one clearing an obvious replica.

**Give the seller a route to the filer.** An affected seller should be able to reach the party that filed the notice, not only the platform. This is both fairer and the fastest route to the firm learning about its own errors.

## Who Feels the Pain

The legitimate seller — a reseller, a repairer, a small business — whose listing and sometimes whose livelihood is removed on a determination made in seconds from a photograph, contested through a process designed for someone with lawyers.

The reviewer, asked to make legal determinations at speed without the information that would settle them, and measured on volume.

The brand, which bears the reputational cost when a wrongful action becomes public, and receives a takedown count that does not distinguish.

And the counterfeit operators, who are under-detected relative to the naive listings that match cleanly and are the ones filling the queue.

## Impact If Fixed

A current authorised seller list is a data problem shared with the brand and would prevent a large share of the most damaging errors on its own.

Routing lawful categories to a separate path with legal review directly addresses where the harm originates, and it is a routing change rather than a new capability.

And measuring the wrongful-action rate would create the accountability that currently does not exist anywhere in this chain — for a harm that is documented, recurring, and borne entirely by parties with no voice in the process.
