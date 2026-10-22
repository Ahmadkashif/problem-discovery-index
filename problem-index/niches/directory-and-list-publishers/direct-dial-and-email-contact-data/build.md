# Reachability Scored Before the Rep Dials

**Niche:** [[niches/directory-and-list-publishers/direct-dial-and-email-contact-data/profile|Direct-Dial & Email Contact Data]]
**Industry:** [[industries/directory-and-list-publishers|Directory & List Publishers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Contact vendors tell a rep that a number is "verified" when what the rep needs is the probability it reaches the named person today.
**Tags:** #gradient-boosting #survival-analysis #logistic-regression #evaluation-metrics #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to sell contacts that reach the named person this week — a direct dial that connects, an email that lands — and whoever shows the higher measured connect rate on the customer's own territory wins the renewal.

## The Problem
A sales development rep makes dozens of dials a day from a list of contacts all labelled verified. Some reach the person, most reach voicemail, a switchboard or someone who left a year ago. The label is binary and dated; the reality is a probability that decays from the day the record was checked.

## Why Nobody Has Built This
Vendors verify records in batches and sell a status, because a probability invites scrutiny. The label that would train a score — whether a real dial connected to the named person — sits in customers' dialers and is not contributed back in structured form.

## What to Build
A per-contact reachability score with an expected decay curve, trained on dial and email outcomes contributed by customers under clear terms, re-verification calls, job-change signals and number line type. Survival models estimate time to staleness by seniority and industry; the score ranks the rep's list and triggers re-verification where a dial is likely wasted. Customers who contribute outcomes get better scores, which builds the label pool.

## Target Customer
Contact data vendors competing on connect rate, and the sales development leaders who buy from them.

## Impact If Built
Reps spend dials on contacts likely to answer, and the vendor can show a measured connect-rate advantage on a buyer's own territory — the exact test the renewal turns on.
