# State UST Notification and Testing Deadline Tracking

**Niche:** [[niches/environmental-consultants/underground-storage-tank-specialists/profile|Underground Storage Tank Specialists]]
**Industry:** [[industries/environmental-consultants|Environmental Consultants]]
**Type:** Fix (Pain Point)
**One-liner:** Every state UST program has different notification deadlines, testing intervals, and compliance requirements — consultants working across state lines must maintain separate compliance calendars for each state, and a single missed deadline triggers violations starting at $10,000/day.
**Tags:** #compliance #automation #workflow-orchestration #worker-facing

## The Problem
UST compliance requirements vary significantly by state: some states require annual tank tightness testing, others require it every 3 years; notification deadlines for suspected releases range from 24 hours (California) to 30 days; cathodic protection survey intervals vary from annual to triennial; operator training requirements differ in scope and renewal frequency. A consultant managing facilities in 3-5 states must track these varying requirements without confusing which state's rules apply to which facility. The compliance calendar for a 100-facility portfolio across 3 states contains 800-1,200 individual deadlines per year. Missing one can result in five-figure penalties.

## Why It's Still Broken
No centralized, machine-readable database of state UST compliance requirements exists. EPA publishes federal minimum requirements, but states often exceed them, and the state-specific requirements are scattered across state administrative codes, guidance documents, and program websites. Tracking requirement changes requires monitoring each state's UST program announcements — a state may change its testing interval or notification deadline with 60-90 days' notice. The consultant learns about changes through industry associations, state newsletters, or (worst case) when they receive a violation notice.

## What a Fix Looks Like
A state UST requirements database that maps every compliance obligation (test type, interval, notification deadline, operator training requirement, financial assurance method) to each state program. When the consultant registers a facility, the system auto-generates the compliance calendar based on the facility's state, tank installation dates, and product types. Changes to state requirements are monitored and pushed as alerts: "Florida has changed the SIR reporting interval from monthly to quarterly, effective January 1 — your 12 Florida facilities have updated compliance calendars." The database is maintained by a central service rather than each consultant independently.

## Who Feels the Pain
UST consultants operating across state boundaries who must manually research and track different compliance requirements for each state — particularly those expanding into new states where they don't yet know the program's specific rules.

## Impact If Fixed
Prevents the 2-5 violations per year that a typical multi-state UST consultant experiences due to tracking errors, each costing $10,000-50,000 in penalties plus client relationship damage. Saves 5-10 hours/month of manual compliance calendar maintenance.
