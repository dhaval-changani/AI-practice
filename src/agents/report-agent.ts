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
      customerId: z.number().int().positive(),
    }),
    async execute({ startDate, endDate, customerId }) {
      if (customerId !== 1) {
        return `ERROR: The customerId ${customerId} does not exists, ask customer to verify!`;
      }
      return `Sales data for ${startDate} and ${endDate} for ${customerId} is 100$.`;
    },
  });

  getAgent() {
    return new Agent({
      name: "Report Agent",
      instructions: `You are agent which helps in sales reporting queries. Today's date is ${new Date().toISOString()}`,
      handoffDescription:
        "Use this agent when task is related to reporting or sales data",
      model: this.modelName,
      tools: [this.orderReportTool],
    });
  }
}
