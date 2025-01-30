import { dev } from '$app/environment';
import client from '$lib/clients';
import { AuthSchema } from '$lib/schemas/auth';
import type { Actions } from './$types';
import { fail } from '@sveltejs/kit';
import { superValidate, message } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';

export const actions = {
  login: async ({ request, cookies }) => {
    const form = await superValidate(request, zod(AuthSchema));

    if (!form.valid) {
      return fail(400, { form });
    }

    const { data, error, response } = await client.POST('/api/v1/auth/login/', {
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
  register: async ({ request }) => {
    const form = await superValidate(request, zod(AuthSchema));

    if (!form.valid) {
      return fail(400, { form });
    }

    const { data, error, response } = await client.POST('/api/v1/auth/register/', {
      body: { ...form.data }
    });

    if (response.ok && data) {
      return { form };
    } else if (error) {
      return message(form, error.errors[0]?.detail, { status: 401 });
    }
  }
} satisfies Actions;
