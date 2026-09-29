# Lineage: Physical Therapy

**Industry:** [[industries/physical-therapy|Physical Therapy]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** the Medicare outpatient therapy cap — the annual per-beneficiary dollar limit of §4541(c) of the Balanced Budget Act of 1997, $1,500 in 1999 — and the KX modifier a therapist attaches to certify medical necessity above it
**Builder:** US Congress
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

Physical therapy is sold in time. A plan of care is a number of visits, each a stack of 15-minute units of exercise, manual therapy and modalities, repeated for weeks.

For the payer, that is the difficulty: the service has no natural end point. A fracture heals and the surgeon's bill stops; a stiff shoulder or a weak post-stroke leg can always use another session, and the spend grows with the visits.

## What Got Built

Two things in one section of one budget bill.

**§4541(a)(2)** of the Balanced Budget Act of 1997 moved outpatient rehabilitation — physical therapy, occupational therapy and speech-language pathology, except in hospitals — onto a prospective fee schedule. Claims from April 1 1998 had to report units by HCPCS procedure code rather than by revenue code. That is where the familiar arithmetic comes from: the Medicare manual's table converting minutes to units, 8 to 22 minutes for one unit, 23 to 37 for two, and so on — the "8-minute rule" every PT biller knows.

**§4541(c)** put a dollar limit on top. From **1999**, each beneficiary had an **annual limit of $1,500** covering all outpatient physical therapy *and* speech-language pathology combined, with a separate limit for occupational therapy. It counted incurred expenses, including deductible and coinsurance, and was indexed to the Medicare Economic Index from 2002.

Then came the valve. Congress repeatedly passed moratoria on the cap, and the **Deficit Reduction Act of 2005** directed CMS to create exceptions for 2006. The mechanism was a modifier: a therapist appends **KX** to a claim to attest that services above the limit are medically necessary and documented as such.

## Who Built It, And Why Them

Congress, because the cap is a spending instrument, and only a budget bill writes one.

The BBA was a deficit-reduction act. A per-patient dollar ceiling is the bluntest possible tool for a service with no end point: it does not ask whether the tenth visit helps, only whether the year's spending has reached a number. The shape follows from that purpose. The limit is in dollars rather than visits so it tracks fee-schedule spend directly; PT and speech therapy share one bucket because the statute grouped them rather than because they are clinically alike. *(The purpose is stated in the bill's context; the drafters' reasoning for the combined bucket was not traced.)*

What Congress could not do was make the ceiling clinically defensible, which is why the exceptions arrived by statute too. Exceptions based on medical necessity exist only when Congress legislates them.

## What It Cost

**The cap turned clinical judgment into a documentation event.** Above the threshold, the question is no longer whether therapy is working but whether the record proves it.

The **Bipartisan Budget Act of 2018, §50202**, repealed the cap itself — and kept the old amounts as a **KX threshold**, above which every claim must carry the modifier, plus a targeted medical-review threshold of **$3,000**. The ceiling was removed and its paperwork retained. And speech-language pathologists still share a threshold with physical therapists because a 1997 bill put them in one line.

## What You Still Touch

A clinic's biller watches each Medicare patient's year-to-date therapy spend and flags the visit where KX becomes mandatory. Commercial payers and their utilisation managers built their own visit authorisations on the same premise: therapy is approved in tranches, each justified by documented progress.

- [[problems/physical-therapy/high-impact|🔴 Authorization Lifecycle Automation]] — the tranche-by-tranche approval the cap normalised
- [[problems/physical-therapy/worker-life-1|🟢 Documentation-to-Medical-Necessity Burden]] — the KX attestation, written up every visit
- [[niches/physical-therapy/prior-authorization/profile|Prior Authorization & Concurrent Review]]
- [[niches/physical-therapy/pt-utilization-management-networks/profile|Physical Medicine Utilization Management Networks]]
- [[niches/physical-therapy/cash-pay-direct-access/profile|Cash-Pay / Direct-Access PT]] — the route around the cap entirely

**Sources:** CMS *Medicare Claims Processing Manual*, Pub. 100-04, Chapter 5 — §10.2 *The Financial Limitation Legislation* (BBA §4541(a)(2) and §4541(c), P.L. 105-33; $1,500 limit in 1999 for PT and SLP combined, separate OT limit, MEI indexing from 2002; moratoria; Deficit Reduction Act of 2005 exceptions for 2006; Bipartisan Budget Act of 2018 §50202 repeal, KX threshold, $3,000 medical-review threshold), §10.3 (limits and exceptions applied from January 1 2006; later extension to outpatient hospitals 2012, CAHs 2014, Maryland 2016) and §20.2 (unit reporting by HCPCS from April 1 1998; the minutes-to-units table). ⚠️ **Not established:** the document and date in which the minutes-to-units ("8-minute") counting rule first appeared — often attributed to a 2000 HCFA program memorandum, but no copy was reached, so it is described here only as current manual text; the years each moratorium covered; and how outpatient therapy was paid before the BBA, including whether any earlier per-patient limit applied to independent therapists — deliberately not asserted. **Search budget:** WebSearch was exhausted before this note; claims were verified by direct fetch of the CMS manual only.
