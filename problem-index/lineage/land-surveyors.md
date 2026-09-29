# Lineage: Land Surveyors

**Industry:** [[industries/land-surveyors|Land Surveyors]]
**Wave:** [[series/eras/wave-08-mobile-gps|8 — Mobile & GPS]]
**The tool:** the State Plane Coordinate System — a set of per-state map-projection zones, each held to under 1 part in 10,000 of scale error, that lets a surveyor tie a flat-earth traverse to national geodetic control; defined in Coast and Geodetic Survey Serial No. 562, *Plane Coordinate Systems* (1933)
**Builder:** US Coast and Geodetic Survey
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

Two kinds of measurement described the same ground and could not easily talk to each other.

A property surveyor works in plane geometry: bearings and distances, a traverse that closes on itself, a plat drawn on flat paper. The federal government's control network worked in latitude and longitude on a curved reference surface. Tying a boundary survey to a national control mark meant spherical computation beyond the routine arithmetic of a county office.

So most boundary work was not tied to anything outside itself. A corner was defined by its relation to other corners and to the monuments a deed happened to name. **When the monuments were lost, the survey was lost with them** — there was no independent coordinate to reconstruct a corner from.

## What Got Built

A way to flatten the earth, one state at a time, with a known and bounded error.

In **1933** the North Carolina Department of Transportation asked the US Coast and Geodetic Survey for a comprehensive method of converting curvilinear geodetic coordinates into a simple two-dimensional grid. The agency's answer, published that year as **Serial No. 562, *Plane Coordinate Systems***, by Oscar S. Adams, became the State Plane Coordinate System, with revised editions in 1936 and 1948.

The design choice is the whole tool. Rather than one projection for the country, each state is cut into zones small enough that the grid stays within **1 part in 10,000** of true ground distance. Zones elongated east–west use a Lambert conformal conic projection; zones elongated north–south use a transverse Mercator; the Alaska panhandle uses an oblique Mercator. The current system has **125 zones**: 108 in the contiguous US, 10 in Alaska, 5 in Hawaii, one for Puerto Rico and the US Virgin Islands, and one for Guam.

## Who Built It, And Why Them

The US Coast and Geodetic Survey, because it owned the control.

The bureau, founded in 1807 as the Survey of the Coast and renamed in 1878, had spent a century building the triangulation network the plane grid was meant to expose. Only the agency holding those coordinates could publish them in a new system — and a projection is worthless unless the control points on it carry official values. Adams was its principal authority on map projections through the 1920s–1940s, and co-authored the North Carolina triangulation volumes of 1935 and 1940.

The users were surveyors and engineers who needed to lay out and retrace lines without a geodesist. The agency's interest was reach: a grid local practitioners could use was how its network would be used at county level.

The geodetic functions passed to the National Geodetic Survey within NOAA in 1970. The system was rebuilt on NAD 83, and a State Plane Coordinate System of 2022, with more zones, has been announced.

## What It Cost

**The 1-in-10,000 rule bought simple arithmetic with a patchwork.** Zone boundaries follow state and county lines, not the ground, so a project spanning two zones — the Seattle area is the standard example — has two grids that do not agree. Every grid distance also differs from the distance a chain would measure, and the surveyor must apply a scale factor to reconcile plat and field.

And every datum change — NAD 27, NAD 83, 2022 — moves every coordinate, so legacy plats must be converted before comparison.

## What You Still Touch

A modern boundary plat notes its "basis of bearings" as a state plane zone, and every GNSS rover reports in it. But the deeds the surveyor retraces predate it by a century, written in calls to creeks and stone walls that no zone can hold.

- [[problems/land-surveyors/high-impact|🔴 Property Boundary Interpretation from Historical Deed Language and Field Evidence]] — the pre-coordinate record the grid could never retrofit
- [[problems/land-surveyors/low-impact-1|🟡 Field Data Processing and Deliverable Generation]] — field observations reduced to grid coordinates before drafting
- [[niches/land-surveyors/geodetic-positioning-networks/profile|Geodetic Positioning Networks]]
- [[niches/land-surveyors/boundary-surveys/profile|Boundary Surveys]]

**Sources:** WebSearch was unavailable this session (session cap reached); research was by WebFetch on specific URLs only. Wikipedia, *State Plane Coordinate System* — the 1933 North Carolina request, the 1:10,000 limit, projection choices, the 125-zone count, NAD 27/NAD 83, and SPCS 2022 (described there as expected for release in 2025; its actual release was not confirmed); Wikipedia, *Oscar S. Adams* — Serial No. 562 (1933; revised 1936, 1948) and the North Carolina triangulation volumes (1935, 1940); Wikipedia, *National Geodetic Survey* — 1807, 1878 and 1970 dates. NGS's own SPCS pages returned only navigation this session. ⚠️ **Not established:** the name of the North Carolina official who made the 1933 request, and the exact name of the requesting body in 1933 (the source uses the modern "Department of Transportation"); the dates of state statutes adopting state plane coordinates for property descriptions; whether Adams alone designed the zones. The "agency's interest was reach" argument is analysis, not a sourced statement of motive. An earlier candidate, NGS's OPUS service, was dropped because its launch date could not be confirmed.
