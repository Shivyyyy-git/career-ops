# Story Bank — Master STAR+R Stories

This file accumulates your best interview stories over time. Each evaluation (Block F) adds new stories here. Instead of memorizing 100 answers, maintain 5-10 deep stories that you can bend to answer almost any behavioral question.

## How it works

1. Every time `/career-ops oferta` generates Block F (Interview Plan), new STAR+R stories get appended here
2. Before your next interview, review this file — your stories are already organized by theme
3. The "Big Three" questions can be answered with stories from this bank:
   - "Tell me about yourself" → combine 2-3 stories into a narrative
   - "Tell me about your most impactful project" → pick your highest-impact story
   - "Tell me about a conflict you resolved" → find a story with a Reflection

## Stories

<!-- Stories will be added here as you evaluate offers -->
<!-- Format:
### [Theme] Story Title
**Source:** Report #NNN — Company — Role
**S (Situation):** ...
**T (Task):** ...
**A (Action):** ...
**R (Result):** ...
**Reflection:** What I learned / what I'd do differently
**Best for questions about:** [list of question types this story answers]
-->

### [Agent Design / Customer Embed] Maya AI for NEP — per-account multi-channel agent on Oracle CCS
**Source:** Report #123 — Actively AI — Agent Product Manager
**S (Situation):** NEP runs everything on Oracle CCS — billing, outages, service requests, payment plans — with no AI layer. 200K+ residents, multi-language gap for non-English customers, response times lagging, cost-per-interaction climbing. ESC was non-AI before me.
**T (Task):** Ship a per-account multi-channel agent that handles 70-80% of first-touch volume autonomously while keeping non-technical NEP supervisors in control. Single-customer deploy first, then template for any Oracle CCS utility.
**A (Action):** Architected on AWS Bedrock (Claude Opus/Sonnet/Nova routing) + FastAPI orchestration + n8n production workflows + React supervisor cockpit + Microsoft Teams approval cards + 11 Labs 26-language voice. Built the supervisor cockpit before the agent was working — trust UX first, autonomy second. Spun off a standalone email-triage agent in week 8 to replicate the pattern across email channels.
**R (Result):** Live at NEP in 2.5 months as sole AI on staff. 70-80% first-touch autonomous, 100+ manual manager emails removed per day, ~$225K/mo projected savings. Rolling out at Moreno Valley Electrical Utility, piloting at Delta Utilities.
**Reflection:** The unlock was the supervisor cockpit + takeover button before model accuracy was where I wanted it. Trust UX is the gate, not model quality. The same playbook transfers to Per-Account Agents at GTM scale: ship the operator-control surface (approval, takeover, audit log) first, then turn up autonomy as confidence grows.
**Best for questions about:** "Tell me about your most impactful project," "Describe an AI product you've shipped end-to-end," "How do you ship complex systems fast as the sole technical lead?", "Tell me about working with non-technical operators," "Describe a multi-channel system you designed."

### [Continuous Optimization / Customer Co-Design] SALL recommendation engine
**Source:** Report #123 — Actively AI — Agent Product Manager
**S (Situation):** 5 senior-care advisors at Senior Assisted Living Locators were spending most of their hours researching 250+ communities per consultation. 300+ weekly consultations. Recommendation quality varied by who picked up the call.
**T (Task):** Cut research time to under 2 seconds while keeping advisor judgment in the loop, and bring all 5 advisors to the same recommendation-quality baseline.
**A (Action):** Mapped 8 scoring factors (budget, care level, proximity, family preference, partner revenue) — half from interviews with advisors mid-consultation, half from CRM data. Designed a two-phase pre-filter: hard-constraint pass (budget + care level + radius) drops the candidate set 90% before the AI scoring stage runs, cutting API costs ~70%. Wired four input methods (web form, phone, voice transcription, CRM import) into one pipeline. Auto-logs to CRM + runs AI-driven follow-up to identify missing requirements.
**R (Result):** 300+ weekly consultations live; matching <2 sec; ~70% API cost cut; quality baseline equalized across all 5 advisors.
**Reflection:** Customer co-design beats user surveys. Two of the eight scoring factors only emerged from sitting with advisors during real consultations — they would not have shown up in a structured discovery interview. For Per-Account Agents at AI revenue platforms: shadow paying customers' actual GTM workflows, then write the optimization PRD. The signal is in the live work, not in the post-call summary.
**Best for questions about:** "How do you approach product discovery?", "Tell me about an optimization you ran," "Describe how you cut costs / improved efficiency," "How do you work with frontline operators?", "How do you think about evals and performance data?"

### [Customer-Embedded GTM Delivery] Conference Outreach playbook for the ESC CRO
**Source:** Report #123 — Actively AI — Agent Product Manager
**S (Situation):** The ESC CRO needed to reach 800+ Oracle CIS conference attendees with personalized outreach. Manual drafting was the bottleneck — slow, inconsistent, no audit trail. The CRO didn't trust pure-AI sending without sign-off.
**T (Task):** Build an AI-creative + HITL pipeline that the CRO actually adopts (so it's used the day after I ship it, not the week after). Ship the operator workflow + the technical pipeline together.
**A (Action):** Built 3 workflows: (a) AI generates personalized outreach + posts as Microsoft Teams adaptive cards in the CRO's channel; (b) approve/skip webhook handler — approved emails send via Outlook automatically, skipped logged; (c) edit form so the CRO can revise AI-drafted copy before sending. Sat with the CRO for two iteration cycles before locking the approval-card UI.
**R (Result):** Day-one adoption. CRO went from manual per-email drafting to reviewing 80+ pre-drafted cards/day. Audit trail and revision history persist in n8n logs. The pattern is now reused across 3 other ESC outreach motions.
**Reflection:** Embedding with the customer + iterating the approval surface together is what made it stick. If I'd shipped the pipeline first and asked the CRO to "use it," I'd be on iteration 4 of a system nobody was touching. The lesson translates directly to Per-Account Agents: the agent has to be co-designed with the SDR/AE who will run it, not handed to them as a fait accompli.
**Best for questions about:** "Tell me about a customer-embedded engagement," "Describe an HITL approval system you designed," "How do you drive product adoption?", "Tell me about working with a senior stakeholder who didn't trust AI initially," "How do you ship something that gets used on day one?"

### [Frontline Insights → Product Improvements / Enablement] Maya AI supervisor enablement at NEP
**Source:** Report #123 — Actively AI — Agent Product Manager
**S (Situation):** Once Maya AI was live and handling 70-80% of first-touch volume, NEP supervisors didn't trust autonomous mode. They wanted to manually review every AI response. That was unsustainable at 200K+ residents.
**T (Task):** Build the enablement program + product surfaces that move supervisors from "review every conversation" to "trust autonomy, intervene on exceptions."
**A (Action):** Three weekly cycles of co-design with frontline supervisors: (a) shipped real-time conversation feed with sentiment scoring + agent-confidence indicator + one-click takeover button; (b) wrote the operator runbook ("when to take over, when to let it run, how to escalate"); (c) shipped the audit log so supervisors could review yesterday's autonomous conversations and surface examples back to me to improve the agent. The runbook is now part of NEP's onboarding for new supervisors.
**R (Result):** Supervisors moved from 100% manual review to ~15% intervention rate over 4 weeks. Audit-log examples drove 12 prompt-engineering improvements I couldn't have specced from scratch.
**Reflection:** The frontline-feedback → product-improvement loop is the multiplier. The runbook didn't just enable supervisors — it gave me a structured channel for the operator insights I needed to ship the next agent improvement. The enablement program IS the optimization pipeline; you don't ship one and then build the other.
**Best for questions about:** "Tell me about an enablement program you built," "How do you translate frontline insights into product?", "Describe how you build trust with non-technical users," "How do you scale an AI product after launch?"

### [Cross-Functional Delivery / Building From Scratch] ESC sole-AI cross-functional ship
**Source:** Report #123 — Actively AI — Agent Product Manager
**S (Situation):** ESC Partners was non-AI before me. No AI eng team, no MLOps, no playbook for utility-vertical AI. NEP was the first paying customer for AI.
**T (Task):** Ship Maya AI to a paying client in <3 months as the single AI person, partnering with NEP supervisors, ESC backend, AWS infra, and Microsoft Teams admins.
**A (Action):** Wrote architecture doc on day 4 (Bedrock model routing, FastAPI handlers, n8n workflow shape, Teams adaptive-card spec). Ran weekly NEP supervisor design sessions for the cockpit. Aligned ESC backend on FastAPI handlers with explicit interface contracts so they could ship the integration layer without depending on me. Integrated Microsoft Teams approval cards via webhooks — coordinated with NEP IT for tenant config. Spun off the email-triage agent in week 8.
**R (Result):** Live at NEP in 2.5 months across 4 stakeholder groups. Two follow-on customer rollouts (Moreno Valley + Delta Utilities) using the same pattern. ESC AI capability went from zero to a productized offering.
**Reflection:** Writing the architecture doc on day 4 was the unlock for cross-functional speed — every other team had a single source of truth for "what is Maya AI, what does it do, how does it integrate with you." The mistake I almost made was skipping the doc to "save time and move fast." At scale, the architecture doc per agent + customer is what unblocks the FDE team and the customer's RevOps team in parallel.
**Best for questions about:** "Tell me about working cross-functionally," "How do you build something from scratch in an ambiguous environment?", "Describe the most complex stakeholder coordination you've done," "Why are you the right person to own a forward-deployed seat?"

### [Architecture Pivot / Compliance-Driven Iteration] VaultIQ in-VPC pivot mid-build
**Source:** Report #123 — Actively AI — Agent Product Manager
**S (Situation):** Started building VaultIQ as a standard cloud AI product — financial-analyst document intelligence on Claude Opus + Postgres/pgvector. Two weeks in, the customer's compliance team flagged that the data couldn't leave their VPC.
**T (Task):** Pivot the architecture without losing the build velocity — re-deploy in-VPC on AWS Bedrock inside the customer's AWS account, with Terraform-managed reproducibility for future customers.
**A (Action):** Spent two days with the customer's security team mapping the constraints (VPC peering, IAM policies, data residency). Re-architected to AWS Bedrock in-VPC with Claude Opus + Postgres + pgvector all inside the customer's AWS perimeter. Wrote Terraform modules so the next customer's deployment is one `terraform apply` away, not a 4-week custom build. SSO + role-based access from day one.
**R (Result):** Compliance-grade AI product live for the first regulated-finance customer. The Terraform pattern is now reusable for future customers — onboarding time drops from "weeks" to "hours."
**Reflection:** The frontline insight (the security team's VPC requirement) was the one that would have killed the project if surfaced 6 weeks later. Sitting with their team early caught it. Same lesson for any forward-deployed AI seat: the customer's RevOps/security/IT team will surface compliance/integration constraints that the AE didn't think to mention; the Forward Deployed PM has to be in the room to catch them before they're sunk cost.
**Best for questions about:** "Tell me about a time a customer pushed back on your design," "How do you handle compliance and security requirements?", "Describe a mid-build pivot," "Tell me about turning a setback into a reusable pattern," "How do you embed with technical/security stakeholders?"
