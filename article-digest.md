# Proof-Point Bank

Detailed project descriptions for tailored CVs, cover letters, and interview prep. Each entry maps to target role archetypes so the system can pull the right proof points for each application.

---

### Maya AI

**Enterprise AI email triage and response platform serving 200K utility customers, projected to save $225K/month.**

**Problem:** Nationwide Energy Partners handles massive volumes of customer emails — billing questions, payment issues, account changes — all manually triaged and answered by support staff. At 200K customers, this doesn't scale. Response times lag, quality varies by agent, and the cost per interaction keeps climbing.

**Solution:** Built Maya AI end-to-end: an AI-powered email classification and response system. Inbound emails hit an n8n workflow that classifies intent via AWS Bedrock (Claude Sonnet, Nova Pro), generates a templated or AI-written reply, and routes it to a Microsoft Teams channel as an adaptive card. Managers review and tap Approve, Edit, or Deny — each triggering a dedicated handler workflow. Approve sends the response via Outlook. Edit opens a form for revisions. Deny logs the rejection and flags for manual follow-up. The system also interprets legacy Oracle CCS scripts and drafts new ones, reducing licensing costs and protecting client IP.

**Stack:** AWS Bedrock (Claude Sonnet, Nova Pro), n8n (4 production workflows), Microsoft Teams (adaptive cards + webhooks), Microsoft Outlook, Oracle CCS, AWS DynamoDB, 17 admin APIs for enterprise onboarding, 24-hour key rotation, real-time support dashboard.

**Outcome:** Projected $225K/month savings. 4 production workflows live. Enterprise onboarding with self-serve client setup, DynamoDB-backed tenant governance, and multi-channel support (chat, voice, email, SMS). HITL approval flow builds trust with non-technical stakeholders — managers stay in control without touching the underlying system.

**Archetypes this supports:** Technical AI PM, Agentic PM, AI Platform/LLMOps PM

---

### Conference Outreach System

**3-workflow n8n pipeline automating AI-generated conference outreach with human approval via Teams.**

**Problem:** The CRO needed to reach Oracle CIS conference attendees with personalized outreach but was doing it manually — writing individual emails, tracking who'd been contacted, following up. Slow, inconsistent, and not scalable for conference-sized contact lists.

**Solution:** Designed and built a 3-workflow system. Workflow A generates personalized outreach emails via AI and posts them as Teams approval cards. Workflow B handles approve/skip webhooks — approved emails send automatically via Outlook, skipped contacts get logged. Workflow C provides an edit form so the CRO can revise AI-generated copy before sending. The approval loop ensures every outgoing email has human sign-off while eliminating the drafting bottleneck.

**Stack:** n8n (3 workflows), Microsoft Teams (approval cards + webhooks), Microsoft Outlook, AI-powered email generation.

**Outcome:** Replaced manual per-email drafting with an AI-first workflow where the human role shifts from writing to reviewing. CRO maintains full control over tone and targeting while moving through contact lists at 10x the manual pace.

**Archetypes this supports:** Agentic PM, Technical AI PM

---

### Maya AI Console + Chat Widget

**Real-time conversation monitoring dashboard with live agent takeover capability.**

**Problem:** Once Maya AI was handling customer conversations across email, chat, and voice, there was no way for the operations team to see what was happening in real time. If the AI mishandled a conversation or a customer escalated, no one knew until the complaint came in. The team needed visibility into live AI interactions and the ability to intervene instantly.

**Solution:** Shipped two products: a customer-facing chat widget embedded on the client's site, and an internal Maya AI Console. The console provides a real-time feed of all active AI conversations with status indicators, sentiment signals, and a one-click agent takeover button. When a human takes over, the AI steps back and the conversation continues seamlessly in the same thread. The console also surfaces conversation history, classification decisions, and response confidence scores for post-hoc review.

**Stack:** React (frontend), FastAPI (backend), AWS Bedrock (AI engine), AWS DynamoDB (conversation state and history), deployed on Render.

**Outcome:** Operations team gained real-time visibility into all AI-handled conversations. Agent takeover capability means the AI handles the volume while humans handle the exceptions — without the customer ever noticing a handoff. Confidence scoring enables continuous improvement of the AI's classification and response quality.

**Archetypes this supports:** AI Platform/LLMOps PM, Technical AI PM

---

### Senior Assisted Living Locators

**AI recommendation product matching senior families to care communities in under 2 seconds.**

**Problem:** Five advisors were manually researching 250+ senior living communities for every consultation — checking budget fit, care levels, proximity, amenities, and partner revenue potential. With 300+ consultations per week, the manual process was the bottleneck. Advisors spent more time researching than advising, and recommendation quality varied by who picked up the call.

**Solution:** Built an AI-powered recommendation engine with an 8-factor scoring algorithm combining hard business rules (budget, care level, proximity) with AI-driven analysis (family preference matching, partner revenue optimization). Designed a two-phase architecture: first pass pre-filters by hard constraints to reduce the candidate set, second pass runs the full scoring model. Four input methods — web form, phone intake, real-time voice transcription, and CRM import — feed into the same scoring pipeline. System auto-logs to CRM and runs AI-driven follow-up that identifies missing client requirements before generating final recommendations.

**Stack:** AI scoring engine, real-time voice transcription, CRM integration, automated follow-up pipeline.

**Outcome:** 300+ weekly consultations processed. Matching time cut from minutes of manual research to under 2 seconds. API costs reduced ~70% through two-phase pre-filtering. All 5 advisors on the same recommendation quality baseline. Eliminated manual research entirely — advisors now spend their time advising.

**Archetypes this supports:** Vertical/Enterprise AI PM, Technical AI PM

---

### Vollie

**AI-powered employee coaching platform launched to first client as sole PM, from 0 to working prototype.**

**Problem:** Companies want structured peer coaching — it builds accountability, surfaces blind spots, and improves retention — but it requires trained human facilitators. At $200-500 per session, it doesn't scale past senior leadership. Mid-level employees, who benefit most from coaching, never get it.

**Solution:** Designed and shipped a voice AI moderator that runs structured coaching conversations between employee pairs. The AI facilitates the session — prompts discussion topics, manages turn-taking, ensures both participants engage — and auto-generates post-session reports covering sentiment, engagement levels, and commitments made. Reports go to the participants and optionally to their manager. Built with a privacy-first data model: conversation content stays ephemeral, only structured outputs persist. Owned the entire 0-to-1 journey as sole PM — product strategy, data model design, prototype development, and first client launch (30 employees).

**Stack:** Voice AI, structured conversation engine, automated report generation (sentiment analysis, engagement scoring, commitment tracking).

**Outcome:** Launched to first client with 30 employees. Enabled peer coaching at zero marginal facilitator cost. Privacy-first design was a key selling point for HR stakeholders concerned about recorded conversations.

**Archetypes this supports:** Technical AI PM, Forward Deployed/Solutions PM

---

### CloudApproach + Approachables Exit

**Bootstrapped two ventures from zero, scaled to 200+ clients and $5M+ deals influenced, sold both for $575K.**

**Problem:** Two different market gaps. CloudApproach: SMBs in UK and MENA needed design, web, and marketing services but couldn't afford agency retainers. Approachables: real-estate agencies needed CRM automation and marketing but were buying fragmented point solutions.

**Solution:** Built CloudApproach as a design/web and marketing agency serving 200+ clients across UK and MENA. Built Approachables as a specialized real-estate marketing and CRM automation business serving 80+ agencies. Managed a combined $200K marketing and automation budget. Ran both businesses simultaneously, handling everything from sales and client delivery to hiring and operations. When exit opportunities arose, led acquisition diligence and transition for both — complete records handoff, retention compliance, client communication.

**Stack:** Agency operations, CRM automation, digital marketing, client management at scale.

**Outcome:** $575K in combined exit value ($325K CloudApproach + $250K Approachables). $5M+ in client deals influenced across the portfolio. 95% client retention post-acquisition — buyers kept the entire operation running. Proof that the PM skillset (scoping, prioritizing, shipping, iterating) works outside of tech companies too.

**Archetypes this supports:** AI PM who can think like a founder — understands unit economics, customer acquisition, and when to exit
