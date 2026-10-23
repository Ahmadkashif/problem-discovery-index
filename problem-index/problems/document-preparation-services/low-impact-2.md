# The Thesis That Fails Format Review

**Industry:** [[document-preparation-services|Document Preparation Services]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every graduate school publishes its own thesis manual and rejects deposits for margins, page numbers and front-matter order, and the generic tools students and formatters use check none of those rules.
**Tags:** #cnns #object-detection #feature-engineering #evaluation-metrics #automation #quick-win #worker-facing

## The Problem
Before a dissertation can be deposited, and the degree conferred, a graduate school's format reviewer checks it against the institution's thesis manual. The manuals differ from school to school and sometimes by department. They set margins, including a wider binding margin on the left even though almost nothing is bound any more. They fix the order and content of the preliminary pages (title page, copyright page, abstract with a word limit, dedication, table of contents, lists of figures and tables), roman numerals before chapter one and arabic after, page numbers in the same position on landscape pages, figure captions above or below, headings consistent with the table of contents, and a PDF that embeds every font for the repository and ProQuest.

Reviewers return the deposit with a list of corrections, often more than once, and the deposit deadline for the term doesn't move. A student who misses it graduates a term later, which can mean another semester's fees, a delayed job start, and for an international student a visa timeline problem. Freelance formatters, the formatting desks inside editing firms and campus writing centres spend much of their time on these mechanical rejections. Each fix is easy, finding them all in a 250-page Word file with forty figures, three landscape tables and a reference list exported from Zotero is not, and the most common failures recur every term.

## What Already Exists
Word styles and automatic tables of contents, university-supplied Word and LaTeX templates, reference managers (Zotero, EndNote, Mendeley) that format citations to APA, Chicago or AMA, PDF preflight in Acrobat, and writing tools such as Grammarly, Paperpal and Writefull that check language. Some graduate schools publish a checklist and run workshops before each deadline, and iThenticate is used before deposit for similarity checks.

## The Customisation Gap
The generic tools know general styles; none know the manual. Templates break the moment a student pastes in a chapter written somewhere else, and a reference manager formats the bibliography but cannot see a caption on the wrong side of a figure. The gap is a checker that encodes each institution's manual as rules that can be tested: margin measurements on the rendered page, page-number position and numeral type by section, required front-matter pages in the required order, heading levels matched against the table of contents, landscape-page handling, abstract word count, font embedding and PDF/A for the repository. It should also learn from the reviewer's own rejection history, so it reports the specific corrections this school's reviewers actually return, in their own wording. It must run on the rendered PDF as well as the Word file, because the reviewer sees the PDF.

## Impact If Solved
A pre-deposit check against the actual manual would turn several rounds of rejection into one. It would cut the reviewer's queue in the busy weeks before each deadline and save the students who would otherwise slip a term. Formatters could then spend their hours on the genuinely hard cases: complex tables, equations and multi-part figures.
