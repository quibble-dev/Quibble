import { dev } from '$app/environment';
import client from '$lib/clients/v1/client';
import type { Actions } from './$types';
import { fail } from '@sveltejs/kit';

export const actions = {
  login: async ({ request, cookies }) => {
    const form_data = await request.formData();

    const { data, error, response } = await client.POST('/api/v1/auth/login/', {
      body: {
        email: String(form_data.get('email')),
        password: String(form_data.get('password'))
      }
    });

    if (response.ok && data) {
      cookies.set('auth_token', data.token, {
        httpOnly: true,
        secure: !dev,
        path: '/',
        sameSite: 'lax'
      });

      return { token: data.token };
    } else if (error) {
      return fail(response.status, error.errors[0]);
    }
  }
} satisfies Actions;
