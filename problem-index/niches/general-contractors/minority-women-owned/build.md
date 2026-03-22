# Set-Aside Contract Finder & Bid Opportunity Matcher

**Niche:** [[niches/general-contractors/minority-women-owned/profile|Minority/Women-Owned Contractors]]
**Industry:** [[industries/general-contractors|General Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** DBE/MBE/WBE contractors see every government set-aside and subcontracting opportunity they're qualified for — matched to their certifications, bonding capacity, trade specialties, and geographic range — instead of manually searching 15 different procurement portals.
**Tags:** #large-language-models #transformers #feature-engineering #automation #data-integration #revenue-impact

## The Problem
A certified DBE electrical contractor in Atlanta must monitor SAM.gov for federal set-asides, the Georgia DOT procurement portal for state DBE opportunities, Fulton County's procurement system for local set-asides, and the city of Atlanta's vendor portal — plus watch for prime contractor solicitations on Dodge Data, ConstructConnect, and trade association job boards. Each portal has a different interface, different search taxonomy, and different notification system. The contractor spends 5-10 hours per week scanning these portals and still misses opportunities because the search tools are keyword-based (searching "electrical" misses listings described as "power distribution" or "low-voltage systems"). Meanwhile, prime contractors seeking DBE subcontractors to meet their goals can't efficiently find qualified DBE firms — they rely on outdated certification directories and personal networks.

## Why Nobody Has Built This
Three barriers: (1) procurement data is fragmented across hundreds of federal, state, and local portals with no standard API or data format — aggregation requires building and maintaining scrapers for each source; (2) matching requires understanding both the certification landscape (which certifications qualify for which set-asides — SBA 8(a) vs. state DBE vs. city MBE are not interchangeable) and the construction domain (matching a contractor's capabilities to opportunity requirements using trade-specific terminology); (3) the target market is small firms with limited software budgets, making the unit economics challenging for traditional SaaS. The combination of high data aggregation cost and low willingness to pay has kept venture-backed startups away.

## What to Build
A procurement intelligence platform for certified contractors that: (1) aggregates set-aside and subcontracting opportunities from federal (SAM.gov, GSA), state (all 50 state DOT and procurement portals), and major municipal procurement systems; (2) maintains a contractor profile including certifications held (with certifying agencies), bonding capacity, trade specialties, geographic range, and past performance; (3) matches opportunities to the contractor's profile using semantic understanding of construction scopes (not just keyword matching); (4) scores each opportunity by win probability based on the contractor's size relative to the contract, past experience with the agency, and competition level; (5) provides a two-sided marketplace where prime contractors seeking DBE subcontractors can search by certification, trade, location, and bonding capacity. Revenue model: contractor subscription ($99-299/month) plus prime contractor search fees.

## Target Customer
DBE/MBE/WBE certified construction contractors ($1-15M annual revenue) who currently spend 5-10 hours per week manually searching procurement portals and missing qualified opportunities. Secondary market: prime contractors on government projects who need to find and engage qualified DBE subcontractors to meet contract goals.

## Impact If Built
Increases qualified bid opportunities per firm by 3-5x by surfacing matches the contractor would never have found through manual portal searching. Reduces business development time from 5-10 hours to 1-2 hours per week. For prime contractors, reduces DBE sub-sourcing time from days to hours and improves DBE goal compliance by matching them with genuinely qualified firms rather than paper-only participants.
