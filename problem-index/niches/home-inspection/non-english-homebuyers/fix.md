# Walkthrough Interpretation Coordination

**Niche:** [[niches/home-inspection/non-english-homebuyers/profile|Non-English Homebuyers]]
**Industry:** [[industries/home-inspection|Home Inspection]]
**Type:** Fix (Pain Point)
**One-liner:** The inspection walkthrough — where the inspector explains findings to the buyer in person — is the buyer's primary channel for understanding their home's condition, but non-English-speaking buyers either miss the walkthrough entirely, bring an unqualified family member to translate, or stand silently while the agent summarizes selectively.
**Tags:** #speech-recognition #worker-facing #quick-win #large-language-models

## The Problem
After the 2-3 hour on-site inspection, the inspector walks through the home with the buyer and agent, pointing out key findings and explaining their significance. This 30-45 minute walkthrough is where buyers ask questions, learn about maintenance priorities, and develop confidence in their purchase decision. For non-English-speaking buyers, this walkthrough is either: (1) conducted through a family member translator (a 14-year-old daughter translating technical terms she doesn't know — "the step flashing is failed" becomes "something on the roof is broken"); (2) conducted through the agent who speaks both languages (the agent selectively translates, minimizing concerns to keep the deal alive); or (3) skipped entirely, with the buyer receiving only the written report they can't read. Professional interpreters are rarely used because they cost $100-200/hour and must be booked in advance, adding friction to an already tight scheduling process.

## Why It's Still Broken
Real-time technical interpretation requires someone who speaks both languages and understands home construction terminology — a rare combination. The 25,000 home inspectors in the US include perhaps 1,000 who speak Spanish and fewer than 100 who speak any Asian language. Hiring bilingual inspectors is not scalable — the skill gap is in construction knowledge, not language. Technology has recently caught up: real-time speech-to-text, machine translation, and text-to-speech are individually capable but haven't been combined into a domain-specific interpretation tool for the inspection walkthrough use case.

## What a Fix Looks Like
A real-time interpretation tool on the inspector's phone or tablet that: (1) listens to the inspector's English explanation via speech recognition; (2) translates the text into the buyer's language using domain-trained translation with inspection terminology accuracy; and (3) displays the translation on the screen (for the buyer to read) and optionally plays audio translation. The system uses the inspection report's structured data as context — when the inspector says "this electrical panel," the system knows from the report that it's a Federal Pacific Stab-Lok and includes that context in the translation. For the Q&A portion, the system works bidirectionally: the buyer speaks their question, it's translated to English text for the inspector, and the inspector's response is translated back. This isn't perfect real-time interpretation — it's closer to a shared text display with audio support — but it's dramatically better than a teenager translating "flashing" as "shiny thing."

## Who Feels the Pain
Non-English-speaking buyers who make the largest purchase of their lives without understanding the inspection findings. Inspectors who want to serve these clients well but can't communicate effectively, feeling professionally inadequate. Agents who mediate between the inspector and buyer, adding translation to their already complex role.

## Impact If Fixed
Enables effective walkthroughs for the 8-10% of homebuyers with limited English proficiency, improving their purchase decisions and post-purchase outcomes. Reduces buyer's remorse and post-closing complaints from non-English-speaking buyers who didn't understand defects at the time of inspection. Differentiates inspectors in multilingual markets, increasing referrals from agents serving non-English-speaking communities.
