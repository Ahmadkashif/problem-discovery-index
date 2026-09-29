# Unit Turn & Make-Ready Sequencing

**Parent Industry:** [[industries/proptech-platforms|Proptech Platforms]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in turn operations is fighting to get a vacant unit from move-out to rent-ready in the fewest days across five vendors who do not talk to each other — and whoever cuts days-vacant most takes the account.

## Profile
**Market Size:** ~$1B US spend across turn management, vendor coordination and make-ready operations software
**Share of Parent Industry:** ~9% of proptech revenue
**Digital Adoption:** Medium — inspections are digitised, sequencing is a site manager on the phone
**Target Buyer:** Regional and site managers, VPs of Operations, and the turn-services companies selling into them
**Automation Potential:** Very High — this is dependency-constrained scheduling against a daily cost, which is a solved class of problem

## What Makes This a Distinct Niche
The moment a resident moves out, a clock starts and every day costs a day's rent plus the leasing effort to backfill. Between move-out and rent-ready sits a sequence: inspection, any repairs, painting, flooring, appliance work, cleaning, punch and final inspection — performed by different vendors with their own schedules, some of which strictly depend on others finishing, several of which can overlap and usually do not. The site manager coordinates it by telephone, chasing each vendor and discovering delays after they have happened. It is a dependency-constrained scheduling problem with a known daily cost, which is among the most thoroughly solved classes of problem in operations research, and it is performed by the busiest person on site with a notebook. What makes it terminal under the filter is that the outcome metric is unambiguous and universally tracked: days vacant.

## Current Tools & Gaps
Inspection apps with photo capture are widely deployed and genuinely useful. Turn management modules exist in the major platforms and are largely checklists with dates. Turn-services companies have grown as an outsourced alternative, which moves the coordination burden rather than removing it. Vendor scheduling is phone and text. The gaps are specific: nothing models the dependency structure, so overlaps that could be run in parallel are run in series out of caution; nothing predicts scope or duration from the move-out inspection, so the turn's length is unknown until it is over; nothing detects a vendor slipping until the next step's vendor arrives to a unit that is not ready; and nobody measures which part of the sequence actually consumes the days, so operators attack turn time with exhortation rather than with a diagnosis.

## Problems
- [[niches/proptech-platforms/unit-turn-makeready/build|🔨 Build: The Turn Scheduled as the Dependency Graph It Is]]
- [[niches/proptech-platforms/unit-turn-makeready/buy|🛒 Buy: Project Scheduling Tooling Applied to a Five-Day Project]]
- [[niches/proptech-platforms/unit-turn-makeready/fix|🔧 Fix: Days Vacant With No Decomposition]]
