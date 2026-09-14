import type { Agent } from "@openai/agents";

export interface AIAgent {
  getAgent(): Agent;
}
