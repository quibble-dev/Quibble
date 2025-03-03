import api from '$lib/api';
import { AuthSchema } from '$lib/schemas/auth';
import type { PageServerLoad } from './$types';
import { fail, redirect, type Actions } from '@sveltejs/kit';
import { message, superValidate } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';

export const load: PageServerLoad = async ({ url }) => {
  const initial_data = { email: url.searchParams.get('email') ?? '' };
  const form = await superValidate(initial_data, zod(AuthSchema), { errors: false });

  return { form };
};

export const actions: Actions = {
  default: async ({ request }) => {
    const form = await superValidate(request, zod(AuthSchema));

    if (!form.valid) {
      return fail(400, { form });
    }

    const { data, error, response } = await api.POST('/auth/registration/', {
      body: { ...form.data }
    });

    if (response.ok && data) {
      const params = new URLSearchParams();
      params.set('email', form.data.email);

      redirect(307, `/login?${params.toString()}`);
    } else if (error) {
      return message(form, error.errors[0]?.detail, { status: 401 });
    }
  }
};
