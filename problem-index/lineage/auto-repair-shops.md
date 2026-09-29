# Lineage: Auto Repair Shops

**Industry:** [[industries/auto-repair-shops|Auto Repair Shops]]
**Wave:** [[series/eras/wave-04-client-server-erp|4 — Client–Server & ERP]]
**The tool:** the OBD-II diagnostic port — the 16-pin SAE J1962 connector under the dashboard and the SAE J2012 trouble codes it reports
**Builder:** Society of Automotive Engineers
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A car's engine computer knew what was wrong with it, and only the dealer could ask.

By the late 1980s engine computers stored their own fault codes, but every manufacturer used its own connector, protocol and numbering. One retrospective gives the flavour — a code 32 meant an EGR fault on a Nissan, while Honda used code 12 for the same problem.

**For an independent shop, every make was a separate tool and a separate code book.** The dealer had the factory tester; the independent had a drawer of adapters. And the party that most wanted the fault found was not the shop at all, but the regulator trying to keep emissions controls working after the sale.

## What Got Built

A standard socket and a standard vocabulary.

**SAE J1962** fixed a 16-pin data link connector and its location within reach of the driver's seat. **SAE J1979** fixed the test modes a scan tool uses to request data. **SAE J2012** fixed the diagnostic trouble codes — the five-character codes a technician now reads as, say, a P0-series powertrain fault. **SAE J1978** set out what a generic OBD II scan tool must do.

Together they meant **one inexpensive tool could plug into any compliant car and read the same codes in the same format.** California's regulation incorporates each of these SAE Recommended Practices by reference; it requires essentially all 1996 and later passenger cars and light trucks sold there to carry OBD II. The 1990 federal Clean Air Act amendments led EPA to extend the requirement nationally from the same model year.

## Who Built It, And Why Them

Two parties, and the split is the whole story.

**The California Air Resources Board supplied the reason.** It adopted section 1968.1 of its vehicle regulations on **12 September 1989**, requiring second-generation on-board diagnostics, phased in from the 1994 model year. CARB's interest was emissions: a failed catalyst should be detected by the car, flagged to the driver and readable by an inspection station — which a dealer-only system defeated.

**The Society of Automotive Engineers wrote the artefact.** CARB did not design connectors; it pointed at SAE documents. SAE was the one venue where engineers from competing manufacturers already sat together writing recommended practices, so a connector and code list agreed there could be adopted without any one carmaker's system becoming everyone's. One retrospective dates SAE's first proposal for standardised connectors and codes to 1988 — **not confirmed against an SAE source.**

**Why SAE rather than a manufacturer.** A GM or Ford format would have made rivals adopt a competitor's engineering; a CARB-only format would have lacked the manufacturers' agreement on what their hardware could do. The key follows this sweep's standard-owner precedent; the mandate and motive belong to CARB. Independent repair, which inherited the port, was neither party's stated reason.

## What It Cost

**The port was standardised only as far as emissions required.** J2012 reserves generic codes for everyone and leaves manufacturer-specific ranges to each maker. Systems outside the emissions case — airbags, ABS, body electronics — were not bound by the same rule and stayed proprietary, which is why an independent shop still buys factory-level software or subscriptions for anything beyond the engine light. CARB's own later rulemaking lists "requirements to improve the availability of diagnostic information to repair technicians" — a gap the original rule had left.

The subtler cost: a trouble code names **the monitor that failed, not the part that caused it.** A misfire code says a cylinder misfired; it does not say whether the coil, injector, wiring or valve did it. The port made the symptom universal and left the diagnosis where it was.

## What You Still Touch

The engine light you plug a scanner into is a California emissions rule written in SAE's vocabulary:

- [[problems/auto-repair-shops/high-impact|🔴 Diagnostic Expertise Bottleneck]] — the gap between a code and a cause
- [[niches/auto-repair-shops/confirmed-fix-databases/profile|Confirmed-Fix Diagnostic Knowledge Databases]] — code-to-fix mappings the standard never supplied
- [[niches/auto-repair-shops/diagnostic-tool-coverage-engineering/profile|Diagnostic Tool Coverage Engineering]] — the proprietary systems beyond the generic port
- [[niches/auto-repair-shops/right-to-repair-advocacy/profile|Right to Repair Policy Research]]

The manufacturers' side of this appears in [[origins/auto-oems/profile|Auto OEMs]].

**Sources:** California Air Resources Board, Updated Informative Digest for the section 1968.2 OBD II rulemaking (PDF read directly; document created 2003) for the 12 September 1989 adoption of section 1968.1, its incorporation of SAE J1962, J1978, J1979 and J2012, and the quoted language on diagnostic information for repair technicians; search summaries of CARB regulatory notices for the 1994/1996 phase-in and 1996-and-later scope; Corey Lewis, "Abandoned History: OBD-II and the Standardization of Our Troubles (Part II)," The Truth About Cars (fetched) for the Nissan/Honda code example, SAE's 1988 proposal and OEM resistance — a secondary retrospective whose "1994 ultimatum" framing conflicts with CARB's 1989 adoption date, so CARB's date is used. ⚠️ **Not established:** the publication years of J1962 and J2012 — not found at SAE this session; the ~$61 per-vehicle compliance cost the retrospective cites, omitted as unsourced; the exact EPA rule date implementing the 1990 amendments. The claim that non-emissions systems were outside the rule is a reading of its emissions scope, not a quoted provision.
