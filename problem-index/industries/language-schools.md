# Language Schools

## Profile
**Category:** Education
**Market Size:** ~$15B US language education (ESL, foreign language, test prep — TOEFL/IELTS/Cambridge); ~5,000 independent language schools and intensive English programs
**Tech Maturity:** Low-Medium — consumer apps like Duolingo and Babbel dominate self-study; institutional programs still rely on generic LMS platforms (Canvas, Moodle) or paper-based placement tests, with minimal adoption of speech analytics or adaptive curriculum tools
**Workforce:** Language instructors (often part-time, often non-native credentialed or native uncredentialed), program directors, student advisors/DSOs (Designated School Officials for visa compliance), placement testers, front-desk admin staff

## Key Pain Themes
Enrollment bottlenecks at the placement stage: every new student needs a speaking and writing assessment to be slotted into the right level, but experienced placement testers are scarce and the process is subjective — two testers can place the same student a full level apart. Mixed-proficiency classrooms are the norm because schools cannot afford to run half-empty sections at every CEFR level, so instructors spend enormous prep time differentiating materials for A2 and B1 students sitting side by side. Schools enrolling international students on F-1 or M-1 visas face SEVP/SEVIS reporting obligations (attendance thresholds, full-time enrollment verification, program extension filings) that are manual, error-prone, and carry severe consequences — a missed report can trigger a student's visa termination. Student retention is fragile: learners plateau at intermediate levels, lose motivation, and drop out before reaching the proficiency goal they enrolled for, taking tuition revenue with them.

## Current Tech Landscape
Most schools use a generic LMS (Google Classroom, Canvas, or Moodle) that was designed for K-12 or university courses, not for language-specific progression tracking across CEFR or ACTFL scales. Placement testing is either a licensed standardized instrument (CASAS, BEST Plus) that requires trained proctors and per-test fees, or an in-house oral interview graded on a rubric. SEVIS compliance is managed through the SEVIS portal directly, with DSOs manually entering records — there is no mainstream integration between school SIS systems and SEVIS. Speech-to-text and NLP tools exist but are not packaged for classroom-level proficiency diagnosis.

## Problems
- [[problems/language-schools/high-impact|🔴 High Impact: Automated Student Placement & Proficiency Diagnosis]]
- [[problems/language-schools/low-impact-1|🟡 Low Impact: Adaptive Curriculum Pacing for Mixed-Level Classes]]
- [[problems/language-schools/low-impact-2|🟡 Low Impact: Student Visa Compliance Tracking & SEVIS Automation]]
- [[problems/language-schools/worker-life-1|🟢 Worker Life: Instructor Lesson Planning for Heterogeneous Groups]]
- [[problems/language-schools/worker-life-2|🟢 Worker Life: Student Advisor Enrollment & Visa Paperwork Overload]]
- [[problems/language-schools/ml-opportunity|🔵 ML Opportunities]]
- [[problems/language-schools/ai-agents-platforms|🤖 AI Agents & Platforms]]
