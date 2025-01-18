import { z } from 'zod';

export const zod_required_string = (name: string) => {
  return z
    .string()
    .min(1, { message: `${name} is required` })
    .trim();
};
