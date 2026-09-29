# Lineage: Social Services Nonprofits

**Industry:** [[industries/nonprofits-social-services|Social Services Nonprofits]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** the HMIS Data and Technical Standards — HUD's Final Notice of July 30 2004 fixing the universal data elements every federally funded homeless program records per client, and the privacy and security rules for the shared local database that holds them
**Builder:** US Department of Housing and Urban Development
**Builder in vault:** **ABSENT**
**Verification:** verified — see Sources

## The Problem That Came First

A homeless person may pass through a shelter, a day centre and a transitional-housing program in one month — often three nonprofits, three intake forms.

So every count double-counted. Each agency knew how many *visits* it served; nobody knew how many *people* were homeless, how long they stayed, or where they went next. A funder asking "did this work?" could be shown attendance, not outcomes, because the outcome — the same person not coming back — happened in someone else's file.

The constraint was not effort. It was that the unit of record was the agency, and the question was about the person.

## What Got Built

A federal notice that told every funded program **what to write down, in what form, and where**.

HUD's *Homeless Management Information System (HMIS) Data and Technical Standards Final Notice*, published in the Federal Register on July 30 2004 and effective August 30 2004, did three things.

It set **universal data elements** collected from every client: date of birth, gender, race, ethnicity, veteran status, Social Security Number, disabling condition, residence before program entry, and zip code of last permanent address. The disabling-condition element was added so that chronically homeless people could be identified.

It set **program-specific elements** for programs filing Annual Progress Reports — income sources, services received, and **destination at program exit**. That last field is the whole outcome question reduced to a pick-list.

And it set **baseline privacy and security standards** for the community-wide database into which every participating agency writes, with optional stronger protections for programs serving especially vulnerable clients.

Programs funded under McKinney-Vento were required to take part.

## Who Built It, And Why Them

The Department of Housing and Urban Development — because Congress asked it for a number that no nonprofit could produce.

In the FY 2001 appropriations cycle (Pub. L. 106-377, approved October 27 2000), House Report 106-988 and Senate Report 106-410 directed HUD to develop **"an unduplicated count of homeless people"** and to analyse how people "enter and exit the homeless assistance system and the effectiveness of assistance." The Consolidated Appropriations Act of 2004 (Pub. L. 108-199) repeated the support.

HUD was the only party that could answer. It funded the programs, so it could make data collection a grant condition; it sat above every local agency, so it could impose one schema across all of them. A draft notice went out on July 22 2003 (68 FR 43430) and drew 167 commenters and more than 1,600 distinct comments before the final version.

The business case shaped the artefact. Because the goal was de-duplication, the schema leans on identifiers — SSN, date of birth, name — rather than on what case managers actually do. Because the goal was a national count, the elements are the same whether the agency is a 400-bed shelter or a two-room drop-in centre.

## What It Cost

**Identity became the price of service data.** Asking for a Social Security Number at a shelter door is a real barrier, and the notice had to pair its identifiers with privacy rules to make the trade tolerable. Domestic-violence programs were included in the 2004 notice — the tension between a shared database and a client hiding from an abuser is built in.

The schema also fixed **what counts as an outcome** — mostly housing destination at exit — and left out the things case managers spend their time on. Agencies meeting HUD's elements still keep a second record for everything else, and for every other funder's format.

## What You Still Touch

Every intake a homeless-services case manager completes today begins with the universal data elements in roughly the order HUD listed them, and every "exit destination" drop-down is the 2004 outcome field. The documentation burden and the reporting mismatch the vault describes are what happens when one funder's schema becomes the sector's floor.

- [[problems/nonprofits-social-services/high-impact|🔴 Client Outcome Tracking and Program Effectiveness Measurement]]
- [[problems/nonprofits-social-services/worker-life-1|🟢 Case Manager Documentation Burden]]
- [[niches/nonprofits-social-services/homeless-management-information-systems/profile|Homeless Management Information Systems]]
- [[niches/nonprofits-social-services/homelessness-continuum-of-care/profile|Homelessness Continuum of Care]]

**Sources:** HUD, *Homeless Management Information Systems (HMIS); Data and Technical Standards Final Notice*, Federal Register, July 30 2004 (govinfo document 04-17097): effective date August 30 2004; draft notice July 22 2003, 68 FR 43430, comment period to September 22 2003, 167 commenters and 1,600+ comments; FY 2001 directives in House Report 106-988 and Senate Report 106-410 (Pub. L. 106-377, approved October 27 2000); Senate Report 108-143 and Pub. L. 108-199 (January 23 2004); universal and program-specific data elements; McKinney-Vento participation requirement including domestic-violence programs; baseline and optional privacy standards. WebSearch was unavailable this session (session cap reached); research was by WebFetch on known URLs; hudexchange.info program pages and Wikipedia returned 404. ⚠️ **Not established:** later changes — the subsequent revisions of the HMIS Data Standards, and any statutory restriction on domestic-violence providers entering identifying data into HMIS (commonly attributed to the 2005 reauthorisation of the Violence Against Women Act) — were not confirmed from a fetched source this session and are therefore not asserted. The name of the HUD office or officials who drafted the notice was not established. "Roughly the order HUD listed them" is an observation, not a sourced claim.
