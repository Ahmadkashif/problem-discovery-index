# Web Change Monitoring Adapted to Judicial Publication

**Niche:** [[niches/legal-practice-software/court-rules-deadline-content/profile|Court Rules & Deadline Content]]
**Industry:** [[industries/legal-practice-software|Legal Practice Software]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Website change monitoring is a commodity product sold for a few dollars a month to marketers and compliance teams, and the legal industry's rule maintenance is done by analysts opening browser tabs.
**Tags:** #bert #transformers #large-language-models #evaluation-metrics #confidence-intervals #hypothesis-testing #automation #compliance
**Contested on:** Every serious competitor in court rules content is fighting to detect a rule, standing order or judge-specific practice change before a deadline is computed wrongly from it — and whoever holds detection latency lowest takes the account.

## The Problem
A content analyst maintains a list of court pages and checks them on a rotation. The rotation is set by importance, so the busiest federal districts are checked often and a state trial court's specialty division is checked rarely. Most checks find nothing. When a check finds a changed page, the analyst must determine whether anything substantive changed, which often means comparing a forty-page document against memory. The work is an almost perfect description of what change-monitoring software was built to do, applied by a person.

## What Already Exists
Change monitoring services — Visualping, Distill, ChangeTower and dozens of others — are cheap, mature and handle scheduling, fetching, rendering and visual or textual diffing. Web scraping infrastructure is a commodity. PDF text extraction, including for scanned documents, is reliable. Free legal data infrastructure exists too: CourtListener and the Free Law Project have built substantial public court data capability. Almost every component of a monitoring pipeline is purchasable or free.

## The Customization Gap
The adaptation is in what counts as a change and in the breadth of the crawl. It requires: (1) normalising before diffing — court sites regenerate pages, reorder navigation and change headers constantly, and a raw diff on those produces noise that buries the signal; (2) document-level rather than page-level tracking, since rules live in linked PDFs whose URLs change while their content does not, and vice versa; (3) semantic classification of each diff into substantive, editorial or cosmetic, which is the only way the alert volume becomes workable for a content team; (4) crawl discovery rather than a maintained list, because the long tail is exactly the set of pages nobody put on a list, and judges' pages appear and move; and (5) per-source reliability tracking, so the team knows which courts publish in ways the pipeline handles well and which need a human on a rotation anyway.

## Target Customer
Rules content providers and vendor content teams, and the docketing departments at litigation firms that maintain their own supplementary rule knowledge.

## Impact If Solved
An analyst team that receives classified, substantive-only alerts across a crawl covering thousands of courts is doing a different job than one checking a rotation, and the coverage expansion is where the value is. The tooling cost is close to negligible relative to the analyst salaries it redirects, which makes this the clearest buy-and-adapt case in the industry.
