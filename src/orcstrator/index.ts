import { Agent, run } from "@openai/agents";
import { ReportAgent } from "../agents/report-agent.js";
import type { validEnv } from "../utils/validate-env.js";
import { CustomerAgent } from "../agents/customer-agent.js";
import { MenuAgent } from "../agents/menu-agent.js";

export class Orcestrator {
  constructor(private env: validEnv) {}

  async runLoop(query: string) {
    const reportAgent = new ReportAgent(this.env.model_name).getAgent();
    const result = await run(reportAgent, query);
    console.log("Final Output:", result.finalOutput);
  }

  async runLoopChained(query: string) {
    try {
      const customerAgent = new CustomerAgent(this.env.model_name).getAgent();
      const customerResult = await run(customerAgent, query);
      console.log({ customerAgentOutput: customerResult.finalOutput });

      if (customerResult.finalOutput) {
        const customerId = customerResult.finalOutput.customerId;

        const reportQuery = `${query} and customerId:${customerId}`;
        console.log({ reportQuery });

        const reportAgent = new ReportAgent(this.env.model_name).getAgent();
        const reportResult = await run(reportAgent, reportQuery);
        console.log("Final Output:", reportResult.finalOutput);
      }

      console.log("Programm Exited");
    } catch (err) {
      console.log(err);
    }
  }

  async runTraige(query: string) {
    try {
      const customerAgent = new CustomerAgent(this.env.model_name).getAgent();
      const reportAgent = new ReportAgent(this.env.model_name).getAgent();
      const menuAgent = new MenuAgent(this.env.model_name).getAgent();
      const traigeAngent = new Agent({
        name: "Traige Agent",
        model: this.env.model_name,
        instructions:
          "Choose the correct agent based on the query received, route the primart intent and mention what is dropped",
        handoffs: [menuAgent, customerAgent, reportAgent],
      });
      const result = await run(traigeAngent, query);
      console.log("Final Output:", result.finalOutput);
    } catch (err) {
      console.log(err);
    }
  }
}
