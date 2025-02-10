import client from '$lib/clients/v1/client';
import { json, type RequestHandler } from '@sveltejs/kit';

export const PATCH: RequestHandler = async ({ params, request, cookies }) => {
  try {
    const { action } = await request.json();
    const { data, response, error } = await client.PATCH('/comments/{id}/reaction/', {
      headers: {
        Authorization: `Bearer ${cookies.get('auth_token')}`,
        'Profile-Id': cookies.get('auth_user_profile_id')
      },
      body: { action },
      params: {
        path: { id: Number(params.id) }
      }
    });

    if (data && response.ok) {
      return json({ success: data.success });
    }

    return json({ success: false, error: error?.errors[0]?.detail });
  } catch (err) {
    return json({ success: false, error: 'Internal server error' }, { status: 500 });
  }
};
