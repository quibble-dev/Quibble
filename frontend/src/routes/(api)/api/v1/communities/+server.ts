import client from '$lib/clients/v1/client';
import { json, type RequestHandler } from '@sveltejs/kit';

export const POST: RequestHandler = async ({ cookies, request }) => {
  try {
    const form_data = await request.formData();

    const name = String(form_data.get('name'));
    const description = String(form_data.get('description'));
    const avatar = form_data.get('avatar') as File | null;
    const banner = form_data.get('banner') as File | null;
    const topics = form_data.get('topics');

    const type_raw = form_data.get('types');
    const type =
      type_raw && ['PUBLIC', 'RESTRICTED', 'PRIVATE'].includes(String(type_raw))
        ? (type_raw as 'PUBLIC' | 'RESTRICTED' | 'PRIVATE')
        : undefined;

    const nsfw_raw = form_data.get('nsfw');
    const nsfw = nsfw_raw ? nsfw_raw === 'true' : undefined;

    const { data, error, response } = await client.POST('/communities/', {
      headers: {
        Authorization: `Bearer ${cookies.get('auth_token')}`,
        'Profile-Id': cookies.get('auth_user_profile_id')
      },
      // @ts-expect-error: no 'id' for creation
      body: {
        name,
        description,
        ...(avatar && { avatar }),
        ...(banner && { banner }),
        topics,
        type,
        nsfw
      },
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

    if (data && response.ok) {
      return json({ success: true, data });
    } else if (error) {
      console.error(error);
      return json({ success: false, error: error.errors[0]?.detail });
    }

    return json({ success: false, error: 'Unexpected response from server' });
  } catch (err) {
    console.error('unexected error: ', err);
    return json({ success: false, error: 'Internal server error' }, { status: 500 });
  }
};
