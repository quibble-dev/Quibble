import { z } from 'zod';

export const PostSubmitSchema = z.object({
  community: z.number().min(1, 'This field is required.'),
  title: z.string().min(1).max(300),
  content: z.string()
});
