import { Agent, tool } from "@openai/agents";
import z from "zod";
import type { AIAgent } from "../types/agent.js";

const CustomerSchema = z
  .object({
    name: z.string(),
  })
  .or(
    z.object({
      email: z.email(),
    }),
  );

const ReturnCustomerSchema = z.object({
  name: z.string(),
  email: z.string(),
  customerId: z.number(),
});

export class CustomerAgent implements AIAgent<typeof ReturnCustomerSchema> {
  constructor(private modelName: string) {}

  private findCustmerTool = tool({
    name: "find_customer",
    description:
      "Takes in name or email of customer and fetches and returns customer data",
    parameters: z.object({ customer: CustomerSchema }),
    outputSchema: ReturnCustomerSchema,
    async execute({ customer }) {
      return {
        name: "name" in customer ? customer.name : "",
        email: "email" in customer ? customer.email : "",
        customerId: 1,
      };
    },
  });

  getAgent() {
    return new Agent({
      name: "Customer Agent",
      instructions: "You are a agent which helps with customer queries.",
      handoffDescription:
        "Use this agent when task is about finding cusotmers.",
      model: this.modelName,
      tools: [this.findCustmerTool],
      outputType: ReturnCustomerSchema,
    });
  }
}
