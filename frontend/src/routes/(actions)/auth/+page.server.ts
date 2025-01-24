import { dev } from '$app/environment';
import client from '$lib/clients/v1/client';
import { auth_schema } from '$lib/zod_schemas/auth';
import type { Actions } from './$types';
import { fail } from '@sveltejs/kit';

export const actions = {
  login: async ({ request, cookies }) => {
    const form_data = await request.formData();

    const {
      data: parse_data,
      error: parse_error,
      success: parse_success
    } = auth_schema.safeParse({
      email: form_data.get('email') ?? '',
      password: form_data.get('password') ?? ''
    });

    if (!parse_success) {
      return fail(400, { errors: parse_error.errors });
    }

    const {
      data: api_data,
      error: api_error,
      response: api_response
    } = await client.POST('/api/v1/auth/login/', {
      body: { ...parse_data }
    });

    if (api_response.ok && api_data) {
      cookies.set('auth_token', api_data.token, {
        httpOnly: true,
        secure: !dev,
        path: '/',
        sameSite: 'lax',
        maxAge: 60 * 60 * 24 * 30 // 30 days
      });

      return { token: api_data.token };
    } else if (api_error) {
      return fail(401, { error: api_error.errors[0]?.detail });
    }
  },
  register: async ({ request }) => {
    const form_data = await request.formData();

    const { data, error, response } = await client.POST('/api/v1/auth/register/', {
      body: {
        email: String(form_data.get('email')),
        password: String(form_data.get('password'))
      }
    });

    if (response.ok && data) {
      return { success: true };
    } else if (error) {
      return fail(response.status, error.errors[0]);
    }
  }
} satisfies Actions;
