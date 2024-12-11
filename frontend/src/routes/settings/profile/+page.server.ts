import { isAuthError } from '$lib/utils/errors';
import { fail } from '@sveltejs/kit';
import type { Actions } from './$types';
import { dev } from '$app/environment';
import client from '$lib/clients/client';

export const actions = {
  create: async ({ request, cookies }) => {
    const form_data = await request.formData();

    try {
      await client.POST('/api/v1/u/me/profiles/', {
        headers: {
          Authorization: `Bearer ${cookies.get('auth_token')}`
        },
        // @ts-expect-error: only requires username for POST req
        body: {
          username: form_data.get('username') as string
        }
      });

      return { success: true };
    } catch (err) {
      let message = 'Oops! something went wrong.';
      let code = 500;

      if (isAuthError(err)) {
        message = err.message;
        code = err.code;
      } else if (err instanceof Error) {
        message = err.message;
        code = 400;
      }
      return fail(code, { detail: message });
    }
  },
  select: async ({ request, cookies }) => {
    const form_data = await request.formData();

    cookies.set('auth_user_profile_id', form_data.get('profile_id') as string, {
      httpOnly: true,
      secure: !dev,
      path: '/',
      sameSite: 'lax'
    });

    return { success: true };
  }
} satisfies Actions;
