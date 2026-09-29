# Rule Change Detection Across Every Court That Publishes

**Niche:** [[niches/legal-practice-software/court-rules-deadline-content/profile|Court Rules & Deadline Content]]
**Industry:** [[industries/legal-practice-software|Legal Practice Software]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Court rules are public, published on the web, and change constantly, and the legal industry's method for tracking them is analysts visiting websites — which is why coverage stops exactly where small-firm practice begins.
**Tags:** #bert #large-language-models #transformers #change-point-detection #evaluation-metrics #confidence-intervals #compliance #automation
**Contested on:** Every serious competitor in court rules content is fighting to detect a rule, standing order or judge-specific practice change before a deadline is computed wrongly from it — and whoever holds detection latency lowest takes the account.

## The Problem
A judge revises a standing order changing the time to respond to a particular motion type. It is posted as a PDF on a chambers page. No notice is issued. Firms with cases before that judge compute deadlines from the old rule until somebody notices — a clerk mentions it, an opposing counsel files differently, or a deadline is missed. The information was public from the moment it was posted. The gap between publication and the industry knowing is measured in weeks to months, and in the tail it is never.

## Why Nobody Has Built This
Content maintenance is a services cost centre that vendors size to the coverage they sell, and expanding coverage means hiring analysts, so coverage has a natural ceiling at the courts most customers care about. The technical work is unglamorous and genuinely broad: thousands of court websites with no common structure, documents in every format including scanned PDFs, and changes that are frequently a single sentence inside a forty-page document. Distinguishing a substantive rule change from a reformatted page is the hard part and is where naive monitoring produces so much noise that it is worse than nothing. Nobody has been willing to fund the breadth.

## What to Build
A monitoring pipeline over every court, division and judge page that publishes rules, standing orders or practices — fetch, extract, normalise, diff, and classify. The classifier's job is the one that matters: deciding whether a diff changes a computable obligation, which requires understanding rule text well enough to distinguish a renumbering from a changed period. Confirmed substantive changes are routed to a content analyst with the old and new text, the affected rule identifiers, and a proposed edit, so the analyst reviews rather than discovers. Nothing is published to customers unreviewed, because an incorrect deadline rule is the one failure this industry cannot absorb. The measurement the product is judged on is detection latency from publication to analyst alert, per court, reported openly.

## Target Customer
Court rules content providers, practice management vendors maintaining rule sets in house, large firms with docketing departments, and legal malpractice carriers, whose interest in this is direct and whose willingness to fund it is underexplored.

## Impact If Built
Coverage stops being bounded by analyst headcount, which is what allows state trial courts, specialty divisions and individual judges' standing orders — the courts where small firms practise and where coverage is thinnest today — to be monitored at all. Cutting detection latency from months to days on the long tail addresses the highest-severity failure mode in legal software, and the analyst's job changes from searching to adjudicating.
