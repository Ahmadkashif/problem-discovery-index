# Lineage: Staffing Agencies

**Industry:** [[industries/staffing-agencies|Staffing Agencies]]
**Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**The tool:** the Bullhorn applicant tracking system — a browser-hosted database of candidates, client contacts and job orders that every branch of a staffing firm read and wrote over the internet instead of keeping its own local files
**Builder:** Bullhorn
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A staffing firm's inventory is its candidates, and in a multi-branch firm each branch kept its own.

Recruiters logged candidates, client contacts and open job orders in whatever system their office ran — card files, spreadsheets, or client-server software installed on a local machine. A candidate registered at one branch was invisible to a recruiter at another filling the same kind of order across town. The firm paid to find people it already had. Linking offices meant networking servers, a job small agencies had neither the staff nor the budget to do.

The industry had been placing temps since Kelly Services (1946) and Manpower (1948); the matching itself was old. What was new at the end of the 1990s was a cheap way to put one shared record in front of every office at once: a web browser.

## What Got Built

A hosted applicant tracking system. Candidates, contacts, job orders and the activity history between them lived in one database run by the vendor; recruiters in any branch reached it through a browser. There was no local install and no server for the agency to maintain. Bullhorn's own account says portions of that original ATS code, some written by Art Papas himself, stayed in service until 2015.

The product later grew into the industry's system of record — CRM, back office, time capture and APIs, a SOAP API in 2008 and REST in 2013 — but the first artefact was the shared, hosted candidate and job-order file.

## Who Built It, And Why Them

**Bullhorn**, founded in 1999 in Boston by **Art Papas, Barry Hinckley and Roger Colvin**, with first code written in Papas's Cambridge apartment.

They were not trying to build staffing software. Bullhorn launched as an online marketplace where companies could hire freelance creative talent. It struggled: "We were asking them to hire people sight unseen over the Internet," Papas has said. "We struggled to get employers and companies engaged."

What they did have was a working web application for posting work, tracking people and collaborating across locations — built at a moment when putting a whole business system on the internet was still unusual. Bullhorn's own telling credits its first customer, **Leslie McIntyre**, who wanted a system to speed up cumbersome processes at her staffing company; Papas pitched hosting the whole thing online, and one of the first versions of the ATS followed. The company dates its change of focus to **2001**.

So the builder was a failed marketplace with the right architecture. A staffing firm is itself a labour marketplace with branches; a team that had just built one for freelancers could recognise the shape, and a web-native start-up could offer multi-office access without the server installs incumbents required.

## What It Cost

**The shared record was searched by keyword.** Putting every branch's candidates in one database made the haystack much bigger; it did nothing about how a job order and a resume describe the same skill in different words. Search stayed a string match, and recruiters compensated by hand.

The second cost was dependency. A hosted system of record holds the firm's single most valuable asset — its candidate file — on the vendor's servers, under the vendor's data model. Bullhorn's revenue climbed from about $2 million in 2004 to $67 million in 2013, with private-equity owners from 2012; switching away means migrating the inventory.

## What You Still Touch

Every recruiter's day still begins with a query against a hosted candidate file, and the gap between the words in the requisition and the words in the resume is still theirs to close.

- [[problems/staffing-agencies/high-impact|🔴 Recruiter-to-Requisition Semantic Match Optimization]]
- [[problems/staffing-agencies/worker-life-1|🟢 Recruiter Call/Outreach Volume Pressure]]
- [[niches/staffing-agencies/candidate-matching-ranking/profile|Candidate-to-Requisition Matching & Ranking]]
- [[niches/staffing-agencies/staffing-software-analytics/profile|Staffing Platform & ATS Analytics]]

**Sources:** Wikipedia, *Bullhorn, Inc.* (1999; founders Colvin, Hinckley and Papas; freelancer platform; 2001 change of focus; revenue 2004 and 2013; Vista 2012); Bullhorn, "Our Story" and "Celebrating 20 Years…" (Cambridge apartment; first customer Leslie McIntyre; hosted pitch; original ATS code in use until 2015; SOAP API 2008, REST 2013; multi-branch collaboration as the problem addressed) — vendor-authored, not independent; *Boston Globe*, "Five things you should know about Art Papas", 14 April 2017 (the "sight unseen" quote; pivot 2001). This vault's `history/staffing-agencies.md` supplied the Kelly and Manpower dates (vault material, not independent corroboration). ⚠️ **Sources disagree** on what triggered the pivot: Bullhorn's blog credits a staffing-firm customer, the *Globe* an angel investor. ⚠️ **Not established:** the name of McIntyre's staffing firm, the number of its branches (one secondary summary says four; not found on a primary page), and the first ATS release date. The Bullhorn-owned blog lists Papas and Hinckley only as founders; Wikipedia adds Colvin.
