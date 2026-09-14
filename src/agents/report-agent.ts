import { Agent, tool } from "@openai/agents";
import z from "zod";
import type { AIAgent } from "../types/agent.js";

export class ReportAgent implements AIAgent {
  constructor(private modelName: string) {}

  private orderReportTool = tool({
    name: "get_order_sales_data",
    description:
      "Fetches the orders sales data for specified start date and end date",
    parameters: z.object({
      startDate: z.iso.datetime(),
      endDate: z.iso.datetime(),
    }),
    async execute({ startDate, endDate }) {
      console.log(`Tool called with ${startDate}-${endDate} parameters`);
      return `Sales data for ${startDate} and ${endDate} is 100$.`;
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
