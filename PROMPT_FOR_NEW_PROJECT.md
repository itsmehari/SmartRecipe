# Prompt Instruction: Shape a New B.Sc. Computer Science Final Year Project

Use the text below as your **initial prompt** when you start with a new project. Copy-paste it into the AI chat and **replace the placeholders** in square brackets with your actual project details.

---

## COPY FROM HERE (replace [brackets] with your details)

```
I have a B.Sc. Computer Science final year project that I need to bring to submission shape. Please help me in the following order.

**1. PROJECT & COLLEGE DETAILS**
- Project name: [e.g. SmartRecipe / Library Management / E-Commerce]
- One-line description: [e.g. An ingredient-driven recipe recommendation system]
- College name (full): [e.g. Dhanraj Baid Jain College (Autonomous)]
- College location: [e.g. Thoraipakkam, Chennai – 600097]
- Degree: B.Sc. Computer Science
- Your name placeholder: [Your Full Name]
- Roll/Register no. placeholder: [Your Roll No]
- Guide name placeholder: [Guide Name]
- Guide designation: [e.g. Assistant Professor, Department of Computer Science]
- Academic year: [e.g. 2024 – 2025]

**2. TASKS TO DO**

A. **Analyze the project folder**
   - List folder structure, main files, tech stack (language, framework, database).
   - Identify gaps: e.g. data files not used, placeholders, duplicate files, report vs code mismatch.
   - Give a short “plan” or checklist of what should be fixed or added.

B. **Implement the plan (if any)**
   - Fix gaps you found: e.g. wire CSV/DB into code, align filters with data, fix labels, remove duplicates.
   - Do not create new features unless I ask; focus on making existing report and code consistent.

C. **Single project report**
   - If I have multiple report files (e.g. “continuation” or “chapters”), merge them into ONE project report file (e.g. [ProjectName]_Project_Report.md).
   - Structure: Front matter (title, certificate, declaration, acknowledgement), Abstract, Chapters 1–12 (Introduction, System Study, Requirements, Design, Modules, Coding, Datasets, Results, Limitations, Future Work, Business Model, Conclusion), References, Appendices.
   - Add a proper List of Abbreviations (AI, ML, DB, API, etc. as relevant).

D. **College-specific front matter**
   - Add to the report:
     - Title page with college name, address, NAAC/affiliation if known, project title, your name, roll no., guide, department, academic year.
     - Bonafide certificate (text with placeholders for signatures: Guide, HOD, Principal).
     - Declaration by student (original work, under guidance, not submitted elsewhere).
     - Acknowledgement (college, department, guide, HOD, family/friends).
   - If you don’t know the college address/formal name, search the web for “[College name] [location] address” and use the official details.

E. **References**
   - Convert “example references” or placeholders into a proper numbered list (e.g. framework docs, language docs, university/college link, NAAC if relevant). I can add more later in the same format.

F. **Presentation for PPTX**
   - Create a single Markdown file (e.g. [ProjectName]_Presentation.md) that can be converted to PPTX.
   - Slides: Title, Contents, Introduction, Problem, Objectives, System Study, Solution, Requirements & Tech Stack, Design/Architecture, Implementation, Results, Limitations, Future Work, Conclusion, Thank You.
   - Use --- as slide breaks so tools like Marp or Pandoc can convert to PPTX.
   - If I use Marp, add Marp front matter (marp: true, theme: default, paginate: true, size: 16:9) and use <!-- _class: lead --> for title and thank-you slides.

G. **Export report to DOCX**
   - When the report Markdown is ready, convert [ProjectName]_Project_Report.md to [ProjectName]_Project_Report.docx using Pandoc (or tell me the exact command if Pandoc is available).

**3. DELIVERABLES I EXPECT**
- One consolidated project report (Markdown) with college front matter and placeholders for name/roll no/guide/date.
- One presentation Markdown (Marp-ready) for PPTX.
- Report also as DOCX (if conversion is possible).
- Short note on what I still need to do (e.g. fill placeholders, add TOC in Word, add screenshots, signatures).

Start with step A (analyze the project folder) and then proceed in order. Ask me only if something is unclear (e.g. which file is the “main” report or which college exactly).
```

---

## HOW TO USE

1. **Before pasting:** Replace every `[bracket]` with your real project name, college name, your name, roll no., guide name, designation, and academic year.
2. **Paste** the whole block into the AI chat (Cursor/ChatGPT/Claude etc.).
3. **Share the project folder** (or open the workspace) so the AI can see your code and report files.
4. **Run step by step:** Let the AI do A → B → C → D → E → F → G; you can say “do the next step” if you prefer one at a time.
5. **Afterwards:** Fill placeholders in the report and DOCX, add TOC/screenshots/signatures in Word, export the presentation to PPTX with Marp.

---

## QUICK VERSION (minimal prompt)

If you want a shorter prompt:

```
I have a B.Sc. CS final year project in this folder. Please:
1) Analyze the folder and list structure, tech stack, and gaps.
2) Merge all report parts into one [ProjectName]_Project_Report.md and add college front matter (Title, Bonafide, Declaration, Acknowledgement, List of Abbreviations) for [College name], [Location]. Search the web for official college details if needed.
3) Create [ProjectName]_Presentation.md with slide breaks (---) and Marp front matter for PPTX.
4) Convert the report MD to DOCX with Pandoc.
Project: [name]. College: [full name], [place]. Use placeholders for my name, roll no., guide name, year.
```

---

*Save this file and reuse it for your next project by updating the placeholders.*
