import { Agent, tool } from "@openai/agents";
import z from "zod";

export class ReportAgent {
  constructor(private modelName: string) {}

  getTools() {
    const orderReportTool = tool({
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
    return [orderReportTool];
  }

  getAgent() {
    return new Agent({
      name: "Report Agent",
      instructions: "You are a NOQ agent which helps in reprting queries.",
      model: this.modelName,
      tools: this.getTools(),
    });
  }
}
