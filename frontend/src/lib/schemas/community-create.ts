import type { SuperFormData } from 'sveltekit-superforms/client';
import { z } from 'zod';

export const CommunityCreateSchema = z.object({
  name: z.string().min(1),
  description: z.string().min(1),
  avatar: z
    .instanceof(File)
    .refine((f) => f.size < 5_000_000, 'Max 5 MB upload size.')
    .optional(),
  banner: z
    .instanceof(File)
    .refine((f) => f.size < 5_000_000, 'Max 5 MB upload size.')
    .optional(),
  topics: z.number().array().min(1),
  type: z.enum(['PRIVATE', 'RESTRICTED', 'PUBLIC']).default('PUBLIC'),
  nsfw: z.boolean().default(false)
});

export type CommunityCreateType = typeof CommunityCreateSchema;
export type CommunityCreateFormType = SuperFormData<z.infer<CommunityCreateType>>;
