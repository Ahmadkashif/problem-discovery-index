# Lineage: No-Code App Builders

**Industry:** [[industries/no-code-app-builders|No-Code App Builders]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** Microsoft Access 1.0 and its .mdb file — tables, queries, forms, reports and macros in one Jet database file a non-programmer could build and copy to a share; launched 16 November 1992
**Builder:** Microsoft
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

Before Access, a small database application was a programming job.

On the desktop in the early 1990s, the tools that dominated were dBase, Paradox and FoxPro. They were capable, but building something with them meant writing in their languages, and they had grown up on DOS. Windows 3.x was spreading across office desks, and it had no mass-market database of its own. The people with the most tracking problems — an office manager with a customer list, a department with a request log — sat between two options: a spreadsheet that could not relate one table to another, or a request to IT that would join a queue.

For Microsoft the gap was specific: a Windows desktop with a word processor and a spreadsheet, and nowhere native to put structured data.

## What Got Built

Access 1.0, shown at Comdex Fall in Las Vegas on 16 November 1992 and described by Wikipedia as "the first mass-market database program for Windows."

The design choice that matters is packaging. **Everything — tables, saved queries, data-entry forms, printable reports and macros — lived in one .mdb file**, run by Microsoft's Jet database engine. A user built a form by dragging fields onto a canvas and automated it with macros rather than code; a developer could go further in code, later Visual Basic for Applications. And because the whole application was a single file, it could be emailed, copied to a network drive, and opened by the next person with Access installed.

That is the defining property of every no-code builder since: **the application is an artefact a non-engineer creates and distributes without asking anyone.**

## Who Built It, And Why Them

Microsoft, because the product was a Windows strategy before it was a database. The company needed applications that made Windows the place office work happened, and a database was the missing category.

It did not get there on the first try. Wikipedia records an earlier attempt, **Project Omega**, abandoned as too resource-hungry, before **Project Cirrus** became Access. In the same year Microsoft bought Fox Software, and FoxPro's Rushmore query optimisation went into Access. Access "quickly became the dominant database for Windows."

Microsoft's advantage was not database science — Fox and others had more of it. It was distribution: Access was sold by the company that owned the operating system on those desks, into a Windows installed base no dBase or Paradox vendor controlled. The target was, in Wikipedia's words, "software developers, data architects and power users" — deliberately including the last group.

## What It Cost

**It made building free and owning invisible.** An .mdb had no owner field, no version history, no test, no inventory. It spread by being copied. When the person who built it moved on, the file stayed on the share and kept running a business process nobody else could read.

The single-file design that made distribution trivial also made governance impossible: IT could not see what existed because nothing had to be registered to exist. Microsoft's own later attempt to lift Access onto a server — Access web apps on SharePoint — was retired, and Access no longer ships in the one-time-purchase Office 2021.

## What You Still Touch

Somewhere in most mid-sized companies there is still an .mdb — or its spiritual heir in Airtable or Power Apps — that nobody dares turn off.

- [[problems/no-code-app-builders/high-impact|🔴 The Maintenance Cliff]] — the year-two problem the single file created
- [[problems/no-code-app-builders/worker-life-2|🟢 IT Inheriting Orphaned Applications]]
- [[niches/no-code-app-builders/shadow-app-inventory/profile|Shadow App Inventory]] — the registry the .mdb never had
- [[niches/no-code-app-builders/load-bearing-app-detection/profile|Load-Bearing App Detection]]
- [[niches/no-code-app-builders/inherited-app-administration/profile|Inherited App Administration]]

**Sources:** Wikipedia, *Microsoft Access* (16 November 1992 launch at Comdex Fall; Omega and Cirrus codenames; 1992 FoxPro acquisition and Rushmore; Jet engine and .mdb; "first mass-market database program for Windows"; "quickly became the dominant database for Windows"; target users; macros and VBA; retirement of Access web apps on SharePoint; absence from Office 2021 one-time purchase). ⚠️ **Not established:** Access 1.0's introductory price and first-year sales, often quoted but not in the sources I reached; the dates of Project Omega and of the Access web apps retirement (Microsoft support URL returned 404); the named Microsoft program managers behind Cirrus; any Microsoft statement linking Access to Power Apps — "spiritual heir" above is my characterisation, not Microsoft's. WebSearch was unavailable this session (session budget exhausted); research used WebFetch on known URLs only.
