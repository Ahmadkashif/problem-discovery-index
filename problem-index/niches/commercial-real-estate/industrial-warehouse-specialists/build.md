# Industrial Site Selection Scoring Engine

**Niche:** [[niches/commercial-real-estate/industrial-warehouse-specialists/profile|Industrial & Warehouse Specialists]]
**Industry:** [[industries/commercial-real-estate|Commercial Real Estate]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool scores industrial properties against a specific tenant's physical and logistical requirements — clear height, dock doors, power, interstate proximity, last-mile zone coverage — the way an experienced industrial broker does mentally when matching tenants to buildings.
**Tags:** #gradient-boosting #tacit-knowledge-ml #revenue-impact #data-integration

## The Problem
When a logistics company needs a 150,000 sq ft distribution center with 32-foot clear height, 20 dock doors, and within 5 miles of Interstate 85 in the Charlotte market, the experienced industrial broker immediately narrows to 3-4 buildings from their memorized inventory. A junior broker searches CoStar by square footage and location, producing 20+ results that require manual filtering by physical specifications not reliably tracked in CoStar's database. The experienced broker's instant narrowing — combining physical specs, truck court adequacy, power availability, and zoning — represents tacit knowledge developed over hundreds of site tours and tenant requirement conversations.

## Why Nobody Has Built This
Building specification data (clear height, dock doors, column spacing, power capacity) is inconsistently captured in CoStar and often inaccurate. Accurate spec data requires field verification or ingestion from property condition reports and building plans — documents that exist but aren't digitized in a queryable format. Zoning compatibility requires parsing municipal code, which varies by jurisdiction. The data assembly challenge has deterred CRE tech companies focused on office and multifamily where building specs are simpler.

## What to Build
A specification-matching engine that maintains verified building spec profiles (ingested from listing brochures, property condition reports, and broker-verified data) and scores each property against a tenant's requirement set. Inputs: tenant requirements (size, clear height, dock doors, power, proximity constraints). Outputs: ranked property shortlist with spec-match score, deviation details per requirement, and logistics proximity metrics. Integration with CoStar listing data for availability status.

## Target Customer
Industrial brokerage teams at boutique and mid-size firms serving mid-market tenants (50,000-500,000 sq ft requirements) — approximately 2,000-3,000 teams nationally. Average contract value: $400-$800/month per team.

## Impact If Built
Reduces site selection from 2-3 days of manual filtering to 30 minutes of scored shortlist review. For an industrial broker earning $200,000-$500,000 in annual commission, recovering 15-20 hours per month of manual search time enables 2-3 additional transactions per year.
