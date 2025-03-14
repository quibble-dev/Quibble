import { z } from 'zod';

export const PostSubmitSchema = z.object({
  community: z.number().min(1, 'Please select a community.'),
  title: z.string().min(1, 'Title cannot be empty.').max(300, 'Title is too long.'),
  content: z.string()
});
