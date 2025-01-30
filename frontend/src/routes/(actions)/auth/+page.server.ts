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

    const {
      data: api_data,
      error: api_error,
      response: api_response
    } = await client.POST('/api/v1/auth/login/', {
      body: { ...form.data }
    });

    if (api_response.ok && api_data) {
      cookies.set('auth_token', api_data.token, {
        httpOnly: true,
        secure: !dev,
        path: '/',
        sameSite: 'lax',
        maxAge: 60 * 60 * 24 * 30 // 30 days
      });

      return { form, token: api_data.token };
    } else if (api_error) {
      return message(form, api_error.errors[0]?.detail, { status: 401 });
    }
  },
  register: async ({ request }) => {
    const form = await superValidate(request, zod(AuthSchema));

    if (!form.valid) {
      return fail(400, { form });
    }

    const {
      data: api_data,
      error: api_error,
      response: api_response
    } = await client.POST('/api/v1/auth/register/', {
      body: { ...form.data }
    });

    if (api_response.ok && api_data) {
      return { form };
    } else if (api_error) {
      return message(form, api_error.errors[0]?.detail, { status: 401 });
    }
  }
} satisfies Actions;
