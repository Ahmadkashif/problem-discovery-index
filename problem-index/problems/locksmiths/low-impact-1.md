# Master-Key Systems Kept in Binders

**Industry:** [[locksmiths|Locksmiths]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** A campus or hospital master-key system is a combinatorial design held on a paper bitting chart by one locksmith, and when a grand master goes missing nobody can say quickly which doors it opens or what a rekey will cost.
**Tags:** #combinatorics-and-counting #graph-theory #optimization-fundamentals #data-integration #compliance #automation

## The Problem
A master-key system lets one key open many locks by splitting pin stacks so that each cylinder accepts its own change key plus every master above it. A large system runs from a grand master through masters and sub-masters to thousands of change keys. Designing it is constrained combinatorics. The designer must respect the manufacturer's maximum adjacent cut specification, avoid accidental cross-keying (a change key that opens a door it shouldn't), keep enough unused bittings for the building's next wing, and limit the number of split pins, which make a cylinder easier to pick. The design lives on a bitting chart. At a typical client that chart sits in a binder at the locksmith who designed the system, or in a spreadsheet nobody else can read, next to a key-issue log that records who signed for which key.

The trouble comes at three moments. When a master key is lost or an employee leaves without returning keys, the client asks which doors are exposed and what it costs to fix. When a building is renovated, someone has to extend the system without collisions. And when the client changes locksmiths, the chart often does not come with them.

## What Already Exists
Small desktop programs such as MKExpress and Aero Key generate standard-progression systems and print bitting charts. Lock manufacturers run factory keying services that design and register large or patented systems. Key cabinets and tracking software such as KeyTrak and Traka log who has a key out, and CMMS platforms hold door and asset registers. Many locksmiths still design by hand on worksheets.

## The Customisation Gap
None of these joins the design to its consequences. The locksmith-specific logic is several pieces. A system model that knows every cylinder's pinning, the keyway and its restricted or patented status, and the hierarchy, and can test for cross-keying across the whole system and against neighbouring systems from the same keyway. A key-holder ledger tied to that model, so a lost key resolves instantly to a set of doors. A rekey planner that costs the cheapest change, whether re-pinning a sub-master's cylinders, replacing cores in an interchangeable-core system or moving to a new keyway. And authorisation rules for restricted keyways, where only named signatories may order duplicates. Generic tools track keys as assets. They do not understand that a key is a bitting, and that a bitting implies a set of doors.

## Impact If Solved
A lost-master incident goes from a week of reconstruction and a precautionary full rekey to a same-day answer with a costed, minimal rekey plan. For a campus with thousands of doors that difference is often tens of thousands of dollars (estimate). The locksmith who holds the live system model becomes very hard to replace, and that is the reason the record is worth building.
