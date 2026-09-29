# Lineage: Recruiting Tech Vendors

**Industry:** [[industries/recruiting-tech-vendors|Recruiting Tech Vendors]]
**Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**The tool:** Resumix — a scanner, OCR unit and Sun workstation server that read paper resumes, extracted skills, degrees and job titles into fields, auto-categorised each applicant, matched them to open requisitions and printed the acknowledgment letter
**Builder:** Resumix
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A requisition in 1988 was answered by a stack of paper.

A Fortune 500 recruiting office received hundreds or thousands of resumes a week. Clerks sorted, copied and routed them; each recruiter kept a private filing system by job category, month and surname. One company told candidates asking about status to allow three weeks and call again. Resumes were lost.

The search side was worse. The contemporary case study describes a Sun Microsystems recruiter looking for C and Unix engineers who had to carry **2,400 resumes from the previous three months** home to read them. The alternatives were a newspaper ad costing thousands, or an executive search firm at **20–35% of first-year salary**. Plain OCR with keyword search already existed and failed on exactly the query that mattered: it could not find "C".

## What Got Built

A turnkey box. A clerk fed a scanner roughly **250 two-page resumes an hour** and pressed *process*. The software split each page image into text blocks before OCR, so that a date range sitting in a left margin stayed attached to the job beside it. A pattern matcher with proximity operators — match "C" only near another programming language; treat "RDB" and "RDBMS" as "relational database" — pulled out names, addresses, phone numbers, degrees, employers, titles and skills.

A rule-based expert system then scored the extracted skills and titles across **34 job categories** and assigned each applicant to zero or more of them. Recruiters searched by category, skill, degree, school and area code; a *match resumes to open requisitions* button surfaced new fits. Every action was logged to the applicant's record.

The first unit, Resumix 2000, went live at **Sun Microsystems in January 1989**; AMD, Bank of America, National Semiconductor, Digital, Texas Instruments, General Motors and AT&T followed by mid-1990.

## Who Built It, And Why Them

Resumix Inc., of Sunnyvale, founded by **Steve Leung**, who is credited with first envisioning the system; the engineering was led by Yul J. Inn and Dave C. Sobotka. Development began in **April 1988** and took nine person-months, on two of the company's own Sun-3/50 workstations and a third lent by Sun.

The shape of the product follows from who its first customers were. Late-1980s Silicon Valley hardware firms were hiring engineers in volume, received resumes by the thousand, and — crucially — already ran Unix workstations. A start-up could sell them a scanner-plus-server appliance on hardware they trusted, with Sun itself as a design partner. The skill vocabulary was engineering vocabulary because the pain was engineering hiring.

The system also absorbed a compliance job. The 1990 write-up counts, among its savings, the elimination of a separate equal-employment-opportunity and affirmative-action tracking system: Resumix recorded every applicant and every disposition anyway. The record of rejection was built in from the start, as a by-product of paperwork, not as evidence to learn from.

## What It Cost

**The categorisation replaced judgement with rules, and was sold on that basis.** A former Digital HR manager is quoted: the key to its success was automatic categorisation — "This task is done by skilled people. Resumix removes these people from the loop." At AMD a test against three senior HR staff on 40 resumes was called a draw, with the machine far cheaper.

A draw on 40 resumes is not validation. Once extraction and category rules sat between the applicant and the recruiter, whatever a resume did not say in the knowledge base's words was invisible — and candidates, then an industry of federal "Resumix resume" guides, learned to write for the parser.

## What You Still Touch

Every applicant tracking system still stores every rejection in a disposition field, and still grades none of them. That field descends from a system that logged decisions to replace a paper compliance tracker, not to ask whether the decisions were right.

- [[problems/recruiting-tech-vendors/high-impact|🔴 The System Records Every Rejection and Learns From None of Them]]
- [[problems/recruiting-tech-vendors/low-impact-1|🟡 Sourcing, Search and Application Volume]]
- [[problems/recruiting-tech-vendors/worker-life-2|🟢 The Candidate Who Never Hears Back]]
- [[niches/recruiting-tech-vendors/rejection-audit/profile|Rejection Audit]]
- [[niches/recruiting-tech-vendors/screening-and-matching/profile|Screening & Matching]]
- [[niches/recruiting-tech-vendors/counterfactual-evidence/profile|Counterfactual Evidence]]

**Sources:** Lance Tokuda, "Computers Assist Humans in Human Resources", *IAAI-90 Proceedings*, AAAI, 1990, pp. 179–188 (primary: the 2,400-resume and 20–35% fee figures, 250 resumes/hour, 34 categories, April 1988 start, Sun January 1989, customer list and dates, AMD test, Bahlo quote, EEO/affirmative-action saving, and the acknowledgment naming Steve Leung as founder and president with Yul J. Inn and Dave C. Sobotka as VPs — note the author wrote as a Resumix insider, so the savings figures are vendor claims); Wikipedia, *Yahoo HotJobs* (HotJobs bought Resumix of Sunnyvale in 2000; later use at USAJOBS); CB Insights and Crunchbase company profiles (founded 1988, Sunnyvale); search-result summary of GAO report GGD-94-127 (White House personnel office adopted Resumix in 1993). ⚠️ **Not established:** Steve Leung's background before Resumix, and why he in particular chose HR as the problem — searched, and results returned only an unrelated Hong Kong designer of the same name. The HotJobs purchase price was not found. The link between Resumix-style extraction and today's disposition-field problem is this note's reading, not a documented design intent.
