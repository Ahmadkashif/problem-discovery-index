# Matchback for Mail That Attribution Tools Don't Do

**Industry:** [[direct-mail-agencies|Direct Mail Agencies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every agency rebuilds the same matchback by hand for every client — fuzzy-matching buyers' names and addresses to the mail file inside a response window — because attribution software is built for clicks, not for a postcard that sends someone to a store.
**Tags:** #k-nearest-neighbors #logistic-regression #causal-inference #hypothesis-testing #evaluation-metrics #data-integration #automation

## The Problem
A mailed piece rarely carries its own proof of response. Some buyers enter a promo code or call a tracked number; most type the brand's URL, walk into a store, or order on a marketplace weeks later. So agencies credit mail by matchback: they take the client's orders, donations or applications for a window after the in-home date — commonly 60 to 90 days — and match each buyer back to the mail file by name and address, then roll results up by list, segment, offer and version.

The work is tedious and error-prone. Buyer records arrive from three or four systems with different address formats; households move, use a spouse's name or an apartment number the mail file lacks; the same buyer may have been on two rented lists and the house file; and the client's analytics team wants the result reconciled with their own web attribution before the next circulation plan is due. Each client's matchback becomes a bespoke SQL project maintained by one analyst.

## What Already Exists
Multi-touch and marketing-mix attribution tools, analysed under [[marketing-attribution-vendors|Marketing Attribution Vendors]], plus web analytics (GA4) and customer data platforms with identity resolution. Address standardisation and household matching exist in postal software and data-quality tools (Melissa, Experian's data quality products). Print-and-mail APIs such as Lob and Postalytics offer basic response dashboards for promo codes and QR scans.

## The Customisation Gap
Mail matchback needs logic the generic tools don't carry: CASS-standardised address matching at household and individual level with configurable match rules, so that a "Bob" at the right address counts and a different household in the same building does not; response windows that start at the in-home date (not the drop date) and vary by product; priority rules for a buyer who appears on several source lists, consistent with the merge/purge priority the list owners were paid on; exclusion of buyers who were already active customers, so house-file credit is not inflated; and a holdout comparison wherever the client allows one. Output must roll up to the list, select and version cells the strategist planned, which no web attribution tool knows exist.

## Impact If Solved
A standard matchback engine turns a two-week analyst project per campaign into an overnight job, gives strategists cell-level results before the next plan rather than after it, and produces numbers the client's finance team, the list owners and the agency all compute the same way — which ends the recurring argument about whose attribution is right.
