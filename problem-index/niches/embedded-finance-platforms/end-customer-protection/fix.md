# Nobody to Call

**Niche:** [[niches/embedded-finance-platforms/end-customer-protection/profile|End-Customer Protection]]
**Industry:** [[industries/embedded-finance-platforms|Embedded Finance Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The customer's funds are frozen, the app's support form goes unanswered, and there is no second number to try.
**Tags:** #worker-facing #compliance #workflow-orchestration #quick-win #automation #evaluation-metrics #descriptive-statistics #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to guarantee the end customer's baseline protections — access to funds, disputes, disclosures, error resolution — regardless of which programme they signed up with, and whoever makes those protections a property of the platform rather than of the programme takes the risk the whole category carries.

## The Problem
The customer's paycheque landed in an account they cannot access. They contact the app's support and get an automated acknowledgement. They do not know the bank's name, and if they find it the bank has no record of them by name. The platform, which can see the freeze and the balance and the silence, is invisible to them and has no intake for them. The escalation path that exists is a journalist or a regulator, which is how these cases actually get resolved.

## Why It's Still Broken
Support was contracted to the programme, so a route to the platform looked like undermining the customer's product — the design decision was deliberate and its failure mode was never priced. The platform does not hold the customer relationship or, in many cases, contact details. Volume is feared. And cases resolve eventually through channels nobody counts, which keeps the problem looking rare.

## What a Fix Looks Like
Build the second route and watch the first. Detect the stuck case from the data — funds frozen, no state change, no resolution, days elapsed — which is the fix and requires no customer contact at all, because the silence is visible. Escalate to the programme automatically with a deadline, since most cases are neglect rather than refusal and a prompt resolves them. Act when the deadline passes, because an escalation with no consequence is where this currently stops. Provide a documented route for the customer to reach the platform, which is the missing piece and is a policy choice rather than a build. Publish who the bank is and how to reach it, since the customer cannot exercise a right they cannot locate. Measure time-to-resolution per programme, as that single number identifies the operators who need attention. Flag the programme whose stuck-case rate is rising, because that is the leading indicator of a failing operator. Handle the dark programme explicitly, since its customers currently have nobody at all. Track how cases actually get resolved today, which will show how many needed outside pressure. And report the numbers to sponsor banks, who carry the exposure and cannot currently see a single one of these cases.

## Who Feels the Pain
Customers locked out of their own money; support staff at programmes without the authority to fix it; sponsor banks whose names appear in the eventual complaint; and platforms discovering the case when it is already public.

## Impact If Fixed
The design decision to route everything through the programme was deliberate and its failure mode was never priced. The stuck case is detectable from silence in data the platform already holds, before anyone needs to call.
