# Illustrator Pipeline and Art Revision Management

**Niche:** [[niches/independent-publishers/childrens-book-independents/profile|Children's Book Independents]]
**Industry:** [[industries/independent-publishers|Independent Publishers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No platform manages the children's book illustration pipeline — from illustrator sourcing and portfolio review through concept sketches, color studies, final art, and print-ready file delivery — in a structured workflow with version control.
**Tags:** #workflow-orchestration #data-integration #ai-platform #worker-facing

## The Problem
A children's picture book has 32 pages with 15–20 illustrations, each going through 4–8 revision rounds: thumbnail sketches, refined sketches, color studies, final art, and print corrections. The art director manages this process across 8–15 books simultaneously, with each illustrator working on a different schedule, using different file formats, and requiring different levels of creative direction. Feedback happens in email threads with annotated PDFs attached. File versions accumulate in Dropbox folders with names like "spread_4_v3_FINAL_actually_final.psd." When the art director needs to compare the current version to the approved sketch from 4 months ago, they dig through email. When an illustrator misses a deadline, the entire production schedule shifts — but nobody recalculates the cascade because there's no connected timeline.

## Why Nobody Has Built This
Creative project management tools (Frame.io for video, Figma for design) focus on screen-based creative work, not print production. The children's book illustration workflow has unique requirements: spread-level organization (not page-level), physical mockup stages (dummy books), color gamut considerations for CMYK printing, and a revision approval process that involves the author, art director, and sometimes the editor. The market (500–1,000 independent children's publishers worldwide) is small enough that general-purpose tools haven't specialized, but large enough to support a focused vertical product.

## What to Build
A web-based illustration management platform where: (1) each book project has a spread-by-spread view showing current art status (sketch/color study/final), (2) illustrators upload versions that are automatically organized by spread and stage, (3) the art director provides feedback using on-image annotation (like Frame.io but for still images), (4) approval workflows track who approved what and when, (5) all versions are retained with one-click comparison between any two stages, (6) production timeline auto-adjusts when a stage runs late, showing downstream impact, and (7) print-ready file collection packages all approved art with correct specs. Integrates with Dropbox/Google Drive for file storage but provides the organizational layer on top.

## Target Customer
Art directors and production managers at children's book publishers managing 5+ illustration-driven titles per year.

## Impact If Built
Reduces art direction overhead by 30–40%, saving 8–12 hours per week. Eliminates the 5–10% of illustration deliveries that use wrong specs or outdated versions, preventing $1,000–$3,000 per title in production rework. Shortens average production timeline by 2–3 months through systematic deadline tracking and cascade alerting.
