# Origins — The Eighteen Parents

Industries that sit **above** the vault's 250, not beside them. Each owns a founding computing story that the existing industries inherited.

**Spec:** `series/_plan.md` §6 · **Spine:** `series/_eras.md` · **Build log:** `series/_bookmark.md`

---

## Why these exist

The vault's 250 industries are prospects — places to sell. These eighteen are not. You are not selling an insight engine to Maersk.

They are here because **for the first thirty years of business computing, large enterprises were the only entities that could afford a computer.** Yield management, MRP, barcode scanning, actuarial automation, electronic trading, route optimisation, process control — all of it was invented at scale and trickled down. The vault's 250 industries received that stack. They did not build it.

A history of business computing told only from SMBs and startups is a history with no first act.

**These are teaching cases. They live outside `industries/` deliberately**, so the vault's `industries ↔ problems ↔ niches` parity is untouched and nobody mistakes a parent for a prospect.

## The eighteen

| # | Origin | Wave | Founding event | The contested decision |
|---|---|---|---|---|
| 1 | [[origins/airlines/profile\|Airlines]] | 1 | SABRE live 1960; DINAMO + Ultimate Super Saver 1985 | How many seats do I refuse to sell cheaply today? |
| 2 | [[origins/supermarket-chains/profile\|Supermarket Chains]] | 2 | UPC first scan, June 26 1974, 8:01am | What goes on the shelf, and who pays for the space? |
| 3 | [[origins/retail-banking/profile\|Retail Banking]] | 1 | ERMA in production Sept 14 1959; MICR standard 1956 | How much clerical work can a machine take before it becomes the bank? |
| 4 | [[origins/hospital-systems/profile\|Hospital Systems]] | 7 | HITECH Act, Feb 2009 *(statutory)* | When the penalty arrives before the benefit, what do you actually optimise for? |
| 5 | [[origins/insurance-carriers/profile\|Insurance Carriers]] | 1 | IBM 650-era actuarial computing ~1956; ISO formed April 1 1971 | How much of the pricing calculation do insurers compute together, and how much alone? |
| 6 | [[origins/exchanges-market-makers/profile\|Exchanges & Market Makers]] | 1 → 9 | NASDAQ quotation system, Feb 8 1971; Reg NMS 2005/2007 | When a price is knowable in microseconds, who gets to know it first? |
| 7 | [[origins/telecom-carriers/profile\|Telecom Carriers]] | 4 → 7 | Mozer et al. churn modelling, 1999/2000 | Which subscribers are about to leave, and what does keeping them cost? |
| 8 | [[origins/ocean-shipping-ports/profile\|Ocean Shipping & Ports]] | 2 | SS Ideal-X, April 26 1956 *(pre-computer)* | Do you pay to move the cargo, or to move a box that happens to contain it? |
| 9 | [[origins/semiconductor-fabs/profile\|Semiconductor Fabs]] | 4 | SEMATECH run-to-run CMP control, early 1990s | Which deviation is a real problem, and which is noise you would be foolish to chase? |
| 10 | [[origins/auto-oems/profile\|Auto OEMs]] | 2 | Orlicky formulates MRP c.1964, book 1975 | Push the plan at the floor from a forecast, or let the next station pull? |
| 11 | [[origins/package-carriers/profile\|Package Carriers]] | 2 → 8 | FedEx COSMOS 1979; UPS ORION rollout Oct 2013 | Shortest route between origin and destination, or every package through one sort, every night? |
| 12 | [[origins/credit-bureaus/profile\|Credit Bureaus]] | 1 | FCRA 1970; FICO bureau score Feb 1989 | What an agent believes about a person, or a statistic that does not know their name? |
| 13 | [[origins/online-travel-agencies/profile\|Online Travel Agencies]] | 5 | Expedia Oct 22 1996; Delta's commission cut Feb 9 1995 | What stops a cheap distribution layer becoming a worse gatekeeper than the one you removed? |
| 14 | [[origins/pharma-rd-cros/profile\|Pharma R&D & CROs]] | 4 | FDA 21 CFR Part 11, effective Aug 20 1997 | Can you prove to a regulator, years later, what your system produced — and is that the expensive part? |
| 15 | [[origins/ad-holding-companies/profile\|Ad Holding Companies]] | 9 | The 15% commission, and its erosion; ANA report June 7 2016 | Whose interest does the agency serve, when the media owner is the one paying it? |
| 16 | [[origins/electric-utilities/profile\|Electric Utilities]] | 4 → 8 | Digital EMS from the late 1960s; ARRA AMI grants 2009 | Which generators run, second by second — and which do you dare start or stop? |
| 17 | [[origins/railroads/profile\|Railroads]] | 2 → 4 | TOPS from 1960s; PSR from 1993; PTC mandate 2008 | Wait until the yard is full, or run the schedule regardless? |
| 18 | [[origins/process-manufacturing/profile\|Process Manufacturing]] | 4 | Honeywell TDC 2000, announced Nov 11 1975; Shell's DMC ~1973 | How close to the physical limit do you run, and how much do you trust the model that locates it? |

## Two deliberate irregularities

Both are kept because they teach something the tidy cases do not.

**Ocean shipping's founding event is not a computer.** The container is physical standardisation, and it is what made the later data layer possible — the box became a unit with an identity that a system could track. **Standardisation precedes digitisation.** Three of the first four waves in this spine turn on competitors agreeing a format none of them owned: MICR's E-13B in 1956, the ISO container in 1968, the UPC in 1973.

**Hospital systems' trigger is a statute, not an invention.** HITECH manufactured a software market with money and penalties. Sometimes the best predictor of a software market is a law — and this vault's own blind spot proves the point, since **Epic appears in 92 files as an integration constraint and HITECH in none.**

## Structure

Each origin has five files:

| File | What it holds |
|---|---|
| `profile.md` | What the industry is, who pays, the economics, the contested decision |
| `origin-story.md` | The founding computing event, in narrative depth |
| `the-fight.md` | The competitive contest the technology was built to win — winners and casualties, named |
| `the-mechanism.md` | How the system actually worked: data model, the loop, the algorithm class, the trade-offs taken |
| `legacy.md` | What it bequeathed, linking **down** to the children in `industries/` |

`the-mechanism.md` is the file an FDE should read twice. It is where a commercial question becomes a modelling problem and where the cost of that translation is stated.

## Rejected

Universities, defence primes and federal government. Hard to source, weak transferable pattern, thin FDE relevance.

---

**Created:** 2026-09-18 (Phase 3 · H2)
