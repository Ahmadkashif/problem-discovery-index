# Automatic Time Capture from Activity Streams

**Industry:** [[small-law-firms|Small Law Firms]]
**Type:** High Impact
**One-liner:** Small firm attorneys who under-bill by 20-35% because they don't capture time in real-time recover $50,000-150,000 per attorney annually — not by working more, but by getting credit for work already done.
**Tags:** #transformers #attention-mechanisms #loss-functions #cross-validation #evaluation-metrics #feature-engineering #backpropagation #revenue-impact

## The Problem
Legal billing depends on time entries: a description of the work done, the client and matter it applies to, and the time spent. The standard workflow — attorney works throughout the day and reconstructs time entries at day's end — is structurally broken. Memory-based reconstruction consistently under-bills by 20-35% because attorneys forget the 8-minute call, the 12-minute email review, the 20-minute research tangent. At $300-500/hour billing rates, 2 hours of unbilled daily work represents $60,000-100,000 in annual revenue loss per attorney. This is not a discipline problem — it is a capture problem. The work is done; the billing record doesn't exist because the friction of creating it in real-time is too high.

## Why It's Unsolved
Building automatic time capture requires monitoring attorney activity across multiple work surfaces — email, phone, document editing, court filing systems, case management system — and doing three things with that data: (1) identifying which activity represents billable work; (2) classifying which client and matter the activity applies to; (3) generating a useful time entry description that satisfies billing narrative standards. Current tools handle the monitoring step but fail at the classification and narrative generation steps. The matter classification problem is particularly hard: an attorney who works on 30-50 active matters simultaneously receives email from multiple clients throughout the day, and matching an email to a specific matter (particularly when the email doesn't mention the matter name) requires contextual judgment.

## What a Solution Looks Like
A background activity monitor that captures: email metadata (sender, recipient, subject, duration), calendar events (meeting duration, attendees, meeting title), document edit events (file name, edit duration), phone call logs (duration, direction, contact identity), court filing system activity. An NLP classifier maps each activity to the most likely client/matter using email patterns, contact names, document file names, and matter keywords. An LLM generates a billing narrative from the activity context. The attorney reviews a daily "suggested time entries" inbox — approving, editing, or discarding each entry rather than creating from scratch. Unmatched activities are flagged for manual matter assignment.

## Impact If Solved
A two-attorney firm recovering 1.5 hours of missed billing per attorney per day at $350/hour recovers $255,750 annually — far exceeding any reasonable SaaS cost. At the market level, the 360,000+ solo and small firm attorneys represent a market where automatic time capture could recover billions in currently lost revenue.
