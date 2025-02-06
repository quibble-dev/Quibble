import { z } from 'zod';

// schemas
export const IntroductionSchema = z.object({
  name: z
    .string()
    .min(3)
    .regex(/^[a-zA-Z0-9_]+$/, { message: 'Only letters, numbers, and underscores are allowed' }),
  description: z.string().min(1),
  avatar: z
    .instanceof(File)
    .refine((f) => f.size < 100_000, 'Max 100 kB upload size.')
    .optional(),
  banner: z
    .instanceof(File)
    .refine((f) => f.size < 100_000, 'Max 100 kB upload size.')
    .optional()
});
// infer types
export type IntroductionSchemaType = z.infer<typeof IntroductionSchema>;
