import z from "zod";

process.loadEnvFile();

export const validateEnv = (
  env: NodeJS.ProcessEnv,
): { api_key: string; model_name: string } => {
  const validVars = z
    .object({
      api_key: z.string(),
      model_name: z.string(),
    })
    .parse({
      api_key: env.OPENAI_API_KEY,
      model_name: env.OPENAI_MODEL,
    });
  return validVars;
};
