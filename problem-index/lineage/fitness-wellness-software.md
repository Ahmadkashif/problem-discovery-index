# Lineage: Fitness & Wellness Software

**Industry:** [[industries/fitness-wellness-software|Fitness & Wellness Software]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** the MINDBODY class schedule — a studio's timetable of classes that clients sign into against a pre-paid class pass or series, first written in 1998 for a Pilates studio and put online as a hosted service in 2005
**Builder:** Mindbody
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A gym sells access to a room. A boutique studio sells a seat in a specific class, at a specific hour, with a specific instructor — and there are only so many reformers or bikes in the room.

That changes the unit of accounting. The studio is not tracking whether a member's monthly dues cleared; it is tracking how many of a ten-class pack are left, which class each one was spent on, whether the client showed up, and whether the 6 a.m. spin class is full. In the late 1990s that was a sign-in sheet at the front desk and a paper punch card, reconciled by hand against the till.

Gym software of the day was built for the other model — dues, check-in, a membership that is either active or not. It had no natural place for a seat that expires at 6:45.

## What Got Built

A schedule that is also a ledger. The software held the studio's weekly timetable of classes; a client was signed into a class, and the visit was debited from a class pass or series they had already bought.

That is the data model the category still runs on: **class, capacity, instructor, and a pre-paid bundle of visits drawn down one sign-in at a time.** The early product was desktop-installed; Wikipedia gives the online platform's launch as 2005, after which clients could see the timetable and book a seat from outside the building.

## Who Built It, And Why Them

Mindbody, and the reason is that its founder was sitting inside a studio when he started.

In 1998 Blake Beltram — then studying acting in Los Angeles — was asked to "computerize" **Winsor Pilates**, a studio a fellow actor managed. He began writing software for it as a sole proprietorship called **HardBody SoftWare**, and went on to sell it to yoga, Pilates and spin studios in Los Angeles and San Francisco. On **February 13 2001** the business became an LLC with **Rick Stollmeyer**, a Naval Academy graduate studying technology management at Cal Poly, working out of Stollmeyer's garage in San Luis Obispo.

Why them and not the gym-software vendors: the established vendors sold billing to clubs that lived on monthly dues, and a studio of forty clients buying class packs was too small and too oddly shaped to be worth adapting for. Beltram had one customer whose actual workflow — a class, a pass, a sign-in — was the specification. By the time studios were numerous enough to matter, the product was already shaped around them.

The company went public in June 2015, was taken private by Vista Equity Partners in February 2019 for about $1.9 billion, and acquired ClassPass on October 13 2021.

## What It Cost

The class pack is cash up front for visits delivered later, and the schedule is a public inventory. Putting both online made the studio bookable at midnight, but it also made every empty seat and every unused pass legible — to the studio, and later to aggregators.

The subtler cost is that the pass, not the relationship, became the unit. A client is a balance of remaining visits. Nothing in the model records why a client who used eight of ten classes never bought another pack; it simply stops debiting.

## What You Still Touch

Book a spin class on your phone and pick a bike from a grid: that is the 1998 sign-in sheet with a capacity field, and the pass you draw it from is the punch card.

- [[problems/fitness-wellness-software/high-impact|🔴 Member Lapse Prediction and Intervention]] — the lapse the pass-balance model sees only after it has happened
- [[problems/fitness-wellness-software/low-impact-1|🟡 Class Schedule Construction]] — the timetable itself, still built by hand
- [[problems/fitness-wellness-software/worker-life-1|🟢 Front Desk Cancellation Conversations]]
- [[niches/fitness-wellness-software/boutique-studio-platforms/profile|Boutique Studio Platforms]]
- [[niches/fitness-wellness-software/class-schedule-optimization/profile|Class Schedule Optimisation]]

**Sources:** Wikipedia, *Mindbody Inc.* (HardBody SoftWare 1998, LLC February 13 2001, online platform 2005, IPO June 2015, Vista February 2019 at US$1.9bn, ClassPass October 13 2021); StrengthPortal interview with Rick Stollmeyer (Beltram writing software for boutique studios; Stollmeyer's Navy and Cal Poly background; he dates the garage founding to "2000", which conflicts with the 2001 LLC date — the LLC date is used here); Blake Beltram's IMDb biography (Winsor Pilates and Michael Stadvec — self-published, treat as the founder's own account); SOCAP Global 2017 profile. ⚠️ **Not established:** the specific screens or features of the 1998 desktop product — the "class, pass, sign-in" description rests on a secondary summary of the Stollmeyer interview, not on a product document. The claim that incumbent gym-billing vendors declined the studio segment is inference from the two models' differing units, not a sourced statement.
