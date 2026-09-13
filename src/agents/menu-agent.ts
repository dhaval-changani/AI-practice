import { Agent } from "@openai/agents";

export const menuAgent = new Agent({
  name: "Menu Agent",
  instructions: "You are a NOQ agent which helps in creating menus.",
  model: "gpt-6-luna",
});
