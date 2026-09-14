import process from "node:process";

import { validateEnv } from "./utils/validate-env.js";
import { Orcestrator } from "./orcstrator/index.js";

const env = validateEnv(process.env);

const orc = new Orcestrator(env);

orc.runLoopChained("What is the sales data for 14-sep for Dhaval");
