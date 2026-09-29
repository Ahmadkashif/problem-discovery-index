# Lineage: Game Porting Studios

**Industry:** [[industries/game-porting-studios|Game Porting Studios]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** the 10NES lockout chip (CIC) — the authentication chip in every licensed NES cartridge, US Patent 4,799,635 — and the platform-holder pre-release approval it enforced, ancestor of today's console certification checklists
**Builder:** Nintendo
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

The problem was not porting. It was that anyone could publish.

The US video game crash of 1983 is usually told as a collapse in demand, but the mechanism was supply: consoles that would run any cartridge, and third parties who shipped low-quality games until the shelves were saturated. Per Wikipedia's summary, US industry revenue fell from over $3 billion to about $100 million between 1983 and 1985.

When Nintendo brought the NES to North America — a test launch in New York on 18 October 1985 — it faced retailers who had been burned. It needed to promise them that what sat on the shelf had been vetted, and it needed that promise to be enforceable against publishers who did not want to be vetted.

## What Got Built

A pair of chips. The **CIC** ("Checking Integrated Circuit"), marketed as 10NES, put a lock in the console and a key in each cartridge. The console's chip, a Sharp 4-bit SM590 microcontroller, checked the cartridge; if the key failed, it reset the CPU about once a second and the game never ran. Nintendo patented it as US 4,799,635.

The chip mattered because of what it gated. Only Nintendo, or its licensees, could make a working key. So only a game Nintendo had approved could run — and approval became a condition of existence rather than a marketing seal. Around it sat the licensing rules: in Japan, per Wikipedia, developers were limited to five Famicom games a year and agreed that **no Famicom game would be adapted to other consoles within two years of release**.

That clause is a written rule about ports, and it forbade them.

## Who Built It, And Why Them

Nintendo, because it was the only party positioned to profit from a gate. A publisher has every interest in shipping more games; a retailer cannot inspect cartridges. The platform holder alone sits at the one choke point every game must pass — the hardware — and can collect a licence fee there. Wikipedia's CIC article is blunt: the chip "prevented third-party developers from producing games without Nintendo's approval, and provided the company with licensing fees."

The design follows the business case. A lockout is useless unless it is hard to copy, hence a patent and a microcontroller rather than a mechanical notch. That the gate was a legal instrument as much as a technical one showed when Atari's subsidiary Tengen reverse-engineered the chip: Nintendo sued, a jury found infringement, and the parties settled.

## What It Cost

**It made the platform holder the final judge of "done."** Every console generation since has kept a pre-release conformance check — known in the trade as Lotcheck at Nintendo, TRC at Sony and TCR at Microsoft — but the checklists themselves are distributed under non-disclosure agreement. A porting studio therefore bids a fixed price against acceptance criteria it cannot publish, which change per platform and per generation, and which are judged by a party that is not its client.

The other cost was the exclusivity instinct the gate encoded: a platform holder's interest runs against the port, and porting work has always had to be negotiated around that.

## What You Still Touch

A game that slips because "it failed cert" is running into the gate Nintendo built in 1985 to save a market from its own publishers.

- [[problems/game-porting-studios/high-impact|🔴 Bidding a Fixed Price on a Codebase You Have Not Read]] — certification is one of the costs invisible at bid time
- [[problems/game-porting-studios/worker-life-2|🟢 The Producer and the Codebase That Will Not Stop Moving]]
- [[niches/game-porting-studios/certification-requirements/profile|Certification & Platform Requirements]]
- [[niches/game-porting-studios/port-estimation/profile|Port Estimation]]
- [[niches/game-porting-studios/cross-platform-verification/profile|Cross-Platform Verification]]

**Sources:** Wikipedia, *CIC (Nintendo)* (Sharp SM590, 1 Hz reset, US Patent 4,799,635 expiring 24 January 2006, Tengen infringement verdict and settlement, the "without Nintendo's approval … licensing fees" quote); Wikipedia, *Nintendo Seal* (1983 crash, $3 billion to $100 million, five-games-a-year and two-year adaptation rule, pre-release validation of Famicom games); Wikipedia, *Nintendo Entertainment System* (18 October 1985 New York test launch, "strict standards for software approval"). ⚠️ **Not established:** the date and origin of the name "Lotcheck", and the start dates of Sony's TRC and Microsoft's TCR — no public source I reached documents them (Wikipedia *Lotcheck* returned 404; *Video game development* confirms only that manufacturers have "a standard set of technical requirements"); whether the five-a-year and two-year rules applied verbatim in North America (the NES article does not confirm them); the named Nintendo engineers behind the CIC. WebSearch was unavailable this session (session budget exhausted); research used WebFetch on known URLs only.
