import { dev } from '$app/environment';
import client from '$lib/clients/v1/client';
import { profile_create_schema } from '$lib/zod_schemas/auth';
import type { Actions } from './$types';
import { fail } from '@sveltejs/kit';

export const actions = {
  create: async ({ request, cookies }) => {
    const form_data = await request.formData();

    const {
      data: parse_data,
      error: parse_error,
      success: parse_success
    } = profile_create_schema.safeParse({
      username: form_data.get('username') ?? ''
    });

    if (!parse_success) {
      return fail(400, { errors: parse_error.errors });
    }

    const {
      data: api_data,
      error: api_error,
      response: api_response
    } = await client.POST('/api/v1/users/me/profiles/', {
      headers: {
        Authorization: `Bearer ${cookies.get('auth_token')}`
      },
      // @ts-expect-error: only requires username for POST req
      body: { ...parse_data }
    });

    if (api_response.ok && api_data) {
      return api_data;
    } else if (api_error) {
      return fail(401, { error: api_error.errors[0]?.detail });
    }
  },
  select: async ({ request, cookies }) => {
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
