# Master Data Management Pointed at a Purchased Universe

**Niche:** [[niches/directory-and-list-publishers/market-universe-and-firmographic-counts/profile|Market Universe & Firmographic Counts]]
**Industry:** [[industries/directory-and-list-publishers|Directory & List Publishers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Master data management builds a golden record of the companies a firm already knows; it does not test whether the vendor's universe of companies it does not yet know is complete and correctly sized.
**Tags:** #k-nearest-neighbors #logistic-regression #evaluation-metrics #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to give a revenue team the complete, de-duplicated and correctly sized universe of accounts in its market, and whoever's count survives the customer's own match test — no dead, duplicate or mis-banded firms — becomes the system of record for targeting and territories.

## The Problem
A buyer loads a purchased universe into its CRM to plan territories and finds the file mixes branches with headquarters, keeps firms that closed, and bands companies differently from its own data.

## What Already Exists
Master data management platforms (Informatica, Reltio, Profisee) match and merge records into golden records with survivorship rules; CRM-native duplicate management catches obvious duplicates.

## The Customization Gap
The buyer-side adaptation needs: a universe match report against the vendor file before purchase, separating matched, missing and vendor-only accounts; establishment-versus-entity rules so branches do not inflate counts; size-band reconciliation with the buyer's own won-deal data as ground truth; and a dead-account sample check before territories are cut. On the compiler side the same engine runs in reverse, as the trial a prospect can see.

## Target Customer
Revenue operations teams with an MDM or warehouse, and compilers' sales engineers who run trial matches.

## Impact If Solved
Territory plans start from a universe that has been tested, not trusted.
