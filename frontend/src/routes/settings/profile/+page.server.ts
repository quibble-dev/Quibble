import { isAuthError } from '$lib/utils/errors';
import { apiFetch } from '$lib/utils/api';
import { fail } from '@sveltejs/kit';
import type { Actions } from './$types';
import { dev } from '$app/environment';

export const actions = {
  create: async ({ request, cookies }) => {
    const form_data = await request.formData();

    try {
      await apiFetch('v1/user/me/profiles/', {
        headers: {
          Authorization: `Bearer ${cookies.get('auth_token')}`
        },
        body: JSON.stringify({
          username: form_data.get('username')
        })
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
