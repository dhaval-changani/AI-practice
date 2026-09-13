import process from "node:process";

import { ReportAgent } from "./agents/report-agent.js";
import { validateEnv } from "./utils/validate-env.js";
import { Orcestrator } from "./orcstrator/index.js";

const env = validateEnv(process.env);

const reportAgent = new ReportAgent(env.model_name).getAgent();

const orc = new Orcestrator([reportAgent]);

orc.runLoop("What is the sales data for 14-sep");
