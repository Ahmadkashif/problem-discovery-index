# Lineage: Scheduling & Booking Platforms

**Industry:** [[industries/scheduling-booking-platforms|Scheduling & Booking Platforms]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** iCalendar — RFC 2445 (November 1998), the text format for a calendar event, and the `.ics` file with a VEVENT inside it that every booking confirmation still attaches
**Builder:** IETF
**Builder in vault:** **ABSENT**
**Verification:** verified — dates checked against the RFC header; see Sources

## The Problem That Came First

An appointment has two parties, and until the late 1990s their calendars could not talk.

A booking made in one system — a doctor's front desk, a consultant's scheduler, a corporate calendar — existed only there. To put it in the other party's diary, someone typed it again. Group scheduling products existed, but each vendor's worked only among its own users: a Lotus user and a Microsoft user could email each other freely and could not send each other a meeting.

For a business whose product is the slot, that is the whole problem. A booking that the customer never sees in their own calendar is a booking the customer forgets, and the no-show is born in the gap between the two diaries.

## What Got Built

A plain-text format for an event. A `BEGIN:VEVENT … END:VEVENT` block carries a start, an end, a summary, a location, an organiser and attendees; an `RRULE` carries recurrence; a `VFREEBUSY` block publishes when someone is available without revealing why; and a `METHOD` line says whether the message is a request, a reply or a cancellation.

RFC 2445 states its purpose as "a common format for openly exchanging calendaring and scheduling information across the Internet." Its companions, **RFC 2446 (iTIP)** and **RFC 2447 (iMIP)**, defined how requests and replies move, including over ordinary email. The format was revised as **RFC 5545 in September 2009**, which is the version in force.

## Who Built It, And Why Them

The Internet Engineering Task Force's Calendaring and Scheduling Working Group — with the text written by **Frank Dawson of Lotus** and **Derik Stenerson of Microsoft**, and the group chaired by Anik Ganguly of Open Text.

The authorship is the answer to "why them". Lotus and Microsoft were the two firms whose customers were most visibly unable to schedule each other, and neither could fix it alone: a proprietary format that only one of them adopted was worthless. A neutral standards body was the only place both could commit.

They did not start from nothing. The **Versit Consortium** — founded by Apple, AT&T, IBM and Siemens — released **vCalendar 1.0 on September 18 1996**, and in December 1996 handed the rights to the Internet Mail Consortium. iCalendar is built on vCalendar; the IETF turned a consortium's device-exchange format into an internet standard for scheduling between organisations.

## What It Cost

The format standardised the event and left the business out. iCalendar knows a time, a place and attendees. It has no concept of a deposit, a cancellation window, a resource that must be free at the same time as a person, or a customer who has not shown up.

And it is a snapshot. A `.ics` attached to a confirmation is a copy that does not update on its own; if the business reschedules, the customer's copy is stale unless another message follows. The standard allowed for requests and replies, but in practice the booking platforms own the live record and send the customer a photograph of it.

## What You Still Touch

Book a haircut, a table or a demo call, click "Add to calendar", and the thing that lands in your diary is a VEVENT defined in 1998.

- [[problems/scheduling-booking-platforms/high-impact|🔴 No-Shows and the Unrecoverable Slot]] — the gap between the two diaries the format narrowed but did not close
- [[problems/scheduling-booking-platforms/low-impact-1|🟡 Multi-Resource Availability Logic]] — the resource constraints the event format does not carry
- [[problems/scheduling-booking-platforms/low-impact-2|🟡 Reminder and Confirmation Sequences]]
- [[niches/scheduling-booking-platforms/no-show-and-attendance/profile|No-Show & Attendance]]
- [[niches/scheduling-booking-platforms/multi-resource-availability/profile|Multi-Resource Availability]]

**Sources:** RFC Editor, RFC 2445 header (November 1998; Dawson, Lotus; Stenerson, Microsoft; Proposed Standard; the purpose quotation); Wikipedia, *iCalendar* (IETF Calendaring and Scheduling Working Group, Anik Ganguly as chair, RFC 5545 September 2009, RFC 2446/2447, component names); Wikipedia, *Versit Consortium*, and the vCalendar 1.0 specification hosted at cs.brown.edu (founding members, release September 18 1996, December 1996 transfer to the Internet Mail Consortium). ⚠️ **Not established:** any statement by Lotus or Microsoft that interoperability between their two customer bases was the motive — "why them" is inferred from the authorship, not quoted. No industry figure for how many booking confirmations carry an `.ics` attachment was found; "every" in the tool line describes the convention, not a measured rate.
