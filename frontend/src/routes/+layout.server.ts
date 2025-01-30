import { AuthSchema, ProfileNewSchema } from '$lib/schemas/auth';
import type { LayoutServerLoad } from './$types';
import { superValidate } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';

export const load: LayoutServerLoad = async ({ locals }) => {
  const form_auth_join = await superValidate(zod(AuthSchema));
  const form_auth_profile_new = await superValidate(zod(ProfileNewSchema));

  return {
    profile: locals.profile,
    // superforms
    form_auth_join,
    form_auth_profile_new
  };
};
