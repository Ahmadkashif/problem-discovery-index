# Lineage: Game LiveOps Services

**Industry:** [[industries/game-liveops-services|Game LiveOps Services]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** the battle pass — first shipped as Valve's Dota 2 "Compendium" in May 2013, a time-limited purchasable pass whose rewards unlocked over a season and a quarter of whose revenue went into The International's prize pool
**Builder:** Valve
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A free game has to be paid for by something other than the game.

Dota 2 was, and is, fully free-to-play: no hero or gameplay element has to be bought. Its revenue came from a store of cosmetic items — armour, weapons, couriers — each purchase a one-off decision by one player about one object. That model has two weaknesses a live operator feels every month. Revenue is lumpy, tracking whatever the store happens to have that week. And nothing in a single cosmetic sale gives a player a reason to come back tomorrow.

Valve also had a second, very specific bill. It ran The International, its own world championship, and had set the base prize pool at $1.6 million for 2013. A prize pool is pure cost to a game company unless the audience can be made to fund it.

## What Got Built

In May 2013 Valve put an item in the Dota 2 store called **the Compendium**.

Buying it gave a player an in-game book tied to the tournament, carrying exclusive cosmetics and other bonuses unavailable elsewhere. The load-bearing clause: **25 percent of all Compendium revenue was added to the prize pool.** The pool, starting from $1.6 million, ended above $2.8 million — at the time, the largest in esports history. The tournament itself ran 7–11 August 2013 at Benaroya Hall in Seattle.

Strip away the tournament and the mechanic is the one every live game now runs: **a pass bought once, valid for a fixed window, whose rewards are released progressively and expire with the window.** Fortnite Battle Royale adopted the idea under the name "Battle Pass" from its second season in late 2017, and that is the name that stuck.

## Who Built It, And Why Them

Valve, because it was the only company that owned all three pieces at once: a free-to-play game, a digital store, and a tournament with a prize pool it wanted grown.

The Compendium is shaped by that combination. The **revenue share** exists because the pool needed a funder other than Valve. The **seasonal window** exists because the tournament had a date. The **progressive unlock** exists because the product had to keep paying out between purchase in May and the finals in August. A studio without an esports event would not have invented a pass that ends on a fixed day; a tournament organiser without a game store could not have sold one.

I found no statement from Valve naming the individuals who designed the Compendium, and do not name any.

## What It Cost

**The pass converts a design problem into a calendar.** Once revenue is booked per season, the season has to exist — and the next one has to beat it. The window that made sense because a tournament had a finals date became, in games without tournaments, a treadmill with no reason to stop.

It also moved the currency problem inside the pass. Rewards that unlock progressively are faucets on a schedule: every season injects a fixed tranche of currency, cosmetics and boosts, whatever the economy's state. Dota 2 itself later introduced a monthly subscription, Dota Plus, that per Wikipedia replaced the seasonal battle passes tied to Major tournaments.

## What You Still Touch

Any game with a numbered season and a tier track you are "behind" on is running Valve's 2013 mechanic without the tournament that justified its end date.

- [[problems/game-liveops-services/low-impact-1|🟡 Event Calendar and Content Cadence]] — the season the pass requires
- [[problems/game-liveops-services/high-impact|🔴 Tuning an Economy Whose Failure Appears Three Months Later]] — the scheduled faucet
- [[problems/game-liveops-services/worker-life-1|🟢 The Live Ops Manager and the Game That Never Stops]]
- [[niches/game-liveops-services/season-and-content-cadence/profile|Season & Content Cadence]]
- [[niches/game-liveops-services/inflation-detection/profile|Inflation Detection]]

**Sources:** Wikipedia, *The International 2013* (May 2013 Compendium launch, "a quarter of the total revenue" to the $1.6 million base pool, final pool over $2.8 million, 7–11 August at Benaroya Hall); Wikipedia, *Battle pass* ("one of the first known examples", 25% of revenue, Fortnite adopting "Battle Pass" from its second season, Team Fortress 2 campaign passes 2015); Wikipedia, *Dota 2* (free-to-play and cosmetic store, Dota Plus replacing seasonal passes). ⚠️ **Not established:** the Compendium's 2013 price; the named Valve designers; whether the 2013 Compendium carried prize-pool stretch goals, a feature commonly associated with later passes but which no source I reached attributes to the first one (Dota 2 fandom wiki returned 402, Liquipedia 403); the exact start date of Fortnite's Season 2 (given only as "late 2017"); whether Valve ended the TI battle pass in 2023, which I recall but could not confirm. WebSearch was unavailable this session (session budget exhausted); research used WebFetch on known URLs only.
