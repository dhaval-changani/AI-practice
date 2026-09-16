import process from "node:process";

import { validateEnv } from "./utils/validate-env.js";
import { Orcestrator } from "./orcstrator/index.js";
import { Console } from "node:console";

const env = validateEnv(process.env);

const orcestrator = new Orcestrator(env);

const getqueryFromArgs = () => {
  return process.argv.slice(2).join(" ");
};

const query = getqueryFromArgs();
if (query) {
  orcestrator.runTraige(query);
}

console.log("Process Ended");
