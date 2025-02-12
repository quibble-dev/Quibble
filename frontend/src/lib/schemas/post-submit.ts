import { z } from 'zod';

export const PostSubmitSchema = z.object({
  title: z.string().min(1).max(300),
  content: z.string()
});
