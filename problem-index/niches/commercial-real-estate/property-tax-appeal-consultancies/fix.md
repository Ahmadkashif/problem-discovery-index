# Deadline Management Is a Spreadsheet Against Statutory Loss

**Niche:** [[niches/commercial-real-estate/property-tax-appeal-consultancies/profile|Property Tax Appeal Consultancies]]
**Industry:** [[industries/commercial-real-estate|Commercial Real Estate]]
**Type:** Fix (Pain Point)
**One-liner:** Appeal rights expire on statutory dates that differ by jurisdiction, trigger off events the firm does not control, and are tracked in spreadsheets — and a missed date is a year of a client's savings gone with no remedy.
**Tags:** #workflow-orchestration #automation #change-point-detection #evaluation-metrics #compliance #data-integration #probability-distributions #worker-facing #descriptive-statistics #revenue-impact

## The Problem
The single largest uncompensated risk in the practice is a calendar problem. Appeal windows are statutory and unforgiving, they vary by jurisdiction and sometimes by property class, and many of them trigger off an event the firm does not control — the mailing date of a notice, the certification of a roll, the publication of a ratio. Tracking runs on spreadsheets and case management reminders maintained by staff who know their own jurisdictions. It works until a jurisdiction changes a date, a notice is delayed or lost, a client portfolio acquisition adds parcels nobody registered, or a consultant leaves. When it fails, the client loses a full year of savings, the firm loses the fee and often the relationship, and there is no appeal from a missed appeal.

## Why It's Still Broken
The knowledge is distributed and personal — each consultant knows their counties — and that has been adequate at small scale and has never been consolidated as the firm grew. Deadlines also depend on facts arriving from outside, so any system must handle the case where the triggering event has not been observed rather than assuming a fixed date, which is more complex than a calendar. And nothing forces the fix: misses are individually embarrassing, absorbed quietly, and never aggregated into a number that would justify the investment.

## What a Fix Looks Like
A jurisdiction rule engine holding appeal windows as rules rather than dates — the triggering event, the interval, the property classes covered, and the procedural prerequisites — evaluated continuously against the portfolio. Every parcel carries a computed deadline with the evidence for it, and critically, an explicit state for parcels where the trigger has not been observed, so an un-received notice surfaces as an open risk rather than as silence. Rule changes are monitored as first-class events, because a jurisdiction shifting a date is the failure mode nobody catches. Escalation runs on lead time and on portfolio value at stake rather than on a uniform reminder, and coverage is reported as a standing metric: what fraction of the portfolio has a confirmed deadline, what fraction is awaiting a trigger, and what is at risk. Near-misses are logged alongside misses, because the near-miss rate is the leading indicator and is currently invisible.

## Who Feels the Pain
Consultants carrying personal responsibility for statutory dates across hundreds of parcels; clients who lose a year of savings with no remedy; practice leaders who cannot quantify an exposure they know exists; and the firm's growth, since expanding into unfamiliar jurisdictions multiplies a risk that is managed by familiarity.

## Impact If Fixed
Eliminates the practice's largest uninsured operational risk and removes the constraint on geographic expansion, which is currently limited by how many jurisdictions the staff personally know. Coverage reporting also converts an unmeasured exposure into a managed one, which matters to the firm's own insurers and to the institutional clients who ask how deadline risk is controlled.
