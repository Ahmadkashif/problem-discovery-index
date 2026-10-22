# Ground Lease and Permit Administration

**Industry:** [[outdoor-advertising-companies|Outdoor Advertising Companies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Lease administration software already tracks rents and expiries; it doesn't know that a billboard lease is worthless without its state and local permits, or that a percentage-rent clause needs the face's revenue.
**Tags:** #large-language-models #transformers #survival-analysis #data-integration #workflow-orchestration #compliance #automation

## The Problem
Every structure an outdoor company owns sits on a lease and a stack of permits. Outfront reports ~19,600 lease agreements with ~17,900 different landlords; Lamar ~71,500 leased sites. Terms run from month-to-month to more than ten years. Rent may be fixed, escalate on a schedule, or be the greater of a floor and a percentage of the face's revenue. Leases carry access easements, vegetation-trimming rights, restrictions on what may be advertised (a church landowner who bars alcohol, a car dealer who bars competitors), notice obligations if the land is sold, and renewal options with their own deadlines. Separately, each structure carries a state permit along controlled routes (renewed annually in Texas for $75, with a $100 late fee) and often a local permit, and many structures are legal nonconforming uses that lose their right to exist if a renewal lapses or the structure is substantially rebuilt.

Real estate administrators keep this in a property management system, spreadsheets and paper files. Percentage rents are calculated by hand from billing exports. A renewal option is missed because the notice clause sat in an amendment. A permit lapses because the tag number on the state's list doesn't match the company's.

## What Already Exists
Tenant-side lease administration platforms such as Visual Lease, CoStar Real Estate Manager, LeaseQuery and Yardi handle critical dates, payments and lease accounting. Billboard packages (Apparatix, BillboardPlanet, HighSign Pro) include basic lease modules with renewal alerts for independents. State DOTs publish permit lists, and some offer online renewal portals.

## The Customisation Gap
The billboard-specific logic is the link between lease, permit and face. That means: one record per structure tying the lease, the state permit tag, the local permit and the nonconforming status together, so a lapse on any one shows as risk to the whole site; percentage-rent statements calculated automatically from the face's billed revenue, with the landlord's audit rights in mind; extraction of use restrictions from lease text into rules that the sales and digital scheduling systems enforce; detection of landowner sale notices and lease-buyout solicitations (aggregators pay landowners lump sums of roughly 6–12× annual rent) so the real estate team can respond before the lease is assigned; and state-by-state permit renewal calendars reconciled against each DOT's own list. Generic platforms treat each lease as a standalone office tenancy; a billboard lease only has value with its permits attached.

## Impact If Solved
Administrators stop rebuilding percentage-rent statements by hand each quarter. Lapsed permits and missed renewal options, the two ways a company loses an irreplaceable location through paperwork, become rare and visible. Lease restrictions reach the people selling the face before a contract is signed that the landlord can void.
