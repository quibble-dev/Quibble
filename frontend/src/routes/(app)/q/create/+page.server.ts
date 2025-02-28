import { CommunityCreateSchema } from '$lib/schemas/community-create';
import type { PageServerLoad } from './$types';
import { fail, type Actions } from '@sveltejs/kit';
import { superValidate, withFiles } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';

export const load: PageServerLoad = async () => {
  const form = await superValidate(zod(CommunityCreateSchema));

  return { form };
};

export const actions: Actions = {
  default: async ({ request }) => {
    const form = await superValidate(request, zod(CommunityCreateSchema));
    console.log(form);

    if (!form.valid) {
      console.log(form.errors);
      return fail(400, withFiles({ form }));
    }

    return withFiles({ form });
  }
};
