import client from '$lib/clients/v1/client';
import { json, type RequestHandler } from '@sveltejs/kit';

export const POST: RequestHandler = async ({ cookies, request }) => {
  try {
    const form_data = await request.formData();

    const name = String(form_data.get('name'));
    const description = String(form_data.get('description'));
    const avatar = form_data.get('avatar') as File | null;
    const banner = form_data.get('banner') as File | null;

    const { data, error, response } = await client.POST('/communities/', {
      headers: {
        Authorization: `Bearer ${cookies.get('auth_token')}`,
        'Profile-Id': cookies.get('auth_user_profile_id')
      },
      // @ts-expect-error: no id required for creation
      // body: form_data,
      body: {
        name,
        description,
        ...(avatar && { avatar }),
        ...(banner && { banner })
      },
      bodySerializer(body) {
        const fd = new FormData();
        for (const name in body) {
          // @ts-expect-error: openapi-ts transform issue
          fd.set(name, body[name]);
        }
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
