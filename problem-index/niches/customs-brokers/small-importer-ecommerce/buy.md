# Simplified Duty Calculator for E-Commerce Sellers

**Niche:** [[niches/customs-brokers/small-importer-ecommerce/profile|Small Importer & E-Commerce Sellers]]
**Industry:** [[industries/customs-brokers|Customs Brokers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Descartes CustomsInfo and the USITC HTS database provide tariff lookup by HTS code, but e-commerce sellers don't know their HTS code — they need a tool that takes a plain-language product description ("wireless Bluetooth earbuds with charging case") and returns the likely duty rate, including Section 301 tariffs.
**Tags:** #bert #transformers #large-language-models #revenue-impact #quick-win

## The Problem
An Amazon FBA seller considering importing wireless earbuds from China wants to know the total duty rate before committing to the purchase. They need this number to calculate their landed cost and determine whether the product is profitable at their target selling price. The seller Googles "import duty on earbuds" and finds conflicting information: "headphones are 4.9% duty" vs. "wireless devices might be duty-free" vs. "anything from China has a 25% additional tariff." The HTS database requires a 10-digit code they don't have. The seller either imports without knowing their duty rate (and is surprised by a $3,000 duty bill on arrival) or gives up on the product.

## What Already Exists
Descartes CustomsInfo provides HTS classification lookup and duty rate data — for users who know their HTS code. SimplyDuty and DutyCalculator provide some plain-language duty estimation but with limited accuracy for complex tariff scenarios (Section 301, ADD/CVD, exclusions).

## The Customization Gap
A seller-friendly duty calculator needs: (1) plain-language product description input (not HTS code); (2) automatic HTS classification suggestion from the description, with confidence level; (3) total duty rate including standard tariff + Section 301 + any ADD/CVD applicable to that product from that country; (4) landed cost calculator (product cost + shipping + duty + fees = total cost per unit); (5) alternative sourcing guidance ("if you source from Vietnam instead of China, the duty rate drops from 29.9% to 4.9%").

## Target Customer
E-commerce sellers and small importers evaluating product sourcing decisions who need duty rate information before committing to a purchase order.

## Impact If Solved
Accurate pre-purchase duty estimation prevents the $3K-$15K "duty surprise" that hits 30-40% of first-time importers. Landed cost visibility enables better product selection and pricing decisions, improving profitability for small importers by 5-15%.
