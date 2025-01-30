import { JoinSchema, ProfileCreateSchema } from '$lib/schemas/auth';
import type { LayoutServerLoad } from './$types';
import { superValidate } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';

export const load: LayoutServerLoad = async ({ locals }) => {
  const form_join = await superValidate(zod(JoinSchema));
  const form_profile_create = await superValidate(zod(ProfileCreateSchema));

  return {
    profile: locals.profile,
    // superforms
    form_join,
    form_profile_create
  };
};
