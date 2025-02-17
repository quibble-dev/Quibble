import { dev } from '$app/environment';
import client from '$lib/clients/v1/client';
import { AuthSchema, ProfileCreateSchema } from '$lib/schemas/auth';
import type { PageServerLoad } from './$types';
import { fail, type Actions } from '@sveltejs/kit';
import { message, setError, superValidate, withFiles } from 'sveltekit-superforms';
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
  create: async ({ request, cookies }) => {
    const form = await superValidate(request, zod(ProfileCreateSchema));

    if (!form.valid) {
      return fail(400, withFiles({ form }));
    }

    const { data, error, response } = await client.POST('/u/me/profiles/', {
      headers: {
        Authorization: `Bearer ${cookies.get('auth_token')}`
      },
      // @ts-expect-error: only requires username for POST req
      body: { ...form.data },
      bodySerializer(body) {
        const fd = new FormData();
        Object.entries(body).forEach(([key, value]) => {
          if (value instanceof File || typeof value === 'string') {
            fd.set(key, value);
          } else if (typeof value === 'boolean') {
            fd.set(key, String(value));
          } else if (value !== undefined && value !== null) {
            fd.set(key, JSON.stringify(value));
          }
        });
        return fd;
      }
    });

    if (response.ok && data) {
      return withFiles({ form, profile: data });
    } else if (error) {
      return setError(form, 'username', String(error.errors[0]?.detail));
    }

    // https://superforms.rocks/concepts/files#returning-files-in-form-actions
    return withFiles({ form });
  }
};
