# Hearing Notice Tracking & In-Absentia Prevention

**Niche:** [[niches/immigration-law/removal-defense-asylum/profile|Removal Defense & Asylum]]
**Industry:** [[industries/immigration-law|Immigration Law]]
**Type:** Fix (Pain Point)
**One-liner:** Clients in removal proceedings miss court hearings because notices go to old addresses, resulting in in-absentia removal orders (deportation) — a permanent, life-destroying consequence of an address change that no current system prevents.
**Tags:** #automation #data-integration #workflow-orchestration #compliance #worker-facing

## The Problem
Immigration court hearing notices are sent by postal mail to the respondent's last known address on file with EOIR. Respondents in removal proceedings are often recent arrivals, asylum seekers, or undocumented individuals living in unstable housing situations — they move frequently. When a respondent moves without updating their address with both EOIR and their attorney, the hearing notice goes to the old address. The respondent doesn't know about their hearing. They don't appear. The immigration judge orders them removed in absentia. This order is immediately enforceable — the person can be detained and deported. Reopening an in-absentia order requires proving "exceptional circumstances" or that notice was not properly given, a difficult legal standard. EOIR data shows that approximately 20-25% of all removal orders are issued in absentia. Many of these are people who wanted to attend their hearing and had valid claims but simply didn't receive the notice. The attorney — if one is involved — may not know the hearing was scheduled if they also didn't receive the notice or if the client retained them after the hearing was set.

## Why It's Still Broken
EOIR has no electronic notification system for respondents — all notices go by mail. There is no requirement for respondents to provide email addresses or phone numbers, though some courts have begun accepting them. The EOIR hotline allows checking case status by phone, but respondents (many of whom don't speak English) rarely know to call it. Attorneys can check the hotline but must do so case-by-case. No system sends proactive reminders to respondents about upcoming hearings through channels they actually check (text messages, WhatsApp, phone calls in their language).

## What a Fix Looks Like
A hearing reminder and address verification system with three components: (1) at intake, collect the respondent's phone number, email, and WhatsApp contact (in addition to mailing address), with multilingual consent for electronic notifications, (2) automated hearing date monitoring through EOIR status checking for all active cases, with reminders sent via text/WhatsApp/call in the respondent's language at 30 days, 7 days, and 1 day before each hearing, (3) quarterly address verification outreach — a text/WhatsApp message asking "are you still at [address]? Reply YES or update your address" — with automatic EOIR address change filing when a respondent reports a move. The system must support Spanish, Chinese, Haitian Creole, Portuguese, Hindi, and Arabic at minimum.

## Who Feels the Pain
Respondents who are ordered deported because they didn't receive a piece of mail — losing their asylum claim, their family connections, and their safety. Attorneys who discover that a client they were representing was ordered removed in absentia at a hearing they didn't know about.

## Impact If Fixed
Even a 10% reduction in in-absentia removal orders would affect thousands of cases per year nationally. For a legal aid organization with 100 active removal cases, preventing 5-10 in-absentia orders per year means 5-10 people who get to present their cases instead of being deported without a hearing — the most consequential outcome of any tool in immigration law.
