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

`npm run typecheck` currently **passes**.

No test runner is configured — `npm test` is still the stub that exits 1. If tests are added, wire up a real runner before relying on it.

## Architecture

A POC on top of the **OpenAI Agents SDK** (`@openai/agents`), ESM + TypeScript, executed directly with `tsx` (no build step needed for development).

- `src/index.ts` — entrypoint. Calls `validateEnv(process.env)`, constructs `ReportAgent` with the
  validated model name, wraps the resulting `Agent` in `Orcestrator`, and calls `runLoop()` with a
  hardcoded query string.
- `src/orcstrator/index.ts` — the `Orcestrator` class. Takes an `Agent[]`, but `runLoop()` currently
  runs only `agents[0]` via `run()` and logs `finalOutput`; the remaining agents are ignored. Note
  the two spellings: directory `orcstrator/`, class `Orcestrator` — grep for both.
- `src/agents/*.ts` — one agent per file. Each file exports a **class** (`ReportAgent`,
  `MenuAgent`, `CustomerAgent`) that implements `AIAgent`, takes `modelName` as a constructor
  argument, holds its tools as private fields built with `tool()` and zod v4 `parameters`, and
  exposes `getAgent()` returning a constructed `Agent`.
- `src/agents/index.ts` — barrel re-exporting every agent class; new agents should be added here.
- `src/types/agent.ts` — the `AIAgent` interface (`getAgent(): Agent`), the shared shape all agent
  classes implement.
- `src/utils/validate-env.ts` — calls `process.loadEnvFile()` as a **module-level side effect at
  import time**; nothing else loads `.env`. Exports `validateEnv`, which parses `NodeJS.ProcessEnv`
  through a zod schema remapping `OPENAI_API_KEY` / `OPENAI_MODEL` onto `api_key` / `model_name`
  and throws when either is missing.

Orchestration status: three agents exist, each with at least one real tool. There are no
`handoffs`, no `outputType`, no guardrails, no `RunContext`, no tracing config and no streaming
anywhere yet.

## Known rough edges

Observations only — under Learning Mode these are mine to fix.

- `MenuAgent` and `CustomerAgent` are never instantiated — `src/index.ts` wires up only
  `ReportAgent`, so those two have never been through a real run.
- `Orcestrator.runLoop()` accepts an array but uses only the first element; the constructor
  signature promises orchestration the body does not do yet.
- `validateEnv` returns `api_key`, but nothing consumes it — the SDK reads `OPENAI_API_KEY` from
  `process.env` itself. The validation is fail-fast only.
- `ReportAgent`'s `get_order_sales_data` takes full ISO datetimes (`z.iso.datetime()`); the current
  date is injected into the agent instructions so the model has a reference point to resolve
  relative dates against.
- `nodemon` is a dependency but unused — the scripts use `tsx watch`.
- `dist/` is stale, holding four files from an older build (including a `menu-agent.js` that no
  longer matches the current source layout).

## LEARNING.md

`LEARNING.md` is the companion primer on multi-agent orchestration, and section 7 sets the build
order for this repo: (1) give one agent a real tool, (2) chain two agents in plain code, (3) add a
triage agent using `handoffs`, (4) convert to agents-as-tools with structured outputs. Progress:
step 1 done, step 2 in progress. Read it before suggesting any architectural direction.

## Conventions

- `verbatimModuleSyntax` + `nodenext` module resolution: relative imports **must** carry the `.js` extension (e.g. `./agents/index.js`), and type-only imports must use `import type`.
- Strict mode is on, including `noUncheckedIndexedAccess` and `exactOptionalPropertyTypes` — indexed access yields `T | undefined`, and optional properties cannot be assigned `undefined` explicitly.

## Environment

`.env` at the repo root holds `OPENAI_API_KEY` and `OPENAI_MODEL`, loaded by the import side effect
in `src/utils/validate-env.ts` (Node's built-in loader, not dotenv). `.gitignore` covers `.env`,
`dist/` and `node_modules/`.
