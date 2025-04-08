import { z } from 'zod';

const BasePostSubmitSchema = z.object({
  community: z.coerce
    .number({ invalid_type_error: 'Please select a community.' })
    .min(1, 'Community must be selected.'),
  title: z
    .string({ required_error: 'Please fill out this field.' })
    .min(1, 'Title cannot be empty.')
    .max(300),
  type: z.enum(['TEXT', 'IMAGE'])
});

const TextPostSubmitSchema = BasePostSubmitSchema.extend({
  type: z.literal('TEXT'),
  content: z
    .string({ required_error: 'Please fill out this field.' })
    .min(1, 'Content cannot be empty.')
});

const ImagePostSubmitSchema = BasePostSubmitSchema.extend({
  type: z.literal('IMAGE'),
  cover: z
    .instanceof(File)
    .refine((f) => f.size < 5_000_000, 'Max 5 MB upload size.')
    .refine((f) => f.type.startsWith('image/'), 'Only image files are supported now.')
});

export const PostSubmitSchema = z.discriminatedUnion('type', [
  TextPostSubmitSchema,
  ImagePostSubmitSchema
]);
