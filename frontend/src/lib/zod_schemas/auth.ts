import { zod_required_string } from '$lib/utils/zod';
import { z } from 'zod';

export const auth_schema = z.object({
  email: zod_required_string('Email').email({ message: 'Email is invalid' }),
  password: zod_required_string('Password')
});

export type AuthSchema = z.infer<typeof auth_schema>;
