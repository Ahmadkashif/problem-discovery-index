# Parent Communication and Follow-Up Workflow

**Niche:** [[niches/urgent-care/pediatric-urgent-care/profile|Pediatric Urgent Care]]
**Industry:** [[industries/urgent-care|Urgent Care]]
**Type:** Fix (Pain Point)
**One-liner:** Pediatric UC providers stop handing parents a printed discharge sheet they will lose in the car — getting automated, parent-friendly follow-up instructions, culture result notifications, and PCP handoff communications that actually reach the decision-maker.
**Tags:** #large-language-models #bert #feature-engineering #automation #workflow-orchestration #worker-facing

## The Problem
In pediatric urgent care, the patient and the decision-maker are different people. The 3-year-old cannot read discharge instructions, call for follow-up, or monitor their own symptoms. The parent receives a printed discharge sheet during a stressful visit, often while managing a crying child, and frequently cannot recall the specific follow-up instructions 24 hours later. Critical callbacks — strep culture results that take 48 hours, urine culture results, follow-up X-ray recommendations — go to the phone number on file, which may be a parent's work number or an old cell number. The child's primary care pediatrician receives no visit notification unless the parent remembers to call and report the UC visit. The result: parents call back for clarification (consuming staff time), culture results go undelivered (creating liability), and the PCP is blindsided at the next well-child visit.

## Why It's Still Broken
UC EHR systems generate discharge instructions written at an adult reading level in medical terminology. Patient portal access (Experity's patient portal) is designed for adult patients managing their own care, not for parents managing a child's care — parents must create an account for each child, navigate an unfamiliar portal, and check it proactively for results. Text and email communication features exist in some EHRs but are not configured for parent-child relationships (the text goes to "the patient's phone number" — but the patient is 3 years old). PCP notification requires manual fax or phone call from the UC, which staff deprioritize during busy shifts. No platform handles the full pediatric communication lifecycle: parent-readable discharge instructions, automated culture result notification to the parent (not the child), and structured visit summary transmission to the child's PCP.

## What a Fix Looks Like
An automated parent communication workflow that: sends discharge instructions via text/email to the parent immediately after the visit, written in plain language at a 6th-grade reading level with age-specific symptom watch guidance ("If your child's fever returns above 102F or they stop drinking fluids, return to the clinic or go to the ER"); auto-notifies the parent when culture results finalize, with actionable next steps ("Your child's strep culture is positive — we've called in a prescription for amoxicillin to [pharmacy name]"); sends a structured visit summary to the child's PCP (via Direct messaging, fax, or EHR integration) within 24 hours of the visit; and follows up 48 hours post-visit with a symptom check text ("Is [child's name] feeling better? Reply YES, NO, or WORSE"). The parent's phone number and preferred contact method are confirmed at check-in and linked to the child's chart, not the child's demographic record.

## Who Feels the Pain
Parents who leave the pediatric UC anxious about their child and unable to recall specific instructions 24 hours later. Front desk staff who spend 30-60 minutes per day fielding parent callback questions that could be answered by the discharge instructions they already received. Providers who carry liability for undelivered culture results — a positive culture with no parent notification is a malpractice risk. PCPs who learn about their patient's UC visit weeks later at a follow-up, missing the opportunity for timely care coordination.

## Impact If Fixed
Reduces parent callback volume by 30-40% through proactive instruction delivery and symptom check follow-ups. Eliminates undelivered culture result liability by creating automated, documented notification chains. Improves PCP care coordination by ensuring 95%+ of pediatric UC visits result in a PCP notification within 24 hours, compared to the current estimated rate of under 30%.
