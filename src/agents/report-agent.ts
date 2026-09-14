import { Agent, tool } from "@openai/agents";
import z from "zod";
import type { AIAgent } from "../types/agent.js";

export class ReportAgent implements AIAgent {
  constructor(private modelName: string) {}

  private orderReportTool = tool({
    name: "get_order_sales_data",
    description:
      "Fetches the orders sales data for specified start date and end date for a cusotmer",
    parameters: z.object({
      startDate: z.iso.datetime(),
      endDate: z.iso.datetime(),
      customerId: z.number(),
    }),
    async execute({ startDate, endDate, customerId }) {
      console.log(
        `Tool called with ${startDate}-${endDate} for cusotmer ${customerId}`,
      );
      return `Sales data for ${startDate} and ${endDate} for ${customerId} is 100$.`;
    },
  });

  getAgent() {
    return new Agent({
      name: "Report Agent",
      instructions: `You are agent which helps in reporting queries. Today's date is ${new Date().toISOString()}`,
      model: this.modelName,
      tools: [this.orderReportTool],
    });
  }
}
