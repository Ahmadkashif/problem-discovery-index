# The Store Manager Walking Six Hundred Doors

**Industry:** [[self-storage-operators|Self-Storage Operators]]
**Type:** Worker Life Changing
**One-liner:** A store manager working alone walks every hallway with a clipboard to check that each door matches the ledger. Telling them which doors to check gives back hours each week and keeps them out of empty corridors at closing time.
**Tags:** #worker-facing #cnns #object-detection #hidden-markov-models #automation #quick-win

## The Problem
Most self-storage facilities have one manager on site, sometimes shared with a second store. Between rentals, payments and phone calls, that manager owes the company a lock check. They walk every drive aisle and hallway and compare each door to the ledger. A vacant unit should be open or company-locked. A rented unit should carry the tenant's lock. A delinquent unit should carry the company's overlock. A unit that should be empty but has a lock on it is a squatter, a tenant who moved without paying, or a mistake that costs rent every month. An overlocked unit standing open may mean a break-in or a tenant who cut the overlock. A rented unit with no lock is an insurance claim waiting to happen.

On a 600-unit facility the walk takes hours. Multi-storey stores mean elevators and long climate-controlled corridors, and drive-up stores mean walking the whole site in summer heat. The results go on a paper sheet and are typed into Sitelink or Storable Edge later, if at all. Then there is the rest of the walk: dumped mattresses, a leaking roof over row C, a unit that smells wrong, a person who seems to be living in a unit. Many managers do the check at the end of the day, when the site is quietest and they are most alone.

## Why It Matters to the Worker
The check is the part of the job nobody sees until it goes wrong. If the manager misses a locked vacant unit, the district manager finds it on an audit and the variance is theirs. If they find someone living in a unit, they handle it alone. Public Storage says most of its new hires join as property managers with no industry experience, so a new manager learns which doors matter by walking all of them. The work is physically tiring and repetitive, and it competes with the customer service the manager is scored on.

## What a Solution Looks Like
A check list that tells the manager which doors to look at, built from data the store already holds. Smart locks such as Nokē Smart Entry and unit sensors such as OpenTech's SmartMotion report door and lock events. Gate codes show who entered and when. The ledger shows what each unit should be. A model flags only the doors where these disagree: a "vacant" unit whose door opened last night, a "rented" unit with no access in 14 months and a failed autopay, an overlocked unit with motion inside. Where there are no smart locks, the manager walks with a phone camera. A vision model reads lock type and position on each door photo and fills in the sheet. The manager gets a short route instead of the whole building, and a record that the check was done.

## Impact If Solved
If a full check of ~400–700 doors takes ~3–6 hours a week (estimate) and a flagged list covers the 20–40 doors that matter, the manager gets back ~2–4 hours a week. Each locked vacant unit found a month earlier recovers a month of rent, ~$100–150 for a 10x10 (estimate). The manager also stops walking the whole building alone at closing time.
