import { Agent, tool } from "@openai/agents";
import z from "zod";
import type { AIAgent } from "../types/agent.js";

export class MenuAgent implements AIAgent {
  constructor(private modelName: string) {}

  private itemSchema = z.object({
    name: z.string().min(2).max(50),
    description: z.string().min(2).max(200),
    price: z.number(),
  });

  private itemsSchema = z.array(this.itemSchema);

  private menuSchema = z.object({
    name: z.string().min(2).max(50),
    description: z.string().min(2).max(200),
    items: this.itemsSchema,
  });

  private createMenuTool = tool({
    name: "create_menu",
    description: "Takes in menu data and creates a menu",
    parameters: z.object({ menu: this.menuSchema }),
    async execute({ menu }) {
      console.log(`createMenuTool called`);
      console.log(`Menu name: ${menu.name}`);
      console.log(`Menu description: ${menu.description}`);
      menu.items.map((item) => {
        console.table(item);
      });
      return menu;
    },
  });

  private createItemTool = tool({
    name: "create_item",
    description: "Takes in item data and return items array to create menu",
    parameters: z.object({ items: this.itemsSchema }),
    async execute({ items }) {
      console.log(`createItemTool called`);
      items.map((item) => {
        console.table(item);
      });
      return items;
    },
  });

  getAgent() {
    return new Agent({
      name: "Menu Agent",
      instructions: "You are agent which helps in creating items and menus.",
      handoffDescription:
        "Use this agent when task is about creating items or menus",
      model: this.modelName,
      tools: [this.createMenuTool, this.createItemTool],
    });
  }
}
