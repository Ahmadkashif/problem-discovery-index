# Lineage: Cold Chain Logistics

**Industry:** [[industries/cold-chain-logistics|Cold Chain Logistics]]
**Wave:** [[series/eras/wave-08-mobile-gps|8 — Mobile & GPS]]
**The tool:** the engine-driven, externally mounted truck refrigeration unit — Frederick McKinley Jones and Joseph Numero's "air conditioner for vehicles", US Patent 2,303,857 (filed November 16 1939, granted December 1 1942), sold as the Thermo King
**Builder:** U.S. Thermo Control Company
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A truck is a box that gets warmer every hour it moves.

Before a machine sat on it, keeping perishables cold on the road meant carrying the cold in with the load — something loaded at the start that ran out somewhere along the way. The shipper's range was set by how long that stock lasted, not by how far the truck could drive. The cost of a long haul was not fuel. It was the tail of the trip where the box had stopped doing its job, and the load that spoiled in it.

## What Got Built

A refrigeration machine that travelled with the truck and ran on its own engine.

The 1939 patent application Numero and Jones filed states the object plainly: a means of "tempering, humidifying and circulating the air" in the compartment of "a truck, railroad car or the like", which "shall be conveniently attachable to and removable from such carrier" and "shall automatically effect the desired air conditioning." The unit was mounted outside the box so it did not eat cargo space.

The first version, the Model A, hung under the truck's chassis and piped chilled air into the trailer. It proved too heavy, and Jones reworked it into lighter units. By 1944 he was filing improvements — US Patent 2,475,841, granted 1949 — on problems specific to a machine riding a highway: wind interfering with the cooling, and a gas engine and compressor overheating in a box with no natural convection. A unit on a road has failure modes a unit in a warehouse does not, and the patents track them one by one.

## Who Built It, And Why Them

Not a refrigeration company and not a trucking company. A movie-sound business in Minneapolis.

Numero ran a firm supplying sound equipment for converting silent-film projectors; he hired Jones, a largely self-taught mechanic, in 1927 to improve that gear. Around 1938, at Numero's request, Jones began designing the truck unit. Numero then sold the sound business to RCA and formed U.S. Thermo Control Company with Jones — renamed Thermo King in 1941.

**Why them:** the binding constraint was not the refrigeration cycle, which was well understood. It was making a compressor, engine and controls survive vibration, weather and no attendant — a compact, rugged, self-regulating box. That is the skill set of someone who had spent a decade building portable electromechanical equipment for cinemas, not of a firm selling ice or cold storage. The patent names "automatically" in its object for a reason: there was no one in the trailer to adjust it.

In the Second World War the same units carried blood and medicine to army hospitals.

## What It Cost

The unit made the box cold. It did not make the box *knowable*.

A machine running on the truck meant temperature became a setpoint the driver or shipper chose, rather than a stock that ran down — and so every failure became a machine failure: fuel run out, a compressor fault, a door left open, a pre-cool skipped. The trade was range for a new dependency: the load was now only as safe as an unattended engine, with nobody watching it between pickup and delivery.

That gap — a controlled box nobody could see into — is what the rest of the industry's tooling has been built to close.

## What You Still Touch

The reefer on the front of every refrigerated trailer is this machine's descendant, still mounted outside the box, still running its own engine, and still the single point the load's safety depends on.

- [[problems/cold-chain-logistics/high-impact|🔴 Temperature Excursion Prediction and Early Intervention]] — the watching the 1939 unit could not do
- [[problems/cold-chain-logistics/low-impact-2|🟡 Reefer Unit Maintenance Prediction from Telematics Data]] — the machine as the load's point of failure
- [[problems/cold-chain-logistics/worker-life-2|🟢 Reefer Unit Pre-Cool Time Prediction for Load Planning]]
- [[niches/cold-chain-logistics/refrigeration-equipment-reliability/profile|Refrigeration Equipment Reliability Engineering]]
- [[niches/cold-chain-logistics/small-fleet-reefer-operators/profile|Small Reefer Fleet Operators (5-30 Units)]]

**Sources:** Google Patents, US2303857A (Numero and Jones, *Air conditioner for vehicles*, filed 16 Nov 1939, granted 1 Dec 1942, assignee U.S. Thermo Control Co. — object quoted from the patent) and US2475841A (Jones, *Air conditioning unit*, filed 15 June 1944, granted 12 July 1949, same assignee); Wikipedia, *Frederick McKinley Jones* (Model A under-chassis mounting; 1927 hire; RCA sale; 1991 National Medal of Technology; WWII use) and *Thermo King* (1941 rename). WebSearch was unavailable this session (session cap reached); research was by WebFetch only. ⚠️ **Conflicts and gaps:** Wikipedia's *Thermo King* gives a patent date of 12 July 1940 and dates the RCA sale to 1938; *Frederick McKinley Jones* dates the sale and the partnership to 1939. The patent record shows 12 July is the 1949 grant of a later patent; the founding patent was filed 1939 and granted 1942 — I have used the patent dates and left the company's exact founding year as 1938–1939, unresolved. The widely repeated story that the unit was prompted by a trucker friend of Numero's losing a load could not be confirmed against any source fetched and is omitted. Pre-1938 refrigeration practice (ice, dry ice) is described only generally because no dated source was reached. MNHS and Lemelson-MIT pages on Jones returned 404.
