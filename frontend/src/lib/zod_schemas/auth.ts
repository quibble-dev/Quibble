import { zod_required_string } from '$lib/utils/zod';
import { z } from 'zod';

export const auth_schema = z.object({
  email: zod_required_string({ field_name: 'Email' }).email({
    message: 'Email is invalid'
  }),
  password: zod_required_string({ field_name: 'Password' }).min(8, {
    message: 'Password must contain atleast 8 chararcters'
  })
});

export type AuthSchema = z.infer<typeof auth_schema>;
