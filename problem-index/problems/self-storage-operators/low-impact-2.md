# Competitor Rates Collected by Phone and Screenshot

**Industry:** [[self-storage-operators|Self-Storage Operators]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Market data vendors sell monthly street-rate indices and web scrapers can read any rate page. What a store needs is today's rate for the same unit, with the same features and promotion, at the five stores its customers compare it with.
**Tags:** #large-language-models #feature-engineering #time-series-forecasting #data-integration #automation #quick-win

## The Problem
Street rates move daily. The REITs' systems reprice every store's web rates each day, and Yardi Matrix reports that national advertised rates fell 1.8% year over year in September 2026, with REIT asking rates down more than independents' (search summary). At a regional operator or third-party manager, the district manager keeps the competitor survey. Once a week, sometimes once a month, they open each nearby competitor's website, note the 10x10 climate-controlled rate and the promotion, screenshot the page, and call stores that hide rates behind "call for price". The figures go into a spreadsheet that feeds web-rate changes for the stores the district manager covers.

The survey is slow, partial and hard to compare. One competitor's "10x10" is a 10x10 on the third floor with no elevator, another's is drive-up. One advertises, say, $59 with "first month free" and a $29 admin fee, another $89 with nothing off. Sold-out sizes vanish from websites, so the survey shows only what competitors still have to sell. By the time the spreadsheet is complete, the REIT across the street has repriced twice.

## What Already Exists
TractIQ collects advertised street and web rates monthly across its database of 68,243 facilities, with history from March 2018. Yardi Matrix publishes monthly national and metro reports, and Radius+ and StorTrack sell rate and supply data. General web-scraping tools and browser extensions can read any page. Revenue-management tools from Prorize, Cubby and Monument take a rate feed as an input, and the moving-industry view of this data is profiled at [[niches/moving-companies/storage-facility-market-data/profile|Self-Storage Market Data]].

## The Customisation Gap
The generic feeds are built for investors and monthly trend lines. The store needs a daily, unit-for-unit comparison. The storage-specific layer is a normalisation model. It maps each competitor's unit labels to standard size, climate control, floor and access type, door width and vehicle suitability. It parses promotion text ("first month $1", "50% off 3 months", "free truck") into an effective rent over the expected stay, and it adds admin fees. It separates web, in-store and phone rates and treats a vanished size as sold out rather than unknown. It also has to let the store choose its own comp set, because customers compare by drive time, not radius. A language model can read promotion text and odd unit labels. The comp set and the effective-rent rules have to come from the people who price storage.

## Impact If Solved
Automating the weekly survey gives a district manager covering 10–15 stores back ~3–5 hours a week (estimate). It also moves pricing from a monthly snapshot to a daily one. If that lifts revenue per available square foot by ~1% at a store collecting ~$700,000 a year (estimate), the store earns ~$7,000 a year more.
