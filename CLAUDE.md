# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Learning Mode (highest priority — overrides everything else)

This repo is a learning project. I write all the code myself.

- **Never write or modify code in this repo.** No edits to `src/**`, no new source files, no
  "here, I fixed it" patches — even when asked directly, even for a one-line change.
- **Never output code.** No snippets, no diffs, no pseudo-code that is really code, no type
  signatures or function bodies dressed up as examples. Plain prose only.
- When I ask for help, explain in plain text: what is wrong, why it happens, which concept it
  touches, and what direction to take. Name the file and line, the API, or the doc to read —
  then stop and let me implement it.
- Reviews and debugging: describe the defect and the reasoning. Do not supply the fix.
- Suggest solutions as *ideas*, not implementations. If several approaches exist, describe the
  tradeoffs and let me choose.
- Exception: files I explicitly ask you to edit that are not source code (e.g. this `CLAUDE.md`,
  config, notes). When in doubt, ask before writing anything.

## Commands

```bash
npm start        # run src/index.ts via tsx
npm run dev      # same, with watch/reload
npm run build    # tsc -> dist/
npm run typecheck # tsc --noEmit
```

`npm run typecheck` currently **fails** in `src/orcstrator/index.ts` — that file references a
`this.agents` property that was never assigned. This is the known starting state, not a regression.

No test runner is configured — `npm test` is still the stub that exits 1. If tests are added, wire up a real runner before relying on it.

## Architecture

A POC on top of the **OpenAI Agents SDK** (`@openai/agents`), ESM + TypeScript, executed directly with `tsx` (no build step needed for development).

- `src/index.ts` — entrypoint. Declares a local `Orcestrator` class that is a near-**copy** of the one
  in `src/orcstrator/index.ts`; its `runLoop()` ignores its own constructor arguments and hard-codes a
  `run(reportAgent, ...)` call. `src/index.ts` never imports `src/orcstrator/`.
- `src/orcstrator/index.ts` — untracked work-in-progress orchestrator skeleton. Does not compile and
  nothing imports it. Note the two spellings: directory `orcstrator/`, class `Orcestrator` — grep for
  both.
- `src/agents/*.ts` — one agent per file, each exporting a single `const <name>Agent`. Tools are
  defined module-private directly above the agent that uses them (see `orderReportTool` in
  `report-agent.ts`), with zod `parameters` on the zod v4 API.
- `src/agents/index.ts` — barrel re-exporting every agent; new agents should be added here.
- `src/utils/validate-env.ts` — untracked. Calls `process.loadEnvFile()` as a **module-level side
  effect at import time**; nothing else loads `.env`. Exports `validateEnv`, a zod schema that remaps
  `OPENAI_API_KEY` / `OPENAI_MODEL` onto `api_key` / `model_name` and throws when either is missing.

Orchestration status: one agent (`reportAgent`) has a real tool. There are no `handoffs`, no
`outputType`, no guardrails, no `RunContext`, no tracing config and no streaming anywhere yet.

## Known rough edges

Observations only — under Learning Mode these are mine to fix.

- `hubspotAgent` and `menuAgent` hardcode `model: "gpt-5.6-luna"`, which is not a real model id.
  `reportAgent` instead reads `String(process.env.OPENAI_MODEL)` at module scope.
- That model read is **import-order sensitive**: `src/index.ts` imports the agents barrel before
  `validate-env.ts`, so `loadEnvFile()` may not have run yet when `reportAgent` is constructed.
- `nodemon` is a dependency but unused — the scripts use `tsx watch`.
- `dist/` is stale, holding only two files from an older build.

## LEARNING.md

`LEARNING.md` is the companion primer on multi-agent orchestration, and section 7 sets the build
order for this repo: (1) give one agent a real tool, (2) chain two agents in plain code, (3) add a
triage agent using `handoffs`, (4) convert to agents-as-tools with structured outputs. Progress:
step 1 done, step 2 in progress. Read it before suggesting any architectural direction. Its
section 8 checklist is itself partly outdated — it cites model id `gpt-6-luna` and a missing
`.gitignore`.

## Conventions

- `verbatimModuleSyntax` + `nodenext` module resolution: relative imports **must** carry the `.js` extension (e.g. `./agents/index.js`), and type-only imports must use `import type`.
- Strict mode is on, including `noUncheckedIndexedAccess` and `exactOptionalPropertyTypes` — indexed access yields `T | undefined`, and optional properties cannot be assigned `undefined` explicitly.

## Environment

`.env` at the repo root holds `OPENAI_API_KEY` and `OPENAI_MODEL`, loaded by the import side effect
in `src/utils/validate-env.ts` (Node's built-in loader, not dotenv). `.gitignore` covers `.env`,
`dist/` and `node_modules/`.
