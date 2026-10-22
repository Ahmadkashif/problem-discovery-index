# Bottom-Up Forecasts From a Data Room's Statements

**Niche:** [[niches/music-publishers/catalogue-acquisition-and-underwriting/profile|Catalogue Acquisition & Underwriting]]
**Industry:** [[industries/music-publishers|Music Publishers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A buyer prices a catalogue on a blended multiple because turning ten years of statements into song-by-source forecasts takes longer than the auction allows.
**Tags:** #time-series-forecasting #survival-analysis #bayesian-inference #gradient-boosting #confidence-intervals #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to forecast a catalogue's next ten years of earnings, song by song, more accurately than the rival bidders, and whoever forecasts best wins the catalogues worth winning and walks away from the ones that would be overpaid.

## The Problem
A seller's banker opens a data room holding years of royalty statements from PROs, the MLC, sub-publishers and sync licensees, in dozens of layouts. Bids are due in weeks. The acquisitions team has time to clean the top songs, apply a decay assumption to the rest and argue about the multiple. Song-level questions go unanswered: which songs are still rising, which depend on one sync, and which income is a one-off back payment.

## Why Nobody Has Built This
Statement normalisation is tedious, catalogue-specific work, and each buyer has treated it as a deal cost rather than a product. The decay knowledge sits in valuers' and buyers' heads and spreadsheets. Buyers also see sellers' data only under NDA, which keeps anyone from pooling it.

## What to Build
A pipeline that ingests data-room statements in any format and normalises them into song-by-source quarterly series. On those series sits a hierarchical forecasting model, trained on the buyer's own owned catalogues, that projects each song's earnings with intervals. It adds a hazard term for revival events and flags songs inside a Section 203 termination window. The output is a valuation pack whose every number traces back to a statement line.

## Target Customer
Acquisitions heads at catalogue funds and major publishers, and the lenders and asset-backed security arrangers who finance them.

## Impact If Built
Faster, song-level bids. On a $100M catalogue, a forecast that halves the error on the top twenty songs is worth millions of dollars of avoided overpayment. Lenders get forecasts they can audit instead of a multiple they have to trust.
