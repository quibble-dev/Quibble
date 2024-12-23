import { dev } from '$app/environment';
import client from '$lib/clients/client';
import type { Actions } from './$types';
import { fail } from '@sveltejs/kit';

export const actions = {
  create: async ({ request, cookies }) => {
    const form_data = await request.formData();

    const { data, error, response } = await client.POST('/api/v1/users/me/profiles/', {
      headers: {
        Authorization: `Bearer ${cookies.get('auth_token')}`
      },
      // @ts-expect-error: only requires username for POST req
      body: {
        username: String(form_data.get('username'))
      }
    });

    if (response.ok && data) {
      return data;
    } else if (error) {
      return fail(response.status, error.errors[0]);
    }
  },
  select: async ({ request, cookies }) => {
    const form_data = await request.formData();
    const profile_id = form_data.get('profile_id') as string;

    cookies.set('auth_user_profile_id', profile_id, {
      httpOnly: true,
      secure: !dev,
      path: '/',
      sameSite: 'lax'
    });

    return { success: true };
  }
} satisfies Actions;
