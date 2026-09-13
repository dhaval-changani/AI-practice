import { Agent } from "@openai/agents";

export const hubspotAgent = new Agent({
  name: "Hubspot Agent",
  instructions: "You are a NOQ agent which helps in with client queries.",
  model: "gpt-5.6-luna",
});
