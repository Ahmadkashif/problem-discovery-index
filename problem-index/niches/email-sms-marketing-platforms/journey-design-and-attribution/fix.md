# The Branch That Has Not Fired Since 2022

**Niche:** [[niches/email-sms-marketing-platforms/journey-design-and-attribution/profile|Journey Design & Attribution]]
**Industry:** [[industries/email-sms-marketing-platforms|Email & SMS Marketing Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A condition changed upstream and three branches became unreachable, which nobody noticed because an unreachable branch produces no error and no revenue line.
**Tags:** #change-point-detection #evaluation-metrics #automation #descriptive-statistics #quick-win #workflow-orchestration #compliance #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to tell a brand which branches of its automated journeys earn anything — and whoever does that turns a hand-drawn rule tree into something that can be improved.

## The Problem
Someone renamed a customer property, or changed a segment definition, or a data source stopped populating a field. Three branches of a journey now evaluate false for everyone and have not fired since. There is no error, no alert and no gap in any report, because a branch that never fires simply produces nothing — and nothing looks identical to a branch that fires rarely. The brand discovers it when someone asks why win-back revenue is down and traces it back through a diagram nobody has read in two years. Between the break and the discovery, months of intended messages were never sent.

## Why It's Still Broken
An unreachable branch is a silent failure and the platform's monitoring is built around delivery errors, which this is not — a failure that produces no output produces no signal, which is the whole mechanism. Journeys are edited by several people over years with no dependency tracking between properties and conditions. Nobody audits a flow after building it. And the revenue simply does not appear, which is invisible in a report of what did.

## What a Fix Looks Like
Monitor the journeys for silence. Alert on any branch whose firing rate drops sharply or to zero against its own history, which is the fix, requires only the firing counts the platform already records, and catches this within a day. Validate references when anything upstream changes, so renaming a property surfaces the journeys that depend on it before it breaks them. Report entry and branch volumes as a standing health view, since a journey's shape is currently invisible without opening the diagram. Track dependencies between data fields, segments and journey conditions, which is the structural fix and prevents the class of failure rather than detecting it. Flag branches that have never fired since creation, which are usually a construction error nobody noticed at launch. Alert on the opposite too, since a branch suddenly firing for everyone is the same class of failure with a louder consequence. Require review of journeys touched by a schema change, which is a simple process gate. Show the last-fired date on every branch in the builder, which makes staleness visible at the moment someone is editing. Keep version history with the reason for each change, since these structures are edited by people who leave. And report the estimated revenue of messages not sent, because a silent failure with a number attached gets fixed and one without does not.

## Who Feels the Pain
Brands losing months of automated revenue silently; lifecycle marketers tracing failures through diagrams nobody understands; and customers who stopped receiving messages they had opted in for.

## Impact If Fixed
A branch that never fires produces no output and therefore no signal, while the platform monitors for delivery errors this failure never generates. Alerting on firing-rate collapse uses counts already recorded and catches within a day what currently takes months.
