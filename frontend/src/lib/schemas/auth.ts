import { z } from 'zod';

export const JoinSchema = z.object({
  email: z.string().email(),
  password: z.string().min(8)
});

export const ProfileCreateSchema = z.object({
  username: z.string().min(3)
});
