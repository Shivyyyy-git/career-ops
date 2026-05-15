# User Profile Context -- career-ops

<!-- ============================================================
     THIS FILE IS YOURS. It will NEVER be auto-updated.
     
     Customized for Shivam Sharma — AI Product Manager.
     6 AI PM archetypes with mapped proof points and CV keywords.
     
     The system reads _shared.md (updatable) first, then this
     file (your overrides). Your customizations always win.
     ============================================================ -->

## Your Resume Formatting Hard Rules

**RULE 0 — Never mention Career-Ops in user-facing deliverables (HARD, NO EXCEPTIONS):**
The resume, cover letter, Application Q&A, LinkedIn DMs, and application-form answers must NEVER reference Career-Ops Pipeline or "the harness that produced this application". This applies to anything a recruiter, hiring manager, or interviewer could see. Internal evaluation reports in `reports/` and the Notes column in `data/applications.md` are allowed to mention it (those are private). Substitution rules when stripping: signal-from-noise examples → Maya AI ("100+ requests across NEP, Moreno Valley, Delta Utilities") or SALL ("300+ weekly consultations, 8-factor scoring"); "how did you find this role" → "Found through LinkedIn / Ashby / portal" with no harness framing; Resume Projects section → Conference Outreach Automation, VaultIQ, or Simon Vision fraud detection. Sweep every user-facing artifact before delivery: grep for "Career-Ops", "career-ops", "Career Ops", "career ops".

**RULE 1 — No orphan lines under 3 words (HARD, NO EXCEPTIONS):**
In every rendered resume (HTML, PDF, LaTeX, or any output), **no line of body text may contain fewer than 3 words.** Bullets that wrap and leave 1–2 dangling words on the last line are forbidden. Before generating the PDF, simulate line-wrap at the template column width and rewrite any bullet that would produce a <3-word orphan line. **The fix is logic and word choice, not deletion** — find a synonym, restructure the sentence, or add a meaningful qualifier so the line breaks cleanly. Never just chop words to compress; never sacrifice impact.

**MANDATORY AUDIT STEP after every resume PDF generation:** run `node audit-orphans.mjs <path-to-resume.html>` from the career-ops directory. If the audit reports any violations, rewrite the offending bullets in the HTML, regenerate the PDF, and re-audit. Only deliver the resume to the user when the audit returns `Total violations: 0`. Do not skip this step.

## Your Resume Delivery Protocol — Four-Pass Audit (HARD, MANDATORY)

**Never hand the resume to the user without running all four audits below.** Do not optimize for tokens or speed — accuracy and quality outrank cost.

**Audit Pass 1 — Format integrity:**
- Page does not overflow at the bottom or break awkwardly anywhere.
- Run `node audit-orphans.mjs <resume.html>` → must return `Total violations: 0`.
- Any line that would be <3 words: rewrite the bullet with logic (synonyms, restructure, qualifier) so the line breaks cleanly without losing impact. Search for alternative phrasings before settling.
- Spacing, margins, and section gaps look consistent.

**Audit Pass 2 — JD reference check (deep, honest):**
- Re-read the full JD. List every must-have, nice-to-have, and keyword.
- Walk the resume and confirm each one is reflected somewhere — bullets, summary, skills line. Flag misses.
- Add coverage by **truthfully** mapping existing experience to the JD's language. Diplomatic and honest reframing of real work is allowed and encouraged. **Inventing experience, metrics, tools, or titles is forbidden.**
- If a hard requirement genuinely isn't there, surface it to the user before delivering rather than faking it.

**Audit Pass 3 — Strict ATS compliance:**
- Standard section headers (Summary, Experience, Education, Skills, Projects). No clever renaming.
- No tables, no text boxes, no columns that break ATS parsing. No images, no icons in HTML content, no graphics for substantive text.
- Plain bullet characters. Consistent date format. Standard fonts (Arial, Helvetica, Calibri, Times).
- Keywords from the JD appear in natural prose, not stuffed.
- File saved as PDF with selectable text (not a flattened image). Filename: `Shivam Sharma Resume.pdf`.
- Contact info as plain text at the top, not in a header/footer that ATS may strip.

**Audit Pass 4 — Human tone (final, blocking):**
- Read the resume end-to-end as if you were a recruiter who has never heard of Maya AI, VaultIQ, SALL, NEP, ESC, or any of the project names. Does every line make sense in plain English? Does it sound like a real person wrote it?
- **No em-dashes (—). No en-dashes (–) as punctuation.** Use periods, commas, or restructure the sentence. Hyphens in compound words (AI-powered, end-to-end) are OK only when grammatically natural; prefer alternatives where possible.
- Strip AI tells: "leveraging", "leveraged", "seamless", "robust", "comprehensive", "spearheaded", overly parallel triplets ("efficient, scalable, and reliable"), generic verb-noun openings on every bullet.
- The recruiter should feel: this person is the best candidate they could have, every claim makes sense, every project is understandable even to a non-technical reader, the writing is delightful to skim.
- If a non-technical reader couldn't tell what you actually did from a bullet, rewrite it.

**Company-fit sentence in the Summary:**
- Before generating, do a quick web search on the company: what they build, recent news, mission, who their customers are.
- Add **one or two sentences** in the Summary that name a specific reason this company excites the candidate. Concrete, not generic. Example: "Drawn to [Company] for [specific product/mission/customer outcome] because [link to candidate's proven work]."
- If web research returns nothing usable, fall back to a sentence anchored to the company's stated mission from the JD itself.

**Only after all four audits pass and the company-fit sentence is in place do you announce the resume is ready.**

## Output Folder + File Naming (HARD)

Folder: `output/{Company} - {Role}/`. Files inside use ATS-favored names with the candidate name as prefix on every deliverable: `Shivam Sharma Resume.{md,html,pdf}`, `Shivam Sharma Cover Letter.{md,html,pdf}`, `Shivam Sharma Application Q&A.{md,html,pdf}`, `Shivam Sharma LinkedIn Messages.{md,html,pdf}`. `Job Description.md` stays prefix-less (internal reference, no candidate name needed). Spaces are fine for modern ATS parsers.

## LinkedIn Outreach Messages (HARD, MANDATORY)

For every JD I process — especially LinkedIn JDs that name a hiring team — also produce:
`output/{Company} - {Role}/Shivam Sharma LinkedIn Messages.md` + `.html` + `.pdf`

Inside, draft personalized DMs for every named contact (founder/CEO, hiring manager, recent hires, recruiters). For non-LinkedIn JDs, do a quick web search to surface the equivalent contacts (founders, heads of product) and draft for them. Each contact gets two versions:

- **Short (≤300 chars)** — LinkedIn connection-request note
- **Long (~600-800 chars)** — InMail / post-connection message

Tone is critical: completely human, contractions, varied sentence length, specific to that person, mentions the application, clear and small ask (15-min coffee or Zoom, no agenda). Same no-em-dash and no-AI-tell rules as the rest. Open with first name, never "Hi team".

## Application Q&A Companion Document (HARD, MANDATORY)

For every resume you generate, also produce a companion file in the same output folder, in **all three formats** (.md + .html + .pdf — never md alone):
`output/{Company} - {Role}/Application Q&A.md` + `Application Q&A.html` + `Application Q&A.pdf`

After writing the .md, mirror it to .html with the cover-letter CSS (Calibri 10.5pt body, 1.35 line-height, Letter @ 0.55in/0.7in margins), then `node generate-pdf.mjs <input.html> <output.pdf> --format=letter`. Multi-page PDF is fine for Q&A — readability beats single-page squeeze. Same audit rules apply (no em-dashes, no AI tells, no Career-Ops mentions).

**Contents:**
- Pre-fill answers to common application questions tailored to the company and role.
- At minimum, always include: **"Why this company?"** (2–3 short paragraphs anchored to the company-fit research from the resume summary, expanded with one concrete example from the candidate's work that ties to the company's mission/product).
- Add other questions if they're in the JD or known to be in the company's application form: "Tell me about a time you...", "What's your biggest accomplishment?", "Why are you leaving your current role?", "What are your comp expectations?", "When can you start?", "Are you authorized to work in the US?".
- During conversation, if the user mentions a specific application asks for question X, add an answer for X to this file.

Answers must follow the same human-tone rules as the resume (no em-dashes, no AI tells, plain English, concrete examples).

## Learn-From-Corrections Protocol (HARD, MANDATORY)

**Every time the user corrects something during a resume edit, save the correction as a memory immediately.** Do not wait for the user to remind you. The point: any rule the user has to repeat twice is a rule I failed to learn. Aim for zero repeats.

**Triggers — save a feedback memory when the user:**
- Corrects wording, framing, a metric, a title, a date, or a project name
- Tells you a phrase, word, or pattern to avoid ("don't say leveraged", "drop the em-dashes", "stop calling it Maya")
- Tells you a phrase, word, or pattern to use ("always say AI Product Manager/Engineer", "lead with the founder card")
- Rejects a structural choice (section order, summary length, bullet density)
- Validates a non-obvious choice ("yes that framing worked, keep doing it")

**How to save:**
- Write a new file at `/Users/shivamsharma/.claude/projects/-Users-shivamsharma-Documents-Shivy-career-ops/memory/feedback_resume_<topic>.md` with frontmatter (`name`, `description`, `type: feedback`) and a body that includes the rule, **Why** (the user's stated reason or context), and **How to apply** (when this rule fires).
- Add a one-line index entry to `MEMORY.md`.
- If a memory on the same topic already exists, update it instead of creating a duplicate.

This is the compounding mechanism: every correction makes the next resume better automatically.

## Your Target Roles

**ESC role title allowlist (HARD RULE):** the ESC Partners line on the resume is the only role that flexes per JD, and it MUST come from this allowlist:

- AI Product Manager
- AI Product Engineer
- AI Product Builder
- AI Product Owner
- AI Product Lead

The combined slash form `AI Product Manager/Engineer` is also allowed (joins two allowlist entries) and is the safe default when the JD is ambiguous or asks for both build and lead motion. **Any title outside this allowlist is forbidden for ESC**, even if the JD uses different wording (e.g., "Product Manager" without "AI" → render as "AI Product Manager"; "Founding PM" → "AI Product Manager" or "AI Product Builder"; "Engineering Manager" → "AI Product Engineer"; "Solutions Architect" → keep slash form).

The substance is the same across the allowlist: you build and ship production AI end-to-end. The variation is which face of the work the JD weights.

**How to pick within the allowlist:**
- Hands-on building, 0→1, dev tools → `AI Product Engineer` or `AI Product Builder`
- Roadmap ownership, strategy, vision → `AI Product Manager` or `AI Product Lead`
- Backlog, sprints, agile → `AI Product Owner`
- Hybrid or unclear → `AI Product Manager/Engineer` (slash form)

| Archetype | Thematic axes | What they buy |
|-----------|---------------|---------------|
| **AI Product Engineer / Builder** | Hands-on shipping, Claude Code, Markdown-based development, agent orchestration, AI Factory / reusable delivery assets, 0-to-1 builds with no dedicated backend team | An engineer-PM hybrid who ships production AI without waiting for a team — writes the code, runs the workflows, owns the outcome |
| **Technical AI PM** | LLM integration, prompt engineering, API design, model evaluation, production AI systems | A PM who ships — writes specs in code/prompts, works directly with LLM APIs, makes architecture decisions |
| **AI/ML PM** | Model training, embeddings, fine-tuning, data pipelines, ML evaluation, A/B testing | A PM who owns the ML model lifecycle end-to-end — from eval to data pipelines to production |
| **Agentic PM** | Agents, tool-use, function calling, HITL, orchestration, approval workflows, n8n, automation | A PM who designs multi-agent systems with human-in-the-loop workflows that actually ship |
| **AI Platform / LLMOps PM** | Observability, monitoring, dashboards, developer tooling, internal platforms, reliability | A PM who builds the internal AI platform and operational tooling that engineering teams depend on |
| **Vertical / Enterprise AI PM** | Industry-specific, enterprise, regulated, compliance, domain expertise | A PM who applies AI to a specific vertical with deep domain understanding and measurable customer outcomes |
| **Forward Deployed / Solutions PM** | Customer-facing, pre-sales, implementation, consulting, integrations | A PM embedded with customers shipping custom AI — owns the relationship and the delivery |

## Your Adaptive Framing

| If the role is... | Lead CV framing with... | Primary proof points | Secondary proof points | Keywords to inject in tailored CV |
|-------------------|-------------------------|----------------------|------------------------|-----------------------------------|
| **AI Product Engineer / Builder** | Shipping production AI on Claude Code as sole AI engineer | Maya AI (Oracle CCS overlay, 26-language, 2.5 months, sole AI on staff), VaultIQ (air-gapped Claude Opus) | Career-Ops Pipeline (Claude Code harness), Vollie (0-to-1 voice AI) | Claude Code, Markdown-based development, reusable delivery assets, AI Factory, agent orchestration, end-to-end, ship, build, hands-on |
| **Technical AI PM** | Architecture decisions and hands-on AI building | Maya AI (end-to-end build: Bedrock model routing, n8n workflows, React console, Teams integration) | Conference Outreach System, Vollie (0-to-1 voice AI) | LLM integration, prompt engineering, API design, model evaluation, production AI, end-to-end, PRD, technical specification, system architecture |
| **AI/ML PM** | ML system design and evaluation methodology | Maya AI (intent classification + Bedrock model routing), SALL (8-factor scoring algorithm, two-phase pre-filtering) | VentureForge (AI scoring + grading), Simon Vision (XGBoost fraud detection) | ML evaluation, model selection, data pipeline, A/B testing, scoring algorithm, embeddings, intent classification, model lifecycle, fine-tuning |
| **Agentic PM** | Workflow orchestration and human-in-the-loop design | Conference Outreach System (3-workflow: generate → approve → send), Maya AI (approve/edit/deny handler workflows) | Vollie (voice AI moderator with structured turn-taking) | multi-agent, orchestration, HITL, approval workflow, tool-use, function calling, n8n, automation, workflow design, agent reliability |
| **AI Platform / LLMOps PM** | Platform thinking and operational tooling | Maya AI Console (live monitoring + agent takeover, confidence scoring, conversation history) | Maya AI (17 admin APIs, 24-hour key rotation, DynamoDB tenant governance, real-time dashboard) | observability, monitoring, developer tooling, internal platform, reliability, dashboards, operational metrics, agent takeover, confidence scoring |
| **Vertical / Enterprise AI PM** | Domain impact and customer outcomes | NEP/energy via Maya AI (200K customers, $225K/mo savings), SALL (300+ weekly consultations, 250+ communities) | Vollie (employee coaching, 30-person pilot), VentureForge (50+ MBA students, education) | enterprise AI, vertical, regulated, compliance, domain expertise, customer outcomes, ROI, industry-specific, scalability |
| **Forward Deployed / Solutions PM** | Client relationships and hands-on delivery | NEP client work (enterprise onboarding, 17 admin APIs, multi-channel support), CloudApproach ($5M+ deals influenced, 200+ clients) | Conference Outreach System (built for CRO), SALL (built for 5 advisors) | customer-facing, implementation, consulting, pre-sales, integrations, client delivery, enterprise onboarding, fast delivery, prototype to production |

## Proof Point → Archetype Mapping

<!-- Quick reference: which article-digest.md entries to pull for each archetype -->

| Proof Point | Tech AI PM | AI/ML PM | Agentic PM | Platform PM | Vertical PM | Solutions PM |
|-------------|:----------:|:--------:|:----------:|:-----------:|:-----------:|:------------:|
| Maya AI (core) | **primary** | **primary** | strong | strong | **primary** | strong |
| Maya AI Console | strong | — | — | **primary** | — | — |
| Conference Outreach | strong | — | **primary** | — | — | strong |
| SALL | — | **primary** | — | — | **primary** | — |
| Vollie | strong | — | strong | — | strong | strong |
| CloudApproach Exit | — | — | — | — | — | **primary** |
| VentureForge (cv.md) | — | strong | — | — | strong | — |
| Simon Vision (cv.md) | — | strong | — | — | — | — |

## Your Exit Narrative

Use the candidate's exit story from `config/profile.yml` to frame ALL content:

> **The story:** AI Product Manager who builds, not just specs. Built Maya AI — a production AI email triage system for a major energy client — end-to-end: architecture, n8n workflows, AWS Bedrock model routing, React console, Teams approval flows. Promoted to AI Product Manager after shipping Maya AI — still underpaid at $46K for $190K+ market-value work. Looking for a team that matches scope to title and title to comp.

- **In PDF Summaries:** Bridge from builder-who-shipped to PM-who-leads — the hands-on experience is the differentiator, not a liability
- **In STAR stories:** Reference proof points from article-digest.md, always grounding in shipped outcomes with metrics
- **In Draft Answers:** The transition narrative appears in the first response — "I don't just write PRDs, I build the thing"

## Your Cross-cutting Advantage

Frame profile as **"AI PM who builds and ships, not just specs"** — adapts framing per archetype:

- **For Technical / ML roles:** Lead with architecture decisions, model selection, system design
- **For Agentic / Platform roles:** Lead with workflow orchestration, operational tooling, reliability
- **For Vertical / Solutions roles:** Lead with client outcomes, domain impact, delivery speed
- **Always:** The founder background (CloudApproach + Approachables exits) signals ownership mentality — this PM doesn't wait for permission

## Your Portfolio / Demo

- Portfolio: https://shivamsportfolio.webflow.io/ (being revamped)
- When to share: All roles — the portfolio demonstrates the "PM who builds" narrative

## Your Comp Targets

- Target range: Open (speed-to-offer optimization)
- Minimum: $75K
- Currency: USD
- Location flexibility: Anywhere in US; open to remote, hybrid, or on-site
- Visa: STEM OPT (F-1), H-1B eligible — do NOT filter on sponsorship, but always surface H-1B data in reports

**General guidance:**
- Use WebSearch for current market data (Glassdoor, Levels.fyi, Blind)
- Frame by role title, not by skills
- Contractor rates are typically 30-50% higher than employee base

## Your Negotiation Scripts

**Salary expectations:**
> "Based on market data for this role, I'm targeting a range that reflects the scope of work. I'm flexible on structure — what matters is the total package and the opportunity to own AI product outcomes end-to-end."

**Geographic discount pushback:**
> "The roles I'm competitive for are output-based, not location-based. My track record — Maya AI, two exits, production AI systems — doesn't change based on postal code."

**When offered below target:**
> "I'm comparing with opportunities in a higher range. I'm drawn to [company] because of [reason]. Can we explore [target]?"

**The founder card (when comp is low but role is right):**
> "I took a $46K role because the scope was right — and I shipped a $225K/month AI system. I'm not optimizing for ceiling right now, I'm optimizing for the right team and the right scope. But the comp needs to be fair."

## Your Location Policy

**In forms:**
- Location: Rochester, NY
- Willing to relocate anywhere in the US
- Timezone: EST
- Remote/hybrid/on-site: all acceptable

**In evaluations (scoring):**
- Remote dimension for hybrid outside your area: score **3.0** (not 1.0) — relocation is on the table
- Only score 1.0 if JD says "must be on-site 4-5 days/week, no exceptions" in a location you can't reach
- International roles: flag visa considerations but don't auto-disqualify
