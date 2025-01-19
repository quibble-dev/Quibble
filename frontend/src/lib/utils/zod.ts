import { z } from 'zod';

export const zod_required_string = ({ field_name }: { field_name: string }) => {
  return z
    .string()
    .min(1, { message: `${field_name} is required` })
    .trim();
};
