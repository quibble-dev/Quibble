import { dev } from '$app/environment';
import { fail } from '@sveltejs/kit';
import type { Actions } from './$types';
import { isAuthError } from '$lib/utils/errors';
import client from '$lib/clients/client';

export const actions = {
  login: async ({ request, cookies }) => {
    const form_data = await request.formData();

    try {
      const { data } = await client.POST('/api/v1/users/auth/login/', {
        body: {
          email: form_data.get('email') as string,
          password: form_data.get('password') as string
        }
      });

      if (data !== undefined) {
        cookies.set('auth_token', data.token, {
          httpOnly: true,
          secure: !dev,
          path: '/',
          sameSite: 'lax'
        });
      }

      return { token: data?.token };
    } catch (err) {
      let message = 'Oops! something went wrong.';
      let code = 500;

      if (isAuthError(err)) {
        message = err.message;
        code = err.code;
      } else {
        console.error(err);
      }
      return fail(code, { detail: message });
    }
  }
} satisfies Actions;
