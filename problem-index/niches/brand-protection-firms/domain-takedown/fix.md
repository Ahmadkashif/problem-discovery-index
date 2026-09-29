# Fix: Taken Down After the Campaign Finished

**Niche:** Domain & Phishing Takedown
**Industry:** [[industries/brand-protection-firms|Brand Protection Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The takedown is reported as a success and the domain had already collected everything it was going to collect.
**Tags:** #evaluation-metrics #confidence-intervals #survival-analysis #change-point-detection #automation #revenue-impact
**Contested on:** Whether a malicious domain is removed fast enough to matter.

## The Problem

The report says the domain was taken down in thirty-one hours, which compares well against the industry.

The campaign ran for six. A phishing page's victim interactions are heavily concentrated in the first hours after the messages go out, because that is when people read email. By hour thirty-one the operator had already moved on and the domain was disposable.

So the takedown removed an abandoned asset and is counted as an enforcement success. The harm it was meant to prevent had already occurred, and nothing in the report distinguishes a takedown at ninety minutes from one at three days except a number that both parties treat as good.

The metric compounds the problem. Because time to takedown is reported, and because takedown is slow by nature, the whole operation optimises around a channel that cannot be fast enough. The channels that could be fast — blocklists, email security, customer warning — are supplementary because they do not produce a takedown.

Nobody in the chain is measuring the thing that matters, which is how many users were exposed before protection reached them.

## Why It's Still Broken

**Takedown is the deliverable.** The contract counts removals, so removal is the action, and its speed is bounded by third-party abuse queues.

**Exposure is not measured.** Nobody counts how many users visited the page before it was blocked or removed, though the brand's own fraud data and the blocklist telemetry would bound it.

**Registrar response times are outside anyone's control.** Firms can submit quickly and cannot make a registrar act quickly, which encourages treating the delay as a fixed cost.

**Detection latency is unexamined.** Time to takedown starts when detection surfaces the domain, which hides however long it took to detect. The full clock from registration to protection is rarely reported.

**Blocklist protection is invisible.** A blocklist entry protects users and produces no artefact the brand can see, so it is undervalued relative to a removal.

**Thirty-one hours sounds acceptable.** Without the campaign duration alongside it, the number reads as prompt rather than as far too late.

## What a Fix Looks Like

**Report time to protection, not time to takedown.** From first observation to the point where users are protected by any means — blocklist, email block, DNS filter, removal. This measures the harm and would immediately reveal that the blocklist path is the one that matters.

**Report the full clock.** Registration to detection, detection to submission, submission to protection, submission to removal. This exposes where the delay actually is, which is frequently detection rather than the registrar.

**Estimate exposure.** Visits before protection, bounded from blocklist telemetry, the brand's own fraud reports and where available the hosting provider's data. An exposure estimate makes the speed metric meaningful.

**Submit to blocklists first, always.** Before the takedown request, not after. This is a sequencing change with no cost that would protect users hours earlier on every incident.

**Warn the brand's customers directly.** Where a campaign targets a specific customer base, the brand can warn them immediately. This is frequently the fastest protection available and is rarely used because response is owned by the enforcement vendor.

**Measure registrar and host performance.** Median time to action per provider, tracked, so submissions route to the faster path and the slow ones face a published record.

**Detect earlier.** Certificate transparency and registration feeds surface domains before weaponisation. Time spent improving detection latency is worth more than time spent chasing a registrar.

## Who Feels the Pain

The users who entered credentials or payment details during the hours between the campaign starting and protection arriving.

The brand, absorbing the fraud losses and the customer harm, while receiving a report of a successful takedown.

The security team, who understand the timing perfectly and receive a metric that does not reflect it.

And the takedown operation itself, working hard at a channel whose structural latency means it can rarely arrive in time.

## Impact If Fixed

Reporting time to protection rather than time to takedown aligns the metric with the harm, and it is measurable immediately by any firm willing to report it.

Submitting to blocklists before filing the takedown is a free sequencing change that protects users hours earlier on every single incident.

And reporting the full clock from registration to protection would show that the delay is frequently in detection rather than in the registrar — which is the part the firm actually controls and currently does not measure.
