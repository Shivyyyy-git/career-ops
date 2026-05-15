# Application Q&A: Sarvam AI Product Manager Chanakya

*Pre-filled answers for the Sarvam Chanakya application form and likely screen-1 questions. Same human-tone rules as the resume: no em-dashes, no AI tells, plain English, concrete examples. Update as the conversation evolves.*

## Why Sarvam AI and why Chanakya?

Sovereign Indian AI is the most important infrastructure bet on the subcontinent for the next decade. Chanakya is the layer where that bet gets shipped into the customers who need it most: defence, government, regulated enterprise. Replicable, deployable atoms built on top of Sarvam-105B and the Sarvam stack means each customer engagement compounds the platform instead of forking it. That is the engineering and product discipline I want to be inside.

The atom list is also exactly the surface area I have already been building at smaller scale: VaultIQ (air-gapped Claude Opus inside the VPC), Maya AI (multi-tenant agent), Conference Outreach (3-workflow agentic atom). Going from "we built this for one customer" to "we ship this as a deployable atom across many" is the scaling I want next.

## Why this role?

Seven lines from the JD describe how I already work:

1. **Own the atom library roadmap.** Maya AI roadmap at ESC: I run the quarterly atom list across utility deployments. I decide what gets built, what gets cut, and what gets generalised into reusable infrastructure.
2. **Translate field learnings into precise product requirements.** Two weeks of NEP supervisor sit-throughs became the Maya AI PRD. Five-advisor consultation observation at SALL became the 8-factor scoring spec.
3. **Structured discovery with defence and enterprise clients.** Defence is a gap. Enterprise discovery (utility supervisors, senior-care advisors, agency owners across UK + MENA, ESC's enterprise customers) is the muscle I have.
4. **Prioritize ruthlessly and define what gets cut.** Three feature requests cut from the Maya backlog this quarter with written decision logs. Done is finished, not "documented as nice-to-have."
5. **Define and track product metrics across atom deployments.** Maya AI: confidence + sentiment + takeover frequency as SLOs. VaultIQ: query latency + data-residency audit + role-based access correctness. SALL: time-to-recommendation + advisor override rate.
6. **Write PRDs, specs, decision logs.** Engineers at ESC describe my specs as "clear and free of assumptions."
7. **Coordinate sprints and stakeholder communication.** Daily across ESC engineering, NEP operations, Moreno Valley Electrical, Delta Utilities. Weekly check-in with CRO.

## Tell me about a time you shipped an air-gapped or on-premises product.

VaultIQ. ESC had a customer in financial intelligence who could not put analyst documents into a managed cloud LLM under any condition: regulatory, contractual, and competitive reasons all pointed at "the data must not leave the VPC."

I architected and shipped VaultIQ on Claude Opus running inside the customer VPC: Next.js front end, Postgres with pgvector for retrieval, Terraform for repeatable deployment, SSO for identity, role-based access controls so analysts and senior leadership see different surfaces. Same Claude Code build pattern as Maya AI; the difference is the deployment perimeter. Audit logs, data-residency verification, and role-correctness tests are all part of the eval framework.

VaultIQ is the closest analog I can offer to Chanakya's defence and on-premises bonus criteria. It is not classified work. The rigor is real.

## Tell me about a time you said no to a client request with reasoning.

One example from this quarter at ESC. NEP wanted Maya AI to push outage updates into the residents' MyAccount portal as a separate write-back, bypassing the existing Oracle CCS event bus. The ask was framed as a quick win. I declined in a written decision log: the parallel write-back would have split the Oracle CCS source-of-truth, broken the confidence-tracking funnel for that intent, and locked us into a second integration surface to maintain. The decision log laid out three alternatives (delay until the Oracle CCS event-bus webhook ships, use the existing supervisor cockpit, or build a one-way mirror with explicit invalidation). NEP went with option three. The eval framework stayed clean.

Saying no to a customer with reasoning, especially a happy one, is the discipline that keeps the atom library coherent over time. I have to do it weekly.

## How do you think about RAG, agents, embeddings, and evaluation?

- **RAG is a retrieval problem before it is a generation problem.** VaultIQ retrieval is on Postgres with pgvector; the eval framework measures recall at k before any LLM is invoked. Most failures are retrieval, not synthesis.
- **Agents need confidence calibration.** Maya AI returns a confidence score on every action. Below threshold, the agent defers to a supervisor. Thresholds tuned per intent.
- **Embeddings need domain audits.** An off-the-shelf model trained on web English fails on utility billing terminology and Indic code-switching. The eval suite has to include domain-specific test sets.
- **Evaluation is a product surface, not a back-office.** SLOs sit in the cockpit. Operators see takeover frequency, confidence distributions, and per-intent reliability the same way an SRE sees error rates.

## Have you been forward-deployed alongside a domain expert?

Yes, three times.

**NEP utility supervisors:** two weeks of sit-throughs before any Maya AI spec was written. Mapped the supervisor workflow, the resident touch-points, and the failure modes that drive overflow into supervisor escalation.

**SALL senior-care advisors:** Five advisors observed across two weeks of consultation calls. The 8-factor scoring algorithm is a literal translation of their intuition into a structured pre-filter.

**Agency owners across UK + MENA:** 4.5 years of forward-deployed work at CloudApproach + Approachables. Two hundred clients. The product roadmap was the client roadmap.

## SQL and analytics fluency?

Daily. Maya AI's DynamoDB telemetry through Athena for funnel analysis. Postgres with pgvector for VaultIQ. SALL's two-phase pre-filter is a SQL-style structured join over advisor history. Analytics tools: built the Maya AI cockpit dashboards from scratch on instrumented telemetry. PostHog / Mixpanel adoption is a one-day pickup; the reflex is what matters.

## How do you handle accountability when a deployment goes wrong?

The owner writes the postmortem. Maya AI has had two production incidents in five months: one where Bedrock's Sonnet rolled out a regression on Tamil code-switching (caught on the shadow channel before the rollout), and one where the supervisor cockpit's takeover button was hidden behind a CSS regression for 90 minutes. Both went into a written postmortem with reproduction steps, root cause, the SLO impact, and the design change. The CRO read both. The team did the same exercise.

## What is your biggest accomplishment?

**Career-wise:** Bootstrapping and selling CloudApproach + Approachables for $575K combined. Two ventures across UK and MENA. 200+ agency clients. 80+ real-estate partners. $5M+ in enterprise deals influenced. Two exits before I turned 25.

**Last six months:** Maya AI live at NEP with 200K+ residents in 2.5 months. VaultIQ shipped as the air-gapped Claude Opus atom inside the customer VPC. Both as the sole AI on staff at ESC.

## Defence, government, or national-security experience?

Honest answer: none directly. What I do have is high-stakes regulated-adjacent work (City of Rochester fraud detection, NEP critical-utility deployment, VaultIQ air-gapped financial intelligence), the discipline that comes from shipping under those constraints, and the willingness to ramp on procurement cycles and clearance processes. The bonus criterion, not the gating one.

## Why are you leaving your current role?

Scope and stage. ESC has been a great place to ship Maya AI and VaultIQ as one-customer atoms, but my next role should put me inside a team where those atoms become the product line at platform scale. Chanakya is that team.

## Compensation expectations?

Open to the Sarvam range. Priority is total package plus equity at unicorn stage given the velocity. Happy to discuss INR or USD denomination depending on the relocation outcome.

## When can you start?

Immediately for remote. Two-week handoff at ESC for Maya AI and VaultIQ roadmaps. If Bengaluru on-site is required, I can be on the ground within 30 to 45 days of offer (visa logistics permitting).

## Work authorization and location?

I am Indian by nationality, currently US-based on STEM OPT through 2027, H-1B eligible. If Sarvam is hard-Bengaluru on-site, I would relocate to India for the right role. If there is any remote-from-US flexibility for the first 6 to 12 months while the seat ramps, I would love to discuss. Defence-sector roles often have residency constraints; happy to align early on what is feasible.

## How did you hear about this role?

Found through the Sarvam careers page directly. Chanakya's atom thesis is exactly the architectural pattern I have been building at ESC; the seat surfaced naturally.

## Anything else you want us to know?

Three proof links if you want to see the work:

- SALL live: https://ai-sales-assistant-frontend.onrender.com/
- SALL walkthrough: https://www.youtube.com/watch?v=eCkP7_ZI348
- Portfolio: https://shivamsportfolio.webflow.io/

Happy to walk through VaultIQ's air-gapped deployment architecture in code, or share a one-page atom-library template for how I would scope the next Chanakya component.
