import { Agent, tool } from "@openai/agents";
import z from "zod";
import type { AIAgent } from "../types/agent.js";

export class CustomerAgent implements AIAgent {
  constructor(private modelName: string) {}

  private customerSchema = z
    .object({
      name: z.string().optional(),
      email: z.email().optional(),
    })
    .refine((data) => data.name || data.email, {
      message: "Name or email any one must be provided",
    });

  private returncustomerSchema = this.customerSchema.extend({
    customerId: z.number(),
  });

  private findCustmerTool = tool({
    name: "find_customer",
    description:
      "Takes in name or email of customer and fetches and returns customer data",
    parameters: z.object({ customer: this.customerSchema }),
    outputSchema: this.returncustomerSchema,
    async execute({ customer }) {
      console.log(`find_customer called`);
      console.log(`customer name: ${customer.name}`);
      console.log(`customer email: ${customer.email}`);
      return { ...customer, customerId: 1 };
    },
  });

  getAgent() {
    return new Agent({
      name: "Customer Agent",
      instructions: "You are a agent which helps with customer queries.",
      model: this.modelName,
      tools: [this.findCustmerTool],
    });
  }
}
