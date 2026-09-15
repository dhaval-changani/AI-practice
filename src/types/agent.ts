import type { Agent, AgentOutputType, TextOutput } from "@openai/agents";

export interface AIAgent<T extends AgentOutputType = TextOutput> {
  getAgent: () => Agent<unknown, T>;
}
