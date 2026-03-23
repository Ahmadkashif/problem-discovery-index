# Payroll Service Adapted for Mixed Employee/Contractor Salon Models

**Niche:** [[niches/hair-salons-independent/commission-payroll/profile|Stylist Commission & Booth-Rent Payroll]]
**Industry:** [[industries/hair-salons-independent|Independent Hair Salons]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Payroll services like Gusto handle either W-2 employees or 1099 contractors, but most salons have both — commission employees and booth renters — requiring two parallel payment systems.
**Tags:** #automation #compliance #data-integration #workflow-orchestration

## The Problem
A salon with 4 commission employees and 4 booth renters needs: W-2 payroll with tax withholding, direct deposit, and benefits for the employees, AND 1099 invoicing with rent collection for the booth renters. Gusto handles the employees; the booth renters are paid (well, they pay the salon) through Venmo and tracked in a spreadsheet. At year-end, the owner generates W-2s through Gusto and manually produces 1099s for the contractors. If the IRS questions whether a "booth renter" is actually an employee (a common audit target in salons), the owner has no documented evidence of the contractor relationship — lease agreement, independent scheduling, own-client control.

## What Already Exists
Gusto, ADP Run, and Paychex handle W-2 payroll with full compliance. QuickBooks and FreshBooks handle 1099 contractor payments. Gusto added 1099 contractor support, but it models contractors as recipients of payment — not as tenants paying the salon rent. No payroll platform models the salon-specific dynamic where some workers are paid BY the salon (employees) and others pay TO the salon (booth renters), with both requiring year-end tax documentation.

## The Customization Gap
The payroll platform needs a salon-specific dual model: (1) W-2 payroll for commission employees with salon-specific compensation calculation, (2) rent invoicing and collection for booth-rent contractors with lease documentation, (3) combined workforce dashboard showing total labor cost (employee commissions + lost rent from vacant booths), (4) independent contractor classification documentation (automated lease agreements, scheduling independence records, tools-and-materials documentation), and (5) unified year-end tax document generation (W-2s + 1099s from one system).

## Target Customer
Salon owners running hybrid employee/contractor models who manage payroll in two separate systems and worry about worker classification audit risk.

## Impact If Solved
Consolidates two payment systems into one, reduces year-end tax preparation time by 50-70%, and provides documentation that protects against worker classification challenges (potential penalties of $5,000-50,000 per misclassified worker).
