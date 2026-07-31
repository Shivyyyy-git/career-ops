# Application Q&A: Morgan Stanley, AI Product Manager

Pre-filled answers for the Morgan Stanley application form and likely screen-one questions. Same tone rules as the resume: plain English, concrete examples, no em-dashes, nothing invented. Update freely as the conversation evolves.

---

## Why Morgan Stanley?

Morgan Stanley published one hard GenAI number that I keep coming back to. DevGen.AI processed roughly nine million lines of legacy code and saved about 280,000 developer hours. That is a numerator, and the interesting question is what those hours converted into. Saved time only becomes value when the capacity is deliberately redeployed, and across the industry most reported time savings never show up as a measurable outcome. Closing that gap is the difference between a reporting function and a vanity dashboard, and it is the part of this job I actually want.

The second reason is timing. Ninety-eight percent of Financial Advisor teams already use the AI @ Morgan Stanley Assistant, so the Firm is past the adoption-evangelism stage that most enterprises are still stuck in. The remaining questions are harder and more interesting: weekly actives against enabled seats, depth cohorts rather than headcount, how often an answer gets corrected or overridden, and what any of it is worth. Those are the questions I built for Maya AI, one product at a time. Doing it across a portfolio, at 80,000-person scale, is the version of the problem I want next.

The third reason is that nobody outside the Firm can tell you what good looks like yet. When SR 26-2 replaced SR 11-7 in April, it explicitly placed generative and agentic AI outside the scope of model risk guidance while leaving the general governance obligation fully intact. The definitions of adoption, quality, and control effectiveness for GenAI have to be built internally. That is a rare thing to get to work on.

---

## Why this role specifically?

The posting says it wants builders who love to build. Most people applying to a data and reporting PM req have consumed adoption dashboards. I have been on the producer side of the number. At ESC I decided what "first-touch autonomous containment" meant, chose the denominator, and then had to defend that choice to the operations managers being measured by it.

Measurement frameworks written by people who have never shipped an agent tend to measure seat counts. I know which numbers move because I picked them.

---

## Tell me about a time you turned data into a product decision.

Maya AI is the clearest one. Once the agent was live at NEP, nobody could answer a basic question: was it actually working? "The agent is handling emails" is not something an operations manager can act on.

So I built the supervisor cockpit. Every conversation carries a confidence score on the response, a sentiment reading, and a record of whether a human took over. Then I set three things as the reported measures of quality: autonomous containment, confidence distribution, and takeover frequency, tracked per intent and per channel rather than as one blended number.

The per-intent split is what changed decisions. Blended containment looked healthy. Broken out, one intent category had a takeover rate several times the others, which told us the problem was not the model, it was that a specific workflow needed a different approval threshold. We changed the threshold for that intent alone instead of degrading the whole system. That is the kind of read you only get if the instrumentation was designed with the decision in mind.

---

## What is your experience with dashboards and reporting platforms?

Honest answer first: I have not used Tableau or Power BI. If your team lives in a governed warehouse with published workbooks, that is a genuine ramp for me and I would rather say so now.

What I have done is build the reporting layer myself. The Maya AI supervisor cockpit is a React front end over a FastAPI service, with conversation state and history in DynamoDB, surfacing live sentiment, confidence scoring, agent performance, and one-click human takeover to non-technical utility operations managers. I defined the metrics, built the surface, and then had to defend the definitions to the people the numbers described. My SQL is application SQL against Postgres, not warehouse modeling with window functions.

The transferable part is not the tool. It is knowing that a metric nobody trusts is worse than no metric, and that the argument about the denominator is the real work.

---

## What do you know about measuring GenAI adoption in a regulated environment?

Four opinions I actually hold:

- **Seat counts are the vanity layer.** Enabled seats, then weekly actives against enabled seats, then depth cohorts, then task-level outcomes. Most programs stop at layer one and call it adoption.
- **Time saved is an input, not a result.** The number only becomes value if the freed capacity is deliberately redeployed, and that redeployment has to be tracked separately or the whole benefit case is unfalsifiable.
- **Quality signals have to be first class.** Confidence, override rate, correction rate, and human takeover frequency tell you where a system is weak. At ESC I tracked these per intent because blended numbers hide exactly the problems you need to find.
- **Governance telemetry serves two audiences at once.** The takeover rate in my cockpit told operations where the agent was weak and told supervisors where the controls were holding. A firmwide reporting layer has to produce both reads from the same data.

---

## Where are the gaps in your background for this role?

I would rather name these than have them found.

- **I have not worked inside a large, complex organization.** My largest context is one where I am the entire AI function. I have shipped into a regulated utility serving 200K residents across three tenant deployments with approval gates, which is the closest structural analogue I have, but it is not a matrixed firm with Internal Audit and a Technology COO org.
- **No Tableau or Power BI.** Covered above.
- **What I have is security and access governance, not data governance.** Tenant isolation, RBAC, SSO, and key rotation are not a data catalog, lineage, stewardship, or a data quality SLA. I have never been through an audit of a data asset.
- **Every AI metric I own is a metric for a product I built myself.** I have never run adoption reporting across a portfolio of use cases owned by other teams, and the politics of that are real.
- **My data science record is one project.** XGBoost with SHAP on the City of Rochester fraud detection engagement through Simon Vision Consulting, accuracy from 62% to 73%, built so loan officers could see why an application was flagged.

---

## Are the numbers on your resume measured or modeled?

Worth being precise, especially for this team.

- **70 to 80% first-touch containment:** measured, but on definitions I set. Happy to walk through the denominator.
- **Roughly $225K per month savings:** projected, not realized. It is a client-side model built from displaced handling time, and I would not present it as a booked benefit.
- **API cost reduction of roughly 70% at SALL:** measured, comparing per-consultation cost before and after the two-phase pre-filter.
- **62% to 73% accuracy lift:** measured on a held-out set.

---

## What AI tools do you use hands-on today?

- **Claude Code:** daily driver. Maya AI's cockpit, the email-triage agent, the React console, and the FastAPI handlers all started as Claude Code sessions.
- **AWS Bedrock:** production routing across Claude Opus, Sonnet, and Nova, chosen per intent on cost and latency rather than one model everywhere.
- **n8n:** orchestration for the approval and triage workflows.
- **Python:** FastAPI services, plus XGBoost and SHAP on the fraud detection work.
- **Claude, ChatGPT, and Perplexity** for research and thinking work; **Cursor** and **GitHub Copilot** inside long-lived codebases.

---

## What is your biggest accomplishment?

**Career:** bootstrapping and selling CloudApproach and Approachables for $575K combined across UK and MENA, with 95% client retention after acquisition.

**Recent:** Maya AI live at a 200K-resident utility in 2.5 months as the only AI person at the company. ESC had never shipped AI before. It has now, and there are two more utilities in rollout.

---

## Why are you leaving your current role?

Scope, and the kind of problem I want next. ESC has been a good place to build, but I am the entire AI function there, measuring products I built myself. I want to work on the version of this problem where the systems belong to other teams and the measurement has to be negotiated rather than declared. That is a harder job and I think it is the right one for me now.

---

## Compensation expectations?

The posted range is $120,000 to $165,000 and I am comfortable working inside it, anchored toward the top given the scope. One clarifying question I would ask early: what corporate title does this role carry, Associate, Vice President, or Executive Director? The posting says "Director Level," which I understand is a job-family label rather than a rung on the Analyst / Associate / VP / ED ladder, and the answer changes what the total package looks like.

---

## When can you start?

Two to four weeks. I would want to hand off the Maya AI roadmap and the supervisor cockpit properly rather than walk out mid-rollout.

---

## Are you authorized to work in the US? Will you require sponsorship?

I am authorized to work now on STEM OPT under my F-1. I will require H-1B sponsorship in the future and I am cap-subject, so the earliest lottery would be March 2027. I would rather confirm early that Morgan Stanley supports STEM OPT and cap-gap for this seat than find out at offer stage.

---

## Are you open to relocating to New York?

Yes. I am in Rochester now and would relocate to New York for this role. I would want the in-office expectation in writing, since public information about the Firm's policy is inconsistent, and I would want to understand whether relocation support exists at this band.

---

## How did you hear about this role?

Found through LinkedIn.

---

## Anything else you want us to know?

Three links if you want to see the work rather than read about it:

- SALL live: https://ai-sales-assistant-frontend.onrender.com/
- SALL walkthrough: https://www.youtube.com/watch?v=eCkP7_ZI348
- Portfolio: https://shivamsportfolio.webflow.io/

Happy to walk through the Maya AI cockpit and how the containment metric was defined, or to sketch a one-page GenAI measurement framework for a portfolio of internal use cases as a working session.
