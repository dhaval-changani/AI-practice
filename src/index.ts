import process from "node:process";

import { validateEnv } from "./utils/validate-env.js";
import { Orcestrator } from "./orcstrator/index.js";
import { retryPolicies } from "@openai/agents";

const env = validateEnv(process.env);

const orcestrator = new Orcestrator(env);

console.log(process.argv.slice(2));

const getqueryFromArgs = () => {
  return process.argv.slice(2).join(" ");
};

const query = getqueryFromArgs();

if (query) {
  orcestrator.runTraige(query);
}
