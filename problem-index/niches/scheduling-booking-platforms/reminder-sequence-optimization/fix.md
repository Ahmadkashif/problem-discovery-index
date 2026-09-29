# Delivery Is Reported, Effect Is Not

**Niche:** [[niches/scheduling-booking-platforms/reminder-sequence-optimization/profile|Reminder Sequence Optimisation]]
**Industry:** [[industries/scheduling-booking-platforms|Scheduling & Booking Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Reminder reporting shows messages sent and delivered, which tells an operator that the feature ran, and nothing about whether it changed anyone's behaviour.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #logistic-regression #quick-win #revenue-impact #automation
**Contested on:** Every serious competitor here is fighting to establish what a reminder should actually say, when, and through which channel, for whom — and whoever produces that evidence takes the category, because a feature deployed in every product has never been tested by anybody.

## The Problem
An operator opens the reminders report: four hundred and twelve sent, four hundred and eight delivered, sixty-one opened. They have no idea whether this improved attendance, whether the timing is right, whether the second reminder is doing anything, or whether the customers who did not open it are the ones who did not show. They also cannot tell whether the two no-shows last Tuesday received a reminder at all. Every one of those questions is answerable from the same database the report is generated from.

## Why It's Still Broken
The reminder feature was implemented on messaging infrastructure whose native metrics are delivery and engagement, and those metrics were surfaced because they were free. Connecting a reminder to an attendance outcome requires joining the messaging log to the appointment record, which is a small piece of work nobody has done. And nobody has asked, because operators do not know what to ask for and vendors report what the messaging provider hands them.

## What a Fix Looks Like
Report the outcome instead of the delivery. Attendance rate among appointments that received a reminder against those that did not, which most operators have naturally through failures and gaps and which is a starting observation rather than a causal claim — and should be labelled as such. Attendance by reminder timing, which operators vary informally and which produces a usable pattern. Failed and undelivered reminders as a specific list, since a wrong number is a silent and complete failure currently invisible. Which no-shows received reminders and which did not, appointment by appointment, since that is the operator's actual question and takes one join. Response rates where the reminder asks for confirmation, and the attendance difference between those who confirmed and those who did not, which is usually large and immediately suggests an intervention. And a small holdout, offered as an option with the reasoning explained, because a few percent of appointments left unreminded turns every one of the above from a suggestive comparison into an answer.

## Who Feels the Pain
Operators configuring a feature with no feedback; customers receiving messages tuned by nobody; and vendors whose most-used feature is unevaluated in their own product.

## Impact If Fixed
Joining the messaging log to the attendance record is a small piece of work that converts a delivery report into an effectiveness report. The undelivered-reminder list is a quick win with a real hit rate, and the optional holdout makes the whole report causal rather than suggestive.
