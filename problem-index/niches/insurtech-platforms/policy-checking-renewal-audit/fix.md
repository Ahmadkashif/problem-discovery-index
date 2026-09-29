# Most of the Book Is Never Checked at All

**Niche:** [[niches/insurtech-platforms/policy-checking-renewal-audit/profile|Policy Checking & Renewal Audit]]
**Industry:** [[industries/insurtech-platforms|Insurtech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Agencies check the policies they have capacity to check, which is the largest accounts, and nobody records what was checked, what was found, or what the unchecked remainder is worth in exposure.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #compliance #workflow-orchestration #quick-win #automation
**Contested on:** Every serious competitor in policy checking is fighting to detect every material difference between an expiring policy, what was requested, and what the carrier actually issued — and whoever catches the most differences without a person reading both documents takes the account.

## The Problem
An agency's policy checking procedure says every policy is checked. Its actual practice is that accounts above a premium threshold are checked thoroughly, accounts in the middle receive a glance at the declarations page, and the small ones are filed. Nobody records which treatment each policy received, so the agency cannot state its own coverage, cannot show a carrier or an errors and omissions insurer what its procedure actually is, and cannot tell whether the differences it does find are concentrated in particular carriers or classes — which would tell it where to focus the capacity it has.

## Why It's Still Broken
The gap between the stated procedure and the practice is uncomfortable to document, which is a substantial reason nothing records it — writing down that four hundred policies were not checked creates a record of a known exposure. Checking findings are also handled as individual corrections with the carrier rather than as data, so the pattern across findings is invisible. And there is no natural owner: the procedure belongs to operations, the exposure belongs to the principal, and the work belongs to whoever has time.

## What a Fix Looks Like
Record what was done and what was found, then use it to allocate the capacity. Every renewal carries a check status — full, declarations only, none — with the reason, which takes a tap and produces an honest picture of coverage. Findings are recorded structurally: what differed, which carrier, which class, how it was resolved. Within a quarter the agency knows which carriers introduce the most unrequested changes at renewal, which is both a prioritisation signal and a conversation to have with the carrier. Prioritise the checking capacity by exposure rather than by premium — a small account with high liability exposure and a carrier with a poor change record deserves the check more than a large account with a clean history — which is a better allocation than the one premium size produces. And the honest coverage number is the argument for the automation in the build note, because an agency that can state how much of its book goes unchecked can justify fixing it.

## Who Feels the Pain
Agency principals carrying an exposure whose size they have never computed; service staff triaging by premium because that is the only rule available; and clients on smaller accounts whose policies nobody read.

## Impact If Fixed
Recording check status and findings costs a tap and produces both an honest exposure picture and a prioritisation that is better than premium size. The carrier-level finding pattern is the unexpectedly valuable output — it identifies which markets change terms at renewal without saying so, which is information the agency can act on in placement as well as in checking.
