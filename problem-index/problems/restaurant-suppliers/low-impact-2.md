# Restaurant-Specific Catalog Search for Smallwares and Equipment

**Industry:** [[restaurant-suppliers|Restaurant Suppliers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** A chef searching for "a prep table that fits in a 30-inch space next to the fryer" gets zero useful results from standard product catalogs built around manufacturer part numbers.
**Tags:** #bert #transformers #word-embeddings #transfer-learning #attention-mechanisms #norms-and-inner-products #evaluation-metrics #feature-engineering

## The Problem
Independent restaurant suppliers carry 5,000-15,000 SKUs in smallwares and equipment (cutting boards, prep tables, sheet pans, portion scales, cold-holding units). When a restaurant operator needs something, they describe it in workflow terms: "I need a cold rail that fits my 48-inch sandwich station" or "something to keep sauces at temp during service." The supplier's catalog is organized by manufacturer and product category, not by kitchen workflow or dimensional constraint. Sales reps become human search engines, flipping through PDFs and calling the office to find the right item — often taking 24-48 hours to respond to what should be a 5-minute lookup.

## What Already Exists
E-commerce search tools like Algolia, Elasticsearch, and Amazon-style faceted search handle product discovery well for standardized retail goods. Restaurant supply e-commerce platforms like WebstaurantStore and Katom have basic search, but they serve retail consumers browsing by category, not restaurant operators solving a specific kitchen layout or workflow problem.

## The Customisation Gap
The search layer needs to understand restaurant kitchen context: station types (prep, line, expo, dish), common equipment dimensions, NSF certification requirements, gas vs. electric compatibility, and workflow adjacency (a cold rail is searched alongside sandwich prep, not alongside other refrigeration). A fine-tuned language model needs to map natural-language kitchen workflow queries to product attributes that aren't in the manufacturer's spec sheet but are known to experienced sales reps. The training data is in years of rep-to-customer email and text threads where reps translated kitchen needs into product recommendations.

## Impact If Solved
Reps reclaim 3-5 hours/week currently spent on manual catalog lookups. Restaurants get same-day product recommendations instead of waiting 24-48 hours, reducing the chance they order from WebstaurantStore or Amazon instead. Equipment and smallwares margins (25-40%) are the highest in the distributor's catalog — faster conversion directly hits profitability.
