# The Vehicle Sits on the Lift While Someone on a Phone Decides Whether the Quote Is Fair

**Niche:** [[niches/auto-repair-shops/fleet-maintenance-analytics/profile|Fleet Maintenance Management Analytics]]
**Industry:** [[industries/auto-repair-shops|Auto Repair Shops]]
**Type:** Fix (Pain Point)
**One-liner:** Every fleet repair needs authorisation before it starts, the authoriser judges it from a verbal description against a rate table and their own memory, and the shop, the driver and the fleet all wait.
**Tags:** #large-language-models #logistic-regression #evaluation-metrics #workflow-orchestration #worker-facing

## The Problem
A fleet vehicle arrives at an independent shop. The shop diagnoses it, then calls the fleet management company for authorisation. An authoriser takes the call, listens to a description of the work, checks the negotiated labour rate and a standard labour time, applies judgment about whether the repair is warranted at this mileage, and approves, reduces or declines it.

That call is the control point for the entire cost structure and it runs on hold music.

For the shop, the vehicle occupies a bay while it waits. Fleet work is already lower-margin than retail because rates are negotiated down, and the authorisation delay is uncompensated. Many shops have a stated preference to avoid fleet work for exactly this reason, which narrows the network and pushes vehicles to shops that are further away or slower.

For the fleet, the vehicle is out of service for the duration. Downtime on a working vehicle costs far more than the disputed portion of most repairs.

For the authoriser, the job is a queue of calls where each decision is made on a verbal account of a car they cannot see, from a shop whose reliability they may or may not remember, against a labour time standard that may not match the actual condition of a ten-year-old vehicle.

The organisation holds millions of prior authorisations that would answer nearly every one of these calls empirically. The authoriser has a rate table and experience.

## Why It's Still Broken
The authorisation exists to control cost and it demonstrably does — shops quote differently when they know a review is coming. The friction is understood as the price of that control, and reducing the friction is assumed to reduce the control. That trade-off has never been measured, and it is not obviously real.

Authorisation is staffed as a call centre and measured like one: calls handled, average handle time, savings captured against quoted amounts. None of those metrics contain shop wait time or vehicle downtime, so the costs the process imposes are borne by parties who are not measured.

The consistency problem is invisible for the same reason. Two authorisers presented with the same repair do not necessarily decide the same way, and nobody measures it, because there is no second opinion recorded anywhere.

The shop's side is also poorly represented. Fleet management companies compete for client fleets, not for shops, and shop experience does not appear in any scorecard — even though network quality and coverage is what determines whether the vehicle gets fixed quickly.

And the data that would fix it lives in a workflow system designed to record decisions rather than to inform them.

## What a Fix Looks Like
**Give the authoriser the empirical distribution before they answer.** What this repair, on this platform, at this mileage, in this market, has actually cost across thousands of prior authorisations — with a range, not a single number. This is a lookup against data already held and it changes the call from memory to evidence.

**Auto-approve the routine and mean it.** A large share of authorisations are unambiguous: standard repair, standard time, in-range price, reasonable for the mileage. Classifying those confidently and approving them instantly frees the authoriser for the calls that actually need judgment, and removes the bay-blocking wait for most repairs.

**Structure the description.** The repair reaches the authoriser as speech or free text. Extracting component, operation and quoted amount reliably is now routine, and it is what makes any of the above possible in real time.

**Score the shop on evidence.** Whether a shop's quotes come in above the distribution, whether its repairs recur, whether its diagnoses hold up — all measurable from history, none currently computed. That number should drive routing, and it should be visible to the shop.

**Measure the whole cost of the decision.** Authoriser savings against quoted amount is a partial metric that ignores downtime and shop time. A comparison that includes both would settle whether the friction is buying anything on the repairs where it is currently applied.

**Test the authorisers against each other.** A sample of repairs reviewed independently by two authorisers gives a disagreement rate. If it is high, the process is adding variance rather than control, and that is worth knowing.

## Who Feels the Pain
The shop, holding a bay for a call. The technician, idle mid-job. The driver, without the vehicle they work from. The authoriser, deciding blind at volume. And the fleet client, paying for downtime that never appears on the savings report.

## Impact If Fixed
Millions of fleet vehicles are repaired through a control point that has not changed in thirty years, run from memory by people sitting on a dataset that would answer nearly every question they are asked.
