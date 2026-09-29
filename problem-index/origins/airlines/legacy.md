# Legacy: What Airlines Bequeathed

**Origin:** [[origins/airlines/profile|Airlines]]

## The Direct Inheritance

Revenue management moved, essentially unchanged, into every business with perishable inventory and heterogeneous willingness to pay.

| Child | What it inherited |
|---|---|
| [[industries/hotels-boutique\|Boutique Hotels]] | Room-nights are seats. The same protection-level logic, same fare fences, same customer resentment. Hotel revenue management is a direct transplant. |
| [[industries/short-term-rentals\|Short-Term Rentals]] | Dynamic pricing tools sold to hosts are Littlewood's rule with a friendlier interface — and, per the vault's own notes, frequently without the demand forecast that makes it work. |
| [[industries/charter-bus-operators\|Charter Bus Operators]] | Perishable seats, no revenue management, and the vault records the gap. |
| [[industries/freight-brokerage\|Freight Brokerage]] | Lane pricing is the same shape: perishable capacity, heterogeneous shippers, a margin that depends on withholding. `problems/freight-brokerage/high-impact.md` is a yield-management problem that does not know its own ancestry. |
| [[industries/rideshare-fleet-operators\|Rideshare Fleet Operators]] | Surge pricing is yield management run in minutes instead of months. |

## The Second Inheritance: the distribution fight

SABRE did something its builders did not intend. By becoming the system travel agents used to book *any* airline, it turned American Airlines into the owner of a distribution channel its competitors depended on — and American was found to have biased screen displays toward its own flights, a practice that drew regulatory attention and a name: **screen-bias**.

That is the first clear instance of a pattern this vault documents everywhere: **the platform that intermediates a market can advantage itself inside that market, and will, until told otherwise.** Retail media networks, app stores, marketplace private labels and ad exchanges are all replaying it.

The GDS layer that grew out of SABRE then became its own industry — and then the fight over who controlled distribution moved to the web, which is [[origins/online-travel-agencies/profile|Online Travel Agencies]].

## The Third Inheritance: the measurement asymmetry

Yield management gave the seller a precise model of the buyer's willingness to pay while the buyer got a price with no explanation. The airline knows why the fare is £412 today. The passenger cannot find out, cannot appeal, and cannot verify.

That asymmetry was novel in 1985 and is now the default condition of consumer commerce. It is the distant ancestor of the vault's **asymmetric hold** — the difference being that in 1985 it was pointed at customers, and by 2015 the same apparatus was pointed at workers. See [[series/eras/wave-08-mobile-gps|Wave 8]].

## What an Episode Should Take From This

Three things, in order of usefulness to a fresh graduate:

1. **The infrastructure arrived 25 years before the weapon.** SABRE went nationwide in 1964; DINAMO shipped in 1985. The capability sat there, unexploited, while everyone could see it. Being early to infrastructure is not the same as being early to advantage.
2. **American won by solving a problem its competitor could not even attempt.** Not by doing the same thing better — by doing something structurally unavailable to the other side. That is what a real moat looks like.
3. **The mathematics was public and the data was not.** Littlewood's rule was published in 1972. Anyone could read it. What American had was thirty years of booking history and a real-time inventory system. **This is the single most transferable lesson in the vault.**

**Sources:** See [[origins/airlines/the-mechanism|The Mechanism]] and [[origins/airlines/the-fight|The Fight]] for full citations; US DOT rulemaking on CRS display bias (1984 onward) for the screen-bias record.
