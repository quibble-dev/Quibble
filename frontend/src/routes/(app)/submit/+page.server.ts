import { PostSubmitSchema } from '$lib/schemas/post-submit';
import { fail, type Actions } from '@sveltejs/kit';
import { superValidate } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';

export const load = async () => {
  const form = await superValidate(zod(PostSubmitSchema));

  return { form };
};

export const actions: Actions = {
  default: async ({ request }) => {
    const form = await superValidate(request, zod(PostSubmitSchema));

    if (!form.valid) {
      return fail(400, { form });
    }

    return { form };
  }
};
