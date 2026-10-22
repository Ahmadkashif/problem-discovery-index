# Court-Specific Proof of Service

**Industry:** [[legal-support-services|Legal Support Services]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every server-management tool can merge job data into an affidavit template; none knows that each state, court and service method demands different facts in the return, so returns get rejected or defaults get vacated over omissions a rules engine would have caught.
**Tags:** #large-language-models #decision-trees #feature-engineering #evaluation-metrics #compliance #automation #quick-win

## The Problem
A completed serve ends in a return: an affidavit or proof of service filed with the court, which the plaintiff's attorney relies on to take a default if the defendant does not answer. What that document must say depends on where the case is and how service was made. California uses a Judicial Council form and, for substituted service, wants a declaration showing reasonable diligence before the papers were left with someone else. New York affidavits carry a physical description of the person served and, in the city, must match the server's electronic log. Texas, Florida and Illinois each specify their own contents and who may sign. Substituted service, posting, service on a corporation's registered agent and service on a minor each add requirements. A national network dispatching work into thousands of courts, or a local firm taking overflow from out of state, is drafting returns for rules it does not know well.

The failure shows up late. A clerk rejects the return, or the attorney does not notice a missing element until the defendant's lawyer moves to vacate the default months later, at which point the server is asked to explain an affidavit they barely remember.

## What Already Exists
ServeManager and similar server-management platforms store job details, GPS and photos, and generate affidavits from templates the firm configures. National networks such as ABC Legal and Proof generate their own returns. Generic document-automation tools (HotDocs, Documate, Word mail merge) can produce any form, and court self-help sites publish blank forms.

## The Customisation Gap
What is missing is a maintained rules layer keyed to court, case type and service method: the required facts for each return, the diligence threshold before substituted service is allowed, notarisation or declaration-under-penalty format, filing deadlines for the return, and how the city's or state's recordkeeping rules (NYC's GPS and electronic-log requirements, for instance) must line up with what the affidavit asserts. The tool should block a return that lacks a required element, flag a return whose facts contradict the device log, and pull the right form for an unfamiliar court rather than leaving the server to find it. The content must be curated and versioned as rules change, which is why template builders have not done it.

## Impact If Solved
Returns that are complete the first time remove clerk rejections and late scrambles, and take away a common ground for vacating defaults. For a small server firm taking out-of-state overflow, it removes the hour of research per unfamiliar court that currently decides whether the job is worth accepting.
