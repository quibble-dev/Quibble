import { z } from 'zod';

export const LoginSchema = z.object({
  email: z.string().email(),
  password: z.string().min(8)
});

export const RegisterSchema = z
  .object({
    email: z.string().email(),
    password1: z.string().min(8),
    password2: z.string().min(8)
  })
  .refine((data) => data.password1 === data.password2, {
    message: `Passwords don't match`,
    path: ['password2']
  });

export const VerificationCodeSchema = z.object({
  code: z.string().min(1).max(6)
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
