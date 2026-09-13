import { run, type Agent } from "@openai/agents";

export class Orcestrator {
  constructor(private agents: Agent[]) {}

  async runLoop(query: string) {
    const agent = this.agents[0];
    if (agent) {
      const result = await run(agent, query);
      console.log(result.finalOutput);
    }
  }
}
