import { Agent } from "@openai/agents";

export const reportAgent = new Agent({
  name: "Report Agent",
  instructions: "You are a NOQ agent which helps in reprting queries.",
  model: "gpt-6-luna",
});
