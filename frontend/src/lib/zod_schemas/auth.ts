import { z } from 'zod';

export const auth_schema = z.object({
  email: z.string().email(),
  password: z.string().min(8)
});

export type AuthSchema = z.infer<typeof auth_schema>;
export type AuthSchemaErrors = z.inferFlattenedErrors<typeof auth_schema>['fieldErrors'];

export const profile_create_schema = z.object({
  username: z.string().min(3)
});

export type ProfileCreateSchema = z.infer<typeof profile_create_schema>;
