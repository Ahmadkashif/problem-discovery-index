# Shareholder Report and Fund Document Production

**Industry:** [[asset-managers|Asset Managers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** A fund complex produces thousands of regulated documents a year whose numbers all come from the same accounting records, and ties them out by hand on a deadline.
**Tags:** #large-language-models #bert #evaluation-metrics #feature-engineering #data-integration #compliance #workflow-orchestration #automation

## The Problem
A US fund complex with a hundred funds produces, every year, annual and semi-annual tailored shareholder reports for each share class under the SEC rule that took effect in July 2024, Form N-PORT holdings filings, Form N-CSR, prospectus and statement of additional information updates, monthly or quarterly fact sheets, and Form N-PX vote records. A UCITS range adds KIDs, factsheets and SFDR periodic disclosures. Each document is built from the same fund accounting, holdings and performance data, laid out differently, and reviewed by legal and compliance.

The production work is a tie-out: the expense ratio in the shareholder report must match the prospectus fee table methodology, the performance must match the performance system, the holdings must match the N-PORT, and the fund's name must still pass the Names Rule 80% policy test. When a number changes late — a restated accrual, a corrected benchmark return — it must change in every document that carries it.

## What Already Exists
Financial document vendors and platforms — DFIN's Arc suite, Broadridge, Workiva, and fund-reporting specialists — handle typesetting, EDGAR filing and some data binding. Fund administrators supply the accounting data. Fact sheet engines such as Kurtosys generate marketing documents from data feeds.

## The Customisation Gap
The tools bind data into templates; they do not understand the regulatory logic of the content. What fund reporting needs on top is lineage from every printed figure back to the record that produced it, regulation-aware validation (is this the expense figure the rule requires, computed the way the rule requires, for this share class?), and change propagation that tells the team which documents a corrected figure touches. The narrative sections — management's discussion of fund performance in a tailored shareholder report, now required to be concise and plain — also have to agree with the attribution numbers and with the commentary the portfolio specialists published separately.

## Impact If Solved
Fund reporting is a deadline-driven cost centre whose failures are public filings with errors in them. Lineage and rule-aware validation turn a manual tie-out across thousands of documents into exception review, and make late corrections a propagation problem rather than a search.
