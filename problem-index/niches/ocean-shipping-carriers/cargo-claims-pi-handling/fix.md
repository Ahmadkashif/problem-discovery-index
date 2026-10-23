# The Survey Report Read After the Time Bar

**Niche:** [[niches/ocean-shipping-carriers/cargo-claims-pi-handling/profile|Cargo Claims & P&I Handling]]
**Industry:** [[industries/ocean-shipping-carriers|Ocean Shipping Carriers]]
**Type:** Fix (Pain Point)
**One-liner:** Claims arrive as long PDFs and sit in a queue, and the deadline that matters — the time bar or the extension request — is found when someone finally reads the file.
**Tags:** #large-language-models #transformers #compliance #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to resolve each cargo claim inside the one-year Hague-Visby time bar for the least money, and whoever settles claims at the lowest paid-to-claimed ratio takes the account.

## The Problem
A claims inbox receives notices of claim, survey reports, extension requests and writs in mixed languages. A handler with a backlog reads them in arrival order. An extension request missed, or a writ filed near the one-year mark, can turn a defensible claim into a default.

## Why It's Still Broken
Nothing reads the documents on arrival; deadline tracking depends on the handler typing dates into a spreadsheet.

## What a Fix Looks Like
Read every incoming claim document on arrival, extract delivery date, time-bar date, extensions requested or granted, amount claimed and the alleged cause, and put the claim in a queue ordered by deadline and amount with the key facts summarised.

## Who Feels the Pain
Claims handlers with backlogs, insurance managers answering to the P&I club, and carriers paying claims they could have defended.

## Impact If Fixed
Suppose a carrier holds ~2,000 open claims (estimate) and misses 1% of time bars or extension requests. That is ~20 defensible claims a year lost by default (estimate), and reading on arrival removes most of them.
