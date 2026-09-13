# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
npm start        # run src/index.ts via tsx
npm run dev      # same, with watch/reload
npm run build    # tsc -> dist/
npm run typecheck # tsc --noEmit
```

No test runner is configured — `npm test` is still the stub that exits 1. If tests are added, wire up a real runner before relying on it.

## Architecture

A POC on top of the **OpenAI Agents SDK** (`@openai/agents`), ESM + TypeScript, executed directly with `tsx` (no build step needed for development).

- `src/index.ts` — entrypoint. Calls `process.loadEnvFile()` (Node's built-in `.env` loader, not dotenv) before importing/using agents, then drives an agent with `run(agent, prompt)`.
- `src/agents/*.ts` — one file per agent, each exporting a single `new Agent({ name, instructions, model })`. Current agents: `menuAgent` (menu creation), `hubspotAgent` (client queries), `reportAgent` (reporting).
- `src/agents/index.ts` — barrel re-exporting every agent; new agents should be added here.

The agents are currently independent — no handoffs, tools, or orchestration are wired up yet. `zod` is a dependency in anticipation of tool schemas but is unused so far.

## Conventions

- `verbatimModuleSyntax` + `nodenext` module resolution: relative imports **must** carry the `.js` extension (e.g. `./agents/index.js`), and type-only imports must use `import type`.
- Strict mode is on, including `noUncheckedIndexedAccess` and `exactOptionalPropertyTypes` — indexed access yields `T | undefined`, and optional properties cannot be assigned `undefined` explicitly.
- Top-level `await` is used in `src/index.ts` (ESM, `target: esnext`).

## Environment

`OPENAI_API_KEY` in `.env` at the repo root, loaded by `process.loadEnvFile()`. `.env`, `dist/`, and `node_modules/` are untracked and there is no `.gitignore` yet.
