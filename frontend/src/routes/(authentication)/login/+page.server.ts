import { dev } from '$app/environment';
import client from '$lib/clients/v1/client';
import { AuthSchema, ProfileCreateSchema } from '$lib/schemas/auth';
import type { PageServerLoad } from './$types';
import { fail, type Actions } from '@sveltejs/kit';
import { message, superValidate } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';

export const load: PageServerLoad = async ({ url }) => {
  const initial_data = { email: url.searchParams.get('email') ?? '' };
  const form = await superValidate(initial_data, zod(AuthSchema), { errors: false });

  return { form };
};

export const actions: Actions = {
  login: async ({ request, cookies }) => {
    const form = await superValidate(request, zod(AuthSchema));

    if (!form.valid) {
      return fail(400, { form });
    }

    const { data, error, response } = await client.POST('/u/login/', {
      body: { ...form.data }
    });

    if (response.ok && data) {
      cookies.set('auth_token', data.token, {
        httpOnly: true,
        secure: !dev,
        path: '/',
        sameSite: 'lax',
        maxAge: 60 * 60 * 24 * 30 // 30 days
      });

      return { form, token: data.token };
    } else if (error) {
      return message(form, error.errors[0]?.detail, { status: 401 });
    }
  },
  create: async ({ request }) => {
    const form = await superValidate(request, zod(ProfileCreateSchema));

    if (!form.valid) {
      return fail(400, { form });
    }

    return { form };
  }
};
