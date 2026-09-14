# Multi-Agent Orchestration — From First Principles

A learning reference for this POC. Read top to bottom once; after that, section 6 is the
part worth re-reading.

---

## 1. The atom: an LLM call is stateless

```
(prompt) → model → (text)
```

That is the entire primitive. No memory, no actions, no loop. Everything else in this
document is scaffolding *you* write around that function.

## 2. Adding tools gives you an agent

An LLM cannot do anything — it can only emit tokens. So you strike a deal: "here are
functions you may call; if you want one, emit JSON describing the call."

```
you:   prompt + tool schemas
model: "call get_menu(restaurant_id=42)"
you:   *actually run it* → result
you:   prompt + tool schemas + call + result
model: "The menu is..."
```

The model never executes anything. **You** execute and feed the result back. An agent is
that loop:

```
while model wants a tool:
    run tool, append result, call model again
return final text
```

> **agent = LLM + tools + a loop + accumulated context**

`run()` from `@openai/agents` is exactly this loop. Every agent in `src/agents/` now carries at
least one `tool()`, so the loop can take a second pass: `get_order_sales_data` on `ReportAgent`,
`find_customer` on `CustomerAgent`, `create_menu` / `create_item` on `MenuAgent`.

## 3. Why more than one agent?

Everything an agent knows lives in one context window. As you pile tools and instructions
into a single agent, three things degrade:

| Failure | What it looks like |
|---|---|
| **Attention dilution** | 40 tools available, and tool-selection accuracy drops — the model picks the wrong one |
| **Instruction conflict** | "be terse for reports" and "be conversational for client queries" fight each other in one prompt |
| **Context pollution** | an 8k-token HubSpot API dump sits in context while the model tries to format a menu |

So: **multiple agents are a context-partitioning strategy.** Not "specialists are smarter" —
each agent simply gets a small, focused context holding only the tools and instructions
relevant to its slice.

Same reasoning as splitting a 2000-line function. Not because small functions are magic,
but because bounded scope is easier to get right.

## 4. Orchestration is the routing question

Once several agents exist, something must decide **who runs, when, and with what context**.
That decision *is* orchestration. Three patterns, ordered by how much control you hand to
the model.

### a) Deterministic chaining — you route, in code

```ts
const data   = await run(customerAgent, query);
const report = await run(reportAgent, data.finalOutput);
```

The sequence is known in advance; no model decides anything structural. Predictable,
testable, cheap. **Most "multi-agent" problems are really this**, and people reach past it
too early.

### b) Handoffs — the model routes

A triage agent receives the other agents *as handoff targets*. It reads the request and
transfers control:

```ts
const triage = new Agent({
  name: "Triage",
  instructions: "Route the user to the right specialist.",
  handoffs: [menuAgent, customerAgent, reportAgent],
});
```

Mechanically, a handoff is a tool call whose effect is "replace the active agent, keep the
conversation." Control **transfers** — triage is now out of the picture. Use it when the
branch depends on natural-language intent you cannot express in an `if`.

### c) Agents-as-tools — the model delegates and stays in charge

```ts
const orchestrator = new Agent({
  name: "Orchestrator",
  tools: [
    customerAgent.asTool({ toolName: "fetch_customer_data", /* ... */ }),
    reportAgent.asTool({ toolName: "write_report",           /* ... */ }),
  ],
});
```

The sub-agent runs in its **own** context; only its final output returns as a tool result.
Control comes back to the caller. This is the important one: a sub-agent can churn through
20k tokens of API responses while the orchestrator only ever sees the 200-token summary.

```
handoff:        orchestrator ──────► specialist        (goto — never returns)
agents-as-tool: orchestrator ──┬───► specialist
                               └───◄ summary only      (call — returns)
```

## 5. The two things that actually make this hard

**Context boundaries.** Every agent hop is a lossy compression step. The sub-agent
summarizes; whatever it drops is gone. If the orchestrator needed a detail that was
discarded, you get a confidently wrong answer and *no error*. Designing what crosses each
boundary matters more than prompt wording.

**Error propagation.** In normal code a failure throws. Here a sub-agent returns a
plausible-sounding string. The caller cannot distinguish "I found no client record" from
"I could not reach the API." Structured outputs — this is what the `zod` dependency is for —
let a sub-agent return a typed object with an explicit failure case, so the caller branches
on a value instead of parsing prose.

## 6. The honest guidance

Orchestration is not free: every hop adds latency, cost, and a lossy boundary.

> **A single agent with 6 well-named tools beats three agents with 2 each, almost every time.**

Escalate only on a real ceiling:

- tool count starts hurting selection accuracy (roughly 15–20+)
- instructions genuinely conflict
- one subtask produces so much intermediate context it crowds out everything else
- you want parallelism (three independent lookups at once)

---

## 7. Build order for this repo

Each step exists to make one concept *observable*. Resist skipping ahead — step 4 only
means something if you have felt steps 1–3.

**1. Give one agent a real tool.** — **done.**
`ReportAgent`, plus a `zod`-typed fake data fetcher (`get_order_sales_data`). `MenuAgent` and
`CustomerAgent` followed the same shape.
→ *verify:* the run loop visibly fires a tool call and feeds the result back in.

**2. Chain two agents in plain code.** — **in progress.**
`CustomerAgent` → `ReportAgent`, wired with `await`. This is where `Orcestrator.runLoop()` has to
stop ignoring everything past `agents[0]`. Settle the shape first: an ordered pipeline feeding each
`finalOutput` into the next agent, or one agent picked per query? Those are different programs, and
the answer decides whether step 3 is an upgrade or a rewrite.
→ *verify:* works end to end — and confirm for yourself that a model-router isn't needed yet.

**3. Add a triage agent using `handoffs`.**
→ *verify:* observe where natural-language routing picks the wrong specialist.

**4. Convert to agents-as-tools with structured outputs.**
→ *verify:* compare context sizes against step 3. That contrast is the payoff of the whole
exercise.

## 8. Open items

Resolved: the fake `"gpt-6-luna"` model id is gone (every agent takes `modelName` from the
validated env), the `.env` key parses cleanly, and `.gitignore` now covers `.env`, `dist/` and
`node_modules/`.

Still open:

- [ ] `MenuAgent` and `CustomerAgent` are constructed nowhere — neither has been through a real
      `run()`. Untested tool schemas are where the surprises live.
- [ ] `Orcestrator` takes an `Agent[]` but runs only `agents[0]`. Step 2 is blocked on this.
- [ ] `dist/` is stale and no longer matches the source layout.
