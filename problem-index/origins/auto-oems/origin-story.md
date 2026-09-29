# Origin Story: Two Plans, Ten Thousand Miles Apart

**Origin:** [[origins/auto-oems/profile|Auto OEMs]]
**Wave:** [[series/eras/wave-02-departmental-item-level|2 — Departmental & Item-Level]]

## What Was True Before

A parts room ran on a reorder point. When the bin holding a part dropped below a marked line, someone ordered more. It is a simple rule and it has one large defect: it has no idea why the part is needed. A bolt used only when a particular sub-assembly is scheduled will nonetheless be reordered the moment the bin looks low, regardless of whether that sub-assembly is scheduled for next week or next quarter.

The consequence is a factory that is simultaneously overstocked on parts it doesn't need yet and short of parts it needs today — the two failure modes of inventory happening at once, in the same warehouse, because the reorder point cannot distinguish **dependent demand** (a part needed only because something else is being built) from **independent demand** (a part that sells on its own, like a spare).

## What They Built, in Armonk

Joseph Orlicky, an engineer at IBM, formulated the core principle around **1964**: if you know the build schedule and the bill of materials, dependent demand is not a forecast, it is an arithmetic explosion. Compute it; don't guess it. **Black & Decker was the first production user that same year**, running the calculation on an IBM 1401 under project lead Dick Alban — batch jobs against punched-card records, reprocessed weekly.

Orlicky's own account of the method waited until his book ***Material Requirements Planning*** (McGraw-Hill, **1975**). It arrived at exactly the right moment for mainframe economics to make it affordable outside a handful of pioneers, and adoption went from roughly 700 companies in 1975 to roughly 8,000 by 1981, running on IBM's BOMP and DBOMP bill-of-materials processors and later on packaged systems — PICS, then COPICS, then MAPICS. **Oliver Wight** extended the idea into **MRP II** in **1983**, closing the loop with capacity planning, shop-floor control and financial integration; Computerworld reported average ROI approaching 200% among full adopters in 1986 — a figure worth treating as an industry-friendly self-reported survey rather than an audited result, the same caveat this vault applies to every unverified ROI statistic.

> **A popular detail does not survive checking.** Several retellings claim Orlicky arrived at MRP by studying the Toyota Production System directly. The dates make this hard to credit: TPS existed in 1964 as an internal, undocumented shop-floor practice at a single Japanese manufacturer, and nothing describing it in a form an IBM engineer in the United States could have studied was published until Ohno's book appeared in Japanese in **1978** — fourteen years later. No source locatable for this file supports Orlicky studying TPS. Treat the claim as unverified, probably apocryphal, and note that the more interesting truth is the one it obscures: **two people on two continents solved a version of the same problem without knowledge of each other.**

## What Was Happening in Toyota's Machine Shop, at the Same Time

Taiichi Ohno began testing a different mechanism inside Toyota's main plant in **1953**: a card — *kanban* — that authorised a station to produce or move exactly one container's worth of parts, issued only when the downstream station consumed one. No forecast, no central schedule, no computer. A plan was developed in **1963** to spread the practice across the whole company, and it was, over the following decade, factory by factory. Ohno's own account, ***Toyota Production System — Beyond Large-Scale Production***, was published in Japanese in **1978** and translated into English only in **1988** — meaning the discipline was running inside Toyota for a quarter of a century before most of the world outside Japan could read a description of it.

## Why It Mattered

MRP is a **push** system: compute a plan from a forecast, then push material at it. Kanban is a **pull** system: let consumption pull replenishment, with no forecast in the loop at all. They are not variations on a theme. They are opposed answers to the same question, and this vault's plan for this phase flags the conflation of the two as one of the most persistent myths in popular business writing about manufacturing.

**Computerisation made the wrong lesson scale first.** MRP could be sold as software, licensed, and installed by a mainframe vendor's field team; by 1981 it was running in 8,000 companies. Kanban could not be sold at all — it had to be learned on a factory floor, one shift at a time, and it stayed largely confined to Toyota's own plants and its closest suppliers for two more decades.

**Sources:** QAD, *Joseph Orlicky: Hero of Material Requirements Planning*; Wikipedia, *Joseph Orlicky*, *Material Requirements Planning*; Toyota Global, *75 Years of Toyota*; ProjectManager, *Kanban History*; Wikipedia, *Toyota Production System*.
