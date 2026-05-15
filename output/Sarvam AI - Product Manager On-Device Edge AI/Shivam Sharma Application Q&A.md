# Application Q&A: Sarvam AI Product Manager On-Device and Edge AI

*Pre-filled answers for the Sarvam On-Device application form and likely screen-1 questions. Same human-tone rules as the resume: no em-dashes, no AI tells, plain English, concrete examples. Update as the conversation evolves.*

## Why Sarvam AI and why the on-device line?

Sovereign Indian AI is the most important infrastructure bet on the subcontinent for the next decade. On-device sovereign AI is where Sarvam's biggest moat sits: Sarvam Kaze wearable glasses, silicon partnerships with Qualcomm + Intel + NVIDIA, and an enterprise customer base (Tata Capital, SBI Life, CRED, IDFC, LIC) that needs data residency on Indian rails. Putting sovereign models on the customer's own silicon is what changes the economics for a billion users.

The enterprise on-device surface (multi-tenant, role-based access, MDM-integrated, audit-grade reliability) is where I have been shipping for the last five months at smaller scale on VaultIQ and Maya AI. The Sarvam seat lets me run that surface at platform scale with silicon-level optimization.

## Why this role?

Eight lines from the JD describe how I already work:

1. **Own roadmap for on-device inference, enterprise deployment, fleet management.** VaultIQ runs inside the customer VPC; Maya AI deploys phased across utilities (NEP, Moreno Valley, Delta).
2. **Define features for IT admin personas, enterprise auth, Microsoft ecosystem.** Maya AI integrates with Microsoft Teams and Outlook. SSO and OAuth2 are shipped on both VaultIQ and Maya AI.
3. **Drive B2B GTM alignment by translating customer pain points into product requirements.** Two weeks of NEP supervisor sit-throughs before Maya AI was scoped. Five-advisor observation at SALL before scoring was written.
4. **Run iterative experiments in enterprise deployments.** Shadow-channel A/B for every new Bedrock model. Takeover-frequency as the regression signal.
5. **Multi-tenant SaaS: tenant isolation, access controls, admin tooling.** Maya AI: DynamoDB tenant governance, role-based access, 17 admin APIs, 24-hour key rotation.
6. **HITL and agentic workflows with enterprise-grade reliability and auditability.** Supervisor cockpit with one-click human takeover. Every agent action logged with reasoning and operator override.
7. **Security and compliance: data residency, SSO/SAML/SCIM, regulatory.** VaultIQ runs inside the customer VPC with no data egress. SSO and OAuth2 shipped. SAML/SCIM is a one-week ramp from where I sit.
8. **Define and track metrics measuring enterprise engagement, retention, workflow depth.** Maya AI: per-tenant SLOs, intent-level reliability, supervisor takeover frequency.

## Tell me about a time you shipped on-device or air-gapped enterprise AI.

VaultIQ. ESC had a customer in financial intelligence who could not put analyst documents into a managed cloud LLM under any condition: regulatory, contractual, and competitive reasons all pointed at "the data must not leave the VPC."

I architected and shipped VaultIQ on Claude Opus running inside the customer VPC: Next.js front end, Postgres with pgvector for retrieval, Terraform for repeatable customer-perimeter deployment, SSO for identity, role-based access controls so analysts and senior leadership see different surfaces. The eval framework includes data-residency verification, role-correctness tests, and audit-log completeness.

VaultIQ is not strictly on-device (it runs inside a VPC, not on a laptop or a wearable), but the deployment perimeter, data-residency rigor, and customer-trust mechanics are the same. The transferable reflexes are exactly what enterprise on-device AI needs.

## Tell me about your enterprise authentication and Microsoft ecosystem experience.

Maya AI is deeply integrated with Microsoft Teams (adaptive cards for HITL approval) and Outlook (the email-triage agent). The supervisor cockpit uses SSO over OAuth2 for identity. Role-based access controls are enforced through DynamoDB tenant governance with per-tenant key rotation.

Where I am honest: I have not directly shipped Entra ID, Intune MDM, SAML, or SCIM as their own products. The transferable rigor is multi-tenant SaaS, OAuth2 SSO, role-based access, and Microsoft Teams + Outlook integration as production surfaces. SAML and SCIM follow naturally from the OAuth2 patterns I already ship. Entra ID and Intune are a first-30-days ramp at Sarvam, not a foundation gap.

## How do you think about HITL and agentic workflows for enterprise reliability?

- **Confidence has to be a first-class signal.** Maya AI returns a confidence score on every action. Below threshold, the agent does not act. It drafts and routes to a human reviewer.
- **Auditability lives in the data model, not the dashboard.** Every agent action logs the reasoning, the input context, and the operator override. Dashboards read from that, not the other way around.
- **Takeover-frequency is the regression signal.** If operators are overriding the agent more often after a model update, the model regressed. Shadow-channel for two weeks before full rollout.
- **HITL is a product, not a fallback.** The supervisor cockpit at Maya AI is a first-class surface, designed for non-technical operators to feel in control. UX matters more than backend correctness for adoption.

## How do you handle structured product experiments in enterprise deployments?

Phased rollout with explicit gates. Maya AI: NEP first (200K residents, deep deployment), then Moreno Valley Electrical, then Delta Utilities pilot. Each phase has an entry criterion (takeover frequency below 15%, confidence calibration within X bands, operator NPS above Y) and a kill criterion. New Bedrock models go through a two-week shadow channel against production traffic before any rollout. Cost-latency-accuracy tradeoffs are negotiated per intent (routine billing on Nova, complex outage triage on Sonnet, high-stakes escalations on Opus), not globally.

## Have you worked with IT admin and enterprise buyer personas?

Yes, across three engagements.

**NEP utility IT and operations:** daily working sessions with the supervisor team and IT operations on Oracle CCS integration, key rotation policy, and audit log retention. The IT admin persona is the one who gates whether Maya AI ships to additional residents.

**CloudApproach + Approachables enterprise sales (UK + MENA):** 200+ agency clients, 80+ real-estate partners. IT admin sign-off was the gating step for every contract. Built the muscle for translating IT concerns (data residency, audit logs, MDM policy) into product features.

**VaultIQ customer:** the IT admin team set the entire deployment perimeter. Multi-week working sessions on VPC topology, Terraform deployment, and role-based access scoping.

## What is your background, and how does it map to CS or EE preferred?

I have a Master of Science in AI in Business (STEM-certified) from Simon Business School and a Bachelor of Arts (Honors) in International Business and Management from the University of Central Lancashire. The CS / EE substance I ship comes from production work: VaultIQ deployment architecture, Maya AI multi-tenant SaaS, RAG on Postgres with pgvector, Bedrock routing, the Claude Code build loop. The non-CS degree is an honest framing reality. The shipped systems should answer the technical depth question more clearly than the diploma does.

## What is your biggest accomplishment?

**Career-wise:** Bootstrapping and selling CloudApproach + Approachables for $575K combined. Two ventures across UK and MENA. 200+ agency clients. 80+ real-estate partners. $5M+ in enterprise deals influenced. Two exits before I turned 25.

**Last six months:** VaultIQ shipped as the air-gapped Claude Opus atom inside the customer VPC. Maya AI live at NEP with 200K+ residents in 2.5 months. Both as the sole AI on staff at ESC.

## Why are you leaving your current role?

Scope and stage. ESC has been a great place to ship VaultIQ and Maya AI for one customer at a time, but my next role should put me inside a team where on-device sovereign AI becomes the product line at platform scale, with silicon-level optimization across phones, glasses, laptops, and vehicles. Sarvam is that team.

## Compensation expectations?

Open to the Sarvam range. Priority is total package plus equity at unicorn stage given the velocity. Happy to discuss INR or USD denomination depending on the relocation outcome.

## When can you start?

Immediately for remote. Two-week handoff at ESC for VaultIQ and Maya AI roadmaps. If Bengaluru on-site is required, I can be on the ground within 30 to 45 days of offer (visa logistics permitting).

## Work authorization and location?

I am Indian by nationality, currently US-based on STEM OPT through 2027, H-1B eligible. If Sarvam is hard-Bengaluru on-site for this seat, I would relocate to India for the right role. The on-device line works with silicon partners that include US-based companies (Qualcomm in San Diego, Intel in Santa Clara, NVIDIA in Santa Clara, Apple in Cupertino), so a remote-from-US window for the first 6 to 12 months might actually be a strategic fit. Happy to discuss either way.

## How did you hear about this role?

Found through the Sarvam careers page directly. The Sarvam Kaze glasses launch and the silicon-partnership announcements have been on my radar; the seat surfaced naturally.

## Anything else you want us to know?

Three proof links if you want to see the work:

- SALL live: https://ai-sales-assistant-frontend.onrender.com/
- SALL walkthrough: https://www.youtube.com/watch?v=eCkP7_ZI348
- Portfolio: https://shivamsportfolio.webflow.io/

Happy to walk through VaultIQ's air-gapped deployment architecture in code, or share a one-page enterprise rollout framework for how I would scope the next phase of Sarvam's on-device line.
