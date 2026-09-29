# Content Currency Is Promised and Never Measured

**Niche:** [[niches/customs-brokers/global-trade-content-databases/profile|Global Trade Content Databases]]
**Industry:** [[industries/customs-brokers|Customs Brokers]]
**Type:** Fix (Pain Point)
**One-liner:** Subscribers file entries against duty rates on the assumption the content is current, and the publisher has no per-field measure of how current it actually is.
**Tags:** #survival-analysis #change-point-detection #confidence-intervals #evaluation-metrics #descriptive-statistics #probability-distributions #compliance #data-integration #workflow-orchestration #worker-facing

## The Problem
The product's single promise is currency, and it is unquantified. Content is refreshed on a cycle mixing automated collection, analyst review, and reactive correction when someone reports a discrepancy. Some fields for some jurisdictions are updated within hours of a change; others have not been verified in a year. The subscriber cannot tell the difference — every rate is displayed identically — and files entries against all of them with equal confidence. When content is stale, the consequence lands entirely on the subscriber as a rejected entry, a penalty, or an underpayment discovered at audit years later, and it lands without warning because nothing indicated the figure might be old.

## Why It's Still Broken
The product was built as a reference database, and reference databases display values. Provenance is captured internally for quality management, in a form meaningful to analysts and not to subscribers. Commercially, definitiveness has been the positioning — a competitor's bake-off compares coverage counts, not staleness distributions — and there has been a reasonable fear that publishing currency metrics invites scrutiny of the weakest jurisdictions. Meanwhile nobody outside can measure it, so nobody has demanded it.

## What a Fix Looks Like
Currency as a measured, surfaced property of every field: when it was last verified, by what method, against which source, and — where the field's underlying rule changes on a predictable cadence — an estimate of the probability it is currently stale. Presented simply enough for a broker to act on in seconds, with detail available. Downstream, currency travels with the data through exports and interfaces, so a rate consumed by a customer's own system does not arrive stripped of the caveat. Internally the same measurement turns staleness into an operational metric that verification effort can be allocated against, which is how the improvement compounds: coverage investment currently goes where volume is, and should go where staleness risk multiplied by subscriber exposure is highest. And the honest reporting of currency by jurisdiction is a differentiator rather than a confession, because every competitor has the same problem and none of them can talk about it.

## Who Feels the Pain
Brokers and importers filing entries against rates of unknown age; compliance teams who discover an underpayment at audit and cannot show they exercised reasonable care; content analysts whose careful verification is displayed identically to a stale carry-forward; and the publisher, whose entire proposition is a currency claim it currently asks subscribers to take on faith.

## Impact If Fixed
Converts the product's biggest unstated risk into its clearest differentiator, using data already held internally. It also gives importers something they genuinely need for the reasonable care standard customs administrations expect — evidence about the reliability of the data they relied on — which turns a data subscription into part of a compliance defence.
