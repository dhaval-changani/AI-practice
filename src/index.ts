import process from "node:process";
import { run } from "@openai/agents";
import { menuAgent, reportAgent, hubspotAgent } from "./agents/index.js"

process.loadEnvFile();

const result = await run(menuAgent, "Who was the first president of the United States?");
console.log(result.finalOutput);
