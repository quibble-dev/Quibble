import { z } from 'zod';

export const AuthSchema = z.object({
  email: z.string().email(),
  password: z.string().min(8)
});

export const ProfileCreateSchema = z.object({
  username: z.string().min(3),
  avatar: z.instanceof(File).optional(),
  cover: z.instanceof(File).optional()
});

export const ProfileNewSchema = z.object({
  username: z.string().min(3)
});
