import { dev } from '$app/environment';
import { fail } from '@sveltejs/kit';
import type { Actions } from './$types';
import client from '$lib/clients/client';

export const actions = {
  login: async ({ request, cookies }) => {
    const form_data = await request.formData();

    const { data, error, response } = await client.POST('/api/v1/u/auth/login/', {
      body: {
        email: form_data.get('email') as string,
        password: form_data.get('password') as string
      }
    });

    if (!response.ok && error) {
      return fail(response.status, error.errors[0]);
    } else if (data) {
      cookies.set('auth_token', data.token, {
        httpOnly: true,
        secure: !dev,
        path: '/',
        sameSite: 'lax'
      });

      return { token: data.token };
    }
  }
} satisfies Actions;
