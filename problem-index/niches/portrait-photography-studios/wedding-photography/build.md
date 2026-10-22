# A Date-Aware, Style-Matched Reply

**Niche:** [[niches/portrait-photography-studios/wedding-photography/profile|Wedding Photography]]
**Industry:** [[industries/portrait-photography-studios|Portrait Photography Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every inquiry is a bid for one specific Saturday, and the reply goes out as a generic template with the same price sheet whether that date is a sold-out June Saturday or a quiet November Friday.
**Tags:** #large-language-models #contrastive-learning #k-nearest-neighbors #gradient-boosting #evaluation-metrics #revenue-impact #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to sell a fixed calendar of peak-season Saturdays — each date sold once and worthless once it passes — to the right couple at the right price a year or more ahead, and whoever fills the prime dates at full price earliest takes the season.

## The Problem
Inquiries carry the signals that matter for selling a date: which date, the venue, guest count, a line about what the couple loves. The photographer knows, roughly, how in demand that date is and has years of galleries from that venue or one like it. The reply ignores both: a canned email, one pricing PDF, a generic portfolio, sent whenever the photographer next has a free evening.

## Why Nobody Has Built This
CRMs automate sending, not composing or pricing. Date-level demand lives in the photographer's memory of past seasons. Portfolio tagging by venue, light and style is tedious, so nobody does it. And photographers fear an automated reply will sound like one.

## What to Build
A reply engine that starts from the date asked for: how many inquiries that date and similar dates have drawn in past seasons, how many prime Saturdays remain, and therefore what price and package to quote and whether to offer a hold. It finds the photographer's own galleries closest to the couple's venue and style using image embeddings, drafts the reply in the photographer's voice from their past emails, and offers consult slots. It sends on rules the photographer sets or queues for one-tap approval.

## Target Customer
Owner-photographers booking roughly 20–40 weddings a year (estimate) whose prime dates sell out and whose off-season dates do not.

## Impact If Built
Prime dates quoted at what they are worth, off-season dates offered where they will sell, and every couple seeing relevant work before a rival replies.
