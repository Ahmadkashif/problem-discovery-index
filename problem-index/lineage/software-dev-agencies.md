# Lineage: Software Development Agencies

**Industry:** [[industries/software-dev-agencies|Software Development Agencies]]
**Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**The tool:** the function point — a count of a system's inputs, outputs, inquiries, internal files and external interfaces, weighted for complexity, used to size an application before any code exists
**Builder:** IBM
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A firm that builds software for someone else has to say how big the job is before it knows.

In the 1970s the only size anyone measured was **lines of code**, and it failed a contractor twice. It could not be known at bid time, because the code did not exist yet. And it punished productivity: a team that switched to a higher-level language delivered the same system in fewer lines, so by the only yardstick available it looked *less* productive. Capers Jones later called this the productivity paradox. An organisation that sold development work and wanted to prove it was getting better at it had no honest number to show a customer — or itself.

## What Got Built

A way of sizing software from the outside, by what it does for its user rather than how it is written.

The analyst counts five things visible in the requirements: **external inputs, external outputs, external inquiries, internal logical files and external interface files.** Each is graded simple, average or complex and weighted; the total, adjusted for a set of general system characteristics, is the application's size in function points. Because it is drawn from what the user sees, it can be counted from a specification — before design, before a language is chosen — and compared across projects written in COBOL, PL/I or anything else.

Albrecht presented it publicly in **"Measuring Application Development Productivity"**, at the Joint SHARE, GUIDE and IBM Application Development Symposium in **Monterey, California, 14–17 October 1979**. The paper reported roughly a **three-to-one productivity improvement across 22 projects between 1974 and 1978**, measured in function points per unit of effort.

## Who Built It, And Why Them

**Allan J. Albrecht, of IBM**, working to measure development productivity in IBM's **DP Services** organisation. Capers Jones places the work with Albrecht and colleagues at IBM's White Plains development centre around 1975.

The reason it was IBM, and specifically that part of IBM, is that DP Services was in the business a software agency is in: building applications for other people. By secondary accounts its projects were customer-contract application development — so it carried a vendor's exposure on every estimate and needed a size measure a customer would accept, one that did not reward writing more code. IBM also had the portfolio to calibrate against: a history of comparable projects to fit weights to. No single agency then had enough projects to do that, and none had the standing to make the result an industry yardstick. IBM put the method into the public domain, and its counting rules passed to the **International Function Point Users Group**, founded in the mid-1980s.

## What It Cost

**The count takes a trained human and a finished specification.** It is slow, it varies between counters, and it presumes requirements stable enough to count — the fixed-scope waterfall contract it grew up in.

It also did not escape the thing it was built to replace as cleanly as intended. Albrecht himself observed that function points correlated strongly with lines of code, and critics went on to argue about the complexity weights for decades. Most small agencies never adopted the method at all; they estimate by analogy and gut, and the function point survives mainly in large outsourcing contracts, government procurement and benchmarking databases.

## What You Still Touch

Any agency that bids fixed-price is still pricing a size it cannot yet measure. Story points and T-shirt sizes are the informal heirs — unit-free, team-specific and uncomparable, which is exactly the problem Albrecht set out to solve.

- [[problems/software-dev-agencies/high-impact|🔴 Project Scoping & Estimation Accuracy]]
- [[problems/software-dev-agencies/low-impact-1|🟡 Client Requirement Docs & Change Tracking]] — the unstable specification the count assumes away
- [[niches/software-dev-agencies/software-estimation-benchmarking/profile|Software Estimation & Project Benchmarking]]
- [[niches/software-dev-agencies/project-estimation-scoping/profile|Project Estimation & Scoping]]
- [[niches/software-dev-agencies/client-change-order-mgmt/profile|Client Change-Order Management]]

**Sources:** Wikipedia, *Function point* and *IFPUG* (Albrecht, IBM, 1979 paper; five component types; Albrecht's own observation of correlation with LOC; ISO/IEC 20926); search-result summaries of the paper's bibliographic record — A. J. Albrecht, "Measuring Application Development Productivity", *Proc. Joint SHARE/GUIDE/IBM Application Development Symposium*, Monterey, 14–17 October 1979, pp. 83–92 (aim: productivity in IBM's DP Services; ~3:1 improvement across 22 projects 1974–78); IFPUG, "40 Years of Function Points" (2019) (October 1979; productivity paradox; IFPUG 1987); Capers Jones, "Function points as a universal software metric", CERM Risk Insights (White Plains circa 1975; public domain 1978). ⚠️ **Sources disagree:** IFPUG's founding is given as 1986 and 1987, and IBM's public-domain release as 1978 while the defining paper is 1979 — hence "mid-1980s" and no release year above. ⚠️ **Not established:** a primary description of DP Services' business — the "customer-contract application development" characterisation rests on secondary summaries, not the 1979 paper text, which I could not read in full this session.
