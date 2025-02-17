import { z } from 'zod';

export const AuthSchema = z.object({
  email: z.string().email(),
  password: z.string().min(8)
});

export const ProfileCreateSchema = z.object({
  username: z.string().min(3),
  avatar: z
    .instanceof(File)
    .refine((f) => f.size < 5_000_000, 'Max 5 MB upload size.')
    .optional(),
  cover: z
    .instanceof(File)
    .refine((f) => f.size < 5_000_000, 'Max 5 MB upload size.')
    .optional()
});

export const ProfileNewSchema = z.object({
  username: z.string().min(3)
});
