import { dev } from '$app/environment';
import client from '$lib/clients';
import { AuthSchema, ProfileNewSchema } from '$lib/schemas/auth';
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
  },
  profile_new: async ({ request, cookies }) => {
    const form = await superValidate(request, zod(ProfileNewSchema));

    if (!form.valid) {
      return fail(400, { form });
    }

    const form_data = await request.formData();

    const { data, error, response } = await client.POST('/api/v1/users/me/profiles/', {
      headers: {
        Authorization: `Bearer ${cookies.get('auth_token')}`
      },
      // @ts-expect-error: only requires username for POST req
      body: { username: form_data.get('username') }
    });

    if (response.ok && data) {
      return data;
    } else if (error) {
      return fail(401, { error: error.errors[0]?.detail });
    }
  },
  profile_select: async ({ request, cookies }) => {
    const form_data = await request.formData();
    const profile_id = String(form_data.get('profile_id'));

    cookies.set('auth_user_profile_id', profile_id, {
      httpOnly: true,
      secure: !dev,
      path: '/',
      sameSite: 'lax',
      maxAge: 60 * 60 * 24 * 30 // 30 days
    });

    return { success: true };
  }
} satisfies Actions;
