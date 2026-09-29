# Lineage: Owner-Operator Trucking

**Industry:** [[industries/owner-operator-trucking|Owner-Operator Trucking]]
**Wave:** [[series/eras/wave-08-mobile-gps|8 — Mobile & GPS]]
**The tool:** the electronic logging device (ELD) of 49 CFR Part 395 Subpart B — an engine-synchronised hours-of-service recorder exporting one standard comma-delimited output file to a roadside inspector
**Builder:** Federal Motor Carrier Safety Administration
**Builder in vault:** **ABSENT**
**Verification:** verified — primary documents, see Sources

## The Problem That Came First

A one-truck business sells hours. The law caps how many it may sell.

Federal hours-of-service rules limit how long a commercial driver may drive and work, and the driver proves compliance with a **record of duty status**: a daily grid on which he draws a line through off-duty, sleeper berth, driving and on-duty-not-driving. For decades that grid was paper, and paper is written by the person it limits.

For an owner-operator paid by the mile, the pressure runs one way. Four unpaid hours at a shipper's dock use up legal hours, and a paper log could be adjusted afterwards to make up the difference.

## What Got Built

A device wired to the engine that writes the log itself.

**The ELD rule (80 FR 78292, published December 16 2015; compliance date December 18 2017) set minimum performance and design standards and required their use by drivers who had to keep records of duty status.** The device must be "integrally synchronised" with the engine, so motion and engine hours are recorded automatically rather than typed in. Edits are allowed, but the driver must accept or reject any change the carrier proposes.

The part inspectors actually use is the output. The rule requires "a single comma-delimited file … using … ASCII character sets," with a header and segments for drivers, vehicles, events, malfunctions, logins and unidentified driving. It must be transferred either by web services and email, or by USB 2.0 and Bluetooth, and shown on a display or printout. Two options in the draft rule, QR codes and TransferJet, were dropped.

An earlier standard for "automatic on-board recording devices" dated from 1988. That older 49 CFR 395.15 standard was optional, and fleets that used it could keep it until December 2019.

## Who Built It, And Why Them

The FMCSA, under orders from Congress, after owner-operators beat its first attempt in court.

The agency finalised an electronic on-board recorder rule in April 2010. The **Owner-Operator Independent Drivers Association** petitioned the Seventh Circuit in June 2010, and on August 26 2011 the court vacated the rule (*OOIDA v. FMCSA*, 656 F.3d 580). It held that the agency had failed to address driver harassment, which the statute required it to consider.

Congress then removed the choice. **Section 32301(b) of MAP-21 (Pub. L. 112-141, July 6 2012) directed the Secretary to require ELDs** and to ensure a device "is not used to harass a vehicle operator." That is why the 2015 rule has anti-harassment provisions and the driver-approval step for edits. OOIDA challenged the new rule as well and lost: *OOIDA v. U.S. Department of Transportation*, 840 F.3d 879 (7th Cir., October 31 2016).

It had to be the regulator. Big fleets had already bought telematics such as Qualcomm's OmniTRACS (see [[lineage/fleet-managers|Lineage: Fleet Managers]]) for their own reasons. Nobody in the market had a reason to put a tamper-evident log in the one-truck operator's cab. Only a mandate would make every device produce the same file.

## What It Cost

**The flexibility of the paper log.** Its slack was how owner-operators absorbed hours lost waiting at docks. The ELD records those hours as they happen, so detention now uses up the driver's legal day.

The money cost was smaller than feared. FMCSA's draft estimated $495 a year per truck, with a range of $165–$832, and cut this to $419 for a telematics-type device in the final rule. The agency projected 1,844 crashes and 26 deaths avoided each year.

Commenters argued the burden fell hardest on small carriers; the record shows the argument, not its resolution.

## What You Still Touch

Every owner-operator's day now runs on an engine-synchronised clock the shipper's dock ignores. Load choice has become a scheduling problem: a load is only worth taking if it can be finished within the hours left on the log.

- [[problems/owner-operator-trucking/low-impact-2|🟡 HOS-Aware Load Planning]] — optimising the hours the ELD now counts exactly
- [[problems/owner-operator-trucking/worker-life-2|🟢 Unpaid Detention and Lumper Time at Shippers and Receivers]] — the waiting the paper log used to hide
- [[niches/owner-operator-trucking/fmcsa-safety-enforcement/profile|FMCSA Safety Measurement & Enforcement Analytics]]
- [[niches/owner-operator-trucking/telematics-safety-analytics/profile|Fleet Telematics & Safety Analytics Teams]]

**Sources:** FMCSA, *Electronic Logging Devices and Hours of Service Supporting Documents*, final rule, 80 FR 78292 (Dec 16 2015), via govinfo.gov and the Federal Register API: dates, device and output-file requirements, transfer options, MAP-21 §32301(b) citation and anti-harassment language, 2010 rule history and the Seventh Circuit vacatur, 1988 AOBRD reference, cost figures ($495 / $165–$832 / $419), 1,844 crashes and 26 lives, small-carrier comments. CourtListener: *OOIDA v. U.S. DOT*, 840 F.3d 879 (7th Cir. Oct 31 2016). Wikipedia, *Electronic logging device* (AOBRD-to-ELD transition by December 2019). ⚠️ WebSearch was unavailable this session (session cap reached); research used direct fetches only. **Not established:** which company built the first commercial AOBRD in 1988, and the dated origin of the paper record-of-duty-status grid. Both were left out rather than guessed.
